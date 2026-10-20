# Week 3 — Impurity Control and Doping
<!-- group: Module 1 · Material Physics & Semiconductor Growth -->

**Plan:** diffusion and ion implantation mechanisms; controlled doping profiles and evaluation of impurity distribution. This page follows your lecturer's handwritten notes on diffusion and ion implantation, including every calculation in them.

## The big picture

A pure silicon wafer is almost useless. To make a diode, a transistor or a chip, we must put **dopant atoms** (boron, phosphorus, arsenic) into chosen parts of the wafer, in chosen amounts, down to a chosen depth. There are two ways to do this:

1. **Diffusion:** heat the wafer in an atmosphere rich in dopant. The dopant atoms creep in by themselves, the way a drop of ink spreads through water.
2. **Ion implantation:** turn the dopant atoms into ions, accelerate them with a high voltage, and fire them into the wafer like tiny bullets.

The purpose of both is the same: to change the electrical properties of the material and form the **n-type and p-type regions** needed for diodes, transistors, MOSFETs and integrated circuits.

Common dopants for silicon:

| Dopant | Symbol | Makes silicon |
|---|---|---|
| Phosphorus | P | n-type |
| Arsenic | As | n-type |
| Antimony | Sb | n-type |
| Boron | B | p-type |
| Gallium | Ga | p-type |

---

## Part A: Diffusion

### What diffusion is

**Diffusion** is the movement of dopant atoms from a region of **high concentration** to a region of **low concentration**, driven by thermal energy.

In processing, the silicon wafer is heated to a high temperature (about 900–1200 °C) and exposed to a dopant source. Dopant atoms enter the silicon surface and gradually move into the crystal.

### Why atoms move "downhill"

Your notes illustrate this with gas molecules in a box. Suppose 21 of 32 oxygen molecules start on the left side of a box. Every molecule moves randomly, left or right with equal chance. Nothing pushes them in any particular direction. But because there are more molecules on the left, **more of them happen to cross from left to right than from right to left**. The result is a net flow towards the emptier side.

- **Concentration difference:** more particles on one side (21 of 32 on the left) creates a **concentration gradient**.
- **Net diffusion:** random motion carries particles both ways, but more move from the crowded side to the less crowded side.
- **Dynamic equilibrium:** eventually both sides have similar concentrations. Particles still move randomly in both directions, but the two flows now cancel, so there is no net change.

> **In plain words.** Diffusion is not a force. It is just statistics: if you have more atoms here than there, random jumping will, on average, carry atoms from here to there. The steeper the difference, the faster the flow.

The basic process is:

    Dopant source → silicon surface → dopant penetration → desired dopant profile

### Fick's first law: how fast atoms flow

    J = −D dC/dx

| Symbol | Meaning | Unit |
|---|---|---|
| J | **dopant flux**: number of dopant atoms crossing 1 cm² each second | atoms/cm²·s |
| D | **diffusion coefficient**: how easily the dopant moves in silicon | cm²/s |
| C | dopant concentration | atoms/cm³ |
| x | distance into the semiconductor | cm |
| dC/dx | the **concentration gradient**: how fast C changes with depth | atoms/cm⁴ |

**Reading the equation.** The flow is proportional to how steeply the concentration changes. No gradient, no flow. The **minus sign** says the flow goes from high concentration towards low concentration: if C falls as x increases (dC/dx negative), J is positive, meaning atoms flow in the +x direction, deeper into the wafer.

(The J here is a flow of atoms, not an electric current. Later weeks use J for current density.)

### The diffusion coefficient depends strongly on temperature

    D = D₀ e^{−E_a/kT}

| Symbol | Meaning |
|---|---|
| D₀ | diffusion constant (cm²/s), a property of the dopant–silicon pair |
| E_a | **activation energy** (eV): the energy barrier an atom must jump over to move one lattice site |
| k | Boltzmann constant, 8.617×10⁻⁵ eV/K |
| T | absolute temperature (K) |

Because T sits inside an exponential, **increasing temperature greatly increases the diffusion rate**. Typical E_a is 3–4 eV, so D rises about tenfold for every 50–100 °C. This is why diffusion only happens in a furnace: at room temperature D is so small that dopants do not move at all in a lifetime.

### How far do atoms travel? The diffusion length

The depth to which dopants spread grows with the **square root** of time:

    diffusion length ≈ √(Dt)

Your notes use the form **L = √(2Dt)**. Other books write 2√(Dt), which is what appears inside the erfc formula below. They are the same idea with a different constant in front. The key fact is that **depth ∝ √(Dt)**: diffusing four times as long only doubles the depth. In a calculation, use whichever form the question gives.

### Two types of diffusion

#### A. Constant-source diffusion (predeposition)

The surface of the semiconductor is kept at an approximately **constant dopant concentration C_s**, because the source (dopant gas or glass) is present all the time. The profile is:

    C(x, t) = C_s erfc( x / 2√(Dt) )

| Symbol | Meaning |
|---|---|
| C_s | surface concentration (atoms/cm³), fixed |
| x | depth |
| D | diffusion coefficient |
| t | diffusion time |
| erfc | the **complementary error function**, erfc(u) = 1 − erf(u). You read it from a table. |

**Characteristics:**

1. The dopant source remains available throughout the process.
2. The surface concentration stays approximately constant.
3. It produces an erfc concentration profile.
4. It is often used for the **initial doping step**.

**What erfc looks like.** erfc(0) = 1, so at the surface C = C_s. As the argument u = x/2√(Dt) grows, erfc falls: erfc(0.5) = 0.48, erfc(1) = 0.16, erfc(2) = 0.005, erfc(3) ≈ 2×10⁻⁵. So the concentration is highest at the surface and falls off steeply with depth. As time goes on, 2√(Dt) gets bigger, so the same depth corresponds to a smaller u, and the profile pushes deeper.

| u | erfc(u) | u | erfc(u) |
|---|---|---|---|
| 0 | 1.000 | 1.0 | 0.157 |
| 0.25 | 0.724 | 1.5 | 0.034 |
| 0.5 | 0.480 | 2.0 | 4.7×10⁻³ |
| 0.527 | 0.456 | 2.5 | 4.1×10⁻⁴ |
| 0.75 | 0.289 | 3.0 | 2.2×10⁻⁵ |

#### B. Limited-source diffusion (drive-in)

After a dopant has been introduced into the surface, the wafer is heated **without** supplying any more dopant. The fixed amount already there spreads deeper. The profile is approximately **Gaussian**:

    C(x, t) = ( Q / √(πDt) ) e^{−x²/4Dt}

| Symbol | Meaning |
|---|---|
| Q | total dopant dose per unit area (atoms/cm²), fixed |
| D | diffusion coefficient |
| t | time |

**Characteristics:**

1. The dopant penetrates deeper.
2. The **surface concentration decreases** (the same atoms are spread over a greater depth).
3. The total dopant quantity is approximately **conserved**.
4. It is used to obtain a desired **junction depth**.

The surface concentration is the value at x = 0, where e⁰ = 1:

    C(0, t) = Q / √(πDt)

@fig figures/diffusion.svg | Left: constant-source (erfc) profiles at three times; the surface value stays fixed while the profile deepens. Right: limited-source (Gaussian) profiles; the area under each curve (the dose) is the same, so the surface value falls as the profile spreads.

> **In plain words.** Constant source: keep pouring ink on the surface, and the colour soaks deeper while the surface stays dark. Limited source: put one drop on, stop, and wait; the colour spreads deeper but gets paler everywhere.

### Junction depth

If the wafer was already doped with the opposite type, at background concentration N_B (for example n-type 10¹⁶ cm⁻³ and we diffuse boron in), a **p-n junction** forms at the depth x_j where the diffused concentration has fallen to equal the background:

    C(x_j) = N_B

    erfc profile:     x_j = 2√(Dt) · erfc⁻¹(N_B/C_s)
    Gaussian profile: x_j = 2√(Dt) · √( ln(C_s/N_B) )

### Step-by-step diffusion process

1. **Wafer preparation.** A high-purity silicon wafer is cleaned to remove (a) dust, (b) organic contamination, (c) metallic impurities and (d) native surface oxide and contamination.
2. **Dopant source preparation.** A suitable dopant source is selected: boron for p-type, phosphorus or arsenic for n-type.
3. **Heating.** The wafer is placed in a diffusion furnace and heated to a high temperature.
4. **Dopant introduction.** The dopant is supplied to the surface of the silicon.
5. **Dopant penetration.** Thermal energy allows dopant atoms to move from the surface into the silicon lattice.
6. **Drive-in.** Additional heating may be used to drive the dopant deeper into the wafer.
7. **Cooling.** The wafer is cooled under controlled conditions.
8. **Characterisation.** The resulting dopant profile is measured to determine (1) junction depth, (2) sheet resistance, (3) dopant concentration and (4) electrical properties.

### Diffusion at the atomic level

Dopant atoms move through the silicon crystal mainly by two mechanisms:

**A. Vacancy mechanism.** A dopant atom sitting on a lattice site can only move when a neighbouring site is empty (a **vacancy**). It jumps into the vacancy:

    atom → vacancy → new lattice position

This is how the main dopants (B, P, As, Sb) move. It is slow, because it needs a vacancy to be next to the atom at the right moment.

**B. Interstitial mechanism.** A small atom moves through the **spaces between** the normal lattice positions without needing a vacancy. This is much faster. Metals such as gold, copper and iron move this way.

Some dopants use both: they move through interstitial sites, or by interactions involving both interstitials and vacancies. Which mechanism a dopant uses determines how quickly it diffuses.

### Advantages and disadvantages of diffusion

| Advantages | Disadvantages |
|---|---|
| Relatively simple process | Requires high temperature |
| Can process many wafers simultaneously | Dopants spread laterally (sideways) as well as vertically |
| Suitable for high-temperature processing | Less precise depth control |
| Good for introducing large dopant concentrations | Difficult to form extremely shallow junctions |
| Historically important in semiconductor fabrication | High-temperature exposure can affect previously fabricated structures |

---

## Diffusion calculations (from the lecture notes)

### Q1. Phosphorus is diffused into silicon with D = 2×10⁻¹³ cm²/s for t = 500 s. Find the approximate diffusion distance using L = √(2Dt).

    L = √(2 × 2×10⁻¹³ × 500) = √(2×10⁻¹⁰) = 1.414×10⁻⁵ cm

Convert to micrometres (1 cm = 10⁴ μm):

    L = 1.414×10⁻⁵ × 10⁴ = 0.141 μm

**L ≈ 0.141 μm.** Note how small this is: dopants move only a fraction of a micrometre in minutes.

### Q2. A dopant concentration gradient in silicon is 4×10¹⁸ cm⁻⁴ and D = 3×10⁻¹⁴ cm²/s. Find the diffusion flux using Fick's first law.

    J = −D dC/dx = −(3×10⁻¹⁴)(4×10¹⁸) = −1.2×10⁵ atoms/cm²·s

**|J| = 1.2×10⁵ atoms/cm²·s.** The minus sign means the dopant moves from the region of higher concentration towards lower concentration (against the direction in which C increases).

### Q4. Find D at T = 1273 K for a dopant with D₀ = 0.5 cm²/s and E_a = 3.5 eV.

    kT = 8.617×10⁻⁵ × 1273 = 0.1097 eV
    E_a/kT = 3.5/0.1097 = 31.90
    D = 0.5 × e^{−31.90} = 0.5 × 1.39×10⁻¹⁴ = 6.9×10⁻¹⁵ cm²/s

**D ≈ 6.9×10⁻¹⁵ cm²/s.** Try T = 1373 K (100 °C hotter): kT = 0.1183 eV, E_a/kT = 29.58, D = 7.1×10⁻¹⁴ cm²/s, ten times larger.

### Q5. Constant-source diffusion: C_s = 1×10²⁰ cm⁻³, D = 1×10⁻¹³ cm²/s, t = 3600 s. Find C at x = 0.2 μm.

Step 1, convert the depth: x = 0.2 μm = 2×10⁻⁵ cm.

Step 2, the diffusion length: √(Dt) = √(1×10⁻¹³ × 3600) = √(3.6×10⁻¹⁰) = 1.897×10⁻⁵ cm.

Step 3, the erfc argument:

    u = x / 2√(Dt) = 2×10⁻⁵ / (2 × 1.897×10⁻⁵) = 0.527

Step 4, from the table: erf(0.527) = 0.544, so erfc(0.527) = 1 − 0.544 = 0.456.

Step 5:

    C = C_s × erfc(u) = 1×10²⁰ × 0.456 = 4.56×10¹⁹ atoms/cm³

**C(0.2 μm) = 4.56×10¹⁹ cm⁻³**, a little under half the surface value.

### Q6. Drive-in: dose Q = 2×10¹⁵ atoms/cm², D = 5×10⁻¹⁴ cm²/s, t = 1000 s. Find the concentration at x = 0.

At x = 0, e^{−0} = 1, so

    C(0, t) = Q / √(πDt)
    Dt = 5×10⁻¹⁴ × 1000 = 5×10⁻¹¹ cm²
    πDt = 1.571×10⁻¹⁰,   √(πDt) = 1.253×10⁻⁵ cm
    C(0, t) = 2×10¹⁵ / 1.253×10⁻⁵ = 1.60×10²⁰ atoms/cm³

**Surface concentration = 1.60×10²⁰ cm⁻³.**

Why x = 0? x is the distance from the silicon surface: x = 0 is exactly at the surface; x = 0.1 μm is 0.1 μm below it; any x > 0 means below the surface. The question asks for the surface concentration, so we set x = 0 and the exponential becomes 1. (The dose is atoms per cm² because it is the total number of atoms under each square centimetre of surface.)

---

## Part B: Ion implantation

### What ion implantation is

**Ion implantation** is a doping technique in which dopant atoms are converted into **ions**, **accelerated** to high energy, and physically **injected** into the semiconductor wafer.

Unlike thermal diffusion, ion implantation allows the **dopant dose** and **implantation depth** to be controlled very precisely.

Basic flowchart:

    Dopant source → ioniser → mass analyser → accelerator → beam → wafer

**Main components:** ion source, mass analyser, acceleration system, beam focusing system, scanning system, the semiconductor wafer, and a vacuum chamber (the ions must not hit air molecules on the way).

### Step-by-step ion implantation

1. **Dopant ion generation.** A dopant-containing material (boron, phosphorus, arsenic) is introduced into an ion source, where its atoms are converted into positively charged ions.
2. **Ion extraction.** An electric field pulls the ions out of the source.
3. **Mass analysis.** The ion beam passes through a magnetic mass analyser. A magnet bends the path of each ion by an amount that depends on its **mass-to-charge ratio**, so only the wanted ion goes through the exit slit. This prevents unwanted species being implanted.
4. **Acceleration.** The selected ions are accelerated through a high electric potential. Their kinetic energy is **E = qV**, where E is the ion energy, q the ion charge and V the accelerating voltage. For a singly charged ion E = eV, so an ion accelerated through 100 kV has 100 keV.
5. **Beam focusing and scanning.** The ion beam is focused and scanned across the wafer so that the dopant is distributed uniformly.
6. **Implantation.** The energetic ions enter the silicon. As they travel through it, they collide with silicon nuclei and electrons and lose energy. Eventually they stop at a particular average depth.
7. **Annealing.** Implantation damages the crystal, because energetic ions knock silicon atoms out of place. The wafer is therefore heated (**thermal annealing**), which repairs crystal damage and moves the dopant atoms into proper lattice positions where they become electrically active.
8. **The implantation profile.** The implanted dopant normally produces an approximately **Gaussian** distribution.

### The implanted profile

    C(x) = ( Q / (√(2π) ΔR_p) ) exp[ −(x − R_p)² / (2ΔR_p²) ]

| Symbol | Meaning |
|---|---|
| Q | implanted dose (ions/cm²) |
| R_p | **projected range**: the average depth at which ions stop |
| ΔR_p | **straggle**: the spread of stopping depths about R_p (standard deviation) |
| x | depth |

The peak is at x = R_p, below the surface, and its height is

    N_p = Q / (√(2π) ΔR_p) ≈ 0.4 Q/ΔR_p

@fig figures/implant.svg | An implanted profile is a bell curve centred at R_p below the surface, with width set by ΔR_p. The junction forms where it falls to the background doping N_B.

> **In plain words.** Fire a million identical bullets into sand at the same speed. They do not all stop at exactly the same depth, but most stop near an average depth (R_p), with a spread (ΔR_p). That is the bell curve.

### Implantation parameters

- **Implantation dose** Q = number of implanted ions per unit area, usually expressed in **ions/cm²**.
- **Implantation energy**, usually expressed in **keV or MeV**. A higher implant energy generally produces a **deeper** implant.

The dose comes from the beam current I, the time t and the area A:

    Q = (I t)/(q A)       (singly charged ions)

### How ion implantation works inside silicon

    ion enters → collisions with atoms → loses energy → changes direction → eventually stops

There are two major energy-loss mechanisms:

**Nuclear stopping.** The implanted ion collides with silicon **nuclei**. This causes (i) deflection of the ion and (ii) displacement of silicon atoms, which is **lattice damage**. The nuclear stopping power is

    S_n = −(1/N_Si) (dE/dx)_nuclear

**Electronic stopping.** The ion interacts with the **electrons** in the silicon, losing energy through excitation and ionisation. At high energies electronic stopping is particularly important. It causes little damage.

    S_e = −(1/N_Si) (dE/dx)_electronic

Here N_Si is the number of silicon atoms per cm³ (5×10²² cm⁻³) and dE/dx the energy lost per unit distance. Heavy ions (As) lose energy mainly to nuclei and stop shallow; light ions (B) lose it mainly to electrons and go deeper.

### Channelling

**Channelling** occurs when ions enter the crystal along certain crystallographic directions and travel relatively deeply through open channels between rows of atoms. This produces an unexpectedly deep dopant distribution.

To reduce channelling, manufacturers may:

1. **tilt** the wafer relative to the ion beam (typically 7°);
2. **rotate** the wafer;
3. use suitable implantation conditions;
4. sometimes introduce a thin **amorphous layer** (a screen oxide, or a pre-amorphising implant) so the crystal channels are hidden.

### Example: forming an n-type region both ways

Suppose we want to convert part of a silicon wafer into an n-type region.

    Using diffusion:          silicon wafer → phosphorus source → high temperature → P atoms diffuse into Si → n-type region
    Using ion implantation:   phosphorus source → P⁺ ions → mass analysis → acceleration → implantation into Si → annealing → n-type region

### Diffusion versus ion implantation

| Feature | Diffusion | Ion implantation |
|---|---|---|
| Dopant introduction | Thermal movement | Accelerated ions |
| Main driving force | Concentration gradient | Ion kinetic energy |
| Temperature | High | Relatively low (implant near room temperature) |
| Depth control | Less precise | Highly precise |
| Dose control | Moderate | Excellent |
| Crystal damage | Low | Significant |
| Annealing | Sometimes required | Normally required |
| Profile | erfc or Gaussian, maximum at the surface | Approximately Gaussian, peak below the surface |
| Modern IC use | Less dominant for shallow junctions | Widely used |
| Equipment | Diffusion furnace | Ion implanter |

---

## Ion implantation calculations (from the lecture notes)

### P1. A silicon wafer is implanted with boron, Q = 1.0×10¹³ cm⁻², R_p = 0.5 μm, ΔR_p = 0.05 μm. (a) Find the peak concentration N_p. (b) Find the boron concentration at the surface (x = 0).

(a) Convert ΔR_p = 0.05 μm = 5.0×10⁻⁶ cm.

    N_p = Q / (√(2π) ΔR_p) = 1.0×10¹³ / (2.5066 × 5.0×10⁻⁶) = 1.0×10¹³ / 1.253×10⁻⁵
        = 7.98×10¹⁷ cm⁻³

(b) At x = 0:

    N(0) = N_p exp( −R_p²/2ΔR_p² ),   R_p/ΔR_p = 0.5/0.05 = 10
    N(0) = N_p exp(−10²/2) = N_p e^{−50} = 7.98×10¹⁷ × 1.93×10⁻²² = 1.54×10⁻⁴ cm⁻³

Effectively **zero boron at the surface**: the whole dose is buried around 0.5 μm.

### P2. An n-type substrate with C_B = 1.0×10¹⁵ cm⁻³ is implanted with boron to form a p-type region. Peak N_p = 1.0×10¹⁷ cm⁻³ at R_p = 0.4 μm, ΔR_p = 0.05 μm. Find the junction depth x_j (where the boron concentration equals C_B).

At the junction N(x_j) = C_B:

    C_B = N_p exp( −(x_j − R_p)²/2ΔR_p² )
    ln(N_p/C_B) = (x_j − R_p)²/2ΔR_p²
    x_j = R_p + ΔR_p √( 2 ln(N_p/C_B) )

Numbers: N_p/C_B = 10¹⁷/10¹⁵ = 100; ln(100) = 4.605; × 2 = 9.21; √9.21 = 3.035.

    x_j = 0.4 μm + 0.05 μm × 3.035 = 0.4 + 0.152 = 0.552 μm

The p-n junction is formed **0.552 μm below the silicon surface**. (There is also a second junction on the shallow side, at R_p − 0.152 = 0.248 μm, because the buried p-region has n-type silicon above it as well as below it.)

### P3. A 300 mm diameter wafer needs a boron dose Q = 2.0×10¹⁴ ions/cm². (a) Find the total number of ions. (b) If the implanter uses singly charged ions (q = 1.6×10⁻¹⁹ C) and processes the wafer in 60 s, what beam current is needed?

(a) Radius r = 300/2 = 150 mm = 15 cm. Area A = πr² = 3.142 × 225 = 706.9 cm².

    N_total = Q × A = 2.0×10¹⁴ × 706.9 = 1.414×10¹⁷ ions

(b) Total charge delivered = N_total × q = 1.414×10¹⁷ × 1.6×10⁻¹⁹ = 0.0226 C.

    I = Q_charge / t = 0.0226 / 60 = 3.77×10⁻⁴ A = 0.377 mA

The implanter needs a beam current of **0.377 mA** to deliver the target dose in one minute.

### P4. A photoresist mask must protect part of a wafer during a boron implant. In photoresist R_p = 0.8 μm and ΔR_p = 0.08 μm. The substrate under the mask must receive no more than 0.1 % of the peak concentration. Find the minimum mask thickness x_mask.

At the bottom of the mask the concentration must be 10⁻³ of the peak:

    N(x_mask)/N_p = exp( −(x_mask − R_p)²/2ΔR_p² ) = 10⁻³

Take logarithms. ln(10⁻³) = −3 ln 10 = −6.908. The minus signs cancel:

    (x_mask − R_p)²/2ΔR_p² = 6.908
    x_mask − R_p = ΔR_p √(2 × 6.908) = ΔR_p √13.816 = 3.717 ΔR_p
    x_mask = 0.8 + 0.08 × 3.717 = 0.8 + 0.297 = 1.097 μm

To keep transmission below 0.1 % the photoresist must be **at least 1.10 μm thick**. In real manufacturing engineers add a safety margin and use about 1.3–1.4 μm.

---

## Part C: Evaluating the impurity distribution

After doping, the engineer must check that the dose, the profile and the junction depth are what was intended (step 8 of the diffusion process). The main methods:

| Method | What it measures | How it works |
|---|---|---|
| Four-point probe | Sheet resistance R_s (Ω/□) | Pass current through the outer two of four probes in a line; measure voltage across the inner two |
| Groove-and-stain | Junction depth x_j | Grind a shallow groove, stain it (p and n regions take different colours), measure under a microscope |
| Spreading resistance profiling | Carrier concentration against depth | Step two probes down a shallow bevel, measuring resistance at each point |
| C-V profiling | Doping against depth | Capacitance of a junction against reverse bias (Week 12) |
| SIMS | All dopant atoms against depth | Sputter the surface with an ion beam and count ejected dopant ions in a mass spectrometer |
| Hall measurement | Carrier type, concentration, mobility | Hall voltage in a magnetic field (Week 7) |

### Sheet resistance, explained

A diffused layer is a thin conducting skin of thickness x_j. Its resistance is described by the **sheet resistance**:

    R_s = ρ / x_j     [ohms per square, Ω/□]

"Per square" means: any square piece of the layer, whatever its size, has resistance R_s between two opposite edges. (A bigger square is longer, which raises R, but also wider by the same factor, which lowers R; the two cancel.) So a resistor L long and W wide made from the layer has

    R = R_s × (L/W) = R_s × (number of squares)

Measured with a four-point probe on a large thin sample:

    R_s = 4.532 × (V/I)

**Example.** A boron layer gives V = 2.0 mV at I = 1.0 mA. R_s = 4.532 × 2.0 = 9.06 Ω/□. If x_j = 1.0 μm, the average resistivity is ρ = R_s x_j = 9.06 × 10⁻⁴ ≈ 9×10⁻⁴ Ω·cm, which corresponds to an average boron concentration of a few times 10¹⁹ cm⁻³.

### Junction depth by groove and stain

A cylindrical groove of radius R is ground into the surface and stained. If the stained chord is a wide at the surface and b wide at the junction:

    x_j ≈ (a² − b²) / (8R)

---

## Key points of Week 3

- Doping puts controlled amounts of B (p-type) or P, As, Sb (n-type) into chosen regions.
- Diffusion: random thermal motion carries dopant from high to low concentration. Fick: J = −D dC/dx.
- D = D₀e^{−E_a/kT}: hotter means much faster. Depth grows as √(Dt).
- Constant source → erfc profile, fixed surface concentration. Limited source → Gaussian, fixed dose, surface concentration falls.
- Ion implantation: ions accelerated to E = qV, Gaussian profile peaked at R_p with spread ΔR_p, dose Q = It/qA, annealing required, channelling avoided by tilting.
- Junction depth is where the dopant concentration equals the background doping.
- Profiles are checked by sheet resistance, junction depth, SIMS, spreading resistance and C-V.

---

## Examination questions solved (Q14–Q21)

### Q14. What is semiconductor doping? Explain why doping is necessary in semiconductor device fabrication.

**Doping** is the intentional introduction of controlled, small quantities of specific impurity atoms into a pure (intrinsic) semiconductor to change its electrical properties. Group V donors (P, As, Sb) make silicon **n-type**; Group III acceptors (B, Al, Ga) make it **p-type**. Typical levels are 10¹⁴ to 10²⁰ cm⁻³.

**Why it is necessary:**

1. **Intrinsic conductivity is too low and uncontrolled.** Pure Si has only n_i ≈ 10¹⁰ cm⁻³ carriers, giving ρ = 1/(qn_i(μ_n + μ_p)) ≈ 3×10⁵ Ω·cm. Doping with 10¹⁶ cm⁻³ P raises n a million times, to ρ ≈ 0.5 Ω·cm.
2. **It sets the carrier type.** Devices depend on regions where electrons or holes dominate. Without n- and p-type regions there can be no p-n junction, no diode, no BJT and no MOSFET.
3. **Temperature stability.** In an extrinsic semiconductor the carrier density is fixed by N_D or N_A over a wide temperature range (the extrinsic region) instead of varying exponentially with T as n_i does.
4. **Device design.** Doping profiles set the built-in potential, depletion width, breakdown voltage, threshold voltage of MOSFETs, current gain of BJTs, sheet resistance of resistors and the quality of Ohmic contacts (heavily doped n⁺, p⁺ regions).
5. **Selective, local control.** Using masks, different areas of one chip can be given different doping, which is what makes integrated circuits possible.

### Q15. Differentiate between n-type and p-type semiconductors.

| Feature | n-type | p-type |
|---|---|---|
| Dopant added | Pentavalent (Group V): P, As, Sb | Trivalent (Group III): B, Al, Ga, In |
| Name of dopant | Donor | Acceptor |
| Effect of dopant | Donates a free electron to the conduction band | Accepts an electron, creating a hole in the valence band |
| Fixed ion left behind | Positive donor ion N_D⁺ | Negative acceptor ion N_A⁻ |
| Majority carriers | Electrons | Holes |
| Minority carriers | Holes | Electrons |
| Carrier densities | n ≈ N_D, p = n_i²/N_D | p ≈ N_A, n = n_i²/N_A |
| Impurity level | E_D just below E_c | E_A just above E_v |
| Fermi level | Above E_i, towards E_c | Below E_i, towards E_v |
| Conductivity | σ ≈ qN_Dμ_n | σ ≈ qN_Aμ_p |
| Hall coefficient | Negative | Positive |

Both remain electrically neutral overall: every free electron (or hole) is balanced by a fixed ion.

### Q16. Explain the difference between donor impurities and acceptor impurities, giving suitable examples.

**Donor impurities** have **one more** valence electron than the host atom they replace. In Si, Group V atoms such as **phosphorus, arsenic and antimony** have five valence electrons; four form covalent bonds with neighbouring Si atoms, and the fifth is bound only by about 0.04–0.05 eV. It is easily thermally released into the conduction band, leaving a positively charged, immobile donor ion. Donors introduce an energy level E_D just below the conduction band and make the material n-type.

**Acceptor impurities** have **one fewer** valence electron than the host. In Si, Group III atoms such as **boron, aluminium, gallium and indium** have three valence electrons and leave one bond incomplete. A nearby valence electron moves in with very little energy (≈ 0.045 eV for B), so the acceptor becomes a negative ion and a mobile hole is created in the valence band. Acceptors introduce a level E_A just above the valence band and make the material p-type.

| | Donor | Acceptor |
|---|---|---|
| Valence electrons (in Si) | 5 | 3 |
| Gives / takes | Gives an electron | Takes an electron (gives a hole) |
| Ionised charge | + | − |
| Level | Near E_c | Near E_v |
| Examples in Si | P, As, Sb | B, Al, Ga, In |
| Examples in GaAs | S, Se, Te (on As site); Si on Ga site | Zn, Be, Mg (on Ga site); C on As site |

### Q17. Describe the mechanism of dopant diffusion in a semiconductor.

Diffusion is the net movement of dopant atoms from a region of high concentration to one of low concentration, driven by random thermal jumps of the atoms in the lattice. At room temperature it is negligible; at 900–1200 °C (silicon) it is significant.

**Atomic mechanisms:**

1. **Vacancy (substitutional) diffusion.** Substitutional dopants (B, P, As, Sb) occupy lattice sites. A dopant can jump only when an adjacent lattice site is vacant. The rate depends on the vacancy concentration (which rises steeply with temperature) and the jump probability. High activation energy (≈ 3–4 eV), so D is small (10⁻¹⁵ to 10⁻¹² cm²/s).
2. **Interstitial diffusion.** Small atoms or those that do not bond into the lattice (Au, Cu, Fe, Na, Li, H) move between lattice sites through the open spaces of the diamond structure. Low activation energy (0.5–1.5 eV), so they diffuse many orders of magnitude faster. These are usually unwanted contaminants.
3. **Interstitialcy (kick-out) and dissociative mechanisms.** A dopant is pushed off its site by a silicon self-interstitial, travels interstitially, then returns to a substitutional site. This explains enhanced diffusion of B and P during oxidation (oxidation-enhanced diffusion).

**Temperature dependence.** D = D₀ exp(−E_a/kT), so D roughly doubles every 20–30 °C.

**Macroscopic description.** The flux obeys Fick's first law F = −D ∂C/∂x, and the profile evolves by Fick's second law ∂C/∂t = D ∂²C/∂x². In practice a two-step process is used: predeposition from a constant surface source (erfc profile) followed by drive-in of the fixed dose (Gaussian profile). Diffusion is masked by SiO₂ windows, and the dopant spreads sideways under the mask edge by about 0.8 of its depth (lateral diffusion).

### Q18. State and explain Fick's first and second laws of diffusion.

**Fick's first law.** The diffusion flux is proportional to the negative of the concentration gradient:

    F = −D ∂C/∂x

- F: number of atoms crossing unit area per unit time (cm⁻²s⁻¹).
- C(x, t): impurity concentration (cm⁻³).
- D: diffusion coefficient (cm²/s), D = D₀exp(−E_a/kT).
- The minus sign: atoms move from high to low concentration. If there is no gradient, there is no net flux.

It describes the flux at one instant but not how the profile changes.

**Fick's second law.** Consider a thin slice of thickness dx. Atoms entering minus atoms leaving equals the increase stored (continuity, no generation or loss):

    ∂C/∂t = −∂F/∂x

Substituting the first law (with D constant):

    ∂C/∂t = D ∂²C/∂x²

This is the diffusion equation. It says the concentration rises where the profile is curved upward (concave) and falls where it is curved downward, so diffusion always smooths the profile. Its solutions, set by the boundary conditions, are the complementary-error-function profile (constant surface source) and the Gaussian profile (fixed dose) described in Part A above.

### Q19. A semiconductor is doped by diffusion with a constant surface concentration of 1 × 10²⁰ cm⁻³. Explain how the impurity concentration varies with depth.

A constant surface concentration is the **predeposition** (unlimited source) case. Solve Fick's second law with:

- C(0, t) = C_s = 1×10²⁰ cm⁻³ (held fixed for all t)
- C(∞, t) = 0 (deep in the wafer)
- C(x, 0) = 0 (no dopant at the start)

The solution is the **complementary error function**:

    C(x, t) = C_s erfc( x / 2√(Dt) ) = 1×10²⁰ · erfc( x / 2√(Dt) )   cm⁻³

**How it varies with depth:**

1. At the surface (x = 0), erfc(0) = 1, so C = 1×10²⁰ cm⁻³, independent of time.
2. The concentration **decreases monotonically** with depth. Near the surface it falls almost linearly; deeper it falls faster than exponentially, because erfc(u) ≈ e^{−u²}/(u√π) for large u.
3. The depth scale is the diffusion length 2√(Dt). At x = 2√(Dt), erfc(1) = 0.157, so C = 1.57×10¹⁹ cm⁻³. At x = 4√(Dt), erfc(2) = 4.7×10⁻³, so C = 4.7×10¹⁷ cm⁻³.
4. As time increases, the profile penetrates deeper (as √t) while the surface stays at 10²⁰ cm⁻³, so the total dose grows: Q = (2/√π)C_s√(Dt).
5. If the wafer has background doping N_B of the opposite type, a junction forms where C(x_j) = N_B.

**Worked illustration** (assume boron into n-Si with N_B = 1×10¹⁶ cm⁻³, D = 1×10⁻¹³ cm²/s at about 1100 °C, t = 1 h = 3600 s):

    √(Dt) = √(1×10⁻¹³ × 3600) = 1.90×10⁻⁵ cm = 0.190 μm
    2√(Dt) = 0.379 μm

    Junction: erfc(u) = N_B/C_s = 10¹⁶/10²⁰ = 10⁻⁴  ⇒  u ≈ 2.75
    x_j = 2.75 × 0.379 μm ≈ 1.04 μm

    Dose: Q = (2/√π)(1×10²⁰)(1.90×10⁻⁵) = 2.14×10¹⁵ atoms/cm²

| Depth x (μm) | u = x/2√(Dt) | erfc(u) | C (cm⁻³) |
|---|---|---|---|
| 0 | 0 | 1 | 1.0×10²⁰ |
| 0.19 | 0.5 | 0.480 | 4.8×10¹⁹ |
| 0.38 | 1.0 | 0.157 | 1.6×10¹⁹ |
| 0.57 | 1.5 | 0.034 | 3.4×10¹⁸ |
| 0.76 | 2.0 | 4.7×10⁻³ | 4.7×10¹⁷ |
| 1.04 | 2.75 | 1.0×10⁻⁴ | 1.0×10¹⁶ (junction) |

So the impurity concentration is highest at the surface and falls off as an erfc curve, reaching the background doping about 1 μm below the surface for these conditions.

### Q20. Explain the principle of ion implantation and identify its major advantages over thermal diffusion.

**Principle.** Ion implantation introduces dopant atoms into a semiconductor by bombarding it with a beam of energetic dopant ions. The dopant is ionised in an ion source, the ions are extracted, selected by mass in a magnetic analyser, accelerated to an energy of a few keV to MeV and scanned uniformly across the wafer. Each ion penetrates the crystal, losing energy by nuclear and electronic collisions, and stops at a depth that depends on its energy and mass. The resulting distribution is approximately Gaussian, peaking at the projected range R_p with straggle ΔR_p. The dose is measured exactly by integrating the beam current in a Faraday cup (Φ = It/qA). Because the impact damages the lattice and leaves dopants on non-lattice sites, the wafer is then annealed (furnace or RTA) to repair the damage and electrically activate the dopants.

**Advantages over thermal diffusion:**

1. **Precise, reproducible dose control** (±1 % or better) over a very wide range, 10¹¹ to 10¹⁶ cm⁻², by measuring charge. Diffusion dose depends on solid solubility, time and temperature and is much less accurate.
2. **Independent control of depth and dose.** Depth is set by energy, dose by charge. In diffusion both depend on the same Dt product.
3. **Low-temperature process.** Implantation is done near room temperature; only a short anneal is needed. Existing profiles are not disturbed and the thermal budget is small, which is vital for shallow junctions.
4. **Wide choice of masks**, including photoresist, which diffusion cannot use.
5. **Buried and retrograde profiles.** The peak can be placed below the surface (e.g. retrograde wells, buried layers); diffusion always peaks at the surface.
6. **Very shallow junctions** with low-energy implants.
7. **Less lateral spread** under the mask edge, allowing smaller devices and self-aligned structures.
8. **Purity.** Mass separation guarantees only the chosen species is implanted.
9. **Not limited by solid solubility**: concentrations above solubility can be obtained (though not all are activated).
10. **Uniformity** across large wafers, and the process is clean (vacuum, dry).

### Q21. Compare diffusion and ion implantation as semiconductor doping techniques.

| Feature | Thermal diffusion | Ion implantation |
|---|---|---|
| Principle | Dopant moves in from a surface source by random thermal jumps (Fick's laws) | Energetic ions are driven into the crystal and stop by collisions |
| Process temperature | High, 900–1200 °C | Room temperature, plus anneal (RTA ≈ 1000 °C for seconds) |
| Profile shape | erfc or Gaussian, always maximum at the surface | Gaussian peaking at R_p below the surface; buried and retrograde profiles possible |
| Dose control | Limited (± 5–10 %), set by solubility, T and t | Excellent (± 1 %), set by measured charge |
| Depth control | Coupled to dose through Dt | Independent: set by energy |
| Junction depth | Relatively deep; hard to make very shallow junctions | Very shallow junctions possible |
| Lateral spread | Large (≈ 0.8 × depth) | Small (≈ straggle) |
| Masking | SiO₂, Si₃N₄ (must survive high T) | Photoresist, oxide, nitride, polysilicon |
| Lattice damage | None | Significant; needs annealing; amorphisation at high dose |
| Channelling | Not applicable | Must be avoided (7° tilt, screen oxide) |
| Throughput and cost | Batch of 100+ wafers, cheap equipment | Single wafer or small batch, expensive equipment |
| Purity | Depends on source and furnace cleanliness | Mass-analysed, very pure |
| Concentration limit | Limited by solid solubility | Can exceed solubility |
| Typical use today | Drive-in, deep wells, solar cells, emitter diffusion in older processes | Source/drain, threshold-adjust, wells, LDD, channel stops in all modern CMOS |

**Summary:** diffusion is simple, cheap and damage-free but gives coarse, coupled control of dose and depth and needs high temperature. Ion implantation gives precise, independent, low-temperature control of dose and depth and is the standard technique for modern VLSI, at the cost of expensive equipment and lattice damage that must be annealed. In practice the two are often combined: implant to set the dose, then a thermal drive-in to set the depth.
