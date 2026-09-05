# Module 10 — Radiation and Antennas

## 10.1 Why anything radiates

Static charge: field lines are attached, energy stays in the near field.
Uniformly moving charge: still no radiation (it is just a static field in a
moving frame).
**Accelerating charge radiates.** Alternating current = charge accelerating back
and forth = radiation.

The field-line picture: when a dipole's charges reverse, field lines that were
attached to the charges pinch off and close on themselves. A closed loop of
**E** with no charges to terminate on cannot stay put — it must propagate away at
c. Those detached loops are the radiated wave.

## 10.2 Retarded potentials

The field here now depends on the source as it was a travel-time ago:

    V(r,t) = ∫ ρ_v(r′, t − R/u) / (4πεR)  dv′
    A(r,t) = ∫ μ J(r′, t − R/u) / (4πR)   dv′

with R = |**r** − **r**′| and retardation t − R/u. Then **B** = ∇×**A** and
**E** = −∇V − ∂**A**/∂t.

Everything about antennas comes out of evaluating **A** and taking curls. The
finite propagation time is what makes radiation possible — with instantaneous
action at a distance, nothing would ever detach.

## 10.3 The Hertzian dipole

An infinitesimal current element of length dl ≪ λ carrying I₀cos ωt. Result in
spherical coordinates (β = 2π/λ):

**Far field (r ≫ λ, the radiation zone):**

    E_θ = j (η₀ I₀ β dl / 4πr) sin θ · e^{−jβr}
    H_φ = E_θ / η₀

Everything else falls faster than 1/r and vanishes.

**Three zones, three behaviours:**

| Term | Falls as | Zone | Meaning |
|---|---|---|---|
| 1/r³ | fastest | near (reactive) | electrostatic/dipole field, stores energy |
| 1/r² | middle | induction | reactive, energy sloshes in and out |
| 1/r | slowest | far (radiation) | the only term that carries net power |

Only the 1/r term matters far away, because power ~ E² ~ 1/r², and the area of a
sphere ~ r² — so the 1/r term delivers constant total power to infinity while all
others deliver zero. **That is the mathematical definition of radiation.**

**Radiated power and radiation resistance:**

    P_rad = ½ ∫ Re{E×H*}·dS = 40π² (dl/λ)² I₀²/... 

carried out: P_rad = ½ I₀² R_rad with

    R_rad = 80π² (dl/λ)²      [Ω]      (Hertzian dipole)

Note (dl/λ)²: a short antenna radiates terribly. dl = λ/100 gives
R_rad = 0.079 Ω — against even a small loss resistance, efficiency collapses.
**This is why electrically small antennas are inefficient**, and why AM broadcast
towers are hundreds of metres tall.

**Small loop** (magnetic dipole), area S, N turns:

    R_rad = 320 π⁴ N² (S/λ²)²

Even worse for small S — but loops are compact and are used in receivers where
the ambient field, not efficiency, sets the signal.

## 10.4 Half-wave dipole

Length ℓ = λ/2, sinusoidal current distribution I(z) = I₀cos βz.

    E_θ = j(η₀I₀/2πr) [cos(π cosθ /2) / sinθ] e^{−jβr}

    S_avg = (η₀I₀²/8π²r²) · [cos((π/2)cosθ)/sinθ]²

    P_rad = 36.56 I₀²  ⇒  **R_rad = 73 Ω**,  Z_in = 73 + j42.5 Ω

Trim slightly below λ/2 (about 0.47λ) and the reactance vanishes — that is why
real dipoles are cut a few percent short.

73 Ω is close to 75 Ω coax, which is not a coincidence: the standard was chosen
to feed dipoles directly.

**Quarter-wave monopole** over a ground plane: image theory makes it equivalent
to half a dipole, so it radiates half the power for the same current:

    R_rad = 36.5 Ω,   same pattern in the upper half-space

## 10.5 Antenna parameters

**Radiation pattern** — |E| or power vs direction, normally plotted in the
E-plane and H-plane. Key numbers: half-power (−3 dB) beamwidth, first-null
beamwidth, side-lobe level, front-to-back ratio.

**Radiation intensity** U(θ,φ) = r² S_avg  [W/sr];  P_rad = ∮ U dΩ.

**Directivity**

    D = U_max / U_avg = 4π U_max / P_rad

| Antenna | D | dBi |
|---|---|---|
| Isotropic (theoretical) | 1 | 0 |
| Hertzian dipole | 1.5 | 1.76 |
| Half-wave dipole | 1.64 | 2.15 |
| Quarter-wave monopole | 3.28 | 5.15 |

**Gain** G = e_r D, with radiation efficiency e_r = R_rad/(R_rad + R_loss).
Gain accounts for ohmic losses; directivity does not.

**Effective aperture** A_e = (λ²/4π) G — the capture area of a receiving antenna.
Note that a *fixed-size* aperture antenna (dish, horn) has G = 4πA_e/λ², so its
gain rises as f²: this is why microwave links use small dishes and get huge gain.

**Beamwidth–directivity rule of thumb:** D ≈ 41253/(θ_E · θ_H) with beamwidths in
degrees.

## 10.6 The Friis transmission equation

    P_r / P_t = G_t G_r (λ / 4πr)²

In dB: P_r = P_t + G_t + G_r − FSPL, where the **free-space path loss** is

    FSPL(dB) = 20 log₁₀(r) + 20 log₁₀(f) + 32.44    (r in km, f in MHz)

Two conclusions worth internalizing:
- Doubling the distance costs 6 dB, always.
- Doubling the frequency also costs 6 dB *for fixed antenna gains* — but if the
  antennas are fixed-*aperture* dishes, higher frequency actually **wins**,
  because each dish gains 6 dB. Hence satellite links climbed from C-band to
  Ku- to Ka-band.

**Radar equation** (round trip, target cross-section σ):

    P_r = P_t G² λ² σ / ((4π)³ r⁴)

r⁴, not r² — the target re-radiates, so the loss happens twice. Doubling radar
range needs 16× the power.

## 10.7 Antenna arrays

N identical elements, spacing d, progressive phase shift α:

    AF = sin(Nψ/2) / sin(ψ/2),    ψ = βd cos θ + α

Total pattern = **element pattern × array factor** (pattern multiplication).

- **Broadside** (α = 0): main beam perpendicular to the array axis.
- **End-fire** (α = −βd): main beam along the array axis.
- **Phased array**: vary α electronically to steer the beam with no moving parts
  — radar, 5G massive MIMO, Starlink terminals.

Two-element array, spacing λ/2:
- α = 0 → broadside figure-of-eight
- α = 180° → end-fire

Array gain over one element ≈ N (ideal), i.e. 10log N dB.

## 10.8 Common antenna types

| Type | Notes |
|---|---|
| Dipole / monopole | The reference. 73 Ω / 36.5 Ω. |
| Folded dipole | Z_in ≈ 300 Ω, wider band; matches twin-lead. |
| Yagi–Uda | Driven element + reflector + directors. 8–15 dBi, cheap, narrowband. |
| Log-periodic | Very wide band, ~7 dBi. TV antennas. |
| Horn | Flared waveguide. 10–25 dBi, low loss, standard gain reference. |
| Parabolic dish | G = e(πD/λ)². 30–60 dBi. Satellite, radio astronomy. |
| Helical | Axial mode gives circular polarization. Satellite uplinks. |
| Microstrip patch | Printed, flat, ~6 dBi, narrowband. Phones, GPS, arrays. |
| Loop | Small: magnetic, poor efficiency. Large (≈λ): efficient. |

## 10.9 Worked examples

**Example 1.** A Hertzian dipole of length 2 cm carries 10 A at 100 MHz. Find
R_rad and P_rad.

λ = 3 m; dl/λ = 0.02/3 = 6.67×10⁻³
R_rad = 80π²(6.67e−3)² = 789.6 × 4.44×10⁻⁵ = **0.0351 Ω**
P_rad = ½I²R = ½(100)(0.0351) = **1.75 W**

Sanity check on efficiency: if the antenna's ohmic resistance is 1 Ω, efficiency
is 0.0351/1.035 = 3.4%. Nearly all the power becomes heat. That is the price of
being short.

**Example 2.** A half-wave dipole radiates 100 W. Find the current, and the field
strength at 10 km broadside (θ = 90°).

P = ½I₀²(73) ⇒ I₀ = √(200/73) = **1.655 A**
E_θ(θ=90°) = η₀I₀/(2πr) = 377 × 1.655/(2π × 10⁴) = 624/62832 = **9.93 mV/m**
S = E²/2η₀ = (9.93e−3)²/754 = **1.31×10⁻⁷ W/m²**
Cross-check with D: S = P·D/(4πr²) = 100(1.64)/(4π×10⁸) = 1.31×10⁻⁷ ✓

**Example 3 (Friis).** A 2.4 GHz link: P_t = 20 dBm, G_t = G_r = 12 dBi,
r = 1 km. Find P_r.

λ = 0.125 m
FSPL = 20log(1) + 20log(2400) + 32.44 = 0 + 67.6 + 32.44 = **100.0 dB**
P_r = 20 + 12 + 12 − 100 = **−56 dBm** (2.5 nW)

Comfortably above a typical −85 dBm receiver sensitivity — 29 dB of link margin.

**Example 4.** A parabolic dish, D = 3 m, at 12 GHz, aperture efficiency 0.6.
Find the gain and half-power beamwidth.

λ = 0.025 m
G = 0.6 (π × 3/0.025)² = 0.6 (376.99)² = 0.6 × 142,122 = 85,273 = **49.3 dBi**
HPBW ≈ 70λ/D = 70(0.025)/3 = **0.583°**

That extreme narrowness is why satellite dishes need careful aiming.

## 10.10 Exercises

1. A Hertzian dipole λ/50 long carries 5 A. Find R_rad, P_rad, and the efficiency
   if R_loss = 0.5 Ω.
2. Find the maximum power density 5 km from a half-wave dipole radiating 1 kW.
3. A 2-element array with d = λ/4 and α = −90°. Sketch |AF| and identify the
   direction of maximum.
4. A GPS satellite transmits 27 W at 1.575 GHz with 13 dBi gain from 20,200 km.
   Compute the received power on a 0 dBi antenna. Comment on why GPS needs
   spread-spectrum processing gain.
5. Prove D = 1.5 for a Hertzian dipole by integrating sin²θ over the sphere.

## Takeaways

- Acceleration radiates; only the 1/r field term carries power to infinity.
- R_rad ∝ (dl/λ)² — short antennas are inefficient, and there is no way around it.
- Half-wave dipole: 73 Ω, 2.15 dBi. Memorize both.
- Friis: 6 dB per doubling of distance; the radar equation costs 12 dB.
- Gain = efficiency × directivity; effective aperture ties gain to physical size.
