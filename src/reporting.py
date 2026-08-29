"""Reporting: figures, literature comparison, and the markdown summary.

Regenerates the canonical thesis deliverables reproducibly (confusion matrices,
ROC curves, F1 comparison, Green-AI charts) and writes them both to the run
directory and to ``results/figures`` / ``results/tables``.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, roc_curve

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import seaborn as sns  # noqa: E402

import config
from src.audit import RunContext
from src.data_preprocessing import DatasetBundle
from src.data_profile import fig_label

sns.set_theme(style="whitegrid")


def _save(fig, ctx: RunContext, stem: str, dataset: str | None = None,
          kind: str = "") -> None:
    """Save a figure to the run dir and the canonical results/figures dir."""
    out = ctx.figures_dir / f"{stem}.png"
    fig.savefig(out, dpi=120, bbox_inches="tight")
    config.FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(config.FIGURES_DIR / f"{stem}.png", dpi=120, bbox_inches="tight")
    plt.close(fig)
    ctx.record("figure", dataset=dataset, kind=kind or stem, path=str(out))


# --------------------------------------------------------------------------- #
# Per-dataset figures                                                         #
# --------------------------------------------------------------------------- #
def plot_roc(bundle: DatasetBundle, roc_data: dict, ctx: RunContext) -> None:
    if not roc_data:
        return
    fig, ax = plt.subplots(figsize=(7, 6))
    for name, (y_true, y_prob) in roc_data.items():
        try:
            fpr, tpr, _ = roc_curve(y_true, y_prob)
            ax.plot(fpr, tpr, lw=1.4, label=name)
        except Exception:
            continue
    ax.plot([0, 1], [0, 1], "k--", lw=0.8, alpha=0.6)
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title(f"{bundle.name} — ROC Curves")
    ax.legend(fontsize=7, loc="lower right")
    _save(fig, ctx, f"{fig_label(bundle.key)}_ROC", bundle.key, "roc")


def plot_confusion_matrices(bundle: DatasetBundle, preds: dict,
                            ctx: RunContext) -> None:
    if not preds:
        return
    n = len(preds)
    ncol = 3
    nrow = int(np.ceil(n / ncol))
    fig, axes = plt.subplots(nrow, ncol, figsize=(4 * ncol, 3.4 * nrow))
    axes = np.atleast_1d(axes).ravel()
    labels = ["Benign", "Ransomware" if bundle.task == "ransomware" else "Malware"]
    for ax, (name, y_pred) in zip(axes, preds.items()):
        cm = confusion_matrix(bundle.y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False, ax=ax,
                    xticklabels=labels, yticklabels=labels)
        ax.set_title(name, fontsize=9)
        ax.set_xlabel("Predicted", fontsize=8)
        ax.set_ylabel("Actual", fontsize=8)
    for ax in axes[n:]:
        ax.axis("off")
    fig.suptitle(f"{bundle.name} — Confusion Matrices", y=1.02)
    _save(fig, ctx, f"{fig_label(bundle.key)}_CM", bundle.key, "confusion_matrix")

    # Generate and save clean, individual 2x2 confusion matrices for each model
    for name, y_pred in preds.items():
        fig_ind, ax_ind = plt.subplots(figsize=(5, 4.2))
        cm = confusion_matrix(bundle.y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False, ax=ax_ind,
                    xticklabels=labels, yticklabels=labels,
                    annot_kws={"size": 11})
        ax_ind.set_title(f"Confusion Matrix — {name}", fontsize=11, fontweight="bold", pad=10)
        ax_ind.set_xlabel("Predicted", fontsize=9)
        ax_ind.set_ylabel("Actual", fontsize=9)
        fig_ind.tight_layout()
        stem = f"{fig_label(bundle.key)}_CM_{name.replace(' ', '_')}"
        _save(fig_ind, ctx, stem, bundle.key, f"confusion_matrix_{name.lower().replace(' ', '_')}")


def plot_f1_comparison(bundle: DatasetBundle, rows: list[dict],
                       ctx: RunContext) -> None:
    df = pd.DataFrame(rows).sort_values("F1-Score", ascending=False)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.bar(df["Model"], df["F1-Score"], color=sns.color_palette("viridis",
                                                                       len(df)))
    ax.set_ylim(0, 1.02)
    ax.set_ylabel("F1-Score")
    ax.set_title(f"{bundle.name} — F1-Score by Model")
    ax.tick_params(axis="x", rotation=45)
    for b, v in zip(bars, df["F1-Score"]):
        ax.text(b.get_x() + b.get_width() / 2, v, f"{v:.3f}", ha="center",
                va="bottom", fontsize=7)
    plt.setp(ax.get_xticklabels(), ha="right")
    _save(fig, ctx, f"{fig_label(bundle.key)}_F1_Comparison", bundle.key, "f1")


# --------------------------------------------------------------------------- #
# Green-AI figures                                                            #
# --------------------------------------------------------------------------- #
def plot_green_ai(df: pd.DataFrame, ctx: RunContext) -> None:
    """Training-time, inference-latency and model-size comparison charts."""
    if df.empty:
        return
    # Mean training time per model across datasets (the canonical Green-AI chart).
    agg = (df.groupby("Model")["Training Time (s)"].mean()
           .sort_values(ascending=True))
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.barh(agg.index, agg.values, color=sns.color_palette("crest", len(agg)))
    ax.set_xlabel("Mean Training Time (s) — lower is greener")
    ax.set_title("Green AI — Mean Training Time by Model (CPU-only)")
    for i, v in enumerate(agg.values):
        ax.text(v, i, f" {v:.2f}s", va="center", fontsize=8)
    _save(fig, ctx, "Green_AI_Training_Time", None, "green_ai_train_time")

    # Supplementary: inference latency and model size.
    for col, stem, label in [
        ("Inference ms/sample", "Green_AI_Inference_Latency",
         "Mean Inference Latency (ms/sample)"),
        ("Model Size (bytes)", "Green_AI_Model_Size", "Mean Model Size (KB)"),
    ]:
        if col not in df.columns:
            continue
        series = df.groupby("Model")[col].mean().sort_values()
        if col == "Model Size (bytes)":
            series = series / 1024.0
        fig, ax = plt.subplots(figsize=(8, 4.5))
        ax.barh(series.index, series.values,
                color=sns.color_palette("flare", len(series)))
        ax.set_xlabel(label)
        ax.set_title(f"Green AI — {label} (CPU-only)")
        _save(fig, ctx, stem, None, stem.lower())


def plot_literature_comparison(df: pd.DataFrame, ctx: RunContext) -> None:
    """Best ensemble-ML accuracy per dataset vs published DL baselines."""
    if df.empty:
        return
    best = (df.sort_values("Accuracy", ascending=False)
            .groupby("Dataset").first().reset_index())
    ml_labels = [f"{r.Dataset}: {r.Model}" for r in best.itertuples()]
    ml_acc = (best["Accuracy"] * 100).tolist()

    dl_labels = [f"{b['model']} ({b['dataset']})" for b in config.DL_BASELINES]
    dl_acc = [b["accuracy"] for b in config.DL_BASELINES]

    fig, ax = plt.subplots(figsize=(10, 5))
    x_ml = np.arange(len(ml_acc))
    x_dl = np.arange(len(dl_acc)) + len(ml_acc) + 0.7
    ax.bar(x_ml, ml_acc, color="#2A9D8F", label="This work (ensemble ML, CPU)")
    ax.bar(x_dl, dl_acc, color="#E76F51", label="DL baselines (literature, GPU)")
    ax.set_xticks(list(x_ml) + list(x_dl))
    ax.set_xticklabels(ml_labels + dl_labels, rotation=45, ha="right", fontsize=7)
    ax.set_ylabel("Accuracy (%)")
    ax.set_ylim(80, 100)
    ax.set_title("Green AI — Ensemble ML (CPU) vs Deep-Learning Baselines (GPU)")
    ax.legend()
    _save(fig, ctx, "Literature_Comparison", None, "literature_comparison")


# --------------------------------------------------------------------------- #
# Markdown summary                                                            #
# --------------------------------------------------------------------------- #
_METRIC_COLS = ["Accuracy", "Precision", "Recall", "F1-Score", "Specificity",
                "FPR", "FNR", "MCC", "Cohen Kappa", "AUC-ROC",
                "Training Time (s)", "Inference ms/sample"]


def write_summary(df: pd.DataFrame, cv_rows: list[dict],
                  cross_rows: list[dict], ctx: RunContext) -> None:
    lines: list[str] = [f"# Results Summary — run `{ctx.run_id}`\n"]

    for key in df["Dataset"].unique() if not df.empty else []:
        sub = df[df["Dataset"] == key].copy()
        name = config.DATASETS.get(key, {}).get("name", key)
        lines.append(f"\n### {name} ({key})\n")
        cols = ["Model", "Family"] + _METRIC_COLS
        cols = [c for c in cols if c in sub.columns]
        sub = sub[cols].sort_values("F1-Score", ascending=False)
        lines.append(_md_table(sub))

    if cross_rows:
        lines.append("\n### Cross-Dataset Transfer (concept-drift proxy)\n")
        lines.append(_md_table(pd.DataFrame(cross_rows)))

    if cv_rows:
        lines.append("\n### Cross-Validation (mean ± std)\n")
        lines.append(_md_table(pd.DataFrame(cv_rows)))

    # Green-AI headline
    if not df.empty:
        best = df.sort_values("Accuracy", ascending=False).iloc[0]
        lines.append("\n### Green-AI Headline\n")
        lines.append(
            f"- Best model: **{best['Model']}** on **{best['Dataset']}** — "
            f"Accuracy {best['Accuracy']:.4f}, F1 {best['F1-Score']:.4f}, "
            f"trained in {best['Training Time (s)']:.2f}s on {config.HARDWARE_NOTE}\n")
        lines.append(
            "- Compare against DL baselines in `config.DL_BASELINES` "
            "(e.g. Xception ColSeq 98.20% / 93.73%), all GPU-trained.\n")

    text = "\n".join(lines)
    (ctx.run_dir / "summary.md").write_text(text, encoding="utf-8")
    config.TABLES_DIR.mkdir(parents=True, exist_ok=True)
    (config.TABLES_DIR / "summary.md").write_text(text, encoding="utf-8")
    ctx.record("summary_written", path=str(ctx.run_dir / "summary.md"))


def _md_table(df: pd.DataFrame) -> str:
    df = df.copy()
    for c in df.columns:
        if pd.api.types.is_float_dtype(df[c]):
            df[c] = df[c].map(lambda v: f"{v:.4f}")
    header = "| " + " | ".join(df.columns) + " |"
    sep = "|" + "|".join(["---"] * len(df.columns)) + "|"
    body = "\n".join("| " + " | ".join(map(str, row)) + " |"
                     for row in df.itertuples(index=False))
    return header + "\n" + sep + "\n" + body + "\n"
