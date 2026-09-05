# Module 04 — Materials, Boundary Conditions, Poisson & Laplace

## 4.1 Conductors, dielectrics, and current

**Conductors** have free electrons. **Dielectrics (insulators)** have bound
charges that can only shift slightly.

### Convection and conduction current

Current density **J** [A/m²]; total current I = ∫_S **J**·d**S**.

- Convection: **J** = ρ_v **u** (charge physically transported, e.g. electron beam)
- Conduction: **J** = σ**E**  ← **point form of Ohm's law**

σ = conductivity [S/m]. Copper 5.8×10⁷, seawater ~4, glass ~10⁻¹².

Deriving circuit Ohm's law from the point form, for a wire length L, area S:
V = EL, I = JS = σES ⇒ R = V/I = L/(σS). Familiar, but now it is a *consequence*.

### Continuity equation (charge conservation)

    ∇·J = −∂ρ_v/∂t

"Current flowing out of a point = rate at which charge there decreases." Combined
with ∇·**D** = ρ_v and **J** = σ**E**, this gives charge relaxation:

    ρ_v(t) = ρ_v0 e^{−t/T_r},   T_r = ε/σ

For copper T_r ≈ 1.5×10⁻¹⁹ s — charge placed inside a conductor rushes to the
surface essentially instantly. Hence:

### Properties of a perfect conductor in statics
1. **E** = 0 inside.
2. ρ_v = 0 inside; all charge sits on the surface.
3. The surface is an **equipotential**.
4. **E** just outside is **normal** to the surface, magnitude ρ_S/ε.

(Any tangential E would push surface charge sideways — it cannot survive in
equilibrium. That is the whole proof.)

## 4.2 Polarization in dielectrics

An applied field stretches each molecule into a tiny dipole. Sum per unit volume
= **polarization P** [C/m²].

    D = ε₀E + P
    P = ε₀χ_e E        (linear, isotropic media)
    D = ε₀(1 + χ_e)E = ε₀ε_r E = εE

- χ_e = electric susceptibility; ε_r = 1 + χ_e = relative permittivity.
- Bound charge densities: ρ_pv = −∇·**P**, ρ_ps = **P**·**a**_n.

Physical consequence: inside a dielectric the field is *reduced* by the factor
ε_r, because the induced dipoles partially cancel the applied field. This is
exactly why inserting a dielectric raises capacitance by ε_r.

**Dielectric strength**: the E-field at which the material breaks down and
conducts. Air ≈ 3 MV/m, mica ≈ 200 MV/m. Design constraint in every HV problem.

## 4.3 Boundary conditions — the most exam-heavy topic

Derived by applying ∮**E**·d**l** = 0 to a thin rectangular loop straddling the
boundary, and ∮**D**·d**S** = Q_enc to a thin pillbox straddling it.

### Dielectric–dielectric

**Tangential E is continuous:**

    E_t1 = E_t2      ⇒  D_t1/ε₁ = D_t2/ε₂

**Normal D jumps by the free surface charge:**

    D_n1 − D_n2 = ρ_S     (and D_n1 = D_n2 if no free surface charge)
    ⇒ ε₁E_n1 = ε₂E_n2

### Law of refraction of field lines
With no free surface charge, if θ₁, θ₂ are measured from the normal:

    tan θ₁ / tan θ₂ = ε₁ / ε₂

Field lines bend away from the normal on entering the denser (higher ε) medium.

### Conductor–dielectric

    E_t = 0,     D_n = ρ_S

Field meets a conductor at 90°, always.

### Conductor–free space (same thing with ε₀)

    D_t = ε₀E_t = 0,    D_n = ε₀E_n = ρ_S

### Magnetic analogues (preview of Module 05)

    B_n1 = B_n2                  (normal B continuous)
    H_t1 − H_t2 = K              (tangential H jumps by surface current K)

**Memory aid:** *E is tangentially continuous; D is normally continuous (up to
ρ_S). B is normally continuous; H is tangentially continuous (up to K).*
Electric and magnetic are swapped — that duality repays memorizing.

## 4.4 Poisson's and Laplace's equations

Start from ∇·**D** = ρ_v, **D** = ε**E**, **E** = −∇V:

    ∇²V = −ρ_v/ε        Poisson
    ∇²V = 0             Laplace (charge-free region)

### Why this matters
Coulomb-style integration needs you to know where all the charge is. In real
problems you know the *boundary conditions* instead (this plate is at 100 V, that
one is grounded). Laplace's equation plus boundary conditions is the practical
route.

### Uniqueness theorem
A solution of Laplace's equation that satisfies the boundary conditions is **the**
solution. Consequence: **guess-and-verify is a legitimate method.** If your
guess fits the equation and the boundaries, you are done — no need to justify how
you found it.

### General solution procedure
1. Choose the coordinate system matching the symmetry.
2. Write ∇²V = 0 and drop all terms that symmetry kills.
3. Integrate (usually twice), producing two constants.
4. Apply the two boundary conditions to fix the constants.
5. **E** = −∇V; ρ_S = D_n at conductor surfaces; Q = ∫ρ_S dS; C = Q/V.

### Worked example — parallel plates
Plates at z = 0 (V=0) and z = d (V=V₀); field varies only with z.

∇²V = d²V/dz² = 0 ⇒ V = Az + B.
BCs: B = 0, A = V₀/d ⇒ **V = V₀ z/d**
**E** = −∇V = −(V₀/d)**a**_z ; D_n = εV₀/d = ρ_S
Q = ρ_S S = εSV₀/d ⇒ **C = εS/d** ✓

### Worked example — coaxial cable
Field varies only with ρ:

(1/ρ) d/dρ (ρ dV/dρ) = 0 ⇒ ρ dV/dρ = A ⇒ V = A ln ρ + B
BCs V(a)=V₀, V(b)=0 ⇒ **V = V₀ ln(b/ρ)/ln(b/a)**
**E** = −dV/dρ **a**_ρ = V₀/(ρ ln(b/a)) **a**_ρ
C = 2πεL/ln(b/a) ✓ — same as Module 03, obtained without Gauss.

### Worked example — spherical
(1/r²) d/dr(r² dV/dr)=0 ⇒ V = −A/r + B; with V(a)=V₀, V(b)=0:
V = V₀ (1/r − 1/b)/(1/a − 1/b), giving C = 4πε/(1/a − 1/b). ✓

## 4.5 Method of images

A point charge Q at height h above an infinite grounded plane. The plane forces
V = 0 on it. Replace the plane by an image charge −Q at depth h; the pair
naturally produces V = 0 on the midplane, so by uniqueness the field above the
plane is correct.

Results:
- V(x,y,z) = (Q/4πε₀)[1/√(x²+y²+(z−h)²) − 1/√(x²+y²+(z+h)²)]
- Force of attraction on Q: F = Q²/(4πε₀(2h)²) = Q²/(16πε₀h²)
- Induced surface charge: ρ_S = −Qh / (2π(x²+y²+h²)^{3/2}); ∫ρ_S dS = −Q exactly.

Line charge above a plane works the same way with an image −ρ_L.
Two perpendicular planes need **three** images (−, −, +) to zero both.

## 4.6 Exercises

1. Region 1 (z>0, ε_r=4) has **E**₁ = 5**a**_x − 2**a**_y + 3**a**_z V/m.
   Region 2 (z<0) has ε_r = 2, no free surface charge. Find **E**₂.
   (Tangential unchanged: 5, −2. Normal: ε₁E_z1 = ε₂E_z2 ⇒ E_z2 = 6.
   **E**₂ = 5**a**_x − 2**a**_y + 6**a**_z V/m.)
2. Show that V = ρ² sin φ does *not* satisfy Laplace's equation, but
   V = ρ sin φ does.
3. A 10 nC charge sits 2 cm above a grounded plane. Find the force on it and the
   maximum induced surface charge density.
4. Solve Laplace's equation for two coaxial cones (V depends on θ only) and find
   the capacitance-like relation.
5. Copper (σ=5.8e7, ε_r=1): compute the relaxation time and comment.

## Takeaways

- **J** = σ**E** is Ohm's law's true form; R = L/σS is a corollary.
- Conductor interiors are field-free; all the action is on the surface.
- Boundary conditions: E_t and D_n for electric, B_n and H_t for magnetic.
- Laplace + boundary conditions + uniqueness is the practical solver, and
  the method of images is uniqueness used cleverly.
