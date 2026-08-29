# Casket — Computationally Efficient Static Ransomware/Malware Detection (Green AI)

Benchmark of **ten machine-learning algorithms** across four mathematical families
(Gradient Boosting, Bagging, Base Non-Linear, Linear/Probabilistic) on **four PE-header
datasets**, evaluated with **eleven metrics** plus Green-AI efficiency measures, on
**CPU-only** hardware. The thesis argument: ensemble ML can match GPU-trained CNN
baselines (e.g. Xception ColSeq) at a fraction of the compute.

> 📖 **New here? Open [`docs/USER_GUIDE.docx`](docs/USER_GUIDE.docx)** — a complete,
> plain-language Word manual: exact commands (Linux/macOS **and Windows**), where
> outputs live, where trained models are saved, and how to reuse them.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate   # optional
pip install -r requirements.txt
```

## Run

```bash
python -m src.runner                 # full run (all datasets, CV + cross-dataset)
python -m src.runner --quick         # fast smoke test (subsampled)
python -m src.runner --datasets D1,D3 --no-cv --no-cross
```

Outputs (never overwritten between runs) land in `results/runs/<run_id>/`:

| File | Contents |
|------|----------|
| `manifest.json` | hardware, OS, Python + library versions, seed, dataset SHA-256 hashes, config snapshot, timing |
| `audit.jsonl` | one timestamped record per pipeline step (ingest → drop-cols → NaN-drop% → encode → split/scale → train/eval → figures) |
| `run.log` | full console log |
| `*_results.csv`, `all_datasets_results.csv` | per-dataset and aggregate metrics |
| `cv_results.csv`, `cross_dataset_results.csv` | confidence intervals & transfer results |
| `summary.md` | comparative performance matrix |
| `figures/` | confusion matrices, ROC, F1, distribution, Green-AI, literature comparison |
| `models/<dataset>/*.joblib` | every fitted model + the dataset's `_scaler.joblib` / `_label_encoder.joblib`, for reuse on new data |

A global append-only `results/ledger.csv` records one row per `(run, dataset, model)`.
Convenience copies of the **most recent** run's figures/tables are mirrored to
`results/latest/figures` and `results/latest/tables` (overwritten each run; the
authoritative per-run record always lives under `results/runs/<run_id>/`).

## Layout

```
config.py                 # paths, dataset registry, seed, DL baseline table
src/audit.py              # RunContext: logging, manifest, audit.jsonl, ledger, hashing
src/data_preprocessing.py # registry-driven 6-step pipeline (audited)
src/data_profile.py       # EDA profiling + class-distribution figures
src/models/model_factory.py  # the 10 models with family tags
src/evaluation.py         # 11 metrics + inference latency + model size
src/runner.py             # orchestration (primary / CV / cross-dataset / reporting)
src/reporting.py          # figures, literature comparison, summary.md
docs/data_reconciliation.md  # actual CSVs vs draft Table 2
```

## Notes
- Datasets are used as shipped; `docs/data_reconciliation.md` records where the draft's
  Table 2 descriptions diverge from the actual CSVs.
- Framing is malware-inclusive: D1/D2 are ransomware-vs-goodware; D3/D4 are general
  malware-vs-benign (tagged via `task` in `config.py`).
