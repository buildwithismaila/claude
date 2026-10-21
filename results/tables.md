### Table 6.1 Accuracy (%) by classifier and noise condition

| Classifier | Clean | 50 dB | 40 dB | 30 dB | 20 dB |
| --- | --- | --- | --- | --- | --- |
| Decision tree | 66.11 ± 6.89 | 67.22 ± 6.43 | 66.67 ± 5.83 | 66.11 ± 7.54 | 60.00 ± 7.58 |
| k-nearest neighbours | 61.67 ± 7.33 | 62.22 ± 7.97 | 56.11 ± 4.78 | 50.56 ± 8.13 | 48.89 ± 5.15 |
| Support vector machine | 73.33 ± 2.83 | 73.89 ± 4.51 | 73.33 ± 2.83 | 72.22 ± 4.65 | 68.33 ± 7.37 |
| Random forest | 83.89 ± 3.69 | 83.89 ± 3.69 | 83.89 ± 4.78 | 82.22 ± 5.72 | 80.00 ± 4.78 |
| Multilayer perceptron | 76.11 ± 7.58 | 76.11 ± 6.71 | 73.89 ± 5.72 | 71.67 ± 8.31 | 66.67 ± 9.13 |

### Table 6.2 Macro-averaged F1 by classifier and noise condition

| Classifier | Clean | 50 dB | 40 dB | 30 dB | 20 dB |
| --- | --- | --- | --- | --- | --- |
| Decision tree | 0.661 ± 0.069 | 0.672 ± 0.063 | 0.663 ± 0.056 | 0.658 ± 0.072 | 0.589 ± 0.080 |
| k-nearest neighbours | 0.606 ± 0.080 | 0.609 ± 0.084 | 0.546 ± 0.039 | 0.500 ± 0.077 | 0.485 ± 0.053 |
| Support vector machine | 0.725 ± 0.036 | 0.733 ± 0.047 | 0.726 ± 0.027 | 0.717 ± 0.042 | 0.678 ± 0.080 |
| Random forest | 0.838 ± 0.038 | 0.838 ± 0.038 | 0.836 ± 0.051 | 0.818 ± 0.062 | 0.800 ± 0.046 |
| Multilayer perceptron | 0.756 ± 0.085 | 0.756 ± 0.076 | 0.731 ± 0.066 | 0.711 ± 0.090 | 0.657 ± 0.094 |

### Table 6.3 Grouped versus random partitioning (overall accuracy, %)

| Classifier | Grouped CV (correct) | Random CV (biased) | Difference |
| --- | --- | --- | --- |
| Decision tree | 65.22 | 91.89 | +26.67 |
| k-nearest neighbours | 55.89 | 77.22 | +21.33 |
| Support vector machine | 72.22 | 94.00 | +21.78 |
| Random forest | 82.78 | 97.22 | +14.44 |
| Multilayer perceptron | 72.89 | 95.56 | +22.67 |

### Table 6.4 Per-class F1, Random forest

| Class | Clean | 50 dB | 40 dB | 30 dB | 20 dB |
| --- | --- | --- | --- | --- | --- |
| C1 Normal | 0.784 | 0.784 | 0.784 | 0.805 | 0.758 |
| C2 Sag | 0.692 | 0.692 | 0.692 | 0.648 | 0.648 |
| C3 Swell | 0.898 | 0.898 | 0.927 | 0.927 | 0.927 |
| C4 Interruption | 0.783 | 0.783 | 0.783 | 0.761 | 0.789 |
| C5 Harmonics | 0.971 | 0.971 | 0.933 | 0.829 | 0.865 |
| C6 Flicker | 0.733 | 0.733 | 0.747 | 0.763 | 0.776 |
| C7 Oscillatory transient | 0.931 | 0.931 | 0.931 | 0.909 | 0.788 |
| C8 Notch | 0.848 | 0.848 | 0.848 | 0.876 | 0.871 |
| C9 Sag + harmonics | 0.899 | 0.899 | 0.883 | 0.841 | 0.781 |

### Table 6.5 Ten highest-ranked features

| Rank | Band | Descriptor | Mean importance |
| --- | --- | --- | --- |
| 1 | D5 | kurtosis | 0.0564 |
| 2 | D5 | entropy | 0.0531 |
| 3 | D4 | std | 0.0481 |
| 4 | D3 | mav | 0.0454 |
| 5 | D1 | kurtosis | 0.0368 |
| 6 | D1 | peak | 0.0366 |
| 7 | D3 | std | 0.0355 |
| 8 | D4 | mav | 0.0338 |
| 9 | D1 | entropy | 0.0327 |
| 10 | D4 | kurtosis | 0.0321 |

### Table 6.6 Sensitivity checks, Random forest, 30 dB

| Configuration | Accuracy (%) | Difference from baseline |
| --- | --- | --- |
| db4, 5 levels, 42 wavelet features (baseline) | 82.22 ± 5.72 | — |
| db10, 5 levels | 78.89 ± 4.51 | -3.33 |
| Time-domain features only (RMS, crest factor, THD) | 83.89 ± 4.08 | +1.67 |
