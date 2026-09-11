# Module 13 — Capacitors and Inductors

Everything up to here has been resistive, so nothing in the circuit had any
memory. Capacitors and inductors **store energy**, which means their behaviour
depends on the past, not just the present. That is what makes the rest of this
course — transients, oscillations, transforms — necessary.

## 13.1 The capacitor

Two conductors separated by a dielectric. Charge q accumulates in proportion to
voltage:

    q = Cv          C in farads (F)

Differentiating, and this is the defining relation:

    i = C dv/dt

**Read it carefully.** Current flows only when voltage is *changing*. Under DC
steady state dv/dt = 0, so i = 0: a capacitor is an **open circuit to DC**.

The inverse relation:

    v(t) = (1/C)∫i dt + v(t_0)

**Energy stored:**

    w = ½Cv²        [J]

The energy is in the electric field between the plates. A capacitor never
dissipates — it returns everything it stores.

### The continuity rule

> **The voltage across a capacitor cannot change instantaneously.**

Because i = C dv/dt, a step change in v would require infinite current. So
v_C(0⁺) = v_C(0⁻) — the voltage just after switching equals the voltage just
before. This one fact supplies the initial condition for every transient problem
in Modules 15 and 16.

(The exception is an idealised circuit where a capacitor is switched directly
across a voltage source or another capacitor with no resistance. That produces an
impulse of current, and real circuits avoid it — the wiring's own resistance
saves you.)

### Combinations

Capacitors combine **opposite to resistors**:

    Series:   1/C_eq = 1/C_1 + 1/C_2 + …
    Parallel: C_eq = C_1 + C_2 + …

In parallel the plate areas add, so capacitance adds. In series the effective
separation adds, so capacitance falls.

## 13.2 The inductor

A coil of wire. Flux linkage is proportional to current, and Faraday's law gives:

    v = L di/dt        L in henries (H)

**Current flows freely under DC** (di/dt = 0 ⇒ v = 0): an inductor is a **short
circuit to DC**.

    i(t) = (1/L)∫v dt + i(t_0)

**Energy stored:**

    w = ½Li²        [J]

stored in the magnetic field.

### The continuity rule

> **The current through an inductor cannot change instantaneously.**

A step in i would demand infinite voltage. So i_L(0⁺) = i_L(0⁻).

This is why opening a switch on an inductive load produces an arc: the circuit
tries to force di/dt to be huge, and v = L di/dt becomes enormous. Relay coils
get a flyback diode for exactly this reason.

### Combinations

Inductors combine **like resistors**:

    Series:   L_eq = L_1 + L_2 + …
    Parallel: 1/L_eq = 1/L_1 + 1/L_2 + …

## 13.3 The duality table

Capacitor and inductor are exact duals. Learn one column and the other follows.

| | Capacitor | Inductor |
|---|---|---|
| Defining relation | i = C dv/dt | v = L di/dt |
| Stores energy in | electric field | magnetic field |
| Energy | ½Cv² | ½Li² |
| Cannot change instantly | **voltage** | **current** |
| At DC | open circuit | short circuit |
| Series | 1/C_eq = Σ1/C_k | L_eq = ΣL_k |
| Parallel | C_eq = ΣC_k | 1/L_eq = Σ1/L_k |
| Impedance | 1/(jωC) | jωL |

The whole of duality in circuits is this swap: v ↔ i, C ↔ L, R ↔ G, series ↔
parallel, Thévenin ↔ Norton, node ↔ mesh.

## 13.4 DC steady state — a shortcut worth having

After all transients have died away in a DC circuit:

- Replace every **capacitor with an open circuit**
- Replace every **inductor with a short circuit**

What remains is a purely resistive network you can solve with Modules 03–06.
This gives you the *final* values for transient problems, and is often a whole
exam question on its own.

## 13.5 Worked examples

**Example 1.** A 10 μF capacitor has v(t) = 50 sin(200t) V. Find i(t) and the
peak energy stored.

    i = C dv/dt = 10×10⁻⁶ × 50 × 200 cos(200t) = 0.1 cos(200t) A

Current **leads** voltage by 90°, as expected for a capacitor.

    w_max = ½Cv_max² = ½(10×10⁻⁶)(50²) = 12.5 mJ

**Example 2.** A 0.5 H inductor carries i(t) = 4e⁻³ᵗ A. Find v(t) and the energy
at t = 0.

    v = L di/dt = 0.5 × 4(−3)e⁻³ᵗ = −6e⁻³ᵗ V
    w(0) = ½(0.5)(4²) = 4 J

The negative voltage says the inductor is *releasing* its stored energy back into
the circuit as the current decays.

**Example 3 — DC steady state.** A 12 V source feeds 4 Ω in series with a
parallel combination of a 6 Ω and a capacitor; an inductor with 2 Ω in series
bridges to ground. Find the capacitor voltage and inductor current in steady
state.

Capacitor → open (carries no current). Inductor → short.

The circuit becomes 12 V through 4 Ω into 6 Ω ∥ 2 Ω:

    6 ∥ 2 = 1.5 Ω
    I_total = 12/(4+1.5) = 2.182 A
    V_node = 2.182 × 1.5 = 3.273 V
    V_C = V_node = 3.273 V     (capacitor sits across the 6 Ω branch)
    I_L = 3.273/2 = 1.636 A

**Example 4.** Three capacitors 2 μF, 3 μF, 6 μF in series. Find C_eq.

    1/C_eq = 1/2 + 1/3 + 1/6 = 1  ⇒  C_eq = 1 μF

Note the result is smaller than the smallest — the opposite of series resistors.

## 13.6 Exercises

1. A 100 μF capacitor is charged to 24 V. Find q and w. (2.4 mC, 28.8 mJ)
2. A 20 mH inductor has v = 10 V applied for 5 ms from rest. Find the final
   current. (2.5 A)
3. Two capacitors 4 μF and 12 μF: find C_eq in series and in parallel.
   (3 μF, 16 μF)
4. A capacitor voltage is v = 5t² V for a 2 mF capacitor. Find i(t). (0.02t A)
5. Explain physically why opening a switch in series with an inductor causes a
   spark, but opening a switch in series with a capacitor does not.

## Takeaways

- i = C dv/dt and v = L di/dt. Everything else follows.
- v_C and i_L are **continuous** — they set the initial conditions of every
  transient.
- At DC: C is open, L is short.
- Capacitors and inductors are exact duals; learn the table once.
