# Module 12 — Millman, Reciprocity, Substitution and Tellegen

The four theorems here are narrower than Thévenin and Norton but each solves one
class of problem very quickly.

## 12.1 Millman's theorem

For several **practical voltage sources connected in parallel** across a common
pair of terminals, the single equivalent is:

    V_eq = (V_1G_1 + V_2G_2 + … + V_nG_n) / (G_1 + G_2 + … + G_n)
    R_eq = 1 / (G_1 + G_2 + … + G_n)

with G_k = 1/R_k. In resistance form:

    V_eq = (V_1/R_1 + V_2/R_2 + … ) / (1/R_1 + 1/R_2 + … )

**What it really is:** a weighted average of the source voltages, weighted by
conductance. The stiffest source (lowest R) dominates — which is exactly what
your intuition about paralleled batteries should say.

**Conditions:** all branches must be in parallel between the *same* two nodes.
A branch with no source is included with V_k = 0 (it still contributes its
conductance to the denominator).

**Example.** Three sources across common terminals: 12 V with 2 Ω, 10 V with
4 Ω, and 6 V with 4 Ω.

    Numerator = 12/2 + 10/4 + 6/4 = 6 + 2.5 + 1.5 = 10
    Denominator = 1/2 + 1/4 + 1/4 = 1.0
    V_eq = 10 V,   R_eq = 1 Ω

Note this is just a one-line nodal analysis. Millman is nodal analysis for the
single-node case, pre-solved.

## 12.2 Reciprocity theorem

> In a linear, **passive**, bilateral network with a **single** source, the
> source and the response may be interchanged without changing the ratio between
> them.

Put a voltage source in branch A and measure the current in branch B. Move the
same source to branch B: the current now measured in branch A is **identical**.

    I_B / V_A = I_A / V_B

**Strict conditions — all four must hold:**
1. Linear
2. Passive — **no dependent sources**, no amplifiers
3. Bilateral — elements behave the same in both directions (resistors do; diodes
   do not)
4. A single independent source

Reciprocity fails immediately if a dependent source is present. That is the
point of the "passive" requirement, and it is why transistor circuits are not
reciprocal — which is precisely what makes amplification possible.

**Use:** it halves the work when a problem asks for the same network driven from
two different branches, and it is a powerful sanity check on a long solution.

## 12.3 Substitution theorem

> Any branch in a network may be replaced by any other branch that produces the
> **same voltage across it and current through it**, without disturbing the rest
> of the circuit.

If a branch carries 2 A with 6 V across it, it may be replaced by:
- a 3 Ω resistor, or
- a 6 V source, or
- a 2 A source, or
- any combination with the same terminal v and i.

**Use:** it justifies replacing a complicated subnetwork with a single measured
source once you know its operating point, and it is the formal basis for the
"replace the load with a source" step in several proofs. Its limitation is that
the substitution is valid **only at that one operating point** — change anything
else in the circuit and the equivalence is void.

## 12.4 Compensation theorem

> If a resistance R in a branch carrying current I changes by ΔR, the change in
> all other currents and voltages is the same as would be produced by inserting
> a voltage source of value **V_c = I·ΔR** in that branch, opposing the original
> current, with all other sources deactivated.

**Use:** sensitivity analysis. It tells you how much a circuit's behaviour shifts
when one component drifts, without re-solving the whole network — useful for
tolerance and error budgets.

**Example.** A branch carries 0.5 A through 20 Ω. The resistor is replaced by a
22 Ω (a +2 Ω change). The perturbation is equivalent to a source of

    V_c = 0.5 × 2 = 1 V

inserted in opposition, with the original sources off. Solve that much simpler
circuit to get the change in every current.

## 12.5 Tellegen's theorem

> For **any** network satisfying KCL and KVL, with branch voltages v_k and
> branch currents i_k taken in the passive sign convention:

    Σ v_k i_k = 0

The remarkable part: this needs **no** assumption of linearity, and the elements
need not even be the same in the two sets. It depends only on the *topology* —
on KCL and KVL holding — not on what the elements are.

For a single network it reduces to conservation of power (Module 01). Its deeper
use is in network theory proofs and in checking large simulations.

## 12.6 Which theorem for which problem

| Problem shape | Reach for |
|---|---|
| Find what a load does | Thévenin or Norton |
| Best load for max power | Maximum power transfer |
| Several sources, want one contribution | Superposition |
| Simplify a source chain | Source transformation |
| Several parallel practical sources | Millman |
| Same network driven from two branches | Reciprocity |
| One component's value drifts | Compensation |
| Check a solved circuit | Tellegen / Σp = 0 |

## 12.7 Exercises

1. Four sources in parallel: 24 V/6 Ω, 12 V/4 Ω, 0 V/12 Ω, 18 V/9 Ω. Find the
   Millman equivalent. (V_eq = 14.73 V, R_eq = 1.636 Ω)
2. A 10 V source in branch A causes 0.4 A in branch B. What current would it
   cause in A if moved to B? (0.4 A)
3. A branch carries 1.5 A through 8 Ω. It is changed to 8.5 Ω. Give the
   compensating source value. (0.75 V)
4. Why does reciprocity fail for a circuit containing a CCCS?
5. Verify Tellegen's theorem on Module 04 Example 3.

## Takeaways

- Millman = one-line nodal analysis for parallel practical sources; it is a
  conductance-weighted average.
- Reciprocity needs linear, passive, bilateral, single-source — dependent sources
  kill it.
- Substitution is valid only at the operating point it was derived from.
- Compensation converts a component change into an equivalent source.
- Tellegen needs only KCL and KVL — topology alone.
