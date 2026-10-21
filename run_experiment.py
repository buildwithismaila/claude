"""Run the full experiment and emit every table and figure in manuscript section 6.

Usage:
    python3 run_experiment.py [--n-per-class 200] [--seed 20251021]

Outputs:
    results/results.json      all numbers, machine readable
    results/tables.md         tables 6.1 - 6.6, ready to paste
    figures/fig_6_1_accuracy_vs_snr.png
    figures/fig_6_2_confusion_20db.png
    figures/fig_6_3_feature_subset.png

Training design (stated explicitly because it affects interpretation):
each classifier is trained ONCE on the pooled training fold, which contains
every noise condition, and is then evaluated separately at each noise
condition. This is the noise-aware design: the classifier has seen noisy
examples during training. It is the realistic deployment case, and it is the
harder test for the leakage question, because pooled training is exactly
where near-duplicate signals would help a leaky split most.
"""

import argparse
import json
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats as sstats
from sklearn.base import clone
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.preprocessing import StandardScaler

from pqclass.evaluate import (
    N_FOLDS,
    accuracy_by_snr,
    cross_validate,
    macro_f1_by_snr,
    make_classifiers,
    per_class_f1_by_snr,
    pooled_confusion,
)
from pqclass.features import (
    TIME_FEATURE_NAMES,
    extract,
    extract_time,
    wavelet_feature_names,
)
from pqclass.signals import CLASS_LABELS, CLASS_NAMES, SNR_LEVELS, generate_dataset

RESULTS = Path("results")
FIGURES = Path("figures")


def snr_key(lv):
    return "clean" if lv is None else f"{int(lv)}dB"


def fmt(mean_std, pct=True):
    m, s = mean_std
    return f"{100*m:.2f} ± {100*s:.2f}" if pct else f"{m:.3f} ± {s:.3f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-per-class", type=int, default=200)
    ap.add_argument("--seed", type=int, default=20251021)
    args = ap.parse_args()

    RESULTS.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    out: dict = {"config": vars(args), "n_folds": N_FOLDS}
    t0 = time.time()

    # ---------------------------------------------------------------- data
    print("Generating dataset ...", flush=True)
    X, y, groups, snr = generate_dataset(args.n_per_class, args.seed)
    print(f"  signals: {X.shape}, base signals: {len(np.unique(groups))}")
    print("Extracting wavelet features ...", flush=True)
    F = extract(X)
    names = wavelet_feature_names()
    print(f"  features: {F.shape}  [{time.time()-t0:.0f}s]", flush=True)

    out["dataset"] = {
        "n_samples": int(X.shape[0]),
        "n_base_signals": int(len(np.unique(groups))),
        "n_features": int(F.shape[1]),
        "signal_length": int(X.shape[1]),
    }

    classes = CLASS_NAMES
    clfs = make_classifiers(args.seed)

    # ------------------------------------------------- 6.1 accuracy vs SNR
    print("\n[6.1] Grouped CV, all classifiers", flush=True)
    grouped_res, acc_tab, f1_tab = {}, {}, {}
    for name, model in clfs.items():
        t = time.time()
        r = cross_validate(model, F, y, groups, snr, grouped=True, seed=args.seed)
        grouped_res[name] = r
        acc_tab[name] = accuracy_by_snr(r, SNR_LEVELS)
        f1_tab[name] = macro_f1_by_snr(r, SNR_LEVELS)
        print(f"  {name:24s} clean={acc_tab[name][None][0]:.3f} "
              f"20dB={acc_tab[name][20.0][0]:.3f}  [{time.time()-t:.0f}s]", flush=True)

    out["table_6_1_accuracy"] = {
        n: {snr_key(k): v for k, v in t.items()} for n, t in acc_tab.items()
    }
    out["table_6_2_macro_f1"] = {
        n: {snr_key(k): v for k, v in t.items()} for n, t in f1_tab.items()
    }

    best = max(acc_tab, key=lambda n: acc_tab[n][20.0][0])
    out["best_classifier_at_20db"] = best
    print(f"  best at 20 dB: {best}")

    # ------------------------------------------- 6.2 grouped vs random split
    print("\n[6.2] Random (leaky) split comparison", flush=True)
    split_cmp = {}
    for name, model in clfs.items():
        r_rand = cross_validate(model, F, y, groups, snr, grouped=False, seed=args.seed)
        a_g = np.mean([accuracy_score(r.y_true, r.y_pred) for r in grouped_res[name]])
        a_r = np.mean([accuracy_score(r.y_true, r.y_pred) for r in r_rand])
        split_cmp[name] = {
            "grouped": float(a_g),
            "random": float(a_r),
            "bias": float(a_r - a_g),
        }
        print(f"  {name:24s} grouped={a_g:.4f} random={a_r:.4f} bias=+{a_r-a_g:.4f}",
              flush=True)
    out["table_6_3_split_bias"] = split_cmp

    # --------------------------------------------------- 6.3 per-class / CM
    print("\n[6.3] Per-class behaviour", flush=True)
    pc = per_class_f1_by_snr(grouped_res[best], SNR_LEVELS, classes)
    out["table_6_4_per_class_f1"] = {
        c: {snr_key(k): v for k, v in d.items()} for c, d in pc.items()
    }
    cm20 = pooled_confusion(grouped_res[best], classes, 20.0)
    out["confusion_20db"] = {"labels": classes, "matrix": cm20.tolist()}

    # top confusions, off-diagonal
    cmn = cm20 / cm20.sum(axis=1, keepdims=True)
    conf = [
        (classes[i], classes[j], float(cmn[i, j]))
        for i in range(len(classes))
        for j in range(len(classes))
        if i != j
    ]
    conf.sort(key=lambda z: -z[2])
    out["top_confusions_20db"] = conf[:6]
    for a, b, v in conf[:6]:
        print(f"  {a} -> {b}: {100*v:.1f}%")

    # ------------------------------------------------- 6.4 feature selection
    print("\n[6.4] Feature importance and subset sweep", flush=True)
    imp = np.zeros(F.shape[1])
    cv = StratifiedGroupKFold(n_splits=N_FOLDS, shuffle=True, random_state=args.seed)
    for tr, _ in cv.split(np.zeros(len(y)), y, groups):
        rf = RandomForestClassifier(n_estimators=300, random_state=args.seed, n_jobs=-1)
        rf.fit(StandardScaler().fit_transform(F[tr]), y[tr])
        imp += rf.feature_importances_
    imp /= N_FOLDS
    order = np.argsort(-imp)
    out["table_6_5_top_features"] = [
        {"rank": i + 1, "feature": names[order[i]],
         "band": names[order[i]].split("_")[0],
         "descriptor": names[order[i]].split("_", 1)[1],
         "importance": float(imp[order[i]])}
        for i in range(10)
    ]
    for e in out["table_6_5_top_features"]:
        print(f"  {e['rank']:2d}. {e['feature']:16s} {e['importance']:.4f}")

    subset_sizes = [5, 10, 15, 20, 30, 42]
    sweep = {}
    full_fold_acc = None
    for k in subset_sizes:
        idx = order[:k]
        r = cross_validate(clfs[best], F[:, idx], y, groups, snr,
                           grouped=True, seed=args.seed)
        a30 = [accuracy_score(rr.y_true[rr.snr == 30.0], rr.y_pred[rr.snr == 30.0])
               for rr in r]
        sweep[k] = {
            "by_snr": {snr_key(lv): v for lv, v in accuracy_by_snr(r, SNR_LEVELS).items()},
            "fold_acc_30db": [float(v) for v in a30],
        }
        if k == 42:
            full_fold_acc = a30
        print(f"  top-{k:2d}: 30dB acc = {np.mean(a30):.4f}", flush=True)

    # smallest subset not significantly worse than full set at 30 dB
    knee = None
    for k in subset_sizes:
        if k == 42:
            continue
        t_stat, p = sstats.ttest_rel(sweep[k]["fold_acc_30db"], full_fold_acc)
        sweep[k]["p_vs_full_30db"] = float(p)
        if p > 0.05 and knee is None:
            knee = k
    out["figure_6_3_sweep"] = {str(k): v for k, v in sweep.items()}
    out["minimal_subset_30db"] = knee
    print(f"  smallest subset indistinguishable from full set at 30 dB: {knee}")
    print("  NOTE: paired t-test over 5 folds has low power; see results discussion.")

    # ---------------------------------------------------- 6.5 sensitivity
    print("\n[6.5] Sensitivity checks", flush=True)
    sens = {}
    base30 = acc_tab[best][30.0]
    sens["db4_5levels_42feat"] = {"acc_30db": base30}

    F10 = extract(X, wavelet="db10")
    r10 = cross_validate(clfs[best], F10, y, groups, snr, grouped=True, seed=args.seed)
    sens["db10_5levels"] = {"acc_30db": accuracy_by_snr(r10, SNR_LEVELS)[30.0]}

    Ft = extract_time(X)
    rt = cross_validate(clfs[best], Ft, y, groups, snr, grouped=True, seed=args.seed)
    sens["time_domain_only"] = {"acc_30db": accuracy_by_snr(rt, SNR_LEVELS)[30.0]}
    out["table_6_6_sensitivity"] = sens
    for k, v in sens.items():
        print(f"  {k:28s} 30dB acc = {v['acc_30db'][0]:.4f}")

    # ------------------------------------------------------------- figures
    print("\nWriting figures ...", flush=True)
    xs = [20, 30, 40, 50, 60]
    xlabels = ["20", "30", "40", "50", "clean"]
    plt.figure(figsize=(7.2, 4.6))
    for name in clfs:
        ys = [acc_tab[name][lv][0] * 100 for lv in [20.0, 30.0, 40.0, 50.0, None]]
        es = [acc_tab[name][lv][1] * 100 for lv in [20.0, 30.0, 40.0, 50.0, None]]
        plt.errorbar(xs, ys, yerr=es, marker="o", capsize=3, lw=1.4, label=name)
    plt.xticks(xs, xlabels)
    plt.xlabel("Signal-to-noise ratio (dB)")
    plt.ylabel("Classification accuracy (%)")
    plt.grid(alpha=0.3)
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(FIGURES / "fig_6_1_accuracy_vs_snr.png", dpi=150)
    plt.close()

    plt.figure(figsize=(7.4, 6.2))
    plt.imshow(cmn, cmap="Blues", vmin=0, vmax=1)
    short = [CLASS_LABELS[c].split(" ", 1)[0] for c in classes]
    plt.xticks(range(len(classes)), short, rotation=45, ha="right", fontsize=8)
    plt.yticks(range(len(classes)), [CLASS_LABELS[c] for c in classes], fontsize=8)
    for i in range(len(classes)):
        for j in range(len(classes)):
            if cmn[i, j] >= 0.005:
                plt.text(j, i, f"{100*cmn[i,j]:.0f}", ha="center", va="center",
                         fontsize=7, color="white" if cmn[i, j] > 0.5 else "black")
    plt.colorbar(label="row-normalised %", fraction=0.046)
    plt.title(f"{best}, 20 dB SNR", fontsize=10)
    plt.tight_layout()
    plt.savefig(FIGURES / "fig_6_2_confusion_20db.png", dpi=150)
    plt.close()

    plt.figure(figsize=(7.2, 4.6))
    for lv in [20.0, 30.0, None]:
        ys = [sweep[k]["by_snr"][snr_key(lv)][0] * 100 for k in subset_sizes]
        plt.plot(subset_sizes, ys, marker="o", lw=1.4,
                 label="clean" if lv is None else f"{int(lv)} dB")
    plt.xlabel("Number of retained features")
    plt.ylabel("Classification accuracy (%)")
    plt.grid(alpha=0.3)
    plt.legend(fontsize=9)
    plt.tight_layout()
    plt.savefig(FIGURES / "fig_6_3_feature_subset.png", dpi=150)
    plt.close()

    # -------------------------------------------------------------- tables
    L = []
    L.append("### Table 6.1 Accuracy (%) by classifier and noise condition\n")
    L.append("| Classifier | Clean | 50 dB | 40 dB | 30 dB | 20 dB |")
    L.append("| --- | --- | --- | --- | --- | --- |")
    for n in clfs:
        row = [fmt(acc_tab[n][lv]) for lv in [None, 50.0, 40.0, 30.0, 20.0]]
        L.append(f"| {n} | " + " | ".join(row) + " |")

    L.append("\n### Table 6.2 Macro-averaged F1 by classifier and noise condition\n")
    L.append("| Classifier | Clean | 50 dB | 40 dB | 30 dB | 20 dB |")
    L.append("| --- | --- | --- | --- | --- | --- |")
    for n in clfs:
        row = [fmt(f1_tab[n][lv], pct=False) for lv in [None, 50.0, 40.0, 30.0, 20.0]]
        L.append(f"| {n} | " + " | ".join(row) + " |")

    L.append("\n### Table 6.3 Grouped versus random partitioning (overall accuracy, %)\n")
    L.append("| Classifier | Grouped CV (correct) | Random CV (biased) | Difference |")
    L.append("| --- | --- | --- | --- |")
    for n, v in split_cmp.items():
        L.append(f"| {n} | {100*v['grouped']:.2f} | {100*v['random']:.2f} "
                 f"| +{100*v['bias']:.2f} |")

    L.append(f"\n### Table 6.4 Per-class F1, {best}\n")
    L.append("| Class | Clean | 50 dB | 40 dB | 30 dB | 20 dB |")
    L.append("| --- | --- | --- | --- | --- | --- |")
    for c in classes:
        row = [f"{pc[c][lv][0]:.3f}" for lv in [None, 50.0, 40.0, 30.0, 20.0]]
        L.append(f"| {CLASS_LABELS[c]} | " + " | ".join(row) + " |")

    L.append("\n### Table 6.5 Ten highest-ranked features\n")
    L.append("| Rank | Band | Descriptor | Mean importance |")
    L.append("| --- | --- | --- | --- |")
    for e in out["table_6_5_top_features"]:
        L.append(f"| {e['rank']} | {e['band']} | {e['descriptor']} "
                 f"| {e['importance']:.4f} |")

    L.append(f"\n### Table 6.6 Sensitivity checks, {best}, 30 dB\n")
    L.append("| Configuration | Accuracy (%) | Difference from baseline |")
    L.append("| --- | --- | --- |")
    b = sens["db4_5levels_42feat"]["acc_30db"][0]
    labels = {
        "db4_5levels_42feat": "db4, 5 levels, 42 wavelet features (baseline)",
        "db10_5levels": "db10, 5 levels",
        "time_domain_only": "Time-domain features only (RMS, crest factor, THD)",
    }
    for k, v in sens.items():
        a = v["acc_30db"][0]
        d = "—" if k == "db4_5levels_42feat" else f"{100*(a-b):+.2f}"
        L.append(f"| {labels[k]} | {fmt(v['acc_30db'])} | {d} |")

    (RESULTS / "tables.md").write_text("\n".join(L) + "\n")
    out["runtime_seconds"] = time.time() - t0
    (RESULTS / "results.json").write_text(json.dumps(out, indent=2))
    print(f"\nDone in {out['runtime_seconds']:.0f}s")
    print("  results/tables.md, results/results.json, figures/*.png")


if __name__ == "__main__":
    main()
