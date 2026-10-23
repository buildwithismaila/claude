# Week 11 — Metal–Semiconductor Interfaces
<!-- group: Module 4 · Junctions, Interfaces & Characterisation -->

**Plan:** Schottky barrier diode physics versus Ohmic contact mechanisms; energy band diagrams under equilibrium and bias.

## Learning objectives

By the end of this week you should be able to:

1. Define work function and electron affinity and relate them.
2. Explain how a Schottky barrier forms and calculate Φ_B and V_bi.
3. Explain thermionic emission and calculate Schottky diode currents.
4. Draw Schottky band diagrams in equilibrium and under bias.
5. Explain the two ways of making Ohmic contacts.
6. Describe the stability problems of metal contacts.
7. Compare Schottky and ohmic contacts, their advantages, limitations and applications.

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
| ε₀ | Permittivity of free space | 8.854×10⁻¹⁴ F/cm |
| ε_s (ε_si) | Permittivity of silicon, 11.7ε₀ | 1.04×10⁻¹² F/cm |
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| μm | Micrometre (micron) | 1 μm = 10⁻⁴ cm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_c (E_C) | Energy of the bottom of the conduction band | eV |
| E_v (E_V) | Energy of the top of the valence band | eV |
| E_g | Band-gap energy, E_c − E_v | eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K |
| E_F | Fermi level: the energy at which a state has a 50 % chance of being occupied | eV |
| N_c | Effective density of states in the conduction band | cm⁻³; Si 2.8×10¹⁹ at 300 K |
| N_D | Donor concentration | cm⁻³ |
| N_A | Acceptor concentration | cm⁻³ |
| Q | Dose: dopant atoms per unit area (in Weeks 13–14, Q also means charge) | atoms/cm² (C or C/cm² for charge) |
| E (field) | Electric field (on band diagrams, E is energy instead) | V/cm |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | cm²/(V·s); Si μ_n 1350, μ_p 480 |
| τ, τ_n, τ_p | Minority-carrier lifetime (τ_eff: effective, including surfaces) | s; Si 1 ns – 1 ms |
| V_bi | Built-in potential of a junction or Schottky contact | V; typically 0.5–1 V |
| V, V_a | Applied voltage (positive for forward bias) | V |
| W | Depletion-region width (in Week 13 W_B, W_E are base and emitter widths; in Week 14 W is channel width) | μm or cm |
| E_max | Peak electric field, at the junction | V/cm |
| I_s, J_s (I_S) | Saturation current (density) of a diode or transistor | A; A/cm² |
| I | Current | A |
| A (area) | Device or contact area | cm² |
| η | Ideality factor of a diode, 1 (ideal) to 2 | dimensionless |
| Φ_m | Work function of a metal | eV; Al 4.28, Au 5.1 |
| Φ_s | Work function of a semiconductor, χ + (E_c − E_F) | eV |
| χ | Electron affinity: energy from E_c up to the vacuum level | eV; Si 4.05 |
| Φ_B | Schottky barrier height seen from the metal | eV (or V) |
| A∗∗ | Effective Richardson constant | A/(cm²·K²); n-Si ≈ 110 |
| ρ_c | Specific contact resistance | Ω·cm² |
| E_vac | Vacuum level: energy of an electron just free of the material | eV |
| R_c | Contact resistance | Ω (specific: Ω·cm²) |
| Φ_Bn, Φ_Bp | Schottky barrier height for electrons (n-type) and for holes (p-type) | eV |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| Ge | Germanium |
| GaAs | Gallium arsenide |
| SiO₂ | Silicon dioxide (silica), the oxide insulator |
| I-V | Current–voltage (measurement or characteristic) |
| MESFET | Metal–semiconductor field-effect transistor |
| IC | Integrated circuit |
| RF | Radio frequency |
| n⁺ | Very heavily doped n-type (similarly p⁺) |


## Key terms

Every important word used this week is defined here, so you can read this week on its own.

**Metal.** A material with a very large number of free electrons (about 10²² cm⁻³), so it conducts electricity very easily. Its electron states are filled up to the Fermi level, and there are empty states immediately above it. Examples: aluminium, gold, platinum, titanium, tungsten.

**Semiconductor.** A material whose conductivity lies between a metal's and an insulator's, and can be controlled by doping, temperature, light and electric fields. Examples: silicon (Si), germanium (Ge), gallium arsenide (GaAs).

**Doping; n-type and p-type.** Doping is adding a small, controlled amount of impurity atoms to a semiconductor. Donor atoms (e.g. phosphorus in Si, concentration N_D) give free electrons and make it **n-type**. Acceptor atoms (e.g. boron, concentration N_A) create holes and make it **p-type**.

**Majority and minority carriers.** The carrier that is in the majority: electrons in n-type material, holes in p-type. The other carrier is the minority carrier. A Schottky diode works with majority carriers only.

**Conduction band edge (E_c) and valence band edge (E_v).** E_c is the lowest energy a free electron can have in the semiconductor. E_v is the highest energy of the (almost full) valence band, where holes live.

**Band gap (E_g).** The energy gap between the conduction and valence bands, in which electrons cannot sit.

    E_g = E_c − E_v

Where:

- E_g = band-gap energy (eV); 1.12 eV for Si at 300 K
- E_c = conduction-band edge (eV)
- E_v = valence-band edge (eV)

**Fermi level (E_F).** The energy at which a state has a 50 % chance of being occupied by an electron. It marks how "full" a material is with electrons. In n-type material it lies near E_c, in p-type near E_v. **At equilibrium the Fermi level is flat (the same everywhere) across any set of materials in contact.** For n-type silicon:

    E_c − E_F = kT ln(N_c/N_D)

Where:

- kT = thermal energy, 0.0259 eV at 300 K (0.02585 eV is used in this week's calculations)
- N_c = effective density of states in the conduction band, 2.8×10¹⁹ cm⁻³ for Si
- N_D = donor concentration (cm⁻³)

*Why it matters:* the Fermi level sets the semiconductor's work function, and lining up the two Fermi levels is what bends the bands at a contact.

**Vacuum level (E_vac).** The energy of an electron at rest just outside the material, free of it. Every other energy this week is measured down from this level.

**Work function (Φ).** The minimum energy needed to remove an electron from the Fermi level and take it to the vacuum level. Φ_m is the metal's work function, Φ_s the semiconductor's.

    Φ_m = E_vac − E_{F,m},     Φ_s = E_vac − E_{F,s}

Where:

- Φ_m, Φ_s = work functions of the metal and of the semiconductor (eV)
- E_{F,m}, E_{F,s} = Fermi levels of the metal and of the semiconductor (eV)

Metal values (eV): Al 4.28, Ti 4.33, Cr 4.5, W 4.55, Au 5.1, Ni 5.15, Pt 5.65.

*Why it matters:* the sign of Φ_m − Φ_s decides whether a contact is rectifying or ohmic.

**Electron affinity (χ).** The energy from the bottom of the conduction band up to the vacuum level. Unlike Φ_s, it does not change with doping, so it is a fixed property of the material: Si 4.05 eV, GaAs 4.07 eV, Ge 4.0 eV.

    χ = E_vac − E_c

**Metal–semiconductor contact (interface).** The boundary formed where a metal touches a semiconductor. Every device has several, because every device must be wired to the circuit with metal.

**Schottky contact (Schottky barrier).** A metal–semiconductor contact that has an energy barrier to majority carriers, so it **rectifies**: current flows easily in one direction and hardly at all in the other. A diode made this way is a **Schottky barrier diode (SBD)**.

**Ohmic contact.** A metal–semiconductor contact with no significant barrier, so current flows equally easily in both directions and the I-V graph is a straight line through the origin (V = IR_c). Its job is to connect a device to the circuit while adding almost no resistance.

**Rectifying.** Conducting much better in one direction (forward bias) than the other (reverse bias).

**Schottky barrier height (Φ_B).** The height of the barrier an electron in the metal must climb to enter the semiconductor. It is fixed by the interface and does not change with bias.

**Depletion region (width W).** A layer next to the interface emptied of free carriers, leaving only the fixed, charged dopant ions (positive donor ions in n-type). Those charges create an electric field and a voltage across the layer.

**Built-in potential (V_bi).** The voltage across the depletion region at equilibrium; the barrier an electron in the semiconductor must climb to reach the metal.

**Band bending.** The upward or downward curving of E_c and E_v near the interface, caused by the voltage across the depletion (or accumulation) region. Upward bending in n-type = a barrier to electrons.

**Accumulation layer.** A thin layer at the interface with **extra** majority carriers (the opposite of depletion). The bands bend downward in n-type, and there is no barrier.

**Forward bias and reverse bias.** For a metal on n-type: forward bias makes the metal positive with respect to the semiconductor (current flows easily); reverse bias makes the metal negative (only a small current flows).

**Thermionic emission.** Current carried by carriers that have enough thermal energy to jump **over** a barrier. It is how current flows in a Schottky diode.

**Tunnelling (field emission).** A quantum effect: an electron passes **through** a barrier that is thin enough (a few nanometres) without having the energy to go over it. It is how most practical ohmic contacts work.

**Saturation current (I_s, J_s) and ideality factor (η).** I_s is the small current that flows under reverse bias; J_s is the same per unit area. The ideality factor η (1 for an ideal diode, 1.0–1.1 for a good Schottky diode) measures how closely a real diode follows the ideal equation.

**Fermi-level pinning.** At a real interface, defects and surface states hold ("pin") the Fermi level near a fixed energy, so the measured barrier height depends much less on the metal than the ideal rule predicts.

**Specific contact resistance (ρ_c).** The resistance of a contact multiplied by its area, in Ω·cm². It lets contacts of different sizes be compared. Good ohmic contacts have ρ_c ≈ 10⁻⁶–10⁻⁸ Ω·cm².

## The big picture

Every device must be wired to the outside world with metal. You might expect a metal touching a semiconductor to behave like a simple wire connection. Sometimes it does: that is an **ohmic contact**, which lets current through equally well in both directions. But sometimes the contact itself forms a **barrier** and conducts in only one direction, like a diode: a **Schottky contact**.

Which one you get depends on the metal, the semiconductor and its doping. Engineers want ohmic contacts for wiring, and Schottky contacts when they want a very fast diode. A real Schottky diode has **both**: a Schottky contact on top that does the rectifying and an ohmic contact underneath that lets the current out.

@fig figures/schottky-device.svg | A Schottky diode in cross-section. The metal anode sits on a lightly doped n-type layer: this is the rectifying Schottky contact, with its depletion region under the metal. The n-type layer is grown on a heavily doped n⁺ substrate whose metal back contact is ohmic. The oxide (SiO₂) ring insulates the edges of the metal.

This week explains both contacts with **energy band diagrams**, using one rule: at equilibrium the Fermi level is flat.

## The energies before contact

Before the metal and semiconductor touch, each has its own Fermi level, and we compare them by measuring everything down from the common vacuum level.

@fig figures/ms-before.svg | A metal and an n-type semiconductor before contact. The metal's Fermi level is qΦ_m below the vacuum level. In the semiconductor the conduction band edge is qχ below the vacuum level and the Fermi level qΦ_s below it. When Φ_m > Φ_s, the semiconductor's Fermi level is higher by q(Φ_m − Φ_s), so electrons will flow from the semiconductor into the metal on contact.

The semiconductor's work function is the electron affinity plus the gap between E_c and E_F:

    Φ_s = χ + (E_c − E_F)

Where:

- Φ_s = work function of the semiconductor (eV)
- χ = electron affinity (eV); 4.05 eV for Si
- E_c − E_F = how far the Fermi level lies below the conduction band edge (eV); it shrinks as N_D increases

#### Example 11.1: work function of doped silicon

**Question.** Calculate the work function of n-type silicon doped with N_D = 1×10¹⁶ cm⁻³ at 300 K. The electron affinity of Si is 4.05 eV.

**Given:** χ = 4.05 eV, N_D = 1×10¹⁶ cm⁻³, N_c = 2.8×10¹⁹ cm⁻³, kT = 0.02585 eV.

**Find:** Φ_s.

**Formula:** E_c − E_F = kT ln(N_c/N_D), then Φ_s = χ + (E_c − E_F).

**Solution.**

Step 1. Position of E_F below E_c:

    E_c − E_F = 0.02585 × ln(2.8×10¹⁹ / 1×10¹⁶) = 0.02585 × 7.94 = 0.205 eV

Step 2. Work function:

    Φ_s = 4.05 + 0.205 = 4.26 eV

**Answer:** **Φ_s = 4.26 eV.**

**What this means:** any metal with Φ_m above 4.26 eV (gold, nickel, platinum) will tend to form a barrier on this silicon; a metal below it would not.

## The Schottky barrier (rectifying contact)

### How it forms: metal on n-type with Φ_m > Φ_s

1. **Before contact**, the semiconductor's Fermi level is **higher** than the metal's by Φ_m − Φ_s (figure above).
2. **On contact**, electrons flow "downhill" from the semiconductor into the metal.
3. The electrons that leave uncover **positive donor ions** near the interface in the semiconductor. These ions cannot move, so a **depletion region** forms. A thin sheet of extra electrons sits on the metal surface.
4. The positive ions and the negative sheet create an **electric field** in the depletion region, pointing from the semiconductor towards the metal.
5. The field makes the semiconductor's bands **bend upward** towards the interface.
6. The flow stops when the two **Fermi levels line up**: one flat E_F through the whole structure. Now the upward bend is a barrier that holds back further electron flow.

@fig figures/schottky.svg | Metal on n-type silicon (Φ_m > Φ_s) after contact. An electron in the metal sees the barrier qΦ_B. An electron in the semiconductor sees the smaller built-in barrier qV_bi.

There are now **two barriers**, depending on which side the electron starts from:

    seen from the metal (barrier height):       Φ_B = Φ_m − χ       (the ideal Schottky–Mott rule)
    seen from the semiconductor (built-in):    V_bi = Φ_m − Φ_s = Φ_B − (E_c − E_F)/q

Where:

- Φ_B = Schottky barrier height for electrons (eV, or V when divided by q)
- Φ_m = metal work function (eV); χ = electron affinity (eV); Φ_s = semiconductor work function (eV)
- V_bi = built-in potential (V); with energies in eV, the number in eV equals the voltage in V

For a **p-type** semiconductor everything flips: a rectifying contact needs Φ_m < Φ_s, and the barrier for holes is

    Φ_{Bp} = E_g − (Φ_m − χ) = E_g − Φ_B

Where Φ_{Bp} = hole barrier height (eV) and E_g = band gap (eV). For example, aluminium on p-Si: Φ_{Bp} = 1.12 − (4.28 − 4.05) = 0.89 eV.

#### Example 11.2: ideal Schottky barrier

**Question.** Gold (Φ_m = 5.1 eV) is deposited on the n-type silicon of Example 11.1. Using the ideal Schottky–Mott model, find the barrier height seen from the metal and the built-in potential seen from the semiconductor. Is the contact rectifying or ohmic?

**Given:** Φ_m = 5.1 eV, χ = 4.05 eV, Φ_s = 4.26 eV.

**Find:** Φ_B, V_bi, and the type of contact.

**Formula:** Φ_B = Φ_m − χ;  V_bi = Φ_m − Φ_s.

**Solution.**

    Φ_B = 5.1 − 4.05 = 1.05 eV

    V_bi = 5.1 − 4.26 = 0.84 V

Φ_m > Φ_s on n-type silicon, so a depletion region forms: the contact is rectifying.

**Answer:** **Φ_B = 1.05 eV, V_bi = 0.84 V: a rectifying (Schottky) contact.**

**What this means:** an electron in the metal faces a 1.05 eV climb, about 40 kT, so very few cross from the metal: that is why the reverse current is small. In practice Fermi-level pinning gives a measured Φ_B of about 0.8 eV for Au on n-Si.

### The depletion region

The depletion region under the metal is exactly like the n side of a very one-sided (p⁺n) junction, because the metal holds its compensating charge in a sheet at its surface. With the depletion approximation (no free carriers in the region, uniform doping):

    W = √( 2ε_s(V_bi − V) / qN_D ),     E_max = qN_D W / ε_s

Where:

- W = depletion width (cm)
- ε_s = permittivity of silicon, 11.7ε₀ = 1.04×10⁻¹² F/cm
- V_bi = built-in potential (V); V = applied voltage (positive for forward bias)
- q = 1.6×10⁻¹⁹ C; N_D = donor concentration (cm⁻³)
- E_max = peak electric field, at the interface (V/cm)

Rearranged at zero bias, V_bi = qN_D W² / 2ε_s. Note that **W ∝ 1/√N_D**: more doping means a thinner depletion region. This is the key to ohmic contacts below.

#### Example 11.3: depletion width under a gold contact

**Question.** For the gold contact of Example 11.2 (V_bi = 0.84 V, N_D = 1×10¹⁶ cm⁻³), calculate the depletion width and the peak field at zero bias.

**Given:** V_bi = 0.84 V, V = 0, N_D = 1×10¹⁶ cm⁻³, ε_s = 1.04×10⁻¹² F/cm, q = 1.6×10⁻¹⁹ C.

**Find:** W and E_max.

**Formula:** W = √(2ε_sV_bi/qN_D);  E_max = qN_D W/ε_s.

**Solution.**

    W = √( 2 × 1.04×10⁻¹² × 0.84 / (1.6×10⁻¹⁹ × 10¹⁶) ) = √(1.09×10⁻⁹) = 3.3×10⁻⁵ cm = 0.33 μm

    E_max = 1.6×10⁻¹⁹ × 10¹⁶ × 3.3×10⁻⁵ / 1.04×10⁻¹² = 5.1×10⁴ V/cm

**Answer:** **W = 0.33 μm, E_max = 5.1×10⁴ V/cm.**

**What this means:** the barrier is about 0.33 μm thick, far too thick for electrons to tunnel through, so they must go over it by thermionic emission. The contact rectifies.

### How current flows: thermionic emission

In a Schottky diode the current is carried by **majority carriers** (electrons in n-type) jumping **over** the barrier. Only electrons with enough thermal energy can get over, so the current depends exponentially on the barrier height:

    J = J_s ( e^{qV/ηkT} − 1 ),     J_s = A∗∗ T² e^{−qΦ_B/kT}

Where:

- J = current density (A/cm²); I = J × A for a diode of area A
- J_s = saturation current density (A/cm²)
- V = applied voltage, positive for forward bias (metal positive on n-type) (V)
- η = ideality factor: 1 for the ideal model, 1.0–1.1 for good diodes
- kT/q = thermal voltage, 0.0259 V at 300 K
- A∗∗ = effective Richardson constant: about 110 A/cm²K² for n-Si, 8 for n-GaAs
- T = absolute temperature (K)
- Φ_B = barrier height (eV in qΦ_B/kT with kT in eV)

The shape is the same as a p-n diode, but J_s is far larger, so the diode turns on at a lower voltage.

#### Example 11.4: Schottky saturation current

**Question.** A Schottky diode on n-type silicon has a barrier height of 0.8 eV. Taking A∗∗ = 110 A/cm²K², calculate the saturation current density at 300 K and the forward voltage needed for 1 A/cm².

**Given:** Φ_B = 0.8 eV, A∗∗ = 110 A/cm²K², T = 300 K, kT = 0.0259 eV, J = 1 A/cm², η = 1.

**Find:** J_s, and V at J = 1 A/cm².

**Formula:** J_s = A∗∗T²e^{−qΦ_B/kT};  V = (kT/q) ln(J/J_s) (forward bias, J ≫ J_s).

**Solution.**

Step 1. Saturation current density:

    J_s = 110 × 300² × e^{−0.8/0.0259} = 9.9×10⁶ × 3.9×10⁻¹⁴ = 3.8×10⁻⁷ A/cm²

Step 2. Forward voltage:

    V = 0.0259 × ln(1/3.8×10⁻⁷) = 0.0259 × 14.8 = 0.38 V

**Answer:** **J_s = 3.8×10⁻⁷ A/cm²; 1 A/cm² flows at about 0.38 V.**

**What this means:** a silicon p-n diode needs about 0.7 V for the same current, because its J_s is about 10⁵ times smaller. The Schottky diode wastes less power as heat when it conducts.

#### Example 11.5: forward current of a Schottky diode

**Question.** An ideal Schottky diode has a saturation current of 2 μA. Calculate its current at 300 K when a forward voltage of 0.20 V is applied.

**Given:** I_s = 2×10⁻⁶ A, V = 0.20 V, η = 1, T = 300 K, kT/q = 0.02585 V.

**Find:** I.

**Formula:** I = I_s ( e^{qV/ηkT} − 1 ).

**Solution.**

Step 1. Exponent: qV/kT = 0.20 / 0.02585 = 7.737

Step 2. Exponential: e^{7.737} = 2291

Step 3. Current:

    I = 2×10⁻⁶ × (2291 − 1) = 4.58×10⁻³ A

**Answer:** **I = 4.58 mA.**

**What this means:** only 0.2 V multiplies the current more than two-thousand-fold above I_s. Every extra 0.1 V multiplies it by a further e^{0.1/0.0259} ≈ 48. In a real diode the series resistance and η > 1 make the current somewhat smaller.

### Schottky diode versus p-n diode

| | Schottky diode | p-n junction diode |
|---|---|---|
| Current carried by | Majority carriers only | Minority carriers injected and diffusing |
| Mechanism | Thermionic emission over the barrier | Diffusion |
| Stored minority charge | Practically none | Q = Iτ |
| Switching speed | Very fast, no reverse-recovery delay | Slower (recovery time ≈ τ) |
| Turn-on voltage (Si) | 0.2–0.4 V | 0.6–0.7 V |
| Reverse leakage | Higher | Lower |
| Breakdown voltage | Lower | Higher |
| Uses | Fast rectifiers in power supplies, microwave mixers and detectors, clamps, MESFET gates | General rectification, high voltage, low leakage |

@fig figures/contact-iv.svg | Current–voltage curves. An ohmic contact gives a straight line through the origin (current both ways). A Schottky diode turns on at about 0.3 V, a silicon p-n diode at about 0.65 V; both pass very little current in reverse.

## Band diagrams under bias

Take the metal on n-type Si. The key rule: **the barrier seen from the metal, qΦ_B, never changes**, because it is fixed by the interface. The applied voltage appears across the depletion region and changes only the barrier seen from the semiconductor. Under bias the two sides are no longer in equilibrium, so there is no single flat Fermi level: the semiconductor's Fermi level moves by qV relative to the metal's.

| | Equilibrium (V = 0) | Forward bias (metal +, V > 0) | Reverse bias (metal −, V < 0) |
|---|---|---|---|
| Fermi levels | One flat E_F | Semiconductor E_F raised by qV relative to the metal | Semiconductor E_F lowered by q\|V\| |
| Band bending | qV_bi | q(V_bi − V), smaller | q(V_bi + \|V\|), larger |
| Depletion width | W₀ = √(2ε_sV_bi/qN_D) | Narrower | Wider |
| Electrons semiconductor → metal | Balanced by metal → semiconductor | Increase by e^{qV/kT} | Suppressed |
| Electrons metal → semiconductor | Small, over Φ_B | Unchanged (Φ_B fixed) | Unchanged: this is the saturation current |
| Net current | 0 | J_s(e^{qV/ηkT} − 1), large | ≈ −J_s, small |

@fig figures/schottky-bias.svg | The same Schottky contact in equilibrium, forward bias and reverse bias. The barrier from the metal (qΦ_B) stays fixed. Forward bias shrinks the semiconductor-side barrier to q(V_bi − V); reverse bias raises it to q(V_bi + |V|).

> **In plain words.** The metal side of the hill never changes height. Forward bias lowers the semiconductor side of the hill, so a flood of electrons pours over it into the metal. Reverse bias raises the semiconductor side, stopping that flow, and only the small trickle from the metal side remains.

At large reverse voltage the field becomes strong enough to cause **breakdown**. Real diodes also show some extra leakage from **image-force lowering** (the barrier is pulled down slightly by the high field) and a voltage drop across their series resistance.

## Ohmic contacts

An **ohmic contact** has a straight-line, symmetric I-V characteristic and a resistance negligible compared with the device. Current passes freely in both directions.

    V = I R_c,     R_c = ρ_c / A

Where:

- V = voltage across the contact (V); I = current through it (A)
- R_c = contact resistance (Ω)
- ρ_c = specific contact resistance (Ω·cm²)
- A = contact area (cm²)

An ohmic contact is **not necessarily a contact with no barrier**. It may have a barrier that is so low, or so thin, that it does not restrict the current. There are three ways to make one.

@fig figures/ohmic-contacts.svg | Two ways to an ohmic contact on n-type silicon. (a) A metal with Φ_m < Φ_s: electrons flow into the semiconductor, the bands bend down into an accumulation layer, and there is no barrier. (b) Heavy doping: a barrier is still there, but it is only a few nanometres thick, so electrons tunnel straight through it.

**1. Choose a low-barrier metal.** For n-type, use a metal with Φ_m < Φ_s (for p-type, Φ_m > Φ_s). Now electrons flow from the **metal into the semiconductor** on contact, piling up an **accumulation layer** instead of a depletion layer. The bands bend **downward**, and there is no barrier for electrons in either direction. In practice Fermi-level pinning makes suitable metals rare for Si and GaAs, so the second method is used.

**2. Dope heavily so that electrons tunnel (the practical method).** Dope the semiconductor very heavily just under the contact (n⁺ or p⁺, above about 10¹⁹ cm⁻³). A barrier still exists, but because W ∝ 1/√N_D the depletion width shrinks to a few nanometres. A barrier that thin is no obstacle: electrons **tunnel** straight through it in both directions.

**3. Engineer the interface.** Clean the surface, then deposit and anneal (heat) the metal so that it reacts with the semiconductor and forms a stable compound with a low barrier: a **silicide** (TiSi₂, CoSi₂, NiSi) on silicon, or an alloyed Au–Ge–Ni contact on n-GaAs.

> **In plain words.** A wall that is high but paper-thin is no barrier to a quantum particle: it goes straight through. Heavy doping makes the barrier paper-thin.

| | Thermionic emission | Tunnelling (field emission) |
|---|---|---|
| How the electron crosses | Over the top of the barrier | Through the barrier |
| Needs | Enough thermal energy | A thin barrier (a few nm) |
| Doping under the contact | Light to moderate (≤ 10¹⁷ cm⁻³) | Heavy (≥ 10¹⁹ cm⁻³) |
| Temperature dependence | Strong (∝ T²e^{−qΦ_B/kT}) | Weak |
| Gives | Schottky (rectifying) contact | Ohmic contact |

#### Example 11.6: why heavy doping makes a contact ohmic

**Question.** The voltage across the depletion region under a contact on n-type silicon is 0.60 V. Calculate the depletion width for N_D = 1×10¹⁶ cm⁻³ and for N_D = 1×10¹⁹ cm⁻³, and say which contact will be ohmic.

**Given:** V_bi − V = 0.60 V, ε_s = 1.04×10⁻¹² F/cm, q = 1.6×10⁻¹⁹ C, N_D = 10¹⁶ and 10¹⁹ cm⁻³.

**Find:** W for each doping.

**Formula:** W = √( 2ε_s(V_bi − V)/qN_D ).

**Solution.**

Step 1. Light doping:

    W = √( 2 × 1.04×10⁻¹² × 0.60 / (1.6×10⁻¹⁹ × 10¹⁶) ) = 2.79×10⁻⁵ cm = 279 nm

Step 2. Heavy doping: N_D is 1000 times larger, so W is √1000 = 31.6 times smaller:

    W = 279 nm / 31.6 = 8.8 nm

**Answer:** **W = 279 nm at 10¹⁶ cm⁻³ and 8.8 nm at 10¹⁹ cm⁻³.**

**What this means:** electrons cannot tunnel through 279 nm, so the lightly doped contact rectifies. A barrier under about 10 nm thick lets a large tunnelling current through, so the heavily doped contact behaves as ohmic, even though the barrier height has not changed.

## Schottky contact versus ohmic contact, and where each is used

| Feature | Schottky contact | Ohmic contact |
|---|---|---|
| Electrical behaviour | Rectifying | Non-rectifying |
| I-V curve | Exponential, asymmetric | Straight line through the origin |
| Barrier | Significant: limits the current | Low, or thin enough to tunnel through |
| Main transport mechanism | Thermionic emission | Tunnelling, or flow over a small barrier |
| Doping under the contact | Moderate | Heavy (n⁺ or p⁺) |
| Used for | Fast rectifiers, clamps, RF detectors and mixers, MESFET gates | Transistor terminals, solar-cell contacts, every IC connection |
| Advantages | Fast switching (majority carriers, no stored charge); low forward voltage | Low resistance; current collected efficiently in both directions |
| Limitations | Higher reverse leakage; lower breakdown voltage | Needs heavy doping and careful processing; resistance rises if fabrication is poor |

Both are needed together: a Schottky diode has a rectifying contact on one side and an ohmic contact on the other. In a **solar cell**, every contact must be ohmic: an accidental barrier adds series resistance, lowers the fill factor and reduces the output power.

**Fermi-level pinning (what really happens).** Measured barriers depend much less on the metal than Φ_B = Φ_m − χ predicts, because surface states at the interface hold ("pin") the Fermi level near a fixed energy. For example, gold on n-Si gives Φ_B ≈ 0.8 eV, not 1.05 eV; on n-GaAs almost every metal gives about 0.8 eV. In calculations, use the measured Φ_B if it is given.

## Stability of contacts

Contacts must keep working through hot processing steps and years of operation:

- **Aluminium spiking:** silicon dissolves into aluminium and aluminium spikes into the silicon, which can short out a shallow junction. Prevented by adding 1 % Si to the Al, or by a barrier layer (TiN, TiW).
- **Electromigration:** at high current density the flowing electrons gradually push metal atoms along, forming voids and breaks. Reduced by Al–Cu alloys or copper wiring.
- **Interdiffusion and chemical reaction** at high temperature change the barrier height; silicides are used because they form a clean, stable interface.
- **Contamination and native oxide** at the interface raise ρ_c and change Φ_B.

## Key points of Week 11

- Φ_s = χ + (E_c − E_F). Metal on n-type with Φ_m > Φ_s → Schottky barrier; Φ_m < Φ_s (or heavy doping) → ohmic.
- Schottky: electrons leave the semiconductor, a depletion region forms, bands bend up, Fermi levels align. Φ_B = Φ_m − χ (ideally), V_bi = Φ_m − Φ_s, W = √(2ε_sV_bi/qN_D).
- Current by thermionic emission of majority carriers: J = A∗∗T²e^{−qΦ_B/kT}(e^{qV/ηkT} − 1). Fast, low turn-on voltage, higher leakage.
- Under bias, qΦ_B is fixed; only the semiconductor-side barrier changes.
- Ohmic contacts: accumulation (low barrier), tunnelling through a thin barrier made by heavy doping (W ∝ 1/√N_D), or a silicide. An ohmic contact may still have a barrier; what matters is that it does not limit the current.

---

## Examination question solved (Q49)

### Q49. Differentiate between a Schottky barrier diode and an Ohmic contact. Explain their energy-band characteristics.

Both are metal–semiconductor junctions. The difference is whether a significant potential barrier to majority-carrier flow exists at the interface.

**Schottky barrier diode (rectifying contact).**

*Condition:* n-type semiconductor with Φ_m > Φ_s (or p-type with Φ_m < Φ_s), moderate doping (≤ 10¹⁷ cm⁻³).

*Energy-band characteristics:*

1. Before contact, E_F in the n-semiconductor lies above E_F in the metal by Φ_m − Φ_s.
2. On contact, electrons flow from semiconductor to metal until the Fermi levels align. A **depletion region** of ionised donors forms in the semiconductor and the bands bend **upward** at the interface.
3. A barrier of height **qΦ_B = q(Φ_m − χ)** opposes electron flow from metal to semiconductor; a built-in barrier **qV_bi = q(Φ_m − Φ_s)** opposes flow from semiconductor to metal. (In practice Φ_B is fixed by Fermi-level pinning, e.g. ≈ 0.8 eV for Au on n-Si.)
4. Forward bias (metal positive) lowers the semiconductor-side barrier to V_bi − V, and electrons are thermionically emitted into the metal: current rises exponentially. Reverse bias raises it to V_bi + |V| while Φ_B stays the same, so only a small saturation current flows.

*I-V:* rectifying, J = A∗∗T²e^{−qΦ_B/kT}[e^{qV/ηkT} − 1].

*Features:* majority-carrier device, negligible minority storage, very fast switching, low forward drop (0.2–0.4 V on Si), higher leakage than a p-n diode.

**Ohmic contact.**

*Condition:* either n-type with Φ_m < Φ_s (p-type with Φ_m > Φ_s), or, in practice, any metal on a **very heavily doped** (n⁺ or p⁺, > 10¹⁹ cm⁻³) surface layer.

*Energy-band characteristics:*

1. **Low-barrier case:** electrons flow from the metal into the semiconductor on contact, forming an **accumulation layer**; the bands bend **downward**. There is no barrier for electrons in either direction.
2. **Tunnelling case:** a barrier exists, but heavy doping makes the depletion region only a few nanometres thick (W ∝ 1/√N_D). Electrons **tunnel** through it freely in both directions (field emission).

*I-V:* linear and symmetric, V = IR_c, with very low specific contact resistance (ρ_c ≈ 10⁻⁶–10⁻⁸ Ω·cm²).

| Feature | Schottky barrier | Ohmic contact |
|---|---|---|
| Work-function condition (n-type) | Φ_m > Φ_s | Φ_m < Φ_s (or heavy doping) |
| Semiconductor doping | Moderate (10¹⁵–10¹⁷ cm⁻³) | Heavy (> 10¹⁹ cm⁻³) |
| Band bending at interface (n-type) | Upward, depletion layer | Downward (accumulation) or very thin barrier |
| Barrier to majority carriers | Yes, qΦ_B and qV_bi | None, or transparent to tunnelling |
| Conduction mechanism | Thermionic emission | Free flow or field-emission tunnelling |
| I-V characteristic | Rectifying, exponential | Linear, symmetric |
| Resistance | Depends on bias and polarity | Small, constant |
| Purpose | Fast rectifier, detector, MESFET gate | Connecting devices to the circuit |
| Examples | Au, Pt, W, PtSi on n-Si; Ti/Au on n-GaAs | Al or silicide on n⁺/p⁺ Si; Au–Ge–Ni on n⁺-GaAs |

---

## Practice questions

These extra questions practise this week's ideas. Work each one on paper before reading the solution; the calculation questions follow the same Question, Given, Find, Solution, Answer layout as the worked examples.

#### Practice 11.1: tungsten on n-type silicon

**Question.** Tungsten (Φ_m = 4.55 eV) is deposited on n-type silicon with N_D = 1×10¹⁵ cm⁻³ (χ = 4.05 eV). Using the ideal model, find Φ_B, Φ_s and V_bi.

**Given:** Φ_m = 4.55 eV, χ = 4.05 eV, N_D = 10¹⁵ cm⁻³, N_c = 2.8×10¹⁹ cm⁻³.

**Find:** Φ_B, Φ_s, V_bi.

**Solution.**

    Φ_B = Φ_m − χ = 4.55 − 4.05 = 0.50 eV
    E_c − E_F = 0.02585 ln(2.8×10¹⁹/10¹⁵) = 0.265 eV
    Φ_s = 4.05 + 0.265 = 4.315 eV
    V_bi = Φ_m − Φ_s = 4.55 − 4.315 = 0.235 V

**Answer:** **Φ_B = 0.50 eV, Φ_s = 4.32 eV, V_bi = 0.24 V.**

#### Practice 11.2: choosing a metal for an Ohmic contact

**Question.** n-type silicon with N_D = 1×10¹⁶ cm⁻³ has Φ_s = 4.26 eV. Using the ideal theory, which of Al (4.28), Ti (4.33), Au (5.1) would give an Ohmic contact? What is done in practice?

**Given:** Φ_s = 4.26 eV; an Ohmic contact on n-type needs Φ_m < Φ_s.

**Find:** a suitable metal.

**Solution.** All three have Φ_m > Φ_s (Al only just, by 0.02 eV), so none meets the ideal Ohmic condition; Au, with the largest Φ_m, would give the strongest barrier.

**Answer:** **None, strictly.** In practice the silicon under the contact is doped n⁺ (above 10¹⁹ cm⁻³) so the barrier becomes thin enough to tunnel through, and Al or a silicide is used.

#### Practice 11.3: Schottky forward voltage

**Question.** A Schottky diode on n-Si has Φ_B = 0.65 eV. Find J_s at 300 K (A∗∗ = 110 A/cm²K²) and the forward voltage at 10 A/cm².

**Given:** Φ_B = 0.65 eV, A∗∗ = 110 A/cm²K², T = 300 K, J = 10 A/cm².

**Find:** J_s and V.

**Solution.**

    J_s = 110 × 300² × e^{−0.65/0.0259} = 9.9×10⁶ × 1.26×10⁻¹¹ = 1.25×10⁻⁴ A/cm²
    V = 0.0259 ln(10/1.25×10⁻⁴) = 0.0259 × 11.29 = 0.29 V

**Answer:** **J_s = 1.25×10⁻⁴ A/cm², V ≈ 0.29 V.**

#### Practice 11.4: why heavy doping gives tunnelling

**Question.** Find the zero-bias depletion width under a contact with V_bi = 0.6 V for N_D = 1×10¹⁶ cm⁻³ and for N_D = 1×10²⁰ cm⁻³. Explain the result.

**Given:** V_bi = 0.6 V, ε_s = 1.04×10⁻¹² F/cm.

**Find:** W for each doping.

**Solution.**

    W(10¹⁶) = √(2 × 1.04×10⁻¹² × 0.6 / (1.6×10⁻¹⁹ × 10¹⁶)) = 2.8×10⁻⁵ cm = 0.28 μm
    W(10²⁰) = W(10¹⁶)/√10⁴ = 2.8×10⁻⁷ cm = 2.8 nm

**Answer:** **0.28 μm and 2.8 nm.** A 2.8 nm barrier is thin enough for electrons to tunnel through, so the heavily doped contact is Ohmic even though the barrier is still there.

#### Practice 11.5: contact resistance of a small contact

**Question.** A contact has specific contact resistance ρ_c = 1×10⁻⁶ Ω·cm² and measures 1 μm × 1 μm. Find its resistance.

**Given:** ρ_c = 10⁻⁶ Ω·cm², A = (10⁻⁴ cm)² = 10⁻⁸ cm².

**Find:** R_c.

**Solution.**

    R_c = ρ_c/A = 10⁻⁶/10⁻⁸ = 100 Ω

**Answer:** **R_c = 100 Ω**, large for a small transistor, which is why modern processes need ρ_c near 10⁻⁸ Ω·cm².

#### Practice 11.6: an Ohmic contact by accumulation

**Question.** Describe the band diagram of an ideal Ohmic contact formed by a low work-function metal (Φ_m < Φ_s) on n-type silicon.

**Answer.** Before contact the metal's Fermi level is higher than the semiconductor's. On contact, electrons flow from the metal into the semiconductor until the Fermi levels align. The extra electrons form an **accumulation layer** at the interface, and the semiconductor bands bend **downward** towards it. There is no depletion region and no barrier to electrons in either direction, so current flows freely both ways and the I-V characteristic is linear.

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Define work function and electron affinity and relate them. | Write Φ_s in terms of χ. | Φ_s = χ + (E_c − E_F). | Key terms; The energies before contact; Example 11.1 |
| 2 | Explain how a Schottky barrier forms and calculate Φ_B and V_bi. | Al (4.28 eV) on n-Si (χ = 4.05 eV): find the ideal barrier height. | Φ_B = 4.28 − 4.05 = 0.23 eV. | The Schottky barrier; Examples 11.2–11.3 |
| 3 | Explain thermionic emission and calculate Schottky diode currents. | Why does a Schottky diode switch faster than a p-n diode? | It is a majority-carrier device with no stored minority charge. | How current flows: thermionic emission; Examples 11.4–11.5 |
| 4 | Draw Schottky band diagrams in equilibrium and under bias. | Which barrier stays constant under bias? | qΦ_B, the barrier seen from the metal. | Band diagrams under bias |
| 5 | Explain the two ways of making Ohmic contacts. | Why does heavy doping make a contact Ohmic? | The depletion layer becomes so thin that electrons tunnel through it. | Ohmic contacts; Example 11.6 |
| 6 | Describe the stability problems of metal contacts. | What is electromigration? | Gradual movement of metal atoms by the flowing electrons, forming voids and opens. | Stability of contacts |
| 7 | Compare Schottky and ohmic contacts, their advantages, limitations and applications. | Give one advantage and one limitation of a Schottky diode, and one use of an ohmic contact. | Advantage: fast switching (or low forward voltage). Limitation: higher reverse leakage (or lower breakdown voltage). Ohmic use: transistor terminals or solar-cell contacts. | Schottky contact versus ohmic contact |
