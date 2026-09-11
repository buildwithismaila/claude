# Module 14 — Elementary Signals

Before analysing how a circuit responds, you need a vocabulary of the inputs
used to probe it. These few functions generate almost every test signal in
circuit theory, and their transforms (Module 19) are the building blocks of
everything after.

## 14.1 The unit step

    u(t) = 0   for t < 0
    u(t) = 1   for t ≥ 0

The mathematical model of a switch closing at t = 0. A source Vu(t) means "V
volts, applied from t = 0 onward".

**Shifted:** u(t − a) switches on at t = a.
**Scaled and shifted:** Au(t − a) is a step of height A at t = a.

**Building pulses.** A rectangular pulse of height A from t = a to t = b is

    A[u(t − a) − u(t − b)]

Any piecewise-constant waveform can be written as a sum of shifted steps. This is
the standard trick for expressing a complicated switching waveform as one
formula.

**Gate function:** u(t − a) − u(t − b) is often written as a gate of width b − a.

## 14.2 The unit ramp

    r(t) = t·u(t)        i.e.  0 for t < 0,  t for t ≥ 0

The ramp is the **integral** of the step:

    r(t) = ∫u(τ)dτ        and       dr/dt = u(t)

A ramp of slope m starting at t = a is m·r(t − a) = m(t − a)u(t − a).

## 14.3 The unit impulse (Dirac delta)

    δ(t) = 0 for t ≠ 0,   and   ∫δ(t)dt = 1

An infinitely tall, infinitely narrow spike of unit **area**. Not a function in
the ordinary sense — it is defined entirely by what it does inside an integral.

**Relationship to the step:**

    δ(t) = du/dt        u(t) = ∫δ(τ)dτ

So the family is a differentiation chain:

    impulse → step → ramp → parabola
        (each is the integral of the one before)

**The sifting property** — the only property you actually use:

    ∫ f(t) δ(t − a) dt = f(a)

The impulse "picks out" the value of f at the point where it sits. This is what
makes impulse response and convolution work.

**Physical meaning.** A voltage impulse delivers a finite amount of charge in
zero time. It is an idealisation, but a narrow pulse behaves like one whenever
its width is far shorter than the circuit's time constant.

## 14.4 The exponential

    f(t) = Ae^{−t/τ} u(t)

τ is the **time constant** — the time for the signal to fall to 1/e = 36.8% of
its initial value.

| Elapsed time | Fraction remaining | Fraction of final value reached (rising) |
|---|---|---|
| 1τ | 36.8% | 63.2% |
| 2τ | 13.5% | 86.5% |
| 3τ | 5.0% | 95.0% |
| 4τ | 1.8% | 98.2% |
| 5τ | 0.7% | 99.3% |

**Engineering convention: after 5τ the transient is over.** That is the rule used
to decide settling times throughout Modules 15–16.

The rising form is A(1 − e^{−t/τ}), approaching A from below.

## 14.5 The sinusoid

    f(t) = A cos(ωt + φ)

- A = amplitude, ω = 2πf = angular frequency (rad/s), φ = phase (rad or degrees)
- Period T = 2π/ω = 1/f

**Damped sinusoid** — the signature of a second-order circuit (Module 16):

    f(t) = Ae^{−αt} cos(ω_d t + φ)

α is the damping factor, ω_d the damped frequency. This single expression
describes every ringing, overshooting circuit you will meet.

**Complex exponential.** By Euler's identity,

    e^{jθ} = cos θ + j sin θ
    cos θ = (e^{jθ} + e^{−jθ})/2
    sin θ = (e^{jθ} − e^{−jθ})/2j

Writing sinusoids as complex exponentials is what makes phasors (Module 17) and
Fourier analysis (Module 22) possible. The generalised form e^{st} with
s = σ + jω covers *all* of these signals at once — constant, exponential,
sinusoid, damped sinusoid — depending on where s sits in the complex plane. That
observation is the seed of the Laplace transform.

## 14.6 Signal properties worth naming

**Periodic:** f(t + T) = f(t) for all t.

**RMS value** of a periodic signal:

    F_rms = √( (1/T)∫₀^T f²(t) dt )

For a sinusoid, F_rms = A/√2. For a square wave of amplitude A, F_rms = A.
RMS matters because it is the value that produces the same heating in a resistor
as an equal DC value — which is why power is always computed with RMS.

**Average (DC) value:**

    F_avg = (1/T)∫₀^T f(t) dt

Zero for a pure sinusoid; A/2 for a sawtooth from 0 to A.

**Causal:** f(t) = 0 for t < 0. Every signal in circuit analysis is causal,
which is why every expression carries a u(t).

## 14.7 Worked examples

**Example 1.** Express a pulse of 5 V from t = 2 s to t = 6 s.

    v(t) = 5[u(t − 2) − u(t − 6)]

**Example 2.** Evaluate ∫(t² + 3t)δ(t − 2)dt.

By sifting, substitute t = 2:

    = 2² + 3(2) = 10

**Example 3.** A signal decays from 20 V with τ = 4 ms. Find v at t = 4 ms and
t = 12 ms, and the settling time.

    v(4 ms) = 20e⁻¹ = 7.36 V
    v(12 ms) = 20e⁻³ = 0.996 V
    Settling (5τ) = 20 ms

**Example 4.** Write the staircase: 0 V until t = 1, 3 V from 1 to 3, 7 V from
3 to 5, 0 after.

    v(t) = 3u(t−1) + 4u(t−3) − 7u(t−5)

Check at t = 4: 3 + 4 = 7 ✓. At t = 6: 3 + 4 − 7 = 0 ✓

**Example 5.** Find the RMS value of a sinusoid of amplitude 170 V, and identify
where you have seen that number.

    V_rms = 170/√2 = 120.2 V

That is the North American mains supply — nominally 120 V RMS, 170 V peak.

## 14.8 Exercises

1. Sketch and write an expression for a triangular pulse rising from 0 to 4 V
   over 0 ≤ t ≤ 2 then falling to 0 at t = 4.
2. Evaluate ∫ cos(πt) δ(t − 1) dt. (−1)
3. A capacitor voltage rises as 12(1 − e^{−t/0.5}) V. Find v at t = 0.5 s and
   the time to reach 90% of final. (7.58 V; 1.15 s)
4. Find the RMS value of a square wave alternating between +6 V and −6 V. (6 V)
5. Express δ(t) as the limit of a rectangular pulse and explain why its area
   must stay at 1.

## Takeaways

- Step, ramp, impulse form a differentiation chain; steps build any switching
  waveform.
- The impulse is defined by sifting: ∫f(t)δ(t−a)dt = f(a).
- Time constant τ: 63% in 1τ, effectively finished at 5τ.
- e^{st} with s = σ + jω unifies every elementary signal — and becomes the
  Laplace transform.
