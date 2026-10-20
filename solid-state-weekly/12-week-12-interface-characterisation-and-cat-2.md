# Week 12 — Interface Characterisation and CAT 2
<!-- group: Module 4 · Junctions, Interfaces & Characterisation -->

**Plan:** methods of characterisation (capacitance–voltage C-V profiling, current–voltage I-V analysis); Continuous Assessment Test 2.

## I-V characterisation

**Set-up.** A source-measure unit (SMU) or semiconductor parameter analyser applies a stepped voltage and measures current (pA to A), usually on a probe station, often at several temperatures.

**What is extracted from a diode:**

Plot ln I against V (semi-log). For the ideal or near-ideal diode

    I = I_s [ exp(qV/ηkT) − 1 ]  ⇒  ln I ≈ ln I_s + qV/(ηkT)

- **Saturation current I_s:** the intercept at V = 0 of the straight-line region.
- **Ideality factor η:** from the slope, η = (q/kT) / (d ln I/dV). η ≈ 1 means diffusion current; η ≈ 2 means depletion-region recombination dominates.
- **Series resistance R_s:** from the bending at high current, where V = V_j + IR_s.
- **Reverse leakage and breakdown voltage V_BR** from the reverse characteristic.
- **Schottky barrier height** from I_s: Φ_B = (kT/q) ln(A∗∗T²/J_s). With temperature-dependent data, an **Arrhenius plot** of ln(J_s/T²) versus 1/T has slope −qΦ_B/k.
- **Ohmic contact check:** the I-V of two contacts should be linear and symmetric. Contact resistance is extracted by the transmission-line method (TLM).

**Other I-V tests:** MOSFET output (I_D–V_DS) and transfer (I_D–V_GS) curves give threshold voltage, transconductance and mobility; BJT Gummel plots give current gain; four-point probe gives sheet resistance; Hall measurements give carrier type, density and mobility.

## C-V characterisation

**Set-up.** A small AC voltage (10–50 mV, 10 kHz – 1 MHz) is superimposed on a DC bias V, and an LCR meter measures the small-signal capacitance C = dQ/dV as the DC bias is swept, usually in reverse.

**Theory.** A reverse-biased junction (p⁺n or Schottky) behaves as a parallel-plate capacitor whose plate separation is the depletion width:

    C = ε_s A / W,     W = √( 2ε_s (V_bi − V) / qN )

so

    C = A √( qε_s N / 2(V_bi − V) )

Squaring and inverting:

    1/C² = 2(V_bi − V) / (q ε_s N A²)

For uniform doping, **1/C² is a straight line against V**:

- **Slope:** d(1/C²)/dV = −2/(qε_s N A²), so

    N = 2 / ( q ε_s A² · |d(1/C²)/dV| )

- **Intercept on the voltage axis** (1/C² = 0) gives V = V_bi. For a Schottky diode, Φ_B = V_bi + (kT/q) ln(N_c/N_D) + kT/q.

@fig figures/cv.svg | Mott–Schottky plot. For uniform doping 1/C² falls on a straight line; the slope gives the doping, the voltage-axis intercept gives the built-in potential.

**Non-uniform doping: profiling.** If N varies with depth, the local slope gives the doping at the edge of the depletion region, and the capacitance gives where that edge is:

    N(W) = 2 / ( q ε_s A² · d(1/C²)/dV ) = −C³ / ( q ε_s A² · dC/dV ),     W = ε_s A / C

Sweeping the reverse bias moves W deeper and maps out the **doping profile** N(x). This works for one-sided junctions (p⁺n, n⁺p) or Schottky diodes, where the depletion region lies in one side only.

**Worked example.** A Si Schottky diode of area A = 1×10⁻³ cm² gives a straight 1/C² plot with slope −1.2×10²¹ F⁻²V⁻¹ and voltage intercept 0.60 V. Then:

    N_D = 2 / (1.602×10⁻¹⁹ × 1.036×10⁻¹² × (10⁻³)² × 1.2×10²¹)
        = 2 / (1.99×10⁻¹⁶) = 1.0×10¹⁶ cm⁻³

    V_bi = 0.60 V

    At V = −5 V:  C = A√(qε_sN_D/2(V_bi − V)) = 10⁻³ √(1.66×10⁻¹⁵/11.2) = 12.2 pF
                  W = ε_sA/C = 1.036×10⁻¹⁵/12.2×10⁻¹² = 0.85 μm

**MOS C-V.** On a MOS capacitor, C-V curves (accumulation, depletion, inversion) give the oxide thickness (C_ox = ε_oxA/t_ox), flat-band and threshold voltages, substrate doping, fixed oxide charge, mobile ions (bias–temperature stress shifts) and interface-trap density D_it (from high- and low-frequency curves). This is the main tool for monitoring gate-oxide quality and stability.

**Precautions.** Use reverse bias (forward bias adds diffusion capacitance and conductance); subtract stray and pad capacitance; choose frequency so traps do not respond (or do, deliberately); include series resistance correction; keep the AC signal small; Debye-length limits resolution near abrupt doping steps.

---

## Examination question solved (Q50)

### Q50. Explain the principles of I-V and C-V characterisation of semiconductor devices and describe how C-V measurements can be used to estimate doping concentration.

**I-V characterisation: principle.** A known DC voltage is applied across the device (swept in steps from reverse to forward bias) and the resulting current is measured with a source-measure unit, usually on a probe station and sometimes at several temperatures. Comparing the measured curve with device theory gives the transport parameters.

For a diode, I = I_s[exp(qV/ηkT) − 1]. From a semi-log plot of ln I versus V:

- the intercept gives the **saturation current I_s** (and, for Schottky diodes, the **barrier height** Φ_B = (kT/q) ln(AA∗∗T²/I_s));
- the slope gives the **ideality factor** η (1 for ideal diffusion current, approaching 2 when depletion-region recombination dominates);
- deviation at high current gives the **series resistance**;
- the reverse branch gives **leakage current** and **breakdown voltage**;
- for contacts, a linear symmetric I-V confirms an **Ohmic** contact and gives contact resistance.

I-V curves of transistors give threshold voltage, transconductance, output resistance, mobility and current gain, and repeated I-V measurement after stress is used to test **stability and reliability**.

**C-V characterisation: principle.** A reverse-biased p-n junction or Schottky barrier has a depletion region free of carriers between two conducting regions; it behaves like a parallel-plate capacitor with dielectric ε_s and plate separation W:

    C = ε_s A / W

The DC reverse bias is swept, and the small-signal capacitance is measured with a small AC voltage (typically 1 MHz, a few tens of mV) using an LCR meter. Since W increases with reverse bias, C decreases.

**Using C-V to estimate doping.** For a one-sided abrupt junction (p⁺n or Schottky on n-type) with uniform doping N:

    W = √( 2ε_s(V_bi − V)/qN )   ⇒   C = A √( qε_sN / 2(V_bi − V) )

Rearranging:

    1/C² = 2(V_bi − V) / (qε_s N A²)

1. Measure C at a series of reverse biases V.
2. Plot **1/C² against V** (the Mott–Schottky plot). For uniform doping it is a **straight line**.
3. The **slope** is −2/(qε_sNA²), so the doping concentration is **N = 2/(qε_sA²·|slope|)**.
4. The **intercept** on the V axis gives the built-in potential V_bi (and from it the Schottky barrier height).
5. **For non-uniform doping**, use the local slope: N(W) = 2/(qε_sA² d(1/C²)/dV) evaluated at each bias, and the depth W = ε_sA/C. This gives the doping profile N(x) as a function of depth.

**Example.** A diode of area 10⁻³ cm² on Si (ε_s = 1.036×10⁻¹² F/cm) gives a 1/C² slope magnitude of 1.2×10²¹ F⁻²V⁻¹:

    N = 2 / (1.602×10⁻¹⁹ × 1.036×10⁻¹² × 10⁻⁶ × 1.2×10²¹) = 1.0×10¹⁶ cm⁻³

**Advantages and limits.** C-V is non-destructive, fast and needs only a simple diode, but only measures the doping on the lightly doped side, only to depths reachable before breakdown, and with resolution limited by the Debye length. Accuracy requires a correct area, correction for stray capacitance and series resistance, and a frequency at which deep traps do not respond.

---

## CAT 2 practice test (60 minutes)

Covers Weeks 7–12. Practice questions, not the actual CAT. Use q = 1.6×10⁻¹⁹ C, kT/q = 0.0259 V, Si: n_i = 1×10¹⁰ cm⁻³, ε_s = 1.04×10⁻¹² F/cm.

1. An n-type Si bar (N_D = 10¹⁶ cm⁻³, μ_n = 1200 cm²/V·s) is 1 cm long with 10⁻³ cm² cross-section. Find its resistance and the current at 5 V.
2. Find the hole diffusion coefficient in Si if μ_p = 450 cm²/V·s, and the diffusion length if τ_p = 2 μs.
3. Holes injected into n-Si fall from 10¹⁴ cm⁻³ at x = 0 with L_p = 30 μm. Find the hole diffusion current density at x = 0 (D_p = 11.6 cm²/s).
4. A Si p⁺n junction has N_D = 5×10¹⁵ cm⁻³ and N_A = 10¹⁸ cm⁻³. Find V_bi, the depletion width at zero bias and at −10 V, and the peak field at −10 V.
5. The diode of Q4 has area 10⁻³ cm² and I_s = 1×10⁻¹⁴ A. Find the current at 0.6 V and the voltage for 1 mA.
6. A Schottky diode on n-Si has Φ_B = 0.7 eV. Find J_s at 300 K (A∗∗ = 110 A/cm²K²) and the forward voltage for J = 10 A/cm².
7. A 1/C² plot for a one-sided junction of area 2×10⁻³ cm² has slope magnitude 4.0×10²⁰ F⁻²V⁻¹. Find the doping.

## CAT 2 solutions

### 1. Resistance of a bar

    σ = qN_Dμ_n = 1.6×10⁻¹⁹ × 10¹⁶ × 1200 = 1.92 S/cm,   ρ = 0.521 Ω·cm
    R = ρL/A = 0.521 × 1 / 10⁻³ = 521 Ω
    I = V/R = 5/521 = 9.6 mA

### 2. Einstein relation and diffusion length

    D_p = (kT/q)μ_p = 0.0259 × 450 = 11.7 cm²/s
    L_p = √(D_pτ_p) = √(11.7 × 2×10⁻⁶) = 4.83×10⁻³ cm = 48 μm

### 3. Diffusion current at the injection point

Δp(x) = Δp(0)e^{−x/L_p}, so dp/dx at x = 0 is −Δp(0)/L_p.

    J_p = −qD_p dp/dx = qD_pΔp(0)/L_p = 1.6×10⁻¹⁹ × 11.6 × 10¹⁴ / 3×10⁻³
        = 0.062 A/cm²

### 4. Junction parameters

    V_bi = 0.0259 ln(10¹⁸ × 5×10¹⁵ / 10²⁰) = 0.0259 ln(5×10¹³) = 0.0259 × 31.54 = 0.817 V

One-sided (N_A ≫ N_D): W = √(2ε_s(V_bi − V)/qN_D).

    V = 0:    W = √(2 × 1.04×10⁻¹² × 0.817 / (1.6×10⁻¹⁹ × 5×10¹⁵)) = √(2.12×10⁻⁹) = 4.6×10⁻⁵ cm = 0.46 μm
    V = −10:  W = √(2 × 1.04×10⁻¹² × 10.817 / 8×10⁻⁴) = √(2.81×10⁻⁸) = 1.68×10⁻⁴ cm = 1.68 μm
    E_max = 2(V_bi − V)/W = 2 × 10.817 / 1.68×10⁻⁴ = 1.29×10⁵ V/cm

### 5. Diode current

    I(0.6 V) = 10⁻¹⁴ (e^{0.6/0.0259} − 1) = 10⁻¹⁴ × 1.15×10¹⁰ = 0.115 mA
    V(1 mA) = 0.0259 ln(10⁻³/10⁻¹⁴ + 1) = 0.0259 × 25.33 = 0.656 V

### 6. Schottky diode

    J_s = A∗∗T²e^{−qΦ_B/kT} = 110 × 9×10⁴ × e^{−0.7/0.0259} = 9.9×10⁶ × 1.82×10⁻¹² = 1.8×10⁻⁵ A/cm²
    V = 0.0259 ln(10/1.8×10⁻⁵) = 0.0259 × 13.23 = 0.343 V

A p-n diode needs about 0.7 V for a similar current density, which is why Schottky diodes are used where a low forward drop matters.

### 7. Doping from C-V

    N = 2/(qε_sA²|slope|) = 2 / (1.6×10⁻¹⁹ × 1.04×10⁻¹² × (2×10⁻³)² × 4.0×10²⁰)
      = 2 / (2.66×10⁻¹⁶) = 7.5×10¹⁵ cm⁻³
