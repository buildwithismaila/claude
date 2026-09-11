# Module 23 — Two-Port Networks

Thévenin reduced a network to a **one-port** — a single pair of terminals. Many
real blocks have two pairs: an input port and an output port. Amplifiers,
filters, transmission lines, transformers and attenuators are all two-ports.

A two-port is characterised by four numbers relating the four terminal
quantities V_1, I_1, V_2, I_2 — with no need to know anything about what is
inside.

**Convention:** both currents flow **into** the positive terminal of their port.

## 23.1 The six parameter sets

Which two of the four variables you treat as independent gives six choices.

### z-parameters (open-circuit impedance)

    V_1 = z_11 I_1 + z_12 I_2
    V_2 = z_21 I_1 + z_22 I_2

```matrix
lhs: z  =
style: bracket
z_11 ; z_12
z_21 ; z_22
```

Found by **open-circuiting** one port at a time:

    z_11 = V_1/I_1 |_{I_2=0}     input impedance, output open
    z_12 = V_1/I_2 |_{I_1=0}     reverse transfer impedance
    z_21 = V_2/I_1 |_{I_2=0}     forward transfer impedance
    z_22 = V_2/I_2 |_{I_1=0}     output impedance, input open

### y-parameters (short-circuit admittance)

    I_1 = y_11 V_1 + y_12 V_2
    I_2 = y_21 V_1 + y_22 V_2

Found by **short-circuiting** one port at a time. The y-matrix is the inverse of
the z-matrix: **[y] = [z]⁻¹**.

### h-parameters (hybrid)

    V_1 = h_11 I_1 + h_12 V_2
    I_2 = h_21 I_1 + h_22 V_2

- h_11 = input impedance (Ω), output shorted
- h_12 = reverse voltage gain (dimensionless)
- h_21 = forward current gain (dimensionless) — **this is transistor β**
- h_22 = output admittance (S), input open

Mixed units, hence "hybrid". These are the standard parameters for bipolar
transistors, which is why they matter far beyond circuit theory.

### Transmission (ABCD) parameters

    V_1 = A V_2 − B I_2
    I_1 = C V_2 − D I_2

Note the **minus signs**: here I_2 is taken as flowing *out* of the network, so
that cascaded stages chain naturally. A is dimensionless, B in Ω, C in S, D
dimensionless.

**The cascade property** is why these exist:

> Two-ports in cascade multiply their ABCD matrices, in order.

That single fact makes ABCD the parameter set for transmission lines and
multi-stage filters.

Also defined: g-parameters (the inverse hybrid) and the inverse transmission
parameters, both rarely used.

## 23.2 Reciprocity and symmetry

| Property | Condition |
|---|---|
| **Reciprocal** | z_12 = z_21, or y_12 = y_21, or AD − BC = 1, or h_12 = −h_21 |
| **Symmetric** | z_11 = z_22, or A = D |

Any network built only from R, L, C and transformers (no dependent sources) is
**reciprocal** — this is Module 12's reciprocity theorem expressed in parameters.
A network containing a dependent source (an amplifier) generally is not, which
is exactly what makes it useful as an amplifier: signal goes forward but not
backward.

**Symmetric** means the two ports are interchangeable — the network looks the
same from either end.

## 23.3 Interconnections

| Connection | Parameters that add |
|---|---|
| Series (both ports in series) | **z** matrices add |
| Parallel (both ports in parallel) | **y** matrices add |
| Cascade (output to input) | **ABCD** matrices multiply |
| Series–parallel | **h** matrices add |

Each parameter set exists because it makes one interconnection trivial. Choose
the set that matches how your blocks are wired.

## 23.4 Conversions

All six sets describe the same network, so any can be converted to any other.
The two you should know:

    [y] = [z]⁻¹

For z from ABCD:

    z_11 = A/C,  z_12 = (AD − BC)/C,  z_21 = 1/C,  z_22 = D/C

And ABCD from z:

    A = z_11/z_21,  B = Δz/z_21,  C = 1/z_21,  D = z_22/z_21

where Δz = z_11z_22 − z_12z_21.

## 23.5 Worked examples

**Example 1 — z-parameters of a T network.**
A T network: Z_a in the input series arm, Z_b in the shunt arm to ground, Z_c in
the output series arm.

With port 2 open (I_2 = 0), no current flows in Z_c:

    z_11 = V_1/I_1 = Z_a + Z_b
    z_21 = V_2/I_1 = Z_b        (V_2 is the voltage across Z_b)

With port 1 open (I_1 = 0):

    z_22 = Z_b + Z_c
    z_12 = Z_b

Since z_12 = z_21 = Z_b, the network is **reciprocal** ✓ (as it must be — it is
passive).

Numerically, with Z_a = 10 Ω, Z_b = 20 Ω, Z_c = 30 Ω:

```matrix
lhs: z  =
style: bracket
30 Ω ; 20 Ω
20 Ω ; 50 Ω
```

**Example 2 — ABCD of a series impedance.**
A single series Z between the ports.

    V_1 = V_2 + I_1 Z,  and  I_1 = −I_2

    A = 1,  B = Z,  C = 0,  D = 1

Check reciprocity: AD − BC = 1 − 0 = 1 ✓

**Example 3 — ABCD of a shunt admittance.**
A single shunt Y across the output.

    A = 1,  B = 0,  C = Y,  D = 1

**Example 4 — cascade.**
Cascade a 10 Ω series element with a 0.05 S shunt element.

```matrix
lhs: T  =
style: bracket
1 ; 10
0 ; 1
```

times

```matrix
lhs: ×
style: bracket
1 ; 0
0.05 ; 1
```

Multiplying:

    A = 1(1) + 10(0.05) = 1.5
    B = 1(0) + 10(1) = 10
    C = 0(1) + 1(0.05) = 0.05
    D = 0(0) + 1(1) = 1

Check: AD − BC = 1.5 − 0.5 = 1 ✓ — still reciprocal, as a passive cascade must
be.

**Example 5 — input impedance with a load.**
A two-port with known z-parameters drives a load Z_L. Then V_2 = −I_2 Z_L, and

    Z_in = z_11 − z_12 z_21/(z_22 + Z_L)

With the T network of Example 1 and Z_L = 50 Ω:

    Z_in = 30 − (20)(20)/(50 + 50) = 30 − 400/100 = 26 Ω

Sanity check directly: 10 + [20 ∥ (30 + 50)] = 10 + (20×80)/100 = 10 + 16 = 26 Ω ✓

## 23.6 Exercises

1. Find the z-parameters of a π network with shunt 10 Ω, series 20 Ω, shunt
   10 Ω.
2. Find ABCD for a 5 Ω series element cascaded with a 0.1 S shunt, and verify
   AD − BC = 1.
3. A two-port has h_21 = 100 and h_11 = 2 kΩ. What kind of device is this
   likely to model, and what does h_21 represent?
4. Show that for a symmetric T network, A = D.
5. Two identical two-ports are connected in parallel. If each has
   y_11 = 0.05 S, what is y_11 of the combination? (0.1 S)

## Takeaways

- Four numbers describe any two-port from outside; six equivalent sets exist.
- z from open circuits, y from short circuits, h mixes both, ABCD cascades.
- Reciprocal ⟺ z_12 = z_21 ⟺ AD − BC = 1; passive networks always are.
- Pick the parameter set that makes your interconnection add or multiply.
