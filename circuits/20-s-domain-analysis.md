# Module 20 — Circuit Analysis in the s-Domain

Rather than write a differential equation and transform it, transform the
**circuit itself**. Every technique from Modules 03–12 then works unchanged, in
algebra, with initial conditions built in.

## 20.1 s-domain impedances

| Element | Time domain | s-domain impedance |
|---|---|---|
| Resistor | v = Ri | Z = R |
| Inductor | v = L di/dt | Z = sL |
| Capacitor | i = C dv/dt | Z = 1/(sC) |

Compare with phasors (Module 17), where the same elements were R, jωL and
1/(jωC). **The s-domain is the generalisation:** set s = jω and you recover the
phasor method. Phasor analysis is the special case of s-domain analysis
restricted to the imaginary axis — that is, to steady-state sinusoids only. The
s-domain handles transients as well, because σ ≠ 0 is allowed.

## 20.2 Initial conditions as sources

This is what makes the method powerful. Non-zero initial conditions appear as
**additional sources** in the transformed circuit.

**Inductor with initial current i(0⁻):**
From ℒ{L di/dt} = sLI(s) − Li(0⁻):

- **Series form:** impedance sL in series with a voltage source **Li(0⁻)**,
  polarity aiding the original current.
- **Parallel form:** impedance sL in parallel with a current source
  **i(0⁻)/s**.

**Capacitor with initial voltage v(0⁻):**
From ℒ{C dv/dt} = sCV(s) − Cv(0⁻):

- **Series form:** impedance 1/(sC) in series with a voltage source
  **v(0⁻)/s**, polarity matching the original charge.
- **Parallel form:** impedance 1/(sC) in parallel with a current source
  **Cv(0⁻)**.

Use the series form with mesh analysis and the parallel form with nodal
analysis. Once these sources are drawn in, the circuit is purely algebraic and
every earlier technique applies.

## 20.3 The method

1. Redraw the circuit in the s-domain: R → R, L → sL, C → 1/(sC).
2. Add initial-condition sources for any L or C with non-zero initial state.
3. Transform the input sources (a step V becomes V/s, an impulse becomes a
   constant, and so on).
4. Solve for the unknown using **any** method — series/parallel, dividers,
   nodal, mesh, Thévenin, Norton, superposition. All remain valid with Z(s) in
   place of R.
5. Invert by partial fractions to get the time-domain answer.

The step that makes it worthwhile: you never write a differential equation, and
you never separately match initial conditions.

## 20.4 Worked examples

**Example 1 — RC step response, redone.**
A 12 V step through 2 kΩ onto an uncharged 500 μF capacitor. (Module 15,
Example 2 solved this classically.)

s-domain: source 12/s, impedances 2000 and 1/(500×10⁻⁶ s) = 2000/s.

Voltage divider:

    V_C(s) = (12/s) × [2000/s] / [2000 + 2000/s]
           = (12/s) × [2000/s] × [s/(2000s + 2000)]
           = (12/s) × 2000/(2000(s + 1))
           = 12/[s(s + 1)]

Partial fractions: 12/[s(s+1)] = 12/s − 12/(s+1)

    v_C(t) = 12(1 − e^{−t}) V ✓

Identical to Module 15, with no differential equation written.

**Example 2 — with an initial condition.**
A 2 H inductor carrying 6 A initially, in series with 4 Ω, is connected to a
12 V source at t = 0. (Module 15, Example 3.)

s-domain, series form: impedance 2s, initial-condition voltage source
Li(0⁻) = 2 × 6 = 12 V, and the input 12/s.

KVL around the loop:

    12/s + 12 = I(s)(2s + 4)
    I(s) = (12/s + 12)/(2s + 4) = (12 + 12s)/[s(2s + 4)]
         = 12(1 + s)/[2s(s + 2)] = 6(s + 1)/[s(s + 2)]

Partial fractions:

    A = 6(s+1)/(s+2) at s=0 = 6/2 = 3
    B = 6(s+1)/s at s=−2 = 6(−1)/(−2) = 3

    I(s) = 3/s + 3/(s+2)
    i(t) = 3 + 3e^{−2t} A ✓

Matches Module 15 exactly — but the initial condition entered as a source rather
than as a separate matching step.

**Example 3 — second order.**
A series RLC with R = 6 Ω, L = 1 H, C = 0.04 F, driven by a 10 V step from rest.
Find v_C(t).

s-domain impedances: 6, s, 25/s (since 1/0.04 = 25).

    V_C(s) = (10/s) × (25/s)/(6 + s + 25/s)

Multiply numerator and denominator by s:

    = (10/s) × 25/(s² + 6s + 25)
    = 250/[s(s² + 6s + 25)]

Complete the square: s² + 6s + 25 = (s+3)² + 16 = (s+3)² + 4²

Partial fractions:

    250/[s((s+3)²+16)] = A/s + (Bs + C)/((s+3)²+16)

    A = 250/25 = 10

Matching: 250 = 10[(s+3)²+16] + (Bs + C)s
        250 = 10s² + 60s + 250 + Bs² + Cs
    ⇒ 0 = (10 + B)s² + (60 + C)s
    ⇒ B = −10,  C = −60

    V_C(s) = 10/s − (10s + 60)/((s+3)² + 16)

Rewrite the numerator around (s+3): 10s + 60 = 10(s+3) + 30

    = 10/s − 10(s+3)/((s+3)²+4²) − (30/4)(4)/((s+3)²+4²)

    v_C(t) = 10 − 10e^{−3t}cos4t − 7.5e^{−3t}sin4t  V

Checks: at t = 0, 10 − 10 − 0 = 0 ✓ (uncharged). As t → ∞, v → 10 V ✓.
Underdamped with α = 3, ω_d = 4 — matching Module 16's classification for these
element values.

**Example 4 — Thévenin in the s-domain.**
Find the s-domain Thévenin equivalent seen by a capacitor 1/(sC), where the rest
of the network is a source V/s in series with R.

    V_th(s) = V/s,   Z_th(s) = R

so V_C(s) = (V/s)·[1/sC]/[R + 1/sC] = V/[s(sRC + 1)], giving the familiar
V(1 − e^{−t/RC}). Every DC theorem carries straight over.

**Example 5 — mesh analysis in the s-domain (from the lecture notes).**
A u(t) source drives a 1 Ω resistor into a node; a ⅓ F capacitor sits from that
node to ground; a 5 Ω resistor leads on to a 1 H inductor to ground. Output is
v_o(t) across the inductor. Zero initial conditions.

Transform everything:

    u(t) → 1/s,   1 H → sL = s,   ⅓ F → 1/(sC) = 3/s

Mesh 1 (source loop, sharing the capacitor branch), mesh 2 (right-hand loop):

    1/s = (1 + 3/s)I₁ − (3/s)I₂
    0   = −(3/s)I₁ + (s + 5 + 3/s)I₂

From the second equation:

    (3/s)I₁ = (s + 5 + 3/s)I₂   ⇒   I₁ = (1/3)(s² + 5s + 3)I₂

Substituting into the first and multiplying through by 3s:

    3 = (s + 3)(s² + 5s + 3)I₂ − 9I₂
      = (s³ + 8s² + 18s + 9)I₂ − 9I₂
      = (s³ + 8s² + 18s)I₂

    I₂ = 3/[s(s² + 8s + 18)]

The output is across the inductor, so V_o(s) = sL·I₂ = s·I₂:

    V_o(s) = 3/(s² + 8s + 18)

Complete the square: s² + 8s + 18 = (s + 4)² + 2 = (s + 4)² + (√2)²

    V_o(s) = (3/√2) · √2/[(s + 4)² + (√2)²]
    v_o(t) = (3/√2) e^{−4t} sin(√2 t)  V,   t ≥ 0
           = 2.121 e^{−4t} sin(1.414t)  V

Underdamped, α = 4, ω_d = √2 — and the √2 appearing as both the damped frequency
and the scaling factor is not a coincidence: the sine pair in the table carries
ω in its numerator, so you must divide by it to match.

**Example 6 — nodal analysis with a stored initial condition and an impulse
source (from the lecture notes).**
A source 10e^{−t}u(t) V feeds through 10 Ω to node v_o; a 10 Ω runs from v_o to
ground; a 0.1 F capacitor charged to v_C(0) = 5 V also runs to ground; and a
2δ(t) A current source injects into the node.

Transform each piece:

    10e^{−t}u(t) → 10/(s + 1)
    0.1 F → 1/(0.1s) = 10/s
    capacitor initial condition → parallel current source Cv(0⁻) = 0.1 × 5 = 0.5 A
    2δ(t) → 2  (the impulse transforms to a constant)

KCL at v_o, taking the two source currents as entering:

    [10/(s+1) − V_o]/10 − V_o/10 − V_o/(10/s) + 2 + 0.5 = 0

Multiply through by 10:

    10/(s+1) − V_o − V_o − sV_o + 25 = 0
    10/(s+1) + 25 = V_o(s + 2)

    V_o(s) = [10/(s+1) + 25]/(s + 2) = [10 + 25(s+1)]/[(s+1)(s+2)]
           = (25s + 35)/[(s+1)(s+2)]

Residues:

    A = (25s+35)/(s+2) at s = −1 = (−25+35)/1 = 10
    B = (25s+35)/(s+1) at s = −2 = (−50+35)/(−1) = 15

    V_o(s) = 10/(s+1) + 15/(s+2)
    v_o(t) = (10e^{−t} + 15e^{−2t}) u(t)  V

Check at t = 0: v_o(0⁺) = 25 V. That is **not** 5 V, and it should not be — the
impulse dumps charge into the capacitor instantaneously, so v_C jumps. This is
the one legitimate exception to "capacitor voltage cannot change abruptly"
(Module 13): an impulse of current is exactly the infinite current that the rule
otherwise forbids.

## 20.5 Why this replaces the classical method

| Classical (Modules 15–16) | s-domain |
|---|---|
| Write and solve a differential equation | Write algebra |
| Classify damping by hand | Poles tell you directly |
| Match initial conditions separately | Built in as sources |
| Awkward for switched or delayed inputs | e^{−as} handles any delay |
| Different method per circuit order | One method for all orders |

The classical method still matters for insight — knowing that α and ω_0 govern
the shape is more useful than a pile of algebra. But for actually getting the
answer, the s-domain wins as soon as the circuit gets past second order.

## 20.6 Exercises

1. A 10 V step is applied to a series RL circuit (R = 5 Ω, L = 1 H) from rest.
   Find i(t) via the s-domain. (2(1 − e^{−5t}) A)
2. A 1 F capacitor charged to 5 V discharges through 2 Ω. Solve in the s-domain.
   (2.5e^{−0.5t} A)
3. Draw both the series and parallel s-domain models of an inductor with
   i(0⁻) = 3 A and L = 0.5 H, labelling the source values. (1.5 V; 3/s A)
4. Find V_C(s) for a parallel RLC driven by an impulse current source.
5. Explain in one sentence how the s-domain reduces to the phasor method.

## Takeaways

- R → R, L → sL, C → 1/(sC), and initial conditions become sources.
- Every technique from Modules 03–12 works unchanged with Z(s).
- Phasor analysis is the s-domain with s = jω — steady state only.
- Solve by algebra, then invert by partial fractions.
