# Week 3 — Impurity Control and Doping
<!-- group: Module 1 · Material Physics & Semiconductor Growth -->

**Plan:** diffusion and ion implantation mechanisms; controlled doping profiles and evaluation of impurity distribution. This page follows your lecturer's handwritten notes on diffusion and ion implantation, including every calculation in them.

## Learning objectives

By the end of this week you should be able to:

1. Explain why doping is needed and name the common dopants of silicon.
2. Explain diffusion and state Fick's first law and the temperature dependence of D.
3. Distinguish constant-source (erfc) and limited-source (Gaussian) diffusion and calculate their profiles.
4. Describe the step-by-step diffusion process and the atomic diffusion mechanisms.
5. Describe ion implantation, its equipment and the Gaussian implant profile.
6. Calculate implant peak concentration, junction depth, dose and beam current.
7. Compare diffusion with ion implantation, and explain channelling and annealing.
8. Describe how a doping profile is evaluated.

## Symbols and abbreviations used this week

Every symbol, constant and abbreviation on this page is listed here, even if an earlier week already defined it, so you can study this page on its own.

**Constants and units**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| q | Magnitude of the electronic charge | 1.6×10⁻¹⁹ C |
| k | Boltzmann constant | 8.617×10⁻⁵ eV/K = 1.381×10⁻²³ J/K |
| kT | Thermal energy | 0.0259 eV (often 0.02585 eV) at 300 K |
| T | Absolute temperature | kelvin (K); room temperature = 300 K |
| h | Planck constant | 6.626×10⁻³⁴ J·s |
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| μm | Micrometre (micron) | 1 μm = 10⁻⁴ cm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_c (E_C) | Energy of the bottom of the conduction band | eV |
| E_v (E_V) | Energy of the top of the valence band | eV |
| E_F | Fermi level: the energy at which a state has a 50 % chance of being occupied | eV |
| E_i | Intrinsic Fermi level, close to mid-gap | eV |
| E_D | Donor energy level, just below E_c | eV; E_c − E_D ≈ 0.045 eV for P in Si |
| E_A | Acceptor energy level, just above E_v | eV; E_A − E_v ≈ 0.045 eV for B in Si |
| E_a | Activation energy of dopant diffusion | eV; about 3–4 eV |
| n | Electron concentration (free electrons per cm³) | cm⁻³ |
| p | Hole concentration (holes per cm³) | cm⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | cm⁻³; Si ≈ 1×10¹⁰ at 300 K |
| N_D | Donor concentration | cm⁻³ |
| N_A | Acceptor concentration | cm⁻³ |
| N_D⁺, N_A⁻ | Concentrations of ionised donors and acceptors | cm⁻³ |
| C_s | Surface concentration of a diffusion (or solid concentration when freezing) | cm⁻³ |
| C(x, t) | Dopant concentration at depth x and time t | cm⁻³ |
| D | Diffusion coefficient (dopants in a furnace, or carriers) | cm²/s |
| D₀ | Diffusion constant in D = D₀e^{−E_a/kT} | cm²/s |
| J (Fick) | Dopant flux: atoms crossing 1 cm² per second | atoms/(cm²·s) |
| F | Particle flux in Fick's law | particles/(cm²·s) |
| Q | Dose: dopant atoms per unit area (in Weeks 13–14, Q also means charge) | atoms/cm² (C or C/cm² for charge) |
| Φ (dose) | Implanted dose (ions per cm²) | cm⁻² |
| erfc | Complementary error function, erfc(u) = 1 − erf(u); read from a table | dimensionless |
| x_j | Junction depth: where the dopant concentration equals the background | μm |
| N_B (C_B) | Background doping of the wafer (in Week 13, N_B is the base doping) | cm⁻³ |
| R_p | Projected range: average depth at which implanted ions stop | μm |
| ΔR_p | Straggle: spread of the implanted ions' stopping depths | μm |
| N_p | Peak concentration of an implanted profile | cm⁻³ |
| S_n, S_e | Nuclear and electronic stopping power of an implanted ion | eV·cm² |
| N_Si | Atom density of silicon | 5×10²² cm⁻³ |
| R_s | Sheet resistance (or diode series resistance in Week 12) | Ω/□ (ohms per square); Ω |
| x_mask | Thickness of an implant mask | μm |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | cm²/(V·s); Si μ_n 1350, μ_p 480 |
| σ | Conductivity, q(nμ_n + pμ_p) (in Week 8, σ is also a capture cross-section) | S/cm (siemens per cm) |
| ρ | Resistivity, 1/σ | Ω·cm |
| R | Recombination rate | cm⁻³s⁻¹ |
| L, L_n, L_p | Diffusion length √(Dτ): distance a minority carrier travels before recombining | μm or cm |
| V, V_a | Applied voltage (positive for forward bias) | V |
| W | Depletion-region width (in Week 13 W_B, W_E are base and emitter widths; in Week 14 W is channel width) | μm or cm |
| I | Current | A |
| A (area) | Device or contact area | cm² |
| N_total | Total number of dopant atoms in a region | atoms |
| B_z, I_x, V_H | Hall effect: magnetic field (z), current (x) and Hall voltage | T (tesla); A; V |
| G_n, G_p, R_n, R_p | Generation and recombination rates of electrons and holes | cm⁻³s⁻¹ |
| Q_charge | Total charge delivered by the ion beam, I × t | C |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| GaAs | Gallium arsenide |
| SiO₂ | Silicon dioxide (silica), the oxide insulator |
| RTA | Rapid thermal annealing |
| SIMS | Secondary-ion mass spectrometry |
| LDD | Lightly doped drain |
| C-V | Capacitance–voltage (measurement or characteristic) |
| MOSFET | Metal–oxide–semiconductor field-effect transistor |
| CMOS | Complementary MOS (n- and p-channel MOSFETs together) |
| BJT | Bipolar junction transistor |
| IC | Integrated circuit |
| VLSI | Very-large-scale integration |
| n⁺ | Very heavily doped n-type (similarly p⁺) |


## Key terms

Every important word used this week is defined here, so you can read this week on its own.

**Doping.** The deliberate addition of small, controlled amounts of chosen impurity atoms (called **dopants**) to a pure semiconductor in order to change how well it conducts and whether its current is carried mainly by electrons or by holes. Typical dopant levels in silicon are 10¹⁴ to 10²⁰ atoms per cm³.

*Why it matters:* pure silicon conducts far too little to be useful; every diode, transistor and integrated circuit is built from doped regions.

**Donor.** A dopant atom with one more outer (valence) electron than the silicon atom it replaces, such as phosphorus, arsenic or antimony (Group V). The spare electron is easily set free to carry current, leaving behind a fixed positive ion.

**Acceptor.** A dopant atom with one fewer valence electron than silicon, such as boron or gallium (Group III). It takes an electron from a neighbouring bond, leaving behind a fixed negative ion and a mobile empty bond called a **hole**, which behaves like a positive charge carrier.

**n-type and p-type semiconductor.** Silicon doped mainly with donors is **n-type**: most of its free carriers are electrons. Silicon doped mainly with acceptors is **p-type**: most of its free carriers are holes.

**p-n junction.** The boundary inside one crystal between a p-type region and an n-type region. It is the basic building block of diodes and transistors.

**Diffusion.** The net movement of atoms from where they are crowded (high concentration) to where they are sparse (low concentration), caused only by their random thermal jumping. In processing, dopants diffuse into a silicon wafer heated to about 900–1200 °C.

**Concentration gradient (dC/dx).** How fast the dopant concentration changes with depth. A steep gradient means a large change over a short distance. It is measured in atoms/cm⁴ (atoms per cm³, per cm).

**Fick's first law.** The rule that the flow of diffusing atoms is proportional to the concentration gradient, and runs from high to low concentration.

    J = −D dC/dx

Where:

- J = dopant flux: number of dopant atoms crossing 1 cm² each second (atoms/cm²·s)
- D = diffusion coefficient (cm²/s), defined next
- C = dopant concentration (atoms/cm³)
- x = depth into the wafer (cm)

**Diffusion coefficient (D).** A number that says how easily a dopant moves through the crystal. It rises steeply with temperature because each atomic jump needs a certain minimum energy, the **activation energy** E_a.

    D = D₀ e^{−E_a/kT}

Where:

- D = diffusion coefficient (cm²/s)
- D₀ = diffusion constant for that dopant in silicon (cm²/s)
- E_a = activation energy, about 3–4 eV for common dopants in silicon (eV)
- k = Boltzmann constant, 8.617×10⁻⁵ eV/K
- T = absolute temperature (K)

*Why it matters:* a furnace only 100 °C hotter makes dopants diffuse about ten times faster, so temperature must be controlled tightly.

**Dose (Q).** The total number of dopant atoms put into the wafer under each square centimetre of surface, in atoms/cm². It is the area under the concentration-against-depth curve.

**Predeposition (constant-source diffusion).** A diffusion in which a dopant source is present at the surface the whole time, so the surface concentration C_s stays fixed while dopant creeps deeper. It gives a complementary-error-function (erfc) profile and is used as the first doping step.

**Drive-in (limited-source diffusion).** A second heating with the source removed, so the fixed dose already in the wafer spreads deeper and the surface concentration falls. It gives a Gaussian (bell-curve) profile and is used to reach the wanted depth.

**Background doping (N_B).** The doping the wafer already had before the new dopant was added, usually of the opposite type (cm⁻³).

**Junction depth (x_j).** The depth below the surface at which the added dopant concentration has fallen to equal the background doping, so that a p-n junction forms there (μm).

    C(x_j) = N_B

*Why it matters:* the junction depth sets the size of a device; modern transistors need junctions only a few tens of nanometres deep.

**Ion implantation.** A doping method in which dopant atoms are turned into ions, accelerated by a high voltage and fired into the wafer, where they stop at a depth set by their energy. The dose is counted exactly from the beam current.

**Projected range (R_p) and straggle (ΔR_p).** The average depth at which implanted ions stop (R_p), and the spread of stopping depths about that average (ΔR_p, a standard deviation). Both are in μm and both increase with ion energy.

**Channelling.** The unwanted travel of implanted ions far deeper than R_p along open "channels" between rows of atoms in the crystal. It is avoided by tilting the wafer about 7° or covering it with a thin non-crystalline layer.

**Annealing.** Heating a wafer after implantation to repair the crystal damage caused by the ions and to move dopant atoms onto proper lattice sites, where they become electrically active.

**Sheet resistance (R_s).** The resistance of a thin doped layer measured between opposite edges of any square of it, in ohms per square (Ω/□). It shows how much dopant has been put in: more dopant, lower R_s.

    R_s = ρ / x_j

Where:

- R_s = sheet resistance (Ω/□)
- ρ = average resistivity of the layer (Ω·cm)
- x_j = thickness of the layer, the junction depth (cm)

## The big picture

A pure silicon wafer is almost useless. To make a diode, a transistor or a chip, we must put **dopant atoms** (boron, phosphorus, arsenic) into chosen parts of the wafer, in chosen amounts, down to a chosen depth. There are two ways to do this:

1. **Diffusion:** heat the wafer in an atmosphere rich in dopant. The dopant atoms creep in by themselves, the way a drop of ink spreads through water.
2. **Ion implantation:** turn the dopant atoms into ions, accelerate them with a high voltage, and fire them into the wafer like tiny bullets.

The purpose of both is the same: to change the electrical properties of the material and form the **n-type and p-type regions** needed for diodes, transistors, MOSFETs and integrated circuits.

Common dopants for silicon:

| Dopant | Symbol | Makes silicon |
|---|---|---|
| Phosphorus | P | n-type |
| Arsenic | As | n-type |
| Antimony | Sb | n-type |
| Boron | B | p-type |
| Gallium | Ga | p-type |

---

## Part A: Diffusion

### What diffusion is

**Diffusion** is the movement of dopant atoms from a region of **high concentration** to a region of **low concentration**, driven by thermal energy.

In processing, the silicon wafer is heated to a high temperature (about 900–1200 °C) and exposed to a dopant source. Dopant atoms enter the silicon surface and gradually move into the crystal.

### Why atoms move "downhill"

Your notes illustrate this with gas molecules in a box. Suppose 21 of 32 oxygen molecules start on the left side of a box. Every molecule moves randomly, left or right with equal chance. Nothing pushes them in any particular direction. But because there are more molecules on the left, **more of them happen to cross from left to right than from right to left**. The result is a net flow towards the emptier side.

- **Concentration difference:** more particles on one side (21 of 32 on the left) creates a **concentration gradient**.
- **Net diffusion:** random motion carries particles both ways, but more move from the crowded side to the less crowded side.
- **Dynamic equilibrium:** eventually both sides have similar concentrations. Particles still move randomly in both directions, but the two flows now cancel, so there is no net change.

> **In plain words.** Diffusion is not a force. It is just statistics: if you have more atoms here than there, random jumping will, on average, carry atoms from here to there. The steeper the difference, the faster the flow.

The basic process is:

    Dopant source → silicon surface → dopant penetration → desired dopant profile

### Fick's first law: how fast atoms flow

    J = −D dC/dx

| Symbol | Meaning | Unit |
|---|---|---|
| J | **dopant flux**: number of dopant atoms crossing 1 cm² each second | atoms/cm²·s |
| D | **diffusion coefficient**: how easily the dopant moves in silicon | cm²/s |
| C | dopant concentration | atoms/cm³ |
| x | distance into the semiconductor | cm |
| dC/dx | the **concentration gradient**: how fast C changes with depth | atoms/cm⁴ |

**Reading the equation.** The flow is proportional to how steeply the concentration changes. No gradient, no flow. The **minus sign** says the flow goes from high concentration towards low concentration: if C falls as x increases (dC/dx negative), J is positive, meaning atoms flow in the +x direction, deeper into the wafer.

(The J here is a flow of atoms, not an electric current. Later weeks use J for current density.)

### The diffusion coefficient depends strongly on temperature

    D = D₀ e^{−E_a/kT}

| Symbol | Meaning |
|---|---|
| D | diffusion coefficient at temperature T (cm²/s) |
| D₀ | diffusion constant (cm²/s), a property of the dopant–silicon pair |
| E_a | **activation energy** (eV): the energy barrier an atom must jump over to move one lattice site |
| k | Boltzmann constant, 8.617×10⁻⁵ eV/K |
| T | absolute temperature (K) |

Because T sits inside an exponential, **increasing temperature greatly increases the diffusion rate**. Typical E_a is 3–4 eV, so D rises about tenfold for every 50–100 °C. This is why diffusion only happens in a furnace: at room temperature D is so small that dopants do not move at all in a lifetime.

### How far do atoms travel? The diffusion length

The depth to which dopants spread grows with the **square root** of time:

    diffusion length ≈ √(Dt)

Where:

- D = diffusion coefficient of the dopant at the furnace temperature (cm²/s)
- t = diffusion time (s)
- √(Dt) = characteristic diffusion length (cm; multiply by 10⁴ for μm)

Your notes use the form **L = √(2Dt)**. Other books write 2√(Dt), which is what appears inside the erfc formula below. They are the same idea with a different constant in front. The key fact is that **depth ∝ √(Dt)**: diffusing four times as long only doubles the depth. In a calculation, use whichever form the question gives.

### Two types of diffusion

#### A. Constant-source diffusion (predeposition)

The surface of the semiconductor is kept at an approximately **constant dopant concentration C_s**, because the source (dopant gas or glass) is present all the time. The profile is:

    C(x, t) = C_s erfc( x / 2√(Dt) )

| Symbol | Meaning |
|---|---|
| C(x, t) | dopant concentration at depth x after time t (atoms/cm³) |
| C_s | surface concentration (atoms/cm³), fixed |
| x | depth |
| D | diffusion coefficient |
| t | diffusion time |
| erfc | the **complementary error function**, erfc(u) = 1 − erf(u). You read it from a table. |

**Characteristics:**

1. The dopant source remains available throughout the process.
2. The surface concentration stays approximately constant.
3. It produces an erfc concentration profile.
4. It is often used for the **initial doping step**.

**The dose put in by predeposition.** Integrating the erfc profile over all depths gives the dose introduced after time t:

    Q = 2C_s √(Dt/π) = (2/√π) C_s √(Dt)

Where:

- Q = dose: dopant atoms introduced per cm² of surface (atoms/cm²)
- C_s = fixed surface concentration (atoms/cm³)
- D = diffusion coefficient (cm²/s)
- t = predeposition time (s)

The dose grows as √t: the longer the source is left on, the more dopant enters, but ever more slowly.

**What erfc looks like.** erfc(0) = 1, so at the surface C = C_s. As the argument u = x/2√(Dt) grows, erfc falls: erfc(0.5) = 0.48, erfc(1) = 0.16, erfc(2) = 0.005, erfc(3) ≈ 2×10⁻⁵. So the concentration is highest at the surface and falls off steeply with depth. As time goes on, 2√(Dt) gets bigger, so the same depth corresponds to a smaller u, and the profile pushes deeper.

| u | erfc(u) | u | erfc(u) |
|---|---|---|---|
| 0 | 1.000 | 1.0 | 0.157 |
| 0.25 | 0.724 | 1.5 | 0.034 |
| 0.5 | 0.480 | 2.0 | 4.7×10⁻³ |
| 0.527 | 0.456 | 2.5 | 4.1×10⁻⁴ |
| 0.75 | 0.289 | 3.0 | 2.2×10⁻⁵ |

#### B. Limited-source diffusion (drive-in)

After a dopant has been introduced into the surface, the wafer is heated **without** supplying any more dopant. The fixed amount already there spreads deeper. The profile is approximately **Gaussian**:

    C(x, t) = ( Q / √(πDt) ) e^{−x²/4Dt}

| Symbol | Meaning |
|---|---|
| C(x, t) | dopant concentration at depth x after drive-in time t (atoms/cm³) |
| Q | total dopant dose per unit area (atoms/cm²), fixed |
| D | diffusion coefficient at the drive-in temperature (cm²/s) |
| t | drive-in time (s) |
| x | depth below the surface (cm) |

**Characteristics:**

1. The dopant penetrates deeper.
2. The **surface concentration decreases** (the same atoms are spread over a greater depth).
3. The total dopant quantity is approximately **conserved**.
4. It is used to obtain a desired **junction depth**.

The surface concentration is the value at x = 0, where e⁰ = 1:

    C(0, t) = Q / √(πDt)

Where:

- C(0, t) = surface concentration after drive-in time t (atoms/cm³)
- Q = dose (atoms/cm²)
- D = diffusion coefficient (cm²/s)
- t = drive-in time (s)

@fig figures/diffusion.svg | Left: constant-source (erfc) profiles at three times; the surface value stays fixed while the profile deepens. Right: limited-source (Gaussian) profiles; the area under each curve (the dose) is the same, so the surface value falls as the profile spreads.

> **In plain words.** Constant source: keep pouring ink on the surface, and the colour soaks deeper while the surface stays dark. Limited source: put one drop on, stop, and wait; the colour spreads deeper but gets paler everywhere.

### Junction depth

If the wafer was already doped with the opposite type, at background concentration N_B (for example n-type 10¹⁶ cm⁻³ and we diffuse boron in), a **p-n junction** forms at the depth x_j where the diffused concentration has fallen to equal the background:

    C(x_j) = N_B

    erfc profile:     x_j = 2√(Dt) · erfc⁻¹(N_B/C_s)
    Gaussian profile: x_j = 2√(Dt) · √( ln(C_s/N_B) )

Where:

- x_j = junction depth (cm; multiply by 10⁴ for μm)
- D = diffusion coefficient (cm²/s); t = diffusion time (s)
- N_B = background doping of the wafer (cm⁻³)
- C_s = surface concentration (cm⁻³); for the Gaussian profile this is the surface value after drive-in, Q/√(πDt)
- erfc⁻¹ = inverse complementary error function: the value u for which erfc(u) equals the number in brackets, read backwards from the erfc table

#### Example 3.1: predeposition dose and junction depth

**Question.** Boron is predeposited into n-type silicon with background doping N_B = 1×10¹⁶ cm⁻³. The surface concentration is held at C_s = 1×10²⁰ cm⁻³, D = 4×10⁻¹⁴ cm²/s and the time is 20 minutes. Find the dose introduced and the junction depth.

**Given:** C_s = 1×10²⁰ cm⁻³, N_B = 1×10¹⁶ cm⁻³, D = 4×10⁻¹⁴ cm²/s, t = 20 min = 1200 s.

**Find:** Q and x_j.

**Formula:**

    Q = 2C_s √(Dt/π),     x_j = 2√(Dt) · erfc⁻¹(N_B/C_s)

**Solution.**

Step 1. The diffusion length:

    Dt = 4×10⁻¹⁴ × 1200 = 4.8×10⁻¹¹ cm²,   √(Dt) = 6.93×10⁻⁶ cm,   2√(Dt) = 1.386×10⁻⁵ cm

Step 2. The dose:

    √(Dt/π) = √(4.8×10⁻¹¹/3.142) = 3.91×10⁻⁶ cm
    Q = 2 × 1×10²⁰ × 3.91×10⁻⁶ = 7.8×10¹⁴ atoms/cm²

Step 3. The junction is where erfc(u) = N_B/C_s = 10¹⁶/10²⁰ = 10⁻⁴. A fuller erfc table gives u = 2.75.

    x_j = 2.75 × 1.386×10⁻⁵ = 3.81×10⁻⁵ cm = 0.381 μm

**Answer:** **Q = 7.8×10¹⁴ atoms/cm², x_j = 0.38 μm.**

**What this means:** a 20-minute predeposition puts in a dose typical of a transistor base or a resistor, but only about 0.4 μm deep. To push the junction deeper without adding more dopant, the wafer is given a drive-in (Example 3.2).

#### Example 3.2: junction depth after a Gaussian drive-in

**Question.** The dose of Example 3.1 (Q = 7.8×10¹⁴ atoms/cm²) is driven in, with the boron source removed, at a higher temperature where D = 3×10⁻¹³ cm²/s, for 2 hours. The background is still N_B = 1×10¹⁶ cm⁻³. Find the new surface concentration and the junction depth.

**Given:** Q = 7.8×10¹⁴ cm⁻², D = 3×10⁻¹³ cm²/s, t = 2 h = 7200 s, N_B = 1×10¹⁶ cm⁻³.

**Find:** C(0, t) and x_j.

**Formula:**

    C(0, t) = Q / √(πDt),     x_j = 2√(Dt) · √( ln(C(0, t)/N_B) )

**Solution.**

Step 1. The Dt product:

    Dt = 3×10⁻¹³ × 7200 = 2.16×10⁻⁹ cm²

Step 2. The surface concentration:

    √(πDt) = √(6.79×10⁻⁹) = 8.24×10⁻⁵ cm
    C(0, t) = 7.8×10¹⁴ / 8.24×10⁻⁵ = 9.5×10¹⁸ cm⁻³

Step 3. The junction depth:

    2√(Dt) = 2 × 4.65×10⁻⁵ = 9.30×10⁻⁵ cm
    ln(C(0, t)/N_B) = ln(947) = 6.85,   √6.85 = 2.62
    x_j = 9.30×10⁻⁵ × 2.62 = 2.43×10⁻⁴ cm = 2.43 μm

**Answer:** **C(0) ≈ 9.5×10¹⁸ cm⁻³, x_j ≈ 2.4 μm.**

**What this means:** the same atoms now occupy a layer about six times deeper, so the surface concentration has dropped about tenfold (from 10²⁰ to under 10¹⁹ cm⁻³). This is the two-step recipe: predeposition fixes how much dopant goes in, drive-in fixes how deep it goes.

### Step-by-step diffusion process

1. **Wafer preparation.** A high-purity silicon wafer is cleaned to remove (a) dust, (b) organic contamination, (c) metallic impurities and (d) native surface oxide and contamination.
2. **Dopant source preparation.** A suitable dopant source is selected: boron for p-type, phosphorus or arsenic for n-type.
3. **Heating.** The wafer is placed in a diffusion furnace and heated to a high temperature.
4. **Dopant introduction.** The dopant is supplied to the surface of the silicon.
5. **Dopant penetration.** Thermal energy allows dopant atoms to move from the surface into the silicon lattice.
6. **Drive-in.** Additional heating may be used to drive the dopant deeper into the wafer.
7. **Cooling.** The wafer is cooled under controlled conditions.
8. **Characterisation.** The resulting dopant profile is measured to determine (1) junction depth, (2) sheet resistance, (3) dopant concentration and (4) electrical properties.

### Diffusion at the atomic level

Dopant atoms move through the silicon crystal mainly by two mechanisms:

**A. Vacancy mechanism.** A dopant atom sitting on a lattice site can only move when a neighbouring site is empty (a **vacancy**). It jumps into the vacancy:

    atom → vacancy → new lattice position

This is how the main dopants (B, P, As, Sb) move. It is slow, because it needs a vacancy to be next to the atom at the right moment.

**B. Interstitial mechanism.** A small atom moves through the **spaces between** the normal lattice positions without needing a vacancy. This is much faster. Metals such as gold, copper and iron move this way.

Some dopants use both: they move through interstitial sites, or by interactions involving both interstitials and vacancies. Which mechanism a dopant uses determines how quickly it diffuses.

### Advantages and disadvantages of diffusion

| Advantages | Disadvantages |
|---|---|
| Relatively simple process | Requires high temperature |
| Can process many wafers simultaneously | Dopants spread laterally (sideways) as well as vertically |
| Suitable for high-temperature processing | Less precise depth control |
| Good for introducing large dopant concentrations | Difficult to form extremely shallow junctions |
| Historically important in semiconductor fabrication | High-temperature exposure can affect previously fabricated structures |

---

## Diffusion calculations (from the lecture notes)

### Q1. Phosphorus is diffused into silicon with D = 2×10⁻¹³ cm²/s for t = 500 s. Find the approximate diffusion distance using L = √(2Dt).

**Given:** D = 2×10⁻¹³ cm²/s, t = 500 s. **Find:** L = √(2Dt).

**Formula:** L = √(2Dt).

**Solution.**

    L = √(2 × 2×10⁻¹³ × 500) = √(2×10⁻¹⁰) = 1.414×10⁻⁵ cm

Convert to micrometres (1 cm = 10⁴ μm):

    L = 1.414×10⁻⁵ × 10⁴ = 0.141 μm

**Answer:** **L ≈ 0.141 μm.**

**What this means:** dopants move only a fraction of a micrometre in about eight minutes, so diffusion depths are controlled on the scale of tenths of a micrometre by choosing the time and temperature.

### Q2. A dopant concentration gradient in silicon is 4×10¹⁸ cm⁻⁴ and D = 3×10⁻¹⁴ cm²/s. Find the diffusion flux using Fick's first law.

**Given:** dC/dx = 4×10¹⁸ cm⁻⁴, D = 3×10⁻¹⁴ cm²/s. **Find:** the flux J = −D dC/dx.

**Formula:** Fick's first law, J = −D dC/dx.

**Solution.**

    J = −D dC/dx = −(3×10⁻¹⁴)(4×10¹⁸) = −1.2×10⁵ atoms/cm²·s

**Answer:** **|J| = 1.2×10⁵ atoms/cm²·s.** The minus sign means the dopant moves from the region of higher concentration towards lower concentration (against the direction in which C increases).

**What this means:** about a hundred thousand atoms cross each cm² every second. That sounds a lot, but a typical dose is 10¹⁴–10¹⁵ atoms/cm², so at this rate building up a doped layer would take a very long time; real diffusions use far steeper gradients and hotter furnaces.

### Q4. Find D at T = 1273 K for a dopant with D₀ = 0.5 cm²/s and E_a = 3.5 eV.

**Given:** D₀ = 0.5 cm²/s, E_a = 3.5 eV, T = 1273 K, k = 8.617×10⁻⁵ eV/K. **Find:** D = D₀e^{−E_a/kT}.

**Formula:** D = D₀ e^{−E_a/kT}.

**Solution.**

    kT = 8.617×10⁻⁵ × 1273 = 0.1097 eV
    E_a/kT = 3.5/0.1097 = 31.90
    D = 0.5 × e^{−31.90} = 0.5 × 1.39×10⁻¹⁴ = 6.9×10⁻¹⁵ cm²/s

**Answer:** **D ≈ 6.9×10⁻¹⁵ cm²/s.** Try T = 1373 K (100 °C hotter): kT = 0.1183 eV, E_a/kT = 29.58, D = 7.1×10⁻¹⁴ cm²/s, ten times larger.

**What this means:** a 100 °C change in furnace temperature changes the diffusion rate tenfold, so a small temperature error gives a large error in junction depth. Furnace temperatures are therefore held to within about ±1 °C.

### Q5. Constant-source diffusion: C_s = 1×10²⁰ cm⁻³, D = 1×10⁻¹³ cm²/s, t = 3600 s. Find C at x = 0.2 μm.

**Given:** C_s = 1×10²⁰ cm⁻³, D = 1×10⁻¹³ cm²/s, t = 3600 s, x = 0.2 μm. **Find:** C(x, t) = C_s erfc(x/2√(Dt)).

**Formula:** C(x, t) = C_s erfc( x / 2√(Dt) ).

**Solution.**

Step 1, convert the depth: x = 0.2 μm = 2×10⁻⁵ cm.

Step 2, the diffusion length: √(Dt) = √(1×10⁻¹³ × 3600) = √(3.6×10⁻¹⁰) = 1.897×10⁻⁵ cm.

Step 3, the erfc argument:

    u = x / 2√(Dt) = 2×10⁻⁵ / (2 × 1.897×10⁻⁵) = 0.527

Step 4, from the table: erf(0.527) = 0.544, so erfc(0.527) = 1 − 0.544 = 0.456.

Step 5:

    C = C_s × erfc(u) = 1×10²⁰ × 0.456 = 4.56×10¹⁹ atoms/cm³

**Answer:** **C(0.2 μm) = 4.56×10¹⁹ cm⁻³**, a little under half the surface value.

**What this means:** after one hour the boron-rich layer is still very shallow: only 0.2 μm down, the concentration has already halved, and it keeps falling ever faster with depth.

### Q6. Drive-in: dose Q = 2×10¹⁵ atoms/cm², D = 5×10⁻¹⁴ cm²/s, t = 1000 s. Find the concentration at x = 0.

**Given:** Q = 2×10¹⁵ cm⁻², D = 5×10⁻¹⁴ cm²/s, t = 1000 s, x = 0. **Find:** C(0, t) = Q/√(πDt).

**Formula:** C(x, t) = ( Q/√(πDt) ) e^{−x²/4Dt}, which at x = 0 becomes C(0, t) = Q/√(πDt).

**Solution.**

At x = 0, e^{−0} = 1, so

    C(0, t) = Q / √(πDt)
    Dt = 5×10⁻¹⁴ × 1000 = 5×10⁻¹¹ cm²
    πDt = 1.571×10⁻¹⁰,   √(πDt) = 1.253×10⁻⁵ cm
    C(0, t) = 2×10¹⁵ / 1.253×10⁻⁵ = 1.60×10²⁰ atoms/cm³

**Answer:** **Surface concentration = 1.60×10²⁰ cm⁻³.**

**What this means:** a short drive-in leaves the dose packed close to the surface, so the surface is still very heavily doped. Longer drive-in times would lower this value as √t grows.

Why x = 0? x is the distance from the silicon surface: x = 0 is exactly at the surface; x = 0.1 μm is 0.1 μm below it; any x > 0 means below the surface. The question asks for the surface concentration, so we set x = 0 and the exponential becomes 1. (The dose is atoms per cm² because it is the total number of atoms under each square centimetre of surface.)

---

## Part B: Ion implantation

### What ion implantation is

**Ion implantation** is a doping technique in which dopant atoms are converted into **ions**, **accelerated** to high energy, and physically **injected** into the semiconductor wafer.

Unlike thermal diffusion, ion implantation allows the **dopant dose** and **implantation depth** to be controlled very precisely.

Basic flowchart:

    Dopant source → ioniser → mass analyser → accelerator → beam → wafer

**Main components:** ion source, mass analyser, acceleration system, beam focusing system, scanning system, the semiconductor wafer, and a vacuum chamber (the ions must not hit air molecules on the way).

### Step-by-step ion implantation

1. **Dopant ion generation.** A dopant-containing material (boron, phosphorus, arsenic) is introduced into an ion source, where its atoms are converted into positively charged ions.
2. **Ion extraction.** An electric field pulls the ions out of the source.
3. **Mass analysis.** The ion beam passes through a magnetic mass analyser. A magnet bends the path of each ion by an amount that depends on its **mass-to-charge ratio**, so only the wanted ion goes through the exit slit. This prevents unwanted species being implanted.
4. **Acceleration.** The selected ions are accelerated through a high electric potential. Their kinetic energy is **E = qV**, where E is the ion energy, q the ion charge and V the accelerating voltage. For a singly charged ion E = eV, so an ion accelerated through 100 kV has 100 keV.
5. **Beam focusing and scanning.** The ion beam is focused and scanned across the wafer so that the dopant is distributed uniformly.
6. **Implantation.** The energetic ions enter the silicon. As they travel through it, they collide with silicon nuclei and electrons and lose energy. Eventually they stop at a particular average depth.
7. **Annealing.** Implantation damages the crystal, because energetic ions knock silicon atoms out of place. The wafer is therefore heated (**thermal annealing**), which repairs crystal damage and moves the dopant atoms into proper lattice positions where they become electrically active.
8. **The implantation profile.** The implanted dopant normally produces an approximately **Gaussian** distribution.

### The implanted profile

    C(x) = ( Q / (√(2π) ΔR_p) ) exp[ −(x − R_p)² / (2ΔR_p²) ]

| Symbol | Meaning |
|---|---|
| C(x) | implanted dopant concentration at depth x (atoms/cm³) |
| Q | implanted dose (ions/cm²) |
| R_p | **projected range**: the average depth at which ions stop |
| ΔR_p | **straggle**: the spread of stopping depths about R_p (standard deviation) |
| x | depth |

The peak is at x = R_p, below the surface, and its height is

    N_p = Q / (√(2π) ΔR_p) ≈ 0.4 Q/ΔR_p

Where:

- N_p = peak concentration, at depth x = R_p (atoms/cm³)
- Q = implanted dose (ions/cm²)
- ΔR_p = straggle (cm: convert from μm by multiplying by 10⁻⁴)
- √(2π) = 2.507, a number from the shape of the bell curve

@fig figures/implant.svg | An implanted profile is a bell curve centred at R_p below the surface, with width set by ΔR_p. The junction forms where it falls to the background doping N_B.

> **In plain words.** Fire a million identical bullets into sand at the same speed. They do not all stop at exactly the same depth, but most stop near an average depth (R_p), with a spread (ΔR_p). That is the bell curve.

### Implantation parameters

- **Implantation dose** Q = number of implanted ions per unit area, usually expressed in **ions/cm²**.
- **Implantation energy**, usually expressed in **keV or MeV**. A higher implant energy generally produces a **deeper** implant.

The dose comes from the beam current I, the time t and the area A:

    Q = (I t)/(q A)       (singly charged ions)

Where:

- Q = dose (ions/cm²)
- I = ion beam current (A)
- t = implant time (s)
- q = charge on each ion, 1.6×10⁻¹⁹ C for a singly charged ion
- A = implanted area (cm²)

#### Example 3.3: peak concentration and junction depth of a phosphorus implant

**Question.** Phosphorus is implanted into p-type silicon (N_B = 1×10¹⁶ cm⁻³) with dose Q = 5×10¹³ cm⁻². At the chosen energy R_p = 0.12 μm and ΔR_p = 0.045 μm. Find the peak concentration, the surface concentration and the junction depth.

**Given:** Q = 5×10¹³ cm⁻², R_p = 0.12 μm, ΔR_p = 0.045 μm = 4.5×10⁻⁶ cm, N_B = 1×10¹⁶ cm⁻³.

**Find:** N_p, C(0) and x_j.

**Formula:**

    N_p = Q / (√(2π) ΔR_p),     C(x) = N_p exp[ −(x − R_p)²/(2ΔR_p²) ]
    x_j = R_p ± ΔR_p √( 2 ln(N_p/N_B) )

(The junction formula comes from setting C(x_j) = N_B, as in P2 below. The + sign gives the junction below the peak, the − sign a possible junction above it.)

**Solution.**

Step 1. Peak concentration:

    √(2π) ΔR_p = 2.507 × 4.5×10⁻⁶ = 1.128×10⁻⁵ cm
    N_p = 5×10¹³ / 1.128×10⁻⁵ = 4.43×10¹⁸ cm⁻³

Step 2. Surface concentration (x = 0):

    R_p/ΔR_p = 0.12/0.045 = 2.667,   (R_p/ΔR_p)²/2 = 3.556
    C(0) = 4.43×10¹⁸ × e^{−3.556} = 4.43×10¹⁸ × 0.0286 = 1.27×10¹⁷ cm⁻³

Step 3. Junction depth:

    N_p/N_B = 443,   ln 443 = 6.094,   √(2 × 6.094) = 3.491
    ΔR_p × 3.491 = 0.045 × 3.491 = 0.157 μm
    deep side:    x_j = 0.12 + 0.157 = 0.277 μm
    shallow side: 0.12 − 0.157 < 0, so there is no junction above the peak

**Answer:** **N_p = 4.4×10¹⁸ cm⁻³, C(0) = 1.3×10¹⁷ cm⁻³, x_j = 0.28 μm.**

**What this means:** because the surface concentration (1.3×10¹⁷ cm⁻³) is still above the background, the n-type layer runs all the way from the surface down to 0.28 μm, giving a single shallow junction. The whole layer is formed at room temperature, and only a short anneal is then needed.

### How ion implantation works inside silicon

    ion enters → collisions with atoms → loses energy → changes direction → eventually stops

There are two major energy-loss mechanisms:

**Nuclear stopping.** The implanted ion collides with silicon **nuclei**. This causes (i) deflection of the ion and (ii) displacement of silicon atoms, which is **lattice damage**. The nuclear stopping power is

    S_n = −(1/N_{Si}) (dE/dx)_nuclear

**Electronic stopping.** The ion interacts with the **electrons** in the silicon, losing energy through excitation and ionisation. At high energies electronic stopping is particularly important. It causes little damage.

    S_e = −(1/N_{Si}) (dE/dx)_electronic

Where:

- S_n, S_e = nuclear and electronic stopping power (eV·cm²)
- N_{Si} = atom density of silicon, 5×10²² cm⁻³
- (dE/dx) = rate of change of the ion's energy with distance travelled, due to collisions with nuclei or with electrons (eV/cm); it is negative because the ion slows down, so the minus sign makes S positive

Here N_{Si} is the number of silicon atoms per cm³ (5×10²² cm⁻³) and dE/dx the energy lost per unit distance. Heavy ions (As) lose energy mainly to nuclei and stop shallow; light ions (B) lose it mainly to electrons and go deeper.

### Channelling

**Channelling** occurs when ions enter the crystal along certain crystallographic directions and travel relatively deeply through open channels between rows of atoms. This produces an unexpectedly deep dopant distribution.

To reduce channelling, manufacturers may:

1. **tilt** the wafer relative to the ion beam (typically 7°);
2. **rotate** the wafer;
3. use suitable implantation conditions;
4. sometimes introduce a thin **amorphous layer** (a screen oxide, or a pre-amorphising implant) so the crystal channels are hidden.

### Advantages and limitations of ion implantation

| Advantages | Limitations |
|---|---|
| Dose known very accurately (about ±1 %) from the measured beam charge | Expensive, complex equipment that needs a high vacuum |
| Depth set by ion energy, independently of dose | Ions damage the crystal, so annealing is always needed |
| Done near room temperature, so earlier profiles are not disturbed | Channelling can give unwanted deep tails unless the wafer is tilted |
| Photoresist can be used as a mask | Wafers are processed one (or a few) at a time, so throughput is lower |
| Peak can be buried below the surface; very shallow junctions possible | Very deep junctions need very high energies (MeV), or a diffusion drive-in afterwards |

### Example: forming an n-type region both ways

Suppose we want to convert part of a silicon wafer into an n-type region.

    Using diffusion:          silicon wafer → phosphorus source → high temperature → P atoms diffuse into Si → n-type region
    Using ion implantation:   phosphorus source → P⁺ ions → mass analysis → acceleration → implantation into Si → annealing → n-type region

### Diffusion versus ion implantation

| Feature | Diffusion | Ion implantation |
|---|---|---|
| Dopant introduction | Thermal movement | Accelerated ions |
| Main driving force | Concentration gradient | Ion kinetic energy |
| Temperature | High | Relatively low (implant near room temperature) |
| Depth control | Less precise | Highly precise |
| Dose control | Moderate | Excellent |
| Crystal damage | Low | Significant |
| Annealing | Sometimes required | Normally required |
| Profile | erfc or Gaussian, maximum at the surface | Approximately Gaussian, peak below the surface |
| Modern IC use | Less dominant for shallow junctions | Widely used |
| Equipment | Diffusion furnace | Ion implanter |

---

## Ion implantation calculations (from the lecture notes)

### P1. A silicon wafer is implanted with boron, Q = 1.0×10¹³ cm⁻², R_p = 0.5 μm, ΔR_p = 0.05 μm. (a) Find the peak concentration N_p. (b) Find the boron concentration at the surface (x = 0).

**Given:** Q = 1.0×10¹³ cm⁻², R_p = 0.5 μm, ΔR_p = 0.05 μm. **Find:** (a) N_p; (b) N(0).

**Formula:** N_p = Q/(√(2π)ΔR_p) and N(x) = N_p exp[ −(x − R_p)²/(2ΔR_p²) ].

**Solution.**

(a) Convert ΔR_p = 0.05 μm = 5.0×10⁻⁶ cm.

    N_p = Q / (√(2π) ΔR_p) = 1.0×10¹³ / (2.5066 × 5.0×10⁻⁶) = 1.0×10¹³ / 1.253×10⁻⁵
        = 7.98×10¹⁷ cm⁻³

(b) At x = 0:

    N(0) = N_p exp( −R_p²/2ΔR_p² ),   R_p/ΔR_p = 0.5/0.05 = 10
    N(0) = N_p exp(−10²/2) = N_p e^{−50} = 7.98×10¹⁷ × 1.93×10⁻²² = 1.54×10⁻⁴ cm⁻³

**Answer:** **(a) N_p = 7.98×10¹⁷ cm⁻³; (b) N(0) ≈ 1.5×10⁻⁴ cm⁻³**, effectively **zero boron at the surface**.

**What this means:** the whole dose is buried in a layer around 0.5 μm deep, with undoped silicon above it. A buried profile like this is impossible with diffusion, which always peaks at the surface.

### P2. An n-type substrate with C_B = 1.0×10¹⁵ cm⁻³ is implanted with boron to form a p-type region. Peak N_p = 1.0×10¹⁷ cm⁻³ at R_p = 0.4 μm, ΔR_p = 0.05 μm. Find the junction depth x_j (where the boron concentration equals C_B).

**Given:** C_B = 1.0×10¹⁵ cm⁻³, N_p = 1.0×10¹⁷ cm⁻³, R_p = 0.4 μm, ΔR_p = 0.05 μm. **Find:** x_j where N(x_j) = C_B.

**Formula:** N(x) = N_p exp[ −(x − R_p)²/(2ΔR_p²) ], with N(x_j) = C_B.

**Solution.**

At the junction N(x_j) = C_B:

    C_B = N_p exp( −(x_j − R_p)²/2ΔR_p² )
    ln(N_p/C_B) = (x_j − R_p)²/2ΔR_p²
    x_j = R_p + ΔR_p √( 2 ln(N_p/C_B) )

Numbers: N_p/C_B = 10¹⁷/10¹⁵ = 100; ln(100) = 4.605; × 2 = 9.21; √9.21 = 3.035.

    x_j = 0.4 μm + 0.05 μm × 3.035 = 0.4 + 0.152 = 0.552 μm

**Answer:** The p-n junction is formed **0.552 μm below the silicon surface**. (There is also a second junction on the shallow side, at R_p − 0.152 = 0.248 μm, because the buried p-region has n-type silicon above it as well as below it.)

**What this means:** the implant creates a buried p-type layer only about 0.3 μm thick (0.248 to 0.552 μm), sandwiched between n-type silicon. Its position is set by the ion energy (through R_p) and its thickness by the straggle.

### P3. A 300 mm diameter wafer needs a boron dose Q = 2.0×10¹⁴ ions/cm². (a) Find the total number of ions. (b) If the implanter uses singly charged ions (q = 1.6×10⁻¹⁹ C) and processes the wafer in 60 s, what beam current is needed?

**Given:** diameter 300 mm, Q = 2.0×10¹⁴ cm⁻², q = 1.6×10⁻¹⁹ C, t = 60 s. **Find:** (a) total ions N; (b) beam current I.

**Formula:** N_total = Q × A with A = πr², and I = Q_charge/t = N_total q/t (the same as Q = It/qA rearranged).

**Solution.**

(a) Radius r = 300/2 = 150 mm = 15 cm. Area A = πr² = 3.142 × 225 = 706.9 cm².

    N_total = Q × A = 2.0×10¹⁴ × 706.9 = 1.414×10¹⁷ ions

(b) Total charge delivered = N_total × q = 1.414×10¹⁷ × 1.6×10⁻¹⁹ = 0.0226 C.

    I = Q_charge / t = 0.0226 / 60 = 3.77×10⁻⁴ A = 0.377 mA

**Answer:** **(a) N_total = 1.41×10¹⁷ ions; (b) I = 0.377 mA.**

**What this means:** a beam current of under half a milliampere is enough to dope a whole 300 mm wafer in a minute. Because the charge is measured directly, the dose is known very accurately, which is the main advantage of implantation.

### P4. A photoresist mask must protect part of a wafer during a boron implant. In photoresist R_p = 0.8 μm and ΔR_p = 0.08 μm. The substrate under the mask must receive no more than 0.1 % of the peak concentration. Find the minimum mask thickness x_mask.

**Given:** R_p = 0.8 μm, ΔR_p = 0.08 μm in resist, N(x_mask)/N_p ≤ 10⁻³. **Find:** minimum x_mask.

**Formula:** N(x)/N_p = exp[ −(x − R_p)²/(2ΔR_p²) ], set equal to 10⁻³ at x = x_mask.

**Solution.**

At the bottom of the mask the concentration must be 10⁻³ of the peak:

    N(x_mask)/N_p = exp( −(x_mask − R_p)²/2ΔR_p² ) = 10⁻³

Take logarithms. ln(10⁻³) = −3 ln 10 = −6.908. The minus signs cancel:

    (x_mask − R_p)²/2ΔR_p² = 6.908
    x_mask − R_p = ΔR_p √(2 × 6.908) = ΔR_p √13.816 = 3.717 ΔR_p
    x_mask = 0.8 + 0.08 × 3.717 = 0.8 + 0.297 = 1.097 μm

**Answer:** To keep transmission below 0.1 % the photoresist must be **at least 1.10 μm thick**.

**What this means:** the mask must be thicker than the projected range plus nearly four straggles to stop almost every ion. In real manufacturing engineers add a safety margin and use about 1.3–1.4 μm.

---

## Part C: Evaluating the impurity distribution

After doping, the engineer must check that the dose, the profile and the junction depth are what was intended (step 8 of the diffusion process). The main methods:

| Method | What it measures | How it works |
|---|---|---|
| Four-point probe | Sheet resistance R_s (Ω/□) | Pass current through the outer two of four probes in a line; measure voltage across the inner two |
| Groove-and-stain | Junction depth x_j | Grind a shallow groove, stain it (p and n regions take different colours), measure under a microscope |
| Spreading resistance profiling | Carrier concentration against depth | Step two probes down a shallow bevel, measuring resistance at each point |
| C-V profiling | Doping against depth | Capacitance of a junction against reverse bias (Week 12) |
| SIMS | All dopant atoms against depth | Sputter the surface with an ion beam and count ejected dopant ions in a mass spectrometer |
| Hall measurement | Carrier type, concentration, mobility | Hall voltage in a magnetic field (Week 7) |

### Sheet resistance, explained

A diffused layer is a thin conducting skin of thickness x_j. Its resistance is described by the **sheet resistance**:

    R_s = ρ / x_j     [ohms per square, Ω/□]

Where:

- R_s = sheet resistance (Ω/□)
- ρ = average resistivity of the doped layer (Ω·cm)
- x_j = thickness of the layer, taken as the junction depth (cm)

"Per square" means: any square piece of the layer, whatever its size, has resistance R_s between two opposite edges. (A bigger square is longer, which raises R, but also wider by the same factor, which lowers R; the two cancel.) So a resistor L long and W wide made from the layer has

    R = R_s × (L/W) = R_s × (number of squares)

Where:

- R = resistance of the resistor (Ω)
- L = length of the resistor in the direction of current flow (μm or cm)
- W = width of the resistor (same unit as L, so L/W is a pure number: the number of squares)

Measured with a four-point probe on a large thin sample:

    R_s = 4.532 × (V/I)

Where:

- V = voltage measured between the two inner probes (V)
- I = current passed through the two outer probes (A)
- 4.532 = π/ln 2, a geometry factor for equally spaced probes on a large, thin sheet

#### Example 3.4: sheet resistance from a four-point probe

**Question.** A four-point probe on a boron-diffused wafer reads V = 2.0 mV when I = 1.0 mA is passed. The junction depth is 1.0 μm. Calculate the sheet resistance of the layer and its average resistivity.

**Given:** V = 2.0 mV, I = 1.0 mA, x_j = 1.0 μm = 1.0×10⁻⁴ cm, R_s = 4.532 V/I.

**Find:** R_s and the average resistivity ρ.

**Formula:**

    R_s = 4.532 × V/I,     ρ = R_s × x_j

**Solution.**

Step 1. Sheet resistance:

    R_s = 4.532 × V/I = 4.532 × (2.0×10⁻³ / 1.0×10⁻³) = 4.532 × 2.0 = 9.06 Ω/□

Step 2. Average resistivity, from R_s = ρ/x_j:

    ρ = R_s × x_j = 9.06 × 1.0×10⁻⁴ = 9.1×10⁻⁴ Ω·cm

**Answer:** **R_s = 9.06 Ω/□, ρ ≈ 9×10⁻⁴ Ω·cm.**

**What this means:** a resistivity this low corresponds to an average boron concentration of a few times 10¹⁹ cm⁻³, a heavily doped p⁺ layer. A resistor 10 squares long made from it would have only about 91 Ω.

### Junction depth by groove and stain

A cylindrical groove of radius R is ground into the surface and stained. If the stained chord is a wide at the surface and b wide at the junction:

    x_j ≈ (a² − b²) / (8R)

Where:

- x_j = junction depth (same unit as a, b and R, usually μm)
- a = width of the groove where it cuts the wafer surface
- b = width of the groove where it cuts the junction (the edge of the stained region)
- R = radius of the grinding cylinder

---

## Key points of Week 3

- Doping puts controlled amounts of B (p-type) or P, As, Sb (n-type) into chosen regions.
- Diffusion: random thermal motion carries dopant from high to low concentration. Fick: J = −D dC/dx.
- D = D₀e^{−E_a/kT}: hotter means much faster. Depth grows as √(Dt).
- Constant source → erfc profile, fixed surface concentration. Limited source → Gaussian, fixed dose, surface concentration falls.
- Ion implantation: ions accelerated to E = qV, Gaussian profile peaked at R_p with spread ΔR_p, dose Q = It/qA, annealing required, channelling avoided by tilting.
- Junction depth is where the dopant concentration equals the background doping.
- Profiles are checked by sheet resistance, junction depth, SIMS, spreading resistance and C-V.

---

## Examination questions solved (Q14–Q21)

### Q14. What is semiconductor doping? Explain why doping is necessary in semiconductor device fabrication.

**Doping** is the intentional introduction of controlled, small quantities of specific impurity atoms into a pure (intrinsic) semiconductor to change its electrical properties. Group V donors (P, As, Sb) make silicon **n-type**; Group III acceptors (B, Al, Ga) make it **p-type**. Typical levels are 10¹⁴ to 10²⁰ cm⁻³.

**Why it is necessary:**

1. **Intrinsic conductivity is too low and uncontrolled.** Pure Si has only n_i ≈ 10¹⁰ cm⁻³ carriers, giving ρ = 1/(qn_i(μ_n + μ_p)) ≈ 3×10⁵ Ω·cm. Doping with 10¹⁶ cm⁻³ P raises n a million times, to ρ ≈ 0.5 Ω·cm.
2. **It sets the carrier type.** Devices depend on regions where electrons or holes dominate. Without n- and p-type regions there can be no p-n junction, no diode, no BJT and no MOSFET.
3. **Temperature stability.** In an extrinsic semiconductor the carrier density is fixed by N_D or N_A over a wide temperature range (the extrinsic region) instead of varying exponentially with T as n_i does.
4. **Device design.** Doping profiles set the built-in potential, depletion width, breakdown voltage, threshold voltage of MOSFETs, current gain of BJTs, sheet resistance of resistors and the quality of Ohmic contacts (heavily doped n⁺, p⁺ regions).
5. **Selective, local control.** Using masks, different areas of one chip can be given different doping, which is what makes integrated circuits possible.

### Q15. Differentiate between n-type and p-type semiconductors.

| Feature | n-type | p-type |
|---|---|---|
| Dopant added | Pentavalent (Group V): P, As, Sb | Trivalent (Group III): B, Al, Ga, In |
| Name of dopant | Donor | Acceptor |
| Effect of dopant | Donates a free electron to the conduction band | Accepts an electron, creating a hole in the valence band |
| Fixed ion left behind | Positive donor ion N_D⁺ | Negative acceptor ion N_A⁻ |
| Majority carriers | Electrons | Holes |
| Minority carriers | Holes | Electrons |
| Carrier densities | n ≈ N_D, p = n_i²/N_D | p ≈ N_A, n = n_i²/N_A |
| Impurity level | E_D just below E_c | E_A just above E_v |
| Fermi level | Above E_i, towards E_c | Below E_i, towards E_v |
| Conductivity | σ ≈ qN_Dμ_n | σ ≈ qN_Aμ_p |
| Hall coefficient | Negative | Positive |

Both remain electrically neutral overall: every free electron (or hole) is balanced by a fixed ion.

### Q16. Explain the difference between donor impurities and acceptor impurities, giving suitable examples.

**Donor impurities** have **one more** valence electron than the host atom they replace. In Si, Group V atoms such as **phosphorus, arsenic and antimony** have five valence electrons; four form covalent bonds with neighbouring Si atoms, and the fifth is bound only by about 0.04–0.05 eV. It is easily thermally released into the conduction band, leaving a positively charged, immobile donor ion. Donors introduce an energy level E_D just below the conduction band and make the material n-type.

**Acceptor impurities** have **one fewer** valence electron than the host. In Si, Group III atoms such as **boron, aluminium, gallium and indium** have three valence electrons and leave one bond incomplete. A nearby valence electron moves in with very little energy (≈ 0.045 eV for B), so the acceptor becomes a negative ion and a mobile hole is created in the valence band. Acceptors introduce a level E_A just above the valence band and make the material p-type.

| | Donor | Acceptor |
|---|---|---|
| Valence electrons (in Si) | 5 | 3 |
| Gives / takes | Gives an electron | Takes an electron (gives a hole) |
| Ionised charge | + | − |
| Level | Near E_c | Near E_v |
| Examples in Si | P, As, Sb | B, Al, Ga, In |
| Examples in GaAs | S, Se, Te (on As site); Si on Ga site | Zn, Be, Mg (on Ga site); C on As site |

### Q17. Describe the mechanism of dopant diffusion in a semiconductor.

Diffusion is the net movement of dopant atoms from a region of high concentration to one of low concentration, driven by random thermal jumps of the atoms in the lattice. At room temperature it is negligible; at 900–1200 °C (silicon) it is significant.

**Atomic mechanisms:**

1. **Vacancy (substitutional) diffusion.** Substitutional dopants (B, P, As, Sb) occupy lattice sites. A dopant can jump only when an adjacent lattice site is vacant. The rate depends on the vacancy concentration (which rises steeply with temperature) and the jump probability. High activation energy (≈ 3–4 eV), so D is small (10⁻¹⁵ to 10⁻¹² cm²/s).
2. **Interstitial diffusion.** Small atoms or those that do not bond into the lattice (Au, Cu, Fe, Na, Li, H) move between lattice sites through the open spaces of the diamond structure. Low activation energy (0.5–1.5 eV), so they diffuse many orders of magnitude faster. These are usually unwanted contaminants.
3. **Interstitialcy (kick-out) and dissociative mechanisms.** A dopant is pushed off its site by a silicon self-interstitial, travels interstitially, then returns to a substitutional site. This explains enhanced diffusion of B and P during oxidation (oxidation-enhanced diffusion).

**Temperature dependence.** D = D₀ exp(−E_a/kT), so D roughly doubles every 20–30 °C.

**Macroscopic description.** The flux obeys Fick's first law F = −D ∂C/∂x, and the profile evolves by Fick's second law ∂C/∂t = D ∂²C/∂x². In practice a two-step process is used: predeposition from a constant surface source (erfc profile) followed by drive-in of the fixed dose (Gaussian profile). Diffusion is masked by SiO₂ windows, and the dopant spreads sideways under the mask edge by about 0.8 of its depth (lateral diffusion).

### Q18. State and explain Fick's first and second laws of diffusion.

**Fick's first law.** The diffusion flux is proportional to the negative of the concentration gradient:

    F = −D ∂C/∂x

- F: number of atoms crossing unit area per unit time (cm⁻²s⁻¹).
- C(x, t): impurity concentration (cm⁻³).
- D: diffusion coefficient (cm²/s), D = D₀exp(−E_a/kT).
- The minus sign: atoms move from high to low concentration. If there is no gradient, there is no net flux.

It describes the flux at one instant but not how the profile changes.

**Fick's second law.** Consider a thin slice of thickness dx. Atoms entering minus atoms leaving equals the increase stored (continuity, no generation or loss):

    ∂C/∂t = −∂F/∂x

Substituting the first law (with D constant):

    ∂C/∂t = D ∂²C/∂x²

This is the diffusion equation. It says the concentration rises where the profile is curved upward (concave) and falls where it is curved downward, so diffusion always smooths the profile. Its solutions, set by the boundary conditions, are the complementary-error-function profile (constant surface source) and the Gaussian profile (fixed dose) described in Part A above.

### Q19. A semiconductor is doped by diffusion with a constant surface concentration of 1 × 10²⁰ cm⁻³. Explain how the impurity concentration varies with depth.

A constant surface concentration is the **predeposition** (unlimited source) case. Solve Fick's second law with:

- C(0, t) = C_s = 1×10²⁰ cm⁻³ (held fixed for all t)
- C(∞, t) = 0 (deep in the wafer)
- C(x, 0) = 0 (no dopant at the start)

The solution is the **complementary error function**:

    C(x, t) = C_s erfc( x / 2√(Dt) ) = 1×10²⁰ · erfc( x / 2√(Dt) )   cm⁻³

**How it varies with depth:**

1. At the surface (x = 0), erfc(0) = 1, so C = 1×10²⁰ cm⁻³, independent of time.
2. The concentration **decreases monotonically** with depth. Near the surface it falls almost linearly; deeper it falls faster than exponentially, because erfc(u) ≈ e^{−u²}/(u√π) for large u.
3. The depth scale is the diffusion length 2√(Dt). At x = 2√(Dt), erfc(1) = 0.157, so C = 1.57×10¹⁹ cm⁻³. At x = 4√(Dt), erfc(2) = 4.7×10⁻³, so C = 4.7×10¹⁷ cm⁻³.
4. As time increases, the profile penetrates deeper (as √t) while the surface stays at 10²⁰ cm⁻³, so the total dose grows: Q = (2/√π)C_s√(Dt).
5. If the wafer has background doping N_B of the opposite type, a junction forms where C(x_j) = N_B.

**Worked illustration** (assume boron into n-Si with N_B = 1×10¹⁶ cm⁻³, D = 1×10⁻¹³ cm²/s at about 1100 °C, t = 1 h = 3600 s):

    √(Dt) = √(1×10⁻¹³ × 3600) = 1.90×10⁻⁵ cm = 0.190 μm
    2√(Dt) = 0.379 μm

    Junction: erfc(u) = N_B/C_s = 10¹⁶/10²⁰ = 10⁻⁴  ⇒  u ≈ 2.75
    x_j = 2.75 × 0.379 μm ≈ 1.04 μm

    Dose: Q = (2/√π)(1×10²⁰)(1.90×10⁻⁵) = 2.14×10¹⁵ atoms/cm²

| Depth x (μm) | u = x/2√(Dt) | erfc(u) | C (cm⁻³) |
|---|---|---|---|
| 0 | 0 | 1 | 1.0×10²⁰ |
| 0.19 | 0.5 | 0.480 | 4.8×10¹⁹ |
| 0.38 | 1.0 | 0.157 | 1.6×10¹⁹ |
| 0.57 | 1.5 | 0.034 | 3.4×10¹⁸ |
| 0.76 | 2.0 | 4.7×10⁻³ | 4.7×10¹⁷ |
| 1.04 | 2.75 | 1.0×10⁻⁴ | 1.0×10¹⁶ (junction) |

So the impurity concentration is highest at the surface and falls off as an erfc curve, reaching the background doping about 1 μm below the surface for these conditions.

### Q20. Explain the principle of ion implantation and identify its major advantages over thermal diffusion.

**Principle.** Ion implantation introduces dopant atoms into a semiconductor by bombarding it with a beam of energetic dopant ions. The dopant is ionised in an ion source, the ions are extracted, selected by mass in a magnetic analyser, accelerated to an energy of a few keV to MeV and scanned uniformly across the wafer. Each ion penetrates the crystal, losing energy by nuclear and electronic collisions, and stops at a depth that depends on its energy and mass. The resulting distribution is approximately Gaussian, peaking at the projected range R_p with straggle ΔR_p. The dose is measured exactly by integrating the beam current in a Faraday cup (Φ = It/qA). Because the impact damages the lattice and leaves dopants on non-lattice sites, the wafer is then annealed (furnace or RTA) to repair the damage and electrically activate the dopants.

**Advantages over thermal diffusion:**

1. **Precise, reproducible dose control** (±1 % or better) over a very wide range, 10¹¹ to 10¹⁶ cm⁻², by measuring charge. Diffusion dose depends on solid solubility, time and temperature and is much less accurate.
2. **Independent control of depth and dose.** Depth is set by energy, dose by charge. In diffusion both depend on the same Dt product.
3. **Low-temperature process.** Implantation is done near room temperature; only a short anneal is needed. Existing profiles are not disturbed and the thermal budget is small, which is vital for shallow junctions.
4. **Wide choice of masks**, including photoresist, which diffusion cannot use.
5. **Buried and retrograde profiles.** The peak can be placed below the surface (e.g. retrograde wells, buried layers); diffusion always peaks at the surface.
6. **Very shallow junctions** with low-energy implants.
7. **Less lateral spread** under the mask edge, allowing smaller devices and self-aligned structures.
8. **Purity.** Mass separation guarantees only the chosen species is implanted.
9. **Not limited by solid solubility**: concentrations above solubility can be obtained (though not all are activated).
10. **Uniformity** across large wafers, and the process is clean (vacuum, dry).

### Q21. Compare diffusion and ion implantation as semiconductor doping techniques.

| Feature | Thermal diffusion | Ion implantation |
|---|---|---|
| Principle | Dopant moves in from a surface source by random thermal jumps (Fick's laws) | Energetic ions are driven into the crystal and stop by collisions |
| Process temperature | High, 900–1200 °C | Room temperature, plus anneal (RTA ≈ 1000 °C for seconds) |
| Profile shape | erfc or Gaussian, always maximum at the surface | Gaussian peaking at R_p below the surface; buried and retrograde profiles possible |
| Dose control | Limited (± 5–10 %), set by solubility, T and t | Excellent (± 1 %), set by measured charge |
| Depth control | Coupled to dose through Dt | Independent: set by energy |
| Junction depth | Relatively deep; hard to make very shallow junctions | Very shallow junctions possible |
| Lateral spread | Large (≈ 0.8 × depth) | Small (≈ straggle) |
| Masking | SiO₂, Si₃N₄ (must survive high T) | Photoresist, oxide, nitride, polysilicon |
| Lattice damage | None | Significant; needs annealing; amorphisation at high dose |
| Channelling | Not applicable | Must be avoided (7° tilt, screen oxide) |
| Throughput and cost | Batch of 100+ wafers, cheap equipment | Single wafer or small batch, expensive equipment |
| Purity | Depends on source and furnace cleanliness | Mass-analysed, very pure |
| Concentration limit | Limited by solid solubility | Can exceed solubility |
| Typical use today | Drive-in, deep wells, solar cells, emitter diffusion in older processes | Source/drain, threshold-adjust, wells, LDD, channel stops in all modern CMOS |

**Summary:** diffusion is simple, cheap and damage-free but gives coarse, coupled control of dose and depth and needs high temperature. Ion implantation gives precise, independent, low-temperature control of dose and depth and is the standard technique for modern VLSI, at the cost of expensive equipment and lattice damage that must be annealed. In practice the two are often combined: implant to set the dose, then a thermal drive-in to set the depth.

---

## Practice questions

These extra questions practise this week's ideas. Work each one on paper before reading the solution; the calculation questions follow the same Question, Given, Find, Solution, Answer layout as the worked examples.

#### Practice 3.1: how far does boron move?

**Question.** Boron diffuses in silicon with D = 1×10⁻¹⁴ cm²/s. Find the characteristic diffusion length √(Dt) after 2 hours, and the scale length 2√(Dt) used in the erfc profile.

**Given:** D = 1×10⁻¹⁴ cm²/s, t = 2 h = 7200 s.

**Find:** √(Dt) and 2√(Dt).

**Solution.**

    √(Dt) = √(1×10⁻¹⁴ × 7200) = √(7.2×10⁻¹¹) = 8.49×10⁻⁶ cm = 0.085 μm
    2√(Dt) = 0.17 μm

**Answer:** **√(Dt) = 0.085 μm, 2√(Dt) = 0.17 μm.**

#### Practice 3.2: predeposition junction depth and dose

**Question.** Boron is predeposited into n-type silicon (N_B = 1×10¹⁷ cm⁻³) from a constant source with C_s = 1×10²⁰ cm⁻³, D = 5×10⁻¹⁴ cm²/s, for 30 minutes. Find the junction depth and the dose introduced.

**Given:** C_s = 10²⁰ cm⁻³, N_B = 10¹⁷ cm⁻³, D = 5×10⁻¹⁴ cm²/s, t = 1800 s.

**Find:** x_j and Q.

**Solution.**

    √(Dt) = √(5×10⁻¹⁴ × 1800) = 9.49×10⁻⁶ cm,   2√(Dt) = 1.90×10⁻⁵ cm
    erfc(u) = N_B/C_s = 10⁻³   ⇒   u = 2.33 (from erfc tables)
    x_j = u × 2√(Dt) = 2.33 × 1.90×10⁻⁵ = 4.4×10⁻⁵ cm = 0.44 μm
    Q = (2/√π) C_s √(Dt) = 1.128 × 10²⁰ × 9.49×10⁻⁶ = 1.07×10¹⁵ cm⁻²

**Answer:** **x_j = 0.44 μm, Q = 1.07×10¹⁵ cm⁻².**

#### Practice 3.3: driving in the dose

**Question.** The dose of Practice 3.2 is driven in, with no further source, at D = 1×10⁻¹³ cm²/s for 1 hour. Find the new surface concentration and junction depth (N_B = 1×10¹⁷ cm⁻³).

**Given:** Q = 1.07×10¹⁵ cm⁻², D = 10⁻¹³ cm²/s, t = 3600 s, N_B = 10¹⁷ cm⁻³.

**Find:** C(0) and x_j.

**Solution.**

    √(πDt) = √(π × 3.6×10⁻¹⁰) = 3.36×10⁻⁵ cm
    C(0) = Q/√(πDt) = 1.07×10¹⁵ / 3.36×10⁻⁵ = 3.2×10¹⁹ cm⁻³
    2√(Dt) = 2√(3.6×10⁻¹⁰) = 3.79×10⁻⁵ cm
    x_j = 2√(Dt) √(ln(C(0)/N_B)) = 3.79×10⁻⁵ × √(ln 318) = 3.79×10⁻⁵ × 2.40 = 9.1×10⁻⁵ cm

**Answer:** **C(0) = 3.2×10¹⁹ cm⁻³ (down from 10²⁰), x_j = 0.91 μm (up from 0.44 μm).** Drive-in trades surface concentration for depth.

#### Practice 3.4: dose from beam current

**Question.** An implanter delivers a singly charged boron beam of 50 μA for 200 s, uniformly over a 150 mm wafer. What dose is implanted?

**Given:** I = 50×10⁻⁶ A, t = 200 s, r = 7.5 cm, q = 1.6×10⁻¹⁹ C.

**Find:** Q (ions/cm²).

**Solution.**

    A = π × 7.5² = 176.7 cm²
    Q = It/(qA) = (50×10⁻⁶ × 200)/(1.6×10⁻¹⁹ × 176.7) = 10⁻²/2.83×10⁻¹⁷ = 3.5×10¹⁴ cm⁻²

**Answer:** **Q = 3.5×10¹⁴ ions/cm².**

#### Practice 3.5: shallow implanted junction

**Question.** Arsenic is implanted into p-type silicon (N_B = 1×10¹⁶ cm⁻³) with Q = 5×10¹⁴ cm⁻², R_p = 0.10 μm and ΔR_p = 0.03 μm. Find the peak concentration and the depth of the junction below the peak.

**Given:** Q = 5×10¹⁴ cm⁻², R_p = 0.10 μm, ΔR_p = 0.03 μm = 3×10⁻⁶ cm, N_B = 10¹⁶ cm⁻³.

**Find:** N_p and x_j.

**Solution.**

    N_p = Q/(√(2π)ΔR_p) = 5×10¹⁴ / (2.507 × 3×10⁻⁶) = 6.6×10¹⁹ cm⁻³
    x_j = R_p + ΔR_p √(2 ln(N_p/N_B)) = 0.10 + 0.03 × √(2 ln 6650) = 0.10 + 0.03 × 4.20 = 0.226 μm

**Answer:** **N_p = 6.6×10¹⁹ cm⁻³, x_j = 0.23 μm.** (Here the surface concentration is high enough that the n⁺ region reaches the surface, so there is only the one junction.)

#### Practice 3.6: diffusion coefficient of phosphorus

**Question.** For phosphorus in silicon D₀ = 3.85 cm²/s and E_a = 3.66 eV. Find D at 1100 °C.

**Given:** D₀ = 3.85 cm²/s, E_a = 3.66 eV, T = 1373 K, k = 8.617×10⁻⁵ eV/K.

**Find:** D.

**Solution.**

    kT = 8.617×10⁻⁵ × 1373 = 0.1183 eV
    E_a/kT = 3.66/0.1183 = 30.93
    D = 3.85 × e^{−30.93} = 3.85 × 3.7×10⁻¹⁴ = 1.4×10⁻¹³ cm²/s

**Answer:** **D ≈ 1.4×10⁻¹³ cm²/s.**

#### Practice 3.7: annealing and tilt

**Question.** Give two reasons an implanted wafer must be annealed, and explain why implants are usually done with the wafer tilted by about 7°.

**Answer.** Annealing (1) repairs the lattice damage caused by the ions knocking silicon atoms out of place (heavy implants even make the surface amorphous), and (2) moves the dopant atoms onto substitutional lattice sites where they become electrically active donors or acceptors. Tilting by about 7° stops the beam lining up with the open channels between rows of atoms along low-index directions; ions entering a channel travel much deeper than R_p predicts (channelling), giving an unwanted deep tail.

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Explain why doping is needed and name the common dopants of silicon. | Which of P, B, As, Ga make silicon n-type? | P and As (Group V); B and Ga make it p-type. | The big picture |
| 2 | Explain diffusion and state Fick's first law and the temperature dependence of D. | By roughly what factor does D change when the furnace is 100 °C hotter (E_a ≈ 3.5 eV, ~1000 °C)? | About tenfold (Q4: 6.9×10⁻¹⁵ → 7.1×10⁻¹⁴ cm²/s). | Part A; Q4 |
| 3 | Distinguish constant-source (erfc) and limited-source (Gaussian) diffusion and calculate their profiles. | In which type of diffusion does the surface concentration fall with time? | Limited-source (drive-in): the fixed dose spreads deeper, so C(0) = Q/√(πDt) falls. | Two types of diffusion; Examples 3.1–3.2; Q5–Q6 |
| 4 | Describe the step-by-step diffusion process and the atomic diffusion mechanisms. | Which mechanism, vacancy or interstitial, is faster, and which do B and P use? | Interstitial is faster; B and P move mainly by the vacancy mechanism. | Step-by-step process; atomic level |
| 5 | Describe ion implantation, its equipment and the Gaussian implant profile. | What does the mass analyser do? | Bends the ion beam with a magnet so only ions of the chosen mass-to-charge ratio reach the wafer. | Part B |
| 6 | Calculate implant peak concentration, junction depth, dose and beam current. | Q = 10¹⁴ cm⁻² with ΔR_p = 0.04 μm: find N_p. | N_p = Q/(√(2π)ΔR_p) = 10¹⁴/(2.507 × 4×10⁻⁶) = 1.0×10¹⁹ cm⁻³. | Example 3.3; implantation calculations P1–P4 |
| 7 | Compare diffusion with ion implantation, and explain channelling and annealing. | Why is the wafer tilted about 7° during implantation? | To stop ions travelling deep along open crystal channels (channelling). | Channelling; comparison table |
| 8 | Describe how a doping profile is evaluated. | What does a four-point probe measure, and how is it calculated? | Sheet resistance, R_s = 4.532 V/I (Ω/□). | Part C; Example 3.4 |
