"""Synthetic power-quality disturbance signal generator.

Nine disturbance classes spanning the IEEE 1159 categories observable in a
10-cycle single-phase voltage record, plus one combination class.

IMPORTANT -- PARAMETER PROVENANCE
---------------------------------
The parametric forms and parameter ranges in CLASS_SPECS below follow the
conventional synthetic PQ signal models used widely in the classification
literature. They are NOT taken from a verified citation in this file.

Before the paper is submitted, every equation and every range here must be
checked line by line against the specific published source cited as [2] in
the manuscript, and against IEEE 1159 itself for the class definitions.
Where the cited source differs, the source wins and this file changes.

Signals are per-unit voltage, nominal amplitude 1.0.
"""

from dataclasses import dataclass

import numpy as np

# ---------------------------------------------------------------------------
# Sampling parameters (manuscript Table 3.1)
# ---------------------------------------------------------------------------

F0 = 50.0            # fundamental frequency, Hz
FS = 3200.0          # sampling frequency, Hz -> 64 samples/cycle
CYCLES = 10          # cycles per record
N = int(CYCLES * FS / F0)   # 640 samples
T = np.arange(N) / FS       # time vector, 200 ms

CLASS_NAMES = [
    "normal",
    "sag",
    "swell",
    "interruption",
    "harmonics",
    "flicker",
    "osc_transient",
    "notch",
    "sag_harmonics",
]
CLASS_LABELS = {
    "normal": "C1 Normal",
    "sag": "C2 Sag",
    "swell": "C3 Swell",
    "interruption": "C4 Interruption",
    "harmonics": "C5 Harmonics",
    "flicker": "C6 Flicker",
    "osc_transient": "C7 Oscillatory transient",
    "notch": "C8 Notch",
    "sag_harmonics": "C9 Sag + harmonics",
}


@dataclass(frozen=True)
class Window:
    """Disturbance onset and end, in seconds."""

    start: float
    end: float

    def mask(self, t: np.ndarray) -> np.ndarray:
        return (t >= self.start) & (t <= self.end)


def _draw_window(rng: np.random.Generator, min_cycles=1.0, max_cycles=9.0) -> Window:
    """Random onset and duration, both in whole-cycle terms, inside the record."""
    duration = rng.uniform(min_cycles, max_cycles) / F0
    latest_start = CYCLES / F0 - duration
    start = rng.uniform(0.0, max(latest_start, 0.0))
    return Window(start, start + duration)


# ---------------------------------------------------------------------------
# Per-class signal models
# ---------------------------------------------------------------------------
# Each builder returns (signal, params dict). phi is the randomised initial
# phase of the fundamental, drawn in generate_base() and shared by all classes
# so no class can be identified by phase alignment.


def _normal(rng, phi):
    return np.sin(2 * np.pi * F0 * T + phi), {}


def _sag(rng, phi, alpha_range=(0.1, 0.9)):
    alpha = rng.uniform(*alpha_range)
    w = _draw_window(rng)
    env = 1.0 - alpha * w.mask(T)
    return env * np.sin(2 * np.pi * F0 * T + phi), {
        "alpha": alpha,
        "start": w.start,
        "end": w.end,
    }


def _swell(rng, phi):
    alpha = rng.uniform(0.1, 0.8)
    w = _draw_window(rng)
    env = 1.0 + alpha * w.mask(T)
    return env * np.sin(2 * np.pi * F0 * T + phi), {
        "alpha": alpha,
        "start": w.start,
        "end": w.end,
    }


def _interruption(rng, phi):
    alpha = rng.uniform(0.9, 1.0)
    w = _draw_window(rng)
    env = 1.0 - alpha * w.mask(T)
    return env * np.sin(2 * np.pi * F0 * T + phi), {
        "alpha": alpha,
        "start": w.start,
        "end": w.end,
    }


def _harmonic_component(rng, phi):
    """3rd/5th/7th harmonics, amplitudes normalised so total power is 1 p.u."""
    a3, a5, a7 = rng.uniform(0.05, 0.15, size=3)
    a1 = np.sqrt(max(1.0 - (a3**2 + a5**2 + a7**2), 1e-9))
    sig = (
        a1 * np.sin(2 * np.pi * F0 * T + phi)
        + a3 * np.sin(3 * (2 * np.pi * F0 * T + phi))
        + a5 * np.sin(5 * (2 * np.pi * F0 * T + phi))
        + a7 * np.sin(7 * (2 * np.pi * F0 * T + phi))
    )
    return sig, {"a1": a1, "a3": a3, "a5": a5, "a7": a7}


def _harmonics(rng, phi):
    return _harmonic_component(rng, phi)


def _flicker(rng, phi):
    alpha = rng.uniform(0.1, 0.2)
    beta = rng.uniform(5.0, 20.0)   # modulation frequency, Hz
    env = 1.0 + alpha * np.sin(2 * np.pi * beta * T)
    return env * np.sin(2 * np.pi * F0 * T + phi), {"alpha": alpha, "beta": beta}


def _osc_transient(rng, phi):
    alpha = rng.uniform(0.1, 0.8)
    fn = rng.uniform(300.0, 900.0)        # transient frequency, Hz
    tau = rng.uniform(0.008, 0.040)       # decay time constant, s
    w = _draw_window(rng, min_cycles=0.5, max_cycles=3.0)
    m = w.mask(T)
    decay = np.zeros(N)
    decay[m] = np.exp(-(T[m] - w.start) / tau) * np.sin(2 * np.pi * fn * (T[m] - w.start))
    return np.sin(2 * np.pi * F0 * T + phi) + alpha * decay, {
        "alpha": alpha,
        "fn": fn,
        "tau": tau,
        "start": w.start,
        "end": w.end,
    }


def _notch(rng, phi):
    """Periodic notches: short zeroing of the waveform, twice per cycle."""
    depth = rng.uniform(0.4, 1.0)
    width_samples = int(rng.integers(2, 6))       # notch width in samples
    per_half_cycle = int(FS / (2 * F0))           # 32 samples
    offset = int(rng.integers(0, per_half_cycle - width_samples))
    sig = np.sin(2 * np.pi * F0 * T + phi)
    notch_mask = np.zeros(N, dtype=bool)
    for k in range(0, N, per_half_cycle):
        lo = k + offset
        notch_mask[lo : lo + width_samples] = True
    sig = sig * (1.0 - depth * notch_mask)
    return sig, {"depth": depth, "width": width_samples, "offset": offset}


def _sag_harmonics(rng, phi):
    base, hp = _harmonic_component(rng, phi)
    alpha = rng.uniform(0.1, 0.9)
    w = _draw_window(rng)
    env = 1.0 - alpha * w.mask(T)
    params = dict(hp)
    params.update({"alpha": alpha, "start": w.start, "end": w.end})
    return env * base, params


BUILDERS = {
    "normal": _normal,
    "sag": _sag,
    "swell": _swell,
    "interruption": _interruption,
    "harmonics": _harmonics,
    "flicker": _flicker,
    "osc_transient": _osc_transient,
    "notch": _notch,
    "sag_harmonics": _sag_harmonics,
}


# ---------------------------------------------------------------------------
# Noise
# ---------------------------------------------------------------------------

SNR_LEVELS = [None, 50.0, 40.0, 30.0, 20.0]   # None = clean


def add_awgn(x: np.ndarray, snr_db, rng: np.random.Generator) -> np.ndarray:
    """Additive white Gaussian noise at a target SNR, measured per signal."""
    if snr_db is None:
        return x.copy()
    power = float(np.mean(x**2))
    sigma2 = power / (10.0 ** (snr_db / 10.0))
    return x + rng.normal(0.0, np.sqrt(sigma2), size=x.shape)


# ---------------------------------------------------------------------------
# Dataset assembly
# ---------------------------------------------------------------------------


def generate_base(n_per_class: int, seed: int, amplitude=None):
    """Clean base signals.

    Returns (X, y, groups) where groups is the base-signal index. The group id
    is what keeps every noisy variant of one waveform inside a single CV fold.

    amplitude
        None (default) fixes the nominal amplitude at exactly 1.0 p.u., which
        is the convention used across the synthetic PQ literature. A (lo, hi)
        tuple instead draws the nominal amplitude uniformly per signal.

        This matters more than it looks. With amplitude fixed, the RMS of a
        record is a deterministic function of its class and disturbance depth
        -- normal and harmonics records both sit at exactly 0.7071 with zero
        variance -- so three elementary time-domain features can separate the
        classes almost as well as the full wavelet set. Real records carry no
        such guarantee. See the amplitude study in amplitude_study.py.
    """
    rng = np.random.default_rng(seed)
    X, y, groups = [], [], []
    gid = 0
    for name in CLASS_NAMES:
        build = BUILDERS[name]
        for _ in range(n_per_class):
            phi = rng.uniform(0.0, 2 * np.pi)
            sig, _params = build(rng, phi)
            if amplitude is not None:
                sig = rng.uniform(*amplitude) * sig
            X.append(sig)
            y.append(name)
            groups.append(gid)
            gid += 1
    return np.asarray(X), np.asarray(y), np.asarray(groups)


def generate_dataset(n_per_class: int = 200, seed: int = 20251021, amplitude=None):
    """Full dataset: every base signal at every noise condition.

    Returns X (n_samples, N), y (class names), groups (base-signal id),
    snr (noise condition per sample; np.nan for clean).
    """
    Xb, yb, gb = generate_base(n_per_class, seed, amplitude)
    rng = np.random.default_rng(seed + 1)
    X, y, groups, snrs = [], [], [], []
    for snr in SNR_LEVELS:
        for i in range(Xb.shape[0]):
            X.append(add_awgn(Xb[i], snr, rng))
            y.append(yb[i])
            groups.append(gb[i])
            snrs.append(np.nan if snr is None else snr)
    return (
        np.asarray(X),
        np.asarray(y),
        np.asarray(groups),
        np.asarray(snrs, dtype=float),
    )
