# Circuit Theorems I — Start Here

**Course:** Circuit Theorems I — Postgraduate Diploma in Electrical/Electronic
Engineering.

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
equations (2×2 and 3×3 by hand). Calculus is **not** required until Module 13,
and even there only lightly.

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

| Module | Title | Role |
|---|---|---|
| 01 | Electrical quantities and sign conventions | Prerequisite |
| 02 | Circuit elements, Ohm's law, sources | Prerequisite |
| 03 | Series–parallel reduction and dividers | Prerequisite |
| 04 | Kirchhoff's laws | Prerequisite |
| 05 | Nodal analysis | Network analysis |
| 06 | Mesh analysis | Network analysis |
| 07 | Linearity and superposition | **Theorem** |
| 08 | Source transformation | **Theorem** |
| 09 | Thévenin's theorem | **Theorem** |
| 10 | Norton's theorem | **Theorem** |
| 11 | Maximum power transfer | **Theorem** |
| 12 | Millman, reciprocity, substitution, Tellegen | **Theorem** |
| 13 | Applying the theorems to AC | Extension |
| 14 | Formula sheet | Reference |
| 15 | Problem set with full solutions | Practice |

## The dependency chain

Nothing here is optional in the middle:

    Sign convention → Ohm + KCL/KVL → Nodal/Mesh → Linearity
                                                      ↓
                    Superposition → Source transformation
                                                      ↓
                              Thévenin ⟷ Norton → Max power transfer

Superposition is what makes Thévenin legal. Thévenin is what makes maximum power
transfer computable. If a theorem ever feels arbitrary, the reason is almost
always that the link above it was skipped.

## How to use this

Read a module, then close it and rework its examples on blank paper **without
looking at the circuit description twice**. Circuit theory is not conceptually
hard; it is bookkeeping-hard. The marks go to whoever keeps their signs and
labels straight under time pressure, and that is a trained skill, not an
understood one.

Every module ends with exercises that have answers. Module 15 has 20 full
problems with complete solutions.

## Notation used throughout

- Uppercase V, I for DC or RMS values; lowercase v, i for instantaneous.
- V_s, I_s for sources; V_th, R_th for Thévenin; I_N, R_N for Norton.
- Ω for ohms, S for siemens, ∥ for "in parallel with".
- R_1 ∥ R_2 means R_1R_2/(R_1 + R_2).
