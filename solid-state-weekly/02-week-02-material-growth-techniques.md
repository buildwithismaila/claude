# Week 2 — Material Growth Techniques
<!-- group: Module 1 · Material Physics & Semiconductor Growth -->

**Plan:** purification of silicon (metallurgical to electronic grade); the Czochralski bulk crystal growth method; epitaxial growth techniques (VPE, LPE, MBE).

## Learning objectives

By the end of this week you should be able to:

1. Describe the conversion of quartzite into metallurgical-grade silicon.
2. Explain how MG-Si is purified into electronic-grade silicon.
3. Explain the principle and steps of the Czochralski method.
4. State the advantages and limitations of CZ growth and compare it with float-zone growth.
5. Use the segregation coefficient to predict doping along an ingot.
6. Explain the principles of VPE, LPE and MBE and compare them.

## The big picture

To make a chip you need three things, in this order:

1. **Extremely pure silicon.** A device stops working if more than about one atom in a billion is an unwanted impurity. Sand is nowhere near that pure.
2. **One single crystal.** The atoms must be lined up perfectly across the whole wafer (Week 1). Polycrystalline silicon, with grains pointing in different directions, scatters carriers and leaks current.
3. **Thin layers on top**, with different doping or even a different material, grown so that they continue the crystal perfectly.

This week covers each step: **purification** (sand → pure polysilicon), **crystal growth** (polysilicon → one big crystal, by the Czochralski method), and **epitaxy** (growing thin crystalline layers on top).

## Part A: Purification of silicon

The whole route, from sand to wafer:

    quartzite (SiO₂) → metallurgical-grade Si (98 %) → trichlorosilane SiHCl₃ → purified SiHCl₃ → electronic-grade polysilicon → single crystal → wafers

| Stage | Product | Purity |
|---|---|---|
| Arc furnace (reduction with carbon) | Metallurgical-grade Si (MG-Si) | About 98–99 % |
| Chlorination, distillation, Siemens CVD | Electronic-grade polysilicon (EG-Si) | 99.9999999 % ("nine nines", 9N) or better |
| Czochralski or float-zone growth | Single-crystal ingot, doped as required | Dopant added deliberately |

### Step 1: making metallurgical-grade silicon (MG-Si)

Quartzite, a fairly pure form of SiO₂ (sand, quartz), is mixed with carbon (coal, coke, wood chips) and heated to about **2000 °C** in an electric arc furnace. Carbon pulls the oxygen off the silicon:

    SiO₂ + 2C → Si + 2CO

Molten silicon is drained from the furnace. This **MG-Si** is about 98 % pure. The 2 % of impurities (Fe, Al, Ca, C, B, P) is still about 10²⁰ impurity atoms per cm³, a hundred million times too many for devices. MG-Si is good enough for making steel and aluminium alloys, but not chips.

### Step 2: turning silicon into a liquid that can be purified

Solids are hard to purify; liquids are easy to purify by distillation. So the next step is to convert silicon into a liquid compound. MG-Si powder is reacted with hydrogen chloride gas at about **300 °C**:

    Si + 3HCl → SiHCl₃ + H₂

The product, **trichlorosilane (SiHCl₃)**, is a liquid that boils at only 32 °C. The impurities also react with HCl and form their own chlorides (FeCl₃, BCl₃, PCl₃ and so on), which boil at different temperatures.

### Step 3: fractional distillation

The trichlorosilane is purified by **fractional distillation**, the same process used to separate petrol from crude oil. Because SiHCl₃ and each impurity chloride boil at different temperatures, repeated distillation leaves SiHCl₃ with impurities at only a few **parts per billion**.

### Step 4: Siemens process (back to solid silicon)

The pure SiHCl₃ is now turned back into silicon. It is mixed with pure hydrogen and passed over thin silicon rods heated electrically to about **1100 °C** inside a reactor. Silicon deposits on the hot rods (chemical vapour deposition, CVD):

    SiHCl₃ + H₂ → Si + 3HCl

Over many hours the rods grow into thick bars of **electronic-grade polycrystalline silicon (EG-Si)**, 9N to 11N pure. The HCl is recycled.

EG-Si is pure but still **polycrystalline** (many small grains) and undoped. The next step turns it into a single crystal and adds the doping.

> **In plain words.** Steps 2–4 are a round trip: solid silicon → liquid compound → solid silicon. The trip is worth it because the liquid can be distilled, and distillation removes almost all the impurities.

## Part B: Czochralski (CZ) crystal growth

### The principle

Dip a small **seed crystal** into molten silicon and pull it out very slowly. Silicon from the melt freezes onto the seed, and as each atom freezes it lines up with the atoms already there. So the growing piece continues the seed's crystal, and you end up with one large single crystal (an **ingot**) with the same orientation as the seed.

It is like pulling a candle out of hot wax, except that each new layer copies the arrangement of the layer before it.

@fig figures/cz.svg | The Czochralski puller. The seed is dipped into the melt and slowly withdrawn while seed and crucible rotate in opposite directions; the melt freezes onto the seed with the seed's orientation.

### The equipment

- A **quartz (SiO₂) crucible** holding the molten silicon, inside a graphite holder.
- **Heaters** (RF induction or resistance) keeping the melt just above silicon's melting point, **1414 °C**.
- A **pull rod** holding the seed, which rotates and rises slowly.
- A chamber filled with **argon** gas, so the hot silicon does not react with air.
- Sensors and control electronics to keep the diameter constant.

### The steps

1. **Load.** Chunks of EG-Si and a carefully weighed amount of dopant (boron for p-type; phosphorus, arsenic or antimony for n-type) go into the crucible.
2. **Melt.** The chamber is filled with argon and the charge is melted at about 1420 °C.
3. **Dip.** The seed (cut to the wanted orientation, e.g. ⟨100⟩) is lowered until it just touches the melt.
4. **Neck (Dash technique).** The seed is pulled up quickly, growing a thin neck about 3 mm across. Dipping a cold seed into hot liquid creates crystal defects (dislocations); in a thin neck they run out of the sides and disappear, so the crystal below is dislocation-free.
5. **Shoulder and body.** The pull rate is reduced so the crystal widens to the full diameter (up to 300 mm). It is then pulled at about **1 mm per minute** while the seed and crucible rotate in **opposite directions** (10–30 rpm) to stir the melt and keep temperature and doping even.
6. **Tail.** At the end the pull rate is increased so the diameter narrows to a cone before the crystal leaves the melt. A sudden break would send defects back up the crystal.
7. **Cool** slowly. A typical ingot is 300 mm wide and up to 2 m long.

**Controlling the diameter:** pulling faster, or making the melt hotter, gives a thinner crystal; pulling slower or cooler gives a thicker one.

After growth the ingot is ground to an exact diameter, marked with a flat or notch to show its orientation, sliced into wafers with a wire saw, then lapped, etched and polished to a mirror finish.

### Dopant segregation: why the doping changes along the ingot

When silicon freezes, impurity atoms "prefer" to stay in the liquid. The **segregation coefficient** measures this:

    k₀ = C_s / C_l

C_s is the concentration in the solid and C_l in the liquid where they meet. For most dopants k₀ < 1: the crystal takes in less dopant than the melt contains.

| Impurity | B | P | As | Sb | Al | Ga | O | Fe |
|---|---|---|---|---|---|---|---|---|
| k₀ in Si | 0.8 | 0.35 | 0.3 | 0.023 | 0.002 | 0.008 | 0.25 | 8×10⁻⁶ |

**Consequence.** The dopant left behind builds up in the shrinking pool of melt. So the end of the ingot that grows last is more heavily doped than the start. If C₀ is the starting melt concentration and f the fraction already frozen,

    C_s = k₀ C₀ (1 − f)^{k₀ − 1}

#### Example 2.1: dopant segregation in a CZ crystal

**Question.** A boron-doped silicon crystal is to be grown by the Czochralski method with a boron concentration of 1×10¹⁶ cm⁻³ at the seed end. The segregation coefficient of boron in silicon is k₀ = 0.8. (a) What boron concentration must the melt contain at the start? (b) What is the boron concentration in the crystal when half of the melt has solidified?

**Given:** C_s(start) = 1×10¹⁶ cm⁻³, k₀ = 0.8, f = 0.5 for part (b).

**Find:** (a) C₀, the initial melt concentration; (b) C_s at f = 0.5.

**Solution.**

(a) At the start, C_s = k₀C₀, so

    C₀ = C_s/k₀ = 1×10¹⁶ / 0.8 = 1.25×10¹⁶ cm⁻³

(b) Use C_s = k₀C₀(1 − f)^{k₀ − 1} with f = 0.5:

    C_s = 0.8 × 1.25×10¹⁶ × (0.5)^{−0.2} = 1×10¹⁶ × 1.149 = 1.15×10¹⁶ cm⁻³

**Answer:** **(a) C₀ = 1.25×10¹⁶ cm⁻³; (b) C_s = 1.15×10¹⁶ cm⁻³**, about 15 % higher than at the seed end, because rejected boron builds up in the melt.

The same effect also **purifies**: iron (k₀ ≈ 10⁻⁵) is almost entirely rejected into the melt.

### Float-zone (FZ) growth, for comparison

A polysilicon rod is held vertically and a narrow molten zone, heated by an RF coil, is moved slowly along it, starting from a seed. **No crucible** touches the molten silicon, so there is almost no oxygen or carbon contamination, and very pure, high-resistivity silicon (up to 10⁴ Ω·cm) can be made. FZ is used for power devices and radiation detectors, but wafers are smaller (≤ 200 mm) and more expensive.

## Part C: Epitaxial growth

### What epitaxy is and why we need it

**Epitaxy** (Greek *epi*, "upon", and *taxis*, "arrangement") is the growth of a thin single-crystal layer on a single-crystal wafer (the **substrate**), so that the new layer continues the substrate's crystal structure and orientation.

Why not just make everything in the bulk crystal? Because devices need **thin layers with different properties stacked on each other**, with sharp boundaries:

- a lightly doped layer on a heavily doped substrate (bipolar transistors, power diodes);
- a layer of a different material, such as AlGaAs on GaAs or InGaAs on InP (lasers, LEDs, high-speed transistors);
- a layer cleaner than the CZ substrate (less oxygen, fewer defects).

**Homoepitaxy:** same material (Si on Si). **Heteroepitaxy:** different materials (GaAs on Si, AlGaAs on GaAs). In heteroepitaxy the two **lattice constants** must be nearly equal (Week 1); otherwise the mismatch creates defects.

@fig figures/epitaxy.svg | The three methods side by side: gas reacting on a hot surface (VPE), a cooling saturated melt (LPE), and atomic beams in ultra-high vacuum (MBE).

### Vapour-phase epitaxy (VPE), also called CVD epitaxy

**Principle.** Gases containing silicon flow over a heated wafer. At the hot surface they react or break down, leaving silicon atoms behind. The atoms move about on the surface until they find the right place in the crystal, so the layer grows as a continuation of the wafer.

For silicon, the common reactions are:

    SiCl₄ + 2H₂ → Si + 4HCl      (≈ 1150–1250 °C)
    SiH₂Cl₂ → Si + 2HCl          (≈ 1000–1100 °C)
    SiH₄ → Si + 2H₂              (≈ 600–1000 °C)

Doping is done by adding a little dopant gas: **B₂H₆** (diborane) for p-type, **PH₃** (phosphine) or **AsH₃** (arsine) for n-type.

The growth rate is limited by one of two steps: how fast gas can reach the surface (**mass-transport limited**, at high temperature) or how fast the reaction happens on the surface (**reaction-rate limited**, at lower temperature).

For compound semiconductors the metal-organic version, **MOCVD**, is used: (CH₃)₃Ga + AsH₃ → GaAs + 3CH₄ at about 600–750 °C. Nearly all commercial LEDs are made this way.

- Growth rate 0.1–5 μm/min; good uniformity; many wafers at once: the industrial workhorse.
- Problems: dopant from the substrate can evaporate and re-enter the layer (**autodoping**), and at high temperature dopant diffuses up from the substrate (**out-diffusion**), blurring the boundary.

### Liquid-phase epitaxy (LPE)

**Principle.** Dissolve the semiconductor in a molten metal until no more will dissolve (a **saturated solution**), like sugar in hot water. Bring the wafer into contact with it and cool slowly. As the liquid cools it can hold less, so the extra semiconductor comes out of solution and crystallises onto the wafer, continuing its crystal.

**Example:** GaAs dissolved in molten gallium, at about **700–900 °C**, cooled at 0.1–1 °C per minute. A **sliding graphite boat** with several wells of different melts moves the wafer from one melt to the next to build up layers.

- Growth happens close to equilibrium, so crystal quality is excellent and defects few; the equipment is simple and cheap.
- But thickness control is poor (about 0.1 μm at best), boundaries are not sharp, surfaces are rough, and the area is small.
- Used for LEDs and the first heterostructure lasers.

### Molecular-beam epitaxy (MBE)

**Principle.** In an **ultra-high vacuum** (about 10⁻¹⁰ Torr, roughly a ten-trillionth of atmospheric pressure), each element (Ga, As, Al, dopants) is heated in its own small oven (**effusion cell**). Atoms evaporate and travel in straight lines, as a beam, to the heated wafer, because there is no air to collide with. They land, move around, and join the crystal. Each oven has a **shutter** that can open or close in a fraction of a second, switching that element on or off.

**Example:** GaAs from Ga and As cells, wafer at about 550–650 °C.

- Growth is slow, about **1 μm per hour**, which is about **one atomic layer per second**. So layers can be controlled to **a single atomic layer**.
- Boundaries are atomically sharp. Ideal for quantum wells, superlattices, high-electron-mobility transistors (HEMTs) and advanced lasers.
- Growth can be watched while it happens by **RHEED** (electron diffraction), which counts the atomic layers.
- Very expensive equipment, slow, low throughput.

### Comparing the three at a glance

| | VPE (CVD) | LPE | MBE |
|---|---|---|---|
| Atoms arrive from | A gas, by chemical reaction | A liquid solution, by precipitation | A beam of atoms, in vacuum |
| Temperature | Highest (Si: 1000–1250 °C) | Medium (700–900 °C) | Lowest (500–650 °C) |
| Thickness control | Good (tens of nm) | Poor (~0.1 μm) | Excellent (one atomic layer) |
| Speed | Fast | Fast | Slow |
| Cost | Moderate | Low | Very high |
| Best for | Mass production (Si epi, LEDs by MOCVD) | Simple, thick, high-quality layers | Atomic-scale research and advanced devices |

## Key points of Week 2

- MG-Si (98 %) is made from quartz and carbon in an arc furnace: SiO₂ + 2C → Si + 2CO.
- It is purified by converting it to liquid SiHCl₃, distilling, then depositing EG-Si by the Siemens process: SiHCl₃ + H₂ → Si + 3HCl.
- CZ growth: a seed is pulled slowly from the melt, rotating; the crystal copies the seed. Dash necking removes dislocations.
- CZ gives large, cheap, dislocation-free crystals, but oxygen from the crucible and segregation (k₀ < 1) are its limitations.
- Epitaxy grows thin crystalline layers on a wafer: VPE from gas (production), LPE from a cooling melt (simple), MBE from atomic beams in vacuum (atomic precision).

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

---

## Practice questions

These extra questions practise this week's ideas. Work each one on paper before reading the solution; the calculation questions follow the same Question, Given, Find, Solution, Answer layout as the worked examples.

#### Practice 2.1: the purification route

**Question.** List the stages from quartzite to electronic-grade silicon, giving the chemical reaction and approximate temperature of each.

**Answer.**

| Stage | Reaction | Temperature |
|---|---|---|
| 1. Arc furnace → MG-Si (98 %) | SiO₂ + 2C → Si + 2CO | ≈ 2000 °C |
| 2. Hydrochlorination | Si + 3HCl → SiHCl₃ + H₂ | ≈ 300 °C |
| 3. Fractional distillation of SiHCl₃ | (physical separation by boiling point) | ≈ 32 °C boiling point |
| 4. Siemens CVD → EG-Si polysilicon | SiHCl₃ + H₂ → Si + 3HCl | ≈ 1100 °C |

#### Practice 2.2: phosphorus segregation along an ingot

**Question.** An n-type CZ crystal must have 5×10¹⁵ cm⁻³ phosphorus at the seed end. The segregation coefficient of P in Si is 0.35. Find the starting melt concentration and the phosphorus concentration in the crystal when 80 % of the melt has solidified.

**Given:** C_s(0) = 5×10¹⁵ cm⁻³, k₀ = 0.35, f = 0.8.

**Find:** C₀ and C_s at f = 0.8.

**Solution.**

    C₀ = C_s/k₀ = 5×10¹⁵/0.35 = 1.43×10¹⁶ cm⁻³
    C_s = k₀C₀(1 − f)^{k₀ − 1} = 5×10¹⁵ × (0.2)^{−0.65} = 5×10¹⁵ × 2.85 = 1.42×10¹⁶ cm⁻³

**Answer:** **C₀ = 1.43×10¹⁶ cm⁻³; at f = 0.8, C_s = 1.42×10¹⁶ cm⁻³**, almost three times the seed-end value. This is why P-doped CZ ingots vary so much in resistivity along their length.

#### Practice 2.3: how much silicon in an ingot?

**Question.** A CZ ingot is 300 mm in diameter and 1.5 m long. Find its mass (density 2.33 g/cm³) and how many wafers it gives if each wafer is 775 μm thick and the saw removes another 200 μm per cut.

**Given:** diameter 30 cm, length 150 cm, ρ = 2.33 g/cm³, 775 + 200 = 975 μm per wafer.

**Find:** mass and number of wafers.

**Solution.**

    Volume = π r² L = π × 15² × 150 = 1.06×10⁵ cm³
    Mass = 1.06×10⁵ × 2.33 = 2.47×10⁵ g = 247 kg
    Wafers = 150 cm / 0.0975 cm = 1538

**Answer:** **about 247 kg and roughly 1500 wafers** (fewer after the shoulder and tail are cut off).

#### Practice 2.4: MBE growth time

**Question.** A 0.5 μm GaAs layer is grown by MBE at 1 μm/h. How long does it take, and how many monolayers (each a/2 = 0.2825 nm thick) are deposited? What is the average monolayer rate?

**Given:** thickness 500 nm, rate 1 μm/h, monolayer 0.2825 nm.

**Find:** time, number of monolayers, rate.

**Solution.**

    t = 0.5 μm / (1 μm/h) = 0.5 h = 1800 s
    monolayers = 500 nm / 0.2825 nm = 1770
    rate = 1770/1800 ≈ 1 monolayer per second

**Answer:** **30 minutes, about 1770 monolayers, at about one atomic layer per second**, which is why MBE can control thickness to a single layer.

#### Practice 2.5: lattice mismatch

**Question.** Calculate the lattice mismatch for (a) Ge on Si (a = 5.65 and 5.43 Å) and (b) AlAs on GaAs (a = 5.661 and 5.653 Å). Which pair is suitable for defect-free heteroepitaxy?

**Given:** lattice constants above. f = (a_layer − a_sub)/a_sub.

**Find:** f for each pair.

**Solution.**

    (a) f = (5.65 − 5.43)/5.43 = 0.041 = 4.1 %
    (b) f = (5.661 − 5.653)/5.653 = 0.0014 = 0.14 %

**Answer:** **4.1 % and 0.14 %.** AlAs/GaAs is almost perfectly matched and grows defect-free, which is why AlGaAs/GaAs heterostructures are so widely used. Ge on Si quickly forms misfit dislocations unless the layer is very thin or graded.

#### Practice 2.6: CZ operating conditions

**Question.** Why is the CZ puller filled with argon, and why do the seed and crucible rotate in opposite directions?

**Answer.** Argon is inert: it stops the hot silicon reacting with oxygen and nitrogen, and the gas flow carries away SiO evaporating from the melt. Counter-rotation stirs the melt, so the temperature around the growing crystal is uniform (giving a round, constant-diameter crystal) and dopant is mixed evenly (giving uniform radial resistivity).

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Describe the conversion of quartzite into metallurgical-grade silicon. | Write the arc-furnace reaction and state the purity of MG-Si. | SiO₂ + 2C → Si + 2CO; about 98 % pure. | Part A, Step 1 |
| 2 | Explain how MG-Si is purified into electronic-grade silicon. | Why is silicon converted into SiHCl₃ before purification? | SiHCl₃ is a liquid (boils at 32 °C) that can be purified by fractional distillation; solids cannot. | Part A, Steps 2–4 |
| 3 | Explain the principle and steps of the Czochralski method. | What is the purpose of the Dash neck? | Growing a thin neck lets dislocations from the thermal shock run out of the crystal, so the ingot is dislocation-free. | Part B |
| 4 | State the advantages and limitations of CZ growth and compare it with float-zone growth. | Why does FZ silicon reach higher resistivity than CZ silicon? | No crucible touches the melt, so there is almost no oxygen or carbon contamination. | Part B; Float-zone |
| 5 | Use the segregation coefficient to predict doping along an ingot. | For phosphorus (k₀ = 0.35), is the tail end of a CZ ingot more or less heavily doped than the seed end? | More heavily doped: rejected phosphorus builds up in the melt. | Dopant segregation; Example 2.1 |
| 6 | Explain the principles of VPE, LPE and MBE and compare them. | Which epitaxy method gives single-atomic-layer thickness control, and why? | MBE: slow growth (≈ one monolayer per second) and shuttered atomic beams in ultra-high vacuum. | Part C |
