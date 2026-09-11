# Module 04 — Kirchhoff's Laws

Ohm's law describes one element. Kirchhoff's laws describe how elements
**constrain each other** once wired together. Together they are sufficient to
solve any lumped circuit — everything later in this course is a shortcut built
on top of them.

## 4.1 Vocabulary

- **Node** — a point where two or more elements meet. An *essential node* joins
  three or more.
- **Branch** — a single element (or unbroken series chain) between two nodes.
- **Loop** — any closed path that returns to its start without passing any node
  twice.
- **Mesh** — a loop containing no other loop inside it. Only planar circuits
  have meshes.

A wire with no element in it is **not** a new node — both its ends are the
*same* node. Redrawing a circuit to collapse wires into single nodes before
starting is often the single most useful step.

## 4.2 Kirchhoff's Current Law (KCL)

> The algebraic sum of currents entering any node is zero.

    Σ i_in = 0        or equivalently        Σ i_in = Σ i_out

**Why it is true:** charge cannot accumulate at a node. A node is an idealised
point with no capacity to store charge, so whatever flows in must flow out at
the same instant.

KCL also applies to any **closed surface** drawn around a group of nodes (a
"supernode" or "Gaussian surface" argument). That generalisation is what makes
supernodes work in Module 05.

## 4.3 Kirchhoff's Voltage Law (KVL)

> The algebraic sum of voltages around any closed loop is zero.

    Σ v = 0

**Why it is true:** voltage is potential difference. Walking a closed loop
returns you to your starting potential, so the rises and drops must cancel.

**Applying it without sign errors — a fixed procedure:**

1. Choose a loop direction (clockwise is a fine default; keep it for all loops).
2. Walk the loop. At each element, write the sign of the terminal you **enter
   first**.
3. Enter at − and leave at + → that is a **rise**, write +v. Enter at + → a
   **drop**, write −v.
4. Set the total to zero.

For a resistor with assumed current i, walking *with* the current gives a drop
of −iR; walking *against* it gives +iR.

Do it the same way every time and the signs stop being a source of error.

## 4.4 The branch-current method

The most direct application of the two laws, and the conceptual ancestor of
nodal and mesh analysis.

1. Label a current in every branch, with an arrow.
2. Write KCL at every essential node **except one** (the last is redundant — it
   is implied by the others).
3. Write KVL around enough loops to reach as many equations as unknowns.
4. Solve.

For a circuit with b branches and n nodes, you need b equations:
(n − 1) from KCL, and b − (n − 1) from KVL.

This method works always but generates many unknowns. Nodal and mesh analysis
(Modules 05–06) are systematic ways of reducing the count before you start.

## 4.5 Worked examples

**Example 1.** Three branches meet at a node. 5 A enters, 2 A leaves. Find the
third branch current and its direction.

    Σ i_in = 0:   5 − 2 − i_3 = 0   ⇒   i_3 = 3 A leaving

**Example 2.** A single loop contains a 20 V source, and resistors 3 Ω, 5 Ω and
2 Ω in series. Find the current and the voltage across each resistor.

KVL clockwise, current i assumed clockwise from the + terminal of the source:

    20 − 3i − 5i − 2i = 0
    20 = 10i     ⇒   i = 2 A

    V_3 = 6 V,  V_5 = 10 V,  V_2 = 4 V     (sum = 20 V ✓)

**Example 3 (two sources, opposing).** A loop contains a 12 V source and a 4 V
source connected in opposition, with 2 Ω and 6 Ω in series. Find i.

Take clockwise, entering the 12 V at − (a rise) and the 4 V at + (a drop):

    12 − 2i − 4 − 6i = 0
    8 = 8i      ⇒   i = 1 A

Power check:
- 12 V source delivers 12 × 1 = 12 W
- 4 V source **absorbs** 4 × 1 = 4 W (it is being charged)
- Resistors absorb 1²(2) + 1²(6) = 8 W
- Total absorbed: −12 + 4 + 8 = 0 ✓

**Example 4 (branch-current method).** Two sources, one shared branch.
V_1 = 10 V in series with 2 Ω on the left; V_2 = 6 V in series with 3 Ω on the
right; a 4 Ω resistor connects the common node to the common reference.

Let i_1 flow in from the left branch, i_2 in from the right, and i_3 down
through the 4 Ω.

KCL at the top node:

    i_1 + i_2 = i_3

KVL left loop: 10 − 2i_1 − 4i_3 = 0
KVL right loop: 6 − 3i_2 − 4i_3 = 0

Substituting i_3 = i_1 + i_2:

    10 = 2i_1 + 4i_1 + 4i_2 = 6i_1 + 4i_2
    6  = 3i_2 + 4i_1 + 4i_2 = 4i_1 + 7i_2

Solving: from the first, i_1 = (10 − 4i_2)/6. Substituting,

    4(10 − 4i_2)/6 + 7i_2 = 6
    (40 − 16i_2)/6 + 7i_2 = 6
    40 − 16i_2 + 42i_2 = 36
    26i_2 = −4    ⇒   i_2 = −0.1538 A
    i_1 = (10 + 0.6154)/6 = 1.769 A
    i_3 = 1.769 − 0.154 = 1.615 A

The negative i_2 says the right-hand source is being charged, not discharged —
a perfectly valid result, and exactly the kind of thing you must not "fix" by
flipping an arrow midway.

Check with KVL on the left loop: 10 − 2(1.769) − 4(1.615) = 10 − 3.538 − 6.462
= 0 ✓

## 4.6 Exercises

1. At a node, currents of 3 A and 7 A enter and 4 A leaves. Find the fourth
   branch current. (6 A leaving)
2. A loop has a 15 V source and 4 Ω, 6 Ω in series. Find i and each voltage.
   (1.5 A; 6 V, 9 V)
3. Repeat Example 3 with the 4 V source reversed so it aids the 12 V source.
   (i = 2 A)
4. How many independent KCL and KVL equations does a circuit with 6 branches
   and 4 nodes require? (3 KCL, 3 KVL)
5. Show that in Example 4 the total power delivered equals the total absorbed.

## Takeaways

- KCL is charge conservation at a node; KVL is energy conservation around a loop.
- Pick one loop direction and one sign rule, and never vary them.
- (n − 1) KCL equations, the rest KVL. The last KCL equation is always redundant.
- A negative current is an answer, not a mistake.
