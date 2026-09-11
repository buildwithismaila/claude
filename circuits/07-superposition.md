# Module 07 — Linearity and Superposition

## 7.1 Linearity

A circuit is **linear** if it contains only linear elements — resistors, and
sources whose dependent relationships are proportional. Linearity means two
properties hold:

**Homogeneity (scaling).** Multiply every independent source by k, and every
voltage and current in the circuit multiplies by k.

**Additivity.** The response to several sources acting together equals the sum
of the responses to each acting alone.

Together these give **superposition**, and superposition is what every remaining
theorem in this course is built on. Thévenin, Norton, source transformation and
maximum power transfer are all consequences.

> **Power is not linear.** p = i²R is a *square* law. You may never superpose
> powers. Superpose the voltage or current first, then square the **total**. A
> question that asks for power via superposition is testing exactly this, and
> the wrong method gives a confidently wrong number.

## 7.2 Superposition — the method

To find any voltage or current in a linear circuit with multiple independent
sources:

1. Take one independent source at a time.
2. **Deactivate all other independent sources:**
   - Voltage source → replace with a **short circuit** (0 V across it)
   - Current source → replace with an **open circuit** (0 A through it)
3. Solve the simplified circuit for the quantity you want.
4. Repeat for each source.
5. **Add** the individual contributions algebraically, respecting sign.

### The rule that gets forgotten

> **Dependent sources are never deactivated.** They stay active in every single
> sub-circuit, because their value is not an independent input to the system —
> it is part of the circuit's own behaviour.

If you kill a dependent source, you are analysing a different circuit.

### Why "short" and "open"?

An ideal voltage source set to zero volts is, by definition, an element with
0 V across it whatever the current — that is exactly a short circuit. An ideal
current source set to zero amps passes 0 A whatever the voltage — exactly an
open circuit. The replacements are not conventions; they are what the
deactivated sources *are*.

## 7.3 When superposition is worth using

Honestly: **often it is not**. For a circuit with three sources you solve three
circuits instead of one. Nodal or mesh analysis is usually faster.

Superposition earns its place when:

- One source is AC and another DC (Module 13) — they *cannot* be combined any
  other way.
- Sources are at different frequencies — same reason.
- You need to understand the *contribution* of one source, not just the total.
- It is the stepping-stone to proving Thévenin, which is its real job here.

## 7.4 Worked examples

**Example 1 — two voltage sources.**
A 12 V source and a 6 V source drive a shared 4 Ω resistor through 2 Ω and 3 Ω
respectively (both source branches meeting at the top of the 4 Ω).
Find the current in the 4 Ω.

*Contribution of the 12 V source* (6 V shorted):
The 3 Ω is now in parallel with the 4 Ω: 3 ∥ 4 = 12/7 = 1.714 Ω

    i_total = 12/(2 + 1.714) = 12/3.714 = 3.231 A
    i_4' = 3.231 × 3/(3+4) = 1.385 A      (current divider)

*Contribution of the 6 V source* (12 V shorted):
The 2 Ω is now in parallel with the 4 Ω: 2 ∥ 4 = 8/6 = 1.333 Ω

    i_total = 6/(3 + 1.333) = 6/4.333 = 1.385 A
    i_4'' = 1.385 × 2/(2+4) = 0.462 A

*Total:*

    i_4 = 1.385 + 0.462 = 1.846 A

Cross-check by nodal analysis. With the top node at V:

    (V − 12)/2 + (V − 6)/3 + V/4 = 0
    6(V−12) + 4(V−6) + 3V = 0
    6V − 72 + 4V − 24 + 3V = 0
    13V = 96   ⇒   V = 7.385 V
    i_4 = 7.385/4 = 1.846 A ✓

**Example 2 — a voltage source and a current source.**
A 10 V source in series with 5 Ω feeds a node; a 2 A source also feeds that
node; the node connects to ground through 10 Ω. Find the node voltage.

*10 V alone* (2 A source opened):

    V' = 10 × 10/(5+10) = 6.667 V

*2 A alone* (10 V source shorted): the 2 A sees 5 ∥ 10 = 3.333 Ω

    V'' = 2 × 3.333 = 6.667 V

*Total:* V = 6.667 + 6.667 = **13.33 V**

Check by nodal: (V − 10)/5 + V/10 = 2 ⇒ 2V − 20 + V = 20 ⇒ 3V = 40 ⇒
V = 13.33 V ✓

**Example 3 — the power trap.**
In Example 2, find the power in the 10 Ω resistor.

**Wrong:** P' = (6.667)²/10 = 4.44 W, P'' = 4.44 W, "total" 8.89 W.
**Right:** V = 13.33 V total, so

    P = V²/R = (13.33)²/10 = 17.8 W

The correct answer is *twice* the naive sum, because power goes as the square.
Superpose the voltage, then square.

**Example 4 — with a dependent source.**
A 6 V source in series with 2 Ω feeds node A; a 3 A source also feeds node A;
node A connects to ground through 4 Ω; and a VCVS of value 2v_x sits in series
with the 2 Ω branch, where v_x is the node A voltage.

The dependent source stays active throughout. Taking the 6 V alone (3 A opened),
then the 3 A alone (6 V shorted), each sub-circuit still contains 2v_x. In
practice, with a dependent source present it is nearly always quicker to abandon
superposition and write one nodal equation — which is the honest lesson here.

## 7.5 Exercises

1. Two sources, 20 V and 5 A, share a 10 Ω load through 5 Ω and 20 Ω
   respectively. Find the load voltage by superposition, then check by nodal.
2. A circuit gives an output of 6 V when driven by a 12 V source. What output
   does a 30 V source give? (15 V — by homogeneity alone)
3. In Example 1, find the power in the 4 Ω, and confirm you cannot get it by
   adding the two individual powers. (13.6 W; the naive sum gives 8.6 W)
4. Explain, in terms of what a source *is*, why deactivating a current source
   means opening it rather than shorting it.
5. A circuit has a 10 V DC source and a sinusoidal source. Why is superposition
   essentially mandatory here?

## Takeaways

- Linearity = scaling + additivity. It holds for v and i, never for p.
- Kill voltage sources by shorting, current sources by opening.
- Dependent sources always stay active.
- Superposition's real importance is as the proof engine for Thévenin, not as a
  day-to-day solving method.
