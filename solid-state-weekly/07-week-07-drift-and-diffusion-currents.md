# Week 7 — Drift and Diffusion Currents
<!-- group: Module 3 · Carrier Transport & Injection Phenomena -->

**Plan:** carrier mobility, scattering mechanisms and conductivity; diffusion of carriers, Fick's law and the Einstein relation.

## Learning objectives

By the end of this week you should be able to:

1. Explain thermal motion, drift velocity and mobility.
2. Explain the scattering mechanisms and the factors that affect mobility.
3. Derive and use the drift current density and conductivity.
4. Explain carrier diffusion and calculate diffusion current with Fick's law.
5. State, explain and use the Einstein relation.

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
| m₀ | Free-electron mass | 9.11×10⁻³¹ kg |
| eV | Electron-volt, a unit of energy | 1 eV = 1.6×10⁻¹⁹ J |
| μm | Micrometre (micron) | 1 μm = 10⁻⁴ cm = 10⁻⁶ m |

**Symbols**

| Symbol | Meaning | Units / typical value |
|---|---|---|
| E_c (E_C) | Energy of the bottom of the conduction band | eV |
| E_g | Band-gap energy, E_c − E_v | eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K |
| E_F | Fermi level: the energy at which a state has a 50 % chance of being occupied | eV |
| E_i | Intrinsic Fermi level, close to mid-gap | eV |
| N_c | Effective density of states in the conduction band | cm⁻³; Si 2.8×10¹⁹ at 300 K |
| n | Electron concentration (free electrons per cm³) | cm⁻³ |
| p | Hole concentration (holes per cm³) | cm⁻³ |
| n_i | Intrinsic carrier concentration (n = p = n_i in pure material) | cm⁻³; Si ≈ 1×10¹⁰ at 300 K |
| N_D | Donor concentration | cm⁻³ |
| N_A | Acceptor concentration | cm⁻³ |
| Δn, Δp | Excess electron and hole concentrations above equilibrium | cm⁻³ |
| m∗, m_n∗, m_p∗ | Effective mass of electrons or holes | kg, or as a multiple of m₀ |
| C(x, t) | Dopant concentration at depth x and time t | cm⁻³ |
| D | Diffusion coefficient (dopants in a furnace, or carriers) | cm²/s |
| F | Particle flux in Fick's law | particles/(cm²·s) |
| R_s | Sheet resistance (or diode series resistance in Week 12) | Ω/□ (ohms per square); Ω |
| E (field) | Electric field (on band diagrams, E is energy instead) | V/cm |
| μ, μ_n, μ_p | Mobility: drift velocity per unit field (electrons, holes) | cm²/(V·s); Si μ_n 1350, μ_p 480 |
| μ_L, μ_I | Mobility limited by lattice scattering, by ionised-impurity scattering | cm²/(V·s) |
| v_d | Drift velocity | cm/s |
| v_th | Thermal velocity of carriers | ≈ 10⁷ cm/s at 300 K |
| v_sat | Saturation velocity at high field | ≈ 10⁷ cm/s in Si |
| τ_m | Mean free time between collisions | s; about 0.1–1 ps |
| σ | Conductivity, q(nμ_n + pμ_p) (in Week 8, σ is also a capture cross-section) | S/cm (siemens per cm) |
| ρ | Resistivity, 1/σ | Ω·cm |
| J, J_n, J_p | Current density (total, electrons, holes) | A/cm² |
| D_n, D_p | Diffusion coefficients of electrons and holes | cm²/s; Si 35 and 12.4 |
| R_H, V_H, B | Hall coefficient, Hall voltage, magnetic flux density | cm³/C; V; T (Wb/m²) |
| R | Recombination rate | cm⁻³s⁻¹ |
| τ, τ_n, τ_p | Minority-carrier lifetime (τ_eff: effective, including surfaces) | s; Si 1 ns – 1 ms |
| L, L_n, L_p | Diffusion length √(Dτ): distance a minority carrier travels before recombining | μm or cm |
| I | Current | A |
| A (area) | Device or contact area | cm² |
| σ_i, ρ_i | Conductivity and resistivity of intrinsic (undoped) material; σ_doped after doping | S/cm; Ω·cm |
| F_n, F_p | Particle flux of electrons and holes (carriers crossing 1 cm² per second) | cm⁻²s⁻¹ |
| B_z, I_x, V_H | Hall effect: magnetic field (z), current (x) and Hall voltage | T (tesla); A; V |
| R_H | Hall coefficient, 1/qp (p-type) or −1/qn (n-type) | cm³/C |
| v_dn, v_dp | Drift velocity of electrons and holes | cm/s |
| μ_i, τ_i (μ_L, μ_I, N_I) | Mobility and scattering time for one scattering mechanism (L: lattice, I: ionised impurity); N_I = ionised-impurity density | cm²/(V·s); s; cm⁻³ |
| J_drift, J_diff | Drift and diffusion parts of the current density | A/cm² |

**Abbreviations**

| Abbreviation | Meaning |
|---|---|
| Si | Silicon |
| Ge | Germanium |
| GaAs | Gallium arsenide |
| SiO₂ | Silicon dioxide (silica), the oxide insulator |
| MOSFET | Metal–oxide–semiconductor field-effect transistor |
| BJT | Bipolar junction transistor |


## Key terms

Every important word used this week is defined here, so you can read this week on its own.

**Band gap (E_g).** The range of energies that an electron in a crystal cannot have. It lies between the valence band (the band of energies occupied by the electrons that form the bonds between atoms) and the conduction band (the next band up, where electrons are free to move through the crystal). For silicon E_g = 1.12 eV at 300 K.

**Electron and hole (carriers).** A free electron is an electron in the conduction band; a hole is an empty place left in the valence band, which behaves like a positive charge +q that can move. Together they are called carriers because they carry the current.

*Why it matters:* every current this week is a flow of electrons, of holes, or of both.

**Doping (N_D, N_A).** Adding small, controlled amounts of impurity atoms to a semiconductor. Donor atoms (concentration N_D, e.g. phosphorus in Si) give free electrons and make the material n-type; acceptor atoms (concentration N_A, e.g. boron) give holes and make it p-type.

**Majority and minority carriers.** The majority carriers are the more numerous type (electrons in n-type, holes in p-type); the minority carriers are the less numerous type.

**Fermi level (E_F).** The energy at which an electron state has a 50 % chance of being occupied. In thermal equilibrium (no battery, no light) it is the same everywhere in the material: it is "flat".

**Thermal velocity (v_th).** The average speed of the random motion that carriers have because of heat, about 10⁷ cm/s in silicon at 300 K. Because the directions are random, it gives no current on its own.

**Scattering and mean free time (τ_m).** Scattering is a collision of a carrier with a vibrating atom, an impurity ion or a defect, which randomises its direction. The mean free time τ_m is the average time between collisions, about 0.1–1 ps.

**Effective mass (m∗).** The mass a carrier appears to have when it is pushed by a force inside the crystal. It is usually written as a multiple of the free-electron mass m₀ (e.g. 0.067m₀ for GaAs electrons). A small effective mass means the carrier is easy to accelerate.

**Drift and drift velocity (v_d).** Drift is the movement of carriers caused by an electric field. The drift velocity v_d is the small, steady average velocity in the field direction that is added on top of the random thermal motion.

**Mobility (μ).** The drift velocity a carrier gains per unit electric field: it measures how easily the carrier moves through the crystal.

    μ = v_d / E = qτ_m / m∗

Where:

- μ = mobility (cm²/V·s); Si: μ_n = 1350, μ_p = 480
- v_d = drift velocity (cm/s)
- E = electric field (V/cm)
- q = electronic charge, 1.6×10⁻¹⁹ C
- τ_m = mean free time between collisions (s)
- m∗ = effective mass (kg)

*Why it matters:* mobility sets both the conductivity of a material and the speed of the devices made from it.

**Current density (J).** The electric current flowing through each square centimetre of cross-section, in A/cm². The current is I = JA, where A is the cross-sectional area.

**Conductivity and resistivity (σ, ρ).** Conductivity σ measures how well a material conducts; resistivity ρ = 1/σ measures how strongly it opposes current. Both depend on how many carriers there are and on their mobilities.

    σ = q(nμ_n + pμ_p),     ρ = 1/σ

Where:

- σ = conductivity (S/cm)
- ρ = resistivity (Ω·cm)
- q = electronic charge, 1.6×10⁻¹⁹ C
- n, p = electron and hole concentrations (cm⁻³)
- μ_n, μ_p = electron and hole mobilities (cm²/V·s)

**Diffusion (Fick's law).** The net flow of particles from where there are more of them to where there are fewer, caused only by their random motion. Fick's law says the flow is proportional to the concentration gradient.

    F = −D dC/dx

Where:

- F = particle flux: particles crossing 1 cm² per second (cm⁻²s⁻¹)
- D = diffusion coefficient (cm²/s)
- C = concentration of the particles (cm⁻³); for carriers, C is n or p
- x = position (cm)

*Why it matters:* diffusion carries the current in the neutral regions of a diode and across the base of a bipolar transistor.

**Diffusion coefficient (D).** The constant in Fick's law that measures how quickly particles spread out by random motion, in cm²/s. For carriers in Si at 300 K, D_n ≈ 35 cm²/s and D_p ≈ 12.4 cm²/s.

**Thermal voltage (kT/q).** The thermal energy kT expressed as a voltage: 0.0259 V (about 26 mV) at 300 K. It sets the voltage scale of almost every semiconductor equation.

**Einstein relation.** The rule that the diffusion coefficient and the mobility of a carrier are always in the same ratio, fixed only by temperature, because both are limited by the same collisions.

    D_n / μ_n = D_p / μ_p = kT/q

Where:

- D_n, D_p = electron and hole diffusion coefficients (cm²/s)
- μ_n, μ_p = electron and hole mobilities (cm²/V·s)
- kT/q = thermal voltage, 0.0259 V at 300 K

*Why it matters:* measuring the mobility (which is easy) immediately gives the diffusion coefficient.

## The big picture

Weeks 4–5 told us **how many** carriers there are. This week asks **how they move**, because moving charge is current. There are exactly two reasons a carrier moves in a particular direction:

1. **Drift:** an electric field pushes it. Like water flowing downhill because of gravity.
2. **Diffusion:** there are more carriers in one place than another, and random motion spreads them out. Like a drop of ink spreading in still water (the same idea as dopant diffusion in Week 3, but for electrons and holes, and much faster).

Every current in every device in this course is drift, diffusion, or a mixture. At the end of the week we will see that the two are tied together by a surprisingly simple rule, the **Einstein relation**.

## Part A: Drift, mobility and conductivity

### Random thermal motion

Even with no voltage applied, electrons in a semiconductor are not still. At room temperature they rush about at the **thermal velocity**, about 10⁷ cm/s (100 km/s), bouncing off vibrating atoms and impurities roughly every 0.1–1 picosecond (the **mean free time** τ_m). Their directions are random, so on average they go nowhere: no current.

### Drift in an electric field

Now apply an electric field E. Between collisions each electron is pushed by the field and gains a little extra speed in one direction. At each collision that extra speed is lost (the direction is randomised again). So on top of the random motion there is a small, steady average **drift velocity**:

    v_d = μE

Where:

- v_d = drift velocity (cm/s)
- μ = mobility (cm²/V·s)
- E = electric field (V/cm)

For electrons the drift is against the field (they are negative); for holes it is along the field.

> **In plain words.** Picture a crowd milling about randomly in a square. Tilt the square slightly. People still wander randomly, but on average the crowd now slides slowly downhill. The slow average slide is the drift velocity; the random wandering is much faster but cancels out.

### Mobility

The constant μ is the **mobility**: how much drift velocity you get per unit field.

    μ = v_d / E = qτ_m / m∗      [cm²/V·s]

Where:

- μ = mobility (cm²/V·s)
- v_d = drift velocity (cm/s)
- E = electric field (V/cm)
- q = electronic charge, 1.6×10⁻¹⁹ C
- τ_m = mean free time between collisions (s)
- m∗ = effective mass of the carrier (kg)

From the formula, mobility is high when:

- **collisions are rare** (long τ_m): fewer things to bump into;
- **the effective mass is small** (m∗ small): the carrier is easy to accelerate.

| Material | μ_n (cm²/V·s) | μ_p (cm²/V·s) |
|---|---|---|
| Si | 1350 | 480 |
| Ge | 3900 | 1900 |
| GaAs | 8500 | 400 |

Electrons are faster than holes in all three, mainly because of their smaller effective mass. 

#### Example 7.1: drift velocity

**Question.** An electric field of 1000 V/cm is applied to a silicon sample. Calculate the drift velocity of the electrons and of the holes.

**Given:** E = 1000 V/cm, μ_n = 1350 cm²/V·s, μ_p = 480 cm²/V·s.

**Find:** v_dn and v_dp.

**Formula:**

    v_d = μE

**Solution.**

    v_dn = μ_nE = 1350 × 1000 = 1.35×10⁶ cm/s
    v_dp = μ_pE = 480 × 1000 = 4.8×10⁵ cm/s

**Answer:** **electrons 1.35×10⁶ cm/s, holes 4.8×10⁵ cm/s**, both far below the random thermal velocity of about 10⁷ cm/s.

**What this means:** even in a fairly strong field the electrons' average drift is only about one-seventh of their random thermal speed, so the field only gently biases the random motion; this is why v_d = μE (a constant mobility) still holds here. Holes drift almost three times more slowly than electrons in the same field.

### What scatters carriers

A perfectly regular, perfectly still crystal would not scatter electrons at all (Bloch's theorem, Week 4). Anything that breaks the perfect regularity causes scattering:

1. **Lattice (phonon) scattering.** The atoms vibrate with heat. The hotter, the more they vibrate, and the more they scatter. Mobility falls as μ_L ∝ T^{−3/2}.
2. **Ionised-impurity scattering.** The charged donor and acceptor ions deflect passing carriers, like a magnet deflecting a passing steel ball. Slow carriers are deflected more, so this is worst at **low** temperature and **high** doping: μ_I ∝ T^{3/2}/N_I.
3. **Neutral-impurity scattering**, important only at very low temperature.
4. **Carrier–carrier scattering**, at very high carrier densities.
5. **Defect scattering** from dislocations, grain boundaries and vacancies.
6. **Surface scattering.** In a MOSFET channel, carriers are pressed against the rough Si/SiO₂ surface; channel mobility is only about half the bulk value.
7. **Polar and alloy scattering** in compound semiconductors and alloys.

When several mechanisms act, their scattering rates add, so the reciprocals of the mobilities add (**Matthiessen's rule**):

    1/μ = 1/μ_L + 1/μ_I + …

Where:

- μ = total mobility (cm²/V·s)
- μ_L = mobility if only lattice scattering acted (cm²/V·s)
- μ_I = mobility if only ionised-impurity scattering acted (cm²/V·s)
- … = one more term for each further scattering mechanism

The **lowest** mobility dominates, just as the narrowest section of a pipe limits the flow.

@fig figures/mobility.svg | Mobility against temperature. At low temperature impurity scattering limits mobility; at high temperature lattice scattering does. Heavier doping lowers the curve and moves its peak to higher temperature.

### What affects mobility (summary)

- **Temperature:** near room temperature, higher T → more lattice vibration → lower μ.
- **Doping:** more impurities → more scattering → lower μ (Si electrons: 1350 at light doping, about 800 at 10¹⁷, about 100 at 10²⁰ cm⁻³).
- **Effective mass:** smaller m∗ → higher μ.
- **Electric field:** at very high fields μ falls (velocity saturation, Week 8).
- **Crystal quality, surfaces, orientation and strain.**

### Drift current density

**Current density** J is the charge crossing 1 cm² per second. It equals (charge per carrier) × (number of carriers per cm³) × (their average speed). For electrons, the charge is −q and the velocity is −μ_nE; the two minus signs cancel:

    J_n = (−q)(n)(−μ_nE) = qnμ_nE

For holes:

    J_p = (+q)(p)(+μ_pE) = qpμ_pE

Electrons move against the field but carry negative charge, so their **current** is in the same direction as the hole current. The total drift current is

    J = q(nμ_n + pμ_p) E = σE

Where:

- J = total drift current density (A/cm²)
- q = electronic charge, 1.6×10⁻¹⁹ C
- n, p = electron and hole concentrations (cm⁻³)
- μ_n, μ_p = electron and hole mobilities (cm²/V·s)
- E = electric field (V/cm)
- σ = conductivity (S/cm)

This is just Ohm's law, with **conductivity** and **resistivity**

    σ = q(nμ_n + pμ_p),     ρ = 1/σ

Where:

- σ = conductivity (S/cm)
- ρ = resistivity (Ω·cm)
- q, n, p, μ_n, μ_p as above

For n-type material n ≫ p, so σ ≈ qN_Dμ_n. For p-type, σ ≈ qN_Aμ_p.

#### Example 7.2: conductivity and resistance of a silicon bar

**Question.** A bar of n-type silicon doped with N_D = 1×10¹⁶ cm⁻³ is 1 cm long and has a cross-section of 1 mm². Calculate its conductivity, resistivity and resistance.

**Given:** N_D = 1×10¹⁶ cm⁻³, μ_n = 1350 cm²/V·s, L = 1 cm, A = 1 mm² = 0.01 cm², q = 1.6×10⁻¹⁹ C.

**Find:** σ, ρ and R.

**Formula:**

    σ ≈ qN_Dμ_n,     ρ = 1/σ,     R = ρL/A

**Solution.**

Step 1. n-type, so σ ≈ qN_Dμ_n:

    σ = 1.6×10⁻¹⁹ × 10¹⁶ × 1350 = 2.16 S/cm

Step 2. ρ = 1/σ = 1/2.16 = 0.46 Ω·cm

Step 3. R = ρL/A:

    R = 0.46 × 1 / 0.01 = 46 Ω

**Answer:** **σ = 2.16 S/cm, ρ = 0.46 Ω·cm, R = 46 Ω.**

**What this means:** only one atom in about five million is a donor (silicon has 5×10²² atoms per cm³), yet the bar's resistance drops from about 34 MΩ (undoped, σ_i = qn_i(μ_n + μ_p) = 2.9×10⁻⁶ S/cm) to 46 Ω. Doping is how we set the resistance of a semiconductor, and the 0.46 Ω·cm value is typical of the wafers used to make chips.

**Sheet resistance.** For a thin layer of thickness t, R_s = ρ/t in ohms per square (Ω/□), measured with a four-point probe (Week 3).

### Hall effect

Put a sample carrying current I_x in a magnetic field B_z. The magnetic force pushes the moving carriers sideways, so charge piles up on one side and a small **Hall voltage** V_H appears across the sample. Its **sign** shows whether the carriers are electrons or holes, and its **size** gives their concentration:

    R_H = 1/qp (p-type, positive),   R_H = −1/qn (n-type, negative)

Where:

- R_H = Hall coefficient (cm³/C), found from the measurement as R_H = V_H t/(I_xB_z)
- V_H = Hall voltage (V)
- t = sample thickness along the magnetic field (cm)
- I_x = current through the sample (A)
- B_z = magnetic flux density (Wb/cm²; 1 T = 10⁻⁴ Wb/cm²)
- q = electronic charge, 1.6×10⁻¹⁹ C
- p, n = hole and electron concentrations (cm⁻³)

Combined with a resistivity measurement it gives the mobility, μ = |R_H|σ. This is the standard way to measure carrier type, concentration and mobility.

## Part B: Diffusion, Fick's law and the Einstein relation

### Diffusion of carriers

Suppose there are more electrons on the left of a sample than on the right, for example because light shines on the left. Each electron moves randomly. With more of them on the left, more cross any plane from left to right than from right to left. There is a net flow towards the right, with no field at all. This is **carrier diffusion**.

The flow obeys **Fick's law** (the same law as in Week 3, now for carriers):

    flux of electrons = −D_n dn/dx,     flux of holes = −D_p dp/dx

Where:

- flux = number of carriers crossing 1 cm² per second (cm⁻²s⁻¹)
- D_n, D_p = electron and hole diffusion coefficients (cm²/s)
- dn/dx, dp/dx = gradients of the electron and hole concentrations (cm⁻⁴)
- the minus sign = the flow is from high concentration to low

D_n and D_p are the carrier **diffusion coefficients** (Si at 300 K: D_n ≈ 35 cm²/s, D_p ≈ 12 cm²/s). These are about 10¹⁴ times larger than dopant diffusion coefficients: carriers diffuse across a device in nanoseconds, while dopant atoms need hours in a furnace.

### Diffusion current density

Multiply each particle flux by the charge of the carrier:

    J_n(diff) = (−q)(−D_n dn/dx) = +qD_n dn/dx
    J_p(diff) = (+q)(−D_p dp/dx) = −qD_p dp/dx

Where:

- J_n(diff), J_p(diff) = electron and hole diffusion current densities (A/cm²)
- q = electronic charge, 1.6×10⁻¹⁹ C
- D_n, D_p = electron and hole diffusion coefficients (cm²/s)
- dn/dx, dp/dx = concentration gradients (cm⁻⁴)

**Watch the signs.** Both electrons and holes flow from high concentration to low. But because the electron charge is negative, the **electron current** points **opposite** to the electron flow, while the hole current points the same way as the hole flow.

@fig figures/diffusion-current.svg | Both carriers diffuse down their concentration gradient. Because electrons are negative, the electron diffusion current points against their flow, while the hole current points with it.

#### Example 7.3: electron diffusion current

**Question.** In a silicon sample the electron concentration falls linearly from 1×10¹⁷ cm⁻³ to zero over a distance of 1 μm. Taking D_n = 35 cm²/s, calculate the electron diffusion current density.

**Given:** Δn = 1×10¹⁷ cm⁻³ over Δx = 1 μm = 1×10⁻⁴ cm, D_n = 35 cm²/s, q = 1.6×10⁻¹⁹ C.

**Find:** J_n(diff).

**Formula:**

    J_n(diff) = qD_n dn/dx

**Solution.**

Step 1. The concentration gradient:

    dn/dx = −10¹⁷ / 10⁻⁴ = −10²¹ cm⁻⁴

Step 2. J_n = qD_n dn/dx:

    J_n = 1.6×10⁻¹⁹ × 35 × (−10²¹) = −5.6×10³ A/cm²

**Answer:** **|J_n| = 5.6×10³ A/cm²**, flowing in the −x direction (opposite to the electron flow, because electrons are negative).

**What this means:** a large current, from a modest gradient: through a device area of 100 μm × 100 μm (10⁻⁴ cm²) it would be 0.56 A. Diffusion is not a small effect: it carries the whole current in a diode's neutral regions and in a transistor's base.

### The total current equations

When a field and a gradient are both present, simply add drift and diffusion:

    J_n = qnμ_nE + qD_n dn/dx
    J_p = qpμ_pE − qD_p dp/dx
    J = J_n + J_p

Where:

- J_n, J_p, J = electron, hole and total current densities (A/cm²)
- q = electronic charge, 1.6×10⁻¹⁹ C
- n, p = electron and hole concentrations (cm⁻³)
- μ_n, μ_p = electron and hole mobilities (cm²/V·s)
- E = electric field (V/cm)
- D_n, D_p = electron and hole diffusion coefficients (cm²/s)
- dn/dx, dp/dx = concentration gradients (cm⁻⁴)

These two equations, together with the continuity equation (Week 9) and Poisson's equation, describe every semiconductor device.

### Drift and diffusion compared

| | Drift | Diffusion |
|---|---|---|
| Cause | An electric field E pushes the carriers | A difference in concentration (a gradient dn/dx or dp/dx); random motion spreads the carriers out |
| Needs a field? | Yes | No; it happens even with no field |
| Electron current | J_n = qnμ_nE | J_n = +qD_n dn/dx |
| Hole current | J_p = qpμ_pE | J_p = −qD_p dp/dx |
| Depends on | How many carriers there are (n, p) | How fast their number changes with position (dn/dx, dp/dx) |
| Material constant | Mobility μ (cm²/V·s) | Diffusion coefficient D (cm²/s) |
| Direction of carrier flow | Holes along E, electrons against E | Both from high to low concentration |
| Direction of current | Electron and hole currents both along E (they add) | Hole current along the hole flow; electron current opposite to the electron flow |
| Which carriers it usually matters for | Majority carriers (there are many of them) | Minority carriers (small numbers, but steep gradients) |
| Where it dominates | Resistors, the channel of a MOSFET, carriers swept across a reverse-biased junction | Neutral regions of a forward-biased diode, the base of a BJT, solar cells |
| Everyday picture | Water flowing downhill | Ink spreading in still water |

The two are tied together by the Einstein relation, D/μ = kT/q, because the same collisions limit both.

### The Einstein relation

Drift and diffusion are two responses of the same carriers to two different pushes, and both are limited by the **same collisions**. So it is no surprise that μ and D are related:

    D_n / μ_n = D_p / μ_p = kT/q

Where:

- D_n, D_p = electron and hole diffusion coefficients (cm²/s)
- μ_n, μ_p = electron and hole mobilities (cm²/V·s)
- k = Boltzmann constant, 8.617×10⁻⁵ eV/K
- T = absolute temperature (K)
- q = electronic charge, 1.6×10⁻¹⁹ C

kT/q is the **thermal voltage**, 0.0259 V (about 26 mV) at 300 K.

**Why it is true (the equilibrium argument).** Take an n-type sample whose doping is higher on the left than on the right, and leave it alone (no battery).

1. Electrons diffuse from the heavily doped left side towards the right.
2. As they leave, they uncover positive donor ions on the left. Positive charge on the left and extra electrons on the right create an internal electric field.
3. The field pulls electrons back to the left: a drift current opposite to the diffusion current.
4. With no battery, no net current can flow, so in equilibrium **drift exactly cancels diffusion**: 0 = qnμ_nE + qD_n dn/dx.
5. In equilibrium the Fermi level is flat (Week 5). Using n = N_c e^{−(E_c − E_F)/kT}, the gradient dn/dx can be written in terms of the field: dn/dx = −(qn/kT)E.
6. Substituting: 0 = qnμ_nE − qD_n(qn/kT)E, which gives D_n/μ_n = kT/q.

**Using it.** Mobility is easy to measure (Hall effect, conductivity), so D follows immediately:

| | μ (cm²/V·s) | D = μ × 0.0259 (cm²/s) |
|---|---|---|
| Si electrons | 1350 | 35.0 |
| Si holes | 480 | 12.4 |
| GaAs electrons | 8500 | 220 |
| Ge electrons | 3900 | 101 |

> **In plain words.** A carrier that rarely collides both drifts easily in a field (high μ) and spreads quickly by itself (high D). The ratio between the two depends only on temperature.

## Key points of Week 7

- Drift: v_d = μE, with μ = qτ/m∗. Electrons are faster than holes; GaAs electrons are fastest.
- Mobility is limited by lattice scattering (worse when hot) and impurity scattering (worse when heavily doped); 1/μ = Σ1/μ_i.
- Drift current J = q(nμ_n + pμ_p)E = σE; σ ≈ qN_Dμ_n for n-type.
- Diffusion: carriers flow down their concentration gradient. J_n = qD_n dn/dx, J_p = −qD_p dp/dx.
- Total current = drift + diffusion.
- Einstein relation: D/μ = kT/q = 0.0259 V at 300 K.

---

## Examination questions solved (Q35–Q40)

### Q35. Define carrier mobility and explain the factors that affect electron and hole mobility in semiconductors.

**Definition.** Carrier mobility μ is the drift velocity acquired per unit applied electric field:

    μ = |v_d| / E = qτ_m / m∗      [cm²/V·s]

where τ_m is the mean free time between collisions and m∗ the effective mass. It measures how easily carriers move through the crystal under a field. Electron mobility μ_n and hole mobility μ_p are different (Si: 1350 and 480 cm²/V·s).

**Factors affecting mobility:**

1. **Effective mass.** μ ∝ 1/m∗. Electrons generally have lighter effective mass than holes, so μ_n > μ_p. GaAs electrons (m∗ = 0.067m₀) have μ_n ≈ 8500 cm²/V·s.
2. **Temperature.** Two opposing effects:
   (a) Lattice scattering increases with T, μ_L ∝ T^{−3/2}.
   (b) Ionised-impurity scattering decreases with T, μ_I ∝ T^{3/2}/N_I, since faster carriers are deflected less.
   Mobility therefore rises at low T, peaks, and falls at high T. Near room temperature lattice scattering usually dominates and μ falls as T rises.
3. **Doping (impurity) concentration.** More ionised impurities mean more Coulomb scattering: μ falls as N_D + N_A increases (Si μ_n ≈ 1350 at 10¹⁴ cm⁻³ but about 100 at 10²⁰ cm⁻³). Compensated material has low mobility even though net doping is small.
4. **Electric field.** At low field μ is constant. At high field carriers heat up, emit optical phonons, and drift velocity saturates, so the effective mobility v_d/E falls.
5. **Crystal defects** (dislocations, grain boundaries, vacancies) add scattering; polycrystalline and amorphous material have much lower mobility.
6. **Surface and interface scattering.** In MOSFET channels, roughness and interface charge reduce mobility to roughly half the bulk value, and it falls further with higher gate field.
7. **Crystal orientation and strain.** Mobility depends on direction in anisotropic bands; strain alters effective masses (strained-Si technology).
8. **Carrier concentration** at high injection (carrier–carrier scattering).

These are combined using Matthiessen's rule, 1/μ = 1/μ_L + 1/μ_I + …

### Q36. Explain the mechanisms responsible for carrier scattering in semiconductor materials.

In a perfectly periodic, motionless lattice an electron would move without scattering (Bloch's theorem). Scattering happens whenever something breaks that perfect periodicity. The main mechanisms:

1. **Lattice (phonon) scattering.** Above 0 K the atoms vibrate about their positions, distorting the periodic potential. Carriers exchange energy and momentum with these lattice vibrations (phonons). *Acoustic-phonon* scattering is low-energy and nearly elastic, dominant at room temperature in Si; its rate increases with T, giving μ_L ∝ T^{−3/2}. *Optical-phonon* scattering involves high-energy phonons (63 meV in Si); it matters at high temperatures and high fields and causes velocity saturation. *Polar-optical and piezoelectric* scattering occur in compound semiconductors (GaAs), where the vibrating ionic bonds create electric fields that scatter carriers strongly.
2. **Ionised-impurity scattering.** Ionised donors (+) and acceptors (−) have Coulomb fields that deflect passing carriers (Rutherford-like scattering). Slower carriers spend more time near the ion and are deflected more, so it is strongest at low temperature and high doping: μ_I ∝ T^{3/2}/N_I.
3. **Neutral-impurity scattering.** Non-ionised impurity atoms scatter weakly by their distorted potential. Matters only at low temperatures when dopants are frozen out.
4. **Carrier–carrier scattering.** Coulomb interactions between carriers. Important at very high carrier densities (heavily doped or highly injected regions, e.g. in power devices and solar cells).
5. **Defect scattering.** Dislocations (charged lines in n-type material), grain boundaries, stacking faults, vacancies and clusters disturb the lattice and scatter carriers.
6. **Surface and interface scattering.** At surfaces and at the Si/SiO₂ interface, surface roughness, interface traps and oxide charges scatter carriers confined near the interface (MOSFET channels).
7. **Alloy scattering.** In alloys such as Al_{x}Ga_{1−x}As or SiGe, the random distribution of different atoms makes the potential non-periodic.
8. **Intervalley scattering.** Carriers move between equivalent or non-equivalent conduction-band minima by absorbing or emitting phonons (basis of the Gunn effect).

The total rate is the sum of the individual rates, 1/τ = Σ 1/τ_i, giving Matthiessen's rule 1/μ = Σ 1/μ_i. Near room temperature in lightly doped Si, lattice scattering dominates; in heavily doped Si or at low temperature, ionised-impurity scattering dominates.

### Q37. Derive the expression for drift current density due to electrons and holes.

**Assumptions:** uniform semiconductor, steady state, uniform field E in the +x direction, low enough field that v_d ∝ E.

**Step 1: drift velocity.** An electron experiences force F = −qE. Between collisions (mean free time τ_m), it accelerates by a = −qE/m_n∗. Averaging over all electrons, momentum gained from the field equals momentum lost in collisions:

    m_n∗ v_dn / τ_m = −qE   ⇒   v_dn = −(qτ_m/m_n∗) E = −μ_n E

Similarly, holes (charge +q) drift with the field:

    v_dp = +(qτ_mp/m_p∗) E = +μ_p E

**Step 2: current density from charge flow.** Current density is charge density × velocity. Consider a bar of cross-section A. In time dt, all carriers within distance v_d·dt of a cross-section pass through it; that is (v_d dt A) × concentration carriers.

For electrons, charge density −qn and velocity v_dn:

    J_n = (−qn)(v_dn) = (−qn)(−μ_n E) = qnμ_n E

For holes, charge density +qp and velocity v_dp:

    J_p = (+qp)(+μ_p E) = qpμ_p E

Electrons move against the field but carry negative charge, so their current is in the same direction as the hole current: both are along E.

**Step 3: total drift current density.**

    J_drift = J_n + J_p = q( nμ_n + pμ_p ) E

Comparing with Ohm's law J = σE:

    σ = q( nμ_n + pμ_p ),     ρ = 1/σ = 1 / [ q(nμ_n + pμ_p) ]

For an n-type sample (n ≫ p), σ ≈ qnμ_n ≈ qN_Dμ_n; for p-type, σ ≈ qN_Aμ_p. For an intrinsic sample, σ_i = qn_i(μ_n + μ_p).

### Q38. A semiconductor has an electron concentration of 2 × 10¹⁶ cm⁻³, electron mobility of 1350 cm²/V·s, and an electric field of 10 V/cm. Calculate the electron drift current density.

**Question.** Calculate the electron drift current density for n = 2×10¹⁶ cm⁻³, μ_n = 1350 cm²/V·s and E = 10 V/cm.

**Given:** n = 2×10¹⁶ cm⁻³, μ_n = 1350 cm²/V·s, E = 10 V/cm, q = 1.602×10⁻¹⁹ C.

**Find:** J_n (drift).

**Formula:**

    J_n = qnμ_nE

**Solution.**

    J_n = q n μ_n E
        = (1.602×10⁻¹⁹ C)(2×10¹⁶ cm⁻³)(1350 cm²/V·s)(10 V/cm)
        = (1.602×10⁻¹⁹)(2.7×10²⁰)   A/cm²
        = 43.3 A/cm²

**Answer:** **J_n ≈ 43.3 A/cm²** (= 4.33×10⁵ A/m²). (With the rounded q = 1.6×10⁻¹⁹ C the result is 43.2 A/cm².)

**Units check:** C · cm⁻³ · cm²/(V·s) · V/cm = C/(s·cm²) = A/cm². ✓

Supporting quantities:

- Drift velocity v_d = μ_nE = 1350 × 10 = 1.35×10⁴ cm/s (well below v_sat = 10⁷ cm/s, so the linear model is valid).
- Conductivity σ = qnμ_n = 4.33 S/cm, resistivity ρ = 0.231 Ω·cm, and J = σE = 4.33 × 10 = 43.3 A/cm². ✓

**What this means:** a modest field of only 10 V/cm (1 V across 1 mm) already drives about 43 A through every square centimetre, because there are so many electrons; the electrons themselves creep along at only 1.35×10⁴ cm/s, almost a thousand times slower than their thermal speed.

### Q39. Explain diffusion current in a semiconductor and state Fick's law.

**Diffusion current** is the current produced by the net movement of carriers from a region of higher concentration to one of lower concentration, caused by their random thermal motion. No electric field is needed. If the concentration varies with position, more carriers cross any plane from the high-concentration side than from the low side simply because there are more of them, so a net flux results. Because the carriers are charged, this flux is a current.

Diffusion current is important wherever carrier gradients exist: in the neutral regions of a forward-biased p-n junction (injected minority carriers diffusing away from the junction), in the base of a bipolar transistor, under non-uniform illumination, and in non-uniformly doped material.

**Fick's (first) law.** The particle flux is proportional to the negative of the concentration gradient:

    F = −D dC/dx

where D is the diffusion coefficient (cm²/s). Applied to electrons and holes:

    Electron flux:  F_n = −D_n dn/dx       Hole flux:  F_p = −D_p dp/dx

**Diffusion current densities** (multiply by the charge, −q for electrons, +q for holes):

    J_{n,diff} = +q D_n dn/dx
    J_{p,diff} = −q D_p dp/dx

In three dimensions, J_n = qD_n∇n and J_p = −qD_p∇p.

**Example.** If the electron concentration falls linearly from 10¹⁷ cm⁻³ to 0 over 1 μm in Si (D_n = 35 cm²/s):

    dn/dx = −10¹⁷/10⁻⁴ = −10²¹ cm⁻⁴
    J_n = q D_n dn/dx = (1.602×10⁻¹⁹)(35)(−10²¹) = −5.6×10³ A/cm²

The negative sign means the current flows in the −x direction, while the electrons themselves flow in +x (down their gradient).

Total current when a field is present: J_n = qnμ_nE + qD_n dn/dx and J_p = qpμ_pE − qD_p dp/dx.

### Q40. State and explain the Einstein relation between carrier mobility and diffusion coefficient.

**Statement.**

    D_n/μ_n = kT/q,      D_p/μ_p = kT/q

The ratio of diffusion coefficient to mobility equals the thermal voltage kT/q (0.0259 V at 300 K), for both electrons and holes, in a non-degenerate semiconductor.

**Explanation.** Drift and diffusion are two responses of the same carriers, both limited by the same random scattering events. Mobility describes the response to an electric field (μ = qτ_m/m∗); diffusion describes the response to a concentration gradient (D = v_th²τ_m/3 ≈ kTτ_m/m∗). Dividing gives D/μ = kT/q: the scattering time and mass cancel, leaving only temperature.

**Derivation (equilibrium argument).** In a non-uniformly doped sample in thermal equilibrium, an internal field E develops such that the drift and diffusion currents cancel exactly:

    J_n = qnμ_nE + qD_n dn/dx = 0

In equilibrium E_F is constant and n = n_i exp((E_F − E_i)/kT). Since E_i varies with the electrostatic potential, dE_i/dx = qE, so

    dn/dx = −(n/kT) dE_i/dx = −(qn/kT) E

Substituting:

    qnμ_nE − qD_n(qn/kT)E = 0   ⇒   D_n = (kT/q)μ_n

**Uses.**

1. One measurement gives the other: mobility is easy to measure (Hall effect, conductivity), so D follows. Si electrons: D_n = 0.0259 × 1350 = **35 cm²/s**; holes: D_p = 0.0259 × 480 = **12.4 cm²/s**.
2. It links the drift and diffusion terms in the current equations and is needed to calculate diffusion lengths L = √(Dτ) and diode saturation currents.
3. It shows why the built-in voltage of a junction is set by kT/q times a logarithm of a concentration ratio.

For degenerate semiconductors the relation is modified (D/μ > kT/q), because carriers then obey Fermi–Dirac rather than Boltzmann statistics.

---

## Practice questions

These extra questions practise this week's ideas. Work each one on paper before reading the solution; the calculation questions follow the same Question, Given, Find, Solution, Answer layout as the worked examples.

#### Practice 7.1: resistivity of p-type silicon

**Question.** Find the resistivity of silicon doped with 5×10¹⁵ cm⁻³ boron, taking μ_p = 470 cm²/V·s.

**Given:** N_A = 5×10¹⁵ cm⁻³, μ_p = 470 cm²/V·s.

**Find:** ρ.

**Solution.**

    σ = qN_Aμ_p = 1.6×10⁻¹⁹ × 5×10¹⁵ × 470 = 0.376 S/cm
    ρ = 1/σ = 2.66 Ω·cm

**Answer:** **ρ = 2.7 Ω·cm.**

#### Practice 7.2: doping for a target resistivity

**Question.** What phosphorus concentration gives n-type silicon a resistivity of 1 Ω·cm? Take μ_n = 1300 cm²/V·s.

**Given:** ρ = 1 Ω·cm, μ_n = 1300 cm²/V·s.

**Find:** N_D.

**Solution.**

    N_D = 1/(qμ_nρ) = 1/(1.6×10⁻¹⁹ × 1300 × 1) = 4.8×10¹⁵ cm⁻³

**Answer:** **N_D ≈ 4.8×10¹⁵ cm⁻³.**

#### Practice 7.3: Hall measurement

**Question.** A semiconductor sample 0.01 cm thick carries I = 1 mA in a magnetic field of 0.1 T (10⁻⁵ Wb/cm²). A Hall voltage of +2 mV is measured, and the resistivity is 4 Ω·cm. Find the carrier type, concentration and mobility.

**Given:** t = 0.01 cm, I = 10⁻³ A, B = 10⁻⁵ Wb/cm², V_H = +2×10⁻³ V, ρ = 4 Ω·cm.

**Find:** type, p, μ.

**Solution.**

    R_H = V_H t/(IB) = (2×10⁻³ × 0.01)/(10⁻³ × 10⁻⁵) = 2000 cm³/C   (positive → holes)
    p = 1/(qR_H) = 1/(1.6×10⁻¹⁹ × 2000) = 3.1×10¹⁵ cm⁻³
    μ_p = R_H/ρ = 2000/4 = 500 cm²/V·s

**Answer:** **p-type, p = 3.1×10¹⁵ cm⁻³, μ_p = 500 cm²/V·s.**

#### Practice 7.4: combining scattering mechanisms

**Question.** In a silicon sample the lattice-limited mobility is 1400 cm²/V·s and the impurity-limited mobility is 2500 cm²/V·s. Find the total mobility.

**Given:** μ_L = 1400, μ_I = 2500 cm²/V·s.

**Find:** μ.

**Solution.**

    1/μ = 1/1400 + 1/2500 = 7.14×10⁻⁴ + 4.0×10⁻⁴ = 1.114×10⁻³
    μ = 897 cm²/V·s

**Answer:** **μ ≈ 900 cm²/V·s**, lower than either mechanism alone.

#### Practice 7.5: drift plus diffusion

**Question.** In a region of silicon the hole concentration is 1×10¹⁵ cm⁻³ and falls with a gradient of −1×10¹⁸ cm⁻⁴, while a field of 50 V/cm acts in the +x direction. Find the hole drift, diffusion and total current densities (μ_p = 480 cm²/V·s, D_p = 12.4 cm²/s).

**Given:** p = 10¹⁵ cm⁻³, dp/dx = −10¹⁸ cm⁻⁴, E = 50 V/cm, μ_p = 480, D_p = 12.4 cm²/s.

**Find:** J_p(drift), J_p(diff), J_p.

**Solution.**

    J_p(drift) = qpμ_pE = 1.6×10⁻¹⁹ × 10¹⁵ × 480 × 50 = 3.84 A/cm²
    J_p(diff) = −qD_p dp/dx = −1.6×10⁻¹⁹ × 12.4 × (−10¹⁸) = +1.98 A/cm²
    J_p = 3.84 + 1.98 = 5.82 A/cm²

**Answer:** **3.84 + 1.98 = 5.8 A/cm²**, both in the +x direction.

#### Practice 7.6: Einstein relation at a higher temperature

**Question.** Holes in a sample have μ_p = 400 cm²/V·s at 400 K. Find D_p.

**Given:** μ_p = 400 cm²/V·s, T = 400 K.

**Find:** D_p.

**Solution.**

    kT/q = 8.617×10⁻⁵ × 400 = 0.0345 V
    D_p = (kT/q)μ_p = 0.0345 × 400 = 13.8 cm²/s

**Answer:** **D_p = 13.8 cm²/s.**

#### Practice 7.7: why doping lowers mobility

**Question.** Explain why electron mobility in silicon falls from about 1350 to about 100 cm²/V·s as the doping rises from 10¹⁴ to 10²⁰ cm⁻³.

**Answer.** Each dopant is an ionised impurity with a Coulomb field that deflects passing carriers. Mobility is μ = qτ_m/m∗; more ionised impurities mean more frequent scattering, a shorter mean free time τ_m, and so a lower μ. At 10¹⁴ cm⁻³ lattice scattering dominates and impurities hardly matter; at 10²⁰ cm⁻³ impurity scattering dominates completely (Matthiessen: 1/μ = 1/μ_L + 1/μ_I, with μ_I ∝ 1/N_I).

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Explain thermal motion, drift velocity and mobility. | Si electrons in a 500 V/cm field: find v_d. | v_d = 1350 × 500 = 6.75×10⁵ cm/s. | Part A; Example 7.1 |
| 2 | Explain the scattering mechanisms and the factors that affect mobility. | Which scattering mechanism dominates at low temperature in heavily doped Si? | Ionised-impurity scattering. | Scattering; factors affecting mobility |
| 3 | Derive and use the drift current density and conductivity. | Find σ for p-type Si with N_A = 10¹⁶ cm⁻³ and μ_p = 480 cm²/V·s. | σ = 1.6×10⁻¹⁹ × 10¹⁶ × 480 = 0.77 S/cm. | Drift current density; Example 7.2 |
| 4 | Explain carrier diffusion and calculate diffusion current with Fick's law. | Why does electron diffusion current point opposite to the electron flow? | Because the electron charge is negative. | Part B; Example 7.3; Drift and diffusion compared |
| 5 | State, explain and use the Einstein relation. | Find D_n for GaAs (μ_n = 8500 cm²/V·s) at 300 K. | D = 0.0259 × 8500 = 220 cm²/s. | The Einstein relation |
