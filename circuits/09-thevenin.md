# Module 09 — Thévenin's Theorem

The central result of the course.

## 9.1 Statement

> Any linear two-terminal network, however complicated, can be replaced — **as
> seen from those two terminals** — by a single voltage source V_th in series
> with a single resistance R_th.

- **V_th** = the **open-circuit voltage** at the terminals
- **R_th** = the resistance looking back into the network with all **independent**
  sources deactivated

## 9.2 What "as seen from those two terminals" means

This is the sentence that decides whether you understand the theorem.

The equivalent reproduces the original network's **v–i relationship at the
terminals**. Connect any load you like and it will draw exactly the same current
and sit at exactly the same voltage as it would have in the original circuit.

It reproduces **nothing else**:

- Internal node voltages are wrong.
- Internal branch currents are wrong.
- **Internal power dissipation is wrong.** The power in R_th is *not* the power
  lost inside the original network.

So: use Thévenin to find what happens to the **load**. Never use it to answer a
question about the interior of the network you replaced. If a problem asks for
the power dissipated by a resistor that got absorbed into R_th, you must go back
to the original circuit.

## 9.3 Finding V_th

Remove the load, leaving the terminals open. Find the voltage across them by any
method — nodal, mesh, divider, superposition, source transformation.

**Note:** with the load removed, no current flows in the branch that led to it,
so any resistance in series with the open terminals drops zero volts and can be
ignored when computing V_th (though it still counts toward R_th).

## 9.4 Finding R_th — three methods

### Method 1 — Deactivate and reduce (no dependent sources)

Turn off all independent sources (voltage → short, current → open) and reduce
the resulting resistor network by series/parallel from the terminals inward.

Fastest when it applies. It applies **only** if there are no dependent sources.

### Method 2 — Test source (works always, required with dependent sources)

Deactivate the **independent** sources only; leave dependent sources active.
Then either:

- Apply a 1 V test source across the terminals, find the current I drawn, and
  take R_th = 1/I; or
- Apply a 1 A test source, find the voltage V, and take R_th = V/1.

Use this whenever a dependent source is present. Method 1 is simply invalid
there, because you may not deactivate a dependent source.

### Method 3 — Open-circuit / short-circuit

    R_th = V_oc / I_sc

where V_oc = V_th is the open-circuit voltage and I_sc is the current that flows
when the terminals are shorted together.

Works always, including with dependent sources, and is often the least error-
prone because both quantities are ordinary circuit-analysis problems. Its one
failure case: a network with V_th = 0 and I_sc = 0 gives 0/0, and you must fall
back to Method 2.

## 9.5 Worked examples

**Example 1 — plain resistive network.**
A 12 V source in series with 4 Ω, with 12 Ω from the junction to ground, and
terminals a–b across the 12 Ω. Find the Thévenin equivalent and then the current
in a 6 Ω load.

*V_th* (load removed, simple divider):

    V_th = 12 × 12/(4+12) = 9 V

*R_th* (12 V shorted; 4 Ω now parallel with 12 Ω):

    R_th = 4 ∥ 12 = 48/16 = 3 Ω

*Load current:*

    I_L = V_th/(R_th + R_L) = 9/(3+6) = 1 A

Check directly: with the 6 Ω in place, 12 ∥ 6 = 4 Ω, total 8 Ω, source current
12/8 = 1.5 A, node voltage 1.5 × 4 = 6 V, so I_6 = 6/6 = 1 A ✓

**Example 2 — two sources, using superposition for V_th.**
A 20 V source through 5 Ω and a 10 V source through 20 Ω both feed terminals
a–b, which also has a 4 Ω to ground.

*V_th* by nodal (terminals open, so the 4 Ω is the only path to ground):

    (V − 20)/5 + (V − 10)/20 + V/4 = 0
    4(V − 20) + (V − 10) + 5V = 0
    4V − 80 + V − 10 + 5V = 0
    10V = 90   ⇒   V_th = 9 V

*R_th* (both sources shorted): 5 ∥ 20 ∥ 4

    1/R_th = 1/5 + 1/20 + 1/4 = 0.2 + 0.05 + 0.25 = 0.5
    R_th = 2 Ω

**Example 3 — open-circuit/short-circuit method.**
Same circuit as Example 1. Short a–b: the 12 Ω is shorted out, so

    I_sc = 12/4 = 3 A
    R_th = V_oc/I_sc = 9/3 = 3 Ω ✓

**Example 4 — with a dependent source (test-source method).**
A network has a 4 Ω from terminal a to node x, a 2 Ω from x to ground, a 6 V
independent source driving x through the 2 Ω branch, and a VCCS of 0.5v_x from
x to ground, where v_x is the voltage across the 2 Ω.

*R_th:* deactivate the 6 V (short it), keep the VCCS. Apply a 1 V test source
at a–b. Let node x be at v_x.

KCL at x (currents leaving x): through the 2 Ω to ground, through the dependent
source, and back through the 4 Ω to the test source:

    v_x/2 + 0.5v_x + (v_x − 1)/4 = 0
    Multiply by 4:  2v_x + 2v_x + v_x − 1 = 0
    5v_x = 1   ⇒   v_x = 0.2 V

Test-source current (into the network through the 4 Ω):

    I = (1 − v_x)/4 = 0.8/4 = 0.2 A
    R_th = 1/0.2 = 5 Ω

Note that Method 1 would have given 4 + 2 = 6 Ω — wrong, because it illegally
removes the dependent source's effect.

## 9.6 Exercises

1. A 30 V source in series with 10 Ω, with 20 Ω across the output terminals.
   Find V_th and R_th. (20 V, 6.67 Ω)
2. Using Example 2's equivalent, find the current delivered to a 3 Ω load.
   (1.8 A)
3. A network has V_oc = 15 V and I_sc = 2.5 A. Find R_th and the load current
   into 4 Ω. (6 Ω; 1.5 A)
4. Explain why the power dissipated in R_th does not equal the power lost inside
   the original network.
5. A network containing a CCVS has its independent sources deactivated, and
   series/parallel reduction gives 8 Ω. Why is that answer not R_th?

## Takeaways

- V_th = open-circuit voltage; R_th = resistance looking in with **independent**
  sources off.
- Three routes to R_th: reduce (no dependent sources), test source (always),
  or V_oc/I_sc (always).
- The equivalent is valid **only at the terminals**. Internal currents, voltages
  and powers are not preserved.
- Dependent sources are never deactivated — this is where most marks are lost.
