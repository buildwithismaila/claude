# Module 07 — Ion Implantation

Examined in Q20–Q21. Ion implantation has replaced diffusion for almost all doping steps in modern ICs, because it lets you set the dose and depth independently and precisely at low temperature.

## 7.1 Principle

Dopant atoms are **ionised**, **accelerated** through a high voltage (typically 1 keV to several MeV) and **fired into** the wafer. The ions lose their energy by collisions with the lattice electrons (electronic stopping) and nuclei (nuclear stopping) and come to rest at some depth. A subsequent **anneal** repairs the damage and moves the dopants onto substitutional sites where they become electrically active.

## 7.2 The implanter

1. **Ion source:** a gas such as BF₃, PH₃ or AsH₃ is ionised in a plasma (arc chamber).
2. **Extraction:** ions are pulled out by an extraction voltage (≈ 20–40 kV).
3. **Mass analyser:** a magnet bends the beam. Only ions with the selected mass-to-charge ratio pass through the slit, so the beam is isotopically pure (e.g. ¹¹B⁺ only).
4. **Acceleration tube:** raises the ions to the final energy.
5. **Scanning and focusing:** electrostatic or mechanical scanning spreads the beam uniformly over the wafer.
6. **Target chamber and dose measurement:** a **Faraday cup** collects the beam current, and integrating it gives the dose.

Dose (ions per cm²):

    Φ = (1/qA) ∫ I dt = I·t / (q·A)       (singly charged ions)

**Example.** Beam current 10 μA for 100 s over a 200 mm wafer (A = 314 cm²): Φ = (10×10⁻⁶ × 100)/(1.602×10⁻¹⁹ × 314) = 2.0×10¹³ ions/cm².

## 7.3 The implanted profile

To first order the profile is **Gaussian**, centred at the **projected range** R_p with **straggle** (standard deviation) ΔR_p:

    N(x) = ( Φ / (√(2π) ΔR_p) ) · exp( −(x − R_p)² / 2ΔR_p² )

    Peak concentration  N_p = Φ / (√(2π) ΔR_p) ≈ 0.4 Φ / ΔR_p

R_p increases with ion energy and decreases with ion mass. Rough values in Si at 100 keV: B, R_p ≈ 0.30 μm; P, 0.12 μm; As, 0.06 μm.

**Example.** Φ = 1×10¹⁵ cm⁻² of As with ΔR_p = 0.02 μm = 2×10⁻⁶ cm gives N_p = 0.4 × 10¹⁵/2×10⁻⁶ = 2×10²⁰ cm⁻³.

@fig figures/implant.svg | An implanted profile peaks below the surface at the projected range R_p, unlike a diffused profile, which always peaks at the surface.

## 7.4 Practical effects

- **Lattice damage.** Each heavy ion displaces thousands of Si atoms. High doses turn the surface **amorphous**.
- **Annealing** repairs damage and activates dopants: furnace anneal (900–1000 °C, 30 min) or **rapid thermal anneal** (RTA, ≈ 1000–1100 °C for a few seconds) which limits further diffusion. Laser and flash anneals use even shorter times.
- **Channelling.** Ions entering along a low-index direction (e.g. ⟨110⟩) travel down open "channels" in the crystal and go much deeper than predicted. Prevented by **tilting the wafer about 7°**, rotating it, implanting through a thin screen oxide, or pre-amorphising the surface.
- **Masking.** Photoresist, SiO₂, Si₃N₄ or polysilicon stops the ions where doping is not wanted. A thick enough mask is a few R_p + ΔR_p.
- **Self-aligned gates.** In a MOSFET the polysilicon gate itself masks the channel while the source and drain are implanted, which aligns them to the gate automatically.

---

## Exam questions solved

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
