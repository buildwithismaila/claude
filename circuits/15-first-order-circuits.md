# Module 15 — First-Order Circuits

A circuit containing **one** energy-storage element (one C or one L) plus
resistors is first order: its behaviour is governed by a first-order
differential equation, and its response is always a single exponential.

## 15.1 Source-free (natural) response

### RC circuit

A capacitor charged to V_0 discharges through R. KCL:

    C dv/dt + v/R = 0    ⇒    dv/dt + v/(RC) = 0

Solving:

    v(t) = V_0 e^{−t/τ},     τ = RC

### RL circuit

An inductor carrying I_0 decays through R. KVL:

    L di/dt + Ri = 0

    i(t) = I_0 e^{−t/τ},     τ = L/R

### The time constant

    τ_RC = RC        τ_RL = L/R

Both have units of seconds. Larger τ means slower response.

**Finding R for τ:** R is the **Thévenin resistance seen by the storage
element** — remove C or L, look back into the remaining network with independent
sources deactivated, and reduce. This is the direct pay-off of Module 09, and is
why the theorems came first.

## 15.2 Step (complete) response

When a DC source is switched in at t = 0, the response is the natural response
plus a forced (steady-state) term. Rather than solve the differential equation
every time, use:

> **The general first-order formula**
>
>     x(t) = x(∞) + [x(0⁺) − x(∞)] e^{−t/τ}

where x is **v_C for a capacitive circuit** or **i_L for an inductive one** —
the continuous variable.

This single equation solves every first-order problem. You need three numbers.

## 15.3 The three-step method

**Step 1 — find x(0⁺), the initial value.**
Analyse the circuit *before* switching (at t = 0⁻), in DC steady state:
capacitor → open, inductor → short. Read off v_C(0⁻) or i_L(0⁻). By continuity
(Module 13), x(0⁺) = x(0⁻).

**Step 2 — find x(∞), the final value.**
Analyse the circuit *after* switching, again in DC steady state with C open and
L short.

**Step 3 — find τ.**
With the source deactivated, find R_th seen from the terminals of C or L. Then
τ = R_th C or L/R_th.

Substitute into the formula. Done.

**Other quantities.** Once you have v_C(t) or i_L(t), get anything else from it:
i_C = C dv_C/dt, v_L = L di_L/dt, and resistor quantities by Ohm's law. Do **not**
apply the formula directly to a resistor current — it is not continuous and its
initial value is not the pre-switch value.

## 15.4 Worked examples

**Example 1 — RC natural response.**
A 100 μF capacitor charged to 20 V discharges through 5 kΩ. Find v(t), the
current at t = 0⁺, and the time to fall to 5 V.

    τ = RC = 5000 × 100×10⁻⁶ = 0.5 s
    v(t) = 20e^{−2t} V
    i(0⁺) = v/R = 20/5000 = 4 mA

For v = 5 V:

    5 = 20e^{−2t}  ⇒  e^{−2t} = 0.25  ⇒  −2t = ln 0.25 = −1.386
    t = 0.693 s

(Note that is exactly τ ln 4; falling to half takes τ ln 2 = 0.347 s.)

**Example 2 — RC step response.**
A 12 V source is switched at t = 0 through 2 kΩ onto an uncharged 500 μF
capacitor. Find v_C(t) and the time to reach 10 V.

    v_C(0⁺) = 0        (uncharged)
    v_C(∞) = 12 V      (capacitor open, no current, no drop across R)
    τ = 2000 × 500×10⁻⁶ = 1 s

    v_C(t) = 12 + (0 − 12)e^{−t} = 12(1 − e^{−t}) V

For 10 V: 10/12 = 1 − e^{−t} ⇒ e^{−t} = 1/6 ⇒ t = ln 6 = **1.79 s**

**Example 3 — RL step response with a pre-existing current.**
A 2 H inductor is in series with 4 Ω across a 24 V source, in steady state. At
t = 0 the source is replaced by a 12 V source. Find i(t).

    i(0⁺) = i(0⁻) = 24/4 = 6 A
    i(∞) = 12/4 = 3 A
    τ = L/R = 2/4 = 0.5 s

    i(t) = 3 + (6 − 3)e^{−2t} = 3 + 3e^{−2t} A

Check: at t = 0, i = 6 A ✓; as t → ∞, i → 3 A ✓

**Example 4 — R_th found by Thévenin.**
A 10 V source in series with 6 Ω feeds a node; from that node a 3 Ω goes to
ground and a 200 μF capacitor also goes to ground. The switch closes at t = 0
with the capacitor uncharged. Find v_C(t).

    v_C(0⁺) = 0
    v_C(∞): capacitor open, divider  =  10 × 3/(6+3) = 3.333 V
    τ: deactivate the source; capacitor sees 6 ∥ 3 = 2 Ω
       τ = 2 × 200×10⁻⁶ = 0.4 ms

    v_C(t) = 3.333(1 − e^{−2500t}) V

**Example 5 — finding a non-continuous quantity.**
For Example 4, find the current through the 3 Ω resistor at t = 0⁺ and t = ∞.

At t = 0⁺ the capacitor is uncharged, so it behaves momentarily as a **short**:
the node is held at 0 V, so i_3(0⁺) = 0. All the source current goes into the
capacitor.

At t = ∞ the capacitor is open: i_3 = 3.333/3 = 1.111 A.

Note i_3 jumps from 0 to a final 1.111 A — resistor currents *may* be
discontinuous. Only v_C and i_L may not.

## 15.5 Two useful special cases

**An uncharged capacitor at t = 0⁺ acts as a short circuit** (v = 0).
**An inductor with zero initial current at t = 0⁺ acts as an open circuit**
(i = 0).

These give you the instantaneous-after-switching circuit directly, which is how
you find initial values of currents and voltages that are *not* continuous.

## 15.6 Exercises

1. A 50 μF capacitor discharges through 20 kΩ from 100 V. Find τ, v(t), and v at
   t = 2 s. (1 s; 100e^{−t}; 13.5 V)
2. An RL circuit has L = 0.5 H, R = 250 Ω, switched onto 50 V from rest. Find
   τ and i(t). (2 ms; 0.2(1 − e^{−500t}) A)
3. A capacitor charges to 63.2% of its final value in 15 ms. Find τ and the time
   to reach 99%. (15 ms; 69 ms)
4. For Example 3, find v_L(t) and confirm it is zero in steady state.
   (−12e^{−2t} V)
5. Why must you never apply the general formula directly to a resistor's current?

## Takeaways

- One storage element ⇒ one exponential, one time constant.
- x(t) = x(∞) + [x(0⁺) − x(∞)]e^{−t/τ}, applied to **v_C or i_L only**.
- τ = R_th C or L/R_th, with R_th the Thévenin resistance seen by the element.
- Initial value from the pre-switch steady state, final value from the
  post-switch steady state, both with C open and L short.
