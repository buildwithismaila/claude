# Module 22 — Fourier Series and Transforms

Laplace handles transients from switching. Fourier answers a different question:
**what frequencies is a signal made of, and what does the circuit do to each?**

## 22.1 Fourier series — periodic signals

Any periodic signal f(t) with period T (satisfying the mild Dirichlet
conditions) can be written as a sum of sinusoids at multiples of the fundamental
ω_0 = 2π/T:

    f(t) = a_0 + Σ_{n=1}^∞ [a_n cos nω_0 t + b_n sin nω_0 t]

with coefficients

    a_0 = (1/T)∫_T f(t) dt                    (the DC or average value)
    a_n = (2/T)∫_T f(t) cos(nω_0 t) dt
    b_n = (2/T)∫_T f(t) sin(nω_0 t) dt

**Amplitude–phase form**, usually more useful:

    f(t) = a_0 + Σ A_n cos(nω_0 t + φ_n)
    A_n = √(a_n² + b_n²)        φ_n = −tan⁻¹(b_n/a_n)

n = 1 is the **fundamental**, n ≥ 2 the **harmonics**.

### Symmetry shortcuts — use these before integrating

| Symmetry | Condition | Consequence |
|---|---|---|
| **Even** | f(−t) = f(t) | all b_n = 0 (cosines only) |
| **Odd** | f(−t) = −f(t) | a_0 = 0 and all a_n = 0 (sines only) |
| **Half-wave** | f(t ± T/2) = −f(t) | all **even** harmonics vanish |

Checking symmetry first can halve or quarter the work. A square wave that is odd
and half-wave symmetric has only odd sine harmonics — three of the four
coefficient families are zero before you integrate anything.

### Exponential form

    f(t) = Σ_{n=−∞}^{∞} c_n e^{jnω_0 t},    c_n = (1/T)∫_T f(t)e^{−jnω_0 t} dt

with c_0 = a_0 and c_n = (a_n − jb_n)/2. Compact, and the natural bridge to the
Fourier transform.

### Standard series worth knowing

**Square wave**, amplitude A, odd, half-wave symmetric:

    f(t) = (4A/π)[sin ω_0t + (1/3)sin 3ω_0t + (1/5)sin 5ω_0t + …]

Odd harmonics only, amplitudes falling as 1/n.

**Sawtooth**, amplitude A, odd:

    f(t) = (2A/π)[sin ω_0t − (1/2)sin 2ω_0t + (1/3)sin 3ω_0t − …]

All harmonics, falling as 1/n.

**Triangular wave**: odd harmonics falling as 1/n² — much faster, which is why a
triangle sounds far less harsh than a square.

**The general rule:** the smoother the waveform, the faster its harmonics decay.
Discontinuities give 1/n; corners give 1/n².

## 22.2 Circuit analysis with Fourier series

This is where superposition (Module 07) earns its keep. Because each harmonic is
a different frequency, you **must** treat them separately:

1. Decompose the input into its harmonics.
2. Evaluate the circuit's response **at each harmonic frequency** — remember
   impedance depends on ω, so Z is different for every n.
3. Compute each harmonic's output using phasor methods.
4. **Add the time-domain results.**

The DC term (n = 0) is handled with L shorted and C opened.

**Average power with harmonics:**

    P = V_dc I_dc + Σ_n (V_n I_n/2) cos θ_n

Only harmonics **present in both** voltage and current contribute. Different
harmonics are orthogonal, so cross terms vanish — which is exactly why you may
add powers here but not in Module 07's superposition (there it was one frequency
in two parts; here it is genuinely different frequencies).

**RMS with harmonics:**

    F_rms = √(F_dc² + Σ (F_n²/2))

for amplitude coefficients F_n.

**Total harmonic distortion:**

    THD = √(Σ_{n≥2} F_n²) / F_1

## 22.3 The Fourier transform — aperiodic signals

Let T → ∞ and the discrete harmonic lines merge into a continuous spectrum:

    F(ω) = ∫_{−∞}^{∞} f(t) e^{−jωt} dt
    f(t) = (1/2π)∫_{−∞}^{∞} F(ω) e^{jωt} dω

**Relationship to Laplace.** For a causal signal, F(ω) = F(s)|_{s=jω}. The
Fourier transform is the Laplace transform evaluated on the imaginary axis — the
same restriction that turns s-domain analysis into phasor analysis (Module 20).

The difference in use:

| | Laplace | Fourier |
|---|---|---|
| Signals | causal, t ≥ 0 | any, including t < 0 |
| Handles growing signals | yes (σ ≠ 0) | no |
| Initial conditions | built in | not handled |
| Best for | transients, switching | steady-state spectra, filtering |

### Common pairs

| f(t) | F(ω) |
|---|---|
| δ(t) | 1 |
| 1 | 2πδ(ω) |
| e^{−at}u(t) | 1/(a + jω) |
| u(t) | πδ(ω) + 1/jω |
| cos ω_0t | π[δ(ω−ω_0) + δ(ω+ω_0)] |
| rect pulse of width τ | τ sinc(ωτ/2) |

Note the reciprocal relationship in the last row: a **narrow** pulse in time has
a **wide** spectrum, and vice versa. A perfect impulse contains all frequencies
equally; a perfect DC level contains only ω = 0. This is the time–bandwidth
trade-off, and it is why fast switching generates broadband interference.

### Properties

Linearity; time shift f(t−a) ⟷ e^{−jωa}F(ω); frequency shift; scaling
(compress in time ⇒ stretch in frequency); and convolution
f * g ⟷ F(ω)G(ω).

**Parseval's theorem** — energy is the same computed either way:

    ∫|f(t)|² dt = (1/2π)∫|F(ω)|² dω

## 22.4 Worked examples

**Example 1 — coefficients of a square wave.**
A square wave of amplitude 10 V, period 2 s, odd symmetry. Find the first three
non-zero terms.

    ω_0 = 2π/2 = π rad/s
    Odd ⇒ a_n = 0, a_0 = 0
    b_n = 4A/(nπ) for odd n = 40/(nπ)

    b_1 = 40/π = 12.73
    b_3 = 40/3π = 4.24
    b_5 = 40/5π = 2.55

    f(t) ≈ 12.73 sin πt + 4.24 sin 3πt + 2.55 sin 5πt + …

Note the fundamental's amplitude (12.73 V) **exceeds** the square wave's own
amplitude (10 V). That is correct, not an error — the harmonics subtract near
the peaks.

**Example 2 — harmonic response.**
The square wave of Example 1 drives an RC low-pass with R = 1 Ω, C = 1 F
(ω_c = 1 rad/s). Find the output amplitude of the first and third harmonics.

    |H(jω)| = 1/√(1 + ω²)

    n=1: ω = π = 3.142 ⇒ |H| = 1/√(1+9.87) = 0.303 ⇒ 12.73 × 0.303 = 3.86 V
    n=3: ω = 3π = 9.425 ⇒ |H| = 1/√(1+88.8) = 0.1055 ⇒ 4.24 × 0.1055 = 0.45 V

The third harmonic is attenuated far more than the first — the filter is
smoothing the square wave toward a sinusoid, which is exactly what a low-pass
filter does to a switching waveform.

**Example 3 — RMS with harmonics.**
A voltage has a 10 V DC component plus harmonics of amplitude 6 V and 4 V. Find
the RMS value.

    V_rms = √(10² + 6²/2 + 4²/2) = √(100 + 18 + 8) = √126 = 11.22 V

**Example 4 — THD.**
A waveform has a fundamental amplitude of 100 V with harmonics 20 V, 10 V, 5 V.

    THD = √(20² + 10² + 5²)/100 = √(400+100+25)/100 = √525/100
        = 22.91/100 = 22.9%

**Example 5 — Fourier transform of a decaying exponential.**

    f(t) = 5e^{−3t}u(t)
    F(ω) = 5/(3 + jω)
    |F(ω)| = 5/√(9 + ω²)

Maximum 5/3 at DC, falling to 0.707 of that at ω = 3 rad/s — the same −3 dB
point as the corresponding filter.

## 22.5 Exercises

1. A waveform is even and half-wave symmetric. Which coefficients survive?
2. Find a_0 for a sawtooth rising linearly from 0 to 10 V over each period.
   (5 V)
3. A signal has fundamental 50 V and third harmonic 15 V. Find RMS and THD.
   (36.9 V; 30%)
4. Find the Fourier transform of 2e^{−4t}u(t) and its magnitude at ω = 4.
   (2/(4+jω); 0.354)
5. Explain why a square wave fed to a good low-pass filter emerges nearly
   sinusoidal.

## Takeaways

- Fourier series decomposes a periodic signal into harmonics of ω_0.
- Check even/odd/half-wave symmetry **before** integrating.
- Each harmonic sees a different impedance — solve separately, add in time.
- Powers of different harmonics **do** add (they are orthogonal); this does not
  contradict Module 07.
- The Fourier transform is Laplace on the imaginary axis; narrow in time means
  wide in frequency.
