"""Registry-driven data ingestion and preprocessing.

Implements the uniform six-step preprocessing pipeline from the thesis (§3.4):

  1. Data ingestion (CSV -> DataFrame)
  2. Non-numeric identifier column removal
  3. Missing-value handling (drop NaN rows; the removed fraction is tracked)
  4. Target encoding (LabelEncoder; optional multiclass -> binary collapse)
  5. Feature standardisation (StandardScaler, fit on TRAIN ONLY)
  6. Stratified 80/20 partition

Every step emits an audit record via the provided :class:`RunContext`, so the
preprocessing of each dataset is fully traceable.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

import config
from src.audit import RunContext


@dataclass
class DatasetBundle:
    """Everything downstream stages need for one dataset."""
    key: str
    name: str
    task: str
    X_train: np.ndarray
    X_test: np.ndarray
    y_train: np.ndarray
    y_test: np.ndarray
    feature_names: list[str]
    scaler: StandardScaler
    label_encoder: LabelEncoder
    provenance: dict[str, Any] = field(default_factory=dict)


def _resolve_path(spec: dict) -> Any:
    return config.DATASETS_DIR / spec["path"]


def load_raw(key: str) -> pd.DataFrame:
    """Step 1 — ingest a dataset's CSV into a DataFrame."""
    spec = config.DATASETS[key]
    return pd.read_csv(_resolve_path(spec), low_memory=False)


def load_xy(key: str) -> tuple[pd.DataFrame, np.ndarray]:
    """Return cleaned numeric features (named columns) and encoded labels.

    Applies steps 2–4 (drop ids, drop NaN, optional collapse, encode) but NOT
    scaling/splitting. Used for cross-dataset transfer, where feature columns
    from two datasets must be intersected by name.
    """
    spec = config.DATASETS[key]
    df = pd.read_csv(_resolve_path(spec), low_memory=False)
    df = df.drop(columns=[c for c in spec["drop_cols"] if c in df.columns],
                 errors="ignore")
    df = df.dropna()
    y_raw = df[spec["target_col"]]
    if spec.get("multiclass_collapse"):
        y_raw = y_raw.apply(lambda v: 0 if v == 0 else 1)
    y = LabelEncoder().fit_transform(y_raw)
    X = df.drop(columns=[spec["target_col"]])
    X = X.apply(pd.to_numeric, errors="coerce").fillna(0)
    return X, y


def load_and_preprocess(key: str, ctx: RunContext) -> DatasetBundle:
    """Run the full six-step pipeline for dataset ``key`` with audit logging."""
    spec = config.DATASETS[key]
    path = _resolve_path(spec)
    ctx.log.info("[%s] Loading %s", key, path)

    # Provenance: hash before touching the data.
    ctx.hash_dataset(key, path)

    # Step 1 — ingestion
    df = pd.read_csv(path, low_memory=False)
    n_rows_raw, n_cols_raw = df.shape
    ctx.record("ingest", dataset=key, rows=n_rows_raw, cols=n_cols_raw)

    # Step 2 — drop non-numeric identifier columns
    present_drop = [c for c in spec["drop_cols"] if c in df.columns]
    df = df.drop(columns=present_drop, errors="ignore")
    ctx.record("drop_identifier_cols", dataset=key, dropped=present_drop,
               remaining_cols=df.shape[1])

    if spec["target_col"] not in df.columns:
        raise KeyError(
            f"[{key}] target column '{spec['target_col']}' not found. "
            f"Available (first 10): {list(df.columns[:10])}"
        )

    # Step 3 — missing-value handling (track removed fraction, per §3.4 Step 3)
    before = len(df)
    df = df.dropna()
    removed = before - len(df)
    pct_removed = round(100.0 * removed / before, 4) if before else 0.0
    ctx.record("drop_na_rows", dataset=key, rows_before=before,
               rows_after=len(df), rows_removed=removed, pct_removed=pct_removed)

    # Split features / target
    X = df.drop(columns=[spec["target_col"]])
    y_raw = df[spec["target_col"]]

    # Step 4 — target encoding (optional multiclass -> binary collapse first)
    if spec.get("multiclass_collapse"):
        original_classes = sorted(pd.unique(y_raw).tolist())
        y_raw = y_raw.apply(lambda v: 0 if v == 0 else 1)
        ctx.record("multiclass_collapse", dataset=key,
                   original_classes=original_classes, mapped_to="0=benign,1=malware")
    le = LabelEncoder()
    y = le.fit_transform(y_raw)

    # Coerce features to numeric (defensive; parsed datasets are already numeric)
    X = X.apply(pd.to_numeric, errors="coerce").fillna(0)
    feature_names = X.columns.tolist()

    # Class balance for the audit trail
    classes, counts = np.unique(y, return_counts=True)
    balance = {int(c): int(n) for c, n in zip(classes, counts)}
    ctx.record("target_encode", dataset=key, n_classes=len(classes),
               class_balance=balance, n_features=len(feature_names))

    # Step 6 — stratified 80/20 partition (done before scaling to avoid leakage)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config.TEST_SIZE, random_state=config.SEED, stratify=y
    )

    # Step 5 — standardisation, FIT ON TRAIN ONLY
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    ctx.record("split_and_scale", dataset=key,
               train_rows=X_train_scaled.shape[0], test_rows=X_test_scaled.shape[0],
               test_size=config.TEST_SIZE, scaler="StandardScaler(fit=train)")

    provenance = {
        "rows_raw": n_rows_raw,
        "cols_raw": n_cols_raw,
        "rows_after_na": len(df),
        "pct_removed_na": pct_removed,
        "n_features": len(feature_names),
        "class_balance": balance,
        "type": spec["type"],
        "task": spec["task"],
    }
    return DatasetBundle(
        key=key, name=spec["name"], task=spec["task"],
        X_train=X_train_scaled, X_test=X_test_scaled,
        y_train=y_train, y_test=y_test,
        feature_names=feature_names, scaler=scaler, label_encoder=le,
        provenance=provenance,
    )
