# Module 11 — Formula Sheet

## Constants
ε₀ = 8.854×10⁻¹² F/m  |  1/4πε₀ = 9×10⁹  |  μ₀ = 4π×10⁻⁷ H/m
c = 3×10⁸ m/s  |  η₀ = 377 Ω ≈ 120π  |  e = 1.602×10⁻¹⁹ C

## Vector operators

| | Cartesian | Cylindrical | Spherical |
|---|---|---|---|
| dl | dx,dy,dz | dρ, ρdφ, dz | dr, rdθ, r sinθ dφ |
| dv | dx dy dz | ρ dρ dφ dz | r² sinθ dr dθ dφ |

∇V (Cart) = ∂V/∂x **a**_x + ...
∇·**A** (Cart) = ∂A_x/∂x + ∂A_y/∂y + ∂A_z/∂z
∇·**A** (Cyl) = (1/ρ)∂(ρA_ρ)/∂ρ + (1/ρ)∂A_φ/∂φ + ∂A_z/∂z
∇·**A** (Sph) = (1/r²)∂(r²A_r)/∂r + (1/r sinθ)∂(A_θsinθ)/∂θ + (1/r sinθ)∂A_φ/∂φ

∮**A**·d**S** = ∫(∇·**A**)dv  |  ∮**A**·d**l** = ∫(∇×**A**)·d**S**
∇×(∇V) = 0  |  ∇·(∇×**A**) = 0  |  ∇²**A** = ∇(∇·**A**) − ∇×(∇×**A**)

## Electrostatics
**F** = Q₁Q₂**a**_R/(4πε₀R²)  |  **E** = **F**/Q  |  **D** = ε**E**
Point: E = Q/4πε₀r²,  V = Q/4πε₀r
Line: E = ρ_L/2πε₀ρ  |  Sheet: E = ρ_S/2ε₀
∮**D**·d**S** = Q_enc  |  ∇·**D** = ρ_v  |  **E** = −∇V  |  ∮**E**·d**l** = 0
Dipole: V = p cosθ/4πε₀r²
w_E = ½εE²  |  W = ½∫**D**·**E**dv  |  W = ½CV²
∇²V = −ρ_v/ε (Poisson), ∇²V = 0 (Laplace)

**C:** plates εS/d | coax 2πεL/ln(b/a) | spheres 4πε/(1/a−1/b) | isolated 4πεa

**BCs:** E_t1 = E_t2 | D_n1 − D_n2 = ρ_S | tanθ₁/tanθ₂ = ε₁/ε₂

## Currents and materials
**J** = σ**E**  |  I = ∫**J**·d**S**  |  R = ℓ/σS  |  ∇·**J** = −∂ρ_v/∂t
T_r = ε/σ  |  **D** = ε₀**E** + **P**  |  ε_r = 1 + χ_e

## Magnetostatics
d**H** = I d**l**×**a**_R/(4πR²)  |  **B** = μ**H**
Wire: H = I/2πρ | Loop centre: H = I/2a | Solenoid: H = nI | Toroid: H = NI/2πρ
Sheet: **H** = ½**K**×**a**_n
∮**H**·d**l** = I_enc  |  ∇×**H** = **J**  |  ∮**B**·d**S** = 0  |  ∇·**B** = 0
**B** = ∇×**A**,  **A** = ∫μI d**l**/4πR
**F** = q(**E** + **u**×**B**)  |  **F** = I**L**×**B**  |  **T** = **m**×**B**
Parallel wires: F/L = μ₀I₁I₂/2πd
w_m = ½μH²  |  W = ½LI²

**L:** solenoid μN²S/ℓ | toroid μN²S/2πρ₀ | coax (μ/2π)ln(b/a)

**BCs:** B_n1 = B_n2 | H_t1 − H_t2 = K | tanθ₁/tanθ₂ = μ₁/μ₂

**Magnetic circuit:** ℱ = NI = Ψℛ, ℛ = ℓ/μS

## Maxwell's equations

| Differential | Integral |
|---|---|
| ∇·**D** = ρ_v | ∮**D**·d**S** = Q_enc |
| ∇·**B** = 0 | ∮**B**·d**S** = 0 |
| ∇×**E** = −∂**B**/∂t | ∮**E**·d**l** = −dΨ/dt |
| ∇×**H** = **J** + ∂**D**/∂t | ∮**H**·d**l** = I + ∫(∂**D**/∂t)·d**S** |

emf = −N dΨ/dt  |  motional emf = ∮(**u**×**B**)·d**l** = Bℓu
**S** = **E**×**H**  |  **S**_avg = ½Re{**E**_s×**H**_s*}
Loss tangent: tan δ = σ/ωε

## Plane waves
γ = α + jβ = √(jωμ(σ+jωε))  |  η = √(jωμ/(σ+jωε))
α = ω√(με/2 [√(1+(σ/ωε)²) − 1]),  β = ω√(με/2 [√(1+(σ/ωε)²) + 1])
u = ω/β  |  λ = 2π/β  |  δ = 1/α

- Free space: β = ω/c, η = 377
- Lossless: β = ω√(με), η = √(μ/ε), u = c/√(ε_rμ_r)
- Good conductor: α = β = 1/δ = √(πfμσ), η = √(ωμ/σ)∠45°, λ = 2πδ
- Good dielectric: α ≈ (σ/2)√(μ/ε), β ≈ ω√(με), η ≈ √(μ/ε)

Γ = (η₂−η₁)/(η₂+η₁)  |  τ = 2η₂/(η₂+η₁)  |  s = (1+|Γ|)/(1−|Γ|)
α[dB/m] = 8.686 α[Np/m]
Snell: sinθ_i/sinθ_t = n₂/n₁ | θ_B = tan⁻¹√(ε₂/ε₁) | θ_c = sin⁻¹(n₂/n₁)

## Transmission lines
γ = √((R+jωL)(G+jωC))  |  Z₀ = √((R+jωL)/(G+jωC))
Lossless: β = ω√(LC), Z₀ = √(L/C), u = 1/√(LC)
LC = με  |  G/C = σ/ε  |  distortionless: RC = GL

Γ_L = (Z_L−Z₀)/(Z_L+Z₀)  |  s = (1+|Γ|)/(1−|Γ|)  |  RL = −20log|Γ|

    Z_in = Z₀ (Z_L + jZ₀ tanβℓ)/(Z₀ + jZ_L tanβℓ)

λ/2: Z_in = Z_L | λ/4: Z_in = Z₀²/Z_L | shorted stub: jZ₀tanβℓ | open: −jZ₀cotβℓ
QW transformer: Z₀′ = √(Z₀Z_L)
Smith chart: one revolution = λ/2, clockwise = toward generator

## Waveguides (rectangular a×b)
f_c = (u′/2)√((m/a)²+(n/b)²)  |  λ_c = 2/√((m/a)²+(n/b)²)
Dominant TE₁₀: f_c = u′/2a, λ_c = 2a
β = β′√(1−(f_c/f)²)  |  λ_g = λ′/√(1−(f_c/f)²)
u_p = u′/√(1−(f_c/f)²)  |  u_g = u′√(1−(f_c/f)²)  |  u_p u_g = u′²
η_TE = η′/√(1−(f_c/f)²)  |  η_TM = η′√(1−(f_c/f)²)
Cavity: f_r = (u′/2)√((m/a)²+(n/b)²+(p/d)²)  |  Q = ωW/P_loss

## Antennas
Hertzian: E_θ = jη₀I₀βdl sinθ e^{−jβr}/4πr,  R_rad = 80π²(dl/λ)², D = 1.5
Half-wave dipole: R_rad = 73 Ω, Z_in = 73+j42.5, D = 1.64 (2.15 dBi)
Monopole: R_rad = 36.5 Ω, D = 3.28 (5.15 dBi)
Small loop: R_rad = 320π⁴N²(S/λ²)²
U = r²S_avg  |  D = 4πU_max/P_rad  |  G = e_r D  |  A_e = λ²G/4π
Friis: P_r/P_t = G_tG_r(λ/4πr)²
FSPL(dB) = 20log r_km + 20log f_MHz + 32.44
Radar: P_r = P_tG²λ²σ/((4π)³r⁴)
Array: AF = sin(Nψ/2)/sin(ψ/2), ψ = βd cosθ + α
Dish: G = e(πD/λ)², HPBW ≈ 70λ/D
