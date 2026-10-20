# Module 01 — Semiconductor Materials: Si, Ge and GaAs

Lecture note §1–§12. This module answers "what is a semiconductor, and which one do I use?".

## 1.1 What a semiconductor is

A **semiconductor** is a material whose electrical conductivity lies between that of a good conductor and an insulator, and whose conductivity can be **controlled** by temperature, illumination, electric field, magnetic field and impurity concentration.

The defining feature is not a particular conductivity value. It is a **finite, moderate energy gap** between occupied and unoccupied electron states. That gap is what makes the conductivity controllable, and controllability is what makes semiconductors useful for switching, amplification, rectification, sensing, energy conversion and computation.

Typical resistivity ranges at room temperature:

| Class | Resistivity ρ (Ω·cm) | Band picture | Examples |
|---|---|---|---|
| Conductor | 10⁻⁶ – 10⁻⁴ | Bands overlap, or a band is partly filled | Cu, Al, Ag |
| Semiconductor | 10⁻³ – 10⁸ | Moderate gap, about 0.1–3.5 eV | Si, Ge, GaAs |
| Insulator | 10¹⁰ – 10¹⁸ | Large gap, more than about 4 eV | SiO₂, glass, diamond |

@fig figures/bands.svg | Band pictures at room temperature. In a metal the highest band is partly filled. In a semiconductor a small gap lets some electrons cross by thermal excitation. In an insulator the gap is too wide for that.

### Temperature: the opposite behaviour

This is the cleanest way to tell a semiconductor from a metal:

- **Metal:** the number of free electrons is fixed and huge. Raising temperature only increases lattice vibration, which scatters electrons more. Resistance **rises** with temperature (positive temperature coefficient).
- **Semiconductor:** raising temperature breaks more covalent bonds and creates more electron–hole pairs, roughly as exp(−E_g/2kT). The carrier increase wins over the extra scattering. Resistance **falls** with temperature (negative temperature coefficient).
- **Insulator:** the gap is so large that almost no carriers are created even when hot.

## 1.2 Valence electrons

Electrons in the outermost shell are **valence electrons**; they form bonds and set the electrical behaviour.

- Si (Z = 14) and Ge (Z = 32) are Group 14 (IV). Each has 4 valence electrons and forms four directional covalent bonds.
- In GaAs, Ga is Group 13 (3 valence electrons) and As is Group 15 (5 valence electrons). The average is **4 per atom**, so GaAs also forms a tetrahedral crystal like Si.

This "average of four" rule is why III–V and II–VI compounds behave like Group IV semiconductors.

## 1.3 Elemental and compound semiconductors

**Elemental:** made of one element. Si, Ge (Group IV); also Se, Te, and diamond C (wide gap).

**Compound:** made of two or more elements, grouped by the periodic-table columns they come from:

- **III–V:** GaAs, InP, GaN, GaP, InSb, AlAs.
- **II–VI:** CdTe, ZnSe, ZnS, CdS.
- **IV–IV:** SiC, SiGe.
- **Ternary and quaternary alloys:** Al_{x}Ga_{1−x}As, In_{0.53}Ga_{0.47}As, InGaAsP.

The advantage of compounds is **band-gap engineering**. By choosing the elements and the alloy fraction x you choose the gap (and so the light wavelength), the mobility and the lattice constant.

## 1.4 The three materials in detail

### Silicon (Si)

- Diamond-cubic, a = 5.43 Å, **indirect** gap 1.12 eV.
- Second most abundant element in the Earth's crust (sand, quartz), so cheap.
- Grows a **stable, high-quality native oxide SiO₂**, the single most important reason for its dominance: it masks diffusion, passivates surfaces, and forms the MOS gate dielectric.
- Large gap compared with Ge, so low intrinsic carrier concentration (n_i ≈ 10¹⁰ cm⁻³), low leakage, and operation up to about 150 °C.
- Strong Si–Si bonds and good thermal conductivity (1.5 W/cm·K); large, dislocation-free crystals are routine.
- Limitation: indirect gap, so it is a poor light emitter. Electron mobility is moderate.

### Germanium (Ge)

- Diamond-cubic, a = 5.65 Å, **indirect** gap 0.66 eV.
- Higher electron and hole mobility than Si (μ_n ≈ 3900, μ_p ≈ 1900 cm²/V·s).
- Small gap means high n_i (≈ 2.4×10¹³ cm⁻³): large leakage current and strong temperature sensitivity. Usable only to about 70–80 °C.
- Its oxide GeO₂ is water-soluble and unstable, so no good MOS technology.
- Uses: infrared detectors and optics, high-speed SiGe heterojunction transistors, substrates for space solar cells.

### Gallium arsenide (GaAs)

- III–V compound, **zinc-blende** structure, a = 5.65 Å, **direct** gap 1.42 eV.
- Very high electron mobility (≈ 8500 cm²/V·s) and low effective mass: microwave and millimetre-wave devices (HEMTs, MESFETs).
- Direct gap gives efficient radiative recombination: LEDs and laser diodes (≈ 870 nm), and efficient solar cells.
- Can be made **semi-insulating** (ρ ≈ 10⁸ Ω·cm), an excellent substrate for RF integrated circuits.
- Limitations: expensive, brittle, arsenic is toxic, low hole mobility, no useful native oxide, poorer thermal conductivity (0.46 W/cm·K), smaller wafers.

## 1.5 Comparison table

| Property | Si | Ge | GaAs |
|---|---|---|---|
| Type | Elemental (IV) | Elemental (IV) | Compound (III–V) |
| Crystal | Diamond cubic | Diamond cubic | Zinc blende |
| Lattice constant | 5.43 Å | 5.65 Å | 5.65 Å |
| E_g at 300 K | 1.12 eV | 0.66 eV | 1.42 eV |
| Gap type | Indirect | Indirect | Direct |
| n_i (cm⁻³) | ≈ 1×10¹⁰ | ≈ 2.4×10¹³ | ≈ 2×10⁶ |
| μ_n (cm²/V·s) | 1350 | 3900 | 8500 |
| μ_p (cm²/V·s) | 480 | 1900 | 400 |
| Relative permittivity ε_r | 11.7 | 16.0 | 12.9 |
| Native oxide | Excellent SiO₂ | GeO₂, unstable | None useful |
| Main uses | ICs, power, sensors, solar | IR, high-speed, SiGe HBT | RF, microwave, LEDs, lasers |
| Relative cost | Low | Higher | High |

## 1.6 Material selection

- **Choose Si** for large-scale integration, low cost, mature processing, good oxide and power devices.
- **Choose GaAs** (or other III–V) for high frequency, high electron mobility, or light emission.
- **Choose Ge** (or SiGe) for high mobility or infrared work.
- **Wide-gap SiC and GaN** for high voltage, high temperature and high power (E_g ≈ 3.3 and 3.4 eV).

In practice it is a trade-off between band gap, mobility, thermal conductivity, breakdown field, defect density, cost and manufacturability.

---

## Exam questions solved

### Q1. Define a semiconductor and explain how its electrical conductivity differs from that of a conductor and an insulator.

**Definition.** A semiconductor is a material whose conductivity lies between that of conductors and insulators (resistivity roughly 10⁻³ to 10⁸ Ω·cm) and can be controlled by temperature, light, electric field and, above all, by adding small amounts of impurity (doping). Examples: Si, Ge, GaAs.

**Difference, explained with energy bands.**

1. **Conductor.** The valence and conduction bands overlap, or the highest band is only partly filled. There is no gap, so a huge number of free electrons (about 10²² cm⁻³) is always present. Conductivity is very high (σ ≈ 10⁶ S/cm) and almost independent of impurities. It **decreases** as temperature rises because lattice scattering increases.
2. **Insulator.** The valence band is full and the conduction band is empty, separated by a wide gap (E_g > about 4 eV, e.g. SiO₂ ≈ 9 eV). Thermal energy at room temperature (kT ≈ 0.026 eV) cannot lift electrons across, so there are practically no carriers. Conductivity is extremely small (σ < 10⁻¹⁰ S/cm).
3. **Semiconductor.** Same full/empty arrangement but a **small gap** (Si 1.12 eV). At room temperature a small fraction of electrons is thermally excited into the conduction band, leaving holes behind, so both electrons and holes conduct. Conductivity is moderate and **increases** with temperature (negative temperature coefficient of resistance), and can be raised by many orders of magnitude by doping.

**Summary.** Conductors have no gap and fixed, abundant carriers; insulators have a wide gap and essentially no carriers; semiconductors have a small gap, two carrier types, and a carrier density that can be engineered.

### Q2. Distinguish between elemental semiconductors and compound semiconductors, giving two examples of each.

| | Elemental | Compound |
|---|---|---|
| Composition | One chemical element | Two or more elements |
| Periodic table | Group IV (14) | Combinations such as III–V, II–VI, IV–IV |
| Crystal structure | Diamond cubic | Zinc blende or wurtzite |
| Bonding | Purely covalent | Covalent with partial ionic character |
| Band gap | Fixed by the element; Si and Ge are indirect | Adjustable by choice of elements and alloying; many are direct |
| Processing | Mature, cheap (especially Si) | More difficult and costly; stoichiometry must be controlled |
| Typical use | ICs, power, detectors | Optoelectronics, RF, high power |
| **Examples** | **Silicon (Si), Germanium (Ge)** | **Gallium arsenide (GaAs), Indium phosphide (InP)**; also GaN, SiC, CdTe |

### Q3. Explain why silicon is widely used in semiconductor device fabrication.

1. **Abundance and cost.** Si makes up about 28 % of the Earth's crust as SiO₂ (sand, quartz). Raw material is cheap and the refining industry is enormous.
2. **Excellent native oxide.** Silicon oxidises to SiO₂, which is stable, insoluble in water, an excellent insulator (E_g ≈ 9 eV, breakdown ≈ 10 MV/cm) and forms a very clean interface with Si (interface trap density about 10¹⁰ cm⁻²eV⁻¹). SiO₂ is used as a diffusion mask, surface passivation, field isolation and the MOSFET gate dielectric. No other semiconductor has a comparable oxide.
3. **Suitable band gap.** At 1.12 eV it is large enough to give low intrinsic concentration and low leakage, so devices work up to about 150 °C (Ge fails above about 75 °C), yet small enough for good conduction when doped.
4. **Mature crystal growth.** Very large (300 mm), nearly defect-free, highly pure single crystals are routinely grown by the Czochralski method.
5. **Mechanical and thermal strength.** Si is hard, can be handled as thin wafers, and conducts heat well (about 3 times better than GaAs), which matters in power devices and dense ICs.
6. **Well-understood doping.** B, P, As and Sb dope it predictably by diffusion and ion implantation.
7. **Elemental.** No stoichiometry to control and no toxic constituents, unlike GaAs.

Its main limitation is the indirect gap, which makes it a poor light emitter; that is why lasers and LEDs use compound semiconductors.

### Q4. Compare the properties and applications of silicon (Si), germanium (Ge), and gallium arsenide (GaAs).

Use the table in §1.5 as the core of the answer, then comment:

- **Structure and bonding.** Si and Ge are elemental, diamond cubic, purely covalent. GaAs is a III–V compound, zinc blende, mainly covalent with partial ionic character (As is more electronegative than Ga).
- **Band gap.** Ge (0.66 eV) < Si (1.12 eV) < GaAs (1.42 eV). The larger the gap, the lower n_i, the lower the leakage and the higher the maximum operating temperature. Si and Ge are **indirect**; GaAs is **direct**, so only GaAs emits light efficiently.
- **Mobility.** GaAs electrons are fastest (8500), then Ge (3900), then Si (1350) cm²/V·s. Hence GaAs and Ge suit high-speed work, though GaAs hole mobility is poor.
- **Oxide.** Only Si has an excellent native oxide, which is why MOS technology and VLSI are silicon.
- **Cost and processing.** Si cheapest and most mature; Ge more expensive; GaAs most expensive, brittle and toxic.

**Applications.**

- **Si:** microprocessors, memories, all digital and analogue ICs, MOSFETs and BJTs, power devices (IGBTs, thyristors), solar cells, sensors and MEMS.
- **Ge:** infrared detectors and lenses, high-speed SiGe heterojunction transistors, substrates for multi-junction space solar cells; historically the first transistors.
- **GaAs:** microwave and RF amplifiers in mobile phones and radar, satellite communication, HEMTs and MESFETs, LEDs, laser diodes for optical fibre links, high-efficiency solar cells for satellites.
