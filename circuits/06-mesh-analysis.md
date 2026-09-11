# Module 06 — Mesh Analysis

Mesh analysis is KVL applied systematically. Where nodal analysis solves for
node voltages, mesh analysis solves for **loop currents**.

**Restriction:** meshes only exist in **planar** circuits — those drawable with
no crossing wires. For a non-planar circuit, nodal analysis is your only option.

## 6.1 The method

1. Confirm the circuit is planar and identify the meshes (windows).
2. Assign a mesh current to each, **all in the same direction** (clockwise by
   convention). This consistency is what makes the by-inspection form work.
3. Write KVL around each mesh, expressing resistor voltages in terms of mesh
   currents.
4. Solve.

**The crucial subtlety:** a resistor on the **boundary between two meshes**
carries the *difference* of the two mesh currents. For a resistor shared by
meshes 1 and 2, the voltage drop when traversing with mesh 1 is

    v = R(i_1 − i_2)

A branch current is not a mesh current unless that branch belongs to only one
mesh. Confusing the two is the defining error of this module.

## 6.2 The standard form

For a planar circuit containing only **independent voltage sources**, KVL
around every mesh collapses to **RI = V**, with the resistance matrix

```matrix
lhs: R  =
style: bracket
R_11 ; −R_12 ; −R_13
−R_21 ; R_22 ; −R_23
−R_31 ; −R_32 ; R_33
```

- R_kk = **sum of all resistances in mesh k** (always positive)
- R_jk = **negative of the resistance shared** between meshes j and k
- V_k = sum of source voltages **driving** mesh current k (a rise in the
  direction of travel counts positive)

As with nodal, the resistance matrix is **symmetric** when no dependent sources
are present. Note the structural duality with Module 05: conductance ↔
resistance, node voltage ↔ mesh current, current source ↔ voltage source. The
two methods are the same idea viewed from opposite sides.

## 6.3 Current sources: three cases

**Case 1 — current source in one mesh only.** That mesh current is *known*
immediately: i_k = ±I_s. One fewer unknown.

**Case 2 — current source shared between two meshes: the supermesh.**
You cannot write KVL through an ideal current source (its voltage is unknown).
Instead:

1. Form a **supermesh** by merging the two meshes and traversing the outer
   boundary, *avoiding* the source branch entirely.
2. Add the **constraint equation** from the source:
   i_1 − i_2 = I_s (with the sign set by the source's direction).

**Case 3 — dependent source.** Same as above, plus an equation relating the
controlling variable to mesh currents.

## 6.4 Worked examples

**Example 1 — two meshes.**
Mesh 1: 10 V source, 2 Ω, and 4 Ω shared. Mesh 2: 4 Ω shared, 6 Ω.
Both currents clockwise.

By inspection:

    (2 + 4)i_1 − 4i_2 = 10
    −4i_1 + (4 + 6)i_2 = 0

    6i_1 − 4i_2 = 10
    −4i_1 + 10i_2 = 0    ⇒   i_1 = 2.5 i_2

Substituting: 15i_2 − 4i_2 = 10 ⇒ 11i_2 = 10 ⇒ **i_2 = 0.909 A**,
**i_1 = 2.273 A**

Current in the shared 4 Ω = i_1 − i_2 = **1.364 A** (downward, in mesh 1's
direction).

Check with KVL on mesh 1: 10 − 2(2.273) − 4(1.364) = 10 − 4.545 − 5.455 = 0 ✓

**Example 2 — current source in one mesh.**
Mesh 1 contains a 3 A source on its own branch; mesh 2 contains 5 Ω and a 20 V
source, sharing an 8 Ω with mesh 1.

    i_1 = −3 A     (negative if the source pushes against the clockwise
                    assumption; take it as given here)

Mesh 2 KVL:  −8(i_2 − i_1) − 5i_2 + 20 = 0

    −8i_2 − 24 − 5i_2 + 20 = 0
    −13i_2 = 4    ⇒   i_2 = −0.3077 A

**Example 3 — supermesh.**
Meshes 1 and 2 share a branch containing a 4 A source (pointing from mesh 2 into
mesh 1). Mesh 1 also has a 12 V source and 2 Ω; mesh 2 also has 6 Ω and 3 Ω.

Constraint from the source:

    i_1 − i_2 = 4

Supermesh KVL around the outer boundary (skipping the source branch):

    12 − 2i_1 − 6i_2 − 3i_2 = 0
    12 − 2i_1 − 9i_2 = 0

Substituting i_1 = i_2 + 4:

    12 − 2i_2 − 8 − 9i_2 = 0
    4 = 11i_2   ⇒   i_2 = 0.364 A,   i_1 = 4.364 A

Check: 12 − 2(4.364) − 9(0.364) = 12 − 8.727 − 3.273 = 0 ✓

**Example 4 — three meshes by inspection.**
Mesh 1: 1 Ω, 2 Ω shared with mesh 2, driven by 9 V.
Mesh 2: 2 Ω shared with 1, 3 Ω, 4 Ω shared with mesh 3.
Mesh 3: 4 Ω shared with 2, 5 Ω.

    (1+2)i_1 − 2i_2 + 0     = 9
    −2i_1 + (2+3+4)i_2 − 4i_3 = 0
    0 − 4i_2 + (4+5)i_3      = 0

    3i_1 − 2i_2        = 9
    −2i_1 + 9i_2 − 4i_3 = 0
         −4i_2 + 9i_3   = 0   ⇒   i_3 = 0.4444 i_2

Substituting into the middle equation:

    −2i_1 + 9i_2 − 1.7778i_2 = 0   ⇒   2i_1 = 7.2222i_2   ⇒   i_1 = 3.6111i_2

Then 3(3.6111i_2) − 2i_2 = 9 ⇒ 10.8333i_2 − 2i_2 = 9 ⇒ 8.8333i_2 = 9

    i_2 = 1.0189 A,   i_1 = 3.6793 A,   i_3 = 0.4528 A

Note the matrix is symmetric, and the zeros in the corners say meshes 1 and 3
share nothing — exactly as drawn.

## 6.5 Exercises

1. Two meshes: mesh 1 has 24 V and 4 Ω, shared 8 Ω, mesh 2 has 12 Ω. Find both
   mesh currents. (i_1 = 2.727 A, i_2 = 1.091 A)
2. Redo Module 05 Example 3 by mesh analysis and confirm the node voltages.
3. A supermesh problem: two meshes sharing a 2 A source, mesh 1 with 10 V and
   3 Ω, mesh 2 with 7 Ω. Find both currents.
4. State why mesh analysis cannot be applied to a non-planar circuit.
5. For Example 4, verify the power delivered by the 9 V source equals the total
   dissipated.

## Takeaways

- All mesh currents in the same direction, always. That is what makes the
  by-inspection matrix work.
- A shared resistor carries the **difference** of two mesh currents.
- Current source in one mesh ⇒ that mesh current is known. Shared ⇒ supermesh
  plus constraint.
- Mesh and nodal are duals: count meshes and nodes, then pick the smaller.
