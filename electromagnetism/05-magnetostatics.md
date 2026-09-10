# Module 05 — Magnetostatics

Steady currents, steady magnetic fields. The structure mirrors Module 03 almost
line for line — which is the fastest way to learn it.

| Electrostatics | Magnetostatics |
|---|---|
| Coulomb's law | Biot–Savart law |
| Gauss's law ∮D·dS = Q | Ampère's law ∮H·dl = I |
| **E** = −∇V | **B** = ∇×**A** |
| ∇·**D** = ρ_v | ∇·**B** = 0 |
| ∇×**E** = 0 | ∇×**H** = **J** |
| C = Q/V | L = λ/I |
| w = ½εE² | w = ½μH² |

## 5.1 Biot–Savart law

A current element I d**l** at **r**′ produces at **r**:

    dH = I dl × a_R / (4πR²)      [A/m]

with **R** = **r** − **r**′, R = |**R**|, **a**_R = **R**/R.

Equivalently d**H** = I d**l** × **R** / (4πR³).

The cross product is the whole story: the field **circles** the current. It is
never along the wire and never radially outward.

For surface and volume currents: I d**l** → **K** dS → **J** dv.

### Standard results — memorize

**Finite straight filament** along z, current I, field at perpendicular distance ρ,
with α₁, α₂ the angles subtended from the field point to the two ends
(measured from the wire, positive toward +z):

    H = I(sin α₂ − sin α₁) / (4πρ)   a_φ

**Symmetric finite conductor** — the same result in the form used when the wire
runs from z = −L to z = +L and the field point sits opposite its **midpoint**:

    H = [I/(2πρ)] · [L / √(L² + ρ²)]   a_φ

This is often the more convenient form, because the bracket is a clean
"finite-length correction factor" that tends to 1 as L/ρ grows. At L = 5ρ it is
already 0.981, so a wire five times longer than the standoff distance is within
2% of infinite. That is worth knowing: it tells you when the infinite-wire
formula is safe to use.

**Infinite straight wire** (α₁ = −90°, α₂ = +90°, or L → ∞ above):

    H = I / (2πρ)  a_φ        ⇒  B = μ₀I/(2πρ)

Direction by right-hand rule: thumb along I, fingers curl along **H**.

**Circular loop** radius a, N turns, on-axis at height h:

    H = N I a² / (2(a²+h²)^{3/2})  a_z ;  at centre H = NI/2a

**Circular arc** of radius a subtending angle α (in radians) at its centre:

    H_centre = I α / (4πa)

Every element of an arc is the same distance a from the centre and contributes
in the same direction, so no integration survives beyond the arc angle. Check it
against the full loop: α = 2π gives H = I/2a ✓. Watch for this one in exams —
problems are often built from straight segments (which contribute nothing at the
centre, since d**l** × **a**_R = 0 along a radial line) plus one arc.

**Infinite solenoid**, n turns per metre: H = nI inside, 0 outside.
**Finite solenoid** on axis: H = (nI/2)(cos θ₂ − cos θ₁).
**Toroid**, N turns, mean radius ρ: H = NI/(2πρ).
**Infinite sheet of current K a_x in z=0 plane**: **H** = ½ **K** × **a**_n
 (i.e. ½K a_y for z>0 and −½K a_y for z<0 — uniform, distance-independent,
 the magnetic twin of the charged sheet).

### Superposition

Magnetic fields superpose in linear media exactly as electric fields do:
**H**_total = **H**₁ + **H**₂ + … Compute each source's contribution as a
vector at the observation point, then add.

The classic check: two long parallel wires a distance d apart carrying **equal
currents in the same direction**. At the midpoint each produces the same
magnitude I/(πd), but the right-hand rule sends them in **opposite** directions,
so they cancel exactly — **H** = 0. Reverse one current and they add instead.
Getting this right is entirely a matter of applying the right-hand rule twice
and being honest about the resulting directions.

### Current density: getting the source right

Before any field calculation, the source itself has to be expressed correctly.
Current is the flux of current density through a surface:

    I = ∫_S J · dS

For uniform **J** normal to a cross-section of area A this collapses to I = JA.
When **J** varies across the section it does not, and the integral has to be done.

**Example — uniform.** A conductor of radius 2 mm carries 5 A uniformly.
A = π(2×10⁻³)² = 1.2566×10⁻⁵ m², so J = 5/1.2566×10⁻⁵ = **3.98×10⁵ A/m²**.

**Example — non-uniform.** A cylindrical conductor of radius a = 4 mm carries
J_z = J₀(1 − ρ²/a²) with J₀ = 8×10⁵ A/m² (current crowded toward the centre,
falling to zero at the surface). Find the total current.

In cylindrical coordinates d**S** = ρ dρ dφ **a**_z, so

    I = ∫₀^{2π} ∫₀^a J₀(1 − ρ²/a²) ρ dρ dφ
      = 2πJ₀ [ρ²/2 − ρ⁴/(4a²)]₀^a = 2πJ₀ (a²/2 − a²/4) = πJ₀a²/2

    I = (π/2)(8×10⁵)(4×10⁻³)² = 20.1 A

Note the answer is exactly half of J₀A — the average of the parabolic profile
over the disc is J₀/2. Sanity checks like that catch algebra slips.

## 5.2 Ampère's circuital law

    ∮_L H·dl = I_enc          (integral)
    ∇ × H = J                 (differential, via Stokes)

The magnetic counterpart of Gauss's law, and used the same way: pick an
**Amperian loop** on which H is constant and parallel to d**l**.

**Coax example.** Inner conductor radius a carrying I, outer shell b<ρ<c carrying
−I return.

- ρ < a: I_enc = I(ρ²/a²) ⇒ H = Iρ/(2πa²)
- a < ρ < b: H = I/(2πρ)
- b < ρ < c: I_enc = I[1 − (ρ²−b²)/(c²−b²)] ⇒ H falls to 0 at ρ=c
- ρ > c: I_enc = 0 ⇒ **H = 0** — the coax confines its own field entirely.
  This is why coaxial cable neither radiates nor picks up interference.

### Reading Ampère's law when there is no symmetry

Two things must stay separate in your head:

1. **The circulation ∮H·dl always equals I_enc.** This holds for any closed
   contour whatsoever, symmetric or not. Sign convention: pick a traversal
   direction, take the surface normal by the right-hand rule, and count currents
   through the surface as positive when they go along that normal.
2. **Extracting H from that circulation needs symmetry.** Only when |H| is
   constant and tangential along the path can you write ∮H·dl = H·(length) and
   divide.

Example: a contour traversed counter-clockwise seen from +z encloses 8 A out of
the page, 3 A into it, and 5 A out. Then I_enc = +8 − 3 + 5 = 10 A, so
∮**H**·d**l** = 10 A — regardless of where inside the contour those currents
sit. But you cannot conclude H = 10/(path length) unless the geometry is
symmetric. The circulation is fixed; its distribution around the path is not.

## 5.3 Magnetic flux density and flux

    B = μ₀H   (free space)     [T = Wb/m²]
    Ψ = ∫_S B·dS               [Wb]

For a **uniform** field crossing a flat area A whose normal makes angle θ with
**B**, this reduces to Ψ = BA cos θ. Note θ is measured from the **normal**, not
from the surface — the single most common slip in flux problems. A field lying
in the plane of the loop (θ = 90°) gives zero flux, not maximum.

**Gauss's law for magnetism:**

    ∮_S B·dS = 0      ⇔     ∇·B = 0

No magnetic monopoles. Every field line that leaves a region comes back. This
is the *only* one of Maxwell's four equations with a zero on the right, and the
only one never modified by anything later.

## 5.4 Magnetic potentials

**Scalar potential** V_m, valid only where **J** = 0:
    H = −∇V_m , with ∇²V_m = 0.
Caution: V_m is multivalued (walk around a wire and it increases by I each lap).

**Vector potential A** [Wb/m], valid everywhere because ∇·**B** = 0 always:

    B = ∇ × A
    A = ∫ μ₀ I dl / (4πR)     (line current)
      = ∫ μ₀ J dv / (4πR)     (volume current)

Flux can then be computed as a line integral instead of a surface one:
Ψ = ∫**B**·d**S** = ∮**A**·d**l** (Stokes). This is often far easier.

In the Coulomb gauge (∇·**A** = 0): ∇²**A** = −μ₀**J** — Poisson again, one
equation per component.

## 5.5 Magnetic forces

**On a moving charge (Lorentz force):**

    F = q(E + u × B)

Note **F** ⊥ **u**, so a magnetic field does **no work** — it changes direction
only, never speed. Cyclotron radius r = mu/(qB), angular frequency ω = qB/m.

**On a current element:**  d**F** = I d**l** × **B**;  **F** = I **L** × **B**
for a straight wire in a uniform field.

**Between two parallel wires**, separation d, currents I₁ and I₂:

    F/L = μ₀I₁I₂ / (2πd)

Attract if currents are parallel, repel if antiparallel. (This is the historical
definition of the ampere.)

**Torque on a loop:** **T** = **m** × **B**, with magnetic moment **m** = I S **a**_n.
This is the entire operating principle of motors and moving-coil meters.

## 5.6 Magnetic materials

Magnetization **M** [A/m] = magnetic dipole moment per unit volume.

    B = μ₀(H + M),   M = χ_m H,   B = μ₀(1+χ_m)H = μ₀μ_r H = μH

- **Diamagnetic** (χ_m slightly negative): bismuth, copper, water.
- **Paramagnetic** (χ_m slightly positive): aluminium, tungsten.
- **Ferromagnetic** (χ_m huge, nonlinear, hysteretic): iron, nickel, cobalt,
  ferrites. μ_r from hundreds to 10⁵. Loses magnetism above the **Curie
  temperature**.

**Hysteresis loop**: B vs H is not single-valued. Retentivity B_r (remaining B at
H=0) and coercivity H_c (H needed to force B to 0). Loop area = energy lost per
cycle per unit volume — the hysteresis loss in every transformer core.

## 5.7 Magnetic boundary conditions

    B_n1 = B_n2                     (normal B continuous)
    H_t1 − H_t2 = K                 (tangential H jumps by surface current)
    ⇒ H_t1 = H_t2 when K = 0, hence B_t1/μ₁ = B_t2/μ₂

Refraction: tan θ₁ / tan θ₂ = μ₁ / μ₂.

Practical consequence: at an air–iron boundary (μ₂ ≫ μ₁), lines in the iron run
almost parallel to the surface, and lines leaving iron into air emerge almost
perpendicular. That is why iron "guides" flux — the basis of magnetic circuits.

## 5.8 Inductance

Flux linkage λ = NΨ.

    L = λ / I         [H]

Method: assume I → find **H** (Ampère) → find **B** → find Ψ = ∫**B**·d**S** →
multiply by N → divide by I.

| Geometry | Inductance |
|---|---|
| Solenoid, N turns, length ℓ, area S | L = μN²S/ℓ |
| Toroid, N turns, mean radius ρ₀, area S | L = μN²S/(2πρ₀) |
| Coax, radii a<b, per unit length | L = (μ/2π) ln(b/a) |
| Two-wire line, per unit length | L = (μ/π) cosh⁻¹(d/2a) |

Mutual inductance M₁₂ = λ₁₂/I₂ = M₂₁; coupling coefficient k = M/√(L₁L₂), 0≤k≤1.

Energy: W_m = ½LI² = ½ ∫ **B**·**H** dv; density w_m = ½μH² = B²/2μ.

Note for coax: LC = με per unit length — a relation that reappears as the
fundamental transmission-line identity in Module 08.

## 5.9 Magnetic circuits

Direct analogy with DC circuits:

| Electric | Magnetic |
|---|---|
| EMF V | MMF ℱ = NI [A-turns] |
| Current I | Flux Ψ [Wb] |
| Resistance R = ℓ/σS | Reluctance ℛ = ℓ/μS [A-t/Wb] |
| V = IR | ℱ = Ψℛ |

Kirchhoff analogues: ΣNI = ΣℛΨ round a loop; ΣΨ = 0 at a node.

**Air gaps dominate.** A 1 mm gap in an iron core with μ_r = 5000 has the same
reluctance as 5 m of iron. Whenever a core has a gap, compute the gap first.

## 5.10 Worked examples

**Example 1.** A 5 A current flows in an infinite wire on the z-axis. Find **H**
at (3, 4, 0) and the force per metre on a parallel wire at (3,4,0) carrying 2 A
in the same direction.

ρ = 5 m. H = 5/(2π·5) = **0.159 A/m**, direction **a**_φ.
B = μ₀H = 4π×10⁻⁷ × 0.159 = 2×10⁻⁷ T.
F/L = μ₀I₁I₂/(2πd) = (4π×10⁻⁷)(5)(2)/(2π·5) = **4×10⁻⁷ N/m**, attractive.

**Example 2.** A toroid has N = 500, mean radius 10 cm, cross-section 4 cm²,
μ_r = 1000. Find L and the current for Ψ = 0.4 mWb.

L = μ₀μ_r N²S/(2πρ₀) = (4π×10⁻⁷)(1000)(250000)(4×10⁻⁴)/(2π×0.1)
  = (1.2566e−3)(250000)(4e−4)/0.6283 = 0.1257/0.6283 = **0.2 H**

ℛ = ℓ/μS = 0.6283/((1.2566e−3)(4e−4)) = 1.25×10⁶ A-t/Wb
NI = Ψℛ = 4×10⁻⁴ × 1.25×10⁶ = 500 A-t ⇒ **I = 1 A**

**Example 3.** Find the energy stored per metre in a coax with a = 1 mm,
b = 5 mm, carrying 10 A.

L/length = (μ₀/2π)ln(5) = 2×10⁻⁷ × 1.609 = 3.22×10⁻⁷ H/m
W = ½LI² = ½(3.22e−7)(100) = **16.1 μJ/m**
(Ignoring the internal inductance of the centre conductor, μ₀/8π = 5×10⁻⁸ H/m,
which would add 2.5 μJ/m.)

## 5.10a Where this shows up in practice

- **Busbars and power conductors** — predicting the field around high-current
  runs, and the forces between them under fault currents.
- **Cable routing** — magnetic exposure limits and conductor spacing.
- **Coils, relays, contactors, electromagnets** — concentrating flux to get force.
- **Electric machines** — torque is the current–field interaction of §5.5.
- **Current sensing** — Hall-effect and Rogowski devices infer current from the
  local field, using H = I/2πρ in reverse.
- **EMC and inductive coupling** — unwanted mutual inductance between circuits.
- **MRI and instrumentation** — precisely controlled, highly uniform fields.

## 5.11 Exercises

1. Use Ampère's law to find **H** inside and outside a solid cylindrical conductor
   of radius a carrying uniform current I.
2. A square loop of side 2 m carries 5 A in a field **B** = 0.5**a**_z T, the loop
   lying in the xy-plane. Find the torque. (Zero — **m** ∥ **B**. Now tilt it 30°
   and redo.)
3. Derive L per unit length for a coax from energy, W = ½∫μH² dv, and confirm it
   matches (μ/2π)ln(b/a).
4. An iron core (μ_r = 2000, mean length 40 cm, area 5 cm²) has a 2 mm air gap
   and 300 turns. Find the current for 0.8 mWb.
5. Two media, μ_r1 = 1 (z>0) and μ_r2 = 200 (z<0), no surface current.
   **B**₁ = 2**a**_x + 5**a**_z mT. Find **B**₂.

## Takeaways

- Biot–Savart is Coulomb's magnetic twin, with a cross product bolted on.
- Ampère's law is the symmetry shortcut; use it exactly like Gauss's law.
- ∇·**B** = 0 is permanent and absolute: no monopoles, closed loops always.
- Magnetic fields do no work; they steer, they never accelerate.
- L, like C, is pure geometry and material: assume I, find Ψ, divide.
