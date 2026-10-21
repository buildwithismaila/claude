"""Amplitude study: does the fixed-amplitude convention make the synthetic
benchmark too easy for trivial features?

Background
----------
The main experiment found that three elementary time-domain features (RMS,
crest factor, THD) classify the nine disturbance classes slightly BETTER than
the 42 wavelet features. That is a surprising result, and before reporting it
we need to know whether it says something about wavelets or something about
the dataset.

It says something about the dataset. The synthetic PQ convention fixes the
nominal amplitude at exactly 1.0 p.u., so a record's RMS is a deterministic
function of its class and disturbance depth: normal and harmonics records
both sit at exactly 0.7071 with zero variance. Real records carry no such
guarantee -- nominal voltage varies with tap position, loading and location.

This script re-runs the wavelet-versus-time-domain comparison with nominal
amplitude drawn uniformly over progressively wider ranges, to show how the
apparent advantage of the trivial features depends on that convention.

Usage:
    python3 amplitude_study.py [--n-per-class 200] [--seed 20251021]

Output:
    results/amplitude_study.json
    results/amplitude_study.md       Table 6.7
    figures/fig_6_4_amplitude.png
"""

import argparse
import json
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from pqclass.evaluate import accuracy_by_snr, cross_validate, make_classifiers
from pqclass.features import extract, extract_time
from pqclass.signals import SNR_LEVELS, generate_dataset

RESULTS = Path("results")
FIGURES = Path("figures")

CONDITIONS = [
    ("Fixed at 1.0 p.u. (literature convention)", None),
    ("U(0.95, 1.05)", (0.95, 1.05)),
    ("U(0.90, 1.10)", (0.90, 1.10)),
    ("U(0.80, 1.20)", (0.80, 1.20)),
]

CLASSIFIER = "Multilayer perceptron"
SNR_AT = 30.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-per-class", type=int, default=200)
    ap.add_argument("--seed", type=int, default=20251021)
    args = ap.parse_args()

    RESULTS.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    model = make_classifiers(args.seed)[CLASSIFIER]
    rows, t0 = [], time.time()

    for label, amp in CONDITIONS:
        X, y, groups, snr = generate_dataset(args.n_per_class, args.seed, amplitude=amp)
        entry = {"condition": label, "amplitude": amp}
        for key, F in (("wavelet_42", extract(X)), ("time_domain_3", extract_time(X))):
            r = cross_validate(model, F, y, groups, snr, grouped=True, seed=args.seed)
            m, s = accuracy_by_snr(r, SNR_LEVELS)[SNR_AT]
            entry[key] = {"mean": m, "std": s}
        entry["gap"] = entry["wavelet_42"]["mean"] - entry["time_domain_3"]["mean"]
        rows.append(entry)
        print(f"{label:44s} wavelet={100*entry['wavelet_42']['mean']:.2f}%  "
              f"time={100*entry['time_domain_3']['mean']:.2f}%  "
              f"gap={100*entry['gap']:+.2f}  [{time.time()-t0:.0f}s]", flush=True)

    out = {
        "classifier": CLASSIFIER,
        "snr_db": SNR_AT,
        "n_per_class": args.n_per_class,
        "seed": args.seed,
        "rows": rows,
    }
    (RESULTS / "amplitude_study.json").write_text(json.dumps(out, indent=2))

    L = [f"### Table 6.7 Wavelet versus time-domain features as nominal amplitude "
         f"varies ({CLASSIFIER}, {int(SNR_AT)} dB)\n",
         "| Nominal amplitude | Wavelet, 42 features (%) | Time-domain, 3 features (%) "
         "| Wavelet advantage |",
         "| --- | --- | --- | --- |"]
    for r in rows:
        L.append(
            f"| {r['condition']} "
            f"| {100*r['wavelet_42']['mean']:.2f} ± {100*r['wavelet_42']['std']:.2f} "
            f"| {100*r['time_domain_3']['mean']:.2f} ± {100*r['time_domain_3']['std']:.2f} "
            f"| {100*r['gap']:+.2f} |"
        )
    (RESULTS / "amplitude_study.md").write_text("\n".join(L) + "\n")

    xs = range(len(rows))
    plt.figure(figsize=(7.4, 4.4))
    plt.plot(xs, [100 * r["wavelet_42"]["mean"] for r in rows], marker="o",
             lw=1.6, label="Wavelet, 42 features")
    plt.plot(xs, [100 * r["time_domain_3"]["mean"] for r in rows], marker="s",
             lw=1.6, label="Time-domain, 3 features")
    plt.xticks(list(xs), ["fixed\n1.0 p.u.", "±5%", "±10%", "±20%"])
    plt.xlabel("Nominal amplitude variation")
    plt.ylabel(f"Accuracy at {int(SNR_AT)} dB (%)")
    plt.grid(alpha=0.3)
    plt.legend(fontsize=9)
    plt.tight_layout()
    plt.savefig(FIGURES / "fig_6_4_amplitude.png", dpi=150)
    print(f"\nDone in {time.time()-t0:.0f}s -> results/amplitude_study.md")


if __name__ == "__main__":
    main()
