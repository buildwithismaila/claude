# Module 14 — Elementary Signals

This module follows the ELE 712 lecture notes closely. It is broader than a
circuits treatment of signals: it covers **discrete-time** signals, the full
catalogue of standard signals, the operations you can perform on them, and the
classification scheme — all of which the notes examine directly.

## 14.1 What a signal is

A signal is a **single-valued function of one or more independent variables that
carries information**. Usually the independent variable is time, but it may be
temperature, pressure or distance.

- **One-dimensional**: depends on one variable, e.g. x(t).
- **Two-dimensional**: depends on two, e.g. an image f(x, y).

**Continuous-time (CT)** signals are defined at every instant, written x(t).
**Discrete-time (DT)** signals are defined only at discrete instants, written
x(n), where n is an **integer**.

## 14.2 Four ways of representing a discrete-time signal

> **Why "discrete-time" and not just "signal".** This four-way list belongs
> specifically to **discrete-time** signals, and the lecture notes head the
> section the same way. The reason is the fourth entry: a *sequence* is a list
> of values at integer instants, and a continuous-time signal has no such list —
> it has a value at every instant, uncountably many. The first three do carry
> over (a continuous signal can be drawn, written as a formula, or sampled into
> a table), but only a discrete signal can be written out in full. So the
> heading is not a slip: four ways is a discrete-time count, and for continuous
> time it would be graphical and functional only.

Take the signal with
x(−2) = −3, x(−1) = 2, x(0) = 0, x(1) = 3, x(2) = 1, x(3) = 2.

**1. Graphical** — a **stem plot**: at each integer n, a vertical line of the
right height with a dot at its tip. The dots matter — they say the signal exists
*only* at the integers, and joining them with a continuous line would assert
something false about the instants in between.

@fig figures/sig-graphical.svg | Graphical representation of x(n) = {−3, 2, 0, 3, 1, 2}. The signal exists only at integer n; the stems and dots say so, and x(0) = 0 is a real value, not an absence.

**2. Tabular** — sampling instant against magnitude:

| n | −2 | −1 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|
| x(n) | −3 | 2 | 0 | 3 | 1 | 2 |

**3. Functional** — the amplitude written against the values of n:

```cases
lhs: x(n)  =
−3 ; n = −2
2 ; n = −1
0 ; n = 0
3 ; n = 1
1 ; n = 2
2 ; n = 3
```

or as a rule:

```cases
lhs: x(n)  =
3ⁿ ; n ≥ 0
0 ; n < 0
```

**4. Sequence** — list the values with an arrow marking n = 0:

@fig figures/sig-sequence.svg | The sequence representation. The arrow says which term sits at n = 0 — here the third, so the signal starts two samples before the origin.

**The arrow is not decoration.** If no arrow is shown, the convention is that
the **first term corresponds to n = 0**. Losing the arrow shifts the whole
signal, which changes every subsequent answer.

## 14.3 The standard signals

### (i) Unit step

```cases
lhs: u(t)  =
1 ; t ≥ 0
0 ; t < 0
```

Its usefulness: multiplying any signal by u(t) forces it to start at t = 0.

Shifted: u(t − a) switches on at t = a.

Discrete:

```cases
lhs: u(n)  =
1 ; n ≥ 0
0 ; n < 0
```

with the shifted version u(n − k) switching on at n = k.

@fig figures/sig-step-shift.svg | The unit step, and the same step delayed to t = a. Subtracting a from the argument moves the signal later — the opposite of what the minus sign suggests at first glance.

### (ii) Unit ramp

```cases
lhs: r(t)  =
t ; t ≥ 0
0 ; t < 0
```

or, compactly, r(t) = t·u(t).

Shifted: r(t − a) = (t − a)u(t − a).
Discrete:

```cases
lhs: r(n)  =
n ; n ≥ 0
0 ; n < 0
```

so r(n) = n·u(n), and r(n − k) = (n − k)u(n − k).

### (iii) Unit impulse (Dirac delta)

```cases
lhs: δ(t)  =
unbounded ; t = 0
0 ; t ≠ 0
```

    with      ∫_{−∞}^{∞} δ(t) dt = 1

> **A point of care.** The lecture notes write "δ(t) = 1 for t = 0". Read that
> as shorthand. The impulse is not *equal to 1* at the origin — it is unbounded
> there, and what equals 1 is its **area**. Everything the impulse does follows
> from the area, so keep that in mind whenever you use it.

Relationship to the step:

    δ(t) = du/dt        u(t) = ∫_{−∞}^{t} δ(τ) dτ

(Note the upper limit is **t**, not ∞; integrating to ∞ would just give 1.)

**Sifting property** — the property you actually use:

    ∫ f(t) δ(t − a) dt = f(a)

Discrete:

```cases
lhs: δ(n)  =
1 ; n = 0
0 ; n ≠ 0
```

and δ(n − k) = 1 at n = k, zero elsewhere. For the discrete
impulse the value at the origin genuinely **is** 1 — the CT and DT impulses are
different objects, and only the DT one is an ordinary function.

### (iv) Unit parabolic

```cases
lhs: p(t)  =
t²/2 ; t ≥ 0
0 ; t < 0
```

or, compactly, p(t) = (t²/2)u(t).

Shifted: p(t − a) = ((t−a)²/2)u(t − a).
Discrete:

```cases
lhs: p(n)  =
n²/2 ; n ≥ 0
0 ; n < 0
```

**The integration chain.** Each of these is the integral of the one before:

@fig figures/sig-chain.svg | The four singularity functions. Integrating moves right along the chain, differentiating moves left — so remembering any one of the four gives you the other three.

    δ(t)  →  u(t)  →  r(t)  →  p(t)
           ∫        ∫        ∫

and differentiating runs the other way:

    r(t) = dp/dt        u(t) = d²p/dt²        δ(t) = d³p/dt³

Knowing this chain means you only have to remember one transform of the four.

### (v) Sinusoidal

    x(t) = A sin(ωt + φ)

A = amplitude, ω = angular frequency (rad/s), φ = phase (rad),
T = 1/f = 2π/ω.

Discrete: x(n) = A sin(ωn + φ), with period N = 2πm/ω for integers N, m.

> **A discrete sinusoid is not automatically periodic.** For x(n) to repeat,
> ω must be a **rational multiple of 2π**. This has no continuous-time analogue
> — every CT sinusoid is periodic — and it is a favourite examination point.

### (vi) Real exponential

    x(t) = A e^{αt}

Three cases, decided entirely by α:

| α | Behaviour |
|---|---|
| α = 0 | constant for all time |
| α > 0 | grows exponentially |
| α < 0 | decays exponentially |

@fig figures/sig-exponential.svg | The real exponential Ae^(αt). The sign of α alone decides between a constant, unbounded growth, and decay toward zero.

Discrete: x(n) = αⁿ, with the same three cases governed by whether |α| is 1,
greater than 1, or less than 1.

### (vii) Complex exponential

    x(t) = A e^{st},   s = σ + jω
         = A e^{σt} e^{jωt}
         = A e^{σt}(cos ωt + j sin ωt)

This **single expression contains every signal above** as a special case:

| σ | ω | Result |
|---|---|---|
| 0 | 0 | constant |
| < 0 | 0 | decaying exponential |
| > 0 | 0 | growing exponential |
| 0 | ≠ 0 | pure sinusoid (constant amplitude) |
| < 0 | ≠ 0 | **damped sinusoid** |
| > 0 | ≠ 0 | growing oscillation |

@fig figures/sig-complex-exp.svg | The six cases of e^(st) with s = σ + jω. The dashed line is the envelope e^(σt): σ sets growth or decay, ω sets oscillation. This is the same table you meet again in Module 21 as pole locations.

That table is the reason the Laplace transform uses e^{st} rather than e^{jωt},
and it is exactly the pole-location table you will meet again in Module 21.
Learn it once here and Module 21 costs nothing.

Discrete: x(n) = aⁿe^{j(ω₀n + φ)} — sinusoid with constant envelope for a = 1,
growing for a > 1, decaying for a < 1.

### (viii) Rectangular pulse

A constant amplitude over a fixed duration, zero elsewhere:

```cases
lhs: rect(t/τ)  =
1 ; \|t\| ≤ τ/2
0 ; otherwise
```

Equivalently built from steps: u(t + τ/2) − u(t − τ/2).

Used throughout digital communications, radar and sampling theory.

### (ix) Signum

```cases
lhs: sgn(t)  =
+1 ; t > 0
0 ; t = 0
−1 ; t < 0
```

Extracts the sign of its argument. Related to the step by

    sgn(t) = 2u(t) − 1        u(t) = ½[1 + sgn(t)]

Used in signal processing to detect polarity, and in control systems where the
response to positive and negative error must differ.

### (x) Sinc

    sinc(t) = sin(t)/t,     −∞ < t < ∞

with sinc(0) = 1 (by the limit). It is **even**, oscillates with period 2π, and
decays as 1/t. It is the Fourier transform of a rectangular pulse — which is why
it governs everything about sampling and bandwidth (Module 22).

@fig figures/sig-rect-sgn-sinc.svg | Rectangular pulse, signum and sinc. The open circles on sgn(t) mark that the value at t = 0 is 0, belonging to neither branch.

## 14.4 Operations on signals

### Time shifting

    y(t) = x(t − t₀)

- t₀ **positive** → shift **right** → **delay**
- t₀ **negative** → shift **left** → **advance**

The sign trips people up: subtracting from t moves the signal *later*.

Discrete: y(n) = x(n − N), N an integer.

### Time reversal

    y(t) = x(−t)

A mirror image about the vertical axis. An **even** signal is unchanged by
reversal; an **odd** signal is negated.

### Time scaling

    y(t) = x(at)

- a > 1 → **compression** by a factor a (the signal happens faster)
- a < 1 → **expansion** by a factor a (slower)

Note the inversion: multiplying t by a *larger* number makes the signal
*shorter*. A useful check — x(2t) reaches whatever x(t) reached at t = 2 by the
time t = 1.

### Amplitude scaling

    y(t) = A x(t)

A > 1 is **amplification**, A < 1 is **attenuation**.

### Addition and multiplication

Both are performed **point by point**:

    y(t) = x₁(t) + x₂(t)        y(t) = x₁(t) · x₂(t)

Subtraction likewise. There is no shortcut — you evaluate at each instant.

@fig figures/sig-operations.svg | One signal under three operations. Delay moves it right; reversal mirrors it about the vertical axis; compression by 2 halves its width while keeping its height.

**Order matters** when shifting and scaling are combined. x(2t − 4) is *not*
the same as first scaling then shifting by 4. Safest method: always write it as
x(2(t − 2)) — factor out the coefficient of t — then read it as "compress by 2,
then delay by 2".

## 14.5 Classification of signals

### Continuous-time vs discrete-time
Defined at every instant, x(t); or only at integers, x(n).

### Deterministic vs random
**Deterministic** — no uncertainty in magnitude or phase at any instant; has a
regular pattern and can be written as a mathematical expression.
**Random** — uncertain, irregular, cannot be described by an equation. Noise is
the standard example.

### Periodic vs aperiodic

```cases
lhs: x(t)  =
x(t + T) for all t ; periodic
x(t + T) for no T ; aperiodic
```

Discrete: x(n) = x(n + N), with N an integer period.

### Energy and power signals

    Energy (CT):  E = ∫_{−∞}^{∞} |x(t)|² dt
    Energy (DT):  E = Σ_{n=−∞}^{∞} |x(n)|²

    Power (CT):   P = lim_{T→∞} (1/2T) ∫_{−T}^{T} |x(t)|² dt
    Power (DT):   P = lim_{N→∞} (1/(2N+1)) Σ_{n=−N}^{N} |x(n)|²

The classification:

```cases
lhs: x(t) is an
energy signal ; 0 < E < ∞, and then P = 0
power signal ; 0 < P < ∞, and then E = ∞
neither ; if both fail
```

**A signal cannot be both**, and some signals are neither. The rule of thumb:
signals that die away (pulses, decaying exponentials) are energy signals;
signals that persist forever (periodic signals, the step) are power signals.

### Even and odd signals

    Even (symmetric):      x(−t) = x(t)      — symmetric about the vertical axis
    Odd (antisymmetric):   x(−t) = −x(t)     — and necessarily x(0) = 0

cos is even; sin is odd. Same definitions for x(n).

**Every signal decomposes uniquely** into an even and an odd part:

    x(t) = x_e(t) + x_o(t)

with

    x_e(t) = ½[x(t) + x(−t)]
    x_o(t) = ½[x(t) − x(−t)]

> **Watch the sign in the odd part.** The lecture notes' derivation is correct —
> it reaches 2x_o(t) = x(t) − x(−t) — but the final boxed line is typed with a
> plus, for both the continuous and discrete cases. It must be a **minus**.
> Quick self-check: x_e + x_o should give back x(t), and with two plus signs it
> would give x(t) + x(−t) instead. Use the minus.

Discrete: x_e(n) = ½[x(n) + x(−n)], x_o(n) = ½[x(n) − x(−n)].

@fig figures/sig-even-odd.svg | Any signal splits uniquely into an even part, symmetric about the vertical axis, and an odd part, antisymmetric through the origin. Add the two right-hand plots point by point and the left-hand one comes back.

### Products of even and odd signals

| Product | Result |
|---|---|
| even × even | **even** |
| odd × odd | **even** |
| even × odd | **odd** |

The same rule as multiplying signs, which is exactly why it works: substitute
x(−t) for each factor and count the minus signs.

## 14.6 Worked examples

**Example 1 — express a pulse.** Write a 5 V pulse from t = 2 s to t = 6 s.

    v(t) = 5[u(t − 2) − u(t − 6)]

**Example 2 — sifting.** Evaluate ∫(t² + 3t)δ(t − 2)dt.

Substitute t = 2:  4 + 6 = **10**

**Example 3 — even and odd parts.** Find the even and odd parts of
x(t) = e^{−2t}u(t).

    x(−t) = e^{2t}u(−t)
    x_e(t) = ½[e^{−2t}u(t) + e^{2t}u(−t)]
    x_o(t) = ½[e^{−2t}u(t) − e^{2t}u(−t)]

Check at t = +1: x_e = ½e^{−2}, x_o = ½e^{−2}, sum = e^{−2} = x(1) ✓
Check at t = −1: x_e = ½e^{−2}, x_o = −½e^{−2}, sum = 0 = x(−1) ✓

**Example 4 — energy or power?** Classify x(t) = e^{−2t}u(t) and x(t) = 5u(t).

For e^{−2t}u(t):

    E = ∫₀^∞ e^{−4t} dt = [−e^{−4t}/4]₀^∞ = 1/4

Finite ⇒ **energy signal** (and P = 0).

For 5u(t):  E = ∫₀^∞ 25 dt = ∞, so compute power:

    P = lim (1/2T)∫₀^T 25 dt = lim 25T/2T = 12.5

Finite ⇒ **power signal**.

**Example 5 — combined operations.** Given x(t), sketch x(−2t + 4).

Write it as x(−2(t − 2)). Read right to left:
1. **Reverse** (the minus), 2. **compress** by 2, 3. **delay** by 2.

Check: the point where the argument is zero is t = 2, so whatever x did at its
own origin now happens at t = 2 ✓

**Example 6 — discrete periodicity.** Is x(n) = cos(3πn/5) periodic? What about
cos(3n)?

For cos(3πn/5): ω = 3π/5. Is ω/2π = 3/10 rational? **Yes** ⇒ periodic, with
N = 10 (the denominator).

For cos(3n): ω = 3, and 3/2π is **irrational** ⇒ **not periodic**, even though
the continuous version cos(3t) certainly is.

## 14.7 Exercises

1. Write the sequence representation of x(n) = {1, 4, 0, −2} with the arrow at
   n = 1, and give its tabular form.
2. Express a staircase: 0 V until t = 1, 3 V from 1 to 3, 7 V from 3 to 5,
   0 after. (3u(t−1) + 4u(t−3) − 7u(t−5))
3. Find the even and odd parts of x(t) = t + t² + t³.
   (x_e = t², x_o = t + t³)
4. Classify x(t) = 10cos(5t) as energy or power, and find the relevant value.
   (Power signal; P = 50)
5. Show sgn(t) = 2u(t) − 1 and hence write the ramp in terms of sgn.
6. Is x(n) = sin(πn/4) + cos(πn/6) periodic? If so find N. (Yes; N = 24)
7. Given x(t) nonzero only on 0 ≤ t ≤ 2, over what interval is x(3t − 6)
   nonzero? (2 ≤ t ≤ 8/3)

## Takeaways

- Four representations of a DT signal; the arrow marking n = 0 carries meaning.
- δ → u → r → p is an integration chain; remember one, derive the rest.
- e^{st} with s = σ + jω generates every elementary signal — and is the reason
  the Laplace transform looks the way it does.
- A discrete sinusoid is periodic only when ω is a rational multiple of 2π.
- Energy signals have finite E and zero P; power signals have finite P and
  infinite E; never both.
- x_e = ½[x(t) + x(−t)], x_o = ½[x(t) **−** x(−t)].
