# Module 01 — Electrical Quantities and Sign Conventions

## 1.1 Charge and current

Charge q is measured in coulombs (C). The electron carries −1.602×10⁻¹⁹ C.

**Current** is the rate of flow of charge past a point:

    i = dq/dt        [A = C/s]

For a steady flow, I = Q/t.

**Conventional current** flows in the direction positive charge would move —
opposite to actual electron drift. Every formula in this course uses
conventional current. Electron flow is a physical fact you can safely forget.

A current has **no meaning without a reference arrow**. "The current is 3 A" is
incomplete; "the current is 3 A in the direction of the arrow" is complete. If
the arrow is drawn one way and the true flow is the other, the answer simply
comes out negative — and a negative current is a correct answer, not an error.

## 1.2 Voltage

**Voltage** (potential difference) between two points is the energy per unit
charge required to move charge between them:

    v = dw/dq        [V = J/C]

Voltage is always **between two points**. "The voltage at node A" is shorthand
for "the voltage at A with respect to the reference node". There is no such
thing as an absolute voltage, only a difference.

Notation: V_AB means the potential at A minus the potential at B.

    V_AB = −V_BA        and       V_AB = V_A − V_B

Polarity marks (+ and −) on a circuit diagram play the same role for voltage
that arrows play for current: they declare an assumed reference, not a fact.

## 1.3 The passive sign convention — the most important rule in the course

> **Passive sign convention:** current enters the element at its **+** terminal.

When an element is labelled this way, then

    p = vi

is the power **absorbed** by that element.

- p > 0 → the element is **absorbing** (dissipating or storing) power.
- p < 0 → the element is **delivering** power to the rest of the circuit.

If current instead enters at the − terminal, then p = vi is the power
**delivered**, or equivalently p = −vi is the power absorbed.

**Why this matters so much.** Roughly half of all lost marks in circuit theory
are sign errors, and most of those trace back to an element whose assumed
polarity was never written on the diagram. The fix is mechanical: *before
calculating anything, draw the reference arrow and the ± marks on every element,
and never change them.* If a value comes out negative, leave it negative and
carry it through. Re-drawing arrows halfway is how sign errors are born.

### Conservation of power

In any circuit, at every instant,

    Σ p_absorbed = 0

Equivalently: power delivered by the sources equals power absorbed by everything
else. This is the single best check on a finished answer — total it up, and if
it does not come to zero, you have a sign or arithmetic error somewhere.

## 1.4 Energy

    w = ∫ p dt        [J]

For constant power, W = Pt. The commercial unit is the kilowatt-hour:
1 kWh = 1000 W × 3600 s = 3.6×10⁶ J.

## 1.5 Units and prefixes

| Quantity | Symbol | Unit | Unit symbol |
|---|---|---|---|
| Charge | q, Q | coulomb | C |
| Current | i, I | ampere | A |
| Voltage | v, V | volt | V |
| Power | p, P | watt | W |
| Energy | w, W | joule | J |
| Resistance | R | ohm | Ω |
| Conductance | G | siemens | S |

| Prefix | Symbol | Factor |
|---|---|---|
| pico | p | 10⁻¹² |
| nano | n | 10⁻⁹ |
| micro | μ | 10⁻⁶ |
| milli | m | 10⁻³ |
| kilo | k | 10³ |
| mega | M | 10⁶ |
| giga | G | 10⁹ |

Note the case: **m** is milli, **M** is mega — a factor of 10⁹ apart. And a
capital **G** is giga while an italic G is conductance.

## 1.6 Worked examples

**Example 1.** A charge of 12 C passes a point in 4 s. Find the current.

    I = Q/t = 12/4 = 3 A

**Example 2.** An element has 12 V across it with the + mark on the left, and
2 A flowing into the left terminal. Find the power and say whether the element
absorbs or delivers.

Current enters the + terminal ⇒ passive sign convention applies.

    p = vi = 12 × 2 = 24 W    (absorbed)

The element absorbs 24 W. It is behaving as a load.

**Example 3.** Same element, but the 2 A flows **out of** the + terminal.

Current enters the − terminal, so p = vi is now the power *delivered*:

    p_delivered = 12 × 2 = 24 W   ⇒   p_absorbed = −24 W

The element delivers 24 W. It is behaving as a source. This is exactly what a
battery being discharged does — and a battery being *charged* absorbs, which is
why the same element can appear with either sign.

**Example 4.** A circuit has three elements: a source delivering 50 W, a
resistor absorbing 30 W, and a third element. Find the third element's power.

    Σ p_absorbed = 0
    (−50) + 30 + p_3 = 0   ⇒   p_3 = +20 W absorbed

**Example 5.** A 60 W lamp runs for 8 hours. Find the energy in kWh and joules.

    W = Pt = 60 × 8 = 480 Wh = 0.48 kWh
    W = 0.48 × 3.6×10⁶ = 1.728×10⁶ J

## 1.7 Exercises

1. A current of 5 mA flows for 2 minutes. How much charge is transferred?
   (0.6 C)
2. An element absorbs 100 W with 20 V across it. Find the current, and state
   which terminal it enters. (5 A, entering the + terminal)
3. A battery delivers 24 W at 12 V while being discharged. Find the current.
   Now the same battery is charged at 1.5 A at 12 V — what power does it absorb?
   (2 A; 18 W)
4. In a three-element circuit, element A absorbs −40 W and element B absorbs
   25 W. Find element C's absorbed power. (15 W)
5. Convert: 0.0047 A to mA; 2.2 MΩ to Ω; 470 pF to F.

## Takeaways

- Current needs an arrow, voltage needs ± marks. Both are *assumptions*, and a
  negative answer means the assumption was backwards — which is fine.
- Passive sign convention: current into +, then p = vi is absorbed power.
- Σ p_absorbed = 0 across the whole circuit. Use it to check every answer.
