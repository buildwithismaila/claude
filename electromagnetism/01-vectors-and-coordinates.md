# Module 01 — Vector Algebra and Coordinate Systems

## 1.1 Why vectors

A field assigns a value to every point in space. A **scalar field** assigns a
number (temperature T(x,y,z), potential V(x,y,z)). A **vector field** assigns a
number *and a direction* (electric field **E**(x,y,z), velocity of water in a pipe).

Electromagnetism is almost entirely vector fields, so the algebra must be fluent.

## 1.2 Vector basics

A vector **A** = A_x **a**_x + A_y **a**_y + A_z **a**_z.

- Magnitude: |**A**| = √(A_x² + A_y² + A_z²)
- Unit vector: **a**_A = **A**/|**A**|  (length 1, direction of **A**)
- Addition is componentwise.

**Position vector** of point P(x,y,z): **r** = x**a**_x + y**a**_y + z**a**_z.

**Distance vector** from P₁ to P₂: **R**₁₂ = **r**₂ − **r**₁. This single object
appears in every Coulomb-law and Biot–Savart problem you will ever do.

## 1.3 Dot product — "how much of A lies along B"

**A**·**B** = A_x B_x + A_y B_y + A_z B_z = |A||B| cos θ

Properties and uses:
- Result is a **scalar**.
- **A**·**B** = 0 ⟺ perpendicular. This is how you test orthogonality.
- Projection of **A** onto direction **a**_B is (**A**·**a**_B).
- Work = **F**·**d**. Flux through a surface = **D**·**S**. Both are dot products
  because both ask "how much is aligned?"

## 1.4 Cross product — "the perpendicular one"

**A** × **B** = |A||B| sin θ **a**_n , with **a**_n by the right-hand rule.

Determinant form:

```
          | a_x  a_y  a_z |
A × B  =  | A_x  A_y  A_z |
          | B_x  B_y  B_z |
```

= (A_y B_z − A_z B_y)**a**_x − (A_x B_z − A_z B_x)**a**_y + (A_x B_y − A_y B_x)**a**_z

Uses:
- Result is a **vector** perpendicular to both.
- **A** × **B** = 0 ⟺ parallel.
- Magnetic force: **F** = q**v** × **B**. Poynting vector: **S** = **E** × **H**.
  The "sideways" nature of magnetism is entirely a cross product.
- Note **A**×**B** = −**B**×**A**. Order matters; sign errors here are the #1
  source of wrong answers in magnetostatics.

### Triple products
- Scalar triple: **A**·(**B**×**C**) = volume of parallelepiped; cyclic-invariant.
- Vector triple: **A**×(**B**×**C**) = **B**(**A**·**C**) − **C**(**A**·**B**)
  ("BAC−CAB"). Needed in wave and antenna derivations.

## 1.5 Coordinate systems — choose one that matches the symmetry

The physics never changes; the algebra does. Pick the system whose surfaces match
your object and half the work vanishes.

### Cartesian (x, y, z)
- Differential length: d**l** = dx **a**_x + dy **a**_y + dz **a**_z
- Differential area: dS_z = dx dy **a**_z (and cyclic)
- Differential volume: dv = dx dy dz
- Use for: slabs, boxes, plane waves, rectangular waveguides.

### Cylindrical (ρ, φ, z)
ρ = distance from z-axis, φ = angle from x-axis, z = height.

- x = ρ cos φ, y = ρ sin φ, z = z; ρ = √(x²+y²), φ = tan⁻¹(y/x)
- d**l** = dρ **a**_ρ + ρ dφ **a**_φ + dz **a**_z   ← note the ρ in the φ term
- dS_ρ = ρ dφ dz **a**_ρ ;  dS_φ = dρ dz **a**_φ ;  dS_z = ρ dρ dφ **a**_z
- dv = ρ dρ dφ dz
- Use for: wires, coaxial cables, solenoids, circular waveguides.

### Spherical (r, θ, φ)
r = distance from origin, θ = polar angle from +z (0 to π), φ = azimuth (0 to 2π).

- x = r sinθ cosφ, y = r sinθ sinφ, z = r cosθ
- d**l** = dr **a**_r + r dθ **a**_θ + r sinθ dφ **a**_φ
- dS_r = r² sinθ dθ dφ **a**_r
- dv = r² sinθ dr dθ dφ
- Use for: point charges, spheres, antenna radiation patterns.

> **Critical warning.** In cylindrical and spherical systems the unit vectors
> **change direction from point to point**. **a**_ρ at φ=0 is not **a**_ρ at
> φ=90°. Therefore you may **never** add vectors at different points by adding
> their components, and you may **never** pull **a**_r outside an integral over φ.
> Cartesian unit vectors are the only constant ones. When in doubt, convert to
> Cartesian, integrate, convert back.

### Conversion of vector components
To convert **A** from Cartesian to cylindrical, dot with the new unit vectors:

A_ρ = **A**·**a**_ρ = A_x cosφ + A_y sinφ
A_φ = **A**·**a**_φ = −A_x sinφ + A_y cosφ
A_z = A_z

Spherical similarly, using the standard 3×3 transformation matrix.

## 1.6 Worked examples

**Example 1.** Given **A** = 3**a**_x − 2**a**_y + **a**_z and
**B** = **a**_x + 4**a**_y − 2**a**_z, find (a) **A**·**B**, (b) the angle
between them, (c) **A**×**B**.

(a) 3(1) + (−2)(4) + (1)(−2) = 3 − 8 − 2 = **−7**
(b) |A| = √14 = 3.742, |B| = √21 = 4.583.
  cos θ = −7/(3.742×4.583) = −0.408 → θ = **114.1°**
(c) **A**×**B** = ((−2)(−2) − (1)(4))**a**_x − ((3)(−2) − (1)(1))**a**_y + ((3)(4) − (−2)(1))**a**_z
  = (4−4)**a**_x − (−6−1)**a**_y + (12+2)**a**_z = **7a_y + 14a_z**

Check: dot the result with **A**: 0(3) + 7(−2) + 14(1) = 0 ✓ (perpendicular, as required).

**Example 2.** Point P has Cartesian coordinates (3, 4, 5). Give it in
cylindrical and spherical.

Cylindrical: ρ = √(9+16) = 5, φ = tan⁻¹(4/3) = 53.13°, z = 5 → **(5, 53.13°, 5)**
Spherical: r = √(9+16+25) = √50 = 7.071, θ = cos⁻¹(5/7.071) = 45°, φ = 53.13°
→ **(7.071, 45°, 53.13°)**

**Example 3.** Find the unit vector from P(1,2,3) toward Q(4,6,3).

**R** = (4−1, 6−2, 3−3) = (3, 4, 0); |**R**| = 5;
**a** = **0.6a_x + 0.8a_y**

## 1.7 Exercises

1. **A** = 2**a**_x + **a**_y − 3**a**_z, **B** = **a**_x − **a**_y + **a**_z.
   Find **A**·**B**, **A**×**B**, and the component of **A** along **B**.
2. Convert **A** = y**a**_x − x**a**_y + z**a**_z into cylindrical coordinates.
   (Answer: −ρ**a**_φ + z**a**_z — a purely circulating field. Remember this one;
   it is the shape of the magnetic field around a wire.)
3. Show that **A**×(**B**×**C**) ≠ (**A**×**B**)×**C** in general by picking
   **A**=**a**_x, **B**=**a**_x, **C**=**a**_y.
4. Find the volume of the region 1 ≤ r ≤ 2, 0 ≤ θ ≤ π/2, 0 ≤ φ ≤ π/2 in
   spherical coordinates by integrating dv. (Answer: 7π/6)

## Takeaways

- Dot product = alignment (scalars, flux, work). Cross product = perpendicularity
  (forces, power flow, rotation).
- Symmetry chooses the coordinate system; the right choice makes hard integrals easy.
- Non-Cartesian unit vectors are position-dependent. Most beginner errors live here.
