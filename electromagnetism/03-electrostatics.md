# Module 03 — Electrostatics

Static charges, static fields. Everything here follows from one experimental law
plus the calculus of Module 02.

## 3.1 Coulomb's law

Force on charge Q₂ due to Q₁, separated by **R**₁₂:

    F₁₂ = (Q₁Q₂ / 4πε₀ R²) a_R12      [N]

- ε₀ = 8.854×10⁻¹² F/m; 1/(4πε₀) ≈ 9×10⁹ m/F.
- Like charges repel, unlike attract (sign comes out of the product Q₁Q₂).
- Forces **superpose**: total force = vector sum of pairwise forces. This linearity
  is what makes the whole subject tractable.

## 3.2 Electric field intensity E

Define **E** as force per unit *test* charge:

    E = F/Q_test      [V/m or N/C]

For a point charge Q at the origin:

    E = (Q / 4πε₀ r²) a_r

For charge at **r**′ observed at **r**:

    E(r) = Q(r − r′) / (4πε₀ |r − r′|³)

### Continuous distributions
Replace Q by a differential element and integrate:

- Line charge ρ_L [C/m]:   **E** = ∫ ρ_L dl (**r**−**r**′)/(4πε₀|**r**−**r**′|³)
- Surface charge ρ_S [C/m²]: same with ρ_S dS
- Volume charge ρ_v [C/m³]: same with ρ_v dv

### Three standard results — memorize these

**Infinite line charge** ρ_L along the z-axis:

    E = ρ_L / (2πε₀ρ)  a_ρ            (falls as 1/ρ)

**Infinite sheet of charge** ρ_S in the z=0 plane:

    E = ρ_S / (2ε₀)  a_n              (does NOT fall off with distance)

**Two parallel sheets** +ρ_S and −ρ_S: field is ρ_S/ε₀ between them, zero
outside. This is the parallel-plate capacitor.

> **A distinction worth pinning down now.** An isolated charged sheet gives
> E = ρ_S/(2ε) on *each* side — the charge radiates both ways. But just outside
> a **conductor** carrying surface charge ρ_S the field is E = ρ_S/ε, twice as
> large. There is no contradiction: inside the conductor the field is zero, so
> all of the flux is forced out on one side instead of splitting between two.
> Examiners like this pair precisely because the factor of 2 looks like an error.

**Ring of charge** radius a, on its axis at height h:

    E = ρ_L a h / (2ε₀ (a²+h²)^{3/2})  a_z

## 3.3 Electric flux density D

    D = ε₀E   (in free space)      [C/m²]

**D** is deliberately defined without ε so that it depends only on the *free
charge*, not on the material. This makes Gauss's law material-independent.

Flux: Ψ = ∫_S **D**·d**S**  [C]

## 3.4 Gauss's law — the workhorse

    ∮_S D·dS = Q_enc          (integral form)
    ∇·D = ρ_v                 (differential form, via divergence theorem)

**Total electric flux out of any closed surface equals the free charge enclosed.**

### How to actually use it
Gauss's law is always true but only *useful* when symmetry lets you pull D out of
the integral. Procedure:

1. Identify the symmetry (spherical, cylindrical, planar).
2. Choose a **Gaussian surface** on which |**D**| is constant and **D** is either
   parallel or perpendicular to d**S** everywhere.
3. Then ∮**D**·d**S** = D × (area), and D = Q_enc/area.

**Example — coaxial cable.** Inner conductor radius a carrying ρ_L, outer shield
radius b. Gaussian surface: cylinder radius ρ, length L.

    D(2πρL) = ρ_L L  ⇒  D = ρ_L/(2πρ),  E = ρ_L/(2πε ρ)   for a < ρ < b

Inside the conductor (ρ<a) and outside the shield (ρ>b), Q_enc = 0 ⇒ E = 0.

**Example — uniformly charged sphere**, radius a, volume density ρ_v.

- r > a: D(4πr²) = ρ_v(4/3)πa³ ⇒ D = ρ_v a³/(3r²)  (looks like a point charge)
- r < a: D(4πr²) = ρ_v(4/3)πr³ ⇒ D = ρ_v r/3       (grows linearly from centre)

### Flux depends on enclosure, not on position

Two consequences of Q_enc that are conceptually important and heavily examined:

**Position inside doesn't matter.** Put Q = 18 nC anywhere inside a cube and the
total flux through the cube is 18 nC. If it sits at the *centre*, symmetry
divides it equally among the six faces: Ψ_face = 18/6 = **3 nC**. Move the
charge off-centre and the total is unchanged while the per-face split is not.

**External charges contribute nothing to net flux.** A charge outside the
surface changes **D** at individual points on it — its field lines enter one
side and leave the other — but they enter and leave in equal measure, so the net
flux is zero. If a closed surface encloses +8, −3 and +10 nC while +20 nC sits
outside, then Q_enc = **15 nC** and Ψ = 15 nC. The external charge is real and
affects the local field; it just cancels itself in the total.

### When Gauss's law actually helps

Gauss's law is *always true*. Whether it is *useful* depends entirely on whether
symmetry lets you pull D outside the integral.

| Situation | Gauss's law |
|---|---|
| Point charge or spherical distribution | Excellent |
| Infinite line or cylindrical symmetry | Excellent |
| Infinite sheet or planar symmetry | Excellent |
| Several asymmetric point charges | True, but useless for finding **E** |
| Irregular finite distribution | True, but useless for finding **E** |

Set against Coulomb-style integration:

| Problem | Coulomb / superposition | Gauss |
|---|---|---|
| Point charge | Convenient | Convenient |
| Several discrete charges | Convenient (vector sum) | Rarely helps |
| Spherical symmetry | Workable | Excellent |
| Infinite line charge | Needs integration | Immediate |
| Infinite sheet charge | Needs integration | Immediate |
| Physical flux insight | Limited | Strong |

Rule of thumb: **if you can name the Gaussian surface on which |D| is constant,
use Gauss. If you cannot, integrate.**

## 3.5 Electric potential V

Work done moving charge Q from A to B against the field:

    W = −Q ∫_A^B E·dl

Potential difference:

    V_AB = V_A − V_B = −∫_A^B E·dl        [V]

Absolute potential (reference at infinity) of a point charge:

    V = Q / (4πε₀ r)

Superposition applies to V too — and since V is a **scalar**, summing potentials
is far easier than summing fields. Standard trick: find V by summation, then get
**E** = −∇V.

### The conservative property

    ∮ E·dl = 0        ⟺       ∇ × E = 0

Work done round a closed loop is zero. **This holds only in statics.** Module 06
breaks it.

### E from V

    E = −∇V

Example: V = 10/r² in spherical → **E** = −∂V/∂r **a**_r = **20/r³ a_r** V/m.

## 3.6 Electric dipole

Two charges +Q, −Q separated by small **d**. Dipole moment **p** = Q**d**.

    V = (p cos θ) / (4πε₀ r²)                  falls as 1/r²
    E = (p / 4πε₀r³)(2cosθ a_r + sinθ a_θ)     falls as 1/r³

Remember the pattern: monopole V~1/r, dipole V~1/r², quadrupole V~1/r³. Higher
multipoles die faster. This is the basis of the multipole expansion and, later,
of antenna theory.

## 3.7 Energy in the electrostatic field

Assembling n point charges takes work:

    W_E = ½ Σ Q_k V_k

In continuous form, the energy lives *in the field* itself:

    W_E = ½ ∫_v D·E dv = ½ ∫ ε E² dv        [J]

Energy density w_E = ½ εE² = ½ D·E = D²/(2ε)  [J/m³].

This is a conceptual turning point: energy is not "in the charges", it is stored
in the space around them. Later, that stored energy is what propagates away as a
wave.

## 3.8 Capacitance

    C = Q / V        [F]

Method: assume Q on the conductors → find **D** (Gauss) → find **E** → find
V = −∫**E**·d**l** between them → divide.

Standard results:

| Geometry | Capacitance |
|---|---|
| Parallel plates, area S, spacing d | C = εS/d |
| Coaxial, radii a<b, length L | C = 2πεL / ln(b/a) |
| Concentric spheres, radii a<b | C = 4πε / (1/a − 1/b) |
| Isolated sphere radius a | C = 4πεa |
| Two-wire line, radius a, spacing d | C = πε / cosh⁻¹(d/2a) |

Energy stored: W = ½CV² = ½QV = Q²/2C.

## 3.9 Worked examples

**Example 1.** Point charges Q₁ = 2 mC at (0,0,0) and Q₂ = −3 mC at (2,0,0).
Find **E** at (1,0,0).

From Q₁: E₁ = 9×10⁹ × 2×10⁻³ / 1² = 1.8×10⁷ V/m along +**a**_x.
From Q₂: distance 1 m, magnitude 9×10⁹ × 3×10⁻³ /1² = 2.7×10⁷ V/m, pointing
*toward* Q₂ (negative charge attracts), i.e. +**a**_x.

**E** = (1.8 + 2.7)×10⁷ **a**_x = **4.5×10⁷ a_x V/m**

**Example 2.** A coaxial cable has a = 1 mm, b = 4 mm, ε_r = 2.25. Find C per
metre and the maximum E if 1 kV is applied.

C/L = 2πε₀ε_r / ln(b/a) = 2π(8.854e−12)(2.25)/ln 4 = 1.252e−10/1.386
  = **90.3 pF/m**

E(ρ) = V / (ρ ln(b/a)). Maximum at ρ = a:
E_max = 1000/(1e−3 × 1.386) = **7.2×10⁵ V/m = 0.72 MV/m**

(Note: E is largest at the inner conductor — that is where cables break down,
and why HV cable design fattens the centre conductor.)

**Example 3.** Find the work to move a 2 μC charge from infinity to a point 0.5 m
from a 10 μC charge.

V = 9×10⁹ × 10×10⁻⁶ / 0.5 = 1.8×10⁵ V
W = QV = 2×10⁻⁶ × 1.8×10⁵ = **0.36 J**

## 3.10 Exercises

1. An infinite line charge ρ_L = 5 nC/m lies along the z-axis. Find **E** at
   (3, 4, 0). (Answer: 17.98 **a**_ρ V/m, with ρ = 5 m and **a**_ρ = 0.6**a**_x+0.8**a**_y.)
2. A spherical shell of radius 2 m carries ρ_S = 10 nC/m². Find E at r = 1 m and
   r = 4 m. (0 and 28.2 V/m.)
3. V = 2x²y − 5z. Find **E** at (−4, 3, 6) and the energy density there.
4. Derive C for concentric spheres from scratch, starting with Gauss's law.
5. Two parallel plates 5 mm apart with ε_r = 4 have 500 V across them. Find
   **E**, **D**, and the stored energy density.

## Takeaways

- Coulomb → superposition → Gauss. Gauss is Coulomb repackaged for symmetry.
- V is a scalar; use it whenever you can, then differentiate to get **E**.
- Energy lives in the field, density ½εE².
- Capacitance is a pure geometry-plus-material number: Q/V, and Q cancels.
