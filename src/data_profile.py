"""Exploratory profiling and class-distribution figures.

Produces a compact profile of each dataset (shape, class balance, NaN%, feature
count, hash) for the audit trail, and regenerates the per-dataset class
distribution figure (``Dataset_N_Distribution.png``) reproducibly.
"""
from __future__ import annotations

import numpy as np

import matplotlib
matplotlib.use("Agg")  # headless / no display
import matplotlib.pyplot as plt  # noqa: E402

from src.audit import RunContext
from src.data_preprocessing import DatasetBundle


def fig_label(key: str) -> str:
    """Map a registry key (``D1``) to the canonical figure stem (``Dataset_1``)."""
    return f"Dataset_{key[1:]}" if key.startswith("D") and key[1:].isdigit() else key


def profile_bundle(bundle: DatasetBundle, ctx: RunContext) -> dict:
    """Record a profile of a preprocessed dataset to the audit trail."""
    y_all = np.concatenate([bundle.y_train, bundle.y_test])
    classes, counts = np.unique(y_all, return_counts=True)
    balance = {int(c): int(n) for c, n in zip(classes, counts)}
    total = int(y_all.size)
    minority = min(counts) / total if total else 0.0
    profile = {
        "key": bundle.key,
        "name": bundle.name,
        "task": bundle.task,
        "n_features": len(bundle.feature_names),
        "n_samples": total,
        "class_balance": balance,
        "minority_fraction": round(float(minority), 4),
        **bundle.provenance,
    }
    ctx.record("data_profile", dataset=bundle.key, **profile)
    ctx.log.info("[%s] %s | features=%d samples=%d balance=%s",
                 bundle.key, bundle.name, profile["n_features"],
                 total, balance)
    return profile


def plot_distribution(bundle: DatasetBundle, ctx: RunContext,
                      also_canonical=True) -> None:
    """Bar chart of class distribution -> run figures dir (and results/figures)."""
    import config

    y_all = np.concatenate([bundle.y_train, bundle.y_test])
    classes, counts = np.unique(y_all, return_counts=True)
    pos_label = "Ransomware" if bundle.task == "ransomware" else "Malware"
    names = ["Benign" if c == 0 else pos_label for c in classes]

    fig, ax = plt.subplots(figsize=(5, 4))
    bars = ax.bar(names, counts, color=["#4C72B0", "#C44E52"][: len(names)])
    ax.set_title(f"{bundle.name}\nClass Distribution")
    ax.set_ylabel("Sample count")
    for b, n in zip(bars, counts):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height(), f"{int(n)}",
                ha="center", va="bottom", fontsize=9)
    fig.tight_layout()

    stem = fig_label(bundle.key)
    out = ctx.figures_dir / f"{stem}_Distribution.png"
    fig.savefig(out, dpi=120)
    if also_canonical:
        config.FIGURES_DIR.mkdir(parents=True, exist_ok=True)
        fig.savefig(config.FIGURES_DIR / f"{stem}_Distribution.png", dpi=120)
    plt.close(fig)
    ctx.record("figure", dataset=bundle.key, kind="distribution", path=str(out))
