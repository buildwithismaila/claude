"""Wavelet and reference time-domain feature extraction.

Five-level DWT (db4 by default) gives six bands -- D1..D5 and A5 -- and seven
statistical descriptors are computed from each, for 42 features in total.
Band energies are normalised by total signal energy so the classifier responds
to how energy is distributed across bands rather than to record amplitude.

See manuscript section 4.
"""

import numpy as np
import pywt
from scipy import stats

from .signals import F0, FS

WAVELET = "db4"
LEVELS = 5

DESCRIPTORS = [
    "energy",
    "entropy",
    "std",
    "mav",
    "peak",
    "kurtosis",
    "skewness",
]

BAND_NAMES = ["D1", "D2", "D3", "D4", "D5", "A5"]


def band_descriptors(c: np.ndarray, total_energy: float) -> list[float]:
    """Seven descriptors of one band's coefficient vector."""
    energy = float(np.sum(c**2))
    # Shannon entropy of the normalised energy distribution within the band.
    p = c**2
    s = p.sum()
    if s <= 0:
        entropy = 0.0
    else:
        p = p / s
        nz = p[p > 0]
        entropy = float(-np.sum(nz * np.log2(nz)))
    return [
        energy / total_energy if total_energy > 0 else 0.0,
        entropy,
        float(np.std(c)),
        float(np.mean(np.abs(c))),
        float(np.max(np.abs(c))),
        float(stats.kurtosis(c)),
        float(stats.skew(c)),
    ]


def wavelet_features(x: np.ndarray, wavelet: str = WAVELET, levels: int = LEVELS):
    """42-dimensional wavelet feature vector for one signal."""
    coeffs = pywt.wavedec(x, wavelet, level=levels)
    # pywt returns [A5, D5, D4, D3, D2, D1]; reorder to D1..D5, A5.
    approx, details = coeffs[0], coeffs[1:]
    bands = list(reversed(details)) + [approx]
    total = float(sum(np.sum(b**2) for b in bands))
    feats: list[float] = []
    for b in bands:
        feats.extend(band_descriptors(b, total))
    return np.asarray(feats, dtype=float)


def wavelet_feature_names(levels: int = LEVELS) -> list[str]:
    names = []
    for band in BAND_NAMES[: levels + 1]:
        for d in DESCRIPTORS:
            names.append(f"{band}_{d}")
    return names


# ---------------------------------------------------------------------------
# Reference time-domain features (manuscript section 4.4)
# ---------------------------------------------------------------------------


def time_domain_features(x: np.ndarray) -> np.ndarray:
    """RMS, crest factor, and THD estimated from the magnitude spectrum."""
    rms = float(np.sqrt(np.mean(x**2)))
    peak = float(np.max(np.abs(x)))
    crest = peak / rms if rms > 0 else 0.0

    spec = np.abs(np.fft.rfft(x))
    freqs = np.fft.rfftfreq(len(x), 1.0 / FS)
    # Bin nearest the fundamental, and bins nearest harmonics 2..15.
    def bin_at(f):
        return int(np.argmin(np.abs(freqs - f)))

    fund = spec[bin_at(F0)]
    harm = np.array([spec[bin_at(k * F0)] for k in range(2, 16)])
    thd = float(np.sqrt(np.sum(harm**2)) / fund) if fund > 0 else 0.0
    return np.asarray([rms, crest, thd], dtype=float)


TIME_FEATURE_NAMES = ["rms", "crest_factor", "thd"]


def extract(X: np.ndarray, wavelet: str = WAVELET, levels: int = LEVELS):
    """Wavelet features for a stack of signals."""
    return np.vstack([wavelet_features(x, wavelet, levels) for x in X])


def extract_time(X: np.ndarray):
    return np.vstack([time_domain_features(x) for x in X])
