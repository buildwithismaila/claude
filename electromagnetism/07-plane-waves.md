# Module 07 — Uniform Plane Waves

## 7.1 Deriving the wave equation

Source-free region (ρ_v = 0, **J** = σ**E**). Take the curl of Faraday's law:

    ∇×(∇×E) = −μ ∂(∇×H)/∂t = −μ ∂/∂t (σE + ε ∂E/∂t)

Use ∇×(∇×**E**) = ∇(∇·**E**) − ∇²**E**, and ∇·**E** = 0:

    ∇²E = μσ ∂E/∂t + με ∂²E/∂t²

In a **lossless** medium (σ = 0):

    ∇²E = με ∂²E/∂t²

This is the wave equation, with speed u = 1/√(με). In free space
u = 1/√(μ₀ε₀) = 2.998×10⁸ m/s = c. Maxwell computed this from purely electrical
measurements, got the speed of light, and concluded light is an EM wave.

## 7.2 The uniform plane wave

"Uniform plane wave": **E** and **H** are constant over any plane perpendicular
to the direction of travel, and both lie *in* that plane (transverse). Take
propagation along +z and **E** along x.

Phasor form: ∇²**E**_s = γ²**E**_s, where the **propagation constant** is

    γ = √(jωμ(σ + jωε)) = α + jβ

- α = **attenuation constant** [Np/m]
- β = **phase constant** [rad/m]

Solution:

    E(z,t) = E₀ e^{−αz} cos(ωt − βz) a_x
    H(z,t) = (E₀/|η|) e^{−αz} cos(ωt − βz − θ_η) a_y

General expressions:

    α = ω √( με/2 [ √(1 + (σ/ωε)²) − 1 ] )
    β = ω √( με/2 [ √(1 + (σ/ωε)²) + 1 ] )

**Intrinsic impedance:**

    η = √( jωμ / (σ + jωε) ) = |η| ∠θ_η        [Ω]

with |η| = √(μ/ε) / [1+(σ/ωε)²]^{1/4} and θ_η = ½ tan⁻¹(σ/ωε), 0 ≤ θ_η ≤ 45°.

**Derived quantities:**
- wavelength λ = 2π/β
- phase velocity u = ω/β = fλ
- skin depth δ = 1/α (distance for the amplitude to fall to 1/e = 36.8%)

**Key structural facts (true for every plane wave):**
1. **E** ⊥ **H** ⊥ direction of propagation (a TEM wave).
2. **E** × **H** points in the direction of travel.
3. E/H = η at every point.
4. In a lossy medium **H** *lags* **E** by θ_η.

## 7.3 The four cases

### (a) Free space (σ=0, μ=μ₀, ε=ε₀)
α = 0, β = ω√(μ₀ε₀) = ω/c, η = η₀ = **377 Ω** (≈120π), u = c.

### (b) Lossless dielectric (σ ≈ 0)
α = 0, β = ω√(με), η = √(μ/ε), u = 1/√(με) = c/√(ε_r μ_r).

Refractive index n = √(ε_r μ_r); for nonmagnetic materials n = √ε_r.

### (c) Good conductor (σ/ωε ≫ 1)

    α = β = √(πfμσ) = 1/δ
    δ = 1/√(πfμσ)         skin depth
    η = √(ωμ/σ) ∠45°      ⇒ H lags E by exactly 45°
    u = ω/β = √(2ω/μσ),   λ = 2πδ

**Skin effect.** At high frequency current crowds into a surface layer of
thickness ~δ. Copper (σ=5.8e7, μ₀):

| Frequency | δ |
|---|---|
| 50 Hz | 9.3 mm |
| 1 kHz | 2.1 mm |
| 1 MHz | 66 μm |
| 1 GHz | 2.1 μm |

Consequences you can now explain: AC resistance exceeds DC resistance;
transmission lines use hollow or stranded (Litz) conductors; silver plating a
waveguide works because only the top few μm carry current; and a metal box is an
excellent shield at RF but poor at 50 Hz.

Surface resistance R_s = 1/(σδ) = √(πfμ/σ) [Ω/square]; AC resistance of a round
wire radius a ≈ R_s·(ℓ/2πa) when a ≫ δ.

### (d) Good (lossy) dielectric (σ/ωε ≪ 1)

    α ≈ (σ/2)√(μ/ε)      (small, frequency-independent to first order)
    β ≈ ω√(με)[1 + (1/8)(σ/ωε)²] ≈ ω√(με)
    η ≈ √(μ/ε)[1 + j σ/(2ωε)]

Often written with complex permittivity ε = ε′ − jε″ and loss tangent
tan δ = ε″/ε′ = σ/(ωε).

## 7.4 Power and the Poynting vector

    S_avg = ½ Re{E_s × H_s*} = (E₀²/2|η|) e^{−2αz} cos θ_η  a_z    [W/m²]

Power falls as e^{−2αz} — **twice** the field attenuation rate, because power
goes as the square of amplitude.

Attenuation in decibels: α[dB/m] = 8.686 × α[Np/m].

## 7.5 Polarization

The path traced by the tip of **E** at a fixed point, over one cycle.

- **Linear**: E_x and E_y in phase (or one is zero). Tip oscillates along a line.
- **Circular**: equal amplitudes, 90° out of phase. Tip traces a circle. RHCP or
  LHCP depending on sign.
- **Elliptical**: the general case.

Practical relevance: a linearly polarized receiving antenna misaligned by angle θ
from the incoming wave loses cos²θ in power (fully cross-polarized = nothing).
Satellite links use circular polarization to be immune to receiver rotation and
to Faraday rotation in the ionosphere.

## 7.6 Reflection and transmission at normal incidence

Wave in medium 1 (η₁) hits a plane boundary with medium 2 (η₂) at z = 0.

    Γ = (η₂ − η₁)/(η₂ + η₁)        reflection coefficient
    τ = 2η₂/(η₂ + η₁)              transmission coefficient
    1 + Γ = τ

Special cases:
- η₂ = η₁ (matched): Γ = 0, everything transmits.
- Perfect conductor (η₂ = 0): Γ = −1. Total reflection with a 180° phase flip;
  **E** = 0 at the surface — that is the boundary condition E_t = 0, recovered.
- η₂ = ∞: Γ = +1.

Standing waves form from incident + reflected:

    SWR (s) = (1+|Γ|)/(1−|Γ|) = E_max/E_min,   1 ≤ s ≤ ∞

Power: fraction reflected = |Γ|², fraction transmitted = 1 − |Γ|².

## 7.7 Oblique incidence (summary)

Angles obey **Snell's laws**:
- θ_i = θ_r (reflection)
- sin θ_i / sin θ_t = √(μ₂ε₂)/√(μ₁ε₁) = n₂/n₁ (refraction)

Two polarizations behave differently:
- **Perpendicular (TE)**: **E** ⊥ plane of incidence.
  Γ_⊥ = (η₂cosθ_i − η₁cosθ_t)/(η₂cosθ_i + η₁cosθ_t)
- **Parallel (TM)**: **E** in the plane of incidence.
  Γ_∥ = (η₂cosθ_t − η₁cosθ_i)/(η₂cosθ_t + η₁cosθ_i)

Two named consequences:
- **Brewster angle** θ_B = tan⁻¹(√(ε₂/ε₁)): Γ_∥ = 0, parallel polarization is
  fully transmitted. This is why polarized sunglasses cut glare off water.
- **Total internal reflection** for n₁ > n₂ beyond the critical angle
  θ_c = sin⁻¹(n₂/n₁). This is how optical fibre works.

## 7.8 Worked examples

**Example 1.** In free space, **E** = 10 cos(10⁸t − βz)**a**_x V/m. Find β, λ,
**H**, and S_avg.

β = ω/c = 10⁸/3×10⁸ = **0.333 rad/m**
λ = 2π/β = **18.85 m**;  f = ω/2π = 15.9 MHz
H₀ = E₀/η₀ = 10/377 = 26.5 mA/m ⇒ **H** = 26.5 cos(10⁸t − 0.333z)**a**_y mA/m
S_avg = E₀²/(2η₀) = 100/754 = **0.133 W/m²**

**Example 2.** A wave at 10 GHz in copper (σ = 5.8×10⁷). Find δ, α, β, η, λ, u.

δ = 1/√(πfμ₀σ) = 1/√(π × 10¹⁰ × 4π×10⁻⁷ × 5.8×10⁷)
  = 1/√(2.29×10¹²) = 1/1.513×10⁶ = **0.66 μm**
α = β = 1/δ = **1.513×10⁶ (Np/m and rad/m)**
|η| = √(2)·... simpler: |η| = √(ωμ/σ) = √(2π×10¹⁰×4π×10⁻⁷/5.8×10⁷)
  = √(1.362×10⁻³) = 0.0369 Ω, so **η = 0.0369∠45° Ω**
λ = 2πδ = **4.15 μm**;  u = ω/β = 6.28×10¹⁰/1.513×10⁶ = **4.15×10⁴ m/s**

Note how slow and how short: an EM wave inside copper crawls, and dies within a
micron. That is what "conductors don't let fields in" means quantitatively.

**Example 3.** A plane wave in air strikes a dielectric with ε_r = 4 normally.
Find Γ, τ, SWR, and the transmitted power fraction.

η₁ = 377, η₂ = 377/√4 = 188.5
Γ = (188.5 − 377)/(188.5 + 377) = −188.5/565.5 = **−0.333**
τ = 2(188.5)/565.5 = **0.667**
s = (1+0.333)/(1−0.333) = **2.0**
Reflected power = |Γ|² = 11.1%; **transmitted = 88.9%**

**Example 4.** Loss tangent check: dry earth σ = 10⁻³ S/m, ε_r = 10.
At 1 MHz: σ/ωε = 10⁻³/(2π×10⁶ × 10 × 8.854×10⁻¹²) = 10⁻³/5.56×10⁻⁴ = **1.8**
Neither a good conductor nor a good dielectric — use the exact formulas.

## 7.9 Exercises

1. A 100 MHz wave travels in a medium with ε_r = 9, μ_r = 1, σ = 0. Find u, λ, η.
2. Find the skin depth of aluminium (σ = 3.5×10⁷) at 60 Hz and at 1 GHz.
3. **E** = 5cos(ωt−βz)**a**_x + 5sin(ωt−βz)**a**_y. What polarization is this?
4. A wave in a dielectric (ε_r=2.25) hits free space normally. Find Γ, SWR.
5. Light in glass (n=1.5) hits an air interface. Find the critical angle and
   the Brewster angle.
6. A radio wave attenuates by 30 dB over 100 m. Find α in Np/m.

## Takeaways

- One wave equation, one propagation constant γ = α + jβ, four special cases.
- η is the field-theory version of characteristic impedance; 377 Ω in free space.
- Skin depth explains AC resistance, shielding, and why RF conductors are hollow.
- Γ and SWR at a boundary are exactly the transmission-line results of Module 08,
  arrived at from fields instead of circuits.
