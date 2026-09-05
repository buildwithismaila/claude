# Module 09 — Waveguides and Cavity Resonators

## 9.1 Why waveguides

Above a few GHz, coaxial cable becomes unusable: conductor loss rises as √f
(skin effect), the dielectric loses power, and the inner conductor gets so thin
that power handling collapses. A hollow metal pipe has no centre conductor and no
dielectric — so it can carry high power at low loss.

The price: a waveguide is a **high-pass filter**. Below its cutoff frequency,
nothing propagates at all.

## 9.2 Mode classification

Since there is only one conductor, a TEM wave is impossible (a TEM wave needs
two conductors to hold the transverse voltage). So one field component must lie
along the propagation direction.

- **TE (transverse electric)**: E_z = 0, H_z ≠ 0
- **TM (transverse magnetic)**: H_z = 0, E_z ≠ 0
- **TEM**: both zero — needs two conductors (coax, twin-lead, stripline)

## 9.3 Rectangular waveguide (dimensions a × b, a > b)

Solve the Helmholtz equation with the boundary condition E_t = 0 on all walls,
by separation of variables. Result for TE_mn:

    H_z = H₀ cos(mπx/a) cos(nπy/b) e^{−jβz}

and for TM_mn:

    E_z = E₀ sin(mπx/a) sin(nπy/b) e^{−jβz}

m = half-cycle variations along x, n along y.

### Cutoff frequency

    f_c(mn) = (u′/2) √( (m/a)² + (n/b)² ),   u′ = 1/√(με)

    λ_c = 2 / √((m/a)² + (n/b)²)

### Propagation constant

    β = √(ω²με − (mπ/a)² − (nπ/b)²) = β′ √(1 − (f_c/f)²)

- f > f_c: β real → propagation
- f < f_c: β imaginary → **evanescent**, field decays exponentially, no power flows

### Guide quantities (for f > f_c)

    λ_g = λ′ / √(1 − (f_c/f)²)         guide wavelength (LONGER than free-space)
    u_p = u′ / √(1 − (f_c/f)²)         phase velocity (FASTER than c — allowed!)
    u_g = u′ √(1 − (f_c/f)²)           group velocity (slower than c — energy speed)
    u_p · u_g = u′²

> **Faster than light?** No. u_p is the speed of a phase pattern, carrying no
> information. The wave bounces down the guide at angle; the zig-zag pattern's
> intersection with the wall moves faster than the wave itself, exactly as the
> waterline of a wave hitting a beach obliquely races along the sand. Information
> travels at u_g < c.

### Wave impedances

    η_TE = η′ / √(1 − (f_c/f)²)      (> η′, rises toward ∞ at cutoff)
    η_TM = η′ √(1 − (f_c/f)²)        (< η′, falls to 0 at cutoff)

### Dominant mode

Lowest cutoff mode = **TE₁₀** (for a > b), with

    f_c10 = u′/(2a)      λ_c = 2a

TM modes require both m ≥ 1 and n ≥ 1 (either index zero gives an all-zero
field), so the lowest TM mode is **TM₁₁** — much higher.

**TE₁₀ fields:**

    E_y = −(ωμa/π) H₀ sin(πx/a) sin(ωt − βz)
    H_x = (βa/π) H₀ sin(πx/a) sin(ωt − βz)
    H_z = H₀ cos(πx/a) cos(ωt − βz)

E is vertical, maximum at the centre of the broad wall, zero at the side walls.
This is why a probe feeding a waveguide is placed at the centre of the broad wall.

**Single-mode bandwidth.** With b = a/2 (the standard choice), the next modes are
TE₂₀ at 2f_c10 and TE₀₁ at 2f_c10. So the usable single-mode band is
f_c10 to 2f_c10 — an octave. In practice guides are used over roughly
1.25 f_c to 1.9 f_c to stay clear of cutoff dispersion and higher modes.

Standard example: **WR-90** (X-band), a = 22.86 mm, b = 10.16 mm,
f_c10 = 6.557 GHz, rated band **8.2–12.4 GHz**.

### Power and attenuation

Power transmitted in TE₁₀:

    P_avg = (a b E₀²) / (4 η_TE)      … E₀ the peak field at the guide centre

Attenuation has two sources: dielectric loss (usually air, negligible) and wall
loss α_c, which rises near cutoff and again slowly at high f, giving a minimum
in the middle of the band.

## 9.4 Circular waveguide (brief)

Solutions involve Bessel functions J_n. Cutoff is set by the roots:

- TE modes: p′_nm, the roots of J′_n(x) = 0. Dominant **TE₁₁**, p′₁₁ = 1.841.
- TM modes: p_nm, roots of J_n(x) = 0. Lowest **TM₀₁**, p₀₁ = 2.405.

    f_c = p / (2πa√(με))

TE₀₁ is notable: its wall loss *decreases* with frequency, once proposed for
long-haul waveguide communication (overtaken by optical fibre).

## 9.5 Cavity resonators

Short both ends of a length d of rectangular guide. Standing waves in all three
dimensions. Resonant frequency:

    f_r = (u′/2) √( (m/a)² + (n/b)² + (p/d)² )

Dominant mode TE₁₀₁ (for a > b < d). Cavities replace LC tank circuits at
microwave frequencies, where a lumped inductor's own capacitance would dominate.

**Quality factor:**

    Q = 2π (energy stored) / (energy lost per cycle) = ω W / P_loss

Cavity Q values reach 10⁴–10⁵ (a lumped LC circuit manages a few hundred).
For TE₁₀₁ in a copper cavity:

    Q = (a²+d²)abd / [ δ ( 2b(a³+d³) + ad(a²+d²) ) ]

with δ the skin depth. Note Q scales roughly as volume/(surface × δ) — bigger
cavity, higher Q; superconducting cavities reach 10¹⁰.

Uses: microwave oven cavity, klystron, filters, frequency standards, particle
accelerator cells.

## 9.6 Worked examples

**Example 1.** An air-filled rectangular guide has a = 2.286 cm, b = 1.016 cm.
Find the cutoff frequencies of the first four modes.

f_c(mn) = 15 √((m/2.286)² + (n/1.016)²) GHz  (with dimensions in cm, u′=3e10 cm/s)

- TE₁₀: 15/2.286 = **6.56 GHz**
- TE₂₀: 30/2.286 = **13.12 GHz**
- TE₀₁: 15/1.016 = **14.76 GHz**
- TE₁₁ / TM₁₁: 15√(0.1913 + 0.9688) = 15√1.16 = 15(1.077) = **16.16 GHz**

Single-mode band: 6.56 to 13.12 GHz; the practical rating is 8.2–12.4 GHz.

**Example 2.** Operating that guide at 10 GHz in TE₁₀, find λ_g, u_p, u_g, η_TE.

f_c/f = 6.56/10 = 0.656; √(1 − 0.430) = √0.570 = 0.755
λ′ = 3 cm
λ_g = 3/0.755 = **3.97 cm**
u_p = 3×10⁸/0.755 = **3.97×10⁸ m/s**
u_g = 3×10⁸ × 0.755 = **2.27×10⁸ m/s**  (check: u_p u_g = 9.01×10¹⁶ ≈ c² ✓)
η_TE = 377/0.755 = **499 Ω**

**Example 3.** Same guide at 5 GHz. What happens?

5 GHz < 6.56 GHz ⇒ below cutoff. β = jα with
α = (2π/λ′)√((f_c/f)² − 1) — the field decays exponentially, no propagation.
α = (2π×5×10⁹/3×10⁸)√((1.312)² − 1) = 104.7 × 0.850 = 89 Np/m ≈ 773 dB/m.
Effectively total blockage within a few centimetres. (This is exactly how the
mesh in a microwave oven door works: the holes are far below cutoff at 2.45 GHz,
so microwaves cannot get out, while visible light — 10⁵ times higher in
frequency — passes freely.)

**Example 4.** A cavity 5×4×10 cm, air-filled. Find f for TE₁₀₁.

f = 15 √((1/5)² + 0 + (1/10)²) GHz = 15 √(0.04 + 0.01) = 15(0.2236)
  = **3.35 GHz**

## 9.7 Exercises

1. A guide with a = 4 cm, b = 2 cm is filled with ε_r = 2.25. Find f_c for TE₁₀
   and the single-mode band.
2. Show that TE₀₀, TM₁₀ and TM₀₁ modes cannot exist.
3. At what frequency is η_TE = 600 Ω in an air guide with f_c = 6.56 GHz?
4. Find the dominant-mode cutoff of a circular guide with a = 2 cm.
5. Explain, using cutoff, why you cannot send 1 GHz down a 1 cm × 0.5 cm guide.

## Takeaways

- Waveguide = high-pass filter; below f_c the field is evanescent, not attenuated
  by loss but by geometry.
- TE₁₀ is the dominant rectangular mode: f_c = u′/2a, λ_c = 2a.
- u_p > c and u_g < c, with u_p u_g = u′². Only u_g carries information.
- Cavity = shorted guide section; Q is orders of magnitude above lumped LC.
