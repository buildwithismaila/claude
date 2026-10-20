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
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| μm | Micrometre (micron) | 1 μm = 10⁻⁴ cm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_c (E_C) | Energy of the bottom of the conduction band | eV |
| E_g | Band-gap energy, E_c − E_v | eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K |
| E_F | Fermi level: the energy at which a state has a 50 % chance of being occupied | eV |
| N_c | Effective density of states in the conduction band | cm⁻³; Si 2.8×10¹⁹ at 300 K |
| N_D | Donor concentration | cm⁻³ |
| Q | Dose: dopant atoms per unit area (in Weeks 13–14, Q also means charge) | atoms/cm² (C or C/cm² for charge) |
| τ, τ_n, τ_p | Minority-carrier lifetime (τ_eff: effective, including surfaces) | s; Si 1 ns – 1 ms |
| V_bi | Built-in potential of a junction or Schottky contact | V; typically 0.5–1 V |
| V, V_a | Applied voltage (positive for forward bias) | V |
| W | Depletion-region width (in Week 13 W_B, W_E are base and emitter widths; in Week 14 W is channel width) | μm or cm |
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
| I-V | Current–voltage (measurement or characteristic) |
| MESFET | Metal–semiconductor field-effect transistor |
| n⁺ | Very heavily doped n-type (similarly p⁺) |


## The big picture

Every device must be wired to the outside world with metal. You might expect a metal touching a semiconductor to behave like a simple wire connection. Sometimes it does: that is an **Ohmic contact**, which lets current through equally well in both directions. But sometimes the contact itself forms a **barrier** and conducts in only one direction, like a diode: a **Schottky contact**.

Which one you get depends on the metal, the semiconductor and its doping. Engineers want Ohmic contacts for wiring, and Schottky contacts when they want a very fast diode. This week explains both using band diagrams, with the same flat-Fermi-level reasoning as the p-n junction (Week 10).

## The energies involved

Three quantities describe where the electrons sit, all measured from the **vacuum level** (the energy of an electron just free of the material):

- **Work function Φ_m (metal):** the energy needed to pull an electron from the metal's Fermi level out to the vacuum.
- **Work function Φ_s (semiconductor):** the same for the semiconductor. It depends on doping, because doping moves E_F.
- **Electron affinity χ (semiconductor):** the energy from the **bottom of the conduction band** to the vacuum level. This is a fixed property of the material: Si 4.05 eV, GaAs 4.07 eV, Ge 4.0 eV.

These are linked by

    Φ_s = χ + (E_c − E_F)

Metal work functions (eV): Al 4.28, Ti 4.33, Cr 4.5, W 4.55, Au 5.1, Ni 5.15, Pt 5.65.

#### Example 11.1: work function of doped silicon

**Question.** Calculate the work function of n-type silicon doped with N_D = 1×10¹⁶ cm⁻³ at 300 K. The electron affinity of Si is 4.05 eV.

**Given:** χ = 4.05 eV, N_D = 1×10¹⁶ cm⁻³, N_c = 2.8×10¹⁹ cm⁻³, kT = 0.02585 eV.

**Find:** Φ_s.

**Solution.**

Step 1. Position of E_F (Example 5.1): E_c − E_F = kT ln(N_c/N_D) = 0.205 eV

Step 2. Φ_s = χ + (E_c − E_F) = 4.05 + 0.205 = 4.26 eV

**Answer:** **Φ_s = 4.26 eV.**

## The Schottky barrier (rectifying contact)

### How it forms: metal on n-type with Φ_m > Φ_s

1. **Before contact**, the semiconductor's Fermi level is **higher** than the metal's (its electrons are less tightly held, since Φ_s < Φ_m).
2. **On contact**, electrons flow "downhill" from the semiconductor into the metal, until the two Fermi levels line up, just as in a p-n junction.
3. The electrons that left uncover **positive donor ions** in the semiconductor near the interface: a **depletion region**, exactly like the n side of a p⁺n junction. A thin sheet of extra electrons sits on the metal surface.
4. The bands in the semiconductor bend **upward** towards the interface.

@fig figures/schottky.svg | Metal on n-type silicon (Φ_m > Φ_s) after contact. An electron in the metal sees the barrier qΦ_B. An electron in the semiconductor sees the smaller built-in barrier qV_bi.

There are now **two barriers**, depending on which side the electron starts from:

    seen from the metal (barrier height):       Φ_B = Φ_m − χ       (the ideal Schottky–Mott rule)
    seen from the semiconductor (built-in):    V_bi = Φ_m − Φ_s = Φ_B − (E_c − E_F)/q

#### Example 11.2: ideal Schottky barrier

**Question.** Gold (Φ_m = 5.1 eV) is deposited on the n-type silicon of Example 11.1. Using the ideal Schottky–Mott model, find the barrier height seen from the metal and the built-in potential seen from the semiconductor. Is the contact rectifying or Ohmic?

**Given:** Φ_m = 5.1 eV, χ = 4.05 eV, Φ_s = 4.26 eV.

**Find:** Φ_B, V_bi, and the type of contact.

**Solution.**

    Φ_B = Φ_m − χ = 5.1 − 4.05 = 1.05 eV

    V_bi = Φ_m − Φ_s = 5.1 − 4.26 = 0.84 V

Φ_m > Φ_s on n-type silicon, so a depletion region forms: the contact is rectifying.

**Answer:** **Φ_B = 1.05 eV, V_bi = 0.84 V: a rectifying (Schottky) contact.** In practice Fermi-level pinning gives a measured Φ_B of about 0.8 eV for Au on n-Si.

(For p-type semiconductors everything flips: a rectifying contact needs Φ_m < Φ_s, and the barrier for holes is Φ_{Bp} = E_g/q − (Φ_m − χ).)

**Fermi-level pinning (what really happens).** Measured barriers depend much less on the metal than the simple rule predicts, because surface states at the interface (Week 9) hold ("pin") the Fermi level near a fixed energy. For example, gold on n-Si gives Φ_B ≈ 0.8 eV, not 1.05 eV; on n-GaAs almost every metal gives about 0.8 eV. In calculations, use the measured Φ_B if it is given.

### How current flows: thermionic emission

In a Schottky diode the current is carried by **majority carriers** (electrons in n-type) jumping **over** the barrier. This is **thermionic emission**: only electrons with enough thermal energy can get over, so the current depends exponentially on the barrier height.

    J = J_s ( e^{qV/ηkT} − 1 ),     J_s = A∗∗ T² e^{−qΦ_B/kT}

| Symbol | Meaning |
|---|---|
| A∗∗ | effective Richardson constant (about 110 A/cm²K² for n-Si, 8 for n-GaAs) |
| T | temperature |
| Φ_B | barrier height |
| η | ideality factor, 1.0–1.1 for good diodes |

The shape is the same as a p-n diode, but J_s is far larger.

#### Example 11.3: Schottky saturation current

**Question.** A Schottky diode on n-type silicon has a barrier height of 0.8 eV. Taking A∗∗ = 110 A/cm²K², calculate the saturation current density at 300 K and the forward voltage needed for 1 A/cm².

**Given:** Φ_B = 0.8 eV, A∗∗ = 110 A/cm²K², T = 300 K, kT = 0.0259 eV, J = 1 A/cm².

**Find:** J_s, and V at J = 1 A/cm².

**Solution.**

Step 1. J_s = A∗∗T²e^{−qΦ_B/kT}:

    J_s = 110 × 300² × e^{−0.8/0.0259} = 9.9×10⁶ × 3.9×10⁻¹⁴ = 3.8×10⁻⁷ A/cm²

Step 2. V = (kT/q) ln(J/J_s) for an ideal diode:

    V = 0.0259 × ln(1/3.8×10⁻⁷) = 0.0259 × 14.8 = 0.38 V

**Answer:** **J_s = 3.8×10⁻⁷ A/cm²; 1 A/cm² flows at about 0.38 V**, compared with about 0.7 V for a p-n diode, because J_s is about 10⁵ times larger.

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

## Band diagrams under bias

Take the metal on n-type Si. The key rule: **the barrier seen from the metal, qΦ_B, never changes**, because it is fixed by the interface. The applied voltage appears across the depletion region and changes only the barrier seen from the semiconductor.

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

## Ohmic contacts

An **Ohmic contact** has a straight-line, symmetric I-V characteristic (it obeys Ohm's law) and a resistance negligible compared with the device. Current passes freely in both directions.

There are two ways to make one.

**1. Choose a low-barrier metal.** For n-type, use a metal with Φ_m < Φ_s. Now electrons flow from the **metal into the semiconductor** on contact, piling up an **accumulation layer** instead of a depletion layer. The bands bend **downward**, and there is no barrier for electrons in either direction. In practice Fermi-level pinning makes suitable metals rare for Si and GaAs, so the second method is used.

**2. Dope heavily so that electrons tunnel (the practical method).** Dope the semiconductor very heavily just under the contact (n⁺ or p⁺, above about 10¹⁹ cm⁻³). A barrier still exists, but the depletion width W = √(2ε_sV_bi/qN_D) shrinks to a few nanometres. A barrier that thin is no obstacle: electrons **tunnel** straight through it in both directions (quantum tunnelling, called field emission).

> **In plain words.** A wall that is high but paper-thin is no barrier to a quantum particle: it goes straight through. Heavy doping makes the barrier paper-thin.

The quality of an Ohmic contact is measured by its **specific contact resistance** ρ_c (Ω·cm²), which falls very steeply as the doping increases. Good contacts have ρ_c ≈ 10⁻⁶–10⁻⁸ Ω·cm². Common choices: aluminium or a silicide (TiSi₂, CoSi₂, NiSi) on n⁺ or p⁺ silicon; an alloyed Au–Ge–Ni contact on n-GaAs.

## Stability of contacts

Contacts must keep working through hot processing steps and years of operation:

- **Aluminium spiking:** silicon dissolves into aluminium and aluminium spikes into the silicon, which can short out a shallow junction. Prevented by adding 1 % Si to the Al, or by a barrier layer (TiN, TiW).
- **Electromigration:** at high current density the flowing electrons gradually push metal atoms along, forming voids and breaks. Reduced by Al–Cu alloys or copper wiring.
- **Interdiffusion and chemical reaction** at high temperature change the barrier height; silicides are used because they form a clean, stable interface.
- **Contamination and native oxide** at the interface raise ρ_c and change Φ_B.

## Key points of Week 11

- Φ_s = χ + (E_c − E_F). Metal on n-type with Φ_m > Φ_s → Schottky barrier; Φ_m < Φ_s (or heavy doping) → Ohmic.
- Schottky: depletion region, bands bend up, Φ_B = Φ_m − χ (ideally), V_bi = Φ_m − Φ_s.
- Current by thermionic emission of majority carriers: J = A∗∗T²e^{−qΦ_B/kT}(e^{qV/kT} − 1). Fast, low turn-on voltage, higher leakage.
- Under bias, qΦ_B is fixed; only the semiconductor-side barrier changes.
- Ohmic contacts: accumulation (low barrier) or tunnelling through a thin barrier made by heavy doping (n⁺, p⁺).

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
| 1 | Define work function and electron affinity and relate them. | Write Φ_s in terms of χ. | Φ_s = χ + (E_c − E_F). | The energies involved; Example 11.1 |
| 2 | Explain how a Schottky barrier forms and calculate Φ_B and V_bi. | Al (4.28 eV) on n-Si (χ = 4.05 eV): find the ideal barrier height. | Φ_B = 4.28 − 4.05 = 0.23 eV. | The Schottky barrier; Example 11.2 |
| 3 | Explain thermionic emission and calculate Schottky diode currents. | Why does a Schottky diode switch faster than a p-n diode? | It is a majority-carrier device with no stored minority charge. | Current transport; Example 11.3 |
| 4 | Draw Schottky band diagrams in equilibrium and under bias. | Which barrier stays constant under bias? | qΦ_B, the barrier seen from the metal. | Band diagrams under bias |
| 5 | Explain the two ways of making Ohmic contacts. | Why does heavy doping make a contact Ohmic? | The depletion layer becomes so thin that electrons tunnel through it. | Ohmic contacts |
| 6 | Describe the stability problems of metal contacts. | What is electromigration? | Gradual movement of metal atoms by the flowing electrons, forming voids and opens. | Stability of contacts |
