# Module 13 — ELE 715 Tutorials and Assignment, Fully Solved

Every problem here comes from Prof. D. S. Nyitamen's ELE 715 lecture notes —
the class exercises, the take-home assignment, and the worked examples. The
lecturer supplies answers to some; the rest are worked out in full below, and
all the numbers have been checked independently.

Do these before any other practice. They are the closest thing you have to a
statement of what the examiner considers important.

---

## Part A — Class exercises (vector calculus and Gauss's law)

**A1.** Given **A** = 4**a**_x − 2**a**_y + 4**a**_z, find its magnitude and unit vector.

|**A**| = √(16 + 4 + 16) = √36 = **6**
**a**_A = **A**/6 = **(2/3)a_x − (1/3)a_y + (2/3)a_z**

*Lecturer's answer: |A| = 6, a_A = (2/3)a_x − (1/3)a_y + (2/3)a_z ✓*

---

**A2.** Given V = 2x² + 4y² + z² volts, determine **E**.

∇V = 4x **a**_x + 8y **a**_y + 2z **a**_z
**E** = −∇V = **−4x a_x − 8y a_y − 2z a_z V/m**

*Lecturer's answer ✓*

---

**A3.** A point charge of 20 nC sits at the origin. Determine **D** at r = 0.4 m.

**D** does not involve ε at all — that is the whole point of defining it:

D = Q/(4πr²) = 20×10⁻⁹ / (4π × 0.16) = 20×10⁻⁹ / 2.0106
  = **9.95 nC/m², radially outward (a_r)**

(For comparison, **E** = D/ε₀ = 9.947×10⁻⁹/8.854×10⁻¹² = 1123 V/m.)

---

**A4.** An infinite line has ρ_L = 40 nC/m. Determine **E** at ρ = 0.15 m in free space.

E = ρ_L/(2πε₀ρ) = 40×10⁻⁹ / (2π × 8.854×10⁻¹² × 0.15)
  = 40×10⁻⁹ / 8.345×10⁻⁹ = **4.79 kV/m, radially (a_ρ)**

---

**A5.** Given **D** = 3x²**a**_x + 4y**a**_y + 2z**a**_z, determine ρ_v.

ρ_v = ∇·**D** = ∂(3x²)/∂x + ∂(4y)/∂y + ∂(2z)/∂z = 6x + 4 + 2 = **6x + 6 C/m³**

*Lecturer's answer ✓*

---

**A6.** A closed Gaussian surface contains +10 nC, −4 nC and +7 nC. Determine
the total outward flux.

Ψ = Q_enc = 10 − 4 + 7 = **13 nC**

*Lecturer's answer ✓*

---

**A7.** Explain why Gauss's law can be valid even when it is not convenient for
calculating **E**.

Gauss's law states a fact about a *total*: the net flux of **D** out of any
closed surface equals the charge enclosed. That statement is unconditional — it
holds for every closed surface around every charge distribution, symmetric or
not, and it follows directly from the inverse-square nature of the field.

What symmetry buys you is something different: the ability to *solve for* **D**.
The step from ∮**D**·d**S** = Q_enc to D = Q_enc/(area) requires pulling |**D**|
out of the integral, and that is legitimate only when |**D**| is constant over
the surface and **D** is everywhere parallel to d**S**. For three point charges
scattered asymmetrically, no surface has that property. The law still holds —
you can still state the total flux exactly — but the integral will not surrender
the field at any individual point.

**In one sentence:** Gauss's law always tells you the total; only symmetry lets
you convert the total into a local value.

---

## Part B — Take-home assignment

**B1.** For **D** = (x²y)**a**_x + (3xy²)**a**_y + (4z)**a**_z, determine the
volume charge density.

ρ_v = ∇·**D** = ∂(x²y)/∂x + ∂(3xy²)/∂y + ∂(4z)/∂z
    = 2xy + 6xy + 4 = 8xy + 4 C/m³

Sanity check the units: **D** in C/m², differentiated with respect to metres,
gives C/m³ ✓.

---

**B2.** A non-conducting solid sphere of radius 0.2 m carries a uniform volume
charge density 5 μC/m³. Determine **E** at r = 0.1 m and r = 0.4 m.

*Inside* (r = 0.1 m < a): enclosed charge grows as r³ while area grows as r², so
E rises **linearly** from the centre:

E = ρ_v r / (3ε₀) = (5×10⁻⁶)(0.1) / (3 × 8.854×10⁻¹²)
  = 5×10⁻⁷ / 2.656×10⁻¹¹ = **18.8 kV/m**

*Outside* (r = 0.4 m > a): all the charge is enclosed, and the sphere looks like
a point charge at its centre:

E = ρ_v a³ / (3ε₀ r²) = (5×10⁻⁶)(0.008) / (3 × 8.854×10⁻¹² × 0.16)
  = 4×10⁻⁸ / 4.250×10⁻¹² = **9.41 kV/m**

Worth noticing: the field is *larger* at r = 0.1 m (inside) than at r = 0.4 m
(outside). The maximum sits exactly at the surface, r = a = 0.2 m, where both
expressions agree at 37.65 kV/m. Sketch E against r for this sphere — rising
straight line, then 1/r² decay, peaking at the surface. That shape is worth
carrying in your head.

---

**B3.** Two large parallel plates carry equal and opposite surface charge
densities of 12 nC/m². Determine the field between and outside, in free space.

Between: the two sheets' fields add.

E = ρ_S/ε₀ = 12×10⁻⁹ / 8.854×10⁻¹² = **1.36 kV/m**, directed from + plate to −

Outside: the two fields are equal and opposite ⇒ **E = 0**

(Each sheet alone contributes ρ_S/2ε₀ = 678 V/m; between the plates these add to
1356 V/m, outside they cancel.)

---

**B4.** Explain physically why an external charge can alter the electric field at
points on a Gaussian surface but cannot alter the net flux.

Think in terms of field lines. Lines begin on positive charge and end on
negative charge; they are only created or destroyed *at* charges.

An external charge's lines have to get into the enclosed region and back out
again, because the charge that would terminate them is not inside. Every line
that pierces the surface inward must pierce it outward somewhere else. Inward
and outward crossings are counted with opposite sign in ∮**D**·d**S**, so they
cancel in pairs and the external charge contributes exactly zero to the total.

Locally, though, nothing cancels. At the point on the surface nearest the
external charge, **D** is strongly enhanced; on the far side it is altered
differently. The field at any individual point on the surface depends on
*everything*, inside and out. Only the integrated total is blind to what lies
outside.

This is why Gauss's law is powerful *and* limited in the same breath: the total
is beautifully simple, and the total is all it gives you.

---

## Part C — Lecturer's worked examples, verified

These appear in the notes with solutions. Recomputed independently; every stated
answer is correct. Use them as a self-test — cover the answer column first.

| # | Problem | Answer |
|---|---|---|
| A1 | H = 250**a**_y A/m, μ_r = 80. Find B. | B = μ₀μ_r H = **25.1 mT a_y** |
| A2 | Conductor r = 2 mm, I = 5 A uniform. Find J. | **3.98×10⁵ A/m²** |
| A3 | a = 4 mm, J_z = J₀(1−ρ²/a²), J₀ = 8×10⁵. Find I. | I = πJ₀a²/2 = **20.1 A** |
| A4 | Proton, v = 2×10⁶**a**_x, B = 0.30**a**_y. Find F. | **9.61×10⁻¹⁴ a_z N** |
| A5 | 0.30 m conductor, 10 A ⊥ 0.50 T. Find F. | F = ILB = **1.50 N** |
| A6 | I = 8 A, wire from z = ±0.50 m, ρ = 0.20 m. Find H. | **5.91 A/m a_φ** |
| A7 | Long wire, 10 A, ρ = 5 cm. Find H and B. | **31.8 A/m**, **40.0 μT** |
| A8 | 20-turn coil, a = 0.10 m, 2.5 A. Find B at centre. | H = NI/2a = 250 A/m, **B = 0.314 mT** |
| A9 | Loop a = 0.08 m, 5 A, at z = 0.06 m on axis. Find H. | **16.0 A/m** |
| A10 | Quarter arc, a = 0.10 m, 4 A. Find H at centre. | H = Iα/4πa = **5.00 A/m** |
| A11 | Two wires 0.20 m apart, 10 A same direction. H at midpoint? | Each 15.9 A/m, opposed ⇒ **0** |
| A12 | B = 0.20 T, A = 0.010 m², 60° to normal. Find Φ. | Φ = BA cos θ = **1.00 mWb** |
| A13 | H = 10**a**_φ A/m on a circle ρ = 0.20 m. Find ∮H·dl. | **12.57 A** = I_enc |
| A14 | Contour encloses +8, −3, +5 A. Find ∮H·dl. | **10 A** |
| B1 | **A**·**B** for (2,3,−1) and (4,−1,2) | **3** |
| B2 | \|**A**\| and **a**_A for (3,−4,12) | 13; **(3,−4,12)/13** |
| B3 | V = 3x² + 2yz. Find **E**. | **−6x a_x − 2z a_y − 2y a_z V/m** |
| B4 | **D** = 3x**a**_x + 2y**a**_y + 5z**a**_z. Find ∇·**D**. | **10 C/m³** |
| B5 | **D** = 6**a**_z C/m², A = 4 m², normal +**a**_z | Ψ = **24 C** |
| B6 | D = 10 C/m², A = 2 m², 60° to normal | Ψ = **10 C** |
| B7 | Q = 5 nC, find E at r = 0.25 m | **720 V/m** |
| B8 | Q = 18 nC at centre of a cube, flux per face | **3 nC** |
| B9 | λ = 15 nC/m, ρ = 0.1 m | **2.70 kV/m** |
| B10 | ρ_S = 8 nC/m² isolated sheet | **452 V/m** |
| B11 | Parallel plates, ρ_S = 10 nC/m² | **1.13 kV/m** |
| B12 | **D** = 2x²**a**_x + 3y**a**_y + 4z**a**_z. Find ρ_v. | **4x + 7 C/m³** |
| B13 | **D** = x**a**_x + y**a**_y + z**a**_z over unit cube | ∇·**D** = 3 ⇒ Ψ = **3 C** |
| B14 | Enclosed +8, −3, +10 nC; +20 nC outside | Q_enc = **15 nC** |

---

## Notation: lecturer's symbols vs this course

Same physics, occasionally different letters. Read fluently in both.

| Quantity | Lecture notes | This course | Note |
|---|---|---|---|
| Magnetic flux | Φ_B | Ψ | Both in webers |
| Line charge density | λ or ρ_L | ρ_L | Notes use both |
| Field at arc centre | H_center | H_centre | — |
| Azimuthal component | H_phi, a_phi | H_φ, **a**_φ | — |
| Finite wire | [I/2πρ][L/√(L²+ρ²)] | I(sin α₂ − sin α₁)/4πρ | Same result; the notes' form assumes the midpoint |
| Permittivity | ε (medium), ε₀ (free space) | same | — |

## The lecturer's reading list

- **M. N. O. Sadiku**, *Elements of Electromagnetics*, Oxford — closest in style
  and notation to these notes; the natural first reference.
- **W. H. Hayt & J. A. Buck**, *Engineering Electromagnetics*, McGraw-Hill —
  strongest on worked examples and drill problems.
- **D. K. Cheng**, *Field and Wave Electromagnetics*, Addison-Wesley — cleaner
  on the wave and transmission-line half.
- **F. T. Ulaby & U. Ravaioli**, *Fundamentals of Applied Electromagnetics*,
  Pearson — the most application-oriented.

If you buy one, buy Sadiku: the symbols will match your lecture notes exactly,
which matters more than you'd expect under exam pressure.
