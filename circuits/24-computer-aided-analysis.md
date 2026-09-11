# Module 24 — Introduction to Computer-Aided Analysis

Hand analysis stops being practical somewhere around four or five nodes with
reactive elements. Every real design is checked by simulation. This module covers
what the tools are actually doing, which matters because a simulator that is
quietly wrong is more dangerous than no simulator at all.

## 24.1 What SPICE does

SPICE (Simulation Program with Integrated Circuit Emphasis, Berkeley, 1973) and
its descendants — LTspice, PSpice, Ngspice, Multisim, and the engines inside
Proteus and Altium — all work the same way.

The core algorithm is **modified nodal analysis (MNA)** — Module 05, generalised:

1. Write KCL at every node in terms of node voltages, exactly as you learned.
2. **Modify** it to handle elements whose current cannot be written in terms of
   node voltages — ideal voltage sources and inductors — by adding their branch
   current as an extra unknown, with an extra equation.
3. Assemble and solve the resulting matrix **Ax = b** by LU decomposition.

So the simulator is doing your nodal analysis, on a matrix of a few thousand
unknowns, a few thousand times per second. Understanding Module 05 is
understanding SPICE.

## 24.2 The four analysis types

| Analysis | SPICE name | What it computes | Your module |
|---|---|---|---|
| DC operating point | `.op` | Steady-state node voltages; L shorted, C opened | 05, 13 |
| DC sweep | `.dc` | Output vs a swept source value | 05 |
| **Transient** | `.tran` | v(t), i(t) by numerical integration | 15, 16 |
| **AC (small-signal)** | `.ac` | Magnitude and phase vs frequency | 17, 21 |

Two more that matter:
- **`.noise`** — noise contributions referred to input or output.
- **Monte Carlo / worst-case** — sweeps component tolerances to check whether a
  design survives real parts, not ideal ones.

### Transient analysis

The differential equations are integrated numerically, stepping forward in time.
Methods: backward Euler (robust, damps artificially), trapezoidal (SPICE's
default, accurate but can ring), and Gear (good for stiff circuits).

The simulator chooses step size adaptively — small where things change fast. The
consequence you will meet: `.tran` results depend on the step size, so a
suspiciously clean or suspiciously noisy result should always be re-run with a
tighter maximum step.

### AC analysis is linear only

`.ac` **linearises the circuit around its DC operating point** and then solves
with complex impedances — exactly Module 17. Two consequences:

- The result is a frequency response, and it is meaningless if the circuit is
  genuinely nonlinear at signal level.
- Amplitude is irrelevant in `.ac`; you can ask for 1 V input and get gain
  directly. A "10 V" output in an AC analysis does not mean the real circuit
  would swing 10 V — it might clip long before.

That last point is one of the commonest misreadings of simulator output.

## 24.3 Netlists

Every schematic is compiled to a **netlist** — a text list of elements and the
nodes they connect. Node 0 is always ground.

    * RC low-pass filter
    V1  in  0   AC 1  PULSE(0 5 0 1n 1n 1m 2m)
    R1  in  out 1k
    C1  out 0   1u
    .tran 0 10m
    .ac dec 100 1 100k
    .end

Reading that: a source V1 between node `in` and ground; a 1 kΩ from `in` to
`out`; a 1 μF from `out` to ground; run a transient to 10 ms and an AC sweep
from 1 Hz to 100 kHz at 100 points per decade.

Element letters: R, L, C, V, I, D (diode), Q (BJT), M (MOSFET), E/G/F/H (the
four dependent sources of Module 02).

Being able to read a netlist matters because it is the unambiguous
representation — schematics can hide connection errors that a netlist makes
obvious.

## 24.4 Where simulators go wrong

Worth taking seriously; these cause real design failures.

**Convergence failure.** The solver iterates (Newton–Raphson) and sometimes fails
to settle. Causes: no DC path to ground from some node, a floating node, ideal
switches with zero resistance, or a loop of ideal voltage sources — the same
illegal connections flagged in Module 02. Fixes: add a large resistor to ground,
add small series resistance to ideal sources, relax tolerances.

**Ideal components.** A simulated capacitor has no ESR, no lead inductance and
no voltage coefficient. A real one has all three. Circuits that only work in
simulation usually depend on some ideality.

**Model quality.** Results are only as good as the device models. A transistor
model from a vendor at 25 °C says nothing about behaviour at 85 °C.

**Numerical artefacts.** Trapezoidal integration can produce ringing that is not
physical. Re-run with a different method or smaller step before believing an
oscillation.

> **The rule:** a simulator answers the question you asked about the circuit you
> entered. It does not check that either was sensible. Always sanity-check the
> result against hand analysis — which is why Modules 01–23 come first, not
> instead.

## 24.5 A worked verification

Take the RC low-pass of Module 21 Example 1: R = 1 kΩ, C = 1 μF.

**Hand analysis:**

    f_c = 1/(2πRC) = 1/(2π × 10³ × 10⁻⁶) = 159.15 Hz
    τ = RC = 1 ms, so a step settles in 5τ = 5 ms
    Gain at f_c = 0.707 (−3 dB), phase = −45°

**What the simulator should show:**
- `.ac` — magnitude flat at 0 dB below 159 Hz, falling at −20 dB/decade above,
  passing −3 dB at 159 Hz, phase going 0° → −45° at f_c → −90°.
- `.tran` with a 5 V step — an exponential rise reaching 3.16 V at 1 ms
  (63.2%) and essentially 5 V by 5 ms.

If the simulation disagrees with either, **the simulation is wrong or the
netlist is wrong** — not the mathematics. That is the discipline: hand analysis
predicts, simulation confirms, and disagreement is a bug to be found.

## 24.6 Tools worth knowing

| Tool | Notes |
|---|---|
| **LTspice** | Free, fast, industry standard. The default recommendation. |
| **Ngspice** | Open source, scriptable, engine behind many front ends. |
| **PSpice** | Commercial, common in universities. |
| **Multisim** | Strong instrument-style interface, good for teaching. |
| **MATLAB/Octave** | For solving the matrix equations directly, and for control-style analysis of H(s) — poles, Bode plots, step response. |
| **Python (NumPy/SciPy)** | `scipy.signal` handles transfer functions, Bode plots and step responses in a few lines. |

For this course specifically, the two most useful things you can do
computationally: solve nodal/mesh matrices numerically to check hand answers,
and plot |H(jω)| from a transfer function to check a filter design.

## 24.7 Exercises

1. Write a netlist for a series RLC with R = 10 Ω, L = 1 mH, C = 1 μF driven by
   a 1 V AC source, and add the line for an AC sweep from 100 Hz to 1 MHz.
2. For that circuit, hand-compute ω_0 and Q, and state where the peak should
   appear. (ω_0 = 31,623 rad/s ⇒ 5033 Hz; Q = 3.16)
3. A simulation of a passive RLC shows a growing oscillation. What are the two
   possible explanations, and which is more likely?
4. Explain why `.ac` analysis cannot predict clipping.
5. Give two circuit constructions that commonly cause convergence failure and
   the fix for each.

## Takeaways

- SPICE is modified nodal analysis plus numerical integration — Module 05 at
  scale.
- `.op`, `.dc`, `.tran`, `.ac` map directly onto the analyses you have learned
  by hand.
- `.ac` is linearised and amplitude-blind; it cannot show clipping.
- Convergence failures usually mean an idealisation the solver cannot handle.
- Hand analysis predicts, simulation confirms. Disagreement means a bug.
