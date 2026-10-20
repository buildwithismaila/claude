# Week 11 — Metal–Semiconductor Interfaces
<!-- group: Module 4 · Junctions, Interfaces & Characterisation -->

**Plan:** Schottky barrier diode physics versus Ohmic contact mechanisms; energy band diagrams under equilibrium and bias.

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

**Example.** n-Si with N_D = 10¹⁶ cm⁻³ has E_c − E_F = 0.205 eV (Week 5), so Φ_s = 4.05 + 0.205 = 4.26 eV.

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

**Example.** Au (Φ_m = 5.1 eV) on the n-Si above: ideal Φ_B = 5.1 − 4.05 = 1.05 eV and V_bi = 5.1 − 4.26 = 0.84 V.

(For p-type semiconductors everything flips: a rectifying contact needs Φ_m < Φ_s, and the barrier for holes is Φ_Bp = E_g/q − (Φ_m − χ).)

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

**Example.** n-Si with Φ_B = 0.8 eV at 300 K:

    J_s = 110 × 300² × e^{−0.8/0.0259} = 9.9×10⁶ × 3.9×10⁻¹⁴ = 3.8×10⁻⁷ A/cm²

About 10⁵ times larger than for a comparable p-n junction. So a Schottky diode reaches a given current at about **0.3–0.4 V** instead of 0.6–0.7 V.

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
