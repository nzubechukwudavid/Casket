"""Central configuration for the Casket pipeline.

Holds repo-relative paths, the dataset registry, the global seed, and the
deep-learning baseline table used for the Green-AI comparative analysis.

Everything here is plain data so it can be snapshotted into a run manifest for a
complete audit trail. No hardcoded absolute paths: all locations derive from the
repository root (the directory containing this file).
"""
from __future__ import annotations

from pathlib import Path

# --------------------------------------------------------------------------- #
# Paths (all relative to the repository root)                                  #
# --------------------------------------------------------------------------- #
BASE_DIR = Path(__file__).resolve().parent
DATASETS_DIR = BASE_DIR / "Datasets"
RESULTS_DIR = BASE_DIR / "results"
RUNS_DIR = RESULTS_DIR / "runs"
# "latest" holds convenience copies of the MOST RECENT run's figures + tables,
# overwritten each run. The authoritative, never-overwritten record of any run
# lives under results/runs/<run_id>/.
LATEST_DIR = RESULTS_DIR / "latest"
FIGURES_DIR = LATEST_DIR / "figures"
TABLES_DIR = LATEST_DIR / "tables"
DOCS_DIR = BASE_DIR / "docs"
LEDGER_PATH = RESULTS_DIR / "ledger.csv"

# --------------------------------------------------------------------------- #
# Reproducibility                                                             #
# --------------------------------------------------------------------------- #
SEED = 42
TEST_SIZE = 0.20
CV_FOLDS = 5

# --------------------------------------------------------------------------- #
# Dataset registry                                                            #
# --------------------------------------------------------------------------- #
# One entry per dataset. This replaces the brittle filename-substring matching
# that the original data_preprocessing.py relied on.
#
#   key                : short stable id used in outputs and the ledger
#   name               : human-friendly label (matches the thesis "Dataset N")
#   path               : CSV location (relative to DATASETS_DIR)
#   target_col         : name of the label column
#   drop_cols          : non-feature identifier columns to drop if present
#   type               : "raw_byte" (cols are raw PE header bytes) or
#                        "parsed_field" (named, parsed PE header fields)
#   multiclass_collapse: if True, map target != 0 -> 1 (malware vs benign)
#   task               : "ransomware" (true ransomware-vs-goodware) or
#                        "malware" (general malware-vs-benign)
DATASETS: dict[str, dict] = {
    "D1": {
        "name": "Dataset 1 - Mendeley Data",
        "path": "Dataset 1 - Mendeley Data/Ransomware_headers.csv",
        "target_col": "GR",
        "drop_cols": ["ID", "filename", "family", "Unnamed: 0"],
        "type": "raw_byte",
        "multiclass_collapse": False,
        "task": "ransomware",
    },
    "D2": {
        "name": "Dataset 2 - Oriola Kolawole",
        "path": "Dataset 2 - Oriola Kolawole/pe_headers.csv",
        "target_col": "GR",
        "drop_cols": ["ID", "filename", "family", "Unnamed: 0"],
        "type": "raw_byte",
        "multiclass_collapse": False,
        "task": "ransomware",
    },
    "D3": {
        "name": "Dataset 3 - Joakim Arvidsson",
        "path": "Dataset 3 - Joakim Arvidsson/PE_Header.csv",
        "target_col": "Type",
        "drop_cols": ["SHA256", "Unnamed: 0"],
        "type": "parsed_field",
        "multiclass_collapse": True,   # Type 0=benign, 1..6=malware families
        "task": "malware",
    },
    "D4": {
        "name": "Dataset 4 - AM",
        "path": "Dataset 4 - AM/Malware-Benign.csv",
        "target_col": "Malware",
        "drop_cols": ["Hash_md5_Name", "Unnamed: 0"],
        "type": "parsed_field",
        "multiclass_collapse": False,
        "task": "malware",
    },
}

# Datasets whose positive class is genuinely *ransomware* (used for scope tags).
RANSOMWARE_DATASETS = [k for k, v in DATASETS.items() if v["task"] == "ransomware"]

# Schema-compatible pairs for cross-dataset (concept-drift proxy) transfer.
# D3 and D4 are both parsed PE-header fields and share many columns.
CROSS_DATASET_PAIRS = [("D3", "D4"), ("D4", "D3")]

# --------------------------------------------------------------------------- #
# Deep-learning baselines from the literature (thesis Table 5).               #
# Used for the Green-AI comparative analysis. Values are percentages.         #
# These come from published work (no local CNN training); the comparison      #
# argument is accuracy parity at far lower compute on CPU-only hardware.       #
# --------------------------------------------------------------------------- #
DL_BASELINES = [
    {"model": "Xception ColSeq (CNN)", "dataset": "Moreira", "accuracy": 98.20,
     "precision": 97.50, "recall": 98.76, "f1": 98.12, "source": "Moreira et al. (2023)",
     "gpu": True},
    {"model": "Xception ColSeq (CNN)", "dataset": "Manavi", "accuracy": 93.73,
     "precision": 92.95, "recall": 94.64, "f1": 93.75, "source": "Moreira et al. (2023)",
     "gpu": True},
    {"model": "LSTM", "dataset": "Manavi", "accuracy": 93.25,
     "precision": 93.33, "recall": 93.25, "f1": 93.24, "source": "Manavi & Hamzeh (2021)",
     "gpu": True},
    {"model": "CNN (Grey-scale Zigzag)", "dataset": "Manavi", "accuracy": 93.33,
     "precision": 93.40, "recall": 93.33, "f1": 93.34, "source": "Manavi & Hamzeh (2022)",
     "gpu": True},
    {"model": "Graph Embedding + RF", "dataset": "Manavi", "accuracy": 93.30,
     "precision": 93.48, "recall": 93.30, "f1": 93.28, "source": "Manavi & Hamzeh (2022a)",
     "gpu": False},
]

# Hardware context recorded for the Green-AI claim (thesis §3.7).
HARDWARE_NOTE = "CPU-only commodity endpoint; no GPU/TPU acceleration used."
