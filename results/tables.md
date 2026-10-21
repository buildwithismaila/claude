### Table 6.1 Accuracy (%) by classifier and noise condition

| Classifier | Clean | 50 dB | 40 dB | 30 dB | 20 dB |
| --- | --- | --- | --- | --- | --- |
| Decision tree | 86.11 ± 1.15 | 86.17 ± 0.97 | 84.56 ± 0.85 | 79.06 ± 1.97 | 73.00 ± 1.63 |
| k-nearest neighbours | 76.11 ± 1.77 | 76.11 ± 1.37 | 74.06 ± 1.69 | 71.06 ± 1.45 | 66.22 ± 1.85 |
| Support vector machine | 92.39 ± 0.89 | 92.28 ± 0.95 | 91.28 ± 0.99 | 89.06 ± 1.27 | 86.39 ± 1.05 |
| Random forest | 93.72 ± 1.21 | 93.39 ± 1.03 | 92.56 ± 0.90 | 89.72 ± 1.45 | 86.06 ± 1.46 |
| Multilayer perceptron | 93.72 ± 0.92 | 93.67 ± 0.89 | 92.94 ± 0.72 | 90.17 ± 1.29 | 86.89 ± 0.71 |

### Table 6.2 Macro-averaged F1 by classifier and noise condition

| Classifier | Clean | 50 dB | 40 dB | 30 dB | 20 dB |
| --- | --- | --- | --- | --- | --- |
| Decision tree | 0.862 ± 0.011 | 0.863 ± 0.009 | 0.847 ± 0.008 | 0.789 ± 0.018 | 0.728 ± 0.017 |
| k-nearest neighbours | 0.765 ± 0.018 | 0.765 ± 0.014 | 0.744 ± 0.017 | 0.717 ± 0.013 | 0.675 ± 0.017 |
| Support vector machine | 0.924 ± 0.009 | 0.923 ± 0.010 | 0.913 ± 0.010 | 0.891 ± 0.013 | 0.865 ± 0.010 |
| Random forest | 0.937 ± 0.012 | 0.934 ± 0.010 | 0.925 ± 0.009 | 0.896 ± 0.015 | 0.860 ± 0.016 |
| Multilayer perceptron | 0.937 ± 0.009 | 0.937 ± 0.009 | 0.929 ± 0.007 | 0.902 ± 0.013 | 0.869 ± 0.007 |

### Table 6.3 Grouped versus random partitioning (overall accuracy, %)

| Classifier | Grouped CV (correct) | Random CV (biased) | Difference |
| --- | --- | --- | --- |
| Decision tree | 81.78 | 88.78 | +7.00 |
| k-nearest neighbours | 72.71 | 79.56 | +6.84 |
| Support vector machine | 90.28 | 96.16 | +5.88 |
| Random forest | 91.09 | 96.13 | +5.04 |
| Multilayer perceptron | 91.48 | 96.87 | +5.39 |

### Table 6.4 Per-class F1, Multilayer perceptron

| Class | Clean | 50 dB | 40 dB | 30 dB | 20 dB |
| --- | --- | --- | --- | --- | --- |
| C1 Normal | 0.961 | 0.961 | 0.952 | 0.900 | 0.819 |
| C2 Sag | 0.836 | 0.833 | 0.837 | 0.829 | 0.805 |
| C3 Swell | 0.980 | 0.972 | 0.949 | 0.914 | 0.908 |
| C4 Interruption | 0.837 | 0.831 | 0.839 | 0.848 | 0.827 |
| C5 Harmonics | 0.968 | 0.968 | 0.963 | 0.946 | 0.935 |
| C6 Flicker | 0.972 | 0.970 | 0.938 | 0.903 | 0.839 |
| C7 Oscillatory transient | 0.970 | 0.975 | 0.975 | 0.951 | 0.892 |
| C8 Notch | 0.957 | 0.962 | 0.956 | 0.901 | 0.881 |
| C9 Sag + harmonics | 0.955 | 0.957 | 0.954 | 0.924 | 0.915 |

### Table 6.5 Ten highest-ranked features

| Rank | Band | Descriptor | Mean importance |
| --- | --- | --- | --- |
| 1 | D1 | kurtosis | 0.0527 |
| 2 | D3 | mav | 0.0479 |
| 3 | D5 | kurtosis | 0.0437 |
| 4 | D5 | entropy | 0.0436 |
| 5 | D1 | entropy | 0.0424 |
| 6 | D1 | peak | 0.0406 |
| 7 | D4 | std | 0.0363 |
| 8 | D3 | std | 0.0355 |
| 9 | D2 | std | 0.0344 |
| 10 | D1 | std | 0.0332 |

### Table 6.6 Sensitivity checks, Multilayer perceptron, 30 dB

| Configuration | Accuracy (%) | Difference from baseline |
| --- | --- | --- |
| db4, 5 levels, 42 wavelet features (baseline) | 90.17 ± 1.29 | — |
| db10, 5 levels | 90.67 ± 1.11 | +0.50 |
| Time-domain features only (RMS, crest factor, THD) | 91.94 ± 0.75 | +1.78 |
