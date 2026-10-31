# Questions 1–13 — Material Physics and Semiconductor Growth
<!-- group: The 50 questions, answered -->

Module 1, part 1: what a semiconductor is, the main materials, crystal structure and Miller indices, bonding, and how silicon is purified and grown into crystals and epitaxial layers. Each question stands on its own: its key terms are defined with it, so you can start anywhere.

## Symbols and abbreviations used on this page

Every symbol, constant and abbreviation on this page is listed here, even if another page already defined it, so you can study this page on its own.

**Constants and units**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| q | Magnitude of the electronic charge | 1.6×10⁻¹⁹ C |
| k | Boltzmann constant | 8.617×10⁻⁵ eV/K = 1.381×10⁻²³ J/K |
| kT | Thermal energy | 0.0259 eV (often 0.02585 eV) at 300 K |
| T | Absolute temperature | kelvin (K); room temperature = 300 K |
| h | Planck constant | 6.626×10⁻³⁴ J·s |
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| μm | Micrometre (micron) | 1 μm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_c (E_C) | Energy of the bottom of the conduction band | eV |
| E_v (E_V) | Energy of the top of the valence band | eV |
| E_g | Band-gap energy, E_c − E_v | eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K |
| f(E) | Fermi–Dirac function: probability that a state at energy E is occupied | dimensionless, 0 to 1 |
| n | Electron concentration (free electrons per m³) | m⁻³ |
| p | Hole concentration (holes per m³) | m⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | m⁻³; Si ≈ 1×10¹⁶ at 300 K |
| k (wave vector) | Wave vector, 2π/λ; measures the electron's momentum, p = ħk | m⁻¹ |
| λ | Wavelength | μm or nm; λ(μm) = 1.24/E(eV) |
| a | Lattice constant: edge length of the cubic unit cell | nm; Si 0.543, Ge and GaAs 0.565 |
| (h k l), {h k l} | Miller indices of a plane; family of equivalent planes | integers |
| [u v w], ⟨u v w⟩ | A crystal direction; family of equivalent directions | integers |
| d_hkl | Spacing between neighbouring (h k l) planes, a/√(h² + k² + l²) | nm |
| k₀ | Segregation coefficient, C_s/C_l at the freezing interface | dimensionless; B 0.8, P 0.35 |
| C_s | Surface concentration of a diffusion (or solid concentration when freezing) | m⁻³ |
| C_l, C₀ | Concentration in the melt (liquid); C₀ at the start | m⁻³ |
| f (growth) | Fraction of the melt already solidified | 0 to 1 |
| C(x, t) | Dopant concentration at depth x and time t | m⁻³ |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | m²/(V·s); Si μ_n 0.135, μ_p 0.048 |
| σ | Conductivity, q(nμ_n + pμ_p) (in Week 8, σ is also a capture cross-section) | S/m (siemens per metre) |
| ρ | Resistivity, 1/σ | Ω·m |
| α, β, γ (cell) | Angles between the edges of a unit cell | degrees; 90° for cubic |
| v_pull | Pull rate of a Czochralski crystal | mm/min |
| r (atom) | Atomic radius (hard-sphere model), half the nearest-neighbour distance | nm |

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
| III–V | Compound of Group III and Group V elements (e.g. GaAs) |
| MG-Si | Metallurgical-grade silicon (≈ 98 % pure) |
| EG-Si | Electronic-grade silicon (99.9999999 % or better) |
| CZ | Czochralski crystal growth |
| FZ | Float-zone crystal growth |
| CVD | Chemical vapour deposition |
| VPE | Vapour-phase epitaxy |
| LPE | Liquid-phase epitaxy |
| MBE | Molecular-beam epitaxy |
| MOCVD | Metal-organic chemical vapour deposition |
| UHV | Ultra-high vacuum (≈ 10⁻¹⁰ Torr) |
| RHEED | Reflection high-energy electron diffraction (counts atomic layers during MBE) |
| MOS | Metal–oxide–semiconductor |
| MOSFET | Metal–oxide–semiconductor field-effect transistor |
| CMOS | Complementary MOS (n- and p-channel MOSFETs together) |
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
| VCSEL | Vertical-cavity surface-emitting laser |


## Questions on this page

| Q | Question |
|---|---|
| 1 | Define a semiconductor and explain how its electrical conductivity differs from that of a conductor and an insulator. |
| 2 | Distinguish between elemental semiconductors and compound semiconductors, giving two examples of each. |
| 3 | Explain why silicon is widely used in semiconductor device fabrication. |
| 4 | Compare the properties and applications of silicon (Si), germanium (Ge), and gallium arsenide (GaAs). |
| 5 | What is a crystal lattice? Explain the significance of crystal structure in semiconductor materials. |
| 6 | Define Miller indices and explain how they are used to identify crystal planes. |
| 7 | Determine the Miller indices of a crystal plane having intercepts of 2a, 3b, and 1c. |
| 8 | Explain the difference between covalent, ionic, and metallic bonding and identify the dominant bonding mechanism in silicon. |
| 9 | Describe the major stages involved in converting metallurgical-grade silicon (MG-Si) into electronic-grade silicon (EG-Si). |
| 10 | Explain the principle and operation of the Czochralski (CZ) crystal growth method. |
| 11 | State four advantages and two limitations of the Czochralski method. |
| 12 | Explain the principles of vapour-phase epitaxy (VPE), liquid-phase epitaxy (LPE), and molecular-beam epitaxy (MBE). |
| 13 | Compare VPE, LPE, and MBE in terms of growth mechanism, temperature, precision, and applications. |

## Model answers

### Q1. Define a semiconductor and explain how its electrical conductivity differs from that of a conductor and an insulator.

> **Question type:** Definition and explanation · **Topic:** classification of solids by conductivity · **Full notes:** Week 1 (Introduction to Semiconductor Materials)

**What the examiner wants.** First a precise definition of a semiconductor (conductivity between metals and insulators, and controllable). Then an explanation, using energy bands, of why the three classes of material conduct so differently, including how each responds to temperature. A labelled band sketch and a short comparison table earn the full marks.

**Key terms.**

- **Conductivity (σ):** how easily a material carries electric current, in S/m; its inverse is resistivity ρ = 1/σ in Ω·m.
- **Energy band:** a wide range of closely spaced allowed electron energies formed when many atoms join into a solid.
- **Valence band:** the highest band that is full at 0 K; it holds the electrons that form the bonds.
- **Conduction band:** the band above the valence band; electrons in it are free to move and carry current.
- **Band gap (E_g):** the forbidden energy range between the top of the valence band (E_v) and the bottom of the conduction band (E_c), E_g = E_c − E_v, in electron-volts (eV).
- **Hole:** the empty place left in a bond when an electron is freed; it moves through the crystal like a positive charge.
- **Doping:** adding a small, controlled amount of a chosen impurity to change the number of carriers.
- **kT:** the typical thermal energy of a particle; 0.0259 eV at 300 K (k = Boltzmann's constant, T = absolute temperature).

**Model answer.**

**Definition.** A semiconductor is a material whose electrical conductivity lies between that of a conductor and an insulator (resistivity roughly 10⁻⁵ to 10⁶ Ω·m) and can be changed over many orders of magnitude by temperature, light, electric field and, above all, by doping. Examples: silicon (Si), germanium (Ge), gallium arsenide (GaAs).

**How conductivity depends on carriers.** Current is carried by mobile charges, so

    σ = q(nμ_n + pμ_p)

Where:

- σ = conductivity (S/m)
- q = electronic charge, 1.6×10⁻¹⁹ C
- n, p = concentrations of free electrons and holes (m⁻³)
- μ_n, μ_p = electron and hole mobilities, i.e. drift speed per unit field (m²/V·s)

The three classes differ mainly in **how many free carriers they have**, and that is decided by their energy-band structure.

@fig figures/bands.svg | Energy bands of a metal, a semiconductor and an insulator at room temperature: no gap, a small gap, and a wide gap.

Sketch in the exam: three band diagrams side by side, label "conduction band", "valence band", "E_g", and show a few electrons above a small gap for the semiconductor.

**1. Conductor (metal).** The valence and conduction bands overlap, or the top band is only partly filled, so there is no gap. About 10²⁸ free electrons per m³ are always present. Conductivity is very high (σ ≈ 10⁷–10⁸ S/m; copper ρ = 1.7×10⁻⁸ Ω·m) and is hardly changed by impurities. When temperature rises the number of electrons stays the same but lattice vibrations scatter them more, so conductivity **falls** (positive temperature coefficient of resistance).

**2. Insulator.** The valence band is full and the conduction band empty, separated by a wide gap (E_g > about 4 eV; SiO₂ ≈ 9 eV). Room-temperature thermal energy (kT ≈ 0.026 eV) is far too small to lift electrons across, so there are practically no free carriers. Resistivity is very high (10⁸–10¹⁶ Ω·m) and changes little with temperature under normal conditions.

**3. Semiconductor.** The arrangement is the same as in an insulator (full valence band, empty conduction band at 0 K) but the gap is **small** (Si 1.12 eV, Ge 0.66 eV, GaAs 1.42 eV). At room temperature a small fraction of bonds is broken thermally: each freed electron enters the conduction band and leaves a hole in the valence band, so **both electrons and holes** conduct. Pure silicon has only n = p = n_i = 1×10¹⁶ m⁻³ at 300 K, so its conductivity is low; but:

- heating breaks more bonds (n_i rises roughly as e^{−E_g/2kT}), so conductivity **rises** with temperature (negative temperature coefficient of resistance);
- doping with about one phosphorus atom per million Si atoms (5×10²² m⁻³) raises the conductivity more than a million times.

**Comparison.**

| Property | Conductor | Semiconductor | Insulator |
|---|---|---|---|
| Band gap | None (bands overlap) | Small, ≈ 0.5–3.5 eV | Large, > 4 eV |
| Free carriers | ≈ 10²⁸ m⁻³, fixed | Few, controllable; electrons **and** holes | Practically none |
| Resistivity (Ω·m) | ≈ 10⁻⁸ | ≈ 10⁻⁵ to 10⁶ | 10⁸ to 10¹⁶ |
| Effect of heating | σ falls | σ rises | Very small |
| Effect of impurities | Small | Very large | Small |
| Examples | Cu, Al, Ag | Si, Ge, GaAs | Glass, SiO₂, rubber |

**Conclusion.** Conductors have no gap and a fixed, huge number of carriers; insulators have a wide gap and essentially none; semiconductors have a small gap, two kinds of carrier, and a carrier density that we can engineer, which is what makes devices possible.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ definition: conductivity between conductor and insulator **and** controllable (doping, temperature, light)
- ✓ at least two examples (Si, Ge, GaAs)
- ✓ labelled band diagram for all three classes
- ✓ conductor: overlapping bands, ≈ 10²⁸ m⁻³ electrons, σ falls with temperature
- ✓ insulator: wide gap (> 4 eV, e.g. SiO₂ 9 eV), no carriers
- ✓ semiconductor: small gap (Si 1.12 eV), electron–hole pairs created thermally, σ rises with temperature
- ✓ effect of doping on a semiconductor (orders of magnitude)
- ✓ typical resistivity ranges or a comparison table

**Common mistakes.**

- Defining a semiconductor only as "conductivity between a conductor and an insulator". The key word is *controllable*; without it you lose the main definition mark.
- Saying a semiconductor conducts "less when hot, like a metal". It is the opposite: heating creates carriers, so σ rises.
- Forgetting holes. Semiconductors have two carrier types; metals have only electrons.
- Drawing the semiconductor band diagram with overlapping bands, or the metal with a gap.

**Remember it.** "No gap, small gap, big gap": metal, semiconductor, insulator, and only the small gap can be tuned.

**Try a variant.** Explain why the resistance of a silicon sample falls when it is heated, while that of a copper wire rises. *Answer:* In copper the number of free electrons (≈ 10²⁸ m⁻³) is fixed; heating only increases lattice vibrations, which scatter the electrons and lower their mobility, so resistance rises. In silicon heating breaks covalent bonds, creating electron–hole pairs; n_i grows roughly as e^{−E_g/2kT}, so the number of carriers rises far faster than the mobility falls, and resistance drops.

---

### Q2. Distinguish between elemental semiconductors and compound semiconductors, giving two examples of each.

> **Question type:** Compare / distinguish · **Topic:** classes of semiconductor material · **Full notes:** Week 1 (Introduction to Semiconductor Materials)

**What the examiner wants.** Define each class, then set them side by side under the same headings (composition, position in the periodic table, crystal structure, bonding, band gap, processing, uses). Two correct examples of each are compulsory marks. End with a comparison table.

**Key terms.**

- **Elemental semiconductor:** a semiconductor made of a single chemical element.
- **Compound semiconductor:** a semiconductor made of two or more different elements in a fixed ratio.
- **Group IV, III–V, II–VI:** columns of the periodic table; e.g. a III–V compound joins a group III element (Ga, In, Al) with a group V element (As, P, N).
- **Band gap (E_g):** the energy (eV) needed to free an electron from a bond, i.e. to lift it from the valence band to the conduction band.
- **Direct / indirect band gap:** direct means an electron can drop across the gap and emit light without changing its momentum; indirect means a lattice vibration (phonon) must also take part, so light emission is weak.
- **Diamond cubic / zinc blende:** the crystal structures of Si and of GaAs; both have each atom bonded to four neighbours, but in zinc blende the two kinds of atom alternate.
- **Stoichiometry:** the exact ratio of the elements in a compound (1 : 1 for GaAs).
- **Band-gap engineering:** tuning E_g by alloying compounds, e.g. Al_{x}Ga_{1−x}As.

**Model answer.**

**Elemental semiconductors.** These consist of atoms of one element, all from group IV of the periodic table, each with four valence electrons. They crystallise in the diamond-cubic structure, where every atom forms four identical covalent bonds, so the bonding is purely covalent. Their band gap is fixed by the element, and both important ones are indirect.

*Examples:* **silicon (Si)**, E_g = 1.12 eV; **germanium (Ge)**, E_g = 0.66 eV.

**Compound semiconductors.** These are formed from two or more elements whose valence electrons average four per atom, for example a group III atom (3 electrons) with a group V atom (5 electrons). They crystallise in the zinc-blende (or wurtzite) structure. Because the two atoms have different electronegativities, the bonds are covalent with partial ionic character. Their band gap depends on the elements chosen and can be tuned continuously by alloying; many are direct-gap.

*Examples:* **gallium arsenide (GaAs)**, III–V, E_g = 1.42 eV direct; **indium phosphide (InP)**, III–V. Others: gallium nitride (GaN, 3.4 eV), silicon carbide (SiC, IV–IV), cadmium telluride (CdTe, II–VI).

**Main points of difference.**

1. **Composition:** one element versus two or more elements in a fixed ratio.
2. **Bonding:** purely covalent versus covalent with some ionic character.
3. **Band gap:** fixed and indirect (Si, Ge) versus adjustable and often direct, so compounds can emit light.
4. **Mobility:** compounds such as GaAs can have much higher electron mobility (≈ 0.85 m²/V·s against 0.135 for Si), suiting very high frequencies.
5. **Processing:** elemental crystals are easier to grow and dope, cheaper and more mature; compounds need careful control of stoichiometry, are more brittle, costly, and sometimes toxic (arsenic).
6. **Applications:** elemental for integrated circuits, power devices and solar cells; compound for LEDs, lasers, microwave/RF and high-power wide-gap devices.

**Comparison table.**

| Feature | Elemental | Compound |
|---|---|---|
| Composition | One element | Two or more elements |
| Periodic-table groups | Group IV | III–V, II–VI, IV–IV |
| Crystal structure | Diamond cubic | Zinc blende or wurtzite |
| Bonding | Purely covalent | Covalent, partly ionic |
| Band gap | Fixed; Si and Ge indirect | Tunable by alloying; many direct |
| Light emission | Very poor | Efficient (direct-gap ones) |
| Cost and processing | Cheap, mature (especially Si) | Costly, stoichiometry must be controlled |
| Typical uses | ICs, power devices, solar cells | LEDs, lasers, RF, high-power |
| **Examples** | **Si, Ge** | **GaAs, InP** (also GaN, SiC, CdTe) |

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ definition of elemental (single element, group IV)
- ✓ definition of compound (two or more elements, e.g. III–V)
- ✓ two elemental examples: Si, Ge
- ✓ two compound examples, e.g. GaAs, InP (or GaN, SiC)
- ✓ difference in bonding (purely covalent vs partly ionic)
- ✓ difference in band gap (fixed/indirect vs tunable/often direct) and its consequence for light emission
- ✓ difference in cost/processing and in applications
- ✓ comparison table

**Common mistakes.**

- Giving SiO₂ or diamond as a "compound semiconductor". SiO₂ is an insulator; diamond is elemental (carbon).
- Calling SiGe or SiC "elemental" because they contain silicon. They contain two elements, so they are compound (IV–IV).
- Listing only examples with no actual point of difference. The question says *distinguish*: give at least four contrasting features.
- Stating that all compound semiconductors are direct-gap. GaP and SiC are indirect.

**Remember it.** "One element, one gap; two elements, choose your gap."

**Try a variant.** Classify the following as elemental or compound and state the group combination: Ge, GaN, CdTe, SiC. *Answer:* Ge, elemental (group IV); GaN, compound III–V; CdTe, compound II–VI; SiC, compound IV–IV.

---

### Q3. Explain why silicon is widely used in semiconductor device fabrication.

> **Question type:** Explanation · **Topic:** properties of silicon · **Full notes:** Week 1 (Introduction to Semiconductor Materials)

**What the examiner wants.** A list of distinct reasons, each explained in one or two sentences with a supporting fact or number (abundance, native oxide, band gap, crystal growth, doping, mechanical and thermal properties). Six or seven well-explained reasons, plus one limitation, make a full-mark answer.

**Key terms.**

- **Native oxide:** an oxide that grows directly on the material by heating it in oxygen or steam; for silicon it is silicon dioxide (SiO₂).
- **Band gap (E_g):** the energy needed to free an electron from a bond; 1.12 eV for Si at 300 K.
- **Intrinsic carrier concentration (n_i):** the number of electrons (equal to holes) per m³ created by heat in pure material; 1×10¹⁶ m⁻³ for Si at 300 K.
- **Leakage current:** the small unwanted current through a reverse-biased junction, caused by thermally generated carriers.
- **Czochralski (CZ) method:** growth of a large single crystal by slowly pulling a seed crystal from molten silicon.
- **Interface trap density (D_it):** the number of unwanted electron states at the Si/SiO₂ boundary per m² per eV.
- **Dopant:** an impurity added on purpose to control conductivity, e.g. boron (B) or phosphorus (P).

**Model answer.**

Silicon is used for more than 90 % of all semiconductor devices because it combines the following advantages.

**1. Abundant and cheap.** Silicon is about 28 % of the Earth's crust, in the form of SiO₂ (sand, quartz). The raw material costs little and the refining industry is enormous, so wafers are inexpensive.

**2. An excellent native oxide.** Heating silicon in oxygen grows SiO₂, which is:

- an excellent insulator (E_g ≈ 9 eV, breakdown field ≈ 10⁹ V/m, i.e. 1 GV/m);
- chemically stable and insoluble in water;
- joined to silicon by a very clean interface (D_it ≈ 10¹⁴ m⁻²eV⁻¹).

It is used as the MOSFET gate insulator, a mask against dopant diffusion, surface passivation, and isolation between devices. No other semiconductor has an oxide this good; this one property is why MOS technology and VLSI are built on silicon.

**3. A well-suited band gap.** E_g = 1.12 eV is large enough to keep n_i small (1×10¹⁶ m⁻³ at 300 K), so leakage is low and devices work up to about 150 °C (germanium, with 0.66 eV, fails above about 75 °C). It is also small enough that doped silicon conducts well.

**4. Mature crystal growth.** Very large (300 mm diameter), highly pure (impurities below 1 part per billion) and nearly defect-free single crystals are grown routinely by the Czochralski method.

**5. Easy, predictable doping.** Boron (p-type) and phosphorus, arsenic and antimony (n-type) can be introduced accurately by diffusion and ion implantation, using SiO₂ as a mask.

**6. Good mechanical and thermal properties.** Silicon is hard and strong enough to be handled as thin wafers and conducts heat about three times better than GaAs, which helps remove heat from dense ICs and power devices.

**7. Elemental and non-toxic.** As a single element it has no stoichiometry to control and no toxic constituents (unlike the arsenic in GaAs), which simplifies processing.

**Limitation.** Silicon has an **indirect** band gap, so it emits light very poorly, and its electron mobility (0.135 m²/V·s) is lower than that of GaAs (≈ 0.85). LEDs, lasers and the highest-frequency circuits therefore use compound semiconductors instead.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ abundance and low cost (sand, ≈ 28 % of crust)
- ✓ stable native oxide SiO₂ and its uses (gate dielectric, mask, passivation)
- ✓ band gap 1.12 eV: low leakage, operation to ≈ 150 °C (compared with Ge)
- ✓ large, pure single crystals by the CZ method
- ✓ controllable doping by diffusion and ion implantation
- ✓ mechanical strength and thermal conductivity
- ✓ one limitation (indirect gap, poor light emitter)

**Common mistakes.**

- Writing "silicon has the highest mobility". It does not; Ge and GaAs are higher. Silicon wins on oxide, cost and maturity, not speed.
- Listing reasons without explaining them ("good oxide" alone earns little; say what the oxide is used for).
- Forgetting the oxide altogether. It is the single most important reason and examiners expect it.

**Remember it.** "Sand, oxide, gap": cheap sand, a perfect oxide, and a gap that is just right.

**Try a variant.** Explain why gallium arsenide, not silicon, is used to make laser diodes. *Answer:* GaAs has a direct band gap of 1.42 eV, so an electron dropping from the conduction band to the valence band can give its energy out as a photon without needing a phonon; emission is efficient, at λ = 1.24/1.42 = 0.87 μm (infrared). Silicon's gap is indirect, so recombination needs a phonon as well and the energy is lost mainly as heat.

---

### Q4. Compare the properties and applications of silicon (Si), germanium (Ge), and gallium arsenide (GaAs).

> **Question type:** Compare · **Topic:** Si, Ge and GaAs · **Full notes:** Week 1 (Introduction to Semiconductor Materials)

**What the examiner wants.** A side-by-side comparison of the three materials under the same headings (type, structure, band gap and its nature, mobility, thermal behaviour, oxide, cost), a short explanation of what each difference means for devices, and the main applications of each. A comparison table is expected.

**Key terms.**

- **Band gap (E_g):** the energy (eV) between the top of the valence band and the bottom of the conduction band.
- **Direct / indirect band gap:** direct means an electron can recombine and emit a photon without changing momentum (efficient light emission); indirect needs a lattice vibration (phonon) as well (poor emission).
- **Electron mobility (μ_n):** drift velocity per unit electric field, m²/V·s; higher mobility means faster devices.
- **Intrinsic carrier concentration (n_i):** thermally generated electrons per m³ in pure material; smaller for wider gaps.
- **Diamond cubic / zinc blende:** crystal structures in which every atom has four tetrahedral neighbours; in zinc blende the neighbours are of the other element.
- **HEMT / MESFET:** high-speed field-effect transistors made in GaAs for microwave circuits.
- **SiGe HBT:** a fast bipolar transistor with a silicon–germanium base.

**Model answer.**

**Comparison of properties (300 K).**

| Property | Si | Ge | GaAs |
|---|---|---|---|
| Type | Elemental (group IV) | Elemental (group IV) | Compound (III–V) |
| Crystal structure | Diamond cubic | Diamond cubic | Zinc blende |
| Lattice constant | 0.543 nm | 0.565 nm | 0.565 nm |
| Bonding | Covalent | Covalent | Covalent, partly ionic |
| Band gap | 1.12 eV | 0.66 eV | 1.42 eV |
| Nature of gap | Indirect | Indirect | **Direct** |
| Electron mobility (m²/V·s) | 0.135 | 0.39 | 0.85 |
| Max. operating temperature | ≈ 150 °C | ≈ 75 °C | High (wide gap) |
| Native oxide | Excellent (SiO₂) | Poor, water-soluble | None useful |
| Light emission | Very poor | Very poor | Efficient |
| Cost / maturity | Lowest, most mature | Higher | Highest; brittle, toxic As |

**What the differences mean.**

- **Band gap and temperature.** The order is Ge (0.66) < Si (1.12) < GaAs (1.42 eV). A wider gap gives a smaller n_i, so lower leakage current and a higher maximum working temperature. Germanium leaks most and fails first when hot; this is why silicon replaced it.
- **Direct versus indirect.** Only GaAs is direct, so only GaAs emits light efficiently; the emitted wavelength is λ = 1.24/E_g = 1.24/1.42 = 0.87 μm (near infrared).
- **Mobility and speed.** GaAs electrons are about six times faster than silicon's, and Ge about three times, so GaAs (and Ge) suit very high-frequency work. GaAs hole mobility is poor, however, which makes GaAs CMOS impractical.
- **Oxide.** Only silicon has a stable, high-quality native oxide; this is why MOS transistors and very large-scale integration (VLSI) are silicon technologies.
- **Cost and processing.** Si is the cheapest and most mature; Ge is costlier; GaAs is the most expensive, brittle, and contains toxic arsenic.

@fig figures/ek.svg | Energy–momentum (E–k) diagrams: in GaAs the conduction-band minimum lies directly above the valence-band maximum (direct gap); in Si they are at different momentum (indirect gap).

Sketch in the exam: two small E–k curves, one with the band edges aligned (GaAs, label "photon") and one offset (Si, label "phonon needed").

**Applications.**

- **Silicon:** microprocessors and memories, all digital and analogue ICs, MOSFETs and BJTs, power devices (IGBTs, thyristors), solar cells, sensors and MEMS.
- **Germanium:** infrared detectors and lenses, SiGe high-speed transistors, substrates for multi-junction space solar cells; historically the first transistors (1947).
- **Gallium arsenide:** microwave and RF amplifiers in mobile phones, radar and satellite links (HEMTs, MESFETs), LEDs and laser diodes for optical-fibre links, high-efficiency solar cells for satellites.

**Conclusion.** Silicon wins on cost, oxide and thermal stability, so it dominates integrated circuits; germanium survives where its high mobility or narrow gap (infrared) helps; GaAs is chosen where speed or light emission matters more than cost.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ band gaps: Si 1.12, Ge 0.66, GaAs 1.42 eV
- ✓ direct (GaAs) versus indirect (Si, Ge) and its consequence for light emission
- ✓ electron mobilities in the right order (GaAs > Ge > Si) with values
- ✓ crystal structures: diamond cubic (Si, Ge), zinc blende (GaAs)
- ✓ thermal stability / leakage linked to band gap
- ✓ silicon's native oxide as its key advantage
- ✓ cost and processing comparison
- ✓ at least two applications for each material

**Common mistakes.**

- Mixing up the band gaps (e.g. giving Ge a larger gap than Si). Learn the order Ge < Si < GaAs.
- Saying GaAs is better than Si "in every way". It has no useful oxide, poor hole mobility and is costly.
- Writing only a table with no explanation. *Compare* asks what the differences mean, not just what they are.
- Forgetting applications: half of the question is about them.

**Remember it.** "Ge leaks, Si thinks, GaAs shines": germanium has the narrowest gap, silicon runs the computers, GaAs makes the light.

**Try a variant.** Which of Si, Ge and GaAs would you choose for (a) a photodetector for 1.55 μm fibre-optic light, (b) a red/infrared laser, (c) a microprocessor? Justify. *Answer:* The photon energy at 1.55 μm is E = 1.24/1.55 = 0.80 eV. (a) **Ge**: its gap (0.66 eV) is below 0.80 eV so it absorbs the light; Si (1.12 eV) is transparent to it. (b) **GaAs**: direct gap, emits at 0.87 μm. (c) **Si**: excellent oxide for MOSFETs, cheap, mature, low leakage.

---

### Q5. What is a crystal lattice? Explain the significance of crystal structure in semiconductor materials.

> **Question type:** Definition and explanation · **Topic:** crystal structure · **Full notes:** Week 1 (Introduction to Semiconductor Materials)

**What the examiner wants.** A precise definition of a crystal lattice (with unit cell and basis), the crystal structures of Si and GaAs as illustrations, and then several distinct reasons why the arrangement of atoms matters for semiconductor behaviour and processing, each explained in a sentence or two.

**Key terms.**

- **Crystal lattice:** an infinite, periodic three-dimensional array of points in which every point has identical surroundings.
- **Basis:** the atom or group of atoms attached to each lattice point; crystal = lattice + basis.
- **Unit cell:** the smallest block which, repeated by translation in three directions, rebuilds the whole crystal.
- **Lattice constant (a):** the edge length of a cubic unit cell; Si 0.543 nm (1 nm = 10⁻⁹ m).
- **Single crystal:** a solid with the same lattice and orientation throughout; *polycrystalline* material is made of many small crystals (grains), *amorphous* has no long-range order.
- **Diamond cubic structure:** two interpenetrating face-centred cubic (FCC) lattices offset by a quarter of the body diagonal; each atom has four tetrahedral neighbours (the structure of Si and Ge).
- **Mobility (μ):** drift velocity per unit electric field (m²/V·s); it falls when carriers are scattered.
- **Epitaxy:** growth of a thin single-crystal layer that copies the crystal arrangement of the substrate.

**Model answer.**

**Crystal lattice.** A crystal lattice is a regular, infinitely repeating three-dimensional array of points in space, arranged so that every point has exactly the same surroundings. The smallest repeating block, the **unit cell**, is described by its edge lengths a, b, c and angles α, β, γ; repeating it in three directions rebuilds the whole crystal. Placing a **basis** (one or more atoms) on each lattice point gives the real crystal:

    crystal structure = lattice + basis

Where:

- lattice = the geometric array of repeating points
- basis = the group of atoms attached to every lattice point

*Examples.* Silicon has an FCC lattice with a two-atom basis, giving the **diamond-cubic** structure: 8 atoms per cubic cell, each bonded covalently to 4 neighbours at 109.5°, a = 0.543 nm, atom density 8/a³ = 5.0×10²⁸ m⁻³. GaAs has the same arrangement, but the two basis atoms are Ga and As, giving the **zinc-blende** structure.

Sketch in the exam: a cube labelled with edge a, showing the corner and face-centre atoms (FCC), and note that the diamond structure adds four atoms inside the cube.

**Significance of crystal structure.**

**1. It creates the energy bands.** The periodic arrangement of atoms produces a periodic potential, which spreads the sharp atomic energy levels into allowed bands separated by a forbidden gap. The size of the gap and whether it is direct or indirect depend on the structure and atomic spacing.

**2. It sets carrier mobility.** In a perfectly periodic lattice electrons move without being scattered. Any break in periodicity (lattice vibrations, impurities, defects, grain boundaries) scatters them. Single crystals therefore have much higher mobility than polycrystalline or amorphous material, which is why devices are made on single-crystal wafers.

**3. Properties depend on direction (anisotropy).** Surface atom density, oxidation rate, etch rate and the density of interface traps all depend on which crystal plane is exposed. MOS chips use (100) wafers because they give the lowest Si/SiO₂ interface-trap density; KOH etches (100) much faster than (111), giving V-grooves used in MEMS.

**4. Doping and diffusion.** A dopant becomes electrically active only when it occupies a substitutional lattice site. The open diamond structure (only 34 % of space filled by atoms) also allows atoms to diffuse through interstitial spaces.

**5. Epitaxy and heterostructures.** A defect-free layer can be grown only on a substrate with the same structure and almost the same lattice constant (e.g. AlGaAs on GaAs, both ≈ 0.565 nm).

**6. Defects control lifetime and leakage.** Departures from the ideal structure (vacancies, dislocations, grain boundaries) introduce energy states in the gap that trap carriers and act as recombination centres, shortening carrier lifetime and increasing junction leakage.

**7. Mechanical behaviour.** Cleavage planes (e.g. {111} in Si, {110} in GaAs), hardness and how wafers are sawn and diced follow from the structure and bond directions.

**Conclusion.** The crystal structure is not just geometry: it fixes the band structure, how fast carriers move, how the material can be doped, grown and processed, and how reliable the final device is.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ definition: periodic 3-D array of points, identical surroundings
- ✓ unit cell and lattice constant mentioned
- ✓ crystal = lattice + basis
- ✓ example: Si diamond cubic (two FCC lattices, 4 neighbours, a = 0.543 nm) and/or GaAs zinc blende
- ✓ periodic potential gives energy bands and the band gap
- ✓ single crystal gives high mobility; defects and grain boundaries scatter carriers
- ✓ anisotropy and wafer orientation ((100) for MOS)
- ✓ at least two further points (doping sites, epitaxy/lattice matching, defects, cleavage)

**Common mistakes.**

- Defining a lattice as "a group of atoms". A lattice is an array of *points*; the atoms are the basis placed on the points.
- Confusing "lattice" with "unit cell". The unit cell is the smallest repeating block; the lattice is the whole infinite array.
- Giving only one vague reason ("structure affects properties"). Name specific effects: bands, mobility, anisotropy, epitaxy, defects.
- Saying silicon is "simple cubic" or "FCC". It is diamond cubic: an FCC lattice with a two-atom basis.

**Remember it.** "Order makes bands, breaks in order make trouble."

**Try a variant.** Calculate the number of atoms per m³ in silicon, given that its diamond-cubic unit cell (a = 0.543 nm) contains 8 atoms. *Answer:* Atoms per cell = 8 corners × 1/8 + 6 faces × 1/2 + 4 inside = 8. Volume of cell = a³ = (5.43×10⁻¹⁰ m)³ = 1.60×10⁻²⁸ m³. Atom density = 8 / 1.60×10⁻²⁸ = **5.0×10²⁸ atoms/m³**.

---

### Q6. Define Miller indices and explain how they are used to identify crystal planes.

> **Question type:** Definition and explanation · **Topic:** Miller indices · **Full notes:** Week 1 (Introduction to Semiconductor Materials)

**What the examiner wants.** A precise definition (smallest integers proportional to the reciprocals of the intercepts), the step-by-step procedure for finding them, the rules for zero and negative indices, the bracket notation, and a worked example. Stating why they matter in semiconductor processing completes the answer.

**Key terms.**

- **Crystal plane:** a flat sheet passing through lattice points of a crystal.
- **Intercept:** the distance from the origin at which a plane cuts a crystal axis, measured in units of the lattice constants a, b, c.
- **Reciprocal:** one divided by a number; the reciprocal of 2 is 1/2, and of ∞ is 0.
- **Lattice constant (a, b, c):** the edge lengths of the unit cell; in a cubic crystal a = b = c.
- **Lowest common multiple (LCM):** the smallest number that all the denominators divide into exactly.
- **Interplanar spacing (d_hkl):** the perpendicular distance between neighbouring parallel planes of the same (h k l) set.
- **Wafer orientation:** the crystal plane parallel to the wafer surface, e.g. a (100) wafer.

**Model answer.**

**Definition.** Miller indices are a set of three smallest whole numbers (h k l), proportional to the **reciprocals of the intercepts** a plane makes on the x, y and z crystal axes (measured in units of the lattice constants a, b, c). They specify the orientation of that plane and of every plane parallel to it.

**Procedure for finding them.**

1. Choose an origin at a lattice point that does not lie on the plane, and find where the plane cuts the x, y and z axes, in units of a, b and c. Call these intercepts p, q and r.
2. Take the reciprocals 1/p, 1/q, 1/r.
3. Multiply all three by the LCM of the denominators to clear the fractions.
4. Reduce to the smallest set of integers with the same ratio and write them in round brackets with no commas: (h k l).

In symbols:

    (h k l) = smallest integers in the ratio 1/p : 1/q : 1/r

Where:

- h, k, l = Miller indices for the x, y, z axes (integers)
- p, q, r = intercepts on the x, y, z axes, in units of a, b, c

**Rules.**

- A plane **parallel** to an axis meets it at infinity; 1/∞ = 0, so that index is **zero**. For example, a plane cutting x at a and parallel to y and z is (1 0 0).
- A **negative** intercept gives a negative index, written with a bar over the number, e.g. (1̄ 1 0).
- A large index means the plane cuts that axis close to the origin.

**Worked example.** Intercepts a, 2b, 3c → p, q, r = 1, 2, 3 → reciprocals 1, 1/2, 1/3 → multiply by 6 → **(6 3 2)**.

**Notation.**

| Notation | Meaning |
|---|---|
| (h k l) | One particular plane (and all planes parallel to it) |
| {h k l} | A family of planes equivalent by symmetry, e.g. {100} = (100), (010), (001) and their negatives |
| [u v w] | A direction in the crystal |
| ⟨u v w⟩ | A family of equivalent directions |

In a cubic crystal the direction [h k l] is perpendicular to the plane (h k l), and the spacing of the planes is

    d_hkl = a / √(h² + k² + l²)

Where:

- d_hkl = spacing between neighbouring (h k l) planes (nm)
- a = lattice constant of the cubic cell (nm); Si 0.543 nm
- h, k, l = the Miller indices

@fig figures/planes.svg | The (100), (110) and (111) planes of a cubic unit cell, the three planes most used in semiconductor work.

Sketch in the exam: a cube with x, y, z axes and the (100), (110) and (111) planes shaded, each labelled.

**How they are used in semiconductors.**

- **Wafer specification:** wafers are sold as (100) or (111). MOS ICs use (100) because it has the lowest Si/SiO₂ interface-trap density; bipolar and some power devices use (111).
- **Processing:** oxidation rate, etch rate and surface atom density depend on the plane; KOH etches (100) much faster than (111), forming 54.7° V-grooves.
- **Cleavage and dicing:** Si cleaves along {111}, GaAs along {110}.
- **Ion implantation:** wafers are tilted about 7° away from low-index directions to avoid channelling.
- **X-ray diffraction:** each diffraction peak is labelled by the (h k l) planes that produce it, which is how crystal orientation is checked.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ definition: smallest integers proportional to the reciprocals of the intercepts
- ✓ intercepts measured in units of the lattice constants
- ✓ four-step procedure (intercepts, reciprocals, clear fractions, reduce)
- ✓ zero index for a plane parallel to an axis; bar for a negative index
- ✓ notation (h k l), {h k l}, [u v w], ⟨u v w⟩
- ✓ worked example with the correct answer
- ✓ d_hkl = a/√(h² + k² + l²) or [h k l] ⊥ (h k l) in cubic crystals
- ✓ at least one use (wafer orientation (100)/(111), etching, cleavage, XRD)

**Common mistakes.**

- Using the intercepts directly instead of their reciprocals: intercepts 1, 2, 3 do **not** give (1 2 3).
- Writing a plane parallel to an axis as "∞" in the indices. The index is 0.
- Mixing brackets: (100) is a plane, [100] is a direction, {100} is a family of planes.
- Leaving a common factor, e.g. writing (2 2 0) instead of (1 1 0).

**Remember it.** "Intercept, invert, clear, reduce": flip the intercepts, clear the fractions, bracket the smallest whole numbers.

**Try a variant.** Find the spacing of the (111) planes in silicon (a = 0.543 nm). *Answer:* d₁₁₁ = a/√(1² + 1² + 1²) = 0.543/√3 = **0.314 nm** (0.3135 nm). For comparison d₁₀₀ = 0.543 nm.

---

### Q7. Determine the Miller indices of a crystal plane having intercepts of 2a, 3b, and 1c.

> **Question type:** Calculation · **Topic:** Miller indices · **Full notes:** Week 1 (Introduction to Semiconductor Materials)

**What the examiner wants.** The standard procedure laid out step by step: write the intercepts in lattice units, take reciprocals, clear fractions with the lowest common multiple, check no common factor remains, and state the answer in round brackets. A sketch of the plane is a bonus.

**Key terms.**

- **Miller indices (h k l):** the smallest integers proportional to the reciprocals of a plane's intercepts on the crystal axes; they name the plane's orientation.
- **Intercept:** where the plane cuts an axis, in units of the lattice constants a, b, c.
- **Lattice constants (a, b, c):** the edge lengths of the unit cell along x, y and z.
- **Reciprocal:** 1 divided by the number.
- **Lowest common multiple (LCM):** the smallest number into which all the denominators divide exactly.
- **Interplanar spacing (d_hkl):** perpendicular distance between neighbouring parallel planes; for a cubic crystal d_hkl = a/√(h² + k² + l²).

**Model answer.**

**Given:** intercepts x = 2a, y = 3b, z = 1c, i.e. p = 2, q = 3, r = 1 in lattice units.

**Find:** the Miller indices (h k l).

**Formula:**

    (h k l) = smallest integers in the ratio 1/p : 1/q : 1/r

Where:

- h, k, l = Miller indices for the x, y, z axes
- p, q, r = intercepts on the x, y, z axes in units of a, b, c

**Solution.**

Step 1. Write the intercepts in lattice units: 2, 3, 1.

Step 2. Take reciprocals: 1/2, 1/3, 1/1.

Step 3. The denominators are 2, 3 and 1; their LCM is 6. Multiply each reciprocal by 6: 6 × 1/2 = 3, 6 × 1/3 = 2, 6 × 1 = 6.

Step 4. Check for a common factor: 3, 2 and 6 share none (the highest common factor is 1), so no reduction is needed.

| Step | x | y | z |
|---|---|---|---|
| Intercepts (units of a, b, c) | 2 | 3 | 1 |
| Reciprocals | 1/2 | 1/3 | 1 |
| × LCM (6) | 3 | 2 | 6 |

**Answer:** **Miller indices = (3 2 6)**, read "three two six".

**Check:** going back, 1/3 : 1/2 : 1/6 = 2 : 3 : 1 when multiplied by 6, which reproduces the original intercepts.

**Spacing (if the crystal is cubic):**

    d₃₂₆ = a / √(3² + 2² + 6²) = a / √49 = a/7

Where:

- d₃₂₆ = spacing between neighbouring (3 2 6) planes
- a = lattice constant of the cubic cell

**What this means:** the plane cuts the z-axis closest to the origin (at 1c), so z receives the largest index (6); the y intercept is farthest (3b), so y receives the smallest (2). Every plane parallel to this one carries the same name, (3 2 6). Such a high-index plane is steeply tilted and its planes are closely spaced (a/7, against a for (100)), unlike the low-index (100) and (111) planes used for wafers.

@fig figures/miller-326.svg | The (3 2 6) plane, which cuts the x-axis at 2a, the y-axis at 3b and the z-axis at 1c.

Sketch in the exam: x, y, z axes with marks at 2a on x, 3b on y and 1c on z, joined to form a shaded triangle, labelled (3 2 6).

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ intercepts written in lattice units: 2, 3, 1
- ✓ reciprocals: 1/2, 1/3, 1
- ✓ LCM 6 used to clear fractions
- ✓ check that no common factor remains
- ✓ answer (3 2 6) in round brackets
- ✓ neat step table or numbered steps
- ✓ optional: sketch of the plane, or d = a/7 for a cubic crystal

**Common mistakes.**

- Writing the intercepts as the answer, (2 3 1). Miller indices come from the **reciprocals**.
- Reciprocating correctly but then inverting the order, giving (2 3 6) or (6 2 3). Keep the order x, y, z throughout.
- Multiplying by 2 or 3 only, leaving a fraction (e.g. 1, 2/3, 2). Use the LCM of all denominators.
- Using square brackets [3 2 6]: that is a direction, not a plane.

**Remember it.** "Small intercept, big index": the axis the plane hits nearest the origin gets the largest number.

**Try a variant.** A plane has intercepts 3a, 2b and is parallel to the z-axis. Find its Miller indices. *Answer:* Intercepts 3, 2, ∞ → reciprocals 1/3, 1/2, 0 → × 6 → **(2 3 0)**. The zero shows the plane is parallel to z.

---

### Q8. Explain the difference between covalent, ionic, and metallic bonding and identify the dominant bonding mechanism in silicon.

> **Question type:** Explain and identify · **Topic:** bonding in solids · **Full notes:** Week 1 (Introduction to Semiconductor Materials)

**What the examiner wants.** "Explain the difference" means you describe each bond by how the valence electrons are held, then state the consequences (directional or not, free electrons or not, electrical behaviour) and give an example of each. "Identify" needs a clear one-word answer for silicon (covalent), backed by a reason: four valence electrons, four bonds, tetrahedral lattice.

**Key terms.**

- **Valence electrons:** the electrons in an atom's outermost shell; they are the ones that form bonds. Silicon has four.
- **Octet (full outer shell):** eight electrons in the outer shell, the stable arrangement that atoms reach by bonding.
- **Electronegativity:** how strongly an atom attracts electrons towards itself. A large difference between two atoms favours ionic bonding.
- **Ion:** an atom that has lost electrons (positive ion, e.g. Na⁺) or gained them (negative ion, e.g. Cl⁻).
- **Directional bond:** a bond that points along fixed directions, so it fixes the angles between neighbouring atoms.
- **Delocalised electrons:** electrons not tied to any one atom, free to move through the whole crystal.
- **Electron–hole pair:** a free electron plus the empty bond (hole) it leaves behind when a covalent bond breaks.

**Model answer.**

**1. Covalent bonding.** Neighbouring atoms **share** pairs of valence electrons, one electron from each atom, so that each atom completes its outer shell (eight electrons). The shared pair sits between the two atoms, so the bond is strong and **directional**: it fixes the crystal geometry. At low temperature the electrons are locked in the bonds, but a modest amount of energy can free some of them, so covalent solids are **semiconductors or insulators**. They are hard with high melting points. Examples: Si, Ge, diamond (C).

**2. Ionic bonding.** One atom **transfers** one or more electrons to another atom of very different electronegativity. This creates a positive ion and a negative ion, which are held together by electrostatic (Coulomb) attraction. The attraction acts equally in all directions, so the bond is **non-directional**. The electrons are tightly held by the ions, so there are no free carriers: ionic solids are **insulators** with a large band gap, hard and brittle, and conduct only when molten or dissolved. Example: Na⁺Cl⁻.

**3. Metallic bonding.** Each atom releases its valence electrons into a common **"sea" of delocalised electrons** shared by the whole crystal. The sea holds the lattice of positive ion cores together. The bond is **non-directional**, and the free electron sea gives very high electrical and thermal **conductivity**, lustre and ductility. Examples: Cu, Al, Na.

**4. The key differences** can be summed up in a table:

| | Covalent | Ionic | Metallic |
|---|---|---|---|
| What happens to valence electrons | Shared between pairs of neighbours | Transferred from one atom to another | Shared by all atoms (electron sea) |
| What holds the solid together | Shared electron pairs | Attraction of + and − ions | Attraction of ion cores to the electron sea |
| Directional? | Yes | No | No |
| Free electrons | Few (made thermally) | None | Very many |
| Electrical behaviour | Semiconductor or insulator | Insulator | Conductor |
| Example | Si, Ge, C | NaCl, MgO | Cu, Al |

**5. Dominant bonding in silicon: covalent.**

- Silicon (atomic number 14, shells 2, 8, 4) has **four valence electrons**.
- In the crystal (diamond-cubic lattice) each Si atom sits at the centre of a tetrahedron and forms **four covalent bonds** with four nearest neighbours, at **109.5°** to each other (sp³ bonds). It shares one electron pair with each neighbour, so every atom is surrounded by eight shared electrons, a full octet.
- All the atoms are identical, so there is no electronegativity difference and **no ionic character**; and the electrons stay in the bonds, so there is no electron sea.
- The bonds are only moderately strong. At 0 K every electron is in a bond and pure Si is an insulator. At room temperature thermal energy breaks a few bonds (the energy needed to free an electron is the band gap, E_g = 1.12 eV), creating **electron–hole pairs**. This is exactly what makes silicon a semiconductor.

@fig figures/si-bonds.svg | Silicon drawn flat: each atom shares one electron pair with each of its four neighbours. One bond has been broken by heat, leaving a free electron and a hole.

*Sketch in the exam:* a 3 × 3 grid of Si atoms, each joined to four neighbours by double lines (two shared electrons per bond), with one broken bond showing a free electron and a hole. Label "Si", "shared electron pair", "free electron", "hole".

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ covalent = sharing of electron pairs; directional; example (Si, Ge, diamond)
- ✓ ionic = electron transfer, Coulomb attraction between + and − ions; non-directional; example (NaCl)
- ✓ metallic = delocalised electron sea binding positive ion cores; non-directional; example (Cu)
- ✓ consequence for electrical behaviour of each (semiconductor/insulator, insulator, conductor)
- ✓ silicon identified as covalent
- ✓ reason: four valence electrons, four bonds to four neighbours, full octet
- ✓ tetrahedral (diamond-cubic) arrangement, 109.5°
- ✓ link to semiconduction: thermal breaking of bonds creates electron–hole pairs (E_g = 1.12 eV)

**Common mistakes.**

- Saying silicon has "free electrons like a metal". It does not: at 0 K every electron is in a bond; free electrons appear only when bonds are broken.
- Describing ionic bonding as "sharing". Ionic is *transfer*; covalent is *sharing between two atoms*; metallic is *sharing by all atoms*. Keep the three verbs distinct.
- Forgetting to give examples and the "directional / non-directional" property: both are easy marks.
- Writing that silicon is "partly ionic" like GaAs. Si–Si bonds join identical atoms, so silicon is purely covalent.

**Remember it.** Covalent **shares** with a neighbour, ionic **gives** to a neighbour, metallic **gives to everyone**; silicon shares, four bonds each.

**Try a variant.** Identify the bonding in gallium arsenide and explain how it differs from that in silicon. *Answer:* GaAs is **mainly covalent with partial ionic character**. Ga (group III, 3 valence electrons) and As (group V, 5 valence electrons) together supply an average of four electrons per atom, so each atom still forms four tetrahedral bonds, as in Si. But As attracts electrons more strongly than Ga (higher electronegativity), so the shared pairs sit closer to As, giving As a small negative and Ga a small positive charge. Silicon, with identical atoms, has no such charge transfer and is purely covalent.

---

### Q9. Describe the major stages involved in converting metallurgical-grade silicon (MG-Si) into electronic-grade silicon (EG-Si).

> **Question type:** Describe · **Topic:** silicon purification · **Full notes:** Week 2 (Material Growth Techniques)

**What the examiner wants.** A sequence of stages in the right order, each with its chemical reaction, approximate temperature and purpose. A complete answer starts from MG-Si (briefly saying how it is made), goes through hydrochlorination, distillation and the Siemens process, and states the purity reached.

**Key terms.**

- **Metallurgical-grade silicon (MG-Si):** silicon about 98 % pure, made by reducing quartz with carbon in an arc furnace; too impure for devices.
- **Electronic-grade silicon (EG-Si):** polycrystalline silicon of 99.9999999 % ("9N") purity or better, i.e. at most about one impurity atom per billion silicon atoms.
- **Trichlorosilane (SiHCl₃):** a silicon compound that is liquid at room temperature (boils at 32 °C), used as the carrier that can be purified.
- **Fractional distillation:** separating liquids by repeatedly boiling and condensing them, using their different boiling points.
- **Chemical vapour deposition (CVD):** growing a solid from gases that react on a hot surface.
- **Siemens process:** the CVD step in which purified SiHCl₃ and hydrogen deposit pure silicon on heated silicon rods.
- **Polycrystalline silicon (polysilicon):** solid silicon made of many small crystal grains pointing in different directions.

**Model answer.**

**The idea.** A solid cannot easily be purified to parts per billion, but a liquid can, by distillation. So silicon is turned into a liquid compound, purified, and then turned back into solid silicon.

    MG-Si → SiHCl₃ (liquid) → distilled SiHCl₃ → EG-Si polysilicon

**Starting material: MG-Si.** Quartzite (SiO₂) is reduced with carbon (coke, coal, wood chips) in an electric arc furnace at about 2000 °C:

    SiO₂ + 2C → Si + 2CO

The product is about 98 % pure; the main impurities are Fe, Al, Ca, C, B and P. Since silicon has 5×10²⁸ atoms per m³, 2 % impurity is of order 10²⁷ impurity atoms per m³, millions of times too many for devices.

**Stage 1: Hydrochlorination (making a liquid).** MG-Si is ground to a powder and reacted with dry hydrogen chloride gas at about 300 °C (usually in a fluidised bed with a catalyst):

    Si + 3HCl → SiHCl₃ + H₂

Silicon leaves as trichlorosilane, a liquid that boils at 32 °C. The impurities form their own chlorides (FeCl₃, BCl₃, PCl₃ …), which boil at different temperatures.

**Stage 2: Purification by fractional distillation.** The crude SiHCl₃ is distilled repeatedly. Because each impurity chloride boils at a different temperature from SiHCl₃, it is separated off. The electrically active impurities (especially B and P) are reduced to a few parts per billion.

**Stage 3: Reduction and deposition (Siemens process).** The purified SiHCl₃ is mixed with high-purity hydrogen and passed over thin silicon rods heated electrically to about 1100 °C in a CVD reactor:

    SiHCl₃ + H₂ → Si + 3HCl

Where (for all the reactions above):

- SiO₂ = silicon dioxide (quartzite); C = carbon; CO = carbon monoxide
- HCl = hydrogen chloride; H₂ = hydrogen
- SiHCl₃ = trichlorosilane

Silicon deposits on the hot rods, which grow over many hours into thick bars of **electronic-grade polysilicon**, 9N to 11N pure (an impurity level of order 10¹⁹ m⁻³ or less). The HCl and unreacted gases are collected and recycled.

**Stage 4 (to make wafers): single-crystal growth.** EG-Si is pure but polycrystalline and undoped. It is broken into chunks, melted with the required dopant and grown into a single-crystal ingot by the Czochralski or float-zone method, then sliced and polished into wafers.

**Summary table.**

| Stage | Reaction | Temperature | Result |
|---|---|---|---|
| Arc furnace | SiO₂ + 2C → Si + 2CO | ≈ 2000 °C | MG-Si, 98 % |
| 1. Hydrochlorination | Si + 3HCl → SiHCl₃ + H₂ | ≈ 300 °C | Liquid SiHCl₃ |
| 2. Fractional distillation | Physical separation | SiHCl₃ boils at 32 °C | ppb-pure SiHCl₃ |
| 3. Siemens CVD | SiHCl₃ + H₂ → Si + 3HCl | ≈ 1100 °C | EG-Si polysilicon, 9N+ |

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ MG-Si origin: SiO₂ + 2C → Si + 2CO, ≈ 2000 °C, ≈ 98 % pure
- ✓ hydrochlorination: Si + 3HCl → SiHCl₃ + H₂ at ≈ 300 °C
- ✓ reason for the liquid: SiHCl₃ boils at 32 °C, can be distilled
- ✓ fractional distillation separates impurity chlorides (different boiling points)
- ✓ Siemens process: SiHCl₃ + H₂ → Si + 3HCl on heated Si rods at ≈ 1100 °C
- ✓ product: polycrystalline EG-Si, 9N (99.9999999 %) or better
- ✓ stages in the correct order
- ✓ (bonus) HCl recycled; EG-Si then grown into a single crystal by CZ/FZ

**Common mistakes.**

- Writing that the Siemens process produces a single crystal. It produces **polycrystalline** EG-Si; the single crystal comes later from CZ or FZ growth.
- Leaving out the reason for making SiHCl₃. Say it: a liquid can be purified by distillation, a solid cannot.
- Getting the reaction direction mixed up: HCl is a *reactant* in stage 1 and a *product* in stage 3.
- Listing stages without temperatures or reactions: these carry most of the marks.

**Remember it.** "Furnace, Fizz, Fractionate, Freeze-out": arc furnace → HCl reaction → distillation → Siemens deposition.

**Try a variant.** Why is fractional distillation of SiHCl₃ such an effective purification step, and how pure must EG-Si be compared with MG-Si? *Answer:* Each impurity (Fe, B, P, Al …) forms its own chloride with a boiling point different from that of SiHCl₃ (32 °C), so repeated boiling and condensing leaves those impurities behind. MG-Si contains about 2 % impurity (≈ 10²⁷ m⁻³ in 5×10²⁸ Si atoms/m³); EG-Si at 9N contains at most one impurity per 10⁹ atoms, 5×10²⁸ × 10⁻⁹ = **5×10¹⁹ m⁻³**, about **2×10⁷ times purer**.

---

### Q10. Explain the principle and operation of the Czochralski (CZ) crystal growth method.

> **Question type:** Explain · **Topic:** Czochralski crystal growth · **Full notes:** Week 2 (Material Growth Techniques)

**What the examiner wants.** Two parts. The **principle**: why pulling a seed from a melt gives one single crystal with the seed's orientation. The **operation**: the equipment and the growth steps in order (load, melt, dip, neck, shoulder, body, tail, cool), with typical values. A labelled sketch of the puller earns marks.

**Key terms.**

- **Single crystal:** a solid whose atoms form one regular pattern with the same orientation throughout.
- **Seed crystal:** a small, perfect single crystal cut to the wanted orientation (e.g. ⟨100⟩) that starts the growth.
- **Melt:** the molten silicon in the crucible, held just above silicon's melting point of 1414 °C.
- **Ingot (boule):** the large cylindrical single crystal that is pulled; later sliced into wafers.
- **Dislocation:** a line defect, a row of atoms out of place; it causes leakage and must be removed.
- **Dash necking:** pulling a thin neck (≈ 3 mm wide) quickly at the start so that dislocations grow out of the sides.
- **Dopant:** an impurity added on purpose (boron for p-type; phosphorus, arsenic or antimony for n-type).

**Model answer.**

**1. Principle.** CZ growth is crystal **pulling from the melt**. A seed crystal is dipped into molten silicon kept just above its melting point (1414 °C) and slowly withdrawn. Heat flows up through the seed, so the liquid touching it cools and freezes. As each atom freezes, it takes up the position that continues the lattice of the solid beneath it. The growing solid therefore copies the seed, and the result is one large single crystal with **the same orientation as the seed**. The diameter is controlled by the pull rate and melt temperature: pulling faster or hotter gives a thinner crystal, slower or cooler a thicker one.

**2. Equipment.**

- **Furnace:** a fused-quartz (SiO₂) crucible holding the melt, supported in a graphite susceptor, heated by RF induction or resistance heaters.
- **Crystal-pulling mechanism:** a seed holder on a shaft that rotates and rises slowly; the crucible also rotates (opposite direction) and can be raised.
- **Ambient control:** argon gas at reduced pressure, so hot silicon does not react with air and evaporated SiO is swept away.
- **Control system:** sensors and feedback that hold the temperature and diameter constant.

@fig figures/cz.svg | A Czochralski puller: the rotating seed is lifted slowly from the melt in a quartz crucible, which rotates the other way; the frozen crystal copies the seed's orientation.

*Sketch in the exam:* crucible with melt, heater coils on both sides, the ingot above the melt with the seed and pull rod at the top, curved arrows showing opposite rotations. Label "quartz crucible", "graphite susceptor", "Si melt (1414 °C)", "heater", "seed", "neck", "ingot", "pull rod", "argon in/out".

**3. Operation (steps in order).**

1. **Load:** chunks of EG-Si polysilicon and a carefully weighed amount of dopant go into the crucible.
2. **Melt:** the chamber is purged with argon and the charge is melted (≈ 1420 °C).
3. **Dip:** the seed is lowered until it just touches the melt surface, and the temperature is adjusted so it neither melts away nor grows quickly.
4. **Neck (Dash technique):** the seed is pulled up fast to grow a thin neck about 3 mm across. Dislocations caused by the thermal shock of dipping run out of the sides, so the crystal below is dislocation-free.
5. **Shoulder:** the pull rate and temperature are lowered so the crystal widens to the target diameter (up to 300 mm).
6. **Body:** the crystal is grown at constant diameter, pulled at about **1 mm/min**, while seed and crucible **counter-rotate** (10–30 rpm) to stir the melt and keep temperature and doping even.
7. **Tail:** the pull rate is raised so the diameter narrows to a cone before the crystal leaves the melt; a sudden break would send dislocations back up the crystal.
8. **Cool:** the ingot is lifted clear and cooled slowly to avoid thermal stress.

**4. After growth.** The ingot is checked for orientation, resistivity and defects, ground to an exact diameter, given a flat or notch to mark its orientation, sliced into wafers, lapped, etched and polished.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ principle: seed dipped into melt and slowly pulled; melt freezes onto seed and copies its orientation
- ✓ melting point 1414 °C; melt held just above it
- ✓ equipment: quartz crucible, graphite susceptor, heater, rotating pull rod, argon ambient
- ✓ labelled sketch of the puller
- ✓ Dash necking explained (removes dislocations)
- ✓ shoulder, constant-diameter body, tail in order
- ✓ counter-rotation of seed and crucible, and why (stirring, uniformity)
- ✓ typical values: pull rate ≈ 1 mm/min, diameter up to 300 mm
- ✓ diameter control by pull rate and temperature

**Common mistakes.**

- Describing only the steps and forgetting the **principle** (why the crystal copies the seed). The question asks for both.
- Leaving out Dash necking, or saying it is "to make the crystal thinner". Its purpose is to **remove dislocations**.
- Saying seed and crucible rotate the same way: they rotate in **opposite** directions.
- Mixing up CZ with float-zone growth: CZ uses a crucible; FZ has none.

**Remember it.** "Dip, Neck, Shoulder, Body, Tail": the crystal copies the seed it is pulled from.

**Try a variant.** A 300 mm CZ ingot body 1.5 m long is pulled at 1.2 mm/min. How long does the body take to grow, and what is its mass (density of Si 2330 kg/m³)? *Answer:* t = L/v = 1.5 m ÷ 1.2×10⁻³ m/min = 1250 min ≈ **20.8 h**. m = density × πr²L = 2330 × π × 0.15² × 1.5 = **247 kg**, so the crucible must be charged with well over 250 kg of silicon.

---

### Q11. State four advantages and two limitations of the Czochralski method.

> **Question type:** State · **Topic:** Czochralski crystal growth · **Full notes:** Week 2 (Material Growth Techniques)

**What the examiner wants.** "State" means a short, clear list: exactly four advantages and two limitations, each in one or two sentences with a reason or number. No long description of the process is needed.

**Key terms.**

- **Czochralski (CZ) method:** growing a single crystal by slowly pulling a rotating seed from molten silicon held in a quartz crucible.
- **Float-zone (FZ) method:** the crucible-free alternative, in which a molten zone is moved along a polysilicon rod.
- **Segregation coefficient (k₀):** the ratio of dopant concentration in the freezing solid to that in the liquid, k₀ = C_s/C_l; for most dopants k₀ < 1 (B 0.8, P 0.35).
- **Resistivity (ρ):** how strongly the material opposes current (Ω·m); set mainly by the doping.
- **Intrinsic gettering:** trapping of metal impurities by oxygen precipitates deep in the wafer, away from the devices at the surface.
- **Dislocation:** a line defect in the crystal that causes leakage.

**Model answer.**

**Advantages.**

1. **Large diameters.** Ingots of 200 mm and 300 mm diameter are routine, so many chips fit on each wafer and the cost per chip is low.
2. **Dislocation-free crystals of chosen orientation.** The ingot copies the seed, so (100) or (111) material is obtained at will, and Dash necking removes dislocations.
3. **Controlled doping.** Dopant added to the melt sets the conductivity type and resistivity of the crystal.
4. **High throughput and low cost.** The process is mature and automated, and fast enough that about 95 % of all silicon wafers are CZ-grown.

(A fifth acceptable advantage: the **oxygen** picked up from the crucible strengthens the wafer against warping and slip and allows **intrinsic gettering**.)

**Limitations.**

1. **Contamination from the crucible.** The hot quartz crucible slowly dissolves, adding oxygen (≈ 10²⁴ m⁻³), and graphite parts add carbon. Oxygen forms thermal donors and precipitates and limits the resistivity to about 1 Ω·m or less, so CZ silicon is unsuitable for high-voltage power devices and detectors (FZ is used instead).
2. **Non-uniform doping along the ingot (segregation).** Because k₀ < 1, the crystal rejects dopant into the melt, which becomes steadily richer. The doping therefore rises from the seed end to the tail end:

    C_s = k₀ C₀ (1 − f)^{k₀ − 1}

Where:

- C_s = dopant concentration in the crystal at the point being grown (m⁻³)
- k₀ = segregation coefficient (dimensionless)
- C₀ = dopant concentration in the starting melt (m⁻³)
- f = fraction of the melt already frozen (0 at the seed end)

So resistivity varies along the ingot; melt convection also causes radial variations (growth striations).

(Also acceptable: the crucible is used up each run; high energy use; batch process.)

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ exactly four advantages listed, each with a reason
- ✓ large diameter (200–300 mm) → low cost per chip
- ✓ dislocation-free single crystal with the seed's orientation
- ✓ controlled doping / resistivity
- ✓ high throughput, mature, low cost (or oxygen strengthening and gettering)
- ✓ limitation: oxygen (≈ 10²⁴ m⁻³) and carbon contamination from crucible; limits resistivity
- ✓ limitation: axial doping non-uniformity from segregation, k₀ < 1

**Common mistakes.**

- Giving more or fewer items than asked, or mixing advantages and limitations in one list. Use two numbered lists.
- Listing "oxygen" only as a limitation without noticing it is also an advantage (strength, gettering). Either is fine if you explain it; do not contradict yourself.
- Vague points such as "good quality". Say what is good: dislocation-free, chosen orientation, large diameter.
- Writing that doping *falls* along the ingot. For k₀ < 1 it **rises** towards the tail.

**Remember it.** CZ is **Big, Perfect, Doped and Cheap**, but **Oxygen-laden and Uneven**.

**Try a variant.** An arsenic-doped CZ ingot (k₀ = 0.3) is grown. By what factor is the arsenic concentration at the half-way point (f = 0.5) higher than at the seed end? *Answer:* C_s(f)/C_s(0) = (1 − f)^{k₀ − 1} = (0.5)^{−0.7} = **1.62**, so the doping is 62 % higher and the resistivity about 38 % lower half-way along: a clear example of limitation 2.

---

### Q12. Explain the principles of vapour-phase epitaxy (VPE), liquid-phase epitaxy (LPE), and molecular-beam epitaxy (MBE).

> **Question type:** Explain · **Topic:** epitaxial growth · **Full notes:** Week 2 (Material Growth Techniques)

**What the examiner wants.** First define epitaxy. Then, for each of the three methods, explain where the atoms come from and why they settle in the crystal, with an example reaction or material, the typical temperature and pressure, and how doping is done. A labelled sketch of each set-up earns marks.

**Key terms.**

- **Epitaxy:** growing a thin single-crystal layer on a single-crystal wafer so that the layer continues the wafer's crystal structure and orientation.
- **Substrate:** the wafer on which the layer is grown.
- **Homoepitaxy / heteroepitaxy:** growing the same material (Si on Si) / a different material (AlGaAs on GaAs).
- **Supersaturated solution:** a liquid holding more dissolved material than it can keep at that temperature, so the excess comes out as solid.
- **Ultra-high vacuum (UHV):** pressure of about 10⁻¹⁰ Torr, so low that atoms travel in straight lines without colliding.
- **Effusion cell:** a small heated oven that evaporates one element to make an atomic beam (MBE).
- **RHEED (reflection high-energy electron diffraction):** an electron beam bounced off the growing surface; its pattern shows the surface order and counts atomic layers.
- **MOCVD:** metal-organic chemical vapour deposition, the version of VPE used for III–V compounds.

**Model answer.**

**Epitaxy.** Epitaxy (Greek *epi*, "upon", *taxis*, "arrangement") is the growth of a thin single-crystal layer on a single-crystal substrate so that the layer takes the substrate's crystal structure and orientation. It is used to make layers with different doping or a different material from the substrate, with sharp boundaries. The three methods differ in the **phase from which the atoms arrive**: gas, liquid or atomic beam.

@fig figures/epitaxy.svg | The three epitaxy methods: reacting gases on a hot wafer (VPE), a cooling saturated melt on the wafer (LPE), and atomic beams in ultra-high vacuum (MBE).

#### Vapour-phase epitaxy (VPE)

**Principle: growth from a gas by chemical reaction at a hot surface.** A gas containing the semiconductor, carried by hydrogen, flows over a heated substrate in a reactor. At the hot surface the gas decomposes or is reduced, leaving semiconductor atoms behind. These atoms move over the surface until they reach lattice sites, so the layer continues the substrate crystal. For silicon:

    SiCl₄ + 2H₂ → Si + 4HCl      (≈ 1150–1250 °C)
    SiH₄ → Si + 2H₂              (≈ 600–1000 °C)

Where:

- SiCl₄ = silicon tetrachloride; SiH₄ = silane (silicon sources)
- H₂ = hydrogen (carrier and reducing gas); HCl = hydrogen chloride (by-product)

**Doping:** a little dopant gas is added: diborane (B₂H₆) for p-type, phosphine (PH₃) or arsine (AsH₃) for n-type. **Rate control:** at high temperature the rate is limited by how fast gas reaches the surface (mass-transport limited); at lower temperature by the surface reaction (reaction-rate limited). Pressure is atmospheric or reduced. For III–V compounds the metal-organic form, MOCVD, is used, e.g. (CH₃)₃Ga + AsH₃ → GaAs + 3CH₄ at 600–750 °C.

#### Liquid-phase epitaxy (LPE)

**Principle: growth by precipitation from a cooling saturated solution.** The semiconductor is dissolved in a molten metal solvent until the solution is saturated, e.g. GaAs in liquid gallium at about 700–900 °C. The substrate is brought into contact with the solution and the whole is cooled slowly (≈ 0.1–1 °C/min). As the temperature falls the solution can hold less, becomes **supersaturated**, and the excess semiconductor crystallises onto the substrate, continuing its lattice. Growth takes place **close to thermodynamic equilibrium**, so the crystal is of high quality. A **sliding graphite boat** moves the substrate under a series of melts of different composition or doping to build up multilayers. Dopants are added to the melt.

#### Molecular-beam epitaxy (MBE)

**Principle: physical deposition from atomic beams in ultra-high vacuum.** In a chamber at about 10⁻¹⁰ Torr, each element (Ga, As, Al, dopants such as Si or Be) is heated in its own **effusion cell**. Evaporated atoms travel as collision-free **beams** in straight lines to a heated substrate (≈ 500–650 °C for GaAs). They adsorb, migrate on the surface and are incorporated into lattice sites. Each cell has a **shutter** that opens or closes in a fraction of a second, so composition and doping can be switched abruptly. Growth is slow, about **one atomic layer per second** (≈ 1 μm/h), and is watched in real time by **RHEED**, so thickness is controlled to a single atomic layer. Growth is **far from equilibrium** and controlled by the beam fluxes.

**In one sentence each.** VPE: gas reacts on a hot wafer. LPE: a saturated melt is cooled so solid comes out onto the wafer. MBE: beams of atoms in vacuum stick to the wafer one layer at a time.

*Sketch in the exam:* (a) VPE: horizontal tube, gas inlet (SiCl₄ + H₂), wafers on a heated susceptor, exhaust (HCl). (b) LPE: graphite boat with wells of melt, sliding slider carrying the substrate, furnace. (c) MBE: vacuum chamber, heated substrate facing several effusion cells with shutters, RHEED gun and screen.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ definition of epitaxy (layer continues substrate structure and orientation)
- ✓ VPE: gas-phase source, reaction on hot surface; SiCl₄ + 2H₂ → Si + 4HCl at ≈ 1200 °C
- ✓ VPE doping gases (B₂H₆, PH₃, AsH₃); mention of MOCVD for III–V
- ✓ LPE: saturated solution in molten metal, cooled → supersaturation → precipitation on substrate
- ✓ LPE example: GaAs in Ga, 700–900 °C, sliding graphite boat
- ✓ MBE: UHV ≈ 10⁻¹⁰ Torr, effusion cells, collision-free beams, shutters
- ✓ MBE: ≈ 1 monolayer/s, atomic-layer control, RHEED monitoring
- ✓ labelled sketches (any of the three)

**Common mistakes.**

- Explaining MBE as a chemical reaction. MBE is **physical** deposition of elemental atoms; VPE is the chemical method.
- Forgetting *why* LPE grows: cooling makes the solution supersaturated. "The wafer is dipped in a melt" alone does not explain the principle.
- Not defining epitaxy, or confusing it with simply depositing any film. An epitaxial layer must be **single-crystal and aligned** with the substrate.
- Quoting the MBE vacuum as "low vacuum". It is **ultra-high** vacuum, which is what keeps the beams collision-free.

**Remember it.** **V**apour **R**eacts, **L**iquid **P**recipitates, **M**olecular **B**eams **B**uild layer by layer.

**Try a variant.** Why must MBE be carried out in ultra-high vacuum? *Answer:* Two reasons. (1) The atoms must reach the wafer as beams without colliding with gas molecules: the mean free path of a gas molecule is roughly λ ≈ 5×10⁻⁵/P m (P in Torr), so at 10⁻¹⁰ Torr λ ≈ 5×10⁵ m (about 500 km), far longer than the ≈ 0.2 m cell-to-wafer distance. (2) At one atomic layer per second the surface is easily contaminated, so the background gas must be extremely low to keep the layer pure. UHV also allows electron-beam monitoring (RHEED) during growth.

---

### Q13. Compare VPE, LPE, and MBE in terms of growth mechanism, temperature, precision, and applications.

> **Question type:** Compare · **Topic:** epitaxial growth · **Full notes:** Week 2 (Material Growth Techniques)

**What the examiner wants.** A point-by-point comparison under the four headings named (growth mechanism, temperature, precision, applications), with numbers where possible, ending with a comparison table and a one-line conclusion on when each method is chosen. Extra rows (growth rate, cost, purity) add strength but the four named headings must be there.

**Key terms.**

- **Epitaxy:** growth of a thin single-crystal layer that continues the crystal structure and orientation of the substrate below it.
- **VPE (vapour-phase epitaxy):** epitaxy from gases that react on a hot wafer; MOCVD is its metal-organic form for III–V compounds.
- **LPE (liquid-phase epitaxy):** epitaxy by precipitation from a saturated solution in molten metal as it cools.
- **MBE (molecular-beam epitaxy):** epitaxy from beams of atoms in ultra-high vacuum.
- **Monolayer:** one atomic layer of the crystal, about 0.28 nm thick for GaAs.
- **Interface abruptness:** how sharply the composition or doping changes from one layer to the next.
- **Autodoping / out-diffusion:** unwanted transfer of dopant from the substrate into the growing layer, by evaporation and re-deposition / by diffusion at high temperature.
- **Quantum well / heterostructure:** a very thin layer (a few nm) of one semiconductor sandwiched between another; it needs atomically sharp interfaces.

**Model answer.**

**1. Growth mechanism.**

- **VPE:** chemical. Gas-phase compounds (SiCl₄, SiH₄, or metal-organics in MOCVD) react or decompose at the hot substrate surface and leave atoms behind, e.g. SiCl₄ + 2H₂ → Si + 4HCl. Rate is limited by mass transport or surface reaction.
- **LPE:** precipitation from a liquid. A saturated solution (GaAs in molten Ga) is cooled, becomes supersaturated, and deposits the semiconductor on the substrate. Growth is close to equilibrium.
- **MBE:** physical. Atoms evaporated from effusion cells travel as beams in ultra-high vacuum (≈ 10⁻¹⁰ Torr), adsorb and migrate on the substrate. Growth is far from equilibrium, set by the beam fluxes.

**2. Temperature.**

- **VPE:** highest. Silicon 1000–1250 °C (SiCl₄ ≈ 1200 °C); silane can work lower; MOCVD 600–750 °C for GaAs.
- **LPE:** intermediate, about 700–900 °C for GaAs.
- **MBE:** lowest, about 500–650 °C for GaAs. Low temperature means little diffusion, which keeps interfaces sharp.

**3. Precision (thickness control and interfaces).**

- **VPE:** good, about tens of nm, with good uniformity over many wafers; interfaces moderately sharp, blurred by autodoping and out-diffusion at high temperature. Growth rate 0.1–5 μm/min.
- **LPE:** poorest, about 0.1 μm; interfaces graded and surfaces rough, though crystal quality and purity are very high. Growth rate 0.1–1 μm/min.
- **MBE:** best, a single atomic layer (≈ 0.28 nm for GaAs); atomically abrupt interfaces controlled by shutters and monitored by RHEED. Growth rate slow, ≈ 1 μm/h (≈ 1 monolayer/s).

**4. Applications.**

- **VPE:** silicon epitaxial layers for bipolar transistors, CMOS and power devices; in MOCVD form, mass production of LEDs, lasers, solar cells and HEMTs (GaAs, InP, GaN).
- **LPE:** LEDs, early heterostructure lasers, photodetectors, thick high-quality III–V layers.
- **MBE:** quantum wells, superlattices, high-electron-mobility transistors (HEMTs), heterojunction bipolar transistors (HBTs), quantum-cascade and VCSEL lasers, and research.

**Comparison table.**

| Feature | VPE | LPE | MBE |
|---|---|---|---|
| Source phase | Gas (SiCl₄, SiH₄, metal-organics) | Liquid solution in molten metal | Atomic/molecular beams from solid sources |
| Growth mechanism | Chemical reaction at hot surface | Precipitation from supersaturated solution on cooling; near equilibrium | Physical deposition, adsorption and surface migration; far from equilibrium |
| Pressure | Atmospheric or reduced | Atmospheric (H₂ or inert) | Ultra-high vacuum ≈ 10⁻¹⁰ Torr |
| Temperature | Highest: Si 1000–1250 °C (MOCVD 600–750 °C) | Medium: 700–900 °C | Lowest: 500–650 °C |
| Growth rate | 0.1–5 μm/min | 0.1–1 μm/min | ≈ 1 μm/h (≈ 1 monolayer/s) |
| Thickness precision | Good, tens of nm | Poor, ≈ 0.1 μm | Excellent, one atomic layer |
| Interfaces | Moderately sharp | Graded | Atomically abrupt |
| In-situ monitoring | Limited | None | RHEED |
| Throughput and cost | High throughput, moderate cost | Low throughput, low cost | Low throughput, very high cost |
| Applications | Si epi for BJTs, CMOS, power; MOCVD LEDs, lasers, solar cells | LEDs, early lasers, thick layers, photodetectors | Quantum wells, HEMTs, HBTs, advanced lasers, research |

**Conclusion.** VPE is the industrial workhorse for volume production; LPE is simple and cheap and gives high-quality thick layers but poor control; MBE gives atomic-scale control for advanced heterostructure devices at high cost and low throughput.

**Marking checklist.** The points a marker looks for. Tick each one off in your own answer:

- ✓ mechanism for each: chemical reaction (VPE), precipitation on cooling (LPE), physical beam deposition in UHV (MBE)
- ✓ temperature ranking with values: VPE highest (Si ≈ 1000–1250 °C), LPE 700–900 °C, MBE lowest 500–650 °C
- ✓ precision ranking: MBE (one atomic layer) > VPE (tens of nm) > LPE (≈ 0.1 μm)
- ✓ interface abruptness linked to temperature / shutters
- ✓ growth rates with units
- ✓ at least two applications per method
- ✓ comparison table covering the four named headings
- ✓ conclusion on when each method is chosen

**Common mistakes.**

- Writing three separate descriptions with no comparison. Compare *under each heading*, then give the table.
- Ranking temperatures wrongly. MBE is the **lowest**, not the highest, despite its sophisticated equipment.
- Confusing growth rate units: VPE and LPE are in μm per **minute**, MBE in μm per **hour**, a factor of about 60–300 slower.
- Calling LPE "imprecise and low quality". Its thickness control is poor, but its **crystal quality is very high** (near-equilibrium growth).

**Remember it.** Hotter, faster, coarser → VPE; cooler, slower, finer → MBE; LPE sits in the middle on temperature but last on precision.

**Try a variant.** A 10 nm GaAs quantum well is to be grown. Which method would you choose, and how long does the well take at 1 monolayer per second (monolayer thickness a/2, a = 0.5653 nm)? *Answer:* **MBE**, because only it gives single-atomic-layer control and abrupt interfaces at this thickness. Monolayer = 0.5653/2 = 0.283 nm, so 10 nm needs 10/0.283 ≈ 35 monolayers, taking **≈ 35 s** (the growth rate is 0.283 nm/s ≈ 1.0 μm/h). LPE (± 0.1 μm = 100 nm) could not even define the layer.
