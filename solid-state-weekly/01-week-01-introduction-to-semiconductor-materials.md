# Week 1 — Introduction to Semiconductor Materials
<!-- group: Module 1 · Material Physics & Semiconductor Growth -->

**Plan:** elemental vs compound semiconductors (Si, Ge, GaAs); crystal structures, Miller indices and bonding mechanisms. This page follows the issued Lecture 2 notes in their own order, then goes to the depth the examination needs.

## Learning objectives

By the end of this week you should be able to:

1. Define a semiconductor and distinguish it from a conductor and an insulator.
2. Describe the atomic structure of Si, Ge, Ga and As and identify their valence electrons.
3. Explain covalent bonding in silicon and electron–hole pair generation.
4. Distinguish intrinsic, n-type and p-type semiconductors, and donors from acceptors.
5. Compare elemental and compound semiconductors, and Si, Ge and GaAs.
6. Explain the energy-band picture, the band gap and direct versus indirect gaps.
7. Describe crystal lattices, unit cells and the diamond and zinc-blende structures.
8. Determine Miller indices of planes and the spacing between planes.

> **How to read this page.** Read it in order: each section builds on the one before. The tables and boxed equations are the parts to memorise; the paragraphs around them explain why they are true. The key points at the end summarise the week, and the solved revision and exam questions show how to write the answers.

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
| m₀ | Free-electron mass | 9.11×10⁻³¹ kg |
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| Å | Ångström, a unit of length | 1 Å = 10⁻¹⁰ m = 0.1 nm |
| μm | Micrometre (micron) | 1 μm = 10⁻⁴ cm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_c (E_C) | Energy of the bottom of the conduction band | eV |
| E_v (E_V) | Energy of the top of the valence band | eV |
| E_g | Band-gap energy, E_c − E_v | eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K |
| E_F | Fermi level: the energy at which a state has a 50 % chance of being occupied | eV |
| n | Electron concentration (free electrons per cm³) | cm⁻³ |
| p | Hole concentration (holes per cm³) | cm⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | cm⁻³; Si ≈ 1×10¹⁰ at 300 K |
| N_D | Donor concentration | cm⁻³ |
| N_A | Acceptor concentration | cm⁻³ |
| k (wave vector) | Wave vector, 2π/λ; measures the electron's momentum, p = ħk | m⁻¹ or cm⁻¹ |
| λ | Wavelength | μm or nm; λ(μm) = 1.24/E(eV) |
| ν, hν | Frequency of light, and photon energy | Hz; eV |
| a | Lattice constant: edge length of the cubic unit cell | Å; Si 5.43, Ge and GaAs 5.65 |
| (h k l), {h k l} | Miller indices of a plane; family of equivalent planes | integers |
| [u v w], ⟨u v w⟩ | A crystal direction; family of equivalent directions | integers |
| d_hkl | Spacing between neighbouring (h k l) planes, a/√(h² + k² + l²) | Å |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | cm²/(V·s); Si μ_n 1350, μ_p 480 |
| v_d | Drift velocity | cm/s |
| σ | Conductivity, q(nμ_n + pμ_p) (in Week 8, σ is also a capture cross-section) | S/cm (siemens per cm) |
| ρ | Resistivity, 1/σ | Ω·cm |
| α, β, γ (cell) | Angles between the edges of a unit cell | degrees; 90° for cubic |
| f_T | Transition (cut-off) frequency | Hz |
| λ_max | Longest wavelength a material absorbs, 1.24/E_g (μm, E_g in eV) | μm |
| σ_i, ρ_i | Conductivity and resistivity of intrinsic (undoped) material; σ_doped after doping | S/cm; Ω·cm |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| Ge | Germanium |
| GaAs | Gallium arsenide |
| GaN | Gallium nitride |
| SiC | Silicon carbide |
| InP | Indium phosphide |
| GaP | Gallium phosphide |
| SiO₂ | Silicon dioxide (silica), the oxide insulator |
| FCC | Face-centred cubic lattice |
| BCC | Body-centred cubic lattice |
| SC | Simple cubic lattice |
| APF | Atomic packing factor |
| III–V | Compound of Group III and Group V elements (e.g. GaAs) |
| MOS | Metal–oxide–semiconductor |
| MOSFET | Metal–oxide–semiconductor field-effect transistor |
| MESFET | Metal–semiconductor field-effect transistor |
| HEMT | High-electron-mobility transistor |
| BJT | Bipolar junction transistor |
| HBT | Heterojunction bipolar transistor |
| IC | Integrated circuit |
| VLSI | Very-large-scale integration |
| LED | Light-emitting diode |
| RF | Radio frequency |
| IGBT | Insulated-gate bipolar transistor |
| MEMS | Micro-electro-mechanical systems |
| LCM | Lowest common multiple |
| KOH | Potassium hydroxide (an anisotropic silicon etchant) |
| UV | Ultraviolet |


## Introduction

Semiconductor materials are the foundation of modern electronic and electrical systems. Almost every modern electronic device depends on them, including computers, mobile phones, solar cells, sensors, communication systems, power converters and control systems.

A **semiconductor** is a material whose electrical conductivity lies between that of a good conductor and an insulator. More importantly, its conductivity can be **controlled** by temperature, light, electric fields, magnetic fields, and the intentional addition of impurities known as **dopants**.

The most important semiconductor materials used in electronics are:

| Material | Type | Where you meet it |
|---|---|---|
| Silicon (Si) | Elemental | ICs, microprocessors, solar cells, power devices |
| Germanium (Ge) | Elemental | Early transistors, infrared, SiGe high-speed transistors |
| Gallium arsenide (GaAs) | Compound (III–V) | Microwave, RF, LEDs, lasers |
| Gallium nitride (GaN) | Compound (III–V), wide gap | Blue/white LEDs, power and RF transistors |
| Silicon carbide (SiC) | Compound (IV–IV), wide gap | High-voltage, high-temperature power electronics |
| Indium phosphide (InP) | Compound (III–V) | Fibre-optic lasers and detectors, very high-speed circuits |
| Gallium phosphide (GaP) | Compound (III–V) | Red, yellow and green indicator LEDs |

## What is a semiconductor?

A semiconductor is a material whose electrical conductivity lies between that of a conductor and an insulator, and can be **significantly controlled** by temperature, impurities, light or applied electric fields. Examples: silicon (Si), germanium (Ge) and gallium arsenide (GaAs).

Its conductivity is **not fixed**, and that is exactly what makes it useful for electronic devices. Pure silicon at room temperature conducts poorly. When a small, controlled quantity of an impurity such as phosphorus or boron is introduced, its conductivity rises dramatically: one phosphorus atom per million silicon atoms raises the conductivity about 100,000 times. This process is called **doping**.

## Classification of materials by electrical conductivity

Materials can broadly be classified into **conductors**, **semiconductors** and **insulators**.

**Conductors** have a large number of free electrons available for electrical conduction. Examples: copper, aluminium, silver, gold, iron. Copper is widely used in electrical wiring because of its high conductivity. Characteristics:

- high electrical conductivity (σ ≈ 10⁵–10⁶ S/cm);
- low electrical resistivity (Cu: 1.7×10⁻⁶ Ω·cm);
- large number of free charge carriers (about 10²² cm⁻³);
- small, or effectively overlapping, energy gap.

**Insulators** have very few free charge carriers under normal conditions. Examples: glass, rubber, plastic, ceramic, mica. They strongly resist the flow of electric current. Characteristics:

- very high resistivity (10¹⁰–10¹⁸ Ω·cm);
- very low conductivity;
- large energy band gap (more than about 4 eV; SiO₂ ≈ 9 eV);
- electrons strongly bound to their atoms.

**Semiconductors** have conductivity between conductors and insulators. Examples: silicon, germanium, gallium arsenide, silicon carbide, gallium nitride. Their conductivity can be modified through **temperature, doping, illumination, electric field, magnetic field and mechanical stress**. This controllability is one of the most important characteristics of semiconductor materials.

@fig figures/bands.svg | Band pictures at room temperature. In a metal the highest band is partly filled; in a semiconductor a small gap lets some electrons cross by thermal excitation; in an insulator the gap is too wide.

### Comparison of conductors, semiconductors and insulators

| Property | Conductor | Semiconductor | Insulator |
|---|---|---|---|
| Conductivity | Very high | Moderate, controllable | Very low |
| Resistivity | Very low | Intermediate | Very high |
| Band gap | Approximately zero | Small (≈ 0.5–3.5 eV) | Large (> 4 eV) |
| Free electrons | Many | Moderate, controllable | Very few |
| Temperature effect | Conductivity usually **decreases** | Conductivity usually **increases** | Small effect under normal conditions |
| Examples | Cu, Ag, Al | Si, Ge, GaAs | Glass, rubber, plastic |
| Main application | Wiring | Electronic devices | Electrical isolation |

**Why the temperature effect is opposite.** In a metal the number of free electrons is fixed; heating only makes the lattice vibrate more, which scatters electrons, so resistance rises. In a semiconductor heating breaks covalent bonds and creates many more carriers (roughly as e^{−E_g/2kT}); the extra carriers far outweigh the extra scattering, so resistance falls.

## Atomic structure of semiconductor materials

An atom consists of a **nucleus** containing **protons** (positive) and **neutrons** (neutral), with **electrons** (negative) occupying different energy levels (shells) around it, as in the Bohr model. The electrons in the outermost shell are the most important in determining the electrical properties of a material. These are the **valence electrons**.

@fig figures/bohr-si.svg | Bohr model of silicon (Z = 14): shells hold 2, 8 and 4 electrons. The four outer electrons are the valence electrons.

### Valence electrons

The electrons in the outermost energy level of an atom are its **valence electrons**. They take part in chemical bonding.

| Atom | Z | Electron configuration | Valence electrons | Group |
|---|---|---|---|---|
| Silicon (Si) | 14 | 1s²2s²2p⁶3s²3p² (shells 2, 8, 4) | 4 | IV (14) |
| Germanium (Ge) | 32 | 1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p² (shells 2, 8, 18, 4) | 4 | IV (14) |
| Gallium (Ga) | 31 | [Ar]3d¹⁰4s²4p¹ | 3 | III (13) |
| Arsenic (As) | 33 | [Ar]3d¹⁰4s²4p³ | 5 | V (15) |

Silicon's atomic mass is 28.085. The difference in valence electrons between Ga (3) and As (5) is what allows them to combine into a compound semiconductor (average 4 per atom), and the difference between Si (4) and P (5) or B (3) is what makes doping work.

## Covalent bonding in silicon

Silicon atoms form a **covalent bonding structure**. Each silicon atom has four valence electrons and **shares** them with four neighbouring silicon atoms, so each atom forms **four covalent bonds** and is surrounded by eight shared electrons (a full outer shell).

@fig figures/si-bonds.svg | Two-dimensional picture of the silicon crystal. Each Si atom shares one electron pair with each of four neighbours. One bond has been broken by thermal energy, creating a free electron and a hole.

- The shared electrons hold the crystal structure together.
- At very low temperatures nearly all electrons stay in the covalent bonds, so electrical conductivity is very low (pure Si is an insulator at 0 K).
- When sufficient energy is supplied (heat, light), some electrons break away from their bonds and become mobile.

## Electron–hole pair generation

When a valence electron receives sufficient energy (at least E_g = 1.12 eV in Si) from thermal excitation, it can leave its covalent bond:

- the electron becomes a **free electron**;
- the vacancy it leaves behind in the bond is called a **hole**.

    Energy supplied → electron–hole pair

- The electron carries negative charge, q = −1.6×10⁻¹⁹ C.
- The hole behaves as if it has positive charge, q = +1.6×10⁻¹⁹ C. A neighbouring bond electron can jump into the hole, so the hole moves in the opposite direction to that electron.
- **Both electrons and holes contribute to electrical conduction** in semiconductors. This two-carrier conduction is what separates semiconductors from metals.

The reverse process, a free electron falling back into a hole, is **recombination** (Week 8).

## Intrinsic semiconductor

An **intrinsic semiconductor** is a pure semiconductor without intentionally introduced impurities. Examples: pure silicon, pure germanium. Every free electron came from a broken bond that also left a hole, so

    n = p = n_i

where n is the electron concentration, p the hole concentration and n_i the **intrinsic carrier concentration** (Si: about 1×10¹⁰ cm⁻³ at 300 K; Ge: 2.4×10¹³ cm⁻³). The number of electrons equals the number of holes. In thermal equilibrium the product is constant:

    n · p = n_i²   (mass-action law, true for doped material too)

## Extrinsic semiconductor

An **extrinsic semiconductor** is one whose electrical properties have been deliberately modified by adding controlled impurities. This process is **doping**. There are two major types: **n-type** and **p-type**.

### N-type semiconductor

Produced by adding a **pentavalent impurity** (five valence electrons): phosphorus (P), arsenic (As) or antimony (Sb). Suppose phosphorus is added to silicon. Four of its five valence electrons form covalent bonds with neighbouring Si atoms; the fifth is only weakly bound (about 0.045 eV) and easily becomes a free electron. The phosphorus atom is called a **donor**, and it is left as a fixed positive ion.

- Majority carriers = **electrons**; minority carriers = **holes**.
- n ≈ N_D (donor concentration), p = n_i²/N_D.

### P-type semiconductor

Produced by adding a **trivalent impurity** (three valence electrons): boron (B), aluminium (Al), gallium (Ga) or indium (In). When boron is introduced into silicon, only three covalent bonds can be completed. An electron is missing from the fourth bond; this missing electron is a **hole**. A neighbouring electron easily moves in, so the hole wanders through the crystal. Boron is called an **acceptor**, and it is left as a fixed negative ion.

- Majority carriers = **holes**; minority carriers = **electrons**.
- p ≈ N_A (acceptor concentration), n = n_i²/N_A.

@fig figures/dopant-lattice.svg | Left: a phosphorus atom in silicon donates its fifth electron (n-type). Right: a boron atom leaves one bond incomplete, creating a hole (p-type).

#### Example 1.1: carriers in n-type silicon

**Question.** Silicon at 300 K is doped with 10¹⁶ cm⁻³ phosphorus atoms. Taking n_i = 1×10¹⁰ cm⁻³ and assuming every donor is ionised, calculate the electron and hole concentrations and state which carrier is the majority.

**Given:** N_D = 1×10¹⁶ cm⁻³, n_i = 1×10¹⁰ cm⁻³, T = 300 K, complete ionisation.

**Find:** n, p, and the majority carrier.

**Solution.**

Step 1. Each phosphorus atom gives one free electron, and N_D ≫ n_i, so

    n ≈ N_D = 1×10¹⁶ cm⁻³

Step 2. The mass-action law np = n_i² gives the holes:

    p = n_i²/n = (1×10¹⁰)² / (1×10¹⁶) = 10²⁰/10¹⁶ = 1×10⁴ cm⁻³

**Answer:** **n = 1×10¹⁶ cm⁻³, p = 1×10⁴ cm⁻³.** Electrons are the majority carriers; they outnumber the holes by 10¹².

## Elemental semiconductors

An **elemental semiconductor** is made primarily from a single chemical element.

- **Silicon (Si):** atomic number 14, four valence electrons. Widely used in integrated circuits, power electronics and solar cells.
- **Germanium (Ge):** atomic number 32, four valence electrons. Higher carrier mobility than silicon, lower band gap. Used in specialised high-speed and infrared applications.

## Compound semiconductors

**Compound semiconductors** consist of two or more different elements. Examples: GaAs, GaN, InP, GaP, CdTe. They can provide properties that are difficult to achieve with elemental semiconductors:

- **GaAs** has high electron mobility and is useful in high-frequency electronic systems.
- **GaN** has a wide band gap (3.4 eV) and is important in power electronics, LEDs, RF systems and high-temperature electronics.

They are named by the periodic-table groups of their elements: **III–V** (GaAs, GaN, InP, GaP), **II–VI** (CdTe, ZnSe), **IV–IV** (SiC, SiGe). By alloying (e.g. Al_{x}Ga_{1−x}As) the band gap can be tuned, which is called band-gap engineering.

## Silicon, germanium and gallium arsenide

### Silicon

Silicon is the most widely used semiconductor material in modern electronics.

- Atomic number 14; four valence electrons; diamond-cubic crystal structure.
- Band gap E_g ≈ 1.12 eV at room temperature.
- Used for microprocessors, memory chips, diodes, transistors, solar cells, power devices, sensors and integrated circuits.

Why it dominates: it is abundant (sand), cheap, grows an excellent native oxide (SiO₂), has a band gap large enough for low leakage up to about 150 °C, and can be grown as huge, nearly perfect crystals.

### Germanium

Germanium was one of the earliest semiconductor materials, used extensively for early transistor technology (the first transistor, 1947, was germanium).

- Four valence electrons; diamond-cubic crystal structure.
- Band gap E_g ≈ 0.66 eV at room temperature.
- **Advantages:** high carrier mobility; useful for high-speed applications; useful in infrared technology.
- **Disadvantages:** smaller band gap; higher leakage current; less suitable than silicon for high-temperature applications (works only to about 75 °C).

### Gallium arsenide

Gallium arsenide is a compound semiconductor of gallium and arsenic (Ga + As), abbreviated **GaAs**.

- Band gap E_g ≈ 1.42 eV at room temperature (direct).
- High electron mobility (about 8500 cm²/V·s, six times silicon), so it is particularly useful for high-frequency and optoelectronic applications.
- Applications: microwave circuits, satellite communication, radar, high-frequency amplifiers, LEDs, laser diodes, photodetectors, solar cells.

### Comparison of Si, Ge and GaAs

| Property | Silicon | Germanium | GaAs |
|---|---|---|---|
| Symbol | Si | Ge | GaAs |
| Type | Elemental | Elemental | Compound |
| Valence electrons | 4 | 4 | III–V compound (average 4) |
| Band gap | ≈ 1.12 eV | ≈ 0.66 eV | ≈ 1.42 eV |
| Crystal structure | Diamond cubic | Diamond cubic | Zinc blende |
| Electron mobility | Moderate (1350) | High (3900) | Very high (8500) |
| Thermal stability | Good | Lower | Good |
| Cost | Relatively low | Higher | High |
| IC manufacturing | Excellent | Limited | Specialised |
| High-frequency use | Good | Good | Excellent |
| Optical applications | Limited | Good (infrared) | Excellent |

(Mobilities in cm²/V·s at 300 K, added for reference.)

## Energy band concept

The electrical behaviour of a semiconductor is explained using **energy bands**. When many atoms come together to form a solid, the discrete energy levels of the individual atoms spread into closely spaced energy states called **energy bands**. The two most important are:

- **Valence band:** contains electrons involved in bonding.
- **Conduction band:** contains electrons that can move through the material and contribute significantly to conduction.

Between them is the **forbidden energy gap**, or **band gap E_g**.

### Energy band gap

The band gap is the energy difference between the conduction band and the valence band:

    E_g = E_C − E_V

where E_C is the conduction-band energy (bottom of the conduction band) and E_V the valence-band energy (top of the valence band). It is normally measured in **electron-volts** (1 eV = 1.6×10⁻¹⁹ J).

**Why the band gap is important.** It strongly affects semiconductor behaviour. A smaller band gap makes it easier for electrons to gain enough energy to enter the conduction band; a larger band gap makes it harder. The band gap influences:

- **electrical conductivity** (n_i ∝ e^{−E_g/2kT});
- **temperature dependence** of conductivity;
- **optical absorption** (only photons with hν ≥ E_g are absorbed);
- **light emission** (emitted wavelength λ = 1.24/E_g μm);
- **leakage current** (smaller gap, more leakage);
- **breakdown behaviour** (wider gap, higher breakdown field);
- **device operating temperature** (wider gap, hotter operation).

## Direct and indirect band-gap semiconductors

Semiconductors are classified by the relationship between the valence-band maximum and the conduction-band minimum in momentum (k).

**Direct band gap:** electrons can transition between the conduction and valence bands without a significant change in momentum. Examples: GaAs, GaN, InP. These are suitable for **light-emitting devices**: LEDs, laser diodes, optical communication.

**Indirect band gap:** a momentum change is required during the transition, supplied by a lattice vibration (phonon). Examples: silicon, germanium. Silicon is therefore **not an efficient light emitter**.

@fig figures/ek.svg | E–k diagrams. In GaAs the band extrema line up at the same k, so an electron can drop straight down and emit a photon. In Si they are at different k, so a phonon must also take part.

## Semiconductor crystal structure

A semiconductor is not simply a collection of independent atoms. The atoms are arranged in an ordered three-dimensional pattern called a **crystal lattice**, and this crystal structure determines many of its physical properties. The important concepts are: lattice, unit cell, crystal planes, crystal directions, Miller indices and atomic bonding.

### Crystal lattice and unit cell

- A **crystal lattice** is a regular, repeating arrangement of atoms or points in space.
- A semiconductor crystal can be described by repeating a basic structural unit known as the **unit cell**.
- The unit cell contains enough information to reproduce the entire crystal by translation.

## The cubic lattices

| Structure | Atoms per cell | Coordination no. | Nearest-neighbour distance | APF |
|---|---|---|---|---|
| Simple cubic (SC) | 1 | 6 | a | 0.52 |
| Body-centred cubic (BCC) | 2 | 8 | (√3/2)a | 0.68 |
| Face-centred cubic (FCC) | 4 | 12 | (√2/2)a | 0.74 |
| Diamond cubic | 8 | 4 | (√3/4)a | 0.34 |

Counting atoms in a cubic cell: a corner atom is shared by 8 cells (counts 1/8), a face atom by 2 (counts 1/2), a body atom by 1.

- SC: 8 × 1/8 = 1
- BCC: 8 × 1/8 + 1 = 2
- FCC: 8 × 1/8 + 6 × 1/2 = 4
- Diamond: 8 × 1/8 + 6 × 1/2 + 4 inside = 8

### Silicon crystal structure

- Silicon has a **diamond-cubic** crystal structure.
- It can be regarded as **two interpenetrating face-centred cubic (FCC)** structures, displaced from each other by a quarter of the body diagonal.
- Each silicon atom has **four nearest-neighbour** silicon atoms, arranged at the corners of a tetrahedron (bond angle 109.5°).
- The bonding is predominantly **covalent**.
- This structure is responsible for many of silicon's useful semiconductor properties.

For Si (a = 5.43 Å): nearest-neighbour distance = (√3/4)a = 2.35 Å; atom density = 8/a³ = 5.0×10²² atoms/cm³.

### Germanium crystal structure

- Germanium also has the diamond-cubic structure; each Ge atom forms four covalent bonds with neighbouring Ge atoms.
- Silicon and germanium therefore have similar bonding arrangements, but their atomic sizes (a = 5.65 Å for Ge) and electronic properties differ.

### GaAs crystal structure

- GaAs forms the **zinc-blende** crystal structure under ordinary conditions.
- It consists of two interpenetrating FCC sublattices, one occupied by gallium and the other by arsenic. Each Ga has four As neighbours and vice versa.
- The bonding is mainly covalent with partial ionic character (As is more electronegative than Ga). This structure contributes to its important electronic and optical properties.

### Lattice constant

The **lattice constant** is a characteristic dimension of a crystal unit cell. For a cubic crystal it is written **a** and measured in metres, nanometres or angstroms (1 Å = 10⁻¹⁰ m = 0.1 nm). Si: 5.43 Å; Ge: 5.65 Å; GaAs: 5.65 Å.

The lattice constant determines: atomic spacing; crystal density; crystal matching between materials; epitaxial growth (a layer grows well only on a substrate with nearly the same a); and semiconductor heterostructures (e.g. AlGaAs on GaAs works because their lattice constants are almost identical).

## Miller indices

Miller indices provide a standard notation for crystallographic planes and directions:

| Notation | Meaning |
|---|---|
| (h k l) | A plane |
| {h k l} | A family of equivalent planes |
| [u v w] | A direction |
| ⟨u v w⟩ | A family of equivalent directions |

They are important in wafer orientation, crystal growth, etching, diffraction and device fabrication.

### Procedure

1. Determine the plane's intercepts on the x, y and z axes in lattice units.
2. Take the reciprocals of the intercepts.
3. Multiply by a common factor to obtain the smallest integers.
4. Write the result as (h k l).

- An intercept of **∞** gives an index of **0**, because the plane is parallel to that axis.
- **Negative** indices are shown with a bar, e.g. (1̄10).

@fig figures/planes.svg | The three most important planes in a cubic crystal. MOS wafers are cut on (100); bipolar and some power wafers on (111).

### Examples (from the lecture)

#### Example 1.2: Miller indices of a plane

**Question.** A crystal plane cuts the x, y and z axes at a, 2b and 3c respectively. Determine its Miller indices.

**Given:** intercepts a, 2b, 3c, i.e. 1, 2, 3 in lattice units.

**Find:** (h k l).

**Solution.**

| Step | x | y | z |
|---|---|---|---|
| Intercepts (lattice units) | 1 | 2 | 3 |
| Reciprocals | 1 | 1/2 | 1/3 |
| Multiply by the LCM, 6 | 6 | 3 | 2 |

**Answer:** **(6 3 2).** Remember: Miller indices come from the **reciprocals** of the intercepts, not the intercepts themselves.

#### Example 1.3: a plane parallel to an axis

**Question.** A plane has intercepts x = a, y = 2b and is parallel to the z-axis (z = ∞). Determine its Miller indices.

**Given:** intercepts 1, 2, ∞ in lattice units.

**Find:** (h k l).

**Solution.**

| Step | x | y | z |
|---|---|---|---|
| Intercepts | 1 | 2 | ∞ |
| Reciprocals | 1 | 1/2 | 0 |
| Multiply by 2 | 2 | 1 | 0 |

**Answer:** **(2 1 0).** The zero shows that the plane is parallel to the z-axis.

### Interplanar spacing (cubic crystals)

    d_{hkl} = a / √(h² + k² + l²)

For Si, d₁₁₁ = 5.43/√3 = 3.135 Å and d₁₀₀ = 5.43 Å. In cubic crystals the direction [h k l] is perpendicular to the plane (h k l).

## Why orientation matters in processing

- **Surface atom density** differs by plane: in Si, (100) has 6.8×10¹⁴ atoms/cm², (111) has 7.8×10¹⁴ atoms/cm².
- **Oxidation rate:** (111) oxidises faster than (100).
- **Interface traps:** (100) gives the lowest Si/SiO₂ interface-state density, so **MOS technology uses (100) wafers**.
- **Anisotropic etching:** KOH etches (100) far faster than (111), giving V-grooves with 54.7° walls, used in MEMS.
- **Cleavage:** wafers break along {111} planes in Si and {110} in GaAs.
- **Epitaxy:** the substrate orientation and lattice constant set the orientation and quality of the grown layer.
- **Ion implantation channelling:** along low-index directions ions travel deep; wafers are tilted about 7° to avoid it.

## Bonding mechanisms (exam depth)

## The bonding mechanisms

**Ionic bonding.** One atom transfers electrons to another, producing positive and negative ions held together by electrostatic (Coulomb) attraction. Occurs between elements of very different electronegativity, e.g. Na⁺Cl⁻. The bond is strong but **non-directional**. Electrons are tightly bound to the ions, so ionic solids are insulators with large gaps; they are hard, brittle and have high melting points.

**Covalent bonding.** Neighbouring atoms **share** pairs of valence electrons, one electron from each, so each atom completes its outer shell (8 electrons). The bond is strong and **directional**, which fixes the crystal geometry (tetrahedral, 109.5°). Electrons are localised in bonds at low temperature but can be freed by modest energy, which gives semiconducting behaviour. Examples: Si, Ge, diamond.

**Metallic bonding.** Valence electrons leave their atoms and form a delocalised "sea" or gas of electrons shared by the whole crystal, holding a lattice of positive ion cores together. Non-directional. The free electron sea explains the high electrical and thermal conductivity, lustre and ductility of metals. Examples: Cu, Al, Na.

**Van der Waals bonding.** Weak attraction between fluctuating dipoles in neutral atoms or molecules. Important in layered materials (graphite, MoS₂) and noble-gas solids, not in Si or GaAs.

**Mixed ionic–covalent.** Real compound semiconductors lie between the ideal limits.

| | Ionic | Covalent | Metallic |
|---|---|---|---|
| Mechanism | Electron transfer, ion attraction | Electron-pair sharing | Shared electron sea |
| Directional? | No | Yes | No |
| Free electrons | None | Few (created thermally) | Very many |
| Electrical behaviour | Insulator | Semiconductor (or insulator) | Conductor |
| Example | NaCl | Si, Ge, C | Cu, Al |

## Defects in real crystals

| Type | Dimension | Examples | Effect |
|---|---|---|---|
| Point | 0-D | Vacancy, self-interstitial, substitutional or interstitial impurity, Frenkel pair (vacancy + interstitial) | Traps, recombination centres; vacancies assist diffusion |
| Line | 1-D | Edge and screw dislocations | Leakage paths, recombination along the line, enhanced diffusion |
| Planar | 2-D | Grain boundaries, stacking faults, twin boundaries, surfaces and interfaces | Scattering, interface traps, junction leakage |
| Volume | 3-D | Voids, precipitates (e.g. SiO₂ clusters), inclusions | Gettering sites if controlled, device failure if not |

Defects act as **scattering centres** (lower mobility), **recombination–generation centres** (shorter lifetime, more leakage), **traps** (charge storage and noise) and **diffusion paths**. Not all impurities are unwanted: deliberate dopants are substitutional point defects.

## Key points of Week 1

- A semiconductor's conductivity lies between a conductor's and an insulator's and can be **controlled**, above all by doping.
- Conductors: bands overlap, conductivity falls when hot. Insulators: gap > 4 eV. Semiconductors: gap ≈ 1 eV, conductivity rises when hot.
- Si and Ge have 4 valence electrons and form 4 covalent bonds (diamond cubic). GaAs averages 4 per atom (zinc blende).
- Breaking a bond (energy ≥ E_g) makes an electron–hole pair; both carry current. Intrinsic: n = p = n_i.
- Pentavalent donors (P, As, Sb) → n-type, electrons majority. Trivalent acceptors (B, Al, Ga, In) → p-type, holes majority. np = n_i².
- E_g = E_C − E_V sets conductivity, leakage, light emission (λ = 1.24/E_g μm) and maximum temperature. Direct gap (GaAs) emits light; indirect (Si) does not.
- Miller indices: intercepts → reciprocals → smallest integers → (h k l); ∞ gives 0. d = a/√(h² + k² + l²).

---

## Lecture revision questions solved

These are the lecturer's own Week 1 revision questions (Lecture 2, pages 41–43), in her order.

### R1. Define a semiconductor.

A semiconductor is a material whose electrical conductivity lies between that of a conductor and an insulator (ρ ≈ 10⁻³ to 10⁸ Ω·cm), and whose conductivity can be significantly controlled by temperature, light, electric and magnetic fields, and especially by adding small amounts of impurities (doping). Examples: Si, Ge, GaAs.

### R2. Distinguish between a conductor, semiconductor and insulator.

A **conductor** has many free electrons and overlapping (or no) band gap, very high conductivity, and its conductivity falls as temperature rises (Cu, Ag, Al). An **insulator** has a large band gap (> 4 eV), very few free carriers, very high resistivity, and is used for isolation (glass, rubber, mica). A **semiconductor** has a small band gap (Si 1.12 eV), a moderate and controllable number of carriers (both electrons and holes), and its conductivity rises with temperature and with doping (Si, Ge, GaAs). See the comparison table above.

### R3. What are valence electrons?

Valence electrons are the electrons in the outermost energy level (shell) of an atom. They take part in chemical bonding and determine the electrical properties of a material. Silicon has 4, gallium 3, arsenic and phosphorus 5, boron 3.

### R4. Why does silicon have four valence electrons?

Silicon has atomic number Z = 14, so its 14 electrons fill the shells as 2, 8 and 4 (configuration 1s²2s²2p⁶3s²3p²). The first two shells (n = 1 and n = 2) are complete; the third shell (n = 3) holds only 3s²3p², i.e. **4 electrons**. These four outer electrons are the valence electrons, which places silicon in Group IV (14) of the periodic table.

### R5. Explain covalent bonding in silicon.

Each silicon atom has four valence electrons. In the crystal it shares one electron with each of four neighbouring Si atoms, and each neighbour shares one back, so each pair of atoms is joined by a shared **electron pair** (a covalent bond). Each atom therefore forms four covalent bonds, arranged tetrahedrally at 109.5° (diamond-cubic structure), and is surrounded by eight shared electrons, a stable full shell. The shared electrons hold the crystal together. At low temperature all electrons are locked in bonds, so pure Si hardly conducts; when energy of at least 1.12 eV is supplied, a bond breaks and creates a free electron and a hole.

### R6. Define intrinsic semiconductor.

An intrinsic semiconductor is a pure semiconductor with no intentionally added impurities, in which carriers are produced only by thermal breaking of bonds. Electrons and holes are therefore equal in number: n = p = n_i (Si: n_i ≈ 1×10¹⁰ cm⁻³ at 300 K).

### R7. Define extrinsic semiconductor.

An extrinsic semiconductor is one whose electrical properties have been deliberately modified by adding controlled amounts of impurity atoms (doping). It is n-type if doped with donors (electrons are majority carriers) or p-type if doped with acceptors (holes are majority carriers). n ≠ p, but np = n_i² still holds.

### R8. What is doping?

Doping is the deliberate, controlled introduction of small amounts of specific impurity atoms (typically 10¹⁴–10²⁰ cm⁻³) into a pure semiconductor to increase its conductivity and set its carrier type. Pentavalent dopants (P, As, Sb) give n-type material; trivalent dopants (B, Al, Ga, In) give p-type. Methods are covered in Week 3 (diffusion and ion implantation).

### R9. Differentiate between n-type and p-type semiconductors.

| | n-type | p-type |
|---|---|---|
| Impurity | Pentavalent (P, As, Sb) | Trivalent (B, Al, Ga, In) |
| Impurity name | Donor | Acceptor |
| Majority carriers | Electrons | Holes |
| Minority carriers | Holes | Electrons |
| Fixed ion left | Positive | Negative |
| Concentrations | n ≈ N_D, p = n_i²/N_D | p ≈ N_A, n = n_i²/N_A |
| Fermi level | Near the conduction band | Near the valence band |

### R10. What is a donor impurity?

A donor is a pentavalent impurity atom (P, As or Sb in silicon) with five valence electrons. Four form covalent bonds with neighbouring Si atoms; the fifth is weakly bound (≈ 0.045 eV) and is "donated" to the conduction band as a free electron. The donor becomes a fixed positive ion and makes the material n-type.

### R11. What is an acceptor impurity?

An acceptor is a trivalent impurity atom (B, Al, Ga or In in silicon) with three valence electrons. It completes only three bonds; the incomplete fourth bond "accepts" an electron from a neighbouring bond, creating a mobile hole in the valence band. The acceptor becomes a fixed negative ion and makes the material p-type.

### R12. Define energy band gap.

The energy band gap E_g is the energy difference between the bottom of the conduction band and the top of the valence band, E_g = E_C − E_V. It is the minimum energy needed to free an electron from a covalent bond and create an electron–hole pair. It is measured in eV: Si 1.12 eV, Ge 0.66 eV, GaAs 1.42 eV.

### R13. Differentiate between direct and indirect band-gap semiconductors.

In a **direct** band-gap semiconductor (GaAs, GaN, InP) the conduction-band minimum and valence-band maximum occur at the same momentum, so an electron can fall across the gap and emit a photon without any change in momentum. Light emission is efficient: LEDs, laser diodes, optical communication. In an **indirect** band-gap semiconductor (Si, Ge) they occur at different momenta, so a transition also needs a phonon (lattice vibration) to supply the momentum. This is unlikely, so light emission is very inefficient; the energy is mostly lost as heat. Silicon is therefore not used for LEDs or lasers.

### R14. State the crystal structure of silicon.

Silicon has the **diamond-cubic** crystal structure: two interpenetrating face-centred cubic lattices displaced by one quarter of the body diagonal. Each atom has four nearest neighbours at the corners of a tetrahedron, bonded covalently. Lattice constant a = 5.43 Å, 8 atoms per unit cell, nearest-neighbour distance 2.35 Å.

### R15. State the crystal structure of GaAs.

GaAs has the **zinc-blende** crystal structure: two interpenetrating FCC sublattices, one of gallium atoms and one of arsenic atoms, displaced by a quarter of the body diagonal. Each Ga atom has four As nearest neighbours and each As has four Ga neighbours, tetrahedrally arranged. Lattice constant a = 5.65 Å. The bonding is covalent with partial ionic character.

### R16. What are Miller indices?

Miller indices are a set of three integers (h k l), obtained from the reciprocals of a plane's intercepts on the crystal axes (in lattice units) reduced to the smallest whole numbers, that identify the orientation of a crystal plane. The same notation gives directions [u v w], families of planes {h k l} and families of directions ⟨u v w⟩. They are used to specify wafer orientation, etching and cleavage planes, epitaxial growth and X-ray diffraction.

### R17. Why is silicon widely used in integrated circuits?

1. It is abundant and cheap (sand, quartz), with a mature refining industry.
2. It grows a stable, high-quality native oxide, SiO₂, used for masking, passivation, isolation and the MOSFET gate insulator.
3. Its 1.12 eV band gap gives low leakage and operation up to about 150 °C.
4. Large, nearly defect-free single crystals (300 mm wafers) can be grown.
5. It is mechanically strong and conducts heat well.
6. Its doping by diffusion and ion implantation is well understood and controllable.

### R18. State three applications of GaAs.

Any three of: microwave and RF amplifiers (mobile phones, radar); satellite communication circuits; high-frequency transistors (HEMTs, MESFETs); LEDs; laser diodes for optical-fibre communication; photodetectors; high-efficiency solar cells for satellites.

### R19. Define carrier mobility.

Carrier mobility μ is the average drift velocity acquired by a charge carrier per unit applied electric field: μ = v_d/E, in cm²/V·s. It measures how easily electrons or holes move through the crystal. In silicon μ_n ≈ 1350 and μ_p ≈ 480 cm²/V·s. (Full treatment in Week 7.)

### R20. Explain why semiconductor conductivity increases with temperature.

Conductivity is σ = q(nμ_n + pμ_p). As temperature rises, more valence electrons gain enough thermal energy to cross the band gap, breaking covalent bonds and creating electron–hole pairs. The intrinsic carrier concentration rises exponentially, n_i ∝ T^{3/2}e^{−E_g/2kT}: in Si it roughly doubles every 8 °C. Mobility does fall slightly with temperature because of increased lattice scattering (μ ∝ T^{−3/2}), but this is a weak power law against an exponential increase in carriers, so the overall conductivity increases. This is the opposite of a metal, where the carrier number is fixed and only scattering increases.

## Lecture calculation questions solved

### C1. An n-type semiconductor has an electron concentration of 5 × 10¹⁶ cm⁻³. If the electron mobility is 1200 cm²/V·s, calculate its conductivity, assuming hole conduction is negligible.

With hole conduction neglected, σ = q n μ_n:

    σ = (1.6×10⁻¹⁹ C)(5×10¹⁶ cm⁻³)(1200 cm²/V·s)
      = 1.6×10⁻¹⁹ × 6×10¹⁹
      = 9.6 S/cm   (Ω⁻¹cm⁻¹)

**σ = 9.6 S/cm** (= 960 S/m), so the resistivity is ρ = 1/σ = **0.104 Ω·cm**. (With q = 1.602×10⁻¹⁹ C, σ = 9.61 S/cm.)

### C2. A semiconductor has n = 2 × 10¹⁶ cm⁻³, p = 5 × 10¹⁵ cm⁻³, μ_n = 1300 cm²/V·s, μ_p = 450 cm²/V·s. Calculate its conductivity using σ = q(nμ_n + pμ_p).

    nμ_n = 2×10¹⁶ × 1300 = 2.6×10¹⁹
    pμ_p = 5×10¹⁵ × 450 = 2.25×10¹⁸
    nμ_n + pμ_p = 2.825×10¹⁹   (cm·V·s)⁻¹

    σ = 1.6×10⁻¹⁹ × 2.825×10¹⁹ = 4.52 S/cm

**σ ≈ 4.52 S/cm**, ρ = 1/σ ≈ **0.221 Ω·cm**. The electrons contribute 92 % of the conductivity (2.6 of 2.825), the holes 8 %.

### C3. Explain why GaAs is preferred to silicon for some high-frequency applications.

1. **Higher electron mobility**: about 8500 cm²/V·s against 1350 for Si, because of its small electron effective mass (0.067m₀). Electrons cross a transistor faster, giving higher transconductance and cut-off frequency (f_T), and lower noise.
2. **Higher peak electron velocity** (about 2×10⁷ cm/s against 1×10⁷ cm/s), so short transit times in small devices.
3. **Semi-insulating substrates** (ρ ≈ 10⁸ Ω·cm) reduce parasitic capacitance and substrate losses, ideal for microwave integrated circuits (MMICs) with on-chip transmission lines.
4. It supports **heterostructure devices** (AlGaAs/GaAs HEMTs and HBTs) with very high mobility two-dimensional electron gases.
5. **Larger band gap** (1.42 eV) gives better radiation hardness and higher-temperature operation than Si.

Silicon is still preferred where cost, integration density and hole mobility matter.

### C4. A crystal plane has intercepts 2a, 3b and ∞c. Determine its Miller indices.

| Step | x | y | z |
|---|---|---|---|
| Intercepts | 2 | 3 | ∞ |
| Reciprocals | 1/2 | 1/3 | 0 |
| Multiply by 6 | 3 | 2 | 0 |

**Miller indices (3 2 0).** The zero shows that the plane is parallel to the z-axis. For a cubic crystal, d₃₂₀ = a/√(9 + 4 + 0) = a/√13.

### C5. Explain the importance of semiconductor band gap in electronic and optoelectronic device design.

**Electronic devices.**

1. **Intrinsic carrier concentration and leakage:** n_i ∝ e^{−E_g/2kT}. A wider gap gives far fewer thermally generated carriers, so lower reverse leakage and less noise (Si leaks less than Ge).
2. **Maximum operating temperature:** a device stops working when n_i approaches the doping level. Ge fails at about 75 °C, Si at about 150–200 °C, and SiC and GaN (3.3–3.4 eV) work above 300 °C.
3. **Breakdown field and power handling:** wider gap means a higher critical field (Si 0.3 MV/cm, GaN 3.3 MV/cm), so thinner, lower-resistance high-voltage devices.
4. **Turn-on voltage:** the diode forward voltage rises with E_g (Ge ≈ 0.3 V, Si ≈ 0.7 V, GaAs ≈ 1.1 V).

**Optoelectronic devices.**

1. **Emission wavelength:** an LED or laser emits at λ = hc/E_g, i.e. λ(μm) = 1.24/E_g(eV). Designers choose or alloy materials for the colour: GaAs 0.87 μm (infrared), GaP green-yellow, GaN 365 nm (blue/UV with InGaN), InGaAsP 1.3–1.55 μm for optical fibres.
2. **Absorption and detection:** only photons with hν ≥ E_g are absorbed. Si detects up to 1.1 μm; Ge and InGaAs are used for longer wavelengths.
3. **Solar cells:** the band gap sets the trade-off between absorbing more of the spectrum and the voltage obtained; the optimum single-junction gap is about 1.1–1.4 eV (Si, GaAs).
4. **Direct or indirect:** only direct-gap materials emit light efficiently.

---

## Examination questions solved (Q1–Q8)

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

Use the comparison table of Si, Ge and GaAs above as the core of the answer, then comment:

- **Structure and bonding.** Si and Ge are elemental, diamond cubic, purely covalent. GaAs is a III–V compound, zinc blende, mainly covalent with partial ionic character (As is more electronegative than Ga).
- **Band gap.** Ge (0.66 eV) < Si (1.12 eV) < GaAs (1.42 eV). The larger the gap, the lower n_i, the lower the leakage and the higher the maximum operating temperature. Si and Ge are **indirect**; GaAs is **direct**, so only GaAs emits light efficiently.
- **Mobility.** GaAs electrons are fastest (8500), then Ge (3900), then Si (1350) cm²/V·s. Hence GaAs and Ge suit high-speed work, though GaAs hole mobility is poor.
- **Oxide.** Only Si has an excellent native oxide, which is why MOS technology and VLSI are silicon.
- **Cost and processing.** Si cheapest and most mature; Ge more expensive; GaAs most expensive, brittle and toxic.

**Applications.**

- **Si:** microprocessors, memories, all digital and analogue ICs, MOSFETs and BJTs, power devices (IGBTs, thyristors), solar cells, sensors and MEMS.
- **Ge:** infrared detectors and lenses, high-speed SiGe heterojunction transistors, substrates for multi-junction space solar cells; historically the first transistors.
- **GaAs:** microwave and RF amplifiers in mobile phones and radar, satellite communication, HEMTs and MESFETs, LEDs, laser diodes for optical fibre links, high-efficiency solar cells for satellites.

### Q5. What is a crystal lattice? Explain the significance of crystal structure in semiconductor materials.

**Crystal lattice.** A crystal lattice is an infinite, periodic three-dimensional array of points in space such that every point has identical surroundings. It is generated by repeating a unit cell (edges a, b, c and angles α, β, γ) by translation. Attaching a basis of one or more atoms to each lattice point gives the real crystal: crystal = lattice + basis. Si, for example, is an FCC lattice with a two-atom basis, which produces the diamond structure.

**Significance of crystal structure.**

1. **It produces the energy bands.** The periodic potential of the lattice splits the atomic levels into allowed bands and forbidden gaps (Bloch's theorem, Kronig–Penney model). The size and type (direct or indirect) of the band gap depend on the structure and the atomic spacing.
2. **Carrier mobility.** In a perfect periodic lattice electrons move without scattering; departures from periodicity (vibrations, impurities, defects, grain boundaries) cause scattering. Single crystals therefore have much higher mobility than polycrystalline or amorphous material.
3. **Anisotropy.** Properties such as surface atom density, oxidation rate, etch rate, interface trap density, piezoelectric response and mobility differ with crystal direction. Wafer orientation ((100) or (111)) is chosen accordingly.
4. **Doping and diffusion.** Dopant atoms sit on substitutional lattice sites to become active. Open structures (diamond, APF 0.34) allow interstitial diffusion.
5. **Epitaxy and heterostructures.** Layers can be grown defect-free only on substrates with matching structure and lattice constant (e.g. AlGaAs on GaAs).
6. **Mechanical behaviour.** Cleavage planes, hardness and how wafers are diced all follow from the structure and bond directions.
7. **Defects.** Departures from the ideal structure (vacancies, dislocations) create states in the gap that act as traps and recombination centres, shortening carrier lifetime.

### Q6. Define Miller indices and explain how they are used to identify crystal planes.

**Definition.** Miller indices are a set of three smallest integers (h k l), proportional to the **reciprocals of the intercepts** a plane makes on the crystal axes (measured in units of the lattice constants), that specify the orientation of that plane and all planes parallel to it.

**How they identify a plane (procedure):**

1. Choose the origin at a lattice point not on the plane. Find the intercepts on x, y, z in units of a, b, c: say p, q, r.
2. Take reciprocals 1/p, 1/q, 1/r. A plane parallel to an axis has an infinite intercept and so a zero index.
3. Multiply by the lowest common multiple of the denominators to obtain integers.
4. Reduce to the smallest integers and enclose in round brackets (h k l). Negative indices carry a bar.

**Use and notation.** (h k l) names a particular plane; {h k l} the family of symmetry-equivalent planes; [u v w] a direction and ⟨u v w⟩ a family of directions. In cubic crystals [h k l] is normal to (h k l), and the spacing between planes is d = a/√(h² + k² + l²). Miller indices are used to specify wafer orientation ((100) for MOS, (111) for bipolar), etch planes, cleavage planes and X-ray diffraction peaks.

**Example.** Intercepts a, 2b, 3c → reciprocals 1, 1/2, 1/3 → × 6 → **(6 3 2)**.

### Q7. Determine the Miller indices of a crystal plane having intercepts of 2a, 3b, and 1c.

| Step | x | y | z |
|---|---|---|---|
| Intercepts (in units of a, b, c) | 2 | 3 | 1 |
| Reciprocals | 1/2 | 1/3 | 1/1 |
| Multiply by the LCM of the denominators, 6 | 3 | 2 | 6 |

**Miller indices = (3 2 6).**

Check: the integers 3, 2, 6 have no common factor, so no further reduction is possible. If the crystal is cubic with lattice constant a, the spacing of these planes is d₃₂₆ = a/√(9 + 4 + 36) = a/√49 = **a/7**.

@fig figures/miller-326.svg | The (3 2 6) plane, cutting the axes at 2a, 3b and 1c.

### Q8. Explain the difference between covalent, ionic, and metallic bonding and identify the dominant bonding mechanism in silicon.

**Covalent bonding.** Adjacent atoms share pairs of valence electrons so that each completes a stable outer shell. The shared electrons are localised between the two atoms, making the bond strong and directional. Covalent solids are hard, have high melting points, and are semiconductors or insulators depending on how tightly the bonds hold their electrons.

**Ionic bonding.** An electropositive atom gives up valence electrons to an electronegative atom; the resulting positive and negative ions attract electrostatically. The bond is strong but non-directional, there are no free electrons, and ionic solids (NaCl, MgO) are brittle insulators that conduct only when molten or dissolved.

**Metallic bonding.** Each atom releases its valence electrons into a common delocalised electron gas that binds the positive ion cores. The bond is non-directional, and the mobile electron gas gives high electrical and thermal conductivity, ductility and metallic lustre.

**Key differences:** how the electrons are held (shared between pairs / transferred to ions / shared by all atoms), directionality (yes / no / no), and the resulting electrical behaviour (semiconductor or insulator / insulator / conductor).

**Bonding in silicon: covalent.** Si has four valence electrons. In the diamond-cubic lattice each Si atom forms four sp³ covalent bonds with four nearest neighbours at 109.5°, sharing one electron pair with each so that every atom has a full octet. Because Si–Si bonds are between identical atoms there is no ionic character. The modest bond strength (equivalent to E_g = 1.12 eV) is what lets thermal energy break a few bonds at room temperature, creating electron–hole pairs and giving silicon its semiconducting behaviour.

---

## Practice questions

These extra questions practise this week's ideas. Work each one on paper before reading the solution; the calculation questions follow the same Question, Given, Find, Solution, Answer layout as the worked examples.

#### Practice 1.1: why germanium leaks more than silicon

**Question.** Explain why a germanium diode has a much larger reverse leakage current than a silicon diode of the same doping.

**Answer.** Leakage is carried by minority carriers, whose concentration is n_i²/N. Germanium's band gap (0.66 eV) is much smaller than silicon's (1.12 eV), so far more bonds are broken thermally: n_i(Ge) ≈ 2.4×10¹³ cm⁻³ against 1×10¹⁰ cm⁻³ for Si. Since leakage ∝ n_i², the Ge diode has about (2.4×10³)² ≈ 6×10⁶ times more minority carriers and a correspondingly larger leakage current.

#### Practice 1.2: Miller indices with a negative intercept

**Question.** A plane cuts the x-axis at −a, the y-axis at 2b and is parallel to the z-axis. Determine its Miller indices.

**Given:** intercepts −1, 2, ∞ (lattice units).

**Find:** (h k l).

**Solution.**

    Reciprocals: −1, 1/2, 0
    Multiply by 2: −2, 1, 0

**Answer:** **(2̄ 1 0)**, written with a bar over the 2 (in plain text (−2 1 0)).

#### Practice 1.3: interplanar spacing in germanium

**Question.** Germanium has a lattice constant of 5.65 Å. Calculate the spacing of the (110) and (111) planes.

**Given:** a = 5.65 Å.

**Find:** d₁₁₀ and d₁₁₁.

**Solution.**

    d₁₁₀ = a/√(1 + 1 + 0) = 5.65/√2 = 3.995 Å
    d₁₁₁ = a/√(1 + 1 + 1) = 5.65/√3 = 3.262 Å

**Answer:** **d₁₁₀ = 4.00 Å, d₁₁₁ = 3.26 Å.**

#### Practice 1.4: atom density and mass density of silicon

**Question.** Silicon has the diamond structure with a = 5.43 Å and atomic mass 28.085 g/mol. Calculate the number of atoms per cm³ and the density of silicon in g/cm³.

**Given:** a = 5.43×10⁻⁸ cm, 8 atoms per unit cell, M = 28.085 g/mol, N_A(Avogadro) = 6.022×10²³ mol⁻¹.

**Find:** atoms per cm³ and density ρ.

**Solution.**

    Cell volume a³ = (5.43×10⁻⁸)³ = 1.601×10⁻²² cm³
    Atoms per cm³ = 8/a³ = 8/1.601×10⁻²² = 5.0×10²² cm⁻³
    Mass of one cell = 8 × 28.085/6.022×10²³ = 3.731×10⁻²² g
    ρ = 3.731×10⁻²² / 1.601×10⁻²² = 2.33 g/cm³

**Answer:** **5.0×10²² atoms/cm³; ρ = 2.33 g/cm³.**

#### Practice 1.5: atom density of GaAs

**Question.** GaAs has the zinc-blende structure with a = 5.65 Å. Each unit cell contains 4 Ga and 4 As atoms; the molar mass of GaAs is 144.64 g/mol. Find the total atom density and the density of GaAs.

**Given:** a = 5.65×10⁻⁸ cm, 8 atoms (4 GaAs pairs) per cell, M = 144.64 g/mol.

**Find:** atoms per cm³ and ρ.

**Solution.**

    a³ = (5.65×10⁻⁸)³ = 1.804×10⁻²² cm³
    Atoms per cm³ = 8/a³ = 4.44×10²² cm⁻³
    ρ = 4 × 144.64 / (6.022×10²³ × 1.804×10⁻²²) = 578.6/108.6 = 5.33 g/cm³

**Answer:** **4.44×10²² atoms/cm³ (half Ga, half As); ρ = 5.33 g/cm³.**

#### Practice 1.6: the effect of doping on conductivity

**Question.** Compare the conductivity of intrinsic silicon (n_i = 1×10¹⁰ cm⁻³) with that of silicon doped with 1×10¹⁵ cm⁻³ donors. Use μ_n = 1350 and μ_p = 480 cm²/V·s.

**Given:** n_i = 10¹⁰ cm⁻³, N_D = 10¹⁵ cm⁻³, μ_n = 1350, μ_p = 480 cm²/V·s.

**Find:** σ_intrinsic, σ_doped and their ratio.

**Solution.**

    σ_i = qn_i(μ_n + μ_p) = 1.6×10⁻¹⁹ × 10¹⁰ × 1830 = 2.93×10⁻⁶ S/cm
    σ = qN_Dμ_n = 1.6×10⁻¹⁹ × 10¹⁵ × 1350 = 0.216 S/cm
    ratio = 0.216/2.93×10⁻⁶ = 7.4×10⁴

**Answer:** **doping with only one atom in 5×10⁷ raises the conductivity about 74 000 times.**

#### Practice 1.7: which light can silicon absorb?

**Question.** What is the longest wavelength of light that silicon (E_g = 1.12 eV) can absorb? Can a silicon photodiode detect the 1.55 μm light used in optical-fibre links?

**Given:** E_g = 1.12 eV.

**Find:** λ_max, and whether 1.55 μm is absorbed.

**Solution.**

    λ_max = 1.24/E_g = 1.24/1.12 = 1.11 μm
    A 1.55 μm photon has energy 1.24/1.55 = 0.80 eV < 1.12 eV

**Answer:** **λ_max = 1.11 μm; no**, 1.55 μm photons do not have enough energy to create electron–hole pairs in silicon. Fibre receivers use Ge or InGaAs.

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Define a semiconductor and distinguish it from a conductor and an insulator. | Why does a semiconductor conduct better when it is heated, while a metal conducts worse? | Heat breaks bonds and creates many more electron–hole pairs (∝ e^{−E_g/2kT}); in a metal the carrier number is fixed and only scattering increases. | Classification of materials |
| 2 | Describe the atomic structure of Si, Ge, Ga and As and identify their valence electrons. | How many valence electrons do Si, Ga and As have? | Si 4, Ga 3, As 5 (GaAs averages 4 per atom). | Atomic structure; valence electrons |
| 3 | Explain covalent bonding in silicon and electron–hole pair generation. | What two carriers are created when a covalent bond in Si breaks, and what minimum energy is needed? | A free electron and a hole; at least E_g = 1.12 eV. | Covalent bonding; electron–hole pairs |
| 4 | Distinguish intrinsic, n-type and p-type semiconductors, and donors from acceptors. | Si is doped with 10¹⁷ cm⁻³ boron. Is it n- or p-type, and what is the electron concentration (n_i = 10¹⁰ cm⁻³)? | p-type; n = n_i²/N_A = 10³ cm⁻³. | Intrinsic and extrinsic semiconductors |
| 5 | Compare elemental and compound semiconductors, and Si, Ge and GaAs. | Give one reason GaAs is preferred to Si for high-frequency work and one reason Si is preferred for ICs. | GaAs: electron mobility ≈ 8500 vs 1350 cm²/V·s. Si: excellent native SiO₂ (also cheaper, larger wafers). | Elemental and compound; comparison table |
| 6 | Explain the energy-band picture, the band gap and direct versus indirect gaps. | Why is silicon not used for LEDs? | Its gap is indirect: a phonon is needed to conserve momentum, so radiative recombination is very inefficient. | Energy band concept; direct and indirect band gaps |
| 7 | Describe crystal lattices, unit cells and the diamond and zinc-blende structures. | How many atoms are in the diamond-cubic unit cell, and how many nearest neighbours does each atom have? | 8 atoms per cell; 4 nearest neighbours. | Semiconductor crystal structure |
| 8 | Determine Miller indices of planes and the spacing between planes. | Find the Miller indices of a plane with intercepts 3a, ∞, c. | Reciprocals 1/3, 0, 1 → × 3 → (1 0 3). | Miller indices; Examples 1.2–1.3 |
