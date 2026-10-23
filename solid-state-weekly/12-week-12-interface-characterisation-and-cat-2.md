# Week 12 — Interface Characterisation and CAT 2
<!-- group: Module 4 · Junctions, Interfaces & Characterisation -->

**Plan:** methods of characterisation (capacitance–voltage C-V profiling, current–voltage I-V analysis); Continuous Assessment Test 2.

## Learning objectives

By the end of this week you should be able to:

1. Describe I-V measurement and extract I_s, η and R_s.
2. Explain how the Schottky barrier height is obtained from I-V data.
3. Explain the principle of C-V measurement.
4. Extract doping and built-in potential from a Mott–Schottky plot.
5. Explain doping profiling and the MOS C-V measurement.

## Symbols and abbreviations used this week

Every symbol, constant and abbreviation on this page is listed here, even if an earlier week already defined it, so you can study this page on its own.

**Constants and units**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| q | Magnitude of the electronic charge | 1.6×10⁻¹⁹ C |
| k | Boltzmann constant | 8.617×10⁻⁵ eV/K = 1.381×10⁻²³ J/K |
| kT | Thermal energy | 0.0259 eV (often 0.02585 eV) at 300 K |
| kT/q | Thermal voltage | 0.0259 V (about 26 mV) at 300 K |
| T | Absolute temperature | kelvin (K); room temperature = 300 K |
| ε_s (ε_si) | Permittivity of silicon, 11.7ε₀ | 1.04×10⁻¹² F/cm |
| ε_ox | Permittivity of SiO₂, 3.9ε₀ | 3.45×10⁻¹³ F/cm |
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| μm | Micrometre (micron) | 1 μm = 10⁻⁴ cm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| p | Hole concentration (holes per cm³) | cm⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | cm⁻³; Si ≈ 1×10¹⁰ at 300 K |
| N_D | Donor concentration | cm⁻³ |
| N_A | Acceptor concentration | cm⁻³ |
| Δn, Δp | Excess electron and hole concentrations above equilibrium | cm⁻³ |
| C(x, t) | Dopant concentration at depth x and time t | cm⁻³ |
| R_s | Sheet resistance (or diode series resistance in Week 12) | Ω/□ (ohms per square); Ω |
| E (field) | Electric field (on band diagrams, E is energy instead) | V/cm |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | cm²/(V·s); Si μ_n 1350, μ_p 480 |
| σ | Conductivity, q(nμ_n + pμ_p) (in Week 8, σ is also a capture cross-section) | S/cm (siemens per cm) |
| ρ | Resistivity, 1/σ | Ω·cm |
| J, J_n, J_p | Current density (total, electrons, holes) | A/cm² |
| D_n, D_p | Diffusion coefficients of electrons and holes | cm²/s; Si 35 and 12.4 |
| R | Recombination rate | cm⁻³s⁻¹ |
| τ, τ_n, τ_p | Minority-carrier lifetime (τ_eff: effective, including surfaces) | s; Si 1 ns – 1 ms |
| L, L_n, L_p | Diffusion length √(Dτ): distance a minority carrier travels before recombining | μm or cm |
| V_bi | Built-in potential of a junction or Schottky contact | V; typically 0.5–1 V |
| V, V_a | Applied voltage (positive for forward bias) | V |
| W | Depletion-region width (in Week 13 W_B, W_E are base and emitter widths; in Week 14 W is channel width) | μm or cm |
| E_max | Peak electric field, at the junction | V/cm |
| I_s, J_s (I_S) | Saturation current (density) of a diode or transistor | A; A/cm² |
| I | Current | A |
| A (area) | Device or contact area | cm² |
| η | Ideality factor of a diode, 1 (ideal) to 2 | dimensionless |
| C, C_j | Capacitance (junction or depletion capacitance) | F (pF = 10⁻¹² F) |
| Φ_B | Schottky barrier height seen from the metal | eV (or V) |
| A∗∗ | Effective Richardson constant | A/(cm²·K²); n-Si ≈ 110 |
| C_ox | Gate-oxide capacitance per unit area, ε_ox/t_ox | F/cm² |
| t_ox | Gate-oxide thickness | nm |
| V_T (V_th) | Threshold voltage of a MOSFET | V |
| V_FB | Flat-band voltage | V |
| V_GS, V_DS, V_SB, V_G | Gate–source, drain–source, source–body and gate voltages | V |
| I_D | Drain current | A (mA) |
| V_junction | Part of the applied voltage that appears across the junction itself | V |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| I-V | Current–voltage (measurement or characteristic) |
| C-V | Capacitance–voltage (measurement or characteristic) |
| LCR | Inductance–capacitance–resistance meter |
| MOS | Metal–oxide–semiconductor |
| MOSFET | Metal–oxide–semiconductor field-effect transistor |
| BJT | Bipolar junction transistor |
| CAT | Continuous Assessment Test |
| DC | Direct current (steady) |
| AC | Alternating current (small signal) |
| n⁺ | Very heavily doped n-type (similarly p⁺) |


## Key terms

Every important word used this week is defined here, so you can read this week on its own.

**Doping (N_D, N_A).** Adding a small, controlled amount of impurity atoms to a semiconductor to set its electrical properties. Donors (concentration N_D) give electrons and make the material n-type; acceptors (concentration N_A) take electrons, create holes and make it p-type. Doping is measured in atoms per cm³.

**Majority and minority carriers.** In n-type material electrons are the more numerous (majority) carriers and holes the less numerous (minority) carriers; in p-type material it is the other way round.

**Depletion region (W).** The thin layer on each side of a p-n junction, or under a metal–semiconductor contact, from which the mobile carriers have been swept away, leaving only the fixed charge of the ionised dopant atoms. Its width W grows when a reverse bias is applied.

**Built-in potential (V_bi).** The voltage that appears across the depletion region of a junction or Schottky contact with no applied bias. It is the barrier that stops majority carriers flowing across in equilibrium, typically 0.5–1 V in silicon.

**One-sided junction.** A p-n junction with one side much more heavily doped than the other (p⁺n or n⁺p). Almost all of the depletion region then lies in the lightly doped side, so measurements on it describe that side alone. A Schottky diode behaves the same way.

**Schottky diode and barrier height (Φ_B).** A Schottky diode is a rectifying metal–semiconductor contact. Its barrier height Φ_B is the energy step an electron in the metal must climb to enter the semiconductor; it fixes how much current the diode can leak.

*Why it matters:* Φ_B cannot be seen directly, but it sets the saturation current, so it can be found from an I-V measurement.

**Saturation current (I_s, J_s).** The small current that a diode carries under reverse bias, and the scale factor in front of the exponential in the diode equation. J_s = I_s/A is the same quantity per unit area.

**Ideality factor (η).** A number between 1 and 2 that says how closely a real diode follows the ideal diode equation. η = 1 means the current is pure diffusion (or, in a Schottky diode, pure thermionic emission); η near 2 means recombination in the depletion region dominates.

    I = I_s ( e^{qV/ηkT} − 1 )

Where:

- I = diode current (A)
- I_s = saturation current (A)
- V = applied voltage, positive for forward bias (V)
- η = ideality factor (dimensionless)
- kT/q = thermal voltage, 0.0259 V at 300 K

*Why it matters:* η tells you which current mechanism is at work, and so how good the junction is.

**Series resistance (R_s).** The resistance of the bulk semiconductor, contacts and leads in series with the junction itself. It wastes part of the applied voltage, so at high current the diode needs more voltage than the ideal equation predicts.

**I-V characterisation.** Measuring the current through a device as the applied voltage is stepped, and comparing the curve with theory to extract I_s, η, R_s, leakage, breakdown and, for a Schottky diode, Φ_B.

**Semi-log plot.** A graph of the natural logarithm of a quantity (here ln I) against a linear quantity (here V). An exponential law becomes a straight line on it, so slope and intercept can be read off.

**Effective Richardson constant (A∗∗).** The material constant in the thermionic-emission law that links a Schottky diode's saturation current density to its barrier height and temperature; about 110 A/(cm²·K²) for n-type Si.

**Arrhenius plot.** A graph of the logarithm of a temperature-dependent quantity against 1/T. A process with an energy barrier gives a straight line whose slope gives the barrier energy.

**Depletion (junction) capacitance (C, C_j).** The capacitance of a reverse-biased junction, which behaves like a parallel-plate capacitor with the depletion region as the gap between the plates. It falls as the reverse bias widens the depletion region.

**C-V characterisation.** Measuring the small-signal capacitance of a reverse-biased junction, Schottky diode or MOS capacitor as the DC bias is stepped, to find the doping, its profile with depth and the built-in potential.

**Mott–Schottky plot.** A graph of 1/C² against V for a one-sided junction or Schottky diode. Uniform doping gives a straight line: its slope gives the doping and its voltage-axis intercept gives V_bi.

*Why it matters:* it is the standard way of measuring doping electrically, without damaging the sample.

**Doping profile (N(x)).** The way the doping concentration changes with depth x below the surface, for example after diffusion or ion implantation.

**MOS capacitor.** A metal (or polysilicon) plate on a thin oxide on a semiconductor: the gate structure of a MOSFET. Its C-V curve reveals the oxide thickness, the flat-band and threshold voltages and the quality of the oxide.

## The big picture

After a device is made, how do you know what is inside it? You cannot see the doping or the barrier height. But you can **measure electrically** and compare the results with the theory of Weeks 10–11. Two measurements do most of the work:

- **I-V (current against voltage)** tells you **how current flows**: the saturation current, how ideal the junction is, the series resistance, leakage and breakdown, and for a Schottky diode the barrier height.
- **C-V (capacitance against voltage)** tells you **how charge is arranged**: the doping concentration (and how it changes with depth) and the built-in potential.

The trick in both cases is to plot the data so that the theory predicts a **straight line**, then read the answers from the slope and the intercept.

| Feature | I-V measurement | C-V measurement |
|---|---|---|
| What is applied | DC voltage, swept from reverse to forward bias | DC reverse bias, plus a small AC signal (10–50 mV, about 1 MHz) |
| What is measured | DC current | Small-signal capacitance |
| Instrument | Source-measure unit (or supply, resistor and meters) | LCR (capacitance) meter |
| Physics probed | How carriers **flow** across the junction | How fixed **charge** is arranged in the depletion region |
| Straight-line plot | ln I against V (semi-log) | 1/C² against V (Mott–Schottky) |
| Slope gives | Ideality factor η | Doping N |
| Intercept gives | Saturation current I_s (and Φ_B for a Schottky diode) | Built-in potential V_bi |
| Also gives | R_s, leakage, breakdown, Ohmic or rectifying contact | Doping profile N(x); for MOS: t_ox, V_FB, V_T, oxide charge |
| Main sources of error | Series resistance, heating, leakage paths at the edges | Stray capacitance, series resistance, uncertain area (N ∝ 1/A²), traps |
| Barrier height Φ_B | From I_s via thermionic emission: sensitive to barrier lowering and patches of low barrier | From V_bi: measures the average barrier, usually slightly higher than the I-V value |

## I-V characterisation

### The measurement

A **source-measure unit** (or a power supply with a series resistor and two meters) applies a voltage to the device in steps, from reverse to forward bias, and records the current at each step. Currents from picoamps to amps may need measuring, often on a probe station, sometimes at several temperatures.

### Turning the curve into a straight line

For a real diode,

    I = I_s ( e^{qV/ηkT} − 1 )

Where:

- I = diode current (A)
- I_s = saturation current (A)
- V = applied voltage, positive for forward bias (V)
- η = ideality factor (dimensionless, 1 to 2)
- q = electronic charge, 1.6×10⁻¹⁹ C; kT = thermal energy, so kT/q = 0.0259 V at 300 K

η (the **ideality factor**) is 1 for a perfect diffusion-current diode and up to 2 when recombination in the depletion region dominates. Above about 0.1 V the −1 is negligible, so take the natural log:

    ln I = ln I_s + (q/ηkT) V

That is a straight line if you plot **ln I against V** (a semi-log plot):

- the **intercept** at V = 0 gives **ln I_s**, so the saturation current I_s;
- the **slope** is q/(ηkT), so **η = (q/kT) / slope**.

#### Example 12.1: ideality factor and saturation current from I-V data

**Question.** A silicon diode carries 0.9 μA at a forward voltage of 0.30 V and 40 μA at 0.40 V. Assuming both points lie on the straight part of the semi-log plot, find the ideality factor and the saturation current (300 K).

**Given:** I₁ = 0.9 μA at V₁ = 0.30 V; I₂ = 40 μA at V₂ = 0.40 V; kT/q = 0.0259 V.

**Find:** η and I_s.

**Formula:**

    slope = ln(I₂/I₁)/(V₂ − V₁),     η = (q/kT)/slope,     I_s = I₁ e^{−slope × V₁}

**Solution.**

Step 1. Slope of ln I against V:

    slope = ln(I₂/I₁)/(V₂ − V₁) = ln(40/0.9)/0.10 = 3.79/0.10 = 37.9 V⁻¹

Step 2. Ideality factor, slope = q/(ηkT):

    η = 1/(0.0259 × 37.9) = 1.02

Step 3. Extrapolate back to V = 0:

    I_s = I₁ / e^{slope × V₁} = 0.9×10⁻⁶ / e^{37.9 × 0.30} = 0.9×10⁻⁶ / 8.7×10⁴ = 1.0×10⁻¹¹ A

**Answer:** **η = 1.02** (almost ideal diffusion current), **I_s ≈ 1×10⁻¹¹ A.**

**What this means:** the current rises by a factor of about 44 for only 0.1 V, almost exactly the 60 mV per decade of an ideal diode, so nearly all the current is diffusion current and depletion-region recombination is negligible. The tiny I_s (10 pA) is what makes the diode switch on only above about 0.5 V.

### What else the I-V curve shows

- **Series resistance R_s:** at high current the curve bends away from the straight line, because part of the voltage is dropped across the resistance of the bulk and contacts: V = V_junction + IR_s. R_s = (extra voltage)/I.
- **Reverse leakage and breakdown voltage** from the reverse branch.
- **Schottky barrier height** from I_s (see below). Measuring at several temperatures and plotting ln(I_s/T²) against 1/T (an **Arrhenius plot**) gives a straight line of slope −qΦ_B/k.
- **Ohmic contacts:** the I-V between two contacts should be a straight line through the origin, the same in both directions.

### Barrier height from the saturation current

In a Schottky diode the current is carried by electrons that have enough thermal energy to jump over the barrier (**thermionic emission**). The saturation current density is

    J_s = I_s/A = A∗∗ T² e^{−qΦ_B/kT}

Where:

- J_s = saturation current density (A/cm²)
- I_s = saturation current, from the intercept of the semi-log plot (A)
- A = diode (contact) area (cm²)
- A∗∗ = effective Richardson constant, 110 A/(cm²·K²) for n-Si
- T = absolute temperature (K)
- Φ_B = Schottky barrier height (eV, or V when multiplied by q)
- kT/q = thermal voltage, 0.0259 V at 300 K

Taking logarithms and solving for the barrier:

    Φ_B = (kT/q) ln( A∗∗ T² / J_s ) = (kT/q) ln( A∗∗ A T² / I_s )

Because Φ_B depends only on the logarithm of I_s, even a factor-of-two error in the area or in A∗∗ changes Φ_B by only 0.0259 × ln 2 ≈ 18 meV. That is why this is the standard I-V method for barrier height.

#### Example 12.2: barrier height from the saturation current

**Question.** A Schottky diode on n-type silicon has an area of 2×10⁻⁴ cm². Its semi-log forward I-V plot is straight with η = 1.03, and extrapolates to I_s = 1.2×10⁻¹⁰ A at V = 0 (300 K). Find the saturation current density, the barrier height, and the forward voltage needed for 1 mA (take η ≈ 1 for this last part).

**Given:** A = 2×10⁻⁴ cm², I_s = 1.2×10⁻¹⁰ A, T = 300 K, A∗∗ = 110 A/(cm²·K²), kT/q = 0.0259 V.

**Find:** J_s, Φ_B and V at I = 1 mA.

**Formula:**

    J_s = I_s/A,     Φ_B = (kT/q) ln( A∗∗T²/J_s ),     V = (kT/q) ln( I/I_s + 1 )

**Solution.**

Step 1. Saturation current density:

    J_s = 1.2×10⁻¹⁰ / 2×10⁻⁴ = 6.0×10⁻⁷ A/cm²

Step 2. A∗∗T² = 110 × (300)² = 9.9×10⁶ A/cm², so

    Φ_B = 0.0259 × ln( 9.9×10⁶ / 6.0×10⁻⁷ ) = 0.0259 × ln(1.65×10¹³) = 0.0259 × 30.43 = 0.79 eV

Step 3. Forward voltage for 1 mA:

    V = 0.0259 × ln( 10⁻³/1.2×10⁻¹⁰ + 1 ) = 0.0259 × 15.94 = 0.41 V

**Answer:** **J_s = 6.0×10⁻⁷ A/cm², Φ_B ≈ 0.79 eV, V ≈ 0.41 V at 1 mA.**

**What this means:** an η so close to 1 shows that thermionic emission over the barrier is the main current mechanism, so the formula applies. A 0.79 eV barrier is typical of a good rectifying contact on n-Si, and the diode turns on at about 0.4 V, well below the 0.6–0.7 V of a silicon p-n diode.

Transistors are characterised the same way: MOSFET I_D–V_GS curves give the threshold voltage and mobility (Week 14, Practical 4), and BJT curves give the current gain.

## C-V characterisation

### The measurement

An **LCR meter** applies a small AC voltage (10–50 mV, typically at 1 MHz) on top of a DC bias, and measures the capacitance. The DC bias is stepped through a range of **reverse** voltages.

### The theory: a capacitor whose plates move

A reverse-biased one-sided junction (p⁺n) or Schottky diode has a depletion region with no mobile carriers, between two conducting regions. It is a **parallel-plate capacitor** whose plate separation is the depletion width W:

    C = ε_s A / W

Where:

- C = depletion (junction) capacitance (F)
- ε_s = permittivity of silicon, 1.04×10⁻¹² F/cm
- A = junction area (cm²)
- W = depletion-region width (cm)

From Week 10, W = √(2ε_s(V_bi − V)/qN), where N is the doping on the lightly doped side. **As the reverse voltage increases, W gets bigger and C gets smaller.** Substituting:

    C = A √( qε_sN / 2(V_bi − V) )

Where:

- q = electronic charge, 1.6×10⁻¹⁹ C
- N = doping on the lightly doped side (cm⁻³)
- V_bi = built-in potential (V)
- V = applied voltage, negative for reverse bias (V)
- C, A, ε_s as above

### Turning it into a straight line: the Mott–Schottky plot

Square both sides and turn upside down:

    1/C² = 2(V_bi − V) / (qε_sNA²)

Where:

- 1/C² = inverse square of the measured capacitance (F⁻²)
- V_bi = built-in potential (V); V = applied voltage (V)
- q = 1.6×10⁻¹⁹ C; ε_s = 1.04×10⁻¹² F/cm
- N = doping on the lightly doped side (cm⁻³); A = area (cm²)

So if you plot **1/C² against V**, uniform doping gives a **straight line**:

- **Slope** = −2/(qε_sNA²), which gives the doping N (equation below).
- **Intercept** on the voltage axis (where 1/C² = 0) is at V = V_bi: the **built-in potential**.

Rearranging the slope for the doping:

    N = 2 / ( qε_s A² × |slope| )

Where:

- N = doping concentration on the lightly doped side (cm⁻³)
- |slope| = magnitude of the slope of the 1/C² against V line (F⁻²V⁻¹)
- q = 1.6×10⁻¹⁹ C; ε_s = 1.04×10⁻¹² F/cm; A = area (cm²)

@fig figures/cv.svg | Mott–Schottky plot. For uniform doping the points fall on a straight line; the slope gives the doping and the voltage-axis intercept gives V_bi.

> **In plain words.** Reverse bias pushes the edge of the depletion region deeper into the semiconductor. How much extra charge is uncovered as the edge moves tells you how many dopant atoms are there. The capacitance measures exactly that.

#### Example 12.3: doping and built-in potential from a C-V plot

**Question.** A silicon Schottky diode of area 1×10⁻³ cm² gives a straight 1/C² against V plot with slope −1.2×10²¹ F⁻²V⁻¹ that meets the voltage axis at +0.60 V. Find the doping concentration and the built-in potential. Also find the capacitance and depletion width at a reverse bias of 5 V.

**Given:** A = 1×10⁻³ cm², slope = −1.2×10²¹ F⁻²V⁻¹, intercept 0.60 V, ε_s = 1.036×10⁻¹² F/cm, q = 1.602×10⁻¹⁹ C, V = −5 V.

**Find:** N_D, V_bi, and C and W at −5 V.

**Formula:**

    N_D = 2/(qε_sA²|slope|),     C = A√( qε_sN_D / 2(V_bi − V) ),     W = ε_sA/C

**Solution.**

Step 1. Doping from the slope:

    N_D = 2/(qε_sA²|slope|) = 2 / (1.602×10⁻¹⁹ × 1.036×10⁻¹² × (10⁻³)² × 1.2×10²¹) = 2/1.99×10⁻¹⁶ = 1.0×10¹⁶ cm⁻³

Step 2. Built-in potential from the intercept: V_bi = 0.60 V

Step 3. At V = −5 V, V_bi − V = 5.6 V:

    C = A√(qε_sN_D / 2(V_bi − V)) = 10⁻³ × √(1.66×10⁻¹⁵ / 11.2) = 1.22×10⁻¹¹ F

    W = ε_sA/C = 1.036×10⁻¹⁵ / 1.22×10⁻¹¹ = 8.5×10⁻⁵ cm

**Answer:** **N_D = 1.0×10¹⁶ cm⁻³, V_bi = 0.60 V; at −5 V, C = 12.2 pF and W = 0.85 μm.**

**What this means:** the semiconductor is moderately doped n-type, about one dopant atom for every 5 million silicon atoms, found without cutting or etching the sample. At −5 V the depletion edge sits 0.85 μm below the contact, so this is the depth at which the doping is being sampled at that bias.

### Doping profiles

If the doping is **not** uniform, the 1/C² plot curves. The local slope at each bias still gives the doping at the edge of the depletion region, and the capacitance tells you where that edge is:

    N(W) = 2 / ( qε_sA² × |d(1/C²)/dV| ),     W = ε_sA/C

Where:

- N(W) = doping at the edge of the depletion region, at depth W (cm⁻³)
- |d(1/C²)/dV| = magnitude of the local slope of the 1/C² curve at that bias (F⁻²V⁻¹)
- W = depletion width, the depth being probed (cm)
- C = measured capacitance at that bias (F)
- q = 1.6×10⁻¹⁹ C; ε_s = 1.04×10⁻¹² F/cm; A = area (cm²)

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
- Schottky barrier height from one I-V curve: Φ_B = (kT/q) ln(A∗∗T²/J_s), with J_s = I_s/A and A∗∗ = 110 A/(cm²·K²) for n-Si.
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

**Question.** An n-type Si bar (N_D = 10¹⁶ cm⁻³, μ_n = 1200 cm²/V·s) is 1 cm long with 10⁻³ cm² cross-section. Find its resistance and the current at 5 V.

**Given:** N_D = 10¹⁶ cm⁻³, μ_n = 1200 cm²/V·s, L = 1 cm, A = 10⁻³ cm², V = 5 V.

**Find:** R and I.

**Formula:**

    σ = qN_Dμ_n,     ρ = 1/σ,     R = ρL/A,     I = V/R

**Solution.**

    σ = qN_Dμ_n = 1.6×10⁻¹⁹ × 10¹⁶ × 1200 = 1.92 S/cm,   ρ = 0.521 Ω·cm
    R = ρL/A = 0.521 × 1 / 10⁻³ = 521 Ω
    I = V/R = 5/521 = 9.6 mA

**Answer:** **R ≈ 521 Ω, I ≈ 9.6 mA.**

**What this means:** with 10¹⁶ donors per cm³ the silicon conducts several hundred thousand times better than pure silicon, but a long thin bar is still a resistor of several hundred ohms; this is how diffused resistors in integrated circuits work.

### 2. Einstein relation and diffusion length

**Question.** Find the hole diffusion coefficient in Si if μ_p = 450 cm²/V·s, and the diffusion length if τ_p = 2 μs.

**Given:** μ_p = 450 cm²/V·s, τ_p = 2×10⁻⁶ s, kT/q = 0.0259 V.

**Find:** D_p and L_p.

**Formula:**

    D_p = (kT/q)μ_p,     L_p = √(D_pτ_p)

**Solution.**

    D_p = (kT/q)μ_p = 0.0259 × 450 = 11.7 cm²/s
    L_p = √(D_pτ_p) = √(11.7 × 2×10⁻⁶) = 4.83×10⁻³ cm = 48 μm

**Answer:** **D_p ≈ 11.7 cm²/s, L_p ≈ 48 μm.**

**What this means:** an injected hole typically wanders about 48 μm before it recombines, far more than the width of a transistor base, so almost all holes injected into a thin region survive to cross it.

### 3. Diffusion current at the injection point

**Question.** Holes injected into n-Si fall from 10¹⁴ cm⁻³ at x = 0 with L_p = 30 μm. Find the hole diffusion current density at x = 0 (D_p = 11.6 cm²/s).

**Given:** Δp(0) = 10¹⁴ cm⁻³, L_p = 30 μm = 3×10⁻³ cm, D_p = 11.6 cm²/s.

**Find:** J_p at x = 0.

**Formula:**

    Δp(x) = Δp(0)e^{−x/L_p},     J_p = −qD_p dp/dx

**Solution.**

Δp(x) = Δp(0)e^{−x/L_p}, so dp/dx at x = 0 is −Δp(0)/L_p.

    J_p = −qD_p dp/dx = qD_pΔp(0)/L_p = 1.6×10⁻¹⁹ × 11.6 × 10¹⁴ / 3×10⁻³
        = 0.062 A/cm²

**Answer:** **J_p ≈ 0.062 A/cm² (62 mA/cm²), flowing in the +x direction.**

**What this means:** with no electric field at all, a concentration difference alone drives a sizeable current; the steeper the fall-off (the shorter L_p), the larger the current.

### 4. Junction parameters

**Question.** A Si p⁺n junction has N_D = 5×10¹⁵ cm⁻³ and N_A = 10¹⁸ cm⁻³. Find V_bi, the depletion width at zero bias and at −10 V, and the peak field at −10 V.

**Given:** N_D = 5×10¹⁵ cm⁻³, N_A = 10¹⁸ cm⁻³, n_i = 10¹⁰ cm⁻³, ε_s = 1.04×10⁻¹² F/cm, kT/q = 0.0259 V.

**Find:** V_bi, W(0), W(−10 V), E_max(−10 V).

**Formula:**

    V_bi = (kT/q) ln(N_{A}N_D/n_i²),     W = √(2ε_s(V_bi − V)/qN_D),     E_max = 2(V_bi − V)/W

**Solution.**

    V_bi = 0.0259 ln(10¹⁸ × 5×10¹⁵ / 10²⁰) = 0.0259 ln(5×10¹³) = 0.0259 × 31.54 = 0.817 V

One-sided (N_A ≫ N_D): W = √(2ε_s(V_bi − V)/qN_D).

    V = 0:    W = √(2 × 1.04×10⁻¹² × 0.817 / (1.6×10⁻¹⁹ × 5×10¹⁵)) = √(2.12×10⁻⁹) = 4.6×10⁻⁵ cm = 0.46 μm
    V = −10:  W = √(2 × 1.04×10⁻¹² × 10.817 / 8×10⁻⁴) = √(2.81×10⁻⁸) = 1.68×10⁻⁴ cm = 1.68 μm
    E_max = 2(V_bi − V)/W = 2 × 10.817 / 1.68×10⁻⁴ = 1.29×10⁵ V/cm

**Answer:** **V_bi = 0.817 V; W = 0.46 μm at 0 V and 1.68 μm at −10 V; E_max = 1.29×10⁵ V/cm.**

**What this means:** the depletion region lies almost entirely in the lightly doped n side and grows as the square root of the voltage. The peak field is still below the roughly 3×10⁵ V/cm at which silicon breaks down, so the junction safely blocks 10 V.

### 5. Diode current

**Question.** The diode of Q4 has area 10⁻³ cm² and I_s = 1×10⁻¹⁴ A. Find the current at 0.6 V and the voltage for 1 mA.

**Given:** I_s = 10⁻¹⁴ A, kT/q = 0.0259 V, ideal diode (η = 1).

**Find:** I at 0.6 V; V at 1 mA.

**Formula:**

    I = I_s(e^{qV/kT} − 1),     V = (kT/q) ln(I/I_s + 1)

**Solution.**

    I(0.6 V) = 10⁻¹⁴ (e^{0.6/0.0259} − 1) = 10⁻¹⁴ × 1.15×10¹⁰ = 0.115 mA
    V(1 mA) = 0.0259 ln(10⁻³/10⁻¹⁴ + 1) = 0.0259 × 25.33 = 0.656 V

**Answer:** **I = 0.115 mA at 0.6 V; V = 0.656 V for 1 mA.**

**What this means:** raising the voltage by only 56 mV multiplies the current by almost nine, which is why a silicon diode looks as if it "turns on" sharply at about 0.6–0.7 V.

### 6. Schottky diode

**Question.** A Schottky diode on n-Si has Φ_B = 0.7 eV. Find J_s at 300 K (A∗∗ = 110 A/cm²K²) and the forward voltage for J = 10 A/cm².

**Given:** Φ_B = 0.7 eV, T = 300 K, A∗∗ = 110 A/(cm²·K²), J = 10 A/cm², kT/q = 0.0259 V.

**Find:** J_s and V.

**Formula:**

    J_s = A∗∗T² e^{−qΦ_B/kT},     V = (kT/q) ln(J/J_s)

**Solution.**

    J_s = A∗∗T²e^{−qΦ_B/kT} = 110 × 9×10⁴ × e^{−0.7/0.0259} = 9.9×10⁶ × 1.82×10⁻¹² = 1.8×10⁻⁵ A/cm²
    V = 0.0259 ln(10/1.8×10⁻⁵) = 0.0259 × 13.23 = 0.343 V

**Answer:** **J_s ≈ 1.8×10⁻⁵ A/cm²; V ≈ 0.34 V for 10 A/cm².**

**What this means:** a p-n diode needs about 0.7 V for a similar current density, which is why Schottky diodes are used where a low forward drop matters.

### 7. Doping from C-V

**Question.** A 1/C² plot for a one-sided junction of area 2×10⁻³ cm² has slope magnitude 4.0×10²⁰ F⁻²V⁻¹. Find the doping.

**Given:** A = 2×10⁻³ cm², |slope| = 4.0×10²⁰ F⁻²V⁻¹, q = 1.6×10⁻¹⁹ C, ε_s = 1.04×10⁻¹² F/cm.

**Find:** N.

**Formula:**

    N = 2/(qε_sA²|slope|)

**Solution.**

    N = 2/(qε_sA²|slope|) = 2 / (1.6×10⁻¹⁹ × 1.04×10⁻¹² × (2×10⁻³)² × 4.0×10²⁰)
      = 2 / (2.66×10⁻¹⁶) = 7.5×10¹⁵ cm⁻³

**Answer:** **N ≈ 7.5×10¹⁵ cm⁻³** (the doping of the lightly doped side).

**What this means:** a shallower 1/C² line means heavier doping; because N depends on 1/A², a 10 % error in the measured area would give about a 20 % error in this doping.

---

## Practice questions

These extra questions practise this week's ideas. Work each one on paper before reading the solution; the calculation questions follow the same Question, Given, Find, Solution, Answer layout as the worked examples.

#### Practice 12.1: ideality factor

**Question.** A diode carries 1 mA at 0.55 V and 10 mA at 0.62 V. Find its ideality factor.

**Given:** a decade of current over ΔV = 0.07 V, kT/q = 0.0259 V.

**Find:** η.

**Solution.**

    slope = ln 10 / 0.07 = 32.9 V⁻¹
    η = 1/(0.0259 × 32.9) = 1.17

**Answer:** **η ≈ 1.17**: some depletion-region recombination current is present.

#### Practice 12.2: series resistance

**Question.** At 50 mA a diode's measured voltage is 0.80 V, while the straight line of the semi-log plot predicts 0.70 V at that current. Find the series resistance.

**Given:** I = 50 mA, ΔV = 0.80 − 0.70 = 0.10 V.

**Find:** R_s.

**Solution.**

    R_s = ΔV/I = 0.10/0.05 = 2 Ω

**Answer:** **R_s = 2 Ω.**

#### Practice 12.3: barrier height from the saturation current

**Question.** A Schottky diode of area 1×10⁻⁴ cm² has I_s = 2×10⁻⁹ A at 300 K. Find the barrier height (A∗∗ = 110 A/cm²K²).

**Given:** I_s = 2×10⁻⁹ A, A = 10⁻⁴ cm², A∗∗ = 110 A/cm²K², T = 300 K.

**Find:** Φ_B.

**Solution.**

    Φ_B = (kT/q) ln(A∗∗AT²/I_s) = 0.0259 × ln(110 × 10⁻⁴ × 9×10⁴ / 2×10⁻⁹)
        = 0.0259 × ln(4.95×10¹¹) = 0.0259 × 26.93 = 0.70 eV

**Answer:** **Φ_B ≈ 0.70 eV.**

**What this means:** a 2 nA leakage from such a small contact points to a moderate barrier; a diode with Φ_B only 0.1 eV lower would leak about 50 times more.

#### Practice 12.4: doping from two C-V points

**Question.** A one-sided silicon junction of area 1×10⁻³ cm² has C = 20 pF at −1 V and 12 pF at −4 V. Assuming uniform doping, find N and V_bi.

**Given:** C(−1 V) = 20 pF, C(−4 V) = 12 pF, A = 10⁻³ cm², ε_s = 1.04×10⁻¹² F/cm.

**Find:** N and V_bi.

**Solution.**

    1/C² at −1 V = 1/(20×10⁻¹²)² = 2.50×10²¹ F⁻²
    1/C² at −4 V = 1/(12×10⁻¹²)² = 6.94×10²¹ F⁻²
    |slope| = (6.94 − 2.50)×10²¹ / 3 = 1.48×10²¹ F⁻²V⁻¹
    N = 2/(qε_sA²|slope|) = 2/(1.6×10⁻¹⁹ × 1.04×10⁻¹² × 10⁻⁶ × 1.48×10²¹) = 8.1×10¹⁵ cm⁻³
    1/C² = |slope|(V_bi − V):  2.50×10²¹ = 1.48×10²¹ (V_bi + 1)  ⇒  V_bi = 0.69 V

**Answer:** **N = 8.1×10¹⁵ cm⁻³, V_bi = 0.69 V.**

**What this means:** two capacitance readings are enough to estimate both the doping and the built-in potential, but only if the doping is uniform; a real profile needs many points so that the curvature of the 1/C² plot can be seen.

#### Practice 12.5: oxide thickness from MOS C-V

**Question.** A MOS capacitor of area 1×10⁻³ cm² shows a capacitance of 345 pF in accumulation. Find the oxide thickness.

**Given:** C = 345 pF, A = 10⁻³ cm², ε_ox = 3.45×10⁻¹³ F/cm.

**Find:** t_ox.

**Solution.**

    C_ox = C/A = 345×10⁻¹² / 10⁻³ = 3.45×10⁻⁷ F/cm²
    t_ox = ε_ox/C_ox = 3.45×10⁻¹³ / 3.45×10⁻⁷ = 1×10⁻⁶ cm

**Answer:** **t_ox = 10 nm.**

#### Practice 12.6: why one-sided?

**Question.** Why is C-V profiling done on a p⁺n (or n⁺p) junction or a Schottky diode rather than a junction with similar doping on both sides?

**Answer.** The formula N = 2/(qε_sA²|d(1/C²)/dV|) assumes that the depletion region grows into **one** side only, so that the change in charge measures one doping. In a one-sided junction or Schottky diode, almost all of W lies in the lightly doped side, and the measurement gives that side's doping at depth W. If both sides were similarly doped, W would grow into both at once, and the result would be a mixture (an effective N_{A}N_D/(N_A + N_D)) that cannot be assigned to either side or to a depth.

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Describe I-V measurement and extract I_s, η and R_s. | What plot gives a straight line for a diode, and what does its slope give? | ln I against V; slope = q/(ηkT). | I-V characterisation; Example 12.1; I-V vs C-V table (The big picture) |
| 2 | Explain how the Schottky barrier height is obtained from I-V data. | What is plotted in an Arrhenius plot of a Schottky diode? | ln(I_s/T²) against 1/T; slope = −qΦ_B/k. | What else the I-V curve shows; Barrier height from the saturation current; Example 12.2 |
| 3 | Explain the principle of C-V measurement. | Why does the junction capacitance fall with reverse bias? | The depletion width W grows, and C = ε_sA/W. | C-V characterisation |
| 4 | Extract doping and built-in potential from a Mott–Schottky plot. | What gives N and what gives V_bi in a 1/C² plot? | N from the slope, N = 2/(qε_sA²|slope|); V_bi from the voltage intercept. | Mott–Schottky plot; Example 12.3 |
| 5 | Explain doping profiling and the MOS C-V measurement. | Where is the doping being measured at each bias? | At the depletion edge, depth W = ε_sA/C. | Doping profiles; MOS C-V |
