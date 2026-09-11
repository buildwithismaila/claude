# Module 10 — Norton's Theorem

## 10.1 Statement

> Any linear two-terminal network can be replaced, as seen from those terminals,
> by a single current source I_N in parallel with a single resistance R_N.

- **I_N** = the **short-circuit current** at the terminals
- **R_N** = R_th, found exactly as in Module 09

Norton is the dual of Thévenin. Everything true of one is true of the other with
"voltage/series" and "current/parallel" swapped.

## 10.2 The relationship between them

    I_N = V_th / R_th          V_th = I_N R_N          R_N = R_th

This is just source transformation (Module 08) applied to the equivalent itself.
Given either equivalent you have the other immediately — so in practice you find
whichever is easier and convert.

The three quantities V_th, I_N and R_th are linked by R_th = V_oc/I_sc, so
**any two of them determine the third**. Finding two is always enough.

## 10.3 Which to use

| Use Thévenin when | Use Norton when |
|---|---|
| The load is in series | The load is in parallel |
| Sources are mostly voltage sources | Sources are mostly current sources |
| You want load voltage | You want load current |
| Combining with mesh analysis | Combining with nodal analysis |

Neither is more "correct". They describe the same straight-line v–i
characteristic, seen from different ends:

    V = V_th − I R_th       (Thévenin form)
    I = I_N − V/R_N         (Norton form)

The intercepts are V_th (at I = 0) and I_N (at V = 0), and the slope is R_th
either way.

## 10.4 Worked examples

**Example 1.** Find the Norton equivalent of a 12 V source in series with 4 Ω,
with 12 Ω across the terminals. (Same circuit as Module 09 Example 1.)

*I_N* — short the terminals. The 12 Ω is shorted out:

    I_N = 12/4 = 3 A

*R_N* — sources off: 4 ∥ 12 = 3 Ω

Equivalent: **3 A in parallel with 3 Ω**

Cross-check against Thévenin: V_th = I_N R_N = 3 × 3 = 9 V ✓ (matches
Module 09)

Load current into 6 Ω, by current divider:

    I_L = 3 × 3/(3+6) = 1 A ✓

**Example 2 — current-source network.**
A 6 A source in parallel with 10 Ω, feeding a 15 Ω in series to the terminals.
Find the Norton equivalent.

*I_N* — short the terminals. The 15 Ω is then in parallel with the 10 Ω, and the
6 A divides:

    I_N = 6 × 10/(10+15) = 2.4 A

*R_N* — open the 6 A source: 10 Ω in series with 15 Ω = 25 Ω

Equivalent: **2.4 A in parallel with 25 Ω**

Check: V_th = 2.4 × 25 = 60 V. Directly, the open-circuit voltage is the 6 A
through the 10 Ω (no current flows in the 15 Ω when open), giving
6 × 10 = 60 V ✓

**Example 3 — mixed sources.**
A 24 V source in series with 6 Ω, in parallel with a 2 A source, feeding
terminals a–b.

Transform the 24 V/6 Ω into 4 A ∥ 6 Ω. Now two parallel current sources:

    I_N = 4 + 2 = 6 A
    R_N = 6 Ω

Equivalent: **6 A in parallel with 6 Ω**, i.e. V_th = 36 V behind 6 Ω.

**Example 4 — with a dependent source.**
Using the network from Module 09 Example 4, R_N = R_th = 5 Ω. If the
open-circuit voltage of that network is 3 V, then

    I_N = V_th/R_th = 3/5 = 0.6 A

## 10.5 Exercises

1. Convert a Thévenin equivalent of 18 V behind 9 Ω to Norton form. (2 A ∥ 9 Ω)
2. A network has I_sc = 4 A and V_oc = 24 V. Give both equivalents.
   (24 V + 6 Ω; 4 A ∥ 6 Ω)
3. Find the Norton equivalent of a 5 A source in parallel with 4 Ω, in series
   with 6 Ω to the terminals. (2 A ∥ 10 Ω)
4. For a source with V_oc = 10 V and R_th = 5 Ω, sketch the v–i line and mark
   both intercepts.
5. A load of 2 Ω is connected to the equivalent of Exercise 3. Find the load
   current and voltage. (1.667 A; 3.33 V)

## Takeaways

- I_N = short-circuit current, R_N = R_th.
- I_N = V_th/R_th — the two equivalents are one source transformation apart.
- Any two of V_th, I_N, R_th give the third.
- Pick the form that matches how the load connects and which analysis method you
  are already using.
