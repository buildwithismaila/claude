# Module 02 — Vector Calculus: Gradient, Divergence, Curl

Maxwell's equations are four statements written with div and curl. If you
understand these two operators *physically*, Maxwell's equations stop being
symbols and become sentences.

## 2.1 Line, surface, volume integrals

**Line integral** ∫_L **A**·d**l** — add up the component of **A** along a path.
"How much does the field push you as you walk this route?" Work and voltage are
line integrals.

If the path is closed we write ∮ **A**·d**l** and call it the **circulation**.

**Surface integral (flux)** Ψ = ∫_S **A**·d**S** — add up the component of **A**
passing *through* a surface. "How much crosses this net?"

For a closed surface, ∮_S **A**·d**S** is the *net outflow*.

**Volume integral** ∫_v ρ dv — total amount of a scalar density in a region.

## 2.2 Gradient — steepest climb of a scalar field

For scalar V, ∇V points in the direction of maximum increase of V, with
magnitude equal to that rate of increase.

- Cartesian: ∇V = (∂V/∂x)**a**_x + (∂V/∂y)**a**_y + (∂V/∂z)**a**_z
- Cylindrical: ∇V = (∂V/∂ρ)**a**_ρ + (1/ρ)(∂V/∂φ)**a**_φ + (∂V/∂z)**a**_z
- Spherical: ∇V = (∂V/∂r)**a**_r + (1/r)(∂V/∂θ)**a**_θ + (1/(r sinθ))(∂V/∂φ)**a**_φ

Key facts:
- dV = ∇V · d**l** (change in V for a small step d**l**).
- ∇V is **perpendicular to surfaces of constant V** (equipotentials).
- In electrostatics **E** = −∇V: the field points "downhill" in potential.

Think of a hill: V is altitude, ∇V points straight uphill, a ball rolls along
−∇V. That is literally what a positive charge does in a potential field.

## 2.3 Divergence — net outflow per unit volume ("is there a source here?")

∇·**A** = lim(Δv→0) [∮_S **A**·d**S**] / Δv

- Cartesian: ∂A_x/∂x + ∂A_y/∂y + ∂A_z/∂z
- Cylindrical: (1/ρ)∂(ρA_ρ)/∂ρ + (1/ρ)∂A_φ/∂φ + ∂A_z/∂z
- Spherical: (1/r²)∂(r²A_r)/∂r + (1/(r sinθ))∂(A_θ sinθ)/∂θ + (1/(r sinθ))∂A_φ/∂φ

Physical reading: put a tiny box at a point. More field lines leaving than
entering ⇒ divergence positive ⇒ a **source** inside. Negative ⇒ a **sink**.
Zero ⇒ lines pass straight through: the field is **solenoidal**.

- ∇·**D** = ρ_v : electric flux diverges from charge. Charge is a source.
- ∇·**B** = 0 : magnetic flux never diverges. No magnetic charge exists;
  B-field lines always close on themselves.

### Divergence theorem (Gauss's theorem)

    ∮_S A·dS = ∫_v (∇·A) dv

"Total outflow through the skin = sum of all the little sources inside."
This converts Maxwell's integral forms into differential forms.

## 2.4 Curl — circulation per unit area ("is there a swirl here?")

The component of ∇×**A** along **a**_n is lim(ΔS→0) [∮_L **A**·d**l**]/ΔS,
with L the rim of ΔS.

Cartesian determinant form:

              | a_x     a_y     a_z  |
    ∇ × A  =  | ∂/∂x    ∂/∂y    ∂/∂z |
              | A_x     A_y     A_z  |

Cylindrical:
∇×**A** = [(1/ρ)∂A_z/∂φ − ∂A_φ/∂z]**a**_ρ + [∂A_ρ/∂z − ∂A_z/∂ρ]**a**_φ
        + (1/ρ)[∂(ρA_φ)/∂ρ − ∂A_ρ/∂φ]**a**_z

Spherical:
∇×**A** = (1/(r sinθ))[∂(A_φ sinθ)/∂θ − ∂A_θ/∂φ]**a**_r
        + (1/r)[(1/sinθ)∂A_r/∂φ − ∂(rA_φ)/∂r]**a**_θ
        + (1/r)[∂(rA_θ)/∂r − ∂A_r/∂θ]**a**_φ

Physical reading: drop a tiny paddlewheel into the field. If it spins, curl is
nonzero, directed along the spin axis by the right-hand rule. Zero curl
everywhere ⇒ **irrotational** / **conservative** ⇒ a potential exists.

- ∇×**E** = 0 (statics): electrostatic field is conservative, V well-defined.
- ∇×**H** = **J** + ∂**D**/∂t : current and changing E-flux make magnetic swirl.
- ∇×**E** = −∂**B**/∂t : changing magnetic flux makes electric swirl — why
  transformers work, and why "voltage" stops being single-valued in AC fields.

### Stokes's theorem

    ∮_L A·dl = ∫_S (∇×A)·dS

"Circulation round the rim = total swirl over any surface stretched on that rim."

## 2.5 Two identities you must memorize

    ∇ × (∇V) = 0        curl of a gradient is always zero
    ∇ · (∇ × A) = 0     divergence of a curl is always zero

Consequences:
- ∇×**E** = 0 in statics ⇒ **E** is a gradient ⇒ **E** = −∇V exists.
- ∇·**B** = 0 always ⇒ **B** is a curl ⇒ **B** = ∇×**A** defines the magnetic
  vector potential **A**.

## 2.6 The Laplacian

∇²V = ∇·(∇V)

- Cartesian: ∂²V/∂x² + ∂²V/∂y² + ∂²V/∂z²
- Cylindrical: (1/ρ)∂/∂ρ(ρ ∂V/∂ρ) + (1/ρ²)∂²V/∂φ² + ∂²V/∂z²
- Spherical: (1/r²)∂/∂r(r²∂V/∂r) + (1/(r²sinθ))∂/∂θ(sinθ ∂V/∂θ)
             + (1/(r²sin²θ))∂²V/∂φ²

∇²V = 0 is **Laplace's equation** (source-free regions).
∇²V = −ρ_v/ε is **Poisson's equation**.

Vector identity used to derive the wave equation:
∇²**A** = ∇(∇·**A**) − ∇×(∇×**A**)

## 2.7 Worked examples

**Example 1.** **A** = x²y **a**_x + yz **a**_y + xz² **a**_z. Find ∇·**A** and
∇×**A** at (1, 2, 1).

∇·**A** = 2xy + z + 2xz → 4 + 1 + 2 = **7**

∇×**A**:
- x: ∂A_z/∂y − ∂A_y/∂z = 0 − y = −y → −2
- y: ∂A_x/∂z − ∂A_z/∂x = 0 − z² = −z² → −1
- z: ∂A_y/∂x − ∂A_x/∂y = 0 − x² = −x² → −1

∇×**A** = **−2a_x − a_y − a_z**

**Example 2.** Show **E** = (Q/4πε₀r²)**a**_r is divergence-free except at r=0.

∇·**E** = (1/r²) ∂/∂r [ r² · Q/(4πε₀r²) ] = (1/r²) ∂/∂r [Q/(4πε₀)] = **0**, r>0.

Gauss's law in action: no charge anywhere except the origin, so the field
diverges nowhere else — yet flux through any enclosing sphere is Q/ε₀ because
all the source sits at that one point.

**Example 3.** Verify Stokes's theorem for
**A** = ρ cosφ **a**_ρ + ρ² sinφ **a**_φ over the quarter disc ρ ≤ 2,
0 ≤ φ ≤ π/2 in the z = 0 plane.

(∇×**A**)_z = (1/ρ)[∂(ρ·ρ²sinφ)/∂ρ − ∂(ρcosφ)/∂φ]
            = (1/ρ)[3ρ² sinφ + ρ sinφ] = 3ρ sinφ + sinφ

∫∫ (3ρ sinφ + sinφ) ρ dρ dφ = ∫₀^{π/2} sinφ dφ · ∫₀² (3ρ² + ρ) dρ
 = 1 · [ρ³ + ρ²/2]₀² = 8 + 2 = **10**

The closed line integral over the three edges gives 10 as well: the two straight
radial edges contribute 0 (A_ρ·dl integrates to 0 at φ=0 and the a_φ term is
perpendicular there), and the arc contributes 10.

## 2.8 Exercises

1. For V = x²yz find ∇V at (1,1,1), then verify ∇×(∇V) = 0.
2. Find ∇·**A** and ∇×**A** for **A** = (1/ρ)**a**_φ, ρ ≠ 0. Why does this
   matter for the field around a current-carrying wire?
3. Verify the divergence theorem for **A** = r **a**_r over a sphere of radius a.
   (Both sides = 4πa³.)
4. Show ∇²(1/r) = 0 for r ≠ 0.

## Takeaways

- **grad**: scalar → vector, "steepest ascent".
- **div**: vector → scalar, "source strength".
- **curl**: vector → vector, "swirl strength and axis".
- Divergence and Stokes theorems bridge the integral and differential forms of
  every law that follows.
