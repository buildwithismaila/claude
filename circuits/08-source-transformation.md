# Module 08 — Source Transformation

## 8.1 The transformation

A practical voltage source and a practical current source are
**indistinguishable from outside** if:

    V_s = I_s R          I_s = V_s / R          R unchanged

That is:

> A voltage source V_s **in series** with R ⟺ a current source I_s = V_s/R
> **in parallel** with the same R.

### Why they are equivalent

Compare terminal behaviour. For the voltage source in series with R, the
terminal voltage at load current I is

    V = V_s − IR

For the current source in parallel with R, the current through the load is
I_s − V/R, so

    I = I_s − V/R   ⇒   V = (I_s − I)R = I_s R − IR

These are the same straight line provided V_s = I_s R. Two black boxes with
identical v–i characteristics cannot be told apart by any external measurement.

### The direction rule

The current source arrow must point **toward the terminal that the voltage
source's + terminal faced**. Get this backwards and every sign in the rest of
the problem inverts. Mark it on the diagram before moving on.

## 8.2 What it is for

Source transformation is a **circuit-simplification engine**. Alternating
between the two forms lets you merge sources that could not otherwise be
combined:

- Current sources **in parallel** add directly.
- Voltage sources **in series** add directly.
- Neither can be done in the other configuration.

So the working pattern is: transform → merge → transform back → merge again,
marching the sources toward the terminals of interest until only one remains.
Doing this to completion *is* finding the Thévenin or Norton equivalent, which
is why this module sits immediately before those two.

## 8.3 Limitations

- The resistance must be **genuinely in series** (for a voltage source) or
  **genuinely in parallel** (for a current source). An ideal source with no
  associated resistance cannot be transformed at all.
- The internal behaviour is **not** preserved. Power dissipated in R differs
  between the two forms even though the terminal behaviour is identical. See
  §8.5 — this is a favourite exam trap.
- A dependent source **can** be transformed, provided its controlling variable
  is not inside the part being transformed away.

## 8.4 Worked examples

**Example 1 — basic conversion.**
A 24 V source in series with 6 Ω. Convert.

    I_s = 24/6 = 4 A in parallel with 6 Ω

**Example 2 — repeated transformation.**
A 12 V source in series with 3 Ω feeds node A; node A has a 6 Ω to ground; a
2 A source also feeds node A. Find the current in a 4 Ω load at node A.

Step 1 — transform the 12 V/3 Ω into 4 A ∥ 3 Ω.

Now at node A: 4 A source, 3 Ω, 6 Ω, 2 A source, and the 4 Ω load.

Step 2 — merge the two current sources (parallel): 4 + 2 = 6 A.
Merge 3 ∥ 6 = 2 Ω.

Step 3 — now a 6 A source in parallel with 2 Ω, feeding the 4 Ω load.
Current divider:

    I_4 = 6 × 2/(2+4) = 2 A

Check by transforming back: 6 A ∥ 2 Ω = 12 V in series with 2 Ω, so
I = 12/(2+4) = 2 A ✓

**Example 3 — marching toward the terminals.**
A 10 V source in series with 5 Ω, then a 5 Ω to ground, then a 10 Ω in series
to terminals a–b. Reduce to a single source at a–b.

    10 V / 5 Ω  →  2 A ∥ 5 Ω
    5 ∥ 5 = 2.5 Ω, still 2 A
    2 A ∥ 2.5 Ω  →  5 V in series with 2.5 Ω
    Add the series 10 Ω:  5 V in series with 12.5 Ω

So looking into a–b you see a 5 V source behind 12.5 Ω — which is precisely the
Thévenin equivalent of the whole thing.

**Example 4 — the internal-power trap.**
A 24 V source in series with 6 Ω drives a 6 Ω load. Compare the power in the
internal resistance with that of the transformed equivalent.

*Voltage form:* I = 24/12 = 2 A. Power in the internal 6 Ω = 2²(6) = **24 W**.
Source delivers 24 × 2 = 48 W.

*Current form:* 4 A ∥ 6 Ω into a 6 Ω load. Load gets 2 A (divider), so the
parallel 6 Ω also carries 2 A, dissipating 2²(6) = **24 W** — the same here, but
the *source's* delivered power is now 4 A × 12 V = 48 W with the internal
element carrying a different current in general.

The load sees identical behaviour in both: 2 A, 12 V, 24 W. That is all the
equivalence promises. **Never** use a transformed circuit to compute the power
inside the original source.

## 8.5 Exercises

1. Convert a 5 A source in parallel with 8 Ω to its voltage form. (40 V, 8 Ω)
2. A 15 V source in series with 3 Ω, in parallel with a 6 A source and 2 Ω.
   Reduce to a single current source and resistance. (11 A ∥ 1.2 Ω)
3. Use repeated source transformation to find the current through a 5 Ω load fed
   by a 20 V source in series with 10 Ω, with a 4 A source in parallel at the
   load terminals.
4. Why can an ideal voltage source (no series resistance) not be transformed?
5. Show algebraically that the two forms have the same v–i line, and identify
   what the slope and intercepts represent physically.

## Takeaways

- V_s = I_s R, same R, arrow pointing toward where + was.
- Transform to merge: current sources in parallel add, voltage sources in
  series add.
- Terminal behaviour is preserved; internal power is not.
- Marching transformations all the way to a terminal pair yields Thévenin or
  Norton directly.
