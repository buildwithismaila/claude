# Module 21 — Transfer Functions, Poles, Zeros and Stability

## 21.1 Definition

For a circuit at rest (all initial conditions zero), the **transfer function** is
the ratio of output transform to input transform:

    H(s) = Y(s)/X(s)

It is a property of the **circuit alone** — independent of what you drive it
with. That is what makes it useful: characterise the circuit once, then predict
its response to anything.

Four kinds, depending on what is input and output:

| H(s) | Name | Units |
|---|---|---|
| V_o/V_i | Voltage gain | — |
| I_o/I_i | Current gain | — |
| V_o/I_i | Transfer impedance | Ω |
| I_o/V_i | Transfer admittance | S |

Driving-point impedance Z(s) = V/I at a single port is a special case.

**Impulse response.** Since ℒ{δ(t)} = 1, driving with an impulse gives
Y(s) = H(s), so

    h(t) = ℒ⁻¹{H(s)}

The impulse response *is* the inverse transform of the transfer function. And
for any input, y(t) = h(t) * x(t) — convolution in time, multiplication in s.
That equivalence is the practical reason transforms are used at all.

## 21.2 Poles and zeros

Write H(s) as a ratio of polynomials and factor:

    H(s) = K (s − z_1)(s − z_2)… / [(s − p_1)(s − p_2)…]

- **Zeros** z_i: values of s where H(s) = 0 — the circuit blocks that frequency.
- **Poles** p_i: values of s where H(s) → ∞ — the circuit's natural frequencies.

**The poles determine the response shape**, entirely. Each pole contributes a
term to the time response:

| Pole location | Contributes | Behaviour |
|---|---|---|
| Real, negative (−a) | e^{−at} | decaying exponential |
| Real, positive (+a) | e^{+at} | growing — unstable |
| At origin (0) | constant | integrator |
| Complex pair (−α ± jω_d) | e^{−αt}cos(ω_d t + φ) | damped oscillation |
| Imaginary pair (±jω) | cos(ωt + φ) | sustained oscillation |
| Right-half complex pair | e^{+αt}cos(...) | growing oscillation — unstable |
| Repeated pole on the axis | t·(…) | grows — unstable |

Notice this reproduces Module 16's three cases exactly: overdamped = two real
poles, critically damped = repeated real pole, underdamped = complex pair. The
pole plot is the same information in a picture.

**Distance from the origin** sets the frequency; **distance left of the
imaginary axis** sets how fast it decays.

## 21.3 Stability

> A linear circuit is **stable** if and only if **every pole of H(s) lies
> strictly in the left half of the s-plane** (Re(p) < 0).

- All poles strictly left → **stable**. Every natural response decays; output
  stays bounded for bounded input (BIBO stable).
- Any pole strictly right → **unstable**. Response grows without limit.
- Simple (non-repeated) poles **on** the imaginary axis → **marginally stable**.
  Sustained oscillation, neither growing nor decaying. An ideal LC tank.
- **Repeated** poles on the imaginary axis → unstable (the t factor grows).

**Zeros do not affect stability.** They shape the response's amplitude and
phase, but they cannot make a stable circuit unstable. Only poles matter.

### Passive circuits are always stable

Any circuit made only of positive R, L and C cannot be unstable — there is no
source of energy to sustain growth, and any R guarantees poles move strictly
left. Instability requires an **active** element: a dependent source, an
amplifier, or feedback. This is why op-amp and transistor circuits need stability
analysis and a resistor network never does.

### Routh–Hurwitz test

To test stability without factoring the denominator, take the characteristic
polynomial a_n s^n + … + a_1 s + a_0.

**Necessary condition:** all coefficients present and of the same sign. If any
coefficient is zero or has the opposite sign, the system is **not** stable — and
this alone settles many exam questions immediately.

**Sufficient test:** build the Routh array; the number of sign changes in the
first column equals the number of right-half-plane poles. Zero sign changes
means stable.

For a second-order polynomial s² + a_1s + a_0, the necessary condition is also
sufficient: **stable ⟺ a_1 > 0 and a_0 > 0**.

## 21.4 Frequency response from H(s)

Set s = jω:

    H(jω) = |H(jω)| ∠φ(ω)

- |H(jω)| is the **magnitude response** — the gain at each frequency
- φ(ω) is the **phase response**

Gain in decibels: |H|_dB = 20 log₁₀|H(jω)|. The **cutoff (half-power)
frequency** is where |H| falls to 1/√2 = 0.707 of maximum, i.e. −3 dB, which is
where the output power halves.

Standard filter shapes, identified by where the zeros sit:

| Filter | H(s) shape | Passes |
|---|---|---|
| Low-pass | K/(s + a) | low frequencies |
| High-pass | Ks/(s + a) | high frequencies |
| Band-pass | Ks/(s² + as + b) | a band around ω_0 |
| Band-stop (notch) | K(s² + ω_0²)/(s² + as + b) | everything except ω_0 |

A zero at the origin blocks DC → high-pass. A zero at infinity (denominator of
higher degree) blocks high frequencies → low-pass.

## 21.5 Worked examples

**Example 1 — RC low-pass.**
R in series, C to ground, output across C.

    H(s) = (1/sC)/(R + 1/sC) = 1/(1 + sRC) = (1/RC)/(s + 1/RC)

One pole at s = −1/RC, no finite zeros. Stable (pole is left-half).

Cutoff: |H(jω)| = 1/√(1 + (ωRC)²) = 0.707 when ωRC = 1, so

    ω_c = 1/RC,   f_c = 1/(2πRC)

For R = 1 kΩ, C = 1 μF: f_c = 1/(2π × 10⁻³) = **159 Hz**.

**Example 2 — classify from poles.**

    H(s) = 10/(s² + 4s + 13)

    s = [−4 ± √(16 − 52)]/2 = −2 ± j3

Complex pair, real part −2 < 0 ⇒ **stable**, underdamped. Response rings at
3 rad/s inside an e^{−2t} envelope. Compare Module 16: α = 2, ω_d = 3,
ω_0 = √13 = 3.61.

**Example 3 — instability from a dependent source.**

    H(s) = K/(s² + (3 − K)s + 2)

For stability both coefficients must be positive: 2 > 0 always, and we need

    3 − K > 0   ⇒   K < 3

At K = 3 the poles sit on the imaginary axis at ±j√2 — marginally stable,
oscillating at √2 rad/s. Above K = 3 the circuit oscillates with growing
amplitude. This is exactly how an oscillator is designed: set the gain at the
boundary.

**Example 4 — band-pass.**

    H(s) = 20s/(s² + 20s + 10000)

Zero at s = 0 (blocks DC), poles from s² + 20s + 10⁴:

    ω_0 = √10000 = 100 rad/s,  2α = 20 ⇒ α = 10
    Q = ω_0/2α = 100/20 = 5

Peak gain at ω = ω_0 = 100 rad/s, where H(j100) = 20(j100)/(−10000 + j2000 +
10000) = 2000j/2000j = 1. Bandwidth = 2α = 20 rad/s.

**Example 5 — Routh necessary condition.**
Is s³ + 2s² − s + 5 stable?

The s coefficient is **negative** while the others are positive. A sign change
means at least one right-half-plane root ⇒ **unstable**. No further work needed.

## 21.6 Exercises

1. Find H(s) = V_o/V_i for an RL circuit with output across R. Identify the
   filter type. (sL-free: H = R/(R+sL), low-pass)
2. H(s) = (s+2)/[(s+1)(s+5)]. List poles and zeros and state stability.
3. For what K is H(s) = K/(s² + (K−4)s + 9) stable? (K > 4)
4. An RC high-pass has R = 10 kΩ, C = 10 nF. Find f_c. (1.59 kHz)
5. Explain why a circuit of positive R, L and C alone can never be unstable.

## Takeaways

- H(s) = output/input with zero initial conditions; h(t) = ℒ⁻¹{H(s)}.
- Poles set the response shape; zeros shape amplitude and phase only.
- Stable ⟺ all poles strictly in the left half plane.
- Passive RLC is always stable; instability needs an active element.
- s = jω converts the transfer function into the frequency response.
