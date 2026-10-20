# Module 17 — Device Technology: BJT and MOSFET

On the official syllabus ("physics of operational solid-state devices including p-n diodes, BJTs and FETs/MOSFETs") but not on the 50-question paper. This module shows how the physics of Modules 09–16 makes the two transistors work, so a long essay question on devices will not catch you out.

## 17.1 The bipolar junction transistor (BJT)

An npn BJT is two p-n junctions back to back sharing a thin p-type **base**: heavily doped n⁺ emitter, thin moderately doped p base, lightly doped n collector.

**Forward-active mode:** emitter–base junction forward biased, collector–base junction reverse biased.

1. The forward-biased E–B junction **injects electrons** from the emitter into the base (law of the junction: n_p(0) = n_p0 e^{qV_BE/kT}).
2. The base is much thinner than the electron diffusion length (W_B ≪ L_n), so almost all injected electrons **diffuse across** the base without recombining. The profile is nearly linear.
3. At the reverse-biased C–B junction the field **sweeps** them into the collector.

Collector current, from the slope of the linear profile:

    I_C = (qAD_n n_i² / (N_A W_B)) · exp(qV_BE/kT) = I_S e^{qV_BE/kT}

The base current is the much smaller hole current injected back into the emitter plus recombination in the base.

**Efficiencies and gain:**

    Emitter injection efficiency  γ ≈ 1 − (D_p N_A W_B)/(D_n N_D L_pE)   → keep N_D(emitter) ≫ N_A(base)
    Base transport factor  α_T ≈ 1 − W_B²/(2L_n²)                       → thin base, long lifetime
    α = γα_T = I_C/I_E,     β = α/(1 − α) = I_C/I_B   (typically 50–500)

**Non-ideal effects:** base-width modulation (**Early effect**, finite output resistance), high-level injection, base resistance, avalanche breakdown of the C–B junction, and the base transit time τ_B = W_B²/2D_n which limits f_T. The SiGe heterojunction bipolar transistor (HBT) improves γ by using a narrower-gap base.

## 17.2 The MOS capacitor

Metal (or poly-Si) gate, SiO₂ insulator, p-type Si substrate. As gate voltage V_G increases:

- **Accumulation** (V_G < V_FB): holes pile up at the surface; C = C_ox.
- **Depletion** (V_FB < V_G < V_T): holes pushed away, leaving negative acceptor ions; C falls.
- **Inversion** (V_G > V_T): the surface potential reaches 2φ_F, where φ_F = (kT/q) ln(N_A/n_i). Electrons become the majority at the surface: an n-type **inversion layer** (channel).

Threshold voltage:

    V_T = V_FB + 2φ_F + √(2qε_sN_A·2φ_F) / C_ox,     C_ox = ε_ox/t_ox

V_FB = Φ_ms − Q_f/C_ox includes the work-function difference and fixed oxide charge. Mobile ions (Na⁺) and interface traps make V_T drift: the **stability** problem the syllabus mentions.

## 17.3 The MOSFET

Add n⁺ source and drain on either side of the gate. With V_GS > V_T, the inversion channel connects them and current flows when V_DS is applied.

Square-law (long-channel) model, n-channel:

    Linear (V_DS < V_GS − V_T):   I_D = μ_n C_ox (W/L) [ (V_GS − V_T)V_DS − V_DS²/2 ]
    Saturation (V_DS ≥ V_GS − V_T):  I_D = (μ_n C_ox/2)(W/L)(V_GS − V_T)²

Saturation happens when the channel **pinches off** at the drain end.

**Short-channel effects** connect back to Module 10: velocity saturation (I_D ∝ V_GS − V_T instead of the square), hot-carrier injection, drain-induced barrier lowering, channel-length modulation and reduced surface mobility. CMOS combines n- and p-channel MOSFETs so that almost no static current flows.

## 17.4 Other FETs

- **JFET:** a reverse-biased p-n junction gate widens its depletion region into the channel to pinch it off.
- **MESFET:** the same idea with a Schottky gate (Module 15); standard in GaAs microwave circuits.
- **HEMT:** a modulation-doped AlGaAs/GaAs (or AlGaN/GaN) heterojunction forms a 2-D electron gas with very high mobility, made by MBE or MOCVD (Module 05).

## 17.5 How the course fits together

| Device feature | Physics behind it | Module |
|---|---|---|
| Junction barrier, V_bi | Constant Fermi level, carrier statistics | 09, 14 |
| Exponential I-V | Law of the junction, Boltzmann statistics | 14 |
| Diffusion across base | Diffusion current, continuity equation, L = √(Dτ) | 11, 13 |
| Current gain β | Minority-carrier lifetime, SRH recombination | 12 |
| Channel conduction | Drift, surface mobility | 10 |
| Saturation in short channels | Velocity saturation, hot carriers | 10 |
| Contacts and gates | Schottky and Ohmic contacts | 15 |
| Thin base, sharp doping | Epitaxy, diffusion, ion implantation | 05–07 |
| Gate oxide, (100) wafers | Si/SiO₂ interface, crystal orientation | 01, 02 |
