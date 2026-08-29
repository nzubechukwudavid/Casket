"""Evaluation metrics and efficiency measurements.

The eleven classification metrics defined in the thesis methodology (§3.6) plus
the Green-AI efficiency measures: training time (recorded by the caller),
inference latency per sample, and serialized model size.
"""
from __future__ import annotations

import pickle
import time
from typing import Any

import numpy as np
from sklearn.metrics import (accuracy_score, cohen_kappa_score, confusion_matrix,
                             f1_score, matthews_corrcoef, precision_score,
                             recall_score, roc_auc_score)


def evaluate_model(y_true, y_pred, y_prob=None, train_time: float = 0.0) -> dict:
    """Compute the eleven evaluation metrics from predictions."""
    cm = confusion_matrix(y_true, y_pred)
    if cm.shape == (2, 2):
        tn, fp, fn, tp = cm.ravel()
    else:
        # Degenerate case (single class predicted) — guard against crash.
        tn, fp, fn, tp = 0, 0, 0, 0

    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0.0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0
    fnr = fn / (fn + tp) if (fn + tp) > 0 else 0.0

    if y_prob is not None:
        try:
            auc_roc = roc_auc_score(y_true, y_prob)
        except Exception:
            auc_roc = 0.0
    else:
        auc_roc = 0.0

    return {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred, zero_division=0),
        "Recall": recall_score(y_true, y_pred, zero_division=0),
        "F1-Score": f1_score(y_true, y_pred, zero_division=0),
        "Specificity": specificity,
        "FPR": fpr,
        "FNR": fnr,
        "MCC": matthews_corrcoef(y_true, y_pred),
        "Cohen Kappa": cohen_kappa_score(y_true, y_pred),
        "AUC-ROC": auc_roc,
        "Training Time (s)": train_time,
    }


def model_size_bytes(model: Any) -> int:
    """Serialized size of a fitted model — a proxy for deployment footprint."""
    try:
        return len(pickle.dumps(model))
    except Exception:
        return -1


def measure_inference(model: Any, X_test) -> tuple[np.ndarray, float]:
    """Predict on the test set and return (y_pred, ms-per-sample latency)."""
    start = time.perf_counter()
    y_pred = model.predict(X_test)
    elapsed = time.perf_counter() - start
    n = len(X_test) if len(X_test) else 1
    return y_pred, (elapsed / n) * 1000.0


def predict_proba_safe(model: Any, X_test):
    """Positive-class probabilities if available, else ``None``."""
    if hasattr(model, "predict_proba"):
        try:
            return model.predict_proba(X_test)[:, 1]
        except Exception:
            return None
    return None
