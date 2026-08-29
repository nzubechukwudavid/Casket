"""Audit / experiment-tracking layer for the Casket pipeline.

Provides a single ``RunContext`` object that gives every run a complete,
self-contained audit trail:

* a timestamped run directory ``results/runs/<run_id>/``
* ``run.log``        — full console log (also streamed to stdout)
* ``manifest.json``  — hardware, OS, Python + library versions, seed,
                       dataset SHA-256 hashes, timing, config snapshot
* ``audit.jsonl``    — one timestamped JSON record per pipeline step
* ``results/ledger.csv`` — append-only, one row per (run, dataset, model)

No third-party tracking service is used; everything is plain files so the trail
is fully reproducible and inspectable.
"""
from __future__ import annotations

import csv
import hashlib
import json
import logging
import os
import platform
import random
import sys
import uuid
from datetime import datetime, timezone
from importlib import metadata
from pathlib import Path
from typing import Any

import numpy as np

import config


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def seed_everything(seed: int = config.SEED) -> None:
    """Seed all relevant RNGs for reproducibility."""
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)


def sha256_file(path: str | Path, chunk_size: int = 1 << 20) -> str:
    """Return the SHA-256 hex digest of a file (streamed, memory-safe)."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


# Libraries whose versions are worth pinning into the manifest.
_TRACKED_LIBS = [
    "numpy", "pandas", "scikit-learn", "xgboost",
    "lightgbm", "catboost", "matplotlib", "seaborn", "psutil",
]

# Ordered columns for the append-only ledger.
LEDGER_FIELDS = [
    "run_id", "timestamp", "dataset", "dataset_name", "task", "model", "family",
    "Accuracy", "Precision", "Recall", "F1-Score", "Specificity",
    "FPR", "FNR", "MCC", "Cohen Kappa", "AUC-ROC",
    "Training Time (s)", "Inference ms/sample", "Model Size (bytes)",
]


class RunContext:
    """Owns a single experiment run's directory, logging and audit records."""

    def __init__(self, label: str = "main", seed: int = config.SEED):
        self.seed = seed
        self.started_at = _utc_now_iso()
        ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        self.run_id = f"{ts}-{label}-{uuid.uuid4().hex[:6]}"

        self.run_dir = config.RUNS_DIR / self.run_id
        self.figures_dir = self.run_dir / "figures"
        self.run_dir.mkdir(parents=True, exist_ok=True)
        self.figures_dir.mkdir(parents=True, exist_ok=True)

        self.audit_path = self.run_dir / "audit.jsonl"
        self.manifest_path = self.run_dir / "manifest.json"

        seed_everything(seed)
        self._setup_logging()
        self._dataset_hashes: dict[str, dict] = {}
        self._step_counter = 0

        self.log.info("Run started: %s", self.run_id)
        self.log.info("Run directory: %s", self.run_dir)

    # ------------------------------------------------------------------ #
    # Logging                                                            #
    # ------------------------------------------------------------------ #
    def _setup_logging(self) -> None:
        self.log = logging.getLogger(f"casket.{self.run_id}")
        self.log.setLevel(logging.INFO)
        self.log.propagate = False
        fmt = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s",
                                "%H:%M:%S")
        fh = logging.FileHandler(self.run_dir / "run.log", encoding="utf-8")
        fh.setFormatter(fmt)
        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(fmt)
        self.log.handlers.clear()
        self.log.addHandler(fh)
        self.log.addHandler(sh)

    # ------------------------------------------------------------------ #
    # Audit records                                                      #
    # ------------------------------------------------------------------ #
    def record(self, step: str, dataset: str | None = None,
               model: str | None = None, **fields: Any) -> None:
        """Append a single timestamped record to ``audit.jsonl``."""
        self._step_counter += 1
        rec = {
            "seq": self._step_counter,
            "ts": _utc_now_iso(),
            "step": step,
            "dataset": dataset,
            "model": model,
            **fields,
        }
        with open(self.audit_path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, default=str) + "\n")

    def hash_dataset(self, key: str, path: str | Path) -> str:
        """Hash a dataset file, remember it for the manifest, and audit it."""
        digest = sha256_file(path)
        size = os.path.getsize(path)
        self._dataset_hashes[key] = {"path": str(path), "sha256": digest,
                                     "size_bytes": size}
        self.record("dataset_hash", dataset=key, sha256=digest, size_bytes=size)
        return digest

    # ------------------------------------------------------------------ #
    # Ledger (append-only, across all runs)                              #
    # ------------------------------------------------------------------ #
    def ledger_append(self, row: dict) -> None:
        path = config.LEDGER_PATH
        path.parent.mkdir(parents=True, exist_ok=True)
        new_file = not path.exists()
        full = {"run_id": self.run_id, "timestamp": _utc_now_iso()}
        full.update(row)
        with open(path, "a", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=LEDGER_FIELDS,
                                    extrasaction="ignore")
            if new_file:
                writer.writeheader()
            writer.writerow(full)

    # ------------------------------------------------------------------ #
    # Environment capture + manifest                                     #
    # ------------------------------------------------------------------ #
    @staticmethod
    def _library_versions() -> dict[str, str]:
        versions = {}
        for lib in _TRACKED_LIBS:
            try:
                versions[lib] = metadata.version(lib)
            except metadata.PackageNotFoundError:
                versions[lib] = "MISSING"
        return versions

    @staticmethod
    def _hardware_info() -> dict[str, Any]:
        info: dict[str, Any] = {
            "platform": platform.platform(),
            "processor": platform.processor() or platform.machine(),
            "python": platform.python_version(),
            "gpu": False,  # thesis §3.7: CPU-only, no GPU/TPU
        }
        try:
            import psutil
            info["logical_cpus"] = psutil.cpu_count(logical=True)
            info["physical_cpus"] = psutil.cpu_count(logical=False)
            info["ram_total_gb"] = round(psutil.virtual_memory().total / 1e9, 2)
        except Exception:  # pragma: no cover - psutil should be present
            info["logical_cpus"] = os.cpu_count()
        return info

    def finalize(self, extra: dict | None = None) -> Path:
        """Write ``manifest.json`` capturing the full run provenance."""
        config_snapshot = {
            "seed": config.SEED,
            "test_size": config.TEST_SIZE,
            "cv_folds": config.CV_FOLDS,
            "datasets": config.DATASETS,
            "cross_dataset_pairs": config.CROSS_DATASET_PAIRS,
            "hardware_note": config.HARDWARE_NOTE,
        }
        manifest = {
            "run_id": self.run_id,
            "started_at": self.started_at,
            "finished_at": _utc_now_iso(),
            "seed": self.seed,
            "hardware": self._hardware_info(),
            "library_versions": self._library_versions(),
            "dataset_hashes": self._dataset_hashes,
            "config": config_snapshot,
            "command": " ".join(sys.argv),
        }
        if extra:
            manifest.update(extra)
        with open(self.manifest_path, "w", encoding="utf-8") as fh:
            json.dump(manifest, fh, indent=2, default=str)
        self.record("run_finalized", manifest=str(self.manifest_path))
        self.log.info("Manifest written: %s", self.manifest_path)
        return self.manifest_path
