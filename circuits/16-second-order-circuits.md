# Module 16 — Second-Order Circuits and Oscillations

Two energy-storage elements — typically one L and one C — give a second-order
differential equation. Energy can now slosh back and forth between the magnetic
and electric fields, so the response can **oscillate**, which a first-order
circuit never does.

## 16.1 The series RLC circuit

KVL around a series RLC loop, source-free:

    L d²i/dt² + R di/dt + i/C = 0

Divide by L and write in standard form:

    d²i/dt² + 2α di/dt + ω_0² i = 0

with

    α = R/2L           neper frequency (damping), [Np/s]
    ω_0 = 1/√(LC)      undamped natural (resonant) frequency, [rad/s]

## 16.2 The parallel RLC circuit

For the parallel case the equation has the same form in v, but α differs:

    α = 1/(2RC)        ω_0 = 1/√(LC)

**Note the inversion.** In series, larger R means *more* damping. In parallel,
larger R means *less* damping. Getting these the wrong way round is the standard
error in this module — reason it out from where the energy is being lost.

## 16.3 The characteristic equation and the three cases

Assuming a solution e^{st}:

    s² + 2αs + ω_0² = 0
    s = −α ± √(α² − ω_0²)

The **damping ratio** ζ = α/ω_0 decides everything:

| Condition | Name | Roots | Response |
|---|---|---|---|
| α > ω_0 (ζ > 1) | **Overdamped** | two real, distinct | two decaying exponentials, no oscillation |
| α = ω_0 (ζ = 1) | **Critically damped** | two real, equal | fastest possible without overshoot |
| α < ω_0 (ζ < 1) | **Underdamped** | complex conjugates | damped oscillation (ringing) |
| α = 0 (ζ = 0) | Undamped | pure imaginary | sustained oscillation |

### The three solution forms

**Overdamped** (s_1, s_2 real):

    x(t) = A_1 e^{s_1 t} + A_2 e^{s_2 t}

**Critically damped** (s = −α twice):

    x(t) = (A_1 + A_2 t) e^{−αt}

**Underdamped** (s = −α ± jω_d, with the **damped frequency**
ω_d = √(ω_0² − α²)):

    x(t) = e^{−αt}(A_1 cos ω_d t + A_2 sin ω_d t)

The envelope is e^{−αt}, so α controls how fast the ringing dies and ω_d sets
the ringing frequency. Note ω_d < ω_0 always — damping slows the oscillation.

## 16.4 Finding the constants

Two constants need two initial conditions. Get them from the continuity rules:

1. **x(0⁺)** — from v_C(0⁻) or i_L(0⁻), which are continuous.
2. **dx/dt(0⁺)** — obtained from the *other* storage element, using
   i_C = C dv_C/dt or v_L = L di_L/dt at t = 0⁺.

That second step is where marks are lost. For a series RLC solving for v_C:

    dv_C/dt (0⁺) = i_L(0⁺)/C

because the inductor current is what charges the capacitor. For a parallel RLC
solving for i_L:

    di_L/dt (0⁺) = v_C(0⁺)/L

For a **step** response, add the forced term: x(t) = x(∞) + [transient form],
and apply the initial conditions to the *total*.

## 16.5 Practical meaning

- **Overdamped** — sluggish. A door closer set too stiff.
- **Critically damped** — the fastest approach with no overshoot. The design
  target for most control and instrument systems.
- **Underdamped** — fast but overshoots and rings. Acceptable when a little
  overshoot is cheaper than the extra settling time; unacceptable in, say, a
  measuring instrument's needle.

**Quality factor** for a resonant circuit:

    Q = ω_0/(2α)

Series RLC: Q = (1/R)√(L/C). Parallel RLC: Q = R√(C/L) — inverted again.
High Q means low damping, sharp resonance, long ringing.

## 16.6 Worked examples

**Example 1 — classify.** A series RLC has R = 40 Ω, L = 4 H, C = 0.25 F.

    α = R/2L = 40/8 = 5
    ω_0 = 1/√(LC) = 1/√(1) = 1

α > ω_0 ⇒ **overdamped**.

    s = −5 ± √(25 − 1) = −5 ± 4.899
    s_1 = −0.101,  s_2 = −9.899

    i(t) = A_1e^{−0.101t} + A_2e^{−9.899t}

**Example 2 — underdamped.** A series RLC has R = 6 Ω, L = 1 H, C = 0.04 F, with
i(0) = 0 and v_C(0) = 10 V. Find i(t).

    α = 6/2 = 3
    ω_0 = 1/√(0.04) = 5
    α < ω_0 ⇒ underdamped
    ω_d = √(25 − 9) = 4 rad/s

    i(t) = e^{−3t}(A_1 cos 4t + A_2 sin 4t)

Initial conditions. i(0) = 0 ⇒ A_1 = 0.
For di/dt(0⁺), use KVL at t = 0⁺: v_L = −v_C − iR = −10 − 0 = −10 V, so

    di/dt(0⁺) = v_L/L = −10 A/s

Differentiating i(t) = A_2 e^{−3t} sin 4t:

    di/dt = A_2[−3e^{−3t}sin4t + 4e^{−3t}cos4t]
    di/dt(0) = 4A_2 = −10   ⇒   A_2 = −2.5

    i(t) = −2.5 e^{−3t} sin 4t  A

The current rings at 4 rad/s inside a decaying envelope, dying out after about
5/α = 1.67 s.

**Example 3 — critical damping.** For L = 2 H and C = 0.5 F in series, find the
R that gives critical damping.

    ω_0 = 1/√(2 × 0.5) = 1
    Critical: α = ω_0 ⇒ R/2L = 1 ⇒ R = 2L = 4 Ω

**Example 4 — parallel RLC.** R = 5 Ω, L = 0.1 H, C = 0.01 F. Classify.

    α = 1/(2RC) = 1/(2 × 5 × 0.01) = 10
    ω_0 = 1/√(0.1 × 0.01) = 1/√(0.001) = 31.62

α < ω_0 ⇒ **underdamped**, ω_d = √(1000 − 100) = 30 rad/s.

Note that *increasing* R here would reduce α and make it ring more — the
opposite of the series case.

**Example 5 — step response.** The circuit of Example 3 (critically damped,
R = 4 Ω, L = 2 H, C = 0.5 F) is driven by a 10 V step, starting from rest. Find
v_C(t).

    v_C(∞) = 10 V  (capacitor open at DC)
    v_C(0⁺) = 0,   i_L(0⁺) = 0 ⇒ dv_C/dt(0⁺) = i_L(0⁺)/C = 0

    v_C(t) = 10 + (A_1 + A_2 t)e^{−t}

At t = 0:  0 = 10 + A_1 ⇒ A_1 = −10
dv_C/dt = A_2e^{−t} − (A_1 + A_2t)e^{−t}; at t = 0: A_2 − A_1 = 0 ⇒ A_2 = −10

    v_C(t) = 10 − 10(1 + t)e^{−t} V

No overshoot, as critical damping guarantees.

## 16.7 Exercises

1. Series RLC: R = 10 Ω, L = 0.5 H, C = 0.2 F. Find α, ω_0 and classify.
   (α = 10, ω_0 = 1, overdamped)
2. Find R for critical damping in a parallel RLC with L = 1 H, C = 0.25 F.
   (R = 1 Ω)
3. A circuit rings at 200 rad/s with an envelope decaying with τ = 50 ms. Find
   α, ω_d and ω_0. (α = 20, ω_d = 200, ω_0 = 201)
4. For Example 2, find v_C(t) and confirm it starts at 10 V.
5. Explain why increasing R damps a series RLC but undamps a parallel one.

## Takeaways

- α = R/2L (series) or 1/2RC (parallel); ω_0 = 1/√(LC) for both.
- Compare α with ω_0: over, critical, or underdamped.
- Underdamped ⇒ e^{−αt} envelope ringing at ω_d = √(ω_0² − α²) < ω_0.
- Two initial conditions: the continuous variable, and its derivative obtained
  from the *other* storage element.
