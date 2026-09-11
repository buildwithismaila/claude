# Module 03 — Series–Parallel Reduction and Dividers

## 3.1 What "in series" and "in parallel" actually mean

Two elements are **in series** if they share exactly one node and **nothing else
connects to that node**. Same current must flow through both.

Two elements are **in parallel** if they are connected between **the same pair of
nodes**. Same voltage must appear across both.

That second half of the series definition — *nothing else connects to that node*
— is the part people drop, and it is what makes bridge circuits (§3.5) resist
series–parallel reduction entirely.

## 3.2 Series and parallel resistance

**Series** (currents equal, voltages add):

    R_eq = R_1 + R_2 + … + R_n

**Parallel** (voltages equal, currents add):

    1/R_eq = 1/R_1 + 1/R_2 + … + 1/R_n
    G_eq = G_1 + G_2 + … + G_n

For exactly two in parallel, the product-over-sum shortcut:

    R_eq = R_1R_2 / (R_1 + R_2)        written R_1 ∥ R_2

For n **equal** resistors in parallel, R_eq = R/n.

Two useful sanity checks:
- Series R_eq is always **larger** than the largest resistor.
- Parallel R_eq is always **smaller** than the smallest resistor.

If your answer violates either, stop and recheck — this catches a surprising
number of arithmetic slips.

## 3.3 Voltage divider

For resistors in **series** carrying the same current, the source voltage splits
in proportion to resistance:

    V_k = V_s · R_k / (R_1 + R_2 + … + R_n)

For the two-resistor case:

    V_1 = V_s R_1/(R_1+R_2)        V_2 = V_s R_2/(R_1+R_2)

**Condition for use:** the divider must be *unloaded*, or the load must be
included in the calculation. Hanging a load R_L across R_2 means you must first
replace R_2 by R_2 ∥ R_L. Forgetting this is the classic "my potentiometer
doesn't give the voltage I calculated" mistake.

## 3.4 Current divider

For resistors in **parallel** sharing the same voltage, current splits in
proportion to **conductance** — i.e. inversely with resistance:

    I_k = I_s · G_k / (G_1 + … + G_n)

For the two-resistor case, note the deliberately surprising cross-over:

    I_1 = I_s R_2/(R_1+R_2)        I_2 = I_s R_1/(R_1+R_2)

The current through R_1 depends on R_2 — more current takes the easier path.
Compare with the voltage divider, where V_1 depends on R_1. **Getting these two
the wrong way round is the most common error in the whole module**; the way to
keep them straight is to reason from the physics (current prefers low
resistance) rather than to memorise which symbol goes on top.

## 3.5 Ladder reduction

To find the resistance seen at a pair of terminals, work **from the far end
back toward the terminals**, collapsing series and parallel pairs one at a time.
Redraw after every step. Do not try to do two steps in your head.

**Example.** Find R_eq at terminals a–b:
6 Ω in series with (4 Ω parallel with (8 Ω in series with 8 Ω)).

    Innermost: 8 + 8 = 16 Ω
    Then: 4 ∥ 16 = (4)(16)/20 = 3.2 Ω
    Then: 6 + 3.2 = 9.2 Ω

## 3.6 Delta–wye (Δ–Y, or π–T) transformation

Some networks — the Wheatstone bridge above all — contain no two resistors that
are purely in series or purely in parallel. Series–parallel reduction stalls.
The Δ–Y transformation is the way out.

**Delta to wye** (each wye resistor = product of the two adjacent deltas over the
sum of all three):

    R_1 = R_b R_c / (R_a + R_b + R_c)
    R_2 = R_a R_c / (R_a + R_b + R_c)
    R_3 = R_a R_b / (R_a + R_b + R_c)

**Wye to delta** (each delta resistor = sum of pairwise products over the
opposite wye):

    R_a = (R_1R_2 + R_2R_3 + R_3R_1) / R_1
    R_b = (R_1R_2 + R_2R_3 + R_3R_1) / R_2
    R_c = (R_1R_2 + R_2R_3 + R_3R_1) / R_3

**Balanced special case:** if all three deltas are equal to R_Δ, then all three
wye resistors equal R_Δ/3. And conversely R_Δ = 3R_Y. Worth memorising — it
appears constantly in three-phase work.

### Wheatstone bridge

A bridge is **balanced** when no current flows in the detector branch, which
happens when

    R_1/R_2 = R_3/R_4        (opposite products equal: R_1R_4 = R_2R_3)

At balance the middle branch can be removed (or shorted — either, since it
carries no current and has no voltage across it), and the rest reduces by
series–parallel. If the bridge is **not** balanced, use Δ–Y, or fall back on
nodal or mesh analysis.

## 3.7 Worked examples

**Example 1.** Find the equivalent resistance of 12 Ω ∥ 4 Ω, then in series
with 5 Ω.

    12 ∥ 4 = (12)(4)/16 = 3 Ω
    R_eq = 3 + 5 = 8 Ω

Check: parallel result 3 Ω is smaller than the smaller resistor (4 Ω) ✓

**Example 2.** A 24 V source feeds 3 Ω in series with 9 Ω. Find the voltage
across the 9 Ω, then repeat with a 18 Ω load across the 9 Ω.

Unloaded:

    V_9 = 24 × 9/12 = 18 V

Loaded: replace 9 Ω by 9 ∥ 18 = (9)(18)/27 = 6 Ω

    V_out = 24 × 6/(3+6) = 24 × 6/9 = 16 V

The load pulled the output down from 18 V to 16 V. That droop is precisely what
the Thévenin resistance of the divider predicts (Module 09).

**Example 3.** A 10 A source feeds 2 Ω in parallel with 8 Ω. Find both currents.

    I_2 = 10 × 8/(2+8) = 8 A
    I_8 = 10 × 2/(2+8) = 2 A

Check: they sum to 10 A ✓, and the larger current is in the smaller resistor ✓

**Example 4.** A delta of three 15 Ω resistors. Find the equivalent wye.

    R_Y = R_Δ/3 = 5 Ω each

**Example 5.** A bridge has R_1 = 100 Ω, R_2 = 200 Ω, R_3 = 150 Ω. Find R_4 for
balance.

    R_1R_4 = R_2R_3  ⇒  R_4 = (200)(150)/100 = 300 Ω

## 3.8 Exercises

1. Find R_eq for 6 Ω ∥ 3 Ω ∥ 2 Ω. (1 Ω)
2. Three resistors 10 Ω, 20 Ω, 30 Ω in series across 120 V. Find each voltage.
   (20 V, 40 V, 60 V)
3. A current divider splits 6 A between 5 Ω and 20 Ω. Find both. (4.8 A, 1.2 A)
4. Convert a wye of 10 Ω, 20 Ω, 30 Ω into the equivalent delta.
   (R_a = 110 Ω, R_b = 55 Ω, R_c = 36.67 Ω)
5. Why can a balanced bridge's middle branch be either removed *or* shorted with
   no change to the rest of the circuit?

## Takeaways

- Series shares current, parallel shares voltage — and "series" requires that
  nothing else taps the shared node.
- Voltage divider: V_1 ∝ R_1. Current divider: I_1 ∝ R_2. Reason it out from
  "current takes the easy path" rather than memorising.
- A loaded divider is a different divider. Fold the load in first.
- Δ–Y is the escape hatch when nothing is in series or parallel. R_Δ = 3R_Y when
  balanced.
