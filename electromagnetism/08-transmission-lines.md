# Module 08 — Transmission Lines

Where field theory hands the results back to circuit theory.

## 8.1 When does a wire stop being a wire?

Circuit theory assumes signals appear everywhere in the circuit simultaneously.
That is valid when the physical length ℓ ≪ λ. Rule of thumb: if ℓ > λ/10, you
must treat the connection as a transmission line.

At 50 Hz, λ = 6000 km — the wiring in your house is a lumped circuit.
At 3 GHz, λ = 10 cm — a 2 cm PCB trace is a transmission line.

## 8.2 The distributed model

A line is modelled per unit length by four parameters:

- R [Ω/m] — conductor loss (both conductors)
- L [H/m] — series inductance
- G [S/m] — dielectric leakage
- C [F/m] — shunt capacitance

**Universal identities** (any TEM line, any cross-section):

    LC = με        and        G/C = σ/ε

| Line | L (H/m) | C (F/m) | R (Ω/m) |
|---|---|---|---|
| Coax (a,b) | (μ/2π)ln(b/a) | 2πε/ln(b/a) | (R_s/2π)(1/a + 1/b) |
| Two-wire (a, d) | (μ/π)cosh⁻¹(d/2a) | πε/cosh⁻¹(d/2a) | R_s/(πa) |
| Parallel plate (w, d) | μd/w | εw/d | 2R_s/w |

## 8.3 Telegrapher's equations and their solution

    ∂V/∂z = −(R + jωL) I
    ∂I/∂z = −(G + jωC) V

Combine:  d²V/dz² = γ²V, with

    γ = α + jβ = √((R + jωL)(G + jωC))

    Z₀ = √( (R + jωL) / (G + jωC) )      characteristic impedance [Ω]

Solution: V(z) = V₀⁺e^{−γz} + V₀⁻e^{+γz}, and I(z) = (V₀⁺e^{−γz} − V₀⁻e^{+γz})/Z₀.
Forward wave and backward wave — note the **minus sign** on the reflected current.

### Lossless line (R = G = 0) — the case you will use 90% of the time

    α = 0,   β = ω√(LC),   Z₀ = √(L/C)  (real)
    u = 1/√(LC) = 1/√(με),   λ = 2π/β = u/f

**Z₀ is not a resistance you can measure with an ohmmeter.** It is the ratio V/I
of a *single travelling wave*. An infinitely long line — or a finite line
terminated in Z₀ — draws current as if it were a Z₀ resistor, because no wave
ever comes back.

Typical values: 50 Ω (RF/instrumentation), 75 Ω (video/TV), 300 Ω (twin-lead
antenna feed), 100 Ω differential (Ethernet).

### Distortionless line
If RC = GL then α = √(RG) and β = ω√(LC): attenuation and velocity become
frequency-independent, so a pulse keeps its shape. Z₀ = √(R/G), real.
(Heaviside's insight — historically, adding series inductance "loading coils" to
telephone lines to satisfy this condition made long-distance telephony work.)

## 8.4 Reflection, SWR, and input impedance

At a load Z_L at z = 0, with the line of impedance Z₀:

    Γ_L = (Z_L − Z₀)/(Z_L + Z₀)
    s = SWR = (1 + |Γ|)/(1 − |Γ|)
    |Γ| = (s − 1)/(s + 1)

Return loss = −20 log₁₀|Γ| dB.

Reflection coefficient at distance ℓ from the load: Γ(ℓ) = Γ_L e^{−2γℓ},
which for a lossless line is just Γ_L e^{−j2βℓ} — same magnitude, rotating phase.

### Input impedance — the master formula

    Z_in(ℓ) = Z₀ · (Z_L + jZ₀ tan βℓ) / (Z₀ + jZ_L tan βℓ)     [lossless]

Lossy version: replace jtan βℓ with tanh γℓ.

### Special lengths — memorize these

| Length | Result | Use |
|---|---|---|
| ℓ = λ/2 | Z_in = Z_L | "half-wave repeater"; insert without effect |
| ℓ = λ/4 | Z_in = Z₀²/Z_L | **quarter-wave transformer** — impedance matching |
| Z_L = 0, ℓ = λ/4 | Z_in = ∞ | shorted stub acts as an open |
| Z_L = ∞, ℓ = λ/4 | Z_in = 0 | open stub acts as a short |
| Z_L = 0, ℓ < λ/4 | Z_in = jZ₀tan βℓ (inductive) | shorted stub as a variable L |
| Z_L = ∞, ℓ < λ/4 | Z_in = −jZ₀cot βℓ (capacitive) | open stub as a variable C |
| Z_L = Z₀ | Z_in = Z₀ for any ℓ | matched — no reflection ever |

**Quarter-wave transformer.** To match a 100 Ω load to a 50 Ω line, insert a
λ/4 section of Z₀′ = √(50 × 100) = 70.7 Ω. Narrowband (works at one frequency and
its odd multiples) but trivially simple.

### Power

    P_avg = |V₀⁺|²(1 − |Γ|²) / (2Z₀)

Maximum power reaches the load when Γ = 0. Every reflection is wasted power and,
in high-power systems, a source of arcing at the voltage maxima.

## 8.5 The Smith chart

A conformal map of the reflection coefficient plane, with constant-r and
constant-x circles of normalized impedance z = Z/Z₀ overlaid. It converts the
messy Z_in formula into "rotate on a circle".

Rules for using it:
1. Normalize: z_L = Z_L/Z₀. Plot it.
2. Centre = matched point (z = 1, Γ = 0). Outer rim = |Γ| = 1 (pure reactance).
3. Radius of the circle through your point is |Γ|; that circle is the **constant
   SWR circle**, and the SWR reads off where it crosses the positive real axis.
4. **Toward the generator = clockwise.** One full revolution = λ/2 (not λ —
   because Γ rotates as e^{−j2βℓ}, twice the electrical angle).
5. Admittance from impedance: rotate 180° (i.e. y = 1/z is the diametrically
   opposite point). Essential for shunt-stub matching.
6. Real axis right of centre = voltage maximum (z real > 1); left of centre =
   voltage minimum.

**Single-stub matching procedure:**
1. Plot z_L, convert to y_L (rotate 180°).
2. Move clockwise (toward generator) along the constant-|Γ| circle to where it
   crosses the g = 1 circle. That distance is d, the stub position.
3. The remaining susceptance there is ±jb. Add a stub whose input susceptance is
   ∓jb to cancel it.
4. Read the stub length off the rim (from the short-circuit point y=∞ for a
   shorted stub, or y=0 for an open stub).

## 8.6 Transients on lines (step response)

Close a switch connecting source V_g with internal R_g to a line of Z₀ and load
Z_L. The line does *not* know about Z_L yet.

1. At t=0 a step of amplitude V₁ = V_g Z₀/(Z₀+R_g) launches down the line.
2. At t = T = ℓ/u it hits the load, reflecting Γ_L V₁.
3. That returns at t = 2T, reflects Γ_g times, and so on.
4. Steady state = the DC answer V_g Z_L/(Z_L + R_g), approached geometrically.

The **bounce diagram** (a zigzag of position vs time) organizes the bookkeeping.
This is exactly how you diagnose signal-integrity ringing on a PCB, and how time-
domain reflectometry (TDR) locates a cable fault: measure the round-trip time of
the reflection, multiply by u/2.

## 8.7 Worked examples

**Example 1.** A lossless 50 Ω line, ε_r = 2.25, operates at 100 MHz with
Z_L = 100 + j50 Ω. Find Γ_L, SWR, and Z_in at 0.3λ from the load.

Γ_L = (100+j50−50)/(100+j50+50) = (50+j50)/(150+j50)
    = (70.71∠45°)/(158.1∠18.43°) = **0.447∠26.57°**
s = (1+0.447)/(1−0.447) = **2.62**

βℓ = 2π(0.3) = 1.885 rad = 108°; tan(108°) = −3.078
Z_in = 50 · (100+j50 + j50(−3.078)) / (50 + j(100+j50)(−3.078))
     = 50 · (100 + j50 − j153.9) / (50 − j307.8 + 153.9)
     = 50 · (100 − j103.9)/(203.9 − j307.8)
     = 50 · (144.2∠−46.1°)/(369.2∠−56.5°)
     = 50 × 0.3906∠10.4° = **19.5∠10.4° Ω ≈ 19.2 + j3.5 Ω**

Also: u = c/√2.25 = 2×10⁸ m/s, λ = 2 m, so 0.3λ = 60 cm.

**Example 2.** Match a 200 Ω antenna to a 50 Ω line at 300 MHz using a
quarter-wave transformer in a medium with ε_r = 1.

Z₀′ = √(50 × 200) = **100 Ω**
λ = c/f = 1 m ⇒ section length = **25 cm**

**Example 3.** A 75 Ω line is terminated in 300 Ω. Find SWR and return loss.

Γ = (300−75)/(300+75) = 0.6; s = 1.6/0.4 = **4.0**
Return loss = −20log(0.6) = **4.44 dB** (poor — 36% of power bounces back).

**Example 4 (TDR).** A pulse on a cable (u = 2×10⁸ m/s) returns after 1.2 μs
with the same polarity. Where and what is the fault?

Distance = u·t/2 = 2×10⁸ × 1.2×10⁻⁶ / 2 = **120 m**.
Same polarity ⇒ Γ > 0 ⇒ Z_L > Z₀ ⇒ an **open circuit / break**.
(Inverted polarity would mean a short.)

## 8.8 Exercises

1. A coax has a = 0.6 mm, b = 3.5 mm, ε_r = 2.3. Find L, C, Z₀, u, and λ at 1 GHz.
2. A lossless 100 Ω line is terminated in 50 − j75 Ω. Find Γ, SWR, and the
   distance from the load to the first voltage minimum.
3. Design a single shorted stub match for Z_L = 60 + j80 Ω on a 50 Ω line.
   Give the stub position and length in wavelengths.
4. A 50 Ω line of length λ/8 is shorted. Find Z_in. (j50 Ω — a pure inductance.)
5. A generator (12 V, R_g = 25 Ω) drives a 50 Ω line 100 m long (u = 2×10⁸ m/s)
   terminated in 150 Ω. Draw the bounce diagram and find V at the load at
   t = 0.5 μs, 1.5 μs, and t → ∞.

## Takeaways

- Long compared with λ ⇒ transmission line, not wire.
- Z₀ = √(L/C) is a wave property; termination in Z₀ makes reflections vanish.
- Z_in rotates with distance, repeating every λ/2; λ/4 inverts it.
- The Smith chart is that rotation drawn as a picture; clockwise = toward source.
- Γ, SWR, and matching here are the same physics as Module 07's boundary,
  with Z₀ playing the role of η.
