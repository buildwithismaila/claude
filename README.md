# Noise-Robust Classification of Power Quality Disturbances

Code accompanying the manuscript *Noise-Robust Classification of Power Quality
Disturbances Using Discrete Wavelet Transform Features and Machine Learning*.

Everything here is pure Python — no MATLAB or proprietary toolbox is needed,
and every reported number regenerates from a single master seed.

## What it does

1. Synthesises nine power-quality disturbance classes (normal, sag, swell,
   interruption, harmonics, flicker, oscillatory transient, notch, and
   sag-with-harmonics) with randomised magnitude, onset, duration and
   fundamental phase.
2. Corrupts every base signal with additive white Gaussian noise at 50, 40,
   30 and 20 dB SNR, keeping the clean signal as a fifth condition.
3. Extracts 42 wavelet features — seven statistical descriptors from each of
   six bands of a five-level db4 decomposition — plus three reference
   time-domain features.
4. Compares five classifiers under **grouped** cross-validation, in which all
   noisy variants of a base signal stay inside one fold, and measures the
   optimistic bias that random splitting would have produced instead.
5. Reports accuracy versus SNR, per-class confusion, feature importance and
   the minimal feature subset, plus sensitivity to the mother wavelet.

## Install and run

```bash
pip install numpy scipy scikit-learn PyWavelets matplotlib
python3 run_experiment.py --n-per-class 200 --seed 20251021
```

Runtime is a few tens of minutes on a laptop. For a quick check:

```bash
python3 run_experiment.py --n-per-class 20
```

## Outputs

| Path | Contents |
| --- | --- |
| `results/tables.md` | Tables 6.1–6.6, formatted for the manuscript |
| `results/results.json` | Every number, machine readable |
| `results/run.log` | Console log of the run |
| `figures/fig_6_1_accuracy_vs_snr.png` | Accuracy versus SNR, all classifiers |
| `figures/fig_6_2_confusion_20db.png` | Confusion matrix at 20 dB |
| `figures/fig_6_3_feature_subset.png` | Accuracy versus feature-subset size |
| `figures/fig_classes.png` | The nine classes, for visual verification |

## Layout

```
pqclass/signals.py    signal models, noise injection, dataset assembly
pqclass/features.py   wavelet decomposition and statistical descriptors
pqclass/evaluate.py   grouped CV, metrics, confusion matrices
run_experiment.py     driver producing all tables and figures
```

## Two things to check before publishing

**The signal-model parameters are unverified.** The parametric forms and
ranges in `pqclass/signals.py` follow the conventional models used across the
PQ classification literature, but they were not transcribed from a verified
citation. Before submission, check every equation and range against the
specific published source cited as [2] in the manuscript, and check the class
definitions against IEEE 1159 itself. Where the source differs, the source
wins and this code changes.

**Training is noise-aware.** Each classifier is trained once on a pooled
training fold containing every noise condition, then evaluated separately at
each condition. This is the realistic deployment case. If you want the
train-and-test-at-one-SNR design instead, that is a different experiment and
needs a separate run.
