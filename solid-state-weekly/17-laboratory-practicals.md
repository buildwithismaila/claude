# Laboratory and Practical Component
<!-- group: Revision & Practicals -->

The course plan requires at least four practical or simulation experiments (3 hours/week). Each practical below gives the aim, theory, procedure, a results table and the analysis. **The readings in the tables are example values** that show what correct results look like; replace them with your own measurements.

## Symbols and abbreviations used on this page

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
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| μm | Micrometre (micron) | 1 μm = 10⁻⁴ cm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_g | Band-gap energy, E_c − E_v | eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K |
| E_F | Fermi level: the energy at which a state has a 50 % chance of being occupied | eV |
| E_i | Intrinsic Fermi level, close to mid-gap | eV |
| N_c | Effective density of states in the conduction band | cm⁻³; Si 2.8×10¹⁹ at 300 K |
| N_v | Effective density of states in the valence band | cm⁻³; Si 1.04×10¹⁹ at 300 K |
| n | Electron concentration (free electrons per cm³) | cm⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | cm⁻³; Si ≈ 1×10¹⁰ at 300 K |
| N_D | Donor concentration | cm⁻³ |
| C(x, t) | Dopant concentration at depth x and time t | cm⁻³ |
| R_s | Sheet resistance (or diode series resistance in Week 12) | Ω/□ (ohms per square); Ω |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | cm²/(V·s); Si μ_n 1350, μ_p 480 |
| V_bi | Built-in potential of a junction or Schottky contact | V; typically 0.5–1 V |
| V, V_a | Applied voltage (positive for forward bias) | V |
| W | Depletion-region width (in Week 13 W_B, W_E are base and emitter widths; in Week 14 W is channel width) | μm or cm |
| I_s, J_s (I_S) | Saturation current (density) of a diode or transistor | A; A/cm² |
| I | Current | A |
| A (area) | Device or contact area | cm² |
| η | Ideality factor of a diode, 1 (ideal) to 2 | dimensionless |
| C, C_j | Capacitance (junction or depletion capacitance) | F (pF = 10⁻¹² F) |
| Φ_B | Schottky barrier height seen from the metal | eV (or V) |
| A∗∗ | Effective Richardson constant | A/(cm²·K²); n-Si ≈ 110 |
| C_ox | Gate-oxide capacitance per unit area, ε_ox/t_ox | F/cm² |
| V_T (V_th) | Threshold voltage of a MOSFET | V |
| V_FB | Flat-band voltage | V |
| V_GS, V_DS, V_SB, V_G | Gate–source, drain–source, source–body and gate voltages | V |
| I_D | Drain current | A (mA) |
| W/L | Channel width-to-length ratio | dimensionless |
| g_m | Transconductance, ∂I_D/∂V_GS | S (A/V) |
| k (MOSFET) | Device parameter μ_nC_ox(W/L) | A/V² (mA/V²) |
| ΔI_D, ΔV_GS | Small changes in drain current and gate voltage (their ratio is g_m) | A; V |
| N(x), N(W) | Doping concentration at depth x (or at the depletion edge W), from C-V profiling | cm⁻³ |
| ΔV, ΔV_BE | A small change in a voltage | V |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| Ge | Germanium |
| SiO₂ | Silicon dioxide (silica), the oxide insulator |
| I-V | Current–voltage (measurement or characteristic) |
| C-V | Capacitance–voltage (measurement or characteristic) |
| LCR | Inductance–capacitance–resistance meter |
| SMU | Source-measure unit |
| MOS | Metal–oxide–semiconductor |
| MOSFET | Metal–oxide–semiconductor field-effect transistor |
| DC | Direct current (steady) |
| AC | Alternating current (small signal) |
| n⁺ | Very heavily doped n-type (similarly p⁺) |
| MATLAB | A numerical computing program (alternative to Python) |


## Key terms

Every important word used on this page is defined here, so you can do these practicals without first rereading the weeks they come from.

**Fermi level (E_F) and intrinsic level (E_i).** The Fermi level is the energy at which a state has a 50 % chance of being occupied by an electron. The intrinsic level E_i is where E_F lies in pure silicon, close to mid-gap; in n-type material E_F lies above E_i by kT ln(n/n_i).

**Intrinsic temperature.** The temperature at which the thermally generated carrier concentration n_i rises to equal the doping, so the material stops behaving as doped and E_F falls back to mid-gap. Above it a device no longer works properly.

**I-V characteristic.** A graph of a device's current against the voltage across it. A semi-log plot shows ln I (or log₁₀ I) against V, which turns an exponential law into a straight line.

**Saturation current (I_s).** The small current that a diode's exponential law extrapolates to at V = 0; it is also the reverse current of an ideal diode. It is read from the intercept of the semi-log plot.

**Ideality factor (η).** A number between 1 and 2 that says how closely a diode follows the ideal exponential law; it is found from the slope of the semi-log plot.

    I = I_s[ e^{qV/ηkT} − 1 ],   η = (q/kT) / slope of ln I against V

Where:

- I = diode current (A); I_s = saturation current (A)
- V = voltage across the diode (V)
- η = ideality factor (dimensionless): 1 for pure diffusion current, nearer 2 when recombination in the depletion region dominates
- kT/q = thermal voltage, 0.0259 V at 300 K

*Why it matters:* η close to 1 shows a good-quality junction; a larger value points to defects or surface leakage.

**Series resistance (R_s).** The resistance of the bulk semiconductor, contacts and leads in series with the junction. At high current it adds a voltage drop IR_s, so the semi-log plot bends away from a straight line.

    R_s = ΔV / I

Where:

- R_s = series resistance (Ω)
- ΔV = extra voltage above the extrapolated straight line at current I (V)
- I = forward current at that point (A)

**Schottky diode and barrier height (Φ_B).** A Schottky diode is a rectifying metal–semiconductor contact whose current is carried by majority carriers crossing an energy barrier of height Φ_B. A lower Φ_B gives a larger I_s, a lower turn-on voltage and a larger reverse leakage than a p-n diode.

**Turn-on voltage and reverse leakage current.** The turn-on voltage is the forward voltage at which a diode's current becomes noticeable (about 0.6 V for a Si p-n diode, 0.2–0.3 V for a Schottky diode). The reverse leakage current is the small current that flows under reverse bias.

**Depletion capacitance (C, C_j).** The capacitance of a reverse-biased junction: the depletion region of width W acts as the insulating layer between two conducting plates, so C = ε_sA/W, and C falls as the reverse bias widens the depletion region.

**Built-in potential (V_bi).** The voltage across a junction's depletion region in equilibrium, typically 0.5–1 V for Si; in C-V profiling it is the voltage at which the straight line of 1/C² reaches zero.

**C-V profiling and the Mott–Schottky plot.** C-V profiling is measuring a junction's capacitance against reverse bias to find its doping. A Mott–Schottky plot is the graph of 1/C² against V: its slope gives the doping N and its intercept gives V_bi. A straight line means uniform doping.

**One-sided junction.** A junction with one side far more heavily doped than the other (p⁺n or n⁺p, or a Schottky contact), so the depletion region lies almost entirely in the lightly doped side and C-V gives that side's doping.

**LCR meter.** An instrument that measures inductance (L), capacitance (C) and resistance (R) by applying a small AC test signal (here 20–50 mV at 1 MHz), usually with an adjustable DC bias added.

**Open-circuit correction (nulling).** Measuring the test fixture with no device in place and subtracting that stray capacitance from every later reading, so only the device's capacitance is recorded.

**Source-measure unit (SMU) and parameter analyser.** An SMU is a precision instrument that applies a chosen voltage (or current) and measures the resulting current (or voltage) at the same time. A semiconductor parameter analyser contains several SMUs and sweeps them automatically to record device characteristics.

**Threshold voltage (V_T).** The gate-to-source voltage at which a MOSFET's channel forms and drain current begins to flow. Here it is found by drawing a straight line through the steepest part of the transfer curve and extending it to I_D = 0 (linear extrapolation).

**Flat-band voltage (V_FB).** The gate voltage at which the energy bands in a MOS structure are flat up to the surface (no surface charge). It is the starting point of the threshold voltage, which adds the voltage needed to bend the bands to inversion and to hold the depletion charge.

**Transfer and output characteristics.** The transfer characteristic is I_D plotted against V_GS at fixed V_DS; the output characteristics are I_D against V_DS for several fixed values of V_GS.

**Transconductance (g_m).** The change in drain current per unit change in gate voltage, measured as the slope of the transfer curve, in siemens (A/V).

    g_m = ΔI_D/ΔV_GS

Where:

- g_m = transconductance (S)
- ΔI_D = small change in drain current (A)
- ΔV_GS = small change in gate-to-source voltage that causes it (V)

**Channel (effective) mobility.** The mobility of electrons in the thin MOSFET channel, worked out from the measured g_m. It is well below the bulk mobility (1350 cm²/V·s in Si) because the electrons scatter off the Si/SiO₂ interface, and it falls further at high gate voltage (mobility degradation).

---

## Practical 1 — Simulation of carrier transport: Fermi-level shifts in Python

**Aim.** Model how the Fermi level of silicon moves with temperature and with doping, and find the temperature at which a doped sample becomes intrinsic.

**Theory (Weeks 4–5).**

    n_i(T) = √(N_cN_v) e^{−E_g(T)/2kT},   N_c, N_v ∝ T^{3/2},   E_g(T) = 1.17 − 4.73×10⁻⁴T²/(T + 636) eV
    n = N_D/2 + √((N_D/2)² + n_i²)   (complete ionisation)
    E_F − E_i = kT ln(n/n_i)

Where:

- n_i(T) = intrinsic carrier concentration at temperature T (cm⁻³)
- N_c, N_v = effective densities of states in the conduction and valence bands, 2.8×10¹⁹ and 1.04×10¹⁹ cm⁻³ at 300 K
- E_g(T) = band gap of Si at temperature T (eV); T = absolute temperature (K)
- k = Boltzmann constant, 8.617×10⁻⁵ eV/K; kT = thermal energy (eV)
- n = electron concentration (cm⁻³); N_D = donor concentration (cm⁻³)
- E_F − E_i = height of the Fermi level above the intrinsic level (eV)

**Procedure.**

1. Run the script below (Python 3 with NumPy and Matplotlib; the same steps work in MATLAB).
2. Plot E_F − E_i against T from 200 K to 700 K for N_D = 10¹⁴, 10¹⁵, 10¹⁶ and 10¹⁷ cm⁻³.
3. Plot E_F − E_i against N_D at 300 K from 10¹⁴ to 10¹⁸ cm⁻³ and measure the slope per decade.
4. For each doping, record the temperature at which n_i = N_D.

```
import numpy as np
import matplotlib.pyplot as plt

k = 8.617e-5                       # Boltzmann constant, eV/K
Nc300, Nv300 = 2.8e19, 1.04e19     # effective densities of states at 300 K, cm^-3

def Eg(T):                         # silicon band gap, eV (Varshni)
    return 1.17 - 4.73e-4 * T**2 / (T + 636)

def ni(T):
    Nc = Nc300 * (T / 300)**1.5
    Nv = Nv300 * (T / 300)**1.5
    raw = np.sqrt(Nc * Nv) * np.exp(-Eg(T) / (2 * k * T))
    return raw * 1e10 / ni_raw300  # scale so n_i(300 K) = 1e10 cm^-3

ni_raw300 = np.sqrt(Nc300 * Nv300) * np.exp(-Eg(300) / (2 * k * 300))

def EF_minus_Ei(T, ND):
    n = ND / 2 + np.sqrt((ND / 2)**2 + ni(T)**2)
    return k * T * np.log(n / ni(T))

T = np.linspace(200, 700, 501)
for ND in (1e14, 1e15, 1e16, 1e17):
    plt.plot(T, EF_minus_Ei(T, ND), label=f"N_D = {ND:.0e} cm^-3")
    Tint = T[np.argmin(abs(ni(T) - ND))]
    print(f"N_D = {ND:.0e}: E_F - E_i at 300 K = {EF_minus_Ei(300, ND):.3f} eV, "
          f"n_i = N_D at about {Tint:.0f} K")
plt.xlabel("T (K)"); plt.ylabel("E_F - E_i (eV)"); plt.legend(); plt.grid()
plt.show()

slope = (EF_minus_Ei(300, 1e17) - EF_minus_Ei(300, 1e16))
print(f"Shift per decade of doping at 300 K: {1000 * slope:.1f} mV")
```

**Results** (output of the script):

| N_D (cm⁻³) | E_F − E_i at 300 K (eV) | Temperature where n_i = N_D |
|---|---|---|
| 10¹⁴ | 0.238 | ≈ 470 K |
| 10¹⁵ | 0.298 | ≈ 550 K |
| 10¹⁶ | 0.357 | ≈ 650 K |
| 10¹⁷ | 0.417 | above 700 K |

Shift per decade of doping at 300 K: 59.5 mV (= kT ln 10).

@fig figures/fermi-vs-t.svg | Output of Practical 1: Fermi level against temperature for silicon. Each curve falls towards zero (mid-gap) once n_i approaches N_D.

**Discussion points.** (1) Why does the curve flatten near zero at high T? (2) Why does heavier doping raise the maximum operating temperature? (3) What would change for germanium (E_g = 0.66 eV)? Germanium reaches n_i = 10¹⁵ cm⁻³ at only about 400 K, which is why Ge devices fail at modest temperatures.

---

## Practical 2 — I-V characterisation of a p-n junction and a Schottky diode

**Aim.** Measure and plot the forward and reverse characteristics of a silicon p-n diode (e.g. 1N4148) and a Schottky diode (e.g. 1N5817 or BAT85); extract the saturation current, ideality factor and series resistance, and compare the two.

**Theory (Weeks 10–12).** I = I_s[exp(qV/ηkT) − 1]. Above about 0.1 V, ln I = ln I_s + qV/(ηkT), so a semi-log plot is a straight line with slope q/(ηkT) and intercept ln I_s.

**Apparatus.** DC supply (0–10 V) or source-measure unit, series resistor (1 kΩ for forward, none for reverse), two digital multimeters, breadboard, diodes.

**Procedure.**

1. Connect supply → resistor → diode (anode to +). Measure the diode voltage V and the current I (from the resistor voltage, or an ammeter).
2. **Forward:** increase the supply so that V rises from 0 to 0.8 V (p-n) or 0 to 0.5 V (Schottky) in 0.05 V steps. Do not exceed the rated current.
3. **Reverse:** reverse the diode, remove the resistor (or use 100 kΩ) and step V from 0 to −10 V, reading the small reverse current (μA range for Schottky, nA range for p-n).
4. Plot I against V on linear axes, and ln I (or log₁₀ I) against V for the forward branch.

**Example readings (forward):**

| V (V) | I, p-n diode | I, Schottky diode |
|---|---|---|
| 0.15 | 0.003 μA | 0.016 mA |
| 0.20 | 0.02 μA | 0.10 mA |
| 0.25 | 0.13 μA | 0.63 mA |
| 0.30 | 0.9 μA | 4.0 mA |
| 0.35 | 5.7 μA | 25 mA |
| 0.40 | 40 μA | (beyond rating) |
| 0.50 | 1.7 mA | — |
| 0.60 | 45 mA (bending: series resistance) | — |

**Analysis.**

- From the straight part of the p-n semi-log plot: between 0.3 V and 0.4 V, I rises from 0.9 μA to 40 μA, a factor of 44.4, so ln(44.4) = 3.79 per 0.1 V, slope = 37.9 V⁻¹. Then η = 1/(0.0259 × 37.9) = 1.02. Extrapolating to V = 0: I_s = 0.9 μA / e^{3.79×3} ≈ 1×10⁻¹¹ A.
- Schottky diode: between 0.25 V and 0.35 V the current rises 40 times per 0.1 V, giving η ≈ 1.05 and I_s ≈ 0.1 mA / e^{0.20/0.0272} ≈ 6×10⁻⁸ A. It reaches a given current at about 0.25–0.3 V lower voltage than the p-n diode; I_s is several orders of magnitude larger, and the reverse current is much larger (μA instead of nA).
- At high current the curves bend away from the straight line: the extra voltage is IR_s. R_s = ΔV/I where ΔV is the deviation from the extrapolated line.
- Schottky barrier height: Φ_B = (kT/q) ln(A∗∗AT²/I_s), using the diode area A from the datasheet.

**Discussion.** Explain the lower turn-on voltage and higher leakage of the Schottky diode in terms of majority-carrier thermionic emission over Φ_B versus minority-carrier diffusion (Weeks 10–11).

---

## Practical 3 — C-V profiling: doping and built-in potential

**Aim.** Measure the capacitance of a reverse-biased one-sided junction (a varactor such as BB112, or a Schottky diode) against bias, and extract the doping concentration and the built-in potential.

**Theory (Week 12).**

    C = A √( qε_sN / 2(V_bi − V) )   ⇒   1/C² = 2(V_bi − V)/(qε_sNA²)

Where:

- C = depletion capacitance (F)
- A = junction area (cm²)
- q = electronic charge, 1.6×10⁻¹⁹ C
- ε_s = permittivity of silicon, 1.04×10⁻¹² F/cm
- N = doping of the lightly doped side (cm⁻³)
- V_bi = built-in potential (V); V = applied voltage, negative in reverse bias (V)

The plot of 1/C² against V is a straight line: the slope gives N, the voltage intercept gives V_bi.

**Apparatus.** LCR meter with DC bias (1 MHz, 20–50 mV AC level), or a capacitance bridge; DC supply; shielded test fixture.

**Procedure.**

1. Null the fixture with the device removed (open-circuit correction) to remove stray capacitance.
2. Connect the diode in reverse bias. Record C at V = 0, −1, −2, … −5 V (or the device's rated range).
3. Plot C against V and 1/C² against V. Fit a straight line to 1/C².
4. Take the area A from the datasheet (or measure the contact diameter).

**Example readings** (A = 1.0×10⁻³ cm², Si):

| V (V) | C (pF) | 1/C² (F⁻²) |
|---|---|---|
| 0 | 37.2 | 7.2×10²⁰ |
| −1 | 22.8 | 1.92×10²¹ |
| −2 | 17.9 | 3.12×10²¹ |
| −3 | 15.2 | 4.33×10²¹ |
| −4 | 13.4 | 5.57×10²¹ |
| −5 | 12.2 | 6.72×10²¹ |

**Analysis.**

    Slope: (6.72×10²¹ − 7.2×10²⁰)/(−5 − 0) = −1.20×10²¹ F⁻²V⁻¹
    N = 2/(qε_sA²|slope|) = 2/(1.602×10⁻¹⁹ × 1.036×10⁻¹² × 10⁻⁶ × 1.20×10²¹) = 1.0×10¹⁶ cm⁻³
    Intercept: 1/C² = 0 at V = 7.2×10²⁰/1.20×10²¹ = +0.60 V  ⇒  V_bi = 0.60 V
    Depletion depth at −5 V: W = ε_sA/C = 1.036×10⁻¹⁵/12.2×10⁻¹² = 0.85 μm

@fig figures/cv.svg | Mott–Schottky plot of the example readings. A straight line means uniform doping; curvature would reveal a doping profile N(W).

**Discussion.** Why must the junction be one-sided? What would curvature in 1/C² tell you? Why measure in reverse bias only?

---

## Practical 4 — MOSFET parameter extraction: threshold voltage and channel mobility

**Aim.** Measure the transfer and output characteristics of an n-channel enhancement MOSFET (e.g. a CD4007 array transistor or 2N7000) and extract V_th, μ_n and the transconductance.

**Theory (Week 14).** In the linear region at small V_DS:

    I_D ≈ μ_nC_ox(W/L)[(V_GS − V_T)V_DS − V_DS²/2]

Where:

- I_D = drain current (A)
- μ_n = channel electron mobility (cm²/V·s)
- C_ox = gate-oxide capacitance per unit area (F/cm²)
- W/L = channel width-to-length ratio
- V_GS, V_DS = gate–source and drain–source voltages (V); V_T = threshold voltage (V)

so I_D against V_GS is a straight line of slope g_m = μ_nC_ox(W/L)V_DS that meets I_D = 0 at V_GS = V_T + V_DS/2. In saturation, √I_D = √(μ_nC_oxW/2L)(V_GS − V_T).

**Apparatus.** Two DC supplies (or a semiconductor parameter analyser), ammeter, voltmeters. C_ox, W and L from the datasheet or test structure.

**Procedure.**

1. **Transfer curve (linear):** set V_DS = 0.1 V. Step V_GS from 0 to 2.5 V in 0.25 V steps; record I_D.
2. **Transfer curve (saturation):** set V_DS = V_GS (gate tied to drain) and repeat; plot √I_D against V_GS.
3. **Output curves:** for V_GS = 1.0, 1.5, 2.0 V, sweep V_DS from 0 to 3 V; record I_D.
4. Find V_T by linear extrapolation at the point of maximum slope; find μ_n from the slope.

**Example readings** (linear region, V_DS = 0.1 V; device with C_ox = 3.45×10⁻⁷ F/cm², W/L = 10):

| V_GS (V) | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 |
|---|---|---|---|---|---|
| I_D (μA) | 15 | 84 | 153 | 222 | 291 |

**Analysis.**

    g_m = ΔI_D/ΔV_GS = (291 − 84) μA / 1.5 V = 1.38×10⁻⁴ S
    Line through (1.0 V, 84 μA): I_D = 0 at V_GS = 1.0 − 84/138 = 0.39 V
    V_T = 0.39 − V_DS/2 = 0.39 − 0.05 = 0.34 V
    μ_n = g_m L / (W C_ox V_DS) = 1.38×10⁻⁴ / (10 × 3.45×10⁻⁷ × 0.1) = 400 cm²/V·s

The channel mobility (400) is about a third of bulk electron mobility in Si (1350) because of surface scattering at the Si/SiO₂ interface (Week 7). At high V_GS the measured slope falls further (mobility degradation by the vertical field), so the extraction uses the maximum-slope point.

**Discussion.** Compare V_T from the linear and saturation methods. Why does mobility degrade at high gate voltage? How would a thicker oxide change V_T and g_m?

---

## Report format

For each practical: title and aim; brief theory with the equations used; circuit diagram; apparatus; procedure; tables of readings with units; graphs (labelled axes, units, fitted lines); calculations; results with uncertainties; discussion of sources of error (lead resistance, stray capacitance, self-heating, meter resolution); conclusion.
