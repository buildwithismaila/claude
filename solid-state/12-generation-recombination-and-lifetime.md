# Module 12 — Generation, Recombination and Carrier Lifetime

Examined in Q42–Q44. Devices work by disturbing equilibrium: light, forward bias or a field injects extra carriers. How fast those extra carriers disappear sets the switching speed of a diode, the gain of a transistor and the efficiency of a solar cell.

## 12.1 Equilibrium and excess carriers

In thermal equilibrium, carriers are generated and recombine continuously at equal rates, G_th = R_th, so n₀p₀ = n_i².

**Excess carriers** are those above equilibrium:

    n = n₀ + Δn,      p = p₀ + Δp

Created optically or by injection, electrons and holes are usually made in pairs, so Δn = Δp. Then np > n_i², and net recombination returns the system towards equilibrium.

**Low-level injection:** Δp ≪ n₀ in n-type material. The majority concentration hardly changes, n ≈ n₀, while the **minority** concentration may change by many orders of magnitude. Minority carriers therefore control the behaviour.

**Example.** n-Si with N_D = 10¹⁶ cm⁻³ (p₀ = 10⁴ cm⁻³) illuminated to give Δn = Δp = 10¹⁴ cm⁻³: n = 1.01×10¹⁶ (1 % change), p = 10¹⁴ (a factor of 10¹⁰ change).

## 12.2 Generation mechanisms

1. **Thermal generation:** lattice vibrations supply E_g to break a bond. Mostly through defect levels in the gap (two small steps are easier than one big one).
2. **Optical generation:** a photon with hν ≥ E_g is absorbed and creates an electron–hole pair. Basis of photodiodes and solar cells. Generation rate G (cm⁻³s⁻¹) falls with depth as e^{−αx}.
3. **Impact ionisation:** a high-field carrier knocks an electron out of a bond (avalanche).
4. **Band-to-band tunnelling** at very high fields (Zener effect).

## 12.3 Recombination mechanisms

@fig figures/recombination.svg | The three recombination paths. Band-to-band emits a photon. Shockley–Read–Hall goes through a trap level in the gap. Auger gives the energy to a third carrier.

1. **Direct (band-to-band, radiative):** an electron falls directly from the conduction band into a hole, emitting a photon of energy ≈ E_g. Rate R = B·np. Dominant in direct-gap GaAs (LEDs, lasers); very weak in indirect Si.
2. **Indirect (trap-assisted, Shockley–Read–Hall):** recombination through a localised **trap** (recombination centre) in the gap, created by defects or impurities such as Au, Fe, Cu or Pt. Energy goes to phonons (heat). Dominant in Si and Ge.
3. **Auger:** the energy released by recombination is given to a third carrier, which is kicked high into its band and then thermalises. Rate ∝ n²p or np². Dominant at very high carrier densities (heavily doped emitters, concentrator solar cells, lasers).
4. **Surface recombination:** SRH recombination through the high density of states at surfaces and interfaces (Module 13).

## 12.4 Shockley–Read–Hall (SRH) recombination

A single trap level at E_t, density N_t, with capture cross-sections σ_n and σ_p. Four processes take place:

1. **Electron capture:** a conduction electron falls into an empty trap. Rate ∝ σ_n v_th n N_t(1 − f_t).
2. **Electron emission:** a trapped electron is emitted to the conduction band. Rate ∝ e_n N_t f_t.
3. **Hole capture:** a trapped electron drops to the valence band, filling a hole. Rate ∝ σ_p v_th p N_t f_t.
4. **Hole emission:** an electron from the valence band jumps into an empty trap, creating a hole. Rate ∝ e_p N_t(1 − f_t).

Recombination is (1) followed by (3); generation is (4) followed by (2). Requiring the trap occupancy f_t to be in steady state (electrons in = electrons out) gives the SRH net rate:

    U = (np − n_i²) / [ τ_p(n + n₁) + τ_n(p + p₁) ]

    τ_n = 1/(σ_n v_th N_t),   τ_p = 1/(σ_p v_th N_t)
    n₁ = n_i exp((E_t − E_i)/kT),   p₁ = n_i exp((E_i − E_t)/kT)

**Key results:**

- U > 0 (net recombination) when np > n_i² (injection). U < 0 (net generation) when np < n_i² (depletion region under reverse bias, the source of junction leakage current).
- U is largest when E_t ≈ E_i (n₁ = p₁ = n_i): **mid-gap traps are the most effective recombination centres.** Gold (E_t ≈ E_i) is therefore a powerful lifetime killer.
- **Low-level injection in n-type** (n ≈ n₀ ≫ p, n₁, p₁): U ≈ Δp/τ_p. The recombination rate is set by the minority-carrier lifetime τ_p = 1/(σ_p v_th N_t), which is inversely proportional to the trap density.

**Example.** N_t = 10¹³ cm⁻³, σ_p = 10⁻¹⁵ cm², v_th = 10⁷ cm/s: τ_p = 1/(10⁻¹⁵ × 10⁷ × 10¹³) = 10⁻⁵ s = **10 μs**.

## 12.5 Minority-carrier lifetime

If the generation source is switched off at t = 0, excess minority carriers decay exponentially (low-level injection, uniform sample):

    dΔp/dt = −Δp/τ_p   ⇒   Δp(t) = Δp(0) e^{−t/τ_p}

τ_p is the **minority-carrier lifetime**: the average time an excess minority carrier survives before recombining. Under steady generation G, Δp = Gτ_p.

Typical values: high-quality Si 1 μs to 1 ms; gold-doped Si for switching diodes about 1–10 ns; GaAs about 1–10 ns (fast radiative recombination).

Combined mechanisms add as rates: 1/τ = 1/τ_SRH + 1/τ_rad + 1/τ_Auger.

@fig figures/decay.svg | Photoconductive decay. After the light pulse ends, the excess carrier density falls to 1/e of its value in one lifetime.

---

## Exam questions solved

### Q42. What is meant by generation and recombination of charge carriers?

**Generation** is any process that creates free electron–hole pairs (or a free carrier from a dopant or trap) by giving an electron enough energy to move from the valence band (or a localised state) into the conduction band. The rate G is the number of pairs created per unit volume per unit time (cm⁻³s⁻¹). Mechanisms:

- **Thermal generation** by lattice vibrations, directly or through trap levels in the gap.
- **Optical generation** by absorption of photons with hν ≥ E_g (photodetectors, solar cells).
- **Impact ionisation** by energetic carriers in high fields (avalanche).
- **Tunnelling** generation at very high fields (Zener).

**Recombination** is the reverse: a conduction-band electron falls back to the valence band and fills a hole, so both carriers are annihilated. The released energy E_g appears as a photon, as heat (phonons), or as kinetic energy of a third carrier. The rate R has the same units. Mechanisms:

- **Direct (band-to-band, radiative)** recombination, emitting a photon; dominant in direct-gap materials.
- **Indirect (trap-assisted, SRH)** recombination through defect or impurity levels in the gap, releasing heat; dominant in Si.
- **Auger** recombination, energy given to a third carrier; dominant at high carrier density.
- **Surface** recombination through surface states.

**Equilibrium and non-equilibrium.** In thermal equilibrium the two processes balance (G_th = R_th), giving n₀p₀ = n_i². If excess carriers are introduced (np > n_i²), net recombination U = R − G > 0 restores equilibrium; if carriers are removed (np < n_i², e.g. a reverse-biased depletion region), net generation occurs. For low-level injection the net recombination rate is U = Δp/τ_p (n-type), where τ_p is the minority-carrier lifetime.

Generation and recombination govern the leakage current of diodes, the operation of solar cells, LEDs and photodetectors, the gain of BJTs and the switching speed of p-n junctions.

### Q43. Explain the Shockley-Read-Hall (SRH) recombination mechanism.

**Principle.** SRH (trap-assisted or indirect) recombination occurs through localised energy levels E_t in the forbidden gap introduced by crystal defects or impurities (e.g. Au, Fe, Cu, vacancies, dislocations). Instead of crossing the whole gap in one step, which in an indirect semiconductor requires an unlikely phonon-assisted transition, the electron makes two smaller steps via the trap, and the energy is released as lattice vibrations (phonons).

**The four processes** at a trap (density N_t, occupation probability f_t):

| Process | Description | Rate |
|---|---|---|
| (a) Electron capture | CB electron captured by an empty trap | r_a = v_thσ_n n N_t(1 − f_t) |
| (b) Electron emission | Trapped electron emitted to CB | r_b = e_n N_t f_t |
| (c) Hole capture | Trapped electron drops to VB, annihilating a hole | r_c = v_thσ_p p N_t f_t |
| (d) Hole emission | VB electron captured by empty trap, leaving a hole | r_d = e_p N_t(1 − f_t) |

**Recombination** = (a) then (c). **Generation** = (d) then (b).

**Derivation outline.** In steady state the trap occupation is constant, so the net electron capture rate equals the net hole capture rate: r_a − r_b = r_c − r_d = U. The emission coefficients follow from detailed balance in equilibrium: e_n = v_thσ_n n₁ and e_p = v_thσ_p p₁. Solving for f_t and substituting gives:

    U = (np − n_i²) / [ τ_p(n + n₁) + τ_n(p + p₁) ]

with τ_n = 1/(σ_n v_th N_t), τ_p = 1/(σ_p v_th N_t), n₁ = n_i e^{(E_t − E_i)/kT}, p₁ = n_i e^{(E_i − E_t)/kT}.

**Interpretation.**

1. The driving force is (np − n_i²): positive for excess carriers (recombination), negative for depletion (generation), zero in equilibrium.
2. U is maximum when E_t is near mid-gap (E_t ≈ E_i). Shallow levels near a band edge just re-emit carriers and are ineffective. **Deep, mid-gap levels are the effective recombination centres.**
3. U ∝ N_t: more traps give faster recombination and shorter lifetime.
4. For low-level injection in n-type material (n ≫ p, n₁, p₁): U = (p − p₀)/τ_p = Δp/τ_p. The rate is limited by capture of the minority carrier.
5. In a reverse-biased depletion region (n, p ≈ 0): U = −n_i/(τ_p + τ_n) ≈ −n_i/2τ₀, a net generation that produces the generation leakage current J_gen = qn_iW/2τ₀.

**Applications:** gold or platinum doping, or electron irradiation, is deliberately used to reduce lifetime in fast-switching diodes and thyristors. Conversely, gettering and clean processing reduce trap densities for long lifetimes in solar cells, CCDs and low-leakage devices.

### Q44. Define minority-carrier lifetime and explain its significance in semiconductor devices.

**Definition.** The minority-carrier lifetime is the average time an excess minority carrier exists in a semiconductor before it recombines with a majority carrier. For low-level injection, τ_p (holes in n-type) or τ_n (electrons in p-type) is defined by

    U = Δp / τ_p

so that, when generation stops, the excess density decays exponentially:

    Δp(t) = Δp(0) e^{−t/τ_p}

τ_p is the time for the excess to fall to 1/e (37 %) of its initial value. With SRH recombination, τ_p = 1/(σ_p v_th N_t): lifetime is inversely proportional to the trap density. Typical values: 1 ns to 1 ms in Si depending on purity.

**Significance:**

1. **Diffusion length.** Injected minority carriers diffuse an average distance L = √(Dτ) before recombining. In Si with D_p = 12 cm²/s and τ_p = 1 μs, L_p = √(12 × 10⁻⁶) = 35 μm. L determines how far carriers travel and therefore device dimensions.
2. **Diode current.** The saturation current J_s = qn_i²(D_p/(L_pN_D) + D_n/(L_nN_A)) depends on lifetime through L. Short lifetime raises leakage; generation current in the depletion region is ∝ 1/τ.
3. **Switching speed.** When a forward-biased diode is turned off, the stored minority charge Q = Iτ must be removed; the reverse-recovery time is ≈ τ. Fast-recovery and switching diodes are gold- or platinum-doped to cut τ to nanoseconds.
4. **BJT current gain.** Electrons injected into a p-type base must cross it before recombining. The base transport factor ≈ 1 − W_B²/2L_n², so long lifetime (L_n ≫ W_B) gives high β.
5. **Solar cells and photodetectors.** Photogenerated carriers must reach the junction before recombining; long lifetime (long L) means higher collection efficiency, current and efficiency.
6. **LEDs and lasers.** The radiative fraction of recombination, and the modulation speed (bandwidth ∝ 1/τ), depend on lifetime.
7. **Power devices.** In p-i-n diodes and IGBTs, long lifetime gives conductivity modulation and low on-state voltage but slow switching; there is a design trade-off.
8. **Material quality indicator.** Lifetime is very sensitive to metallic contamination, so it is measured (photoconductive decay, μ-PCD) to monitor crystal growth and process cleanliness.
