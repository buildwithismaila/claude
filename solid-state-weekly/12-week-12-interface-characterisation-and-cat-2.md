# Week 12 — Interface Characterisation and CAT 2
<!-- group: Module 4 · Junctions, Interfaces & Characterisation -->

**Plan:** methods of characterisation (capacitance–voltage C-V profiling, current–voltage I-V analysis); Continuous Assessment Test 2.

## The big picture

After a device is made, how do you know what is inside it? You cannot see the doping or the barrier height. But you can **measure electrically** and compare the results with the theory of Weeks 10–11. Two measurements do most of the work:

- **I-V (current against voltage)** tells you **how current flows**: the saturation current, how ideal the junction is, the series resistance, leakage and breakdown, and for a Schottky diode the barrier height.
- **C-V (capacitance against voltage)** tells you **how charge is arranged**: the doping concentration (and how it changes with depth) and the built-in potential.

The trick in both cases is to plot the data so that the theory predicts a **straight line**, then read the answers from the slope and the intercept.

## I-V characterisation

### The measurement

A **source-measure unit** (or a power supply with a series resistor and two meters) applies a voltage to the device in steps, from reverse to forward bias, and records the current at each step. Currents from picoamps to amps may need measuring, often on a probe station, sometimes at several temperatures.

### Turning the curve into a straight line

For a real diode,

    I = I_s ( e^{qV/ηkT} − 1 )

where η (the **ideality factor**) is 1 for a perfect diffusion-current diode and up to 2 when recombination in the depletion region dominates. Above about 0.1 V the −1 is negligible, so take the natural log:

    ln I = ln I_s + (q/ηkT) V

That is a straight line if you plot **ln I against V** (a semi-log plot):

- the **intercept** at V = 0 gives **ln I_s**, so the saturation current I_s;
- the **slope** is q/(ηkT), so **η = (q/kT) / slope**.

**Example.** The current rises from 0.9 μA at 0.30 V to 40 μA at 0.40 V.

    slope = ln(40/0.9)/0.10 = 3.79/0.10 = 37.9 per volt
    η = 1/(0.0259 × 37.9) = 1.02
    I_s = 0.9 μA / e^{37.9 × 0.30} ≈ 1×10⁻¹¹ A

### What else the I-V curve shows

- **Series resistance R_s:** at high current the curve bends away from the straight line, because part of the voltage is dropped across the resistance of the bulk and contacts: V = V_junction + IR_s. R_s = (extra voltage)/I.
- **Reverse leakage and breakdown voltage** from the reverse branch.
- **Schottky barrier height** from I_s: Φ_B = (kT/q) ln(A∗∗AT²/I_s), where A is the diode area. Measuring at several temperatures and plotting ln(I_s/T²) against 1/T (an **Arrhenius plot**) gives a straight line of slope −qΦ_B/k.
- **Ohmic contacts:** the I-V between two contacts should be a straight line through the origin, the same in both directions.

Transistors are characterised the same way: MOSFET I_D–V_GS curves give the threshold voltage and mobility (Week 14, Practical 4), and BJT curves give the current gain.

## C-V characterisation

### The measurement

An **LCR meter** applies a small AC voltage (10–50 mV, typically at 1 MHz) on top of a DC bias, and measures the capacitance. The DC bias is stepped through a range of **reverse** voltages.

### The theory: a capacitor whose plates move

A reverse-biased one-sided junction (p⁺n) or Schottky diode has a depletion region with no mobile carriers, between two conducting regions. It is a **parallel-plate capacitor** whose plate separation is the depletion width W:

    C = ε_s A / W

From Week 10, W = √(2ε_s(V_bi − V)/qN), where N is the doping on the lightly doped side. **As the reverse voltage increases, W gets bigger and C gets smaller.** Substituting:

    C = A √( qε_sN / 2(V_bi − V) )

### Turning it into a straight line: the Mott–Schottky plot

Square both sides and turn upside down:

    1/C² = 2(V_bi − V) / (qε_sNA²)

So if you plot **1/C² against V**, uniform doping gives a **straight line**:

- **Slope** = −2/(qε_sNA²). Therefore

    N = 2 / ( qε_s A² × |slope| )

- **Intercept** on the voltage axis (where 1/C² = 0) is at V = V_bi: the **built-in potential**.

@fig figures/cv.svg | Mott–Schottky plot. For uniform doping the points fall on a straight line; the slope gives the doping and the voltage-axis intercept gives V_bi.

> **In plain words.** Reverse bias pushes the edge of the depletion region deeper into the semiconductor. How much extra charge is uncovered as the edge moves tells you how many dopant atoms are there. The capacitance measures exactly that.

### Worked example

A Si Schottky diode of area A = 1×10⁻³ cm² gives a straight 1/C² plot with slope −1.2×10²¹ F⁻²V⁻¹ and voltage intercept 0.60 V.

    N_D = 2 / (1.602×10⁻¹⁹ × 1.036×10⁻¹² × (10⁻³)² × 1.2×10²¹)
        = 2 / 1.99×10⁻¹⁶ = 1.0×10¹⁶ cm⁻³

    V_bi = 0.60 V

    At V = −5 V:  C = A√(qε_sN_D / 2(V_bi − V)) = 10⁻³ × √(1.66×10⁻¹⁵ / 11.2) = 12.2 pF
                  W = ε_sA/C = 1.036×10⁻¹⁵ / 12.2×10⁻¹² = 0.85 μm

### Doping profiles

If the doping is **not** uniform, the 1/C² plot curves. The local slope at each bias still gives the doping at the edge of the depletion region, and the capacitance tells you where that edge is:

    N(W) = 2 / ( qε_sA² × d(1/C²)/dV ),     W = ε_sA/C

Sweeping the bias moves W deeper and maps out the **doping profile** N(x). This only works for one-sided junctions (p⁺n, n⁺p) or Schottky diodes, where the depletion region is all on one side.

### MOS C-V

For a MOS capacitor (Week 14), the C-V curve shows accumulation (C = C_ox), depletion (C falling) and inversion. It gives the oxide thickness (from C_ox = ε_oxA/t_ox), the flat-band and threshold voltages, the substrate doping, the charge trapped in the oxide, and the density of interface traps. It is the main tool for checking the quality and stability of gate oxides.

### Getting accurate C-V results

- Measure only in **reverse** bias (forward bias adds a large diffusion capacitance).
- Subtract stray and probe-pad capacitance (an open-circuit correction).
- Correct for series resistance.
- Keep the AC signal small.
- Choose the frequency so that deep traps do not respond (or so that they do, if you want to measure them).
- Know the device area accurately: N depends on 1/A².

## Key points of Week 12

- I-V: plot ln I against V. Intercept → I_s; slope → η = (q/kT)/slope; bending at high current → R_s; Arrhenius plot → Φ_B.
- C-V: a reverse-biased junction is a capacitor C = ε_sA/W, with W growing with reverse bias.
- Mott–Schottky: 1/C² = 2(V_bi − V)/(qε_sNA²). Slope → N = 2/(qε_sA²|slope|); intercept → V_bi.
- Non-uniform doping: local slope gives N at depth W = ε_sA/C.
- MOS C-V gives t_ox, V_FB, V_T, substrate doping and oxide quality.

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
