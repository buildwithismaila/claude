# Module 12 — Problem Set with Full Solutions

Work each problem on paper before reading the solution. Twenty problems spanning
the whole course, roughly in exam order and exam style.

---

**P1.** Given **A** = 2**a**_x − 3**a**_y + **a**_z and **B** = 4**a**_x + 5**a**_z,
find the angle between them and the component of **A** perpendicular to **B**.

*Solution.* **A**·**B** = 8 + 0 + 5 = 13. |A| = √14 = 3.742, |B| = √41 = 6.403.
cos θ = 13/23.96 = 0.5426 ⇒ **θ = 57.1°**
Parallel component: (**A**·**a**_B)**a**_B = (13/41)(4**a**_x + 5**a**_z)
 = 1.268**a**_x + 1.585**a**_z
Perpendicular part: **A** − that = **0.732a_x − 3a_y − 0.585a_z**
(Check: dot with **B** = 2.93 − 2.93 = 0 ✓)

---

**P2.** Verify the divergence theorem for **A** = 2ρz **a**_ρ + ρ **a**_z over
the cylinder ρ ≤ 2, 0 ≤ z ≤ 3.

*Solution.* ∇·**A** = (1/ρ)∂(ρ·2ρz)/∂ρ + ∂(ρ)/∂z = (1/ρ)(4ρz) = 4z
∫∇·**A** dv = ∫₀^{2π}∫₀²∫₀³ 4z ρ dz dρ dφ = 2π · [ρ²/2]₀² · [2z²]₀³
 = 2π(2)(18) = **72π**

Surface: curved wall (ρ=2): ∫ 2(2)z · (2 dφ dz) = ∫₀^{2π}∫₀³ 8z dz dφ
 = 2π(4·9) = 72π. Top (z=3): ∫ρ·ρdρdφ = 2π(8/3) = 16π/3.
Bottom (z=0), outward is −**a**_z: −∫ρ·ρdρdφ = −16π/3.
Total = 72π + 16π/3 − 16π/3 = **72π** ✓

---

**P3.** Two point charges, 5 nC at (2,0,4) and −2 nC at (−3,0,5). Find the
potential at (1,0,1) and the energy needed to bring a 1 nC charge there from ∞.

*Solution.* R₁ = √((1−2)²+0+(1−4)²) = √10 = 3.162
R₂ = √((1+3)²+0+(1−5)²) = √32 = 5.657
V = 9×10⁹[5e−9/3.162 + (−2e−9)/5.657] = 9[1.581 − 0.3536] = 9(1.2276)
 = **11.05 V**
W = QV = 1e−9 × 11.05 = **11.05 nJ**

---

**P4.** A spherical volume charge ρ_v = 10/r² nC/m³ exists for 1 ≤ r ≤ 3 m.
Find **D** at r = 2 m and r = 5 m.

*Solution.* Q(r) = ∫₁^r (10e−9/r′²)(4πr′²)dr′ = 40π×10⁻⁹ (r−1)
At r = 2: Q = 40π×10⁻⁹ = 1.257×10⁻⁷ C
D = Q/4πr² = 1.257e−7/(4π·4) = **2.5 nC/m²**
At r = 5: all charge enclosed, Q = 40π×10⁻⁹(2) = 2.513×10⁻⁷
D = 2.513e−7/(4π·25) = **0.8 nC/m²**

---

**P5.** Region z > 0 has ε_r = 2, region z < 0 has ε_r = 5, no free surface
charge. **E**₁ (in z>0) = 4**a**_x − 3**a**_y + 6**a**_z V/m. Find **E**₂ and
the angles the fields make with the normal.

*Solution.* Tangential continuous: E_x2 = 4, E_y2 = −3.
Normal D continuous: 2(6) = 5E_z2 ⇒ E_z2 = 2.4
**E₂ = 4a_x − 3a_y + 2.4a_z V/m**
θ₁: tanθ₁ = √(16+9)/6 = 5/6 ⇒ θ₁ = **39.8°**
θ₂: tanθ₂ = 5/2.4 = 2.083 ⇒ θ₂ = **64.4°**
Check: tanθ₁/tanθ₂ = 0.8333/2.083 = 0.4 = ε₁/ε₂ = 2/5 ✓

---

**P6.** A coaxial capacitor a = 5 mm, b = 15 mm, length 60 cm, with two
dielectric layers: ε_r = 4 from 5 to 10 mm, ε_r = 2 from 10 to 15 mm.
Find C.

*Solution.* Series combination (same Q, potentials add).
C₁ = 2πε₀(4)(0.6)/ln(10/5) = 2π(8.854e−12)(4)(0.6)/0.6931
 = 1.335e−10/0.6931 = 192.6 pF
C₂ = 2πε₀(2)(0.6)/ln(15/10) = 6.674e−11/0.4055 = 164.6 pF
C = C₁C₂/(C₁+C₂) = (192.6×164.6)/357.2 = **88.8 pF**

---

**P7.** A 20 nC point charge is 3 cm above an infinite grounded conducting plane.
Find the force on it and the total induced charge.

*Solution.* Image −20 nC at 3 cm below; separation 6 cm.
F = (9e9)(20e−9)²/(0.06)² = (9e9)(4e−16)/(3.6e−3) = 3.6e−6/3.6e−3
 = **1.0×10⁻³ N = 1 mN**, attractive (toward the plane).
Total induced charge = **−20 nC** exactly (all field lines from Q terminate on
the plane).

---

**P8.** An infinite sheet of current **K** = 10**a**_x A/m lies in the z = 0
plane. Find **H** at z = ±2 m, and the force per unit area on a second sheet
**K** = 5**a**_x A/m at z = 2.

*Solution.* **H** = ½**K**×**a**_n.
For z>0, **a**_n = **a**_z: ½(10**a**_x × **a**_z) = ½(10)(−**a**_y) = **−5a_y A/m**
For z<0: **+5a_y A/m**
**B** at the second sheet = μ₀(−5**a**_y) = −6.28×10⁻⁶ **a**_y T
Force per area = **K**₂ × **B** = 5**a**_x × (−6.28e−6 **a**_y)
 = −3.14×10⁻⁵ **a**_z N/m² — **attractive** (parallel currents attract), magnitude
**31.4 μN/m²**

---

**P9.** A toroid with a rectangular cross-section (inner radius 4 cm, outer 6 cm,
height 2 cm) has 800 turns and μ_r = 1. Find L exactly (not by the mean-radius
approximation).

*Solution.* H = NI/2πρ, B = μ₀NI/2πρ
Ψ = ∫₀.₀₄^0.06 (μ₀NI/2πρ)(0.02 dρ) = (μ₀NI(0.02)/2π) ln(6/4)
 = (4πe−7)(800)I(0.02)(0.4055)/(2π) = (2e−7)(800)(0.02)(0.4055) I
 = 1.298×10⁻⁶ I
L = NΨ/I = 800 × 1.298e−6 = **1.038 mH**

(Mean-radius approximation: L = μ₀N²S/2πρ₀ = (4πe−7)(640000)(4e−4)/(2π×0.05)
= 1.024 mH — within 1.4%.)

---

**P10.** An iron ring (μ_r = 1500, mean length 50 cm, cross-section 4 cm²) has a
1 mm air gap and 500 turns. Find the current for a flux of 0.6 mWb, and comment.

*Solution.* Iron: ℛ_i = ℓ/μS = 0.499/((4πe−7)(1500)(4e−4))
 = 0.499/(7.54e−7) = 6.62×10⁵ A-t/Wb
Gap: ℛ_g = 0.001/((4πe−7)(4e−4)) = 0.001/(5.027e−10) = 1.989×10⁶ A-t/Wb
Total ℛ = 2.65×10⁶
NI = Ψℛ = 6e−4 × 2.65e6 = 1590 A-t ⇒ **I = 3.18 A**

Comment: the 1 mm gap contributes 75% of the total reluctance despite being
0.2% of the path length. **Air gaps dominate magnetic circuits.**

---

**P11.** A square loop of side 20 cm lies in the xy-plane. **B** = 0.4 cos(500t)
**a**_z T. Find the induced emf and the current if the loop resistance is 0.5 Ω.

*Solution.* Ψ = BS = 0.4(0.04)cos(500t) = 0.016 cos(500t) Wb
emf = −dΨ/dt = 0.016(500) sin(500t) = **8 sin(500t) V**
I = 8 sin(500t)/0.5 = **16 sin(500t) A**

---

**P12.** Show that in a good conductor the conduction current dominates and
compute the frequency at which they are equal for copper (σ = 5.8×10⁷, ε_r = 1).

*Solution.* σ = ωε ⇒ f = σ/(2πε₀) = 5.8e7/(2π × 8.854e−12)
 = 5.8e7/5.563e−11 = **1.04×10¹⁸ Hz**

That is in the X-ray region — far above optical. Copper is a conductor at every
frequency you will ever engineer with. This is why "good conductor
approximation" is essentially always valid for metals.

---

**P13.** A uniform plane wave in a lossy medium (ε_r = 4, μ_r = 1, σ = 10⁻³ S/m)
at 50 MHz. Find tan δ, α, β, η, u, λ, and δ_skin.

*Solution.* ωε = 2π(5e7)(4)(8.854e−12) = 1.1124×10⁻²
tan δ = 1e−3/1.1124e−2 = **0.0899** (a low-loss dielectric)

Use good-dielectric approximations:
α ≈ (σ/2)√(μ/ε) = (5e−4)(377/2) = (5e−4)(188.5) = **0.0943 Np/m**
 (= 0.819 dB/m)
β ≈ ω√(με) = ω√(ε_r)/c = 2π(5e7)(2)/3e8 = **2.094 rad/m**
η ≈ √(μ/ε)(1 + j tanδ/2) = 188.5(1 + j0.045) = **188.5∠2.57° Ω**
u = ω/β = 3.14e8/2.094 = **1.5×10⁸ m/s** (= c/2 ✓)
λ = 2π/β = **3 m**
δ_skin = 1/α = **10.6 m**

---

**P14.** A wave travelling in air strikes a lossless medium (ε_r = 9, μ_r = 1)
normally with E₀ = 6 V/m. Find Γ, τ, the reflected and transmitted E, the SWR,
and the power in each.

*Solution.* η₁ = 377, η₂ = 377/3 = 125.7
Γ = (125.7 − 377)/(125.7 + 377) = −251.3/502.7 = **−0.5**
τ = 2(125.7)/502.7 = **0.5**
E_r = −3 V/m (phase reversal), E_t = 3 V/m
s = 1.5/0.5 = **3.0**
S_i = 36/(2×377) = 47.7 mW/m²
S_r = |Γ|²S_i = 0.25(47.7) = 11.9 mW/m² (25%)
S_t = 9/(2×125.7) = 35.8 mW/m² (75%) ✓ (11.9 + 35.8 = 47.7)

---

**P15.** A lossless 50 Ω line is terminated in 25 − j50 Ω at 500 MHz, u = 2×10⁸.
Find Γ, SWR, Z_in at 20 cm, and the distance to the first voltage minimum.

*Solution.* λ = 2e8/5e8 = 0.4 m; β = 2π/0.4 = 15.708 rad/m
Γ = (25−j50−50)/(25−j50+50) = (−25−j50)/(75−j50)
 = (55.9∠−116.57°)/(90.14∠−33.69°) = **0.620∠−82.88°**
s = 1.620/0.380 = **4.26**

Z_in at ℓ = 0.2 m = λ/2 ⇒ **Z_in = Z_L = 25 − j50 Ω**
(Half-wavelength repeats the load — no calculation needed.)

First voltage minimum where the total phase = 180°:
2βℓ_min = 180° + θ_Γ ⇒ ℓ_min = (180° − 82.88°)/(2×360°) · λ
Careful: Γ(ℓ) = |Γ|∠(θ_Γ − 2βℓ). Minimum when θ_Γ − 2βℓ = −180°:
2βℓ = 180° − 82.88° = 97.12° ⇒ βℓ = 48.56° = 0.8476 rad
ℓ = 0.8476/15.708 = **0.054 m = 5.4 cm**

---

**P16.** Match a 120 Ω load to a 50 Ω line at 1 GHz (a) with a quarter-wave
transformer in air, (b) find the SWR if instead nothing is done.

*Solution.* (a) Z₀′ = √(50 × 120) = **77.46 Ω**; λ = 0.3 m ⇒ length
 = **7.5 cm**
(b) Γ = (120−50)/170 = 0.4118; s = 1.4118/0.5882 = **2.40**
Reflected power = 17% of incident.

---

**P17.** An air-filled guide, a = 7.2 cm, b = 3.4 cm, operating at 3 GHz.
Which modes propagate? Find λ_g and η for the dominant mode.

*Solution.* f_c(mn) = 15√((m/7.2)² + (n/3.4)²) GHz (cm)
TE₁₀: 15/7.2 = **2.083 GHz** ✓ propagates
TE₂₀: 30/7.2 = 4.167 GHz ✗
TE₀₁: 15/3.4 = 4.412 GHz ✗
So **only TE₁₀ propagates** — good single-mode operation.

f_c/f = 2.083/3 = 0.6944; √(1 − 0.4822) = √0.5178 = 0.7196
λ′ = 10 cm ⇒ λ_g = 10/0.7196 = **13.90 cm**
η_TE = 377/0.7196 = **524 Ω**
u_p = 3e8/0.7196 = 4.17×10⁸ m/s; u_g = 2.16×10⁸ m/s

---

**P18.** A rectangular cavity 4 × 3 × 5 cm, air-filled. Find the three lowest
resonant frequencies.

*Solution.* f = 15√((m/4)² + (n/3)² + (p/5)²) GHz
TE₁₀₁: 15√(0.0625 + 0.04) = 15(0.3202) = **4.80 GHz**
TE₀₁₁: 15√(0 + 0.1111 + 0.04) = 15(0.3887) = **5.83 GHz**
TE₁₁₀ / TM₁₁₀: 15√(0.0625 + 0.1111) = 15(0.4166) = **6.25 GHz**
(TM₁₁₀ is valid; TE₁₁₀ requires p ≠ 0 so it does not exist.)

---

**P19.** A half-wave dipole is fed 250 W at 150 MHz. Find (a) the feed current,
(b) the field strength 20 km away in the direction of maximum radiation,
(c) the power received by an identical dipole there, correctly oriented.

*Solution.* (a) P = ½I₀²(73) ⇒ I₀ = √(500/73) = **2.617 A**
(b) E = η₀I₀/(2πr) = 377(2.617)/(2π×2e4) = 986.6/125664 = **7.85 mV/m**
(c) S = E²/(2η₀) = (7.85e−3)²/754 = 8.17×10⁻⁸ W/m²
A_e = λ²G/4π; λ = 2 m, G = 1.64 ⇒ A_e = 4(1.64)/(4π) = 0.522 m²
P_r = S·A_e = 8.17e−8 × 0.522 = **4.27×10⁻⁸ W = 42.7 nW**

Cross-check with Friis: FSPL = 20log(20) + 20log(150) + 32.44
 = 26.02 + 43.52 + 32.44 = 101.98 dB
P_t = 10log(250×1000) = 53.98 dBm
P_r = 53.98 + 2.15 + 2.15 − 101.98 = −43.7 dBm = 4.27×10⁻⁸ W ✓

---

**P20.** A radar at 10 GHz has P_t = 100 kW, a 2 m dish with 60% efficiency, and
detects a target of σ = 5 m². The minimum detectable signal is −110 dBm. Find
the maximum range.

*Solution.* λ = 0.03 m
G = 0.6(π×2/0.03)² = 0.6(209.44)² = 0.6(43,865) = 26,319 = **44.2 dBi**
P_min = −110 dBm = 10⁻¹⁴ W

r⁴ = P_t G²λ²σ / ((4π)³ P_min)
 = (1e5)(26319)²(9e−4)(5) / (1984.4 × 1e−14)
 = (1e5)(6.927e8)(9e−4)(5) / (1.9844e−11)
 = (3.117e11)/(1.9844e−11) = 1.571×10²²
r = (1.571e22)^{0.25} = **1.12×10⁵·⁵ ... ** compute: log₁₀ = 22.196/4 = 5.549
r = 10^5.549 = **3.54×10⁵ m ≈ 354 km**

Note the r⁴ dependence: to double this range to 708 km you would need
16 × 100 kW = 1.6 MW of transmit power, or +6 dB of antenna gain (a 4 m dish).

---

## Self-assessment

If you solved 16+ of these unaided, you are exam-ready. If you struggled on:

- P1–P2 → revisit Modules 01–02
- P3–P7 → Modules 03–04
- P8–P10 → Module 05
- P11–P12 → Module 06
- P13–P14 → Module 07
- P15–P16 → Module 08
- P17–P18 → Module 09
- P19–P20 → Module 10
