# Week 14 — Field-Effect Transistors (MOSFETs)
<!-- group: Module 5 · Advanced Device Technology -->

**Plan:** ideal MOS capacitor physics (accumulation, depletion, inversion); MOSFET threshold voltage; linear and saturation operating regions.

The MOSFET is the device in every digital IC. It uses the Si/SiO₂ interface (Week 1), band bending (Weeks 10–11) and drift in a surface channel (Week 7).

## The ideal MOS capacitor

A metal (or heavily doped polysilicon) **gate**, a thin **SiO₂** insulator of thickness t_ox, and a **p-type** silicon substrate (doping N_A). "Ideal" means: no oxide charge, no interface traps, zero metal–semiconductor work-function difference (Φ_ms = 0), and an oxide that conducts no current.

The oxide capacitance per unit area:

    C_ox = ε_ox / t_ox,      ε_ox = 3.9ε₀ = 3.45×10⁻¹³ F/cm

The **bulk Fermi potential** of the substrate:

    φ_F = (kT/q) ln(N_A/n_i)

@fig figures/mos-states.svg | Band diagrams of an ideal MOS capacitor on p-type silicon. Accumulation: bands bend up and holes collect at the surface. Depletion: bands bend down and holes are pushed away. Inversion: the surface becomes n-type once the band bending reaches 2qφ_F.

### Accumulation (V_G < 0)

A negative gate attracts **holes** to the surface. The bands bend **upward** at the surface, E_F moves closer to E_v there, and a thin hole accumulation layer forms. The capacitance is just the oxide: C = C_ox.

### Depletion (0 < V_G < V_T)

A positive gate repels holes, leaving a layer of negative acceptor ions of width W_d. The bands bend **downward** by the surface potential φ_s. The depletion capacitance C_d = ε_s/W_d is in series with C_ox, so C falls as V_G rises:

    W_d = √(2ε_sφ_s / qN_A),     1/C = 1/C_ox + W_d/ε_s

### Inversion (V_G > V_T)

As V_G increases further, the surface bends so far that E_i drops below E_F at the surface: the surface now has more electrons than holes and is **inverted** to n-type. **Strong inversion** is defined as the point where the surface is as n-type as the bulk is p-type:

    φ_s = 2φ_F

Beyond this the depletion width stops growing, at its maximum:

    W_dmax = √(4ε_sφ_F / qN_A),     Q_dmax = −qN_AW_dmax

Extra gate charge is balanced by electrons in the inversion layer, a sheet of charge Q_n = −C_ox(V_G − V_T). This layer is the MOSFET channel.

### C-V curve

| Region | Low frequency | High frequency (1 MHz) |
|---|---|---|
| Accumulation | C_ox | C_ox |
| Depletion | Falls | Falls |
| Inversion | Rises back to C_ox (inversion electrons follow the AC signal) | Stays at minimum C_min = C_ox C_dmin/(C_ox + C_dmin) |

High- and low-frequency C-V curves give t_ox, N_A, V_FB, V_T and the interface-trap density (Week 12).

## Threshold voltage

The gate voltage that brings the surface to strong inversion:

    V_T = V_FB + 2φ_F + |Q_dmax| / C_ox = V_FB + 2φ_F + √(2qε_sN_A · 2φ_F) / C_ox

with the flat-band voltage (non-ideal MOS)

    V_FB = Φ_ms − Q_f / C_ox

Φ_ms is the gate–substrate work-function difference and Q_f the fixed oxide charge. V_T rises with substrate doping and oxide thickness. It is adjusted in manufacture by ion implantation into the channel (threshold-adjust implant, Week 3).

**Body effect.** With a source-to-body voltage V_SB, the depletion charge grows:

    V_T = V_T0 + γ_b ( √(2φ_F + V_SB) − √(2φ_F) ),     γ_b = √(2qε_sN_A) / C_ox

## The MOSFET

An n-channel enhancement MOSFET adds n⁺ **source** and **drain** regions on either side of the gate, on a p-type body, with channel length L and width W. With V_GS < V_T there is no channel and no current (two back-to-back p-n junctions). With V_GS > V_T an inversion channel connects source and drain.

### Linear (triode) region: V_DS < V_GS − V_T

Gradual-channel approximation: at a point y along the channel the inversion charge is Q_n(y) = −C_ox(V_GS − V_T − V(y)). The drift current I_D = W μ_n |Q_n| dV/dy, integrated from source (V = 0) to drain (V = V_DS):

    I_D = μ_nC_ox (W/L) [ (V_GS − V_T)V_DS − V_DS²/2 ]

For small V_DS the channel is a voltage-controlled resistor: I_D ≈ μ_nC_ox(W/L)(V_GS − V_T)V_DS.

### Saturation region: V_DS ≥ V_GS − V_T

When V_DS = V_GS − V_T the inversion charge at the drain end falls to zero: the channel is **pinched off**. Further V_DS drops across the short pinched-off region, and the current stays nearly constant:

    I_D(sat) = (μ_nC_ox/2)(W/L)(V_GS − V_T)²,     V_DS(sat) = V_GS − V_T

With **channel-length modulation**, I_D = I_D(sat)(1 + λV_DS).

### Transconductance

    g_m = ∂I_D/∂V_GS = μ_nC_ox (W/L)(V_GS − V_T)     (saturation)
    g_m = μ_nC_ox (W/L) V_DS                          (linear)

@fig figures/mosfet-iv.svg | Output characteristics of an n-channel MOSFET. The dashed curve V_DS = V_GS − V_T separates the linear region from saturation.

### Short-channel effects

As L shrinks below about 1 μm: velocity saturation makes I_D ∝ (V_GS − V_T) instead of the square (Week 8); V_T falls with L and with V_DS (drain-induced barrier lowering); hot carriers degrade the oxide (Week 8); subthreshold leakage grows. These shape modern CMOS design.

## Worked example

n-channel MOSFET: p-Si body N_A = 10¹⁷ cm⁻³, t_ox = 10 nm, n⁺-polysilicon gate, no oxide charge, channel mobility μ_n = 400 cm²/V·s, W/L = 10.

    φ_F = 0.0259 ln(10¹⁷/10¹⁰) = 0.417 V
    C_ox = 3.45×10⁻¹³ / 10⁻⁶ = 3.45×10⁻⁷ F/cm²
    W_dmax = √(4 × 1.04×10⁻¹² × 0.417 / (1.6×10⁻¹⁹ × 10¹⁷)) = 1.04×10⁻⁵ cm = 0.104 μm
    |Q_dmax| = qN_AW_dmax = 1.6×10⁻¹⁹ × 10¹⁷ × 1.04×10⁻⁵ = 1.66×10⁻⁷ C/cm²

n⁺ poly gate on p-Si: Φ_ms ≈ −(E_g/2 + φ_F) = −(0.56 + 0.417) = −0.98 V, so V_FB = −0.98 V.

    V_T = −0.98 + 2(0.417) + 1.66×10⁻⁷/3.45×10⁻⁷ = −0.98 + 0.834 + 0.482 = 0.34 V

At V_GS = 1.5 V (V_GS − V_T = 1.16 V), with k = μ_nC_ox(W/L) = 400 × 3.45×10⁻⁷ × 10 = 1.38×10⁻³ A/V²:

    Linear, V_DS = 0.1 V:  I_D = 1.38×10⁻³ × (1.16 × 0.1 − 0.005) = 0.153 mA
    Saturation:            I_D = ½ × 1.38×10⁻³ × 1.16² = 0.93 mA,   V_DS(sat) = 1.16 V
    g_m(sat) = 1.38×10⁻³ × 1.16 = 1.6 mS

---

## Practice questions solved

### P1. Explain accumulation, depletion and inversion in an ideal MOS capacitor on p-type silicon.

**Accumulation** (V_G < V_FB = 0 for the ideal case): the negative gate charge attracts majority holes to the oxide interface. The bands bend upward at the surface, the hole density there exceeds N_A, and the capacitance equals C_ox. **Depletion** (0 < V_G < V_T): the positive gate charge repels holes, exposing a region of width W_d of negative acceptor ions. The bands bend downward by the surface potential φ_s < 2φ_F, and the depletion capacitance in series with C_ox lowers the total capacitance. **Inversion** (V_G > V_T): the downward bending makes E_i cross below E_F at the surface, so electrons (minority carriers in the bulk) become the majority at the surface. At φ_s = 2φ_F the surface electron density equals the bulk hole density (strong inversion); the depletion width saturates at W_dmax and further gate charge is balanced by the electron inversion layer, the channel of a MOSFET.

### P2. Derive the expression for the threshold voltage of an n-channel MOSFET.

At threshold the surface potential is φ_s = 2φ_F and the depletion region has its maximum width W_dmax = √(2ε_s(2φ_F)/qN_A), holding charge Q_dmax = −qN_AW_dmax = −√(2qε_sN_A(2φ_F)). The inversion charge is still negligible. The gate voltage divides between the oxide and the silicon: V_G = V_FB + V_ox + φ_s. The oxide voltage is the charge it must support divided by its capacitance, V_ox = |Q_dmax|/C_ox. Therefore:

    V_T = V_FB + 2φ_F + √(2qε_sN_A(2φ_F)) / C_ox,     V_FB = Φ_ms − Q_f/C_ox

### P3. Distinguish between the linear and saturation regions of a MOSFET.

| | Linear (triode) | Saturation |
|---|---|---|
| Condition | V_GS > V_T, V_DS < V_GS − V_T | V_GS > V_T, V_DS ≥ V_GS − V_T |
| Channel | Continuous from source to drain | Pinched off near the drain |
| I_D | μ_nC_ox(W/L)[(V_GS − V_T)V_DS − V_DS²/2] | (μ_nC_ox/2)(W/L)(V_GS − V_T)² |
| Dependence on V_DS | Strong (≈ linear for small V_DS) | Weak (channel-length modulation only) |
| Behaviour | Voltage-controlled resistor | Voltage-controlled current source |
| Use | Switch ON state, analogue resistor | Amplifier |

### P4. How are threshold voltage and channel mobility extracted from measurements?

Measure I_D against V_GS at a small V_DS (say 0.1 V) in the linear region. The curve is a straight line whose slope is the transconductance g_m = μ_nC_ox(W/L)V_DS, giving **μ_n = g_m L/(W C_ox V_DS)**. Extrapolating the line to I_D = 0 gives V_GS = V_T + V_DS/2, giving **V_T**. Alternatively plot √I_D against V_GS in saturation: the slope is √(μ_nC_oxW/2L) and the intercept is V_T. C_ox is found from the accumulation capacitance of a MOS capacitor (Week 12). See Laboratory Practical 4.
