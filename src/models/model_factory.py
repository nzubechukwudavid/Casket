"""Model factory — the ten benchmarked algorithms across four families.

Returns, for each model, a fresh estimator together with its mathematical family
(thesis §3.5) and a snapshot of its hyperparameters, so the run manifest/ledger
records exactly what was trained. Missing optional libraries are logged loudly
(not silently swallowed) so the audit trail makes any gap explicit.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any

from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

import config

_log = logging.getLogger("casket.models")

# Mathematical families (thesis Figure 3.4 / Table 3).
GRADIENT_BOOSTING = "Gradient Boosting"
BAGGING = "Bagging Ensemble"
BASE_NONLINEAR = "Base Non-Linear"
LINEAR_PROB = "Linear/Probabilistic"


@dataclass
class ModelSpec:
    name: str
    family: str
    estimator: Any

    @property
    def params(self) -> dict:
        return self.estimator.get_params()


def get_models() -> dict[str, ModelSpec]:
    """Instantiate the full model set. Raises if a required lib is unavailable."""
    specs: list[ModelSpec] = [
        ModelSpec("XGBoost", GRADIENT_BOOSTING,
                  XGBClassifier(random_state=config.SEED, eval_metric="logloss")),
        ModelSpec("Random Forest", BAGGING,
                  RandomForestClassifier(random_state=config.SEED)),
        ModelSpec("Extra Trees", BAGGING,
                  ExtraTreesClassifier(random_state=config.SEED)),
        ModelSpec("Decision Tree", BASE_NONLINEAR,
                  DecisionTreeClassifier(random_state=config.SEED)),
        ModelSpec("SVM", BASE_NONLINEAR,
                  SVC(random_state=config.SEED, probability=True)),
        ModelSpec("KNN", BASE_NONLINEAR, KNeighborsClassifier()),
        ModelSpec("Logistic Regression", LINEAR_PROB,
                  LogisticRegression(random_state=config.SEED, max_iter=1000)),
        ModelSpec("Gaussian Naive Bayes", LINEAR_PROB, GaussianNB()),
    ]

    # Optional gradient-boosting libraries — required by the thesis (3 GBMs).
    try:
        from lightgbm import LGBMClassifier
        specs.insert(1, ModelSpec("LightGBM", GRADIENT_BOOSTING,
                                  LGBMClassifier(random_state=config.SEED,
                                                 verbose=-1)))
    except ImportError:
        _log.warning("LightGBM not installed — model will be SKIPPED. "
                     "Install it to match the thesis (3 GBM models).")

    try:
        from catboost import CatBoostClassifier
        specs.insert(2, ModelSpec("CatBoost", GRADIENT_BOOSTING,
                                  CatBoostClassifier(random_state=config.SEED,
                                                     verbose=0,
                                                     allow_writing_files=False)))
    except ImportError:
        _log.warning("CatBoost not installed — model will be SKIPPED. "
                     "Install it to match the thesis (3 GBM models).")

    return {spec.name: spec for spec in specs}
