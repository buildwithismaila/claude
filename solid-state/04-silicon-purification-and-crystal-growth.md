# Module 04 — Silicon Purification and Czochralski Growth

Not covered in the lecture note, but examined (Q9–Q11). A device needs silicon with fewer than about one unwanted impurity atom per billion, grown as one perfect crystal. This module explains how sand becomes a wafer.

## 4.1 The route from sand to wafer

    Quartzite (SiO₂) → MG-Si (98 %) → SiHCl₃ → purified SiHCl₃ → EG-Si polysilicon → single-crystal ingot → wafers

| Stage | Product | Purity |
|---|---|---|
| Carbothermic reduction in an arc furnace | Metallurgical-grade Si (MG-Si) | ≈ 98–99 % |
| Hydrochlorination, distillation, Siemens CVD | Electronic-grade polysilicon (EG-Si) | 99.9999999 % (9N) or better; impurities at ppb level |
| Czochralski or float-zone growth | Single-crystal, doped ingot | Dopant set deliberately |

## 4.2 Stage 1: metallurgical-grade silicon

Quartzite (fairly pure SiO₂) is mixed with carbon (coal, coke, wood chips) and heated to about **2000 °C** in a submerged-electrode arc furnace:

    SiO₂ + 2C → Si + 2CO

Molten silicon is tapped from the furnace. MG-Si is about 98 % pure; the main impurities are Fe, Al, Ca, C, B and P. It is fine for steel and aluminium alloys and silicones, but far too impure for devices (it would contain about 10²⁰ cm⁻³ of unwanted impurities).

## 4.3 Stage 2: conversion to trichlorosilane

MG-Si is ground and reacted with dry hydrogen chloride in a fluidised-bed reactor at about **300 °C**:

    Si + 3HCl → SiHCl₃ + H₂

Trichlorosilane (TCS) is a liquid that boils at 32 °C. The impurities form their own chlorides (FeCl₃, AlCl₃, BCl₃, PCl₃) with different boiling points.

## 4.4 Stage 3: fractional distillation

The liquid SiHCl₃ is purified by repeated **fractional distillation**, which separates it from the impurity chlorides because of the boiling-point differences. Because distillation of a liquid is very effective, the TCS reaches impurity levels in the parts-per-billion range.

## 4.5 Stage 4: Siemens process (CVD of polysilicon)

Purified TCS and hydrogen are fed into a bell-jar reactor containing thin, high-purity silicon rods heated electrically to about **1100 °C**. Silicon deposits on the rods by chemical vapour deposition:

    SiHCl₃ + H₂ → Si + 3HCl

The rods grow over many hours into thick bars of **electronic-grade polycrystalline silicon** (EG-Si), purity 9N to 11N. The by-products are recycled. EG-Si is still polycrystalline and undoped; the next step turns it into one crystal with the right doping.

## 4.6 Stage 5: single-crystal growth

The polysilicon is melted and regrown as a single crystal by the **Czochralski (CZ)** method (most wafers) or the **float-zone (FZ)** method (very high resistivity). The ingot is then ground to diameter, given an orientation flat or notch, sliced into wafers with a wire saw, lapped, etched and chemically-mechanically polished.

## 4.7 The Czochralski method

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

---

## Exam questions solved

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
