# Module 02 — Circuit Elements, Ohm's Law and Sources

## 2.1 Resistance and Ohm's law

    v = iR        R = v/i        [Ω]

with the passive sign convention assumed (current into the + terminal).

**Conductance** is the reciprocal:

    G = 1/R       i = Gv        [S]

Conductance is not just notational tidiness — parallel combinations add in
conductance, which is why nodal analysis (Module 05) is naturally written in G.

**Power in a resistor:**

    p = vi = i²R = v²/R

All three forms are the same equation. Use whichever quantity you already know.
Note p is always **positive** for a resistor: a resistor can only absorb. This
is a useful sanity check — if your algebra hands you a negative resistor power,
something upstream is wrong.

### Resistivity

    R = ρℓ/A

with ρ the resistivity (Ω·m), ℓ the length and A the cross-sectional area.
Copper ρ ≈ 1.72×10⁻⁸ Ω·m. Doubling length doubles R; doubling diameter
quarters it.

### Two limiting cases

| | R | v | i |
|---|---|---|---|
| **Short circuit** | 0 | 0 regardless of i | set by the rest of the circuit |
| **Open circuit** | ∞ | set by the rest of the circuit | 0 regardless of v |

These two are worth stating explicitly because half of Thévenin/Norton practice
consists of deliberately short-circuiting or open-circuiting a pair of
terminals and asking what survives.

## 2.2 Independent sources

An **ideal independent voltage source** maintains a specified voltage across its
terminals **whatever current flows through it**. The current is decided by the
external circuit, not by the source.

An **ideal independent current source** pushes a specified current through its
terminals **whatever voltage appears across it**. The voltage is decided by the
external circuit.

Two consequences students routinely get wrong:

- You **cannot** know the current through an ideal voltage source by looking at
  the source. You must analyse the circuit around it.
- You **cannot** know the voltage across an ideal current source by looking at
  the source. Same reason.

**Illegal connections.** Two unequal ideal voltage sources in parallel is a
contradiction (which voltage wins?). Two unequal ideal current sources in series
is likewise a contradiction. Real circuits never contain these; exam questions
sometimes do, as a trap.

### Practical sources

Real sources are not ideal. Model them as:

- **Practical voltage source** = ideal V_s **in series** with R_s
- **Practical current source** = ideal I_s **in parallel** with R_p

The terminal voltage of a practical voltage source **droops** with load:

    V_terminal = V_s − I R_s

A "stiff" source has R_s much smaller than the load resistance. A car battery
(R_s ≈ 0.01 Ω) is stiff; a 9 V PP3 battery near end-of-life is not, which is why
its terminal voltage collapses under load.

## 2.3 Dependent (controlled) sources

A dependent source's value is set by a voltage or current **elsewhere** in the
circuit. There are four types:

| Type | Name | Relationship | Gain units |
|---|---|---|---|
| VCVS | Voltage-controlled voltage source | v = μ v_x | dimensionless |
| VCCS | Voltage-controlled current source | i = g v_x | S |
| CCVS | Current-controlled voltage source | v = r i_x | Ω |
| CCCS | Current-controlled current source | i = β i_x | dimensionless |

Drawn as a **diamond**, where independent sources are circles.

Dependent sources are how transistors, op-amps and amplifiers get represented,
so they are not an exotic special case — they are the normal case in electronics.

**Three rules that will save you:**

1. A dependent source is **never** switched off when applying superposition
   (Module 07). Only independent sources are.
2. A dependent source is **never** switched off when finding R_th (Module 09).
   You must use the test-source method instead.
3. The controlling variable v_x or i_x must stay **inside** the network you are
   analysing. If you extract a Thévenin equivalent that cuts between a dependent
   source and its controlling variable, the result is meaningless.

## 2.4 Worked examples

**Example 1.** A 12 V source drives a 4 Ω resistor. Find I, P and G.

    I = V/R = 12/4 = 3 A
    P = I²R = 9 × 4 = 36 W   (check: P = V²/R = 144/4 = 36 W ✓)
    G = 1/4 = 0.25 S

**Example 2.** A practical source has V_s = 10 V, R_s = 2 Ω, and drives a 8 Ω
load. Find the terminal voltage and the power lost internally.

    I = 10/(2+8) = 1 A
    V_terminal = 10 − 1(2) = 8 V
    P_internal = I²R_s = 1 × 2 = 2 W
    P_load = 1 × 8 = 8 W

Efficiency = 8/10 = **80%**. Note the source's own resistance wastes 20% here.
Module 11 shows that the *maximum power* condition is worse still — 50%.

**Example 3.** A copper wire is 100 m long with cross-section 2.5 mm². Find R.

    R = ρℓ/A = (1.72×10⁻⁸)(100)/(2.5×10⁻⁶) = 1.72×10⁻⁶/2.5×10⁻⁶
    R = 0.688 Ω

**Example 4.** In a circuit, a CCCS produces 4i_x where i_x = 0.5 A is the
current in a nearby branch. What current does the dependent source supply?

    i = 4 × 0.5 = 2 A

If i_x later turns out to be −0.5 A, the dependent source supplies −2 A — it
follows its controller, including the sign.

## 2.5 Exercises

1. A resistor dissipates 20 W with 2 A through it. Find R and V. (5 Ω, 10 V)
2. A 100 Ω and a 25 Ω resistor each have 10 V across them. Which dissipates
   more, and by what factor? (The 25 Ω, by 4×)
3. A practical current source of 2 A with R_p = 50 Ω drives a 50 Ω load. Find
   the load current and the fraction of the source current that is "lost".
   (1 A; half)
4. Explain why two ideal 5 V sources may be connected in parallel but a 5 V and
   a 6 V source may not.
5. An aluminium wire (ρ = 2.82×10⁻⁸ Ω·m) must have the same resistance as the
   copper wire of Example 3. What cross-section does it need? (4.1 mm²)

## Takeaways

- Ohm's law needs the passive sign convention to be unambiguous.
- Ideal voltage sources fix v and let the circuit decide i; ideal current sources
  do the opposite. Never assume either one's unknown quantity.
- Practical sources are ideal ones plus a series (or parallel) resistance — and
  that resistance is exactly what becomes R_th in Module 09.
- Dependent sources are never deactivated. Remember this now; it is the most
  common single error in Thévenin problems.
