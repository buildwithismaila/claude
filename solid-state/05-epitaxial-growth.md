# Module 05 — Epitaxial Growth: VPE, LPE and MBE

Examined in Q12–Q13. **Epitaxy** (Greek *epi* "upon", *taxis* "arrangement") is the growth of a thin single-crystal layer on a single-crystal substrate so that the layer continues the substrate's lattice and orientation.

## 5.1 Why epitaxy is needed

Bulk growth gives one uniformly doped crystal. Devices need thin layers of **different doping or composition** on top of each other, with sharp interfaces:

- A lightly doped layer on a heavily doped substrate (bipolar transistors, power diodes, CMOS latch-up prevention).
- Layers of a different material: AlGaAs on GaAs, InGaAs on InP, GaN on sapphire (heterostructures, quantum wells, lasers, HEMTs).
- Layers with fewer defects and less oxygen than CZ substrates.

**Homoepitaxy:** layer and substrate are the same material (Si on Si). **Heteroepitaxy:** different materials (GaAs on Si, AlGaAs on GaAs). In heteroepitaxy the **lattice mismatch** f = (a_layer − a_sub)/a_sub must be small, otherwise misfit dislocations form above a critical thickness.

## 5.2 Vapour-phase epitaxy (VPE)

Also called **chemical vapour deposition (CVD) epitaxy**. The workhorse for silicon.

**Principle.** Gaseous compounds containing the semiconductor flow over a heated substrate. They decompose or react at the surface, depositing atoms which migrate to lattice sites and continue the crystal.

**Silicon chemistries** (from the hydrogen reduction of chlorosilanes or pyrolysis of silane):

    SiCl₄ + 2H₂ → Si + 4HCl          (≈ 1150–1250 °C)
    SiH₂Cl₂ → Si + 2HCl              (≈ 1000–1100 °C)
    SiH₄ → Si + 2H₂                  (≈ 600–1000 °C)

The HCl by-product etches silicon, so the reaction is reversible; too much SiCl₄ causes etching instead of growth. Dopant gases are added: **B₂H₆** (diborane) for p-type, **PH₃** (phosphine) or **AsH₃** (arsine) for n-type.

**Growth regimes.** Two steps in series: transport of reactant through the gas boundary layer (mass-transport limited, weakly temperature dependent, at high T) and the surface reaction (reaction-rate limited, strongly temperature dependent, at low T). Production reactors usually run mass-transport limited for good uniformity.

**For compound semiconductors:** chloride and hydride VPE, and **metal-organic CVD (MOCVD/MOVPE)**: (CH₃)₃Ga + AsH₃ → GaAs + 3CH₄ at about 600–750 °C. MOCVD is used for most commercial LEDs and lasers.

**Typical figures:** growth rate 0.1–5 μm/min, thickness control about ±5 %, high throughput (many wafers per batch).

**Problems:** **autodoping** (dopant evaporating from the substrate re-enters the layer) and **out-diffusion** from the heavily doped substrate at high temperature both blur the interface.

## 5.3 Liquid-phase epitaxy (LPE)

**Principle.** The substrate is brought into contact with a melt (solution) of the semiconductor dissolved in a solvent metal, saturated at a set temperature. The melt is then cooled slowly. As the solubility falls, the solution becomes supersaturated and the excess semiconductor crystallises onto the substrate, continuing its lattice.

**Example:** GaAs dissolved in molten Ga, growth at about **700–900 °C** while cooling at about 0.1–1 °C/min. AlGaAs layers are grown by adding Al to the melt.

**Apparatus:** the **sliding-boat** (graphite boat with several wells holding different melts; the substrate slides under each in turn to grow a multilayer structure), or tipping and dipping systems.

**Features:** growth is close to thermodynamic equilibrium, so crystal quality is excellent and deep-level defect density is low; equipment is simple and cheap; growth rates are high (0.1–1 μm/min). But thickness control is poor (about 0.1 μm at best), interfaces are not abrupt, surface morphology is rough, the area is small, and some alloys cannot be grown. Historically used for the first double-heterostructure lasers and for LEDs; still used for some LEDs and thick layers.

## 5.4 Molecular-beam epitaxy (MBE)

**Principle.** In **ultra-high vacuum** (about 10⁻¹⁰–10⁻¹¹ Torr), beams of atoms or molecules evaporated from heated **effusion (Knudsen) cells** travel in straight lines (the mean free path is far longer than the chamber) and strike a heated substrate. They adsorb, migrate on the surface and incorporate into the lattice. Growth is controlled by opening and closing **mechanical shutters** in front of each cell, which switches a beam in a fraction of a second.

**Example:** GaAs from Ga and As₄ cells with the substrate at about **550–650 °C**. Dopants: Si (n-type) and Be (p-type) cells.

**Features:**

- Growth rate about **1 μm/h**, i.e. about **one monolayer per second**, so layer thickness is controlled to a **single atomic layer**.
- **Abrupt interfaces** and arbitrary composition and doping profiles: quantum wells, superlattices, modulation-doped HEMTs, quantum-cascade lasers.
- **Low growth temperature** minimises interdiffusion and autodoping.
- **In-situ monitoring**: **RHEED** (reflection high-energy electron diffraction) oscillations count monolayers as they grow; mass spectrometers check beams.
- Disadvantages: very expensive UHV equipment, slow growth, low throughput, difficult with high-vapour-pressure elements like P, and needs long bake-outs.

@fig figures/epitaxy.svg | The three methods side by side: gas reacting at a hot surface (VPE), a cooling saturated melt (LPE), and atomic beams in ultra-high vacuum (MBE).

---

## Exam questions solved

### Q12. Explain the principles of vapour-phase epitaxy (VPE), liquid-phase epitaxy (LPE), and molecular-beam epitaxy (MBE).

Epitaxy is the growth of a thin single-crystal film on a single-crystal substrate such that the film adopts the substrate's crystal structure and orientation. The three methods differ in the phase from which atoms arrive.

**Vapour-phase epitaxy (VPE).** The semiconductor is supplied as a gas-phase chemical compound carried by hydrogen over a heated substrate inside a reactor. The compound decomposes or is reduced at the hot surface, and the released atoms move to lattice sites. For silicon the standard reaction is hydrogen reduction of silicon tetrachloride at about 1200 °C, SiCl₄ + 2H₂ → Si + 4HCl; silane SiH₄ → Si + 2H₂ is used at lower temperature. Doping is achieved by adding gases such as PH₃, AsH₃ or B₂H₆. The rate is set either by mass transport of reactants through the gas boundary layer or by the surface reaction. MOCVD is the metal-organic version used for III–V compounds.

**Liquid-phase epitaxy (LPE).** The substrate is placed in contact with a saturated solution of the semiconductor in a molten metal solvent (e.g. GaAs in liquid Ga). On slow, controlled cooling the solubility decreases, the solution becomes supersaturated and the semiconductor precipitates epitaxially on the substrate. Growth occurs near thermodynamic equilibrium. A sliding graphite boat moves the substrate under successive melts to grow multilayers.

**Molecular-beam epitaxy (MBE).** In ultra-high vacuum (≈ 10⁻¹⁰ Torr), elemental sources in heated effusion cells produce collision-free molecular beams aimed at a heated substrate. Atoms adsorb, migrate and incorporate in the lattice. Each beam has a shutter, so composition and doping can be switched abruptly. Growth is slow (≈ 1 monolayer/s) and is monitored in real time by RHEED, so thickness is controlled to atomic precision.

### Q13. Compare VPE, LPE, and MBE in terms of growth mechanism, temperature, precision, and applications.

| Feature | VPE (CVD) | LPE | MBE |
|---|---|---|---|
| Source phase | Gas (chlorosilanes, silane, metal-organics) | Liquid solution (melt) | Atomic or molecular beams from solid sources |
| Growth mechanism | Chemical reaction / decomposition at the hot surface | Precipitation from a supersaturated solution on cooling; near equilibrium | Physical deposition: adsorption and surface migration; far from equilibrium |
| Environment | Atmospheric or reduced pressure, H₂ carrier | Inert or H₂, graphite boat | Ultra-high vacuum, 10⁻¹⁰–10⁻¹¹ Torr |
| Typical temperature | High: Si 1000–1250 °C; MOCVD 600–750 °C | Intermediate: 700–900 °C (GaAs) | Low: 400–650 °C (GaAs ≈ 600 °C) |
| Growth rate | 0.1–5 μm/min | 0.1–1 μm/min | ≈ 1 μm/h (≈ 1 monolayer/s) |
| Thickness precision | ≈ tens of nm; good uniformity | Poor, ≈ 0.1 μm; rough surface | Excellent, one atomic layer |
| Interface abruptness | Moderate (autodoping, out-diffusion) | Poor (graded) | Atomically abrupt |
| Crystal purity | Good | Very high, low deep-level defects | Very high (UHV) |
| In-situ monitoring | Limited | None | RHEED, mass spectrometry |
| Cost and throughput | Moderate cost, high throughput (batch) | Low cost, low throughput, small area | Very high cost, low throughput |
| Applications | Si epi layers for BJTs, CMOS, power devices; MOCVD for LEDs, lasers, solar cells | LEDs, early heterostructure lasers, thick layers, photodetectors | Quantum wells, superlattices, HEMTs, HBTs, quantum-cascade and VCSEL lasers, research |

**Conclusion.** VPE is the industrial choice for volume production, LPE is a simple low-cost method giving high-quality thick layers with poor control, and MBE gives the ultimate atomic-scale control for advanced heterostructure devices at high cost.
