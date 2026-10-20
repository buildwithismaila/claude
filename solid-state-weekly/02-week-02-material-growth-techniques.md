# Week 2 — Material Growth Techniques
<!-- group: Module 1 · Material Physics & Semiconductor Growth -->

**Plan:** purification of silicon (metallurgical to electronic grade); the Czochralski bulk crystal growth method; epitaxial growth techniques (VPE, LPE, MBE).

A device needs silicon with fewer than about one unwanted impurity atom per billion, grown as a single perfect crystal, and then thin layers of different doping or composition grown on top of it. This week covers all three steps.

## Part A: Purification of silicon

## The route from sand to wafer

    Quartzite (SiO₂) → MG-Si (98 %) → SiHCl₃ → purified SiHCl₃ → EG-Si polysilicon → single-crystal ingot → wafers

| Stage | Product | Purity |
|---|---|---|
| Carbothermic reduction in an arc furnace | Metallurgical-grade Si (MG-Si) | ≈ 98–99 % |
| Hydrochlorination, distillation, Siemens CVD | Electronic-grade polysilicon (EG-Si) | 99.9999999 % (9N) or better; impurities at ppb level |
| Czochralski or float-zone growth | Single-crystal, doped ingot | Dopant set deliberately |

## Stage 1: metallurgical-grade silicon

Quartzite (fairly pure SiO₂) is mixed with carbon (coal, coke, wood chips) and heated to about **2000 °C** in a submerged-electrode arc furnace:

    SiO₂ + 2C → Si + 2CO

Molten silicon is tapped from the furnace. MG-Si is about 98 % pure; the main impurities are Fe, Al, Ca, C, B and P. It is fine for steel and aluminium alloys and silicones, but far too impure for devices (it would contain about 10²⁰ cm⁻³ of unwanted impurities).

## Stage 2: conversion to trichlorosilane

MG-Si is ground and reacted with dry hydrogen chloride in a fluidised-bed reactor at about **300 °C**:

    Si + 3HCl → SiHCl₃ + H₂

Trichlorosilane (TCS) is a liquid that boils at 32 °C. The impurities form their own chlorides (FeCl₃, AlCl₃, BCl₃, PCl₃) with different boiling points.

## Stage 3: fractional distillation

The liquid SiHCl₃ is purified by repeated **fractional distillation**, which separates it from the impurity chlorides because of the boiling-point differences. Because distillation of a liquid is very effective, the TCS reaches impurity levels in the parts-per-billion range.

## Stage 4: Siemens process (CVD of polysilicon)

Purified TCS and hydrogen are fed into a bell-jar reactor containing thin, high-purity silicon rods heated electrically to about **1100 °C**. Silicon deposits on the rods by chemical vapour deposition:

    SiHCl₃ + H₂ → Si + 3HCl

The rods grow over many hours into thick bars of **electronic-grade polycrystalline silicon** (EG-Si), purity 9N to 11N. The by-products are recycled. EG-Si is still polycrystalline and undoped; the next step turns it into one crystal with the right doping.

## Stage 5: single-crystal growth

The polysilicon is melted and regrown as a single crystal by the **Czochralski (CZ)** method (most wafers) or the **float-zone (FZ)** method (very high resistivity). The ingot is then ground to diameter, given an orientation flat or notch, sliced into wafers with a wire saw, lapped, etched and chemically-mechanically polished.

## Part B: Czochralski bulk crystal growth

## The Czochralski method

@fig figures/cz.svg | Czochralski puller. The seed is dipped into the melt and slowly withdrawn while seed and crucible rotate in opposite directions; the melt freezes onto the seed with the seed's orientation.

**Principle.** A single-crystal **seed** of the desired orientation is dipped into molten silicon held just above its melting point (1414 °C). As the seed is slowly pulled up, the melt in contact with it cools and solidifies, and the atoms arrange themselves to continue the seed's lattice. The ingot therefore grows as one crystal with the seed's orientation.

**Equipment.** A fused-silica (quartz, SiO₂) crucible inside a graphite susceptor, heated by RF induction or resistance heaters; a seed holder on a rotating pull rod; a chamber filled with argon at reduced pressure; diameter control by optical sensing.

**Operation.**

1. Load EG-Si chunks and the dopant (B for p-type; P, As or Sb for n-type, often as a heavily doped Si alloy) into the crucible.
2. Evacuate and backfill with argon. Melt the charge at about 1420 °C.
3. Lower the seed until it just touches the melt and let it reach thermal equilibrium.
4. **Necking (Dash technique):** pull fast to grow a thin neck about 3 mm in diameter. Dislocations from the thermal shock of dipping run out of the side of the neck, so the crystal becomes dislocation-free.
5. **Shoulder and body:** reduce the pull rate to widen the crystal to full diameter, then grow the main body at constant diameter. Typical pull rate about 1 mm/min (a few mm/min for small diameters). Seed and crucible rotate in opposite directions (about 10–30 rpm) to mix the melt and keep the temperature and doping uniform.
6. **Tail:** increase the pull rate to narrow the diameter to a cone before separating from the melt, to avoid thermal shock dislocations running back up the crystal.
7. Cool slowly. Ingots up to 300 mm (12 inch) diameter and about 2 m long are routine.

The diameter is controlled by the **pull rate** and the **melt temperature**: pulling faster or making the melt hotter gives a thinner crystal.

### Dopant segregation

Impurities prefer the liquid. The **equilibrium segregation coefficient** is

    k₀ = C_s / C_l

where C_s and C_l are the concentrations in the solid and in the liquid at the interface. Most dopants have k₀ < 1:

| Impurity | B | P | As | Sb | Al | Ga | O | Fe |
|---|---|---|---|---|---|---|---|---|
| k₀ in Si | 0.8 | 0.35 | 0.3 | 0.023 | 0.002 | 0.008 | 0.25 | 8×10⁻⁶ |

As the crystal grows, rejected impurity accumulates in the shrinking melt, so the doping rises along the ingot. If C₀ is the initial melt concentration and f the fraction already solidified:

    C_s = k₀ C₀ (1 − f)^{k₀ − 1}

**Example.** To get boron at 1×10¹⁶ cm⁻³ in the first part of the crystal, the melt needs C₀ = C_s/k₀ = 1×10¹⁶/0.8 = 1.25×10¹⁶ cm⁻³. Half-way along (f = 0.5), C_s = 0.8 × 1.25×10¹⁶ × (0.5)^{−0.2} = 1.15×10¹⁶ cm⁻³, about 15 % higher. For P (k₀ = 0.35) the variation is much larger.

The same physics makes crystal growth a purification step: metals like Fe, with k₀ ≈ 10⁻⁵, are left behind in the melt.

### Float-zone (FZ) comparison

In FZ growth a polysilicon rod is held vertically and a narrow molten zone, produced by an RF coil, is moved along it from a seed. No crucible touches the melt, so oxygen and carbon contamination are very low and resistivity up to about 10⁴ Ω·cm is possible. FZ wafers are used for power devices and detectors, but diameters are limited (≤ 200 mm) and the process is more expensive.

## Part C: Epitaxial growth techniques

## Why epitaxy is needed

Bulk growth gives one uniformly doped crystal. Devices need thin layers of **different doping or composition** on top of each other, with sharp interfaces:

- A lightly doped layer on a heavily doped substrate (bipolar transistors, power diodes, CMOS latch-up prevention).
- Layers of a different material: AlGaAs on GaAs, InGaAs on InP, GaN on sapphire (heterostructures, quantum wells, lasers, HEMTs).
- Layers with fewer defects and less oxygen than CZ substrates.

**Homoepitaxy:** layer and substrate are the same material (Si on Si). **Heteroepitaxy:** different materials (GaAs on Si, AlGaAs on GaAs). In heteroepitaxy the **lattice mismatch** f = (a_layer − a_sub)/a_sub must be small, otherwise misfit dislocations form above a critical thickness.

## Vapour-phase epitaxy (VPE)

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

## Liquid-phase epitaxy (LPE)

**Principle.** The substrate is brought into contact with a melt (solution) of the semiconductor dissolved in a solvent metal, saturated at a set temperature. The melt is then cooled slowly. As the solubility falls, the solution becomes supersaturated and the excess semiconductor crystallises onto the substrate, continuing its lattice.

**Example:** GaAs dissolved in molten Ga, growth at about **700–900 °C** while cooling at about 0.1–1 °C/min. AlGaAs layers are grown by adding Al to the melt.

**Apparatus:** the **sliding-boat** (graphite boat with several wells holding different melts; the substrate slides under each in turn to grow a multilayer structure), or tipping and dipping systems.

**Features:** growth is close to thermodynamic equilibrium, so crystal quality is excellent and deep-level defect density is low; equipment is simple and cheap; growth rates are high (0.1–1 μm/min). But thickness control is poor (about 0.1 μm at best), interfaces are not abrupt, surface morphology is rough, the area is small, and some alloys cannot be grown. Historically used for the first double-heterostructure lasers and for LEDs; still used for some LEDs and thick layers.

## Molecular-beam epitaxy (MBE)

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

## Examination questions solved (Q9–Q13)

### Q9. Describe the major stages involved in converting metallurgical-grade silicon (MG-Si) into electronic-grade silicon (EG-Si).

**Starting point: production of MG-Si.** Quartzite is reduced with carbon in an electric arc furnace at about 2000 °C: SiO₂ + 2C → Si + 2CO. The product is about 98 % pure, with Fe, Al, Ca, B, P and C as the main impurities.

**Stage 1: Hydrochlorination (conversion to a volatile compound).** Pulverised MG-Si is reacted with anhydrous HCl at about 300 °C, usually with a catalyst in a fluidised bed: Si + 3HCl → SiHCl₃ + H₂. Silicon becomes trichlorosilane, a liquid boiling at 32 °C. Impurities form their own chlorides.

**Stage 2: Purification by fractional distillation.** Because SiHCl₃ and the impurity chlorides have different boiling points, repeated fractional distillation separates them, leaving SiHCl₃ with electrically active impurities at parts-per-billion levels.

**Stage 3: Reduction and deposition (Siemens process).** The purified SiHCl₃ is mixed with high-purity hydrogen and passed over electrically heated thin silicon filaments (about 1100 °C) in a CVD reactor: SiHCl₃ + H₂ → Si + 3HCl. Silicon deposits on the rods, which grow into thick polycrystalline bars of **electronic-grade silicon** (purity 9N–11N, i.e. 99.9999999 % or better). HCl and unreacted chlorosilanes are recovered and recycled.

**Stage 4 (to make device material): single-crystal growth.** The EG-Si polysilicon is broken into chunks, melted with the required dopant and grown into a single-crystal ingot by Czochralski or float-zone growth. Segregation during freezing purifies it further. The ingot is then shaped, sliced, lapped, etched and polished into wafers.

### Q10. Explain the principle and operation of the Czochralski (CZ) crystal growth method.

**Principle.** Crystal pulling from the melt. A small single-crystal seed of known orientation is brought into contact with molten silicon held slightly above its melting point (1414 °C). Heat is conducted away up the seed, so the melt at the seed–melt interface solidifies. The freezing atoms take up positions that continue the seed's lattice, so the growing ingot is a single crystal with the same orientation as the seed. Pull rate and temperature control the diameter.

**Equipment.** Furnace (quartz crucible in a graphite susceptor, RF or resistance heater); crystal-pulling mechanism (seed holder on a rotating, slowly rising shaft; crucible rotation and lift); ambient control (argon flow at reduced pressure); diameter and temperature control system.

**Operation.**

1. Polysilicon EG-Si and a precise amount of dopant are loaded into the crucible. The chamber is purged with argon and the charge is melted.
2. The seed is lowered to touch the melt surface.
3. A thin neck is pulled quickly (Dash necking) to eliminate dislocations.
4. The pull rate and temperature are lowered so the crystal widens (shoulder) to the target diameter.
5. The body is grown at constant diameter with typical pull rate about 1 mm/min while seed and crucible counter-rotate to stir the melt and keep it thermally symmetric.
6. At the end the diameter is tapered to a tail cone and the crystal is lifted clear and cooled slowly.

The finished ingot is then characterised for orientation, resistivity and defects before being sliced into wafers.

### Q11. State four advantages and two limitations of the Czochralski method.

**Advantages:**

1. **Large diameters**: 200 mm and 300 mm ingots are routine, which lowers cost per chip.
2. **Dislocation-free crystals** of controlled orientation ((100), (111)) from the seed, thanks to Dash necking.
3. **Controlled doping**: dopant added to the melt gives the required type and resistivity.
4. **High throughput and low cost**: mature, highly automated, relatively fast growth.
5. **Oxygen content strengthens the wafer** against warping and slip, and allows **intrinsic gettering** (oxygen precipitates in the bulk trap metallic impurities away from the device surface).

**Limitations:**

1. **Contamination from the crucible**: the quartz crucible dissolves slowly, introducing oxygen (≈ 10¹⁸ cm⁻³) and the graphite parts introduce carbon. Oxygen forms thermal donors and precipitates, and limits the attainable resistivity (CZ cannot easily exceed about 100 Ω·cm), so FZ is preferred for high-power and detector devices.
2. **Non-uniform axial doping** because of segregation (k₀ < 1): the dopant concentration rises from seed end to tail end, so resistivity varies along the ingot. Melt convection also causes radial non-uniformity and growth striations.

(Also acceptable: the crucible is consumed in each run; high energy consumption; batch process.)

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
