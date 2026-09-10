# PGDEE Electromagnetism — Start Here

**Course:** ELE 715, Electromagnetic Fields and Waves — Postgraduate Diploma in
Electrical/Electronic Engineering. Lecturer: Prof. D. S. Nyitamen.

This course is built to sit alongside the official lecture notes, not to replace
them. Where the notes state a result, this expands the derivation and adds
worked practice; where the notes move fast, this slows down. Module 13 contains
every tutorial and assignment problem from the notes, fully solved.

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

| Module | Title | ELE 715 coverage |
|---|---|---|
| 01 | Vector algebra & coordinate systems | Lecture 1, outcomes 1–3 |
| 02 | Vector calculus: grad, div, curl | Lecture 1, outcomes 4–5 |
| 03 | Electrostatics | Lecture 1, outcomes 6–9 (Gauss's law) |
| 04 | Materials, boundary conditions, Poisson/Laplace | extends the notes |
| 05 | Magnetostatics | Lectures 4–5 (Biot–Savart, Ampère) |
| 06 | Time-varying fields & Maxwell's equations | Week 6 onward; previewed in the notes |
| 07 | Uniform plane waves | the "and Waves" half of the title |
| 08 | Transmission lines | later in the syllabus |
| 09 | Waveguides & resonators | later in the syllabus |
| 10 | Radiation & antennas | later in the syllabus |
| 11 | Formula sheet | exam-day single page |
| 12 | Problem set with full solutions | 20 problems, all topics |
| 13 | **ELE 715 tutorials & assignment, solved** | **straight from the notes** |

**Where the lecture notes and this course meet.** The notes issued so far cover
two blocks: vector calculus through Gauss's law (Modules 01–03), and
magnetostatics through Ampère's law (Module 05). Everything from Module 06
onward — Faraday, displacement current, waves, lines, guides, antennas — is
signposted in the notes as coming later, so read those modules as running ahead
of the lectures rather than alongside them.

## How to use this

Start with Module 13 if an assessment is close — it is the lecturer's own
problems, and it tells you what he considers examinable. Otherwise work forward
from 01.

Read a module, then close it and try to re-derive the boxed results on blank
paper. If you cannot, you read it — you did not learn it. Do the module's
exercises before moving on; each module builds directly on the previous one.

Notation used throughout:
- Vectors in bold: **E**, **B**. Unit vectors: **a**_x, **a**_r, etc.
- Scalars italic-ish: V, ρ, ε.
- ε₀ = 8.854×10⁻¹² F/m, μ₀ = 4π×10⁻⁷ H/m, c = 1/√(μ₀ε₀) ≈ 3×10⁸ m/s.
- η₀ = √(μ₀/ε₀) ≈ 377 Ω (intrinsic impedance of free space).
