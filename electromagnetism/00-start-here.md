# PGDEE Electromagnetism — Start Here

This is a from-scratch course. No prior field theory assumed. You need:

- Algebra, trigonometry
- Basic calculus (derivatives, integrals). Vector calculus is **taught here**, not assumed.
- Circuit basics (V = IR, capacitors, inductors) — helpful, not required.

## The one idea behind the whole subject

Circuit theory says: charge moves through wires, and voltage/current tell you
everything. That is a *lie that works* — it works only when the circuit is much
smaller than the wavelength of the signals in it.

Field theory says: charge creates a condition in the space around it. Another
charge placed there feels a force. That condition is a **field**. Electromagnetism
is the study of two coupled fields — electric (**E**) and magnetic (**H**) — and
the four equations that bind them (Maxwell's equations).

Everything in this course is either:
1. Building the mathematical language (vectors, coordinates, div/curl/grad), or
2. Building the four equations one piece at a time, or
3. Solving the four equations in useful situations (waves, lines, guides, antennas).

## Course map

| Module | Title | What you gain |
|---|---|---|
| 01 | Vector algebra & coordinate systems | The language |
| 02 | Vector calculus: grad, div, curl | The verbs of the language |
| 03 | Electrostatics | Coulomb → Gauss → potential → capacitance |
| 04 | Materials, boundary conditions, Poisson/Laplace | Fields in real matter |
| 05 | Magnetostatics | Biot–Savart → Ampère → inductance |
| 06 | Time-varying fields & Maxwell's equations | The unification |
| 07 | Uniform plane waves | Propagation, loss, skin effect, polarization |
| 08 | Transmission lines | Where EM meets circuits again; Smith chart |
| 09 | Waveguides & resonators | Guided modes, cutoff |
| 10 | Radiation & antennas | How energy leaves the circuit entirely |
| 11 | Formula sheet | Exam-day single page |
| 12 | Problem set with full solutions | Proof you understood |

## How to use this

Read a module, then close it and try to re-derive the boxed results on blank
paper. If you cannot, you read it — you did not learn it. Do the module's
exercises before moving on; each module builds directly on the previous one.

Notation used throughout:
- Vectors in bold: **E**, **B**. Unit vectors: **a**_x, **a**_r, etc.
- Scalars italic-ish: V, ρ, ε.
- ε₀ = 8.854×10⁻¹² F/m, μ₀ = 4π×10⁻⁷ H/m, c = 1/√(μ₀ε₀) ≈ 3×10⁸ m/s.
- η₀ = √(μ₀/ε₀) ≈ 377 Ω (intrinsic impedance of free space).
