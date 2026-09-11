# Module 05 — Nodal Analysis

Nodal analysis is KCL applied systematically. It produces the **smallest set of
equations** whenever a circuit has more branches than nodes — which is most of
the time.

## 5.1 The method

1. Identify all nodes. Choose one as the **reference (ground)**, ideally the one
   with most connections or the − terminal of a source. Its voltage is 0.
2. Label the remaining node voltages V_1, V_2, … These are your unknowns —
   there are (n − 1) of them.
3. Write **KCL at each non-reference node**, expressing every branch current in
   terms of node voltages via Ohm's law.
4. Solve the simultaneous equations.

The key step is 3. For a resistor R between nodes A and B, the current **leaving
node A through R** is

    i = (V_A − V_B)/R

Always write it as *(this node − other node) / R*. Being mechanical about that
eliminates almost all sign errors.

## 5.2 The standard form

For a circuit with only resistors and **current** sources, KCL at every node
collapses to the single matrix equation **GV = I**, with the conductance matrix

```matrix
lhs: G  =
style: bracket
G_11 ; −G_12 ; −G_13
−G_21 ; G_22 ; −G_23
−G_31 ; −G_32 ; G_33
```

where

- G_kk = **sum of all conductances connected to node k** (always positive)
- G_jk = **negative of the conductance directly between nodes j and k**
- I_k = sum of source currents **entering** node k

This "by inspection" form works **only** when every source is an independent
current source. Voltage sources need the treatment in §5.3, and dependent
sources break the symmetry of the matrix.

The conductance matrix is **symmetric** (G_jk = G_kj) for circuits without
dependent sources. If yours comes out asymmetric and you have no dependent
sources, you have made an error — a genuinely useful check.

## 5.3 Voltage sources: three cases

**Case 1 — source between a node and ground.** That node's voltage is simply
*known*. Write V_k = V_s and remove it from the unknowns. This is the easiest
possible situation, so choose your ground to create it whenever you can.

**Case 2 — source between two non-reference nodes: the supernode.**
You cannot write Ohm's law for the source branch (an ideal source has no
resistance). Instead:

1. Enclose both nodes in a **supernode** and write KCL for the whole enclosure —
   legal because KCL applies to any closed surface.
2. Add the **constraint equation** from the source itself:
   V_A − V_B = V_s.

Two equations, two unknowns, no need to know the source current.

**Case 3 — a dependent source.** Treat it as above, then add an equation
expressing its controlling variable in terms of node voltages.

## 5.4 Worked examples

**Example 1 — two unknown nodes, current sources only.**
A 4 A source feeds node 1. Node 1 connects to ground through 2 Ω, and to node 2
through 4 Ω. Node 2 connects to ground through 8 Ω and has a 2 A source feeding
it. Find V_1 and V_2.

Conductances: 1/2 = 0.5, 1/4 = 0.25, 1/8 = 0.125 S

Node 1: (0.5 + 0.25)V_1 − 0.25V_2 = 4
Node 2: −0.25V_1 + (0.25 + 0.125)V_2 = 2

    0.75V_1 − 0.25V_2 = 4
    −0.25V_1 + 0.375V_2 = 2

From the first: V_1 = (4 + 0.25V_2)/0.75. Substituting:

    −0.25(4 + 0.25V_2)/0.75 + 0.375V_2 = 2
    −(1 + 0.0625V_2)/0.75 + 0.375V_2 = 2
    −1.3333 − 0.08333V_2 + 0.375V_2 = 2
    0.29167V_2 = 3.3333   ⇒   V_2 = 11.43 V
    V_1 = (4 + 2.857)/0.75 = 9.14 V

Check by KCL at node 1: (9.14)/2 + (9.14 − 11.43)/4 = 4.571 − 0.571 = 4.0 ✓

**Example 2 — voltage source to ground.**
A 12 V source sits between node 1 and ground. Node 1 connects to node 2 through
3 Ω; node 2 goes to ground through 6 Ω and carries a 2 A source into it.

    V_1 = 12 V (known immediately)

Node 2: (V_2 − 12)/3 + V_2/6 = 2

    2(V_2 − 12) + V_2 = 12
    3V_2 = 36    ⇒   V_2 = 12 V

With V_2 = 12 V there is no current in the 3 Ω at all, and the whole 2 A flows
through the 6 Ω. Check: 12/6 = 2 A ✓

**Example 3 — supernode.**
Nodes 1 and 2 are joined by an 8 V source (+ at node 1). Node 1 connects to
ground through 4 Ω; node 2 connects to ground through 2 Ω. A 3 A source feeds
node 1 from ground.

Supernode KCL (currents leaving the enclosure into the resistors equal the 3 A
entering):

    V_1/4 + V_2/2 = 3

Constraint:

    V_1 − V_2 = 8   ⇒   V_1 = V_2 + 8

Substituting:

    (V_2 + 8)/4 + V_2/2 = 3
    (V_2 + 8) + 2V_2 = 12
    3V_2 = 4    ⇒   V_2 = 1.333 V,   V_1 = 9.333 V

Check: 9.333/4 + 1.333/2 = 2.333 + 0.667 = 3.0 ✓

**Example 4 — dependent source.**
Node 1 has a 6 A source into it, connects to ground via 2 Ω and to node 2 via
1 Ω. Node 2 connects to ground via 3 Ω and also carries a VCCS of 2v_x into it,
where v_x is the voltage across the 2 Ω (i.e. v_x = V_1).

Node 1: V_1/2 + (V_1 − V_2)/1 = 6
Node 2: (V_2 − V_1)/1 + V_2/3 = 2V_1

From node 1:  1.5V_1 − V_2 = 6
From node 2:  −V_1 + V_2 + V_2/3 = 2V_1  ⇒  −3V_1 + 1.3333V_2 = 0
            ⇒  V_2 = 2.25V_1

Substituting: 1.5V_1 − 2.25V_1 = 6 ⇒ −0.75V_1 = 6 ⇒ **V_1 = −8 V**,
**V_2 = −18 V**

A negative node voltage is perfectly legal — the dependent source is driving the
node below ground.

## 5.5 Choosing nodal or mesh

| Prefer nodal when | Prefer mesh when |
|---|---|
| Fewer nodes than meshes | Fewer meshes than nodes |
| Current sources dominate | Voltage sources dominate |
| You want node voltages | You want branch currents |
| Circuit is non-planar | (mesh is impossible — nodal is your only option) |

Count both before starting. Choosing the better method halves the work, and
costs ten seconds.

## 5.6 Exercises

1. Two nodes joined by 5 Ω; node 1 to ground via 10 Ω with 3 A in; node 2 to
   ground via 20 Ω. Find V_1, V_2. (V_1 = 21.43 V, V_2 = 17.14 V)
2. Redo Example 1 using conductances written straight into the matrix by
   inspection, and confirm the matrix is symmetric.
3. A 10 V source sits between nodes 1 and 2, with node 1 to ground via 5 Ω and
   node 2 to ground via 5 Ω, and a 4 A source into node 2. Find both voltages.
4. Why is the (n−1)th KCL equation sufficient — what happened to the nth?
5. Convert the circuit of Example 3 into mesh form and confirm the same answer.

## Takeaways

- Ground the busiest node, or the one that turns a voltage source into a known.
- Current out of node A through R is always (V_A − V_other)/R.
- A voltage source between two live nodes ⇒ supernode + constraint equation.
- The conductance matrix is symmetric unless dependent sources are present.
