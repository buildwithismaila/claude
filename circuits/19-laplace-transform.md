# Module 19 — The Laplace Transform

Modules 15 and 16 solved differential equations by recognising their form.
That stops working for anything more complicated. The Laplace transform converts
differential equations into **algebraic** ones, solves them by algebra, and
converts back. It also handles initial conditions automatically, which is its
real advantage over classical methods.

## 19.1 Definition

    F(s) = ℒ{f(t)} = ∫₀^∞ f(t) e^{−st} dt

with s = σ + jω a complex frequency. The lower limit is 0⁻, which is what allows
impulses at the origin to be captured.

The transform exists whenever the integral converges, which for all signals in
circuit theory it does for Re(s) large enough.

## 19.2 Transform pairs

| f(t), t ≥ 0 | F(s) |
|---|---|
| δ(t) | 1 |
| u(t) | 1/s |
| t | 1/s² |
| t^n | n!/s^{n+1} |
| e^{−at} | 1/(s+a) |
| t e^{−at} | 1/(s+a)² |
| sin ωt | ω/(s² + ω²) |
| cos ωt | s/(s² + ω²) |
| e^{−at} sin ωt | ω/((s+a)² + ω²) |
| e^{−at} cos ωt | (s+a)/((s+a)² + ω²) |
| tⁿe^{−at} | n!/(s+a)^{n+1} |
| sin(ωt + φ) | (s sin φ + ω cos φ)/(s² + ω²) |
| cos(ωt + φ) | (s cos φ − ω sin φ)/(s² + ω²) |

Those ten cover essentially every circuit problem. Note the pattern: **damping
shifts s to s + a** — compare rows 7–8 with 9–10.

## 19.3 Properties

| Property | Statement |
|---|---|
| Linearity | ℒ{af + bg} = aF(s) + bG(s) |
| **Differentiation** | ℒ{df/dt} = sF(s) − f(0⁻) |
| Second derivative | ℒ{d²f/dt²} = s²F(s) − sf(0⁻) − f′(0⁻) |
| **Integration** | ℒ{∫₀^t f dτ} = F(s)/s |
| Time shift | ℒ{f(t−a)u(t−a)} = e^{−as}F(s) |
| Frequency shift | ℒ{e^{−at}f(t)} = F(s+a) |
| Scaling | ℒ{f(at)} = (1/a)F(s/a) |
| Convolution | ℒ{f * g} = F(s)G(s) |
| **Frequency differentiation** | ℒ{t f(t)} = −dF(s)/ds |
| **Time periodicity** | ℒ{f(t)} = F₁(s)/(1 − e^{−sT}) |

**Scaling** in full: ℒ{f(at)} = (1/a)F(s/a). Substitute x = at in the defining
integral and the 1/a falls out of dx = a dt.

**Frequency differentiation** is the one to reach for whenever the time function
carries a factor of t:

    ℒ{t sin ωt} = −d/ds [ω/(s²+ω²)] = 2ωs/(s²+ω²)²

Repeat it for t², t³ and so on. This is far quicker than integrating by parts.

**Time periodicity.** If f(t) is periodic with period T, write it as the sum of
shifted copies of its **first period** f₁(t):

    f(t) = f₁(t) + f₁(t−T)u(t−T) + f₁(t−2T)u(t−2T) + …

Transforming term by term and using the time shift:

    F(s) = F₁(s)[1 + e^{−sT} + e^{−2sT} + …] = F₁(s)/(1 − e^{−sT})

using the geometric series 1 + x + x² + … = 1/(1−x). So you only ever transform
**one period** and divide.

### The full property table

| Property | f(t) | F(s) |
|---|---|---|
| Linearity | a₁f₁(t) + a₂f₂(t) | a₁F₁(s) + a₂F₂(s) |
| Time shift | f(t−a)u(t−a) | e^{−as}F(s) |
| Scaling | f(at) | (1/a)F(s/a) |
| Frequency shift | e^{−at}f(t) | F(s+a) |
| Time differentiation | df/dt | sF(s) − f(0⁻) |
| | d²f/dt² | s²F(s) − sf(0⁻) − f′(0⁻) |
| | dⁿf/dtⁿ | sⁿF(s) − s^{n−1}f(0⁻) − … − f^{(n−1)}(0⁻) |
| Frequency differentiation | t f(t) | −dF(s)/ds |
| Time periodicity | f(t) = f(t + nT) | F₁(s)/(1 − e^{−sT}) |
| Initial value | f(0⁺) | lim_{s→∞} sF(s) |
| Final value | f(∞) | lim_{s→0} sF(s) |

**The differentiation property is the whole point.** Differentiation in time
becomes multiplication by s, and the initial condition f(0⁻) appears
automatically as an additive term. Initial conditions stop being a separate step
— they are built into the algebra.

### Initial and final value theorems

    f(0⁺) = lim_{s→∞} sF(s)
    f(∞)  = lim_{s→0} sF(s)

The final value theorem is **only valid if f(t) actually settles** — that is, if
all poles of sF(s) are in the left half plane. Applying it to an oscillating or
growing response gives a confident wrong answer, and that is a favourite exam
trap.

## 19.4 The inverse transform by partial fractions

Circuit problems produce F(s) = N(s)/D(s), a ratio of polynomials. Factor D(s)
and split into simple terms, then read each back off the table.

**Case 1 — distinct real poles.**

    F(s) = k_1/(s+p_1) + k_2/(s+p_2) + …

with residues found by the cover-up rule:

    k_i = [(s + p_i) F(s)]  evaluated at  s = −p_i

**Case 2 — repeated poles.** For (s+p)^n, include terms
k_1/(s+p) + k_2/(s+p)² + … + k_n/(s+p)^n, with

    k_{n−m} = (1/m!) d^m/ds^m [(s+p)^n F(s)]  at  s = −p

**Case 3 — complex poles.** Either use conjugate residues, or (usually easier)
complete the square in the denominator and match the damped sine/cosine rows of
the table directly.

**Before you start:** if the degree of N(s) is ≥ that of D(s), divide out first.
Partial fractions require a proper fraction.

## 19.5 Worked examples

**Example 1 — transform a differential equation.**
Solve dy/dt + 3y = 6u(t) with y(0⁻) = 2.

Transform both sides:

    sY(s) − 2 + 3Y(s) = 6/s
    Y(s)(s + 3) = 6/s + 2
    Y(s) = 6/[s(s+3)] + 2/(s+3)

Partial fractions on the first term: 6/[s(s+3)] = A/s + B/(s+3)

    A = 6/(s+3) at s=0 = 2
    B = 6/s at s=−3 = −2

    Y(s) = 2/s − 2/(s+3) + 2/(s+3) = 2/s

    y(t) = 2u(t)

The initial condition happens to exactly equal the final value, so nothing
changes — a clean check that the algebra was right.

**Example 2 — distinct poles.**

    F(s) = (s + 4)/[(s + 1)(s + 3)]

    k_1 = (s+4)/(s+3) at s=−1 = 3/2 = 1.5
    k_2 = (s+4)/(s+1) at s=−3 = 1/(−2) = −0.5

    F(s) = 1.5/(s+1) − 0.5/(s+3)
    f(t) = 1.5e^{−t} − 0.5e^{−3t}

Check with the initial value theorem: f(0⁺) = lim sF(s) = 1, and
1.5 − 0.5 = 1 ✓

**Example 3 — complex poles by completing the square.**

    F(s) = 10/(s² + 4s + 29)

    s² + 4s + 29 = (s + 2)² + 25 = (s+2)² + 5²

Matching the damped-sine row with a = 2, ω = 5:

    F(s) = 2 × 5/[(s+2)² + 5²]
    f(t) = 2e^{−2t} sin 5t

**Example 4 — repeated pole.**

    F(s) = 4/[s(s + 2)²] = A/s + B/(s+2) + C/(s+2)²

    A = 4/(s+2)² at s=0 = 1
    C = 4/s at s=−2 = −2
    B: differentiate 4/s, giving −4/s², at s=−2 ⇒ −4/4 = −1

    F(s) = 1/s − 1/(s+2) − 2/(s+2)²
    f(t) = 1 − e^{−2t} − 2t e^{−2t}

Check the final value: lim_{s→0} sF(s) = 1, and as t → ∞ the exponentials vanish
leaving 1 ✓

**Example 5 — time shift.** Find ℒ{5u(t − 3)}.

    = 5e^{−3s}/s

Any delay becomes a factor e^{−as}. This is how switching at a time other than
zero is handled.

## 19.5a Transforming from the definition

The table is derived, not given. Being able to reproduce two or three entries
from the defining integral is examinable, and the method is always the same.

**u(t):**

    ℒ{u(t)} = ∫₀^∞ 1·e^{−st} dt = [−e^{−st}/s]₀^∞ = 0 − (−1/s) = 1/s

**e^{−at}u(t):**

    ℒ{e^{−at}} = ∫₀^∞ e^{−at}e^{−st} dt = ∫₀^∞ e^{−(s+a)t} dt
               = [−e^{−(s+a)t}/(s+a)]₀^∞ = 1/(s+a)

By the same working with +a, ℒ{e^{at}u(t)} = 1/(s − a).

**δ(t):** by the sifting property, ∫δ(t)e^{−st}dt = e^{−s(0)} = **1**.

**r(t) = t u(t):** integrate by parts with u = t, dv = e^{−st}dt:

    ℒ{t} = [−te^{−st}/s]₀^∞ + (1/s)∫₀^∞ e^{−st}dt = 0 + (1/s)(1/s) = 1/s²

**sin ωt:** use Euler, sin ωt = (e^{jωt} − e^{−jωt})/2j:

    ℒ{sin ωt} = (1/2j)[1/(s − jω) − 1/(s + jω)]
              = (1/2j)·[(s + jω) − (s − jω)]/(s² + ω²)
              = (1/2j)(2jω)/(s² + ω²) = ω/(s² + ω²)

The same route with cos ωt = (e^{jωt} + e^{−jωt})/2 gives s/(s² + ω²).

## 19.6 Exercises

1. Find ℒ{3e^{−2t} + 4 sin 5t}. (3/(s+2) + 20/(s²+25))
2. Invert F(s) = (2s + 5)/[(s+1)(s+4)]. (e^{−t} + e^{−4t})
3. Solve d²y/dt² + 5dy/dt + 6y = 0 with y(0) = 1, y′(0) = 0.
   (3e^{−2t} − 2e^{−3t})
4. Find the final value of F(s) = 10/[s(s+5)] and verify by inversion. (2)
5. Explain why the final value theorem fails for F(s) = ω/(s² + ω²).
6. Use frequency differentiation to find ℒ{t² sin 2t} and ℒ{t² cos 3t}.
7. Find the Laplace transform of the gate g(t) = 10[u(t−2) − u(t−3)].
   (10(e^{−2s} − e^{−3s})/s)
8. Find the initial and final values of H(s) = 20/[(s+3)(s²+8s+25)] without
   inverting. (Both zero.)

## Takeaways

- ℒ turns d/dt into ×s and ∫dt into ÷s, carrying initial conditions along
  automatically.
- Ten transform pairs cover the whole of circuit theory.
- Inversion is partial fractions; complete the square for complex poles.
- The final value theorem only applies when the response actually settles.
