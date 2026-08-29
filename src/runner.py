"""End-to-end experiment runner for the Casket pipeline.

Orchestrates the full thesis methodology with a complete audit trail:

  Phase 1  load + preprocess + profile every dataset
  Phase 2  primary 80/20 benchmark: 10 models x 4 datasets, 11 metrics + efficiency
  Phase 3  k-fold cross-validation (confidence intervals)
  Phase 4  cross-dataset transfer (concept-drift proxy)
  Phase 5  reporting: figures, literature comparison, summary.md

Run:
    python -m src.runner                 # full run
    python -m src.runner --quick         # fast smoke test (subsampled)
    python -m src.runner --no-cv --no-cross
    python -m src.runner --datasets D1,D3
"""
from __future__ import annotations

import argparse
import time

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.model_selection import StratifiedKFold, cross_validate

import config
from src import reporting
from src.audit import RunContext
from src.data_preprocessing import DatasetBundle, load_and_preprocess, load_xy
from src.data_profile import plot_distribution, profile_bundle
from src.evaluation import (evaluate_model, measure_inference, model_size_bytes,
                            predict_proba_safe)
from src.models.model_factory import get_models

QUICK_CAP = 1500          # rows per dataset in --quick mode
CV_MAX_N = 8000           # cap CV input size to bound runtime on large datasets
CROSS_MAX_N = 12000       # cap cross-dataset SOURCE training size (bounds SVM cost)


def _stratified_cap(X, y, cap: int, seed: int = config.SEED):
    """Return a stratified subsample of (X, y) of size <= cap."""
    if not cap or len(y) <= cap:
        return X, y
    rng = np.random.RandomState(seed)
    idx = []
    for c in np.unique(y):
        ci = np.where(y == c)[0]
        idx.extend(rng.choice(ci, max(1, int(round(cap * len(ci) / len(y)))),
                              replace=False))
    idx = np.array(idx)
    return (X.iloc[idx] if hasattr(X, "iloc") else X[idx]), y[idx]


# --------------------------------------------------------------------------- #
# Phase 2 — primary 80/20 benchmark                                           #
# --------------------------------------------------------------------------- #
def run_primary(ctx: RunContext, bundle: DatasetBundle, models: dict) -> list[dict]:
    import joblib

    rows = []
    roc_data = {}
    preds = {}

    # Persist the dataset's fitted scaler + label encoder once, so any saved
    # model can be reused for inference on new PE-header rows.
    models_dir = ctx.run_dir / "models" / bundle.key
    models_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(bundle.scaler, models_dir / "_scaler.joblib")
    joblib.dump(bundle.label_encoder, models_dir / "_label_encoder.joblib")

    for name, spec in models.items():
        model = clone(spec.estimator)
        ctx.log.info("  [%s] training %s ...", bundle.key, name)

        t0 = time.perf_counter()
        model.fit(bundle.X_train, bundle.y_train)
        train_time = time.perf_counter() - t0

        y_pred, infer_ms = measure_inference(model, bundle.X_test)
        y_prob = predict_proba_safe(model, bundle.X_test)
        size = model_size_bytes(model)

        # Save the fitted model to disk (results/runs/<id>/models/<dataset>/).
        model_path = models_dir / f"{name.replace(' ', '_')}.joblib"
        joblib.dump(model, model_path)

        metrics = evaluate_model(bundle.y_test, y_pred, y_prob, train_time)
        metrics.update({
            "Inference ms/sample": infer_ms,
            "Model Size (bytes)": size,
            "Model": name,
            "Family": spec.family,
            "Dataset": bundle.key,
        })
        rows.append(metrics)
        preds[name] = np.asarray(y_pred)
        if y_prob is not None:
            roc_data[name] = (np.asarray(bundle.y_test), np.asarray(y_prob))

        ctx.record("train_eval", dataset=bundle.key, model=name,
                   family=spec.family, train_time_s=round(train_time, 4),
                   infer_ms_per_sample=round(infer_ms, 5), model_size_bytes=size,
                   accuracy=round(metrics["Accuracy"], 6),
                   f1=round(metrics["F1-Score"], 6),
                   mcc=round(metrics["MCC"], 6),
                   saved_model=str(model_path.relative_to(ctx.run_dir)))
        ctx.ledger_append({
            "dataset": bundle.key, "dataset_name": bundle.name,
            "task": bundle.task, "model": name, "family": spec.family,
            **{k: metrics[k] for k in (
                "Accuracy", "Precision", "Recall", "F1-Score", "Specificity",
                "FPR", "FNR", "MCC", "Cohen Kappa", "AUC-ROC",
                "Training Time (s)")},
            "Inference ms/sample": infer_ms, "Model Size (bytes)": size,
        })

    # Per-dataset figures for this dataset
    reporting.plot_roc(bundle, roc_data, ctx)
    reporting.plot_confusion_matrices(bundle, preds, ctx)
    reporting.plot_f1_comparison(bundle, rows, ctx)
    return rows


# --------------------------------------------------------------------------- #
# Phase 3 — k-fold cross-validation (confidence intervals)                    #
# --------------------------------------------------------------------------- #
def run_cv(ctx: RunContext, bundle: DatasetBundle, models: dict,
           folds: int, cap: int) -> list[dict]:
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler

    # Use RAW (unscaled) features so standardisation can happen INSIDE each fold
    # via a Pipeline — this prevents validation-fold statistics from leaking into
    # the scaler (a per-fold-correct estimate of the confidence interval).
    X_df, y = load_xy(bundle.key)
    X = X_df.to_numpy()
    if cap and len(y) > cap:
        rng = np.random.RandomState(config.SEED)
        idx = []
        for c in np.unique(y):
            c_idx = np.where(y == c)[0]
            take = max(1, int(round(cap * len(c_idx) / len(y))))
            idx.extend(rng.choice(c_idx, size=min(take, len(c_idx)), replace=False))
        idx = np.array(idx)
        X, y = X[idx], y[idx]
        ctx.record("cv_subsample", dataset=bundle.key, capped_to=len(y), cap=cap)

    skf = StratifiedKFold(n_splits=folds, shuffle=True, random_state=config.SEED)

    rows = []
    for name, spec in models.items():
        try:
            # StandardScaler is refit on the training folds only, every split.
            pipe = Pipeline([("scaler", StandardScaler()),
                             ("model", clone(spec.estimator))])
            cvres = cross_validate(pipe, X, y, cv=skf,
                                   scoring=["f1", "accuracy"], n_jobs=1)
            f1, acc = cvres["test_f1"], cvres["test_accuracy"]
        except Exception as exc:  # pragma: no cover
            ctx.log.warning("  CV failed for %s on %s: %s", name, bundle.key, exc)
            continue
        row = {
            "Dataset": bundle.key, "Model": name, "Family": spec.family,
            "F1 mean": float(f1.mean()), "F1 std": float(f1.std()),
            "Accuracy mean": float(acc.mean()), "Accuracy std": float(acc.std()),
            "folds": folds, "n_samples": int(len(y)),
        }
        rows.append(row)
        ctx.record("cv", dataset=bundle.key, model=name, folds=folds,
                   f1_mean=round(row["F1 mean"], 6), f1_std=round(row["F1 std"], 6),
                   acc_mean=round(row["Accuracy mean"], 6))
        ctx.log.info("  [CV %s] %s F1=%.4f±%.4f", bundle.key, name,
                     row["F1 mean"], row["F1 std"])
    return rows


# --------------------------------------------------------------------------- #
# Phase 4 — cross-dataset transfer (concept-drift proxy)                      #
# --------------------------------------------------------------------------- #
def run_cross_dataset(ctx: RunContext, models: dict, pairs) -> list[dict]:
    from sklearn.preprocessing import StandardScaler

    rows = []
    for src, tgt in pairs:
        Xs, ys = load_xy(src)
        Xt, yt = load_xy(tgt)
        common = sorted(set(Xs.columns) & set(Xt.columns))
        if len(common) < 2:
            ctx.log.warning("  cross %s->%s: only %d common features, skipping",
                            src, tgt, len(common))
            ctx.record("cross_dataset_skip", dataset=src,
                       reason="insufficient common features", target=tgt,
                       common=len(common))
            continue
        Xs_c, ys_c = _stratified_cap(Xs[common], ys, CROSS_MAX_N)
        if len(ys_c) < len(ys):
            ctx.record("cross_dataset_subsample", dataset=f"{src}->{tgt}",
                       source_rows=len(ys), capped_to=len(ys_c), cap=CROSS_MAX_N)
        ctx.log.info("  cross %s->%s on %d shared features (src n=%d)",
                     src, tgt, len(common), len(ys_c))
        scaler = StandardScaler().fit(Xs_c)
        Xs_s = scaler.transform(Xs_c)
        Xt_s = scaler.transform(Xt[common])
        ys = ys_c
        for name, spec in models.items():
            model = clone(spec.estimator)
            model.fit(Xs_s, ys)
            y_pred, infer_ms = measure_inference(model, Xt_s)
            y_prob = predict_proba_safe(model, Xt_s)
            metrics = evaluate_model(yt, y_pred, y_prob, 0.0)
            row = {"Source": src, "Target": tgt, "Model": name,
                   "Family": spec.family, "common_features": len(common),
                   **{k: metrics[k] for k in ("Accuracy", "Precision", "Recall",
                                              "F1-Score", "MCC", "AUC-ROC")}}
            rows.append(row)
            ctx.record("cross_dataset", dataset=f"{src}->{tgt}", model=name,
                       common_features=len(common),
                       accuracy=round(metrics["Accuracy"], 6),
                       f1=round(metrics["F1-Score"], 6))
    return rows


# --------------------------------------------------------------------------- #
# Main                                                                        #
# --------------------------------------------------------------------------- #
def main() -> None:
    ap = argparse.ArgumentParser(description="Casket experiment runner")
    ap.add_argument("--datasets", default=",".join(config.DATASETS),
                    help="comma-separated dataset keys (default: all)")
    ap.add_argument("--quick", action="store_true",
                    help="subsample each dataset for a fast smoke test")
    ap.add_argument("--no-cv", action="store_true")
    ap.add_argument("--no-cross", action="store_true")
    ap.add_argument("--cv-folds", type=int, default=config.CV_FOLDS)
    ap.add_argument("--label", default="main")
    args = ap.parse_args()

    keys = [k.strip() for k in args.datasets.split(",") if k.strip()]
    ctx = RunContext(label="quick" if args.quick else args.label)
    ctx.log.info("Datasets: %s | quick=%s cv=%s cross=%s",
                 keys, args.quick, not args.no_cv, not args.no_cross)

    models = get_models()
    ctx.log.info("Models (%d): %s", len(models), list(models))
    ctx.record("models", models=[{"name": s.name, "family": s.family,
                                  "params": s.params} for s in models.values()])

    all_primary, all_cv, bundles = [], [], {}
    for key in keys:
        ctx.log.info("=== Dataset %s ===", key)
        bundle = load_and_preprocess(key, ctx)
        if args.quick:
            bundle = _subsample_bundle(bundle, QUICK_CAP)
        bundles[key] = bundle
        profile_bundle(bundle, ctx)
        plot_distribution(bundle, ctx)
        all_primary.extend(run_primary(ctx, bundle, models))
        if not args.no_cv:
            all_cv.extend(run_cv(ctx, bundle, models, args.cv_folds, CV_MAX_N))

    # Persist primary results (run dir + canonical tables)
    df_primary = pd.DataFrame(all_primary)
    _write_results(ctx, df_primary, keys)

    cross_rows = []
    if not args.no_cross:
        pairs = [(s, t) for s, t in config.CROSS_DATASET_PAIRS
                 if s in bundles and t in bundles]
        cross_rows = run_cross_dataset(ctx, models, pairs)
        if cross_rows:
            pd.DataFrame(cross_rows).to_csv(
                ctx.run_dir / "cross_dataset_results.csv", index=False)

    if all_cv:
        pd.DataFrame(all_cv).to_csv(ctx.run_dir / "cv_results.csv", index=False)

    # Phase 5 — reporting
    reporting.plot_green_ai(df_primary, ctx)
    reporting.plot_literature_comparison(df_primary, ctx)
    reporting.write_summary(df_primary, all_cv, cross_rows, ctx)

    ctx.finalize(extra={"n_models": len(models), "datasets": keys,
                        "n_primary_rows": len(df_primary)})
    ctx.log.info("DONE. Results in %s", ctx.run_dir)


def _subsample_bundle(bundle: DatasetBundle, cap: int) -> DatasetBundle:
    """Stratified subsample of train/test for quick smoke tests."""
    def take(X, y, n):
        if len(y) <= n:
            return X, y
        rng = np.random.RandomState(config.SEED)
        idx = []
        for c in np.unique(y):
            ci = np.where(y == c)[0]
            idx.extend(rng.choice(ci, max(1, int(n * len(ci) / len(y))), False))
        idx = np.array(idx)
        return X[idx], y[idx]

    Xtr, ytr = take(bundle.X_train, bundle.y_train, cap)
    Xte, yte = take(bundle.X_test, bundle.y_test, max(1, cap // 4))
    bundle.X_train, bundle.y_train = Xtr, ytr
    bundle.X_test, bundle.y_test = Xte, yte
    return bundle


def _write_results(ctx: RunContext, df: pd.DataFrame, keys: list[str]) -> None:
    cols = ["Dataset", "Model", "Family", "Accuracy", "Precision", "Recall",
            "F1-Score", "Specificity", "FPR", "FNR", "MCC", "Cohen Kappa",
            "AUC-ROC", "Training Time (s)", "Inference ms/sample",
            "Model Size (bytes)"]
    df = df[[c for c in cols if c in df.columns]]
    df.to_csv(ctx.run_dir / "all_datasets_results.csv", index=False)
    config.TABLES_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(config.TABLES_DIR / "all_datasets_results.csv", index=False)
    for key in keys:
        sub = df[df["Dataset"] == key]
        sub.to_csv(ctx.run_dir / f"{key}_results.csv", index=False)
        sub.to_csv(config.TABLES_DIR / f"{key}_results.csv", index=False)
    ctx.record("results_written", rows=len(df), datasets=keys)


if __name__ == "__main__":
    main()
