"""Backwards-compatible entry point.

The pipeline now lives in :mod:`src.runner`. This shim preserves the old
``python src/main_pipeline.py`` invocation while delegating to the new runner.
Prefer: ``python -m src.runner``.
"""
from src.runner import main

if __name__ == "__main__":
    main()
