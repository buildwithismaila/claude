# Module 15 — Metal–Semiconductor Contacts: Schottky and Ohmic

Examined in Q49. Every device has to be connected to metal wiring. Depending on the metal, the semiconductor and its doping, the contact either rectifies (Schottky) or conducts freely in both directions (Ohmic).

## 15.1 Energy quantities

- **Work function Φ_m** (metal) or **Φ_s** (semiconductor): energy to take an electron from the Fermi level to the vacuum level. Φ_s depends on doping, because E_F moves.
- **Electron affinity χ**: energy from the bottom of the conduction band to the vacuum level. A material constant: Si 4.05 eV, GaAs 4.07 eV, Ge 4.0 eV.

    Φ_s = χ + (E_c − E_F)

Metal work functions (eV): Al 4.28, Ti 4.33, Cr 4.5, W 4.55, Ni 5.15, Au 5.1, Pt 5.65.

## 15.2 The Schottky barrier (rectifying contact)

**Case: metal on n-type with Φ_m > Φ_s.**

Before contact, the semiconductor Fermi level is higher than the metal's. On contact electrons flow from the semiconductor into the metal until the Fermi levels align. This leaves a **depletion region** of positive donor ions in the semiconductor (with a thin sheet of negative charge on the metal surface). The bands bend **upward** towards the interface.

@fig figures/schottky.svg | Metal on n-type silicon with Φ_m > Φ_s, after contact. Electrons in the metal see the barrier qΦ_B; electrons in the semiconductor see the smaller built-in barrier qV_bi.

Two barriers result:

    Barrier height (seen from the metal):  Φ_B = Φ_m − χ        (ideal Schottky–Mott rule)
    Built-in potential (seen from the semiconductor):  V_bi = Φ_m − Φ_s = Φ_B − (E_c − E_F)/q

For p-type: Φ_Bp = E_g/q − (Φ_m − χ), and a rectifying contact needs Φ_m < Φ_s.

**Fermi-level pinning.** Real barriers depend only weakly on Φ_m, because interface states fix the Fermi level at the surface at a characteristic energy (about one-third of the gap above E_v in Si and GaAs). Measured Φ_B on n-Si: Al ≈ 0.72, Ti ≈ 0.6, Au ≈ 0.8, PtSi ≈ 0.85 eV; on n-GaAs nearly always about 0.8 eV.

**Image-force lowering.** An electron near the metal is attracted by its image charge, which lowers the barrier slightly with field: ΔΦ = √(qE_max/4πε_s).

### Current transport

Current is carried by **majority carriers** (electrons) emitted over the barrier: **thermionic emission**.

    J = J_s [ exp(qV/ηkT) − 1 ],     J_s = A∗∗ T² exp( −qΦ_B/kT )

A∗∗ is the effective Richardson constant (120 A cm⁻²K⁻² for free electrons; about 110 for n-Si, 8 for n-GaAs), η the ideality factor (1.0–1.1 for good diodes).

Forward bias lowers the semiconductor-side barrier to V_bi − V; the metal-side barrier Φ_B is fixed, which gives the small, voltage-independent reverse current.

**Example.** n-Si, Φ_B = 0.8 eV, T = 300 K: J_s = 110 × (300)² × exp(−0.8/0.0259) = 9.9×10⁶ × 3.9×10⁻¹⁴ = 3.8×10⁻⁷ A/cm². That is about 10⁵ times larger than the J_s of a comparable p-n junction, so the Schottky diode turns on at about 0.3–0.4 V instead of 0.6–0.7 V.

### Schottky diode versus p-n diode

| | Schottky diode | p-n junction diode |
|---|---|---|
| Carriers | Majority carriers only | Minority-carrier injection and diffusion |
| Mechanism | Thermionic emission over a barrier | Diffusion |
| Stored charge | Negligible | Minority charge Q = Iτ |
| Switching | Very fast (ps), no reverse recovery | Slower (reverse-recovery time ≈ τ) |
| Turn-on voltage (Si) | 0.2–0.4 V | 0.6–0.7 V |
| Reverse leakage | Higher | Lower |
| Breakdown voltage | Lower | Higher |
| Uses | Microwave mixers and detectors, power-supply rectifiers, clamps in Schottky TTL, MESFET gates | General rectification, high-voltage, low leakage |

## 15.3 Ohmic contacts

An **Ohmic contact** has a linear, symmetric I-V characteristic and a resistance that is negligible compared with the device. It supplies current in either direction without limiting it.

Two ways to make one:

1. **Low barrier** (Φ_m < Φ_s for n-type, or Φ_m > Φ_s for p-type). Electrons flow from metal to semiconductor on contact, forming an **accumulation** layer instead of a depletion layer. There is no barrier to majority-carrier flow. In practice, pinning makes such low-barrier metals rare for Si and GaAs.
2. **Tunnelling contact** (the practical method). Dope the semiconductor very heavily under the contact (n⁺ or p⁺, above about 10¹⁹ cm⁻³). The depletion width W = √(2ε_sV_bi/qN_D) becomes only a few nanometres, so electrons **tunnel** straight through the barrier (field emission) in both directions, whatever its height.

Quality is measured by the **specific contact resistance** ρ_c (Ω·cm²). For tunnelling contacts it falls exponentially with doping:

    ρ_c ∝ exp( (2√(ε_s m∗)/ħ) · Φ_B / √N_D )

Good contacts reach ρ_c ≈ 10⁻⁶–10⁻⁸ Ω·cm². Common choices: Al or silicides (TiSi₂, CoSi₂, NiSi) on n⁺/p⁺ Si; alloyed Au–Ge–Ni on n-GaAs. Contact resistance is measured with the transmission-line (TLM) method.

## 15.4 Stability of contacts

Contacts must stay stable through processing and operation:

- **Al spiking:** Si dissolves into Al and Al penetrates into Si, shorting shallow junctions. Prevented by Al–1%Si alloy or barrier layers (TiN, TiW).
- **Electromigration:** high current densities move metal atoms, causing voids and open circuits. Reduced by Al–Cu alloys or Cu metallisation.
- **Interdiffusion and reaction** at high temperature change the barrier height; silicides are used because they form a clean, stable interface.
- **Interface contamination** and native oxide raise ρ_c and change Φ_B.

---

## Exam questions solved

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
