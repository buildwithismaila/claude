# Module 27 — ELE 712 Assignments and Class Problems, Solved

Everything here is from the ELE 712 teaching materials issued so far: the
*Elementary Signals* notes, the *Dynamic Circuit Behaviour* slides, and the
handwritten *Laplace and Fourier Transform* notes (Nigerian Defence Academy,
Department of Electrical and Electronic Engineering).

The lecturer sets three numbered assignments plus several problems marked "Try
this!!!" and "Practice problem". All are worked in full below. Do them on paper
first — they are the clearest statement available of what he expects.

---

## Part A — Assignment 1

**A1.** Find the Laplace transform of f(t) = cos ωt · u(t).

Work from the definition, using Euler's formula
cos ωt = (e^{jωt} + e^{−jωt})/2:

    ℒ{cos ωt} = ∫₀^∞ [(e^{jωt} + e^{−jωt})/2] e^{−st} dt
              = ½ ∫₀^∞ [e^{−(s−jω)t} + e^{−(s+jω)t}] dt
              = ½ { [−e^{−(s−jω)t}/(s−jω)]₀^∞ + [−e^{−(s+jω)t}/(s+jω)]₀^∞ }
              = ½ [ 1/(s−jω) + 1/(s+jω) ]
              = ½ · [(s+jω) + (s−jω)] / [(s−jω)(s+jω)]
              = ½ · 2s/(s² + ω²)

    ℒ{cos ωt} = s/(s² + ω²)

The sine version in the notes differs only in having a minus between the two
exponentials and a 2j in the denominator, which is what turns the numerator into
ω instead of s.

---

## Part B — Assignment 2 (frequency differentiation)

The property is ℒ{t f(t)} = −dF(s)/ds, so ℒ{t² f(t)} = d²F(s)/ds².

**B1.** f(t) = t² sin 2t · u(t).

Start from F(s) = ℒ{sin 2t} = 2/(s² + 4).

First derivative:

    dF/ds = 2 · d/ds (s² + 4)⁻¹ = 2 · (−1)(s² + 4)⁻²(2s) = −4s/(s² + 4)²

Second derivative, by the quotient rule on −4s(s² + 4)⁻²:

    d²F/ds² = −4(s² + 4)⁻² + (−4s)(−2)(s² + 4)⁻³(2s)
            = −4/(s² + 4)² + 16s²/(s² + 4)³

Put over a common denominator (s² + 4)³:

    = [−4(s² + 4) + 16s²]/(s² + 4)³
    = (−4s² − 16 + 16s²)/(s² + 4)³

    ℒ{t² sin 2t} = (12s² − 16)/(s² + 4)³

Check by initial value: sF(s) → 0 as s → ∞ (degree 3 top, degree 6 bottom) ✓,
consistent with t²sin2t starting at zero.

**B2.** f(t) = t² cos 3t · u(t).

Start from F(s) = s/(s² + 9).

    dF/ds = [(s² + 9) − s(2s)]/(s² + 9)² = (9 − s²)/(s² + 9)²

Differentiate again, quotient rule with numerator (9 − s²) and denominator
(s² + 9)²:

    d²F/ds² = [(−2s)(s² + 9)² − (9 − s²)·2(s² + 9)(2s)]/(s² + 9)⁴

Cancel one factor of (s² + 9):

    = [(−2s)(s² + 9) − 4s(9 − s²)]/(s² + 9)³
    = (−2s³ − 18s − 36s + 4s³)/(s² + 9)³

    ℒ{t² cos 3t} = (2s³ − 54s)/(s² + 9)³ = 2s(s² − 27)/(s² + 9)³

---

## Part C — Assignment 3 (Fourier)

**C1.** Discuss the properties of the Fourier transform.

| Property | f(t) | F(ω) |
|---|---|---|
| Linearity | a f(t) + b g(t) | a F(ω) + b G(ω) |
| Time shift | f(t − t₀) | e^{−jωt₀}F(ω) |
| Frequency shift | e^{jω₀t}f(t) | F(ω − ω₀) |
| Scaling | f(at) | (1/\|a\|)F(ω/a) |
| Time reversal | f(−t) | F(−ω) |
| Duality | F(t) | 2πf(−ω) |
| Differentiation | df/dt | jωF(ω) |
| Integration | ∫f dt | F(ω)/jω + πF(0)δ(ω) |
| Convolution | f * g | F(ω)G(ω) |
| Multiplication | f(t)g(t) | (1/2π)F(ω) * G(ω) |
| Parseval | ∫\|f\|²dt | (1/2π)∫\|F\|²dω |

Two are worth dwelling on. **Scaling** says compressing in time stretches in
frequency — the time–bandwidth trade-off. **Duality** says the transform is
almost its own inverse, which is why a rectangular pulse gives a sinc and a sinc
gives a rectangle.

**C2.** Compare the Fourier and Laplace transforms.

| | Laplace | Fourier |
|---|---|---|
| Kernel | e^{−st}, s = σ + jω | e^{−jωt} |
| Limits | 0⁻ to ∞ (one-sided) | −∞ to ∞ (two-sided) |
| Signals | causal, t ≥ 0 | any, including t < 0 |
| Growing signals | handled (σ chosen to converge) | not handled |
| **Initial conditions** | **built in as sources** | **cannot be represented** |
| Gives | complete response (transient + steady state) | steady-state / spectrum |
| Best for | switching, transients, stability | filtering, spectra, bandwidth |
| Relationship | — | F(ω) = F(s)\|_{s=jω} for a causal, stable f |

The last row is the key one: the Fourier transform is the Laplace transform
evaluated on the imaginary axis. Everything Fourier can do, Laplace can do;
Fourier's advantage is that ω has a direct physical meaning as frequency, which
makes it the natural language for spectra and filters.

**C3.** Write short notes on two RC and two RL oscillators.
*(From the slides' oscillator assignment.)*

**RC oscillators** — use resistor–capacitor phase shift to meet the Barkhausen
condition (loop gain 1, loop phase 0° or 360°):

- **Phase-shift oscillator.** Three cascaded RC sections, each contributing 60°,
  give the 180° needed alongside an inverting amplifier. Frequency
  f = 1/(2πRC√6), and the amplifier must supply a gain of at least 29 to
  overcome the network's attenuation.
- **Wien bridge oscillator.** A series RC and a parallel RC form a
  frequency-selective divider with **zero** phase shift at f = 1/(2πRC), where
  the attenuation is exactly ⅓. A non-inverting amplifier of gain 3 sustains
  oscillation. Low distortion, easily tuned — the standard audio-frequency
  oscillator.

**LC oscillators** — use a resonant tank, generally at much higher frequencies
than RC types:

- **Hartley oscillator.** A tapped inductor (or two inductors L₁, L₂) with one
  capacitor. f = 1/(2π√(L_T C)) with L_T = L₁ + L₂ + 2M. Feedback comes from the
  inductive tap; easy to tune over a wide band.
- **Colpitts oscillator.** The dual: one inductor with a tapped capacitor pair
  C₁, C₂ in series, so f = 1/(2π√(LC_eq)) with C_eq = C₁C₂/(C₁ + C₂). More
  stable at high frequency than Hartley because stray capacitance is absorbed
  into C₁ and C₂ rather than shifting the tuning.

(The assignment says "RL oscillators"; in practice these are LC types — an
inductor alone cannot set a frequency without a capacitor, and the tank is
always LC.)

---

## Part D — "Try this!!!" problems

**D1.** Show that ℒ{e^{at}u(t)} = 1/(s − a).

    ∫₀^∞ e^{at}e^{−st} dt = ∫₀^∞ e^{−(s−a)t} dt = [−e^{−(s−a)t}/(s−a)]₀^∞
                          = 0 − (−1/(s−a)) = 1/(s − a)

(Convergence requires Re(s) > a — the transform of a growing exponential exists,
which is exactly what Fourier could not manage.)

**D2.** Find f(t) for F(s) = 6(s + 2)/[(s + 1)(s + 3)(s + 4)].

Three distinct poles, so use the cover-up rule:

    A = 6(s+2)/[(s+3)(s+4)] at s = −1 = 6(1)/[(2)(3)] = 1
    B = 6(s+2)/[(s+1)(s+4)] at s = −3 = 6(−1)/[(−2)(1)] = 3
    C = 6(s+2)/[(s+1)(s+3)] at s = −4 = 6(−2)/[(−3)(−1)] = −4

    F(s) = 1/(s+1) + 3/(s+3) − 4/(s+4)
    f(t) = (e^{−t} + 3e^{−3t} − 4e^{−4t}) u(t)

Check the initial value: f(0⁺) = 1 + 3 − 4 = 0, and lim sF(s) as s → ∞ = 0 ✓

**D3.** Find g(t) for G(s) = (10s² + 4)/[s(s + 1)(s + 2)²].

A repeated pole, so the expansion is

    G(s) = A/s + B/(s+1) + C/(s+2) + D/(s+2)²

    A = (10s²+4)/[(s+1)(s+2)²] at s = 0 = 4/[(1)(4)] = 1
    B = (10s²+4)/[s(s+2)²] at s = −1 = 14/[(−1)(1)] = −14
    D = (10s²+4)/[s(s+1)] at s = −2 = 44/[(−2)(−1)] = 22

For C, differentiate (s+2)²G(s) = (10s²+4)/[s(s+1)] and evaluate at s = −2.
With numerator N = 10s²+4 and denominator D = s²+s:

    d/ds (N/D) = (20s·D − N·(2s+1))/D²
    At s = −2:  D = 4−2 = 2,  N = 44,  2s+1 = −3
    = (20(−2)(2) − 44(−3))/4 = (−80 + 132)/4 = 52/4 = 13

    C = 13

So

    G(s) = 1/s − 14/(s+1) + 13/(s+2) + 22/(s+2)²
    g(t) = [1 − 14e^{−t} + 13e^{−2t} + 22t e^{−2t}] u(t)

Check the final value: lim_{s→0} sG(s) = 4/[(1)(4)] = 1, and as t → ∞ every
exponential term vanishes leaving 1 ✓

**D4 (Practice problem).** A switch moves from position a to position b at
t = 0. In position a, a current source I₀ has been feeding an R–L branch long
enough to reach steady state; in position b, a voltage source V₀ drives the same
R and L. Find i(t) for t > 0.

At t = 0⁻ the inductor is a short in DC steady state, so all of I₀ flows in it:

    i(0⁻) = I₀ = i(0⁺)     (inductor current is continuous)

For t > 0, in the s-domain with the series initial-condition source Li(0⁻):

    V₀/s + LI₀ = I(s)(R + sL)
    I(s) = [V₀/s + LI₀]/(R + sL) = V₀/[s(R + sL)] + LI₀/(R + sL)

Take the first term: V₀/[sL(s + R/L)] → partial fractions give
(V₀/R)[1/s − 1/(s + R/L)]. The second term is I₀/(s + R/L).

    i(t) = (V₀/R)(1 − e^{−Rt/L}) + I₀e^{−Rt/L}
         = V₀/R + (I₀ − V₀/R) e^{−Rt/L}

which is exactly the general first-order formula of Module 15,
x(t) = x(∞) + [x(0⁺) − x(∞)]e^{−t/τ}, with τ = L/R. The s-domain and classical
methods agree, as they must.

---

## Part E — Notation and a few things to watch

### The lecturer's symbols vs this course

| Meaning | Lecture notes | Here |
|---|---|---|
| Laplace operator | ∠[f(t)] (handwritten script L) | ℒ{f(t)} |
| Impulse | ∂(t) in the typed notes, δ(t) in the handwritten | δ(t) |
| Complex frequency | s = σ + jω | same |
| Angular frequency | w, ω₀, W₀ | ω, ω₀ |
| Fourier operator | ℱ | ℱ |
| Discrete index | n | n |

### Three arithmetic slips worth knowing about

These are in the issued materials. The **methods and final answers are sound**;
it is the transcription that slipped, and each is the kind of thing that costs
marks if copied straight into an exam.

**1. The odd-part formula.** The *Elementary Signals* notes derive
2x_o(t) = x(t) − x(−t) correctly, then type the boxed result with a plus:
"x_o(t) = ½[x(t) + x(−t)]". It must be a **minus**, for both the continuous and
discrete forms. Self-check: x_e + x_o must return x(t).

**2. Millis for micros in the LC examples.** Three slide examples state
milli-units but their stated answers correspond to micro-units:

| Slide example | As printed | Gives | Stated answer | Consistent with |
|---|---|---|---|---|
| Radio tuner | L = 1 mH, C = 3.18 pF | 2.82 MHz | 89.3 MHz | L = 1 **μ**H |
| LC period | L = 40 mH, C = 4 mF | ω = 79 rad/s | ω = 2500 rad/s | C = 4 **μ**F |
| Peak charge | L = 1 mH, C = 10 mF | ω = 316 rad/s | ω = 10⁴ rad/s | C = 10 **μ**F |

So the **answers** on those slides are right and the unit prefixes in the
questions are mistyped. Work them with μ and everything lines up — including the
radio example, which then lands on 89.25 MHz and picks out option (b), WRKF
89.3.

**3. A dropped power of s.** In the handwritten mesh example (page 17), I₂ is
written as 3/(s² + 8s² + 18s) where the working gives 3/(s³ + 8s² + 18s). The
very next line, V_o = sI₂ = 3/(s² + 8s + 18), is correct — so it is a copying
slip, not a method error.

### Where the notes go beyond this course, and vice versa

**In the notes, expanded here:** the *Elementary Signals* chapter is a
signals-and-systems treatment — discrete-time representation, the full signal
catalogue, signal operations, and classification. Module 14 now follows it
closely.

**In this course, not yet in the notes:** three-phase circuits (Module 18),
two-port networks (Module 23), computer-aided analysis (Module 24), and the
network theorems (Modules 07–12). All four are named in the ELE 712 syllabus, so
expect notes on them later in the semester; treat those modules as running ahead
of the lectures.

---

## Self-check

If you can do Parts A–D unaided, you are level with the course as taught so far.
The three places students lose marks in this material, on the evidence of what
the notes emphasise:

1. **Sign and prefix discipline** — the odd-part minus, the m/μ distinction.
2. **Partial fractions with repeated poles** — Part D3 is the pattern; the
   derivative step for the non-highest power is what gets skipped.
3. **Knowing which transform to reach for** — Laplace when there are initial
   conditions or switching, Fourier when the question is about spectrum or
   steady state.
