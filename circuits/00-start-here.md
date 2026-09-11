# ELE 712 Circuit Theory I — Start Here

**Course:** ELE 712 Circuit Theory I (3 credits) — Postgraduate Diploma in
Electrical/Electronic Engineering.

**Official syllabus:** *Elementary signals. Dynamic circuit behaviour,
oscillations. First and second order systems. Laplace and Fourier transforms.
Time and frequency domain solutions of circuit equations. Stability. Transfer
function concepts. Applications of network theorems. Single phase and
three-phase circuits. Two-port network analysis. Introduction to computer-aided
analysis.*

This is a from-scratch course. The prerequisite material — network analysis —
is **taught here in Modules 01–06**, not assumed. If you already have it, skim
those and start at Module 07.

## What this subject is actually for

Real circuits have dozens of elements. Writing one equation per element gives
you an unsolvable mess. The whole of circuit theory is a set of legal moves for
**replacing a complicated thing with a simpler thing that behaves identically at
the terminals you care about**.

That sentence is the course. Every theorem here — Thévenin, Norton,
superposition, source transformation, maximum power transfer — is one such
legal move. Learn what each one is allowed to do, and what it destroys.

The phrase "at the terminals you care about" is doing heavy lifting, and is
where most marks are lost. A Thévenin equivalent reproduces the original
network's behaviour **only** at the two terminals you extracted it from. Internal
voltages, internal currents, and internal power dissipation are all wrong. More
on this in Module 09; it is the single most common misunderstanding in the
subject.

## Prerequisites

You need secondary-school algebra and the ability to solve simultaneous linear
equations (2×2 and 3×3 by hand). Calculus is needed from Module 13 onward (differentiation and
integration; the transform modules use partial fractions heavily). Modules
01–12 need none.

Everything electrical is built up from scratch:

| You need | Taught in |
|---|---|
| Charge, current, voltage, power, energy | Module 01 |
| The passive sign convention | Module 01 — do not skip this |
| Resistance, Ohm's law, sources | Module 02 |
| Series/parallel reduction, dividers, delta–wye | Module 03 |
| Kirchhoff's current and voltage laws | Module 04 |
| Nodal analysis | Module 05 |
| Mesh analysis | Module 06 |

## Course map

### Part 0 — Prerequisites (network analysis)

Not in the syllabus, but assumed by all of it. Skim if you already have it.

| Module | Title |
|---|---|
| 01 | Electrical quantities and sign conventions |
| 02 | Circuit elements, Ohm's law, sources |
| 03 | Series–parallel reduction and dividers |
| 04 | Kirchhoff's laws |
| 05 | Nodal analysis |
| 06 | Mesh analysis |

### Part 1 — Applications of network theorems

| Module | Title | Syllabus line |
|---|---|---|
| 07 | Linearity and superposition | Applications of network theorems |
| 08 | Source transformation | " |
| 09 | Thévenin's theorem | " |
| 10 | Norton's theorem | " |
| 11 | Maximum power transfer | " |
| 12 | Millman, reciprocity, substitution, Tellegen | " |

### Part 2 — Signals and dynamic behaviour

| Module | Title | Syllabus line |
|---|---|---|
| 13 | Capacitors and inductors | (needed for all of it) |
| 14 | Elementary signals | Elementary signals |
| 15 | First-order circuits | First and second order systems |
| 16 | Second-order circuits and oscillations | Dynamic circuit behaviour, oscillations |

### Part 3 — Single-phase and three-phase

| Module | Title | Syllabus line |
|---|---|---|
| 17 | AC steady state and single-phase power | Single phase circuits |
| 18 | Three-phase circuits | Three-phase circuits |

### Part 4 — Transform methods

| Module | Title | Syllabus line |
|---|---|---|
| 19 | The Laplace transform | Laplace transforms |
| 20 | Circuit analysis in the s-domain | Time and frequency domain solutions |
| 21 | Transfer functions, poles, zeros, stability | Transfer function concepts; Stability |
| 22 | Fourier series and transforms | Fourier transforms |

### Part 5 — Networks and tools

| Module | Title | Syllabus line |
|---|---|---|
| 23 | Two-port networks | Two-port network analysis |
| 24 | Computer-aided analysis | Introduction to computer-aided analysis |

### Reference

| Module | Title |
|---|---|
| 25 | Formula sheet |
| 26 | Problem set with full solutions |

## The dependency chain

Nothing here is optional in the middle:

    Sign convention → Ohm + KCL/KVL → Nodal/Mesh → Linearity
                                                      ↓
                    Superposition → Source transformation
                                                      ↓
                              Thévenin ⟷ Norton → Max power transfer
                                     ↓
              C and L → first order → second order → phasors (AC)
                                     ↓                    ↓
                          Laplace → s-domain      three-phase
                                     ↓
                  transfer functions → stability → Fourier
                                     ↓
                          two-port → simulation

Superposition is what makes Thévenin legal. Thévenin is what makes maximum power
transfer computable — and R_th is also what sets the time constant in Module 15.
Phasors (17) are the s-domain (20) restricted to s = jω. Stability (21) is just
"where are the poles", and the poles are the same natural frequencies you met as
α and ω_0 in Module 16.

If a topic ever feels arbitrary, the reason is almost always that the link above
it was skipped.

## How to use this

Read a module, then close it and rework its examples on blank paper **without
looking at the circuit description twice**. Circuit theory is not conceptually
hard; it is bookkeeping-hard. The marks go to whoever keeps their signs and
labels straight under time pressure, and that is a trained skill, not an
understood one.

Every module ends with exercises that have answers. Module 26 has 20 full
problems with complete solutions.

**If you are short of time**, the syllabus weights are not equal. Modules 19–21
(Laplace, s-domain, transfer functions and stability) account for four of the
eleven syllabus lines and are the spine of the course; Modules 15–16 feed
straight into them. The network theorems of Part 1 are one syllabus line, though
they are also the prerequisite for finding R_th in Module 15.

## Notation used throughout

- Uppercase V, I for DC or RMS values; lowercase v, i for instantaneous.
- V_s, I_s for sources; V_th, R_th for Thévenin; I_N, R_N for Norton.
- Ω for ohms, S for siemens, ∥ for "in parallel with".
- R_1 ∥ R_2 means R_1R_2/(R_1 + R_2).
- s = σ + jω is complex frequency; ω = 2πf; τ is a time constant.
- ℒ{f(t)} = F(s) is the Laplace transform; H(s) a transfer function.
