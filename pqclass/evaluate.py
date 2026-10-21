"""Evaluation harness: grouped cross-validation, metrics, and the
grouped-versus-random comparison.

The unit of partitioning is the BASE SIGNAL, not the sample. All noisy
variants of one waveform share a group id and stay inside one fold. The
random-split comparison deliberately violates this to measure the bias it
introduces (manuscript section 6.2).
"""

from dataclasses import dataclass, field

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import StratifiedGroupKFold, StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

N_FOLDS = 5


def make_classifiers(seed: int) -> dict[str, Pipeline]:
    """Five classifiers, each inside a pipeline so scaling is fitted per fold.

    Hyperparameters are fixed at sensible defaults here rather than tuned by
    nested search; see run_experiment.py --tune for the nested variant.
    """
    return {
        "Decision tree": Pipeline(
            [("sc", StandardScaler()),
             ("clf", DecisionTreeClassifier(max_depth=10, random_state=seed))]
        ),
        "k-nearest neighbours": Pipeline(
            [("sc", StandardScaler()), ("clf", KNeighborsClassifier(n_neighbors=5))]
        ),
        "Support vector machine": Pipeline(
            [("sc", StandardScaler()),
             ("clf", SVC(C=10.0, gamma="scale", random_state=seed))]
        ),
        "Random forest": Pipeline(
            [("sc", StandardScaler()),
             ("clf", RandomForestClassifier(n_estimators=300, random_state=seed, n_jobs=-1))]
        ),
        "Multilayer perceptron": Pipeline(
            [("sc", StandardScaler()),
             ("clf", MLPClassifier(hidden_layer_sizes=(100,), alpha=1e-3,
                                   max_iter=1000, random_state=seed))]
        ),
    }


@dataclass
class FoldResult:
    fold: int
    y_true: np.ndarray
    y_pred: np.ndarray
    snr: np.ndarray
    classes: list[str] = field(default_factory=list)


def _splits(y, groups, grouped: bool, seed: int):
    if grouped:
        cv = StratifiedGroupKFold(n_splits=N_FOLDS, shuffle=True, random_state=seed)
        return cv.split(np.zeros(len(y)), y, groups)
    cv = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=seed)
    return cv.split(np.zeros(len(y)), y)


def cross_validate(model, F, y, groups, snr, grouped=True, seed=0) -> list[FoldResult]:
    """Fit and predict across folds, retaining per-sample SNR for slicing."""
    out = []
    for k, (tr, te) in enumerate(_splits(y, groups, grouped, seed)):
        m = model
        from sklearn.base import clone

        m = clone(model)
        m.fit(F[tr], y[tr])
        out.append(FoldResult(k, y[te], m.predict(F[te]), snr[te]))
    return out


def _slice(res: FoldResult, snr_level):
    """Mask selecting one noise condition; snr_level None selects the clean set."""
    if snr_level is None:
        return np.isnan(res.snr)
    return res.snr == snr_level


def accuracy_by_snr(results: list[FoldResult], snr_levels) -> dict:
    """Mean and std accuracy across folds, per noise condition."""
    table = {}
    for lv in snr_levels:
        accs = []
        for r in results:
            m = _slice(r, lv)
            if m.sum() == 0:
                continue
            accs.append(accuracy_score(r.y_true[m], r.y_pred[m]))
        table[lv] = (float(np.mean(accs)), float(np.std(accs)))
    return table


def macro_f1_by_snr(results: list[FoldResult], snr_levels) -> dict:
    table = {}
    for lv in snr_levels:
        vals = []
        for r in results:
            m = _slice(r, lv)
            if m.sum() == 0:
                continue
            vals.append(f1_score(r.y_true[m], r.y_pred[m], average="macro", zero_division=0))
        table[lv] = (float(np.mean(vals)), float(np.std(vals)))
    return table


def per_class_f1_by_snr(results, snr_levels, classes) -> dict:
    """{class: {snr: (mean, std)}} of per-class F1."""
    out = {c: {} for c in classes}
    for lv in snr_levels:
        acc = {c: [] for c in classes}
        for r in results:
            m = _slice(r, lv)
            if m.sum() == 0:
                continue
            f = f1_score(r.y_true[m], r.y_pred[m], labels=classes,
                         average=None, zero_division=0)
            for c, v in zip(classes, f):
                acc[c].append(v)
        for c in classes:
            out[c][lv] = (float(np.mean(acc[c])), float(np.std(acc[c])))
    return out


def pooled_confusion(results, classes, snr_level):
    """Confusion matrix pooled over folds at one noise condition."""
    yt, yp = [], []
    for r in results:
        m = _slice(r, snr_level)
        yt.append(r.y_true[m])
        yp.append(r.y_pred[m])
    return confusion_matrix(np.concatenate(yt), np.concatenate(yp), labels=classes)


def overall_accuracy(results) -> tuple[float, float]:
    accs = [accuracy_score(r.y_true, r.y_pred) for r in results]
    return float(np.mean(accs)), float(np.std(accs))
