"""Per-page symbol and abbreviation tables.

Each page (week, answer key, laboratory) gets a section listing every symbol,
constant and abbreviation that appears on it, so no page relies on an earlier
one for definitions. Run after editing the pages; it replaces the section if
it is already there. The same entries make the course-wide glossary page.

    python3 tools/glossary.py
"""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
END = r"(?![A-Za-z0-9_{])"          # symbol must not continue into a longer one


def sym(pat):
    """Regex for a subscripted symbol such as E_F, also matching E_{F}."""
    base, sub = pat.split("_", 1)
    return re.escape(base) + r"_(?:" + re.escape(sub) + END + r"|\{" + re.escape(sub) + r"\})"


def word(w):
    return r"(?<![A-Za-z0-9-])" + re.escape(w) + r"(?![A-Za-z0-9])"


# (group, regex, symbol as written on the page, meaning, units / typical value)
G = []
def add(group, rx, shown, meaning, units):
    G.append((group, rx, shown, meaning, units))

C, S, A = "Constants", "Symbols", "Abbreviations"

# ---------------------------------------------------------------- constants
add(C, word("q") + r"|qV|qN|qD|qn|qp|qμ|q\(", "q", "Magnitude of the electronic charge", "1.6×10⁻¹⁹ C")
add(C, r"(?<![A-Za-z_])k(?=T|\s*=\s*8\.6|₀)|Boltzmann", "k", "Boltzmann constant", "8.617×10⁻⁵ eV/K = 1.381×10⁻²³ J/K")
add(C, r"(?<![A-Za-z_])kT(?!/q)", "kT", "Thermal energy", "0.0259 eV (often 0.02585 eV) at 300 K")
add(C, r"kT/q", "kT/q", "Thermal voltage", "0.0259 V (about 26 mV) at 300 K")
add(C, r"(?<![A-Za-z_])T(?=\s*=|\s*\(K\)| K|\^\{3/2\}|³ᐟ²| in K)|absolute temperature|temperature T", "T", "Absolute temperature", "kelvin (K); room temperature = 300 K")
add(C, r"(?<![A-Za-z_])h(?=ν|²| =|/2π|/p)|Planck", "h", "Planck constant", "6.626×10⁻³⁴ J·s")
add(C, r"ħ", "ħ", "Reduced Planck constant, h/2π", "1.055×10⁻³⁴ J·s")
add(C, r"m₀", "m₀", "Free-electron mass", "9.11×10⁻³¹ kg")
add(C, r"ε₀", "ε₀", "Permittivity of free space", "8.854×10⁻¹⁴ F/cm")
add(C, sym("ε_s") + "|" + sym("ε_si"), "ε_s (ε_si)", "Permittivity of silicon, 11.7ε₀", "1.04×10⁻¹² F/cm")
add(C, sym("ε_ox"), "ε_ox", "Permittivity of SiO₂, 3.9ε₀", "3.45×10⁻¹³ F/cm")
add(C, sym("ε_r"), "ε_r", "Relative permittivity (dielectric constant)", "Si 11.7, SiO₂ 3.9, GaAs 12.9")
add(C, r"(?<![A-Za-z_])eV(?![A-Za-z])", "eV", "Electron-volt, a unit of energy", "1 eV = 1.6×10⁻¹⁹ J")
add(C, r"Å", "Å", "Ångström, a unit of length", "1 Å = 10⁻¹⁰ m = 0.1 nm")
add(C, r"μm", "μm", "Micrometre (micron)", "1 μm = 10⁻⁴ cm = 10⁻⁶ m")

# ---------------------------------------------------------------- bands and statistics
add(S, sym("E_c") + "|" + sym("E_C"), "E_c (E_C)", "Energy of the bottom of the conduction band", "eV")
add(S, sym("E_v") + "|" + sym("E_V"), "E_v (E_V)", "Energy of the top of the valence band", "eV")
add(S, sym("E_g"), "E_g", "Band-gap energy, E_c − E_v", "eV; Si 1.12, Ge 0.66, GaAs 1.42 at 300 K")
add(S, sym("E_F") + r"|(?<![A-Za-z_])EF(?![A-Za-z_])|Fermi level", "E_F", "Fermi level: the energy at which a state has a 50 % chance of being occupied", "eV")
add(S, sym("E_i"), "E_i", "Intrinsic Fermi level, close to mid-gap", "eV")
add(S, sym("E_Fn") + "|" + sym("E_Fp"), "E_Fn, E_Fp", "Quasi-Fermi levels for electrons and holes, used out of equilibrium", "eV")
add(S, sym("E_D"), "E_D", "Donor energy level, just below E_c", "eV; E_c − E_D ≈ 0.045 eV for P in Si")
add(S, sym("E_A"), "E_A", "Acceptor energy level, just above E_v", "eV; E_A − E_v ≈ 0.045 eV for B in Si")
add(S, sym("E_t"), "E_t", "Energy level of a trap (recombination centre) in the gap", "eV")
add(S, sym("E_a"), "E_a", "Activation energy of dopant diffusion", "eV; about 3–4 eV")
add(S, sym("E_n"), "E_n", "Allowed energy of level n of a particle in a box", "J or eV")
add(S, r"f\(E\)|(?<![A-Za-z_])f(?= =| ≈)", "f(E)", "Fermi–Dirac function: probability that a state at energy E is occupied", "dimensionless, 0 to 1")
add(S, sym("g_c") + "|" + sym("g_v") + r"|g\(E\)", "g(E), g_c, g_v", "Density of states: allowed states per unit energy per unit volume", "states/(eV·cm³)")
add(S, sym("N_c"), "N_c", "Effective density of states in the conduction band", "cm⁻³; Si 2.8×10¹⁹ at 300 K")
add(S, sym("N_v"), "N_v", "Effective density of states in the valence band", "cm⁻³; Si 1.04×10¹⁹ at 300 K")
add(S, r"(?<![A-Za-z_])n(?= =| ≈| ≫|₀|\(x)", "n", "Electron concentration (free electrons per cm³)", "cm⁻³")
add(S, r"(?<![A-Za-z_])p(?= =| ≈| ≫|₀|\(x)", "p", "Hole concentration (holes per cm³)", "cm⁻³")
add(S, sym("n_i"), "n_i", "Intrinsic carrier concentration (n = p = n_i in pure material)", "cm⁻³; Si ≈ 1×10¹⁰ at 300 K")
add(S, r"n₀|p₀", "n₀, p₀", "Equilibrium electron and hole concentrations", "cm⁻³")
add(S, sym("p_n0") + "|" + sym("n_p0") + "|" + sym("n_n0") + "|" + sym("p_p0"), "p_n0, n_p0", "Equilibrium minority concentrations: holes on the n side, electrons on the p side", "cm⁻³; p_n0 = n_i²/N_D")
add(S, sym("N_D"), "N_D", "Donor concentration", "cm⁻³")
add(S, sym("N_A"), "N_A", "Acceptor concentration", "cm⁻³")
add(S, r"N_D⁺|N_A⁻", "N_D⁺, N_A⁻", "Concentrations of ionised donors and acceptors", "cm⁻³")
add(S, r"Δn|Δp", "Δn, Δp", "Excess electron and hole concentrations above equilibrium", "cm⁻³")
add(S, r"m∗|" + sym("m_n") + "|" + sym("m_p"), "m∗, m_n∗, m_p∗", "Effective mass of electrons or holes", "kg, or as a multiple of m₀")
add(S, r"ψ", "ψ", "Wave function (|ψ|² is the probability density)", "—")
add(S, r"(?<![A-Za-z_])V\(x\)|potential energy V", "V(x)", "Potential energy in the Schrödinger equation", "J or eV")
add(S, r"(?<![A-Za-z_])k(?= = 2π|a\)|²)|wave vector|ħk", "k (wave vector)", "Wave vector, 2π/λ; measures the electron's momentum, p = ħk", "m⁻¹ or cm⁻¹")
add(S, r"αa|(?<![A-Za-z_])α = √", "α (Kronig–Penney)", "√(2mE)/ħ, set by the electron energy", "m⁻¹")
add(S, r"(?<![A-Za-z_])P(?= = mV|·| sin)", "P (Kronig–Penney)", "Barrier strength mV₀ba/ħ²", "dimensionless")
add(S, r"V₀", "V₀", "Height of a potential barrier", "J or eV")
add(S, r"(?<![A-Za-z_])λ", "λ", "Wavelength", "μm or nm; λ(μm) = 1.24/E(eV)")
add(S, r"hν|(?<![A-Za-z_])ν(?![A-Za-z])", "ν, hν", "Frequency of light, and photon energy", "Hz; eV")

# ---------------------------------------------------------------- crystals
add(S, r"(?<![A-Za-z_])a(?= = 5|,? b,? c| \(Å\))|lattice constant", "a", "Lattice constant: edge length of the cubic unit cell", "Å; Si 5.43, Ge and GaAs 5.65")
add(S, r"\(h k l\)|\{h k l\}", "(h k l), {h k l}", "Miller indices of a plane; family of equivalent planes", "integers")
add(S, r"\[u v w\]|⟨u v w⟩", "[u v w], ⟨u v w⟩", "A crystal direction; family of equivalent directions", "integers")
add(S, sym("d_hkl") + r"|d₁|d₂|d₃", "d_hkl", "Spacing between neighbouring (h k l) planes, a/√(h² + k² + l²)", "Å")
add(S, sym("r_nn"), "r_nn", "Nearest-neighbour distance", "Å; Si 2.35")

# ---------------------------------------------------------------- growth and doping
add(S, sym("k_0") + r"|k₀", "k₀", "Segregation coefficient, C_s/C_l at the freezing interface", "dimensionless; B 0.8, P 0.35")
add(S, sym("C_s"), "C_s", "Surface concentration of a diffusion (or solid concentration when freezing)", "cm⁻³")
add(S, sym("C_l") + r"|C₀", "C_l, C₀", "Concentration in the melt (liquid); C₀ at the start", "cm⁻³")
add(S, r"(?<![A-Za-z_])f(?= \(|the fraction| =\s*0\.)|fraction already", "f (growth)", "Fraction of the melt already solidified", "0 to 1")
add(S, r"(?<![A-Za-z_])C\(x|dC/dx|(?<![A-Za-z_])C(?= =)", "C(x, t)", "Dopant concentration at depth x and time t", "cm⁻³")
add(S, r"(?<![A-Za-z_])D(?= =| ≈|₀|\(| ∂| d)|D/μ|√\(Dt\)|√\(2Dt\)|πDt", "D", "Diffusion coefficient (dopants in a furnace, or carriers)", "cm²/s")
add(S, r"D₀", "D₀", "Diffusion constant in D = D₀e^{−E_a/kT}", "cm²/s")
add(S, r"(?<![A-Za-z_])J(?= = −D)|dopant flux", "J (Fick)", "Dopant flux: atoms crossing 1 cm² per second", "atoms/(cm²·s)")
add(S, r"(?<![A-Za-z_])F(?= = −D)", "F", "Particle flux in Fick's law", "particles/(cm²·s)")
add(S, r"(?<![A-Za-z_])Q(?= =| /|\)|,| \(dose| is| =)|dose Q", "Q", "Dose: dopant atoms per unit area (in Weeks 13–14, Q also means charge)", "atoms/cm² (C or C/cm² for charge)")
add(S, r"(?<![A-Za-z_])Φ(?= = |\s*\(dose|/)", "Φ (dose)", "Implanted dose (ions per cm²)", "cm⁻²")
add(S, r"erfc", "erfc", "Complementary error function, erfc(u) = 1 − erf(u); read from a table", "dimensionless")
add(S, sym("x_j"), "x_j", "Junction depth: where the dopant concentration equals the background", "μm")
add(S, sym("N_B") + "|" + sym("C_B"), "N_B (C_B)", "Background doping of the wafer (in Week 13, N_B is the base doping)", "cm⁻³")
add(S, sym("R_p"), "R_p", "Projected range: average depth at which implanted ions stop", "μm")
add(S, r"ΔR_p|ΔR_\{p\}", "ΔR_p", "Straggle: spread of the implanted ions' stopping depths", "μm")
add(S, sym("N_p"), "N_p", "Peak concentration of an implanted profile", "cm⁻³")
add(S, sym("S_n") + "|" + sym("S_e"), "S_n, S_e", "Nuclear and electronic stopping power of an implanted ion", "eV·cm²")
add(S, sym("N_Si"), "N_Si", "Atom density of silicon", "5×10²² cm⁻³")
add(S, sym("R_s"), "R_s", "Sheet resistance (or diode series resistance in Week 12)", "Ω/□ (ohms per square); Ω")
add(S, sym("x_mask"), "x_mask", "Thickness of an implant mask", "μm")

# ---------------------------------------------------------------- transport
add(S, r"(?<![A-Za-z_])E(?= = V| \(V/cm\)|_max|·|\s*=\s*1000)|electric field E|field E", "E (field)", "Electric field (on band diagrams, E is energy instead)", "V/cm")
add(S, r"μ(?![_m])|" + sym("μ_n") + "|" + sym("μ_p"), "μ, μ_n, μ_p", "Mobility: drift velocity per unit field (electrons, holes)", "cm²/(V·s); Si μ_n 1350, μ_p 480")
add(S, sym("μ_L") + "|" + sym("μ_I"), "μ_L, μ_I", "Mobility limited by lattice scattering, by ionised-impurity scattering", "cm²/(V·s)")
add(S, sym("v_d") + "|" + sym("v_dn") + "|" + sym("v_dp"), "v_d", "Drift velocity", "cm/s")
add(S, sym("v_th"), "v_th", "Thermal velocity of carriers", "≈ 10⁷ cm/s at 300 K")
add(S, sym("v_sat"), "v_sat", "Saturation velocity at high field", "≈ 10⁷ cm/s in Si")
add(S, sym("τ_m"), "τ_m", "Mean free time between collisions", "s; about 0.1–1 ps")
add(S, r"(?<![A-Za-z_])σ(?![_])", "σ", "Conductivity, q(nμ_n + pμ_p) (in Week 8, σ is also a capture cross-section)", "S/cm (siemens per cm)")
add(S, r"(?<![A-Za-z_])ρ(?![_])", "ρ", "Resistivity, 1/σ", "Ω·cm")
add(S, sym("J_n") + "|" + sym("J_p") + r"|(?<![A-Za-z_])J(?= = q| = σ| ≈)", "J, J_n, J_p", "Current density (total, electrons, holes)", "A/cm²")
add(S, sym("D_n") + "|" + sym("D_p"), "D_n, D_p", "Diffusion coefficients of electrons and holes", "cm²/s; Si 35 and 12.4")
add(S, sym("R_H") + "|" + sym("V_H") + "|" + sym("B_z"), "R_H, V_H, B", "Hall coefficient, Hall voltage, magnetic flux density", "cm³/C; V; T (Wb/m²)")
add(S, sym("T_e"), "T_e", "Electron temperature of hot carriers", "K")

# ---------------------------------------------------------------- recombination
add(S, r"(?<![A-Za-z_])G(?![a-zA-Z_])|" + sym("G_L") + "|" + sym("G_p") + "|" + sym("G_n") + "|" + sym("G_th"), "G, G_L", "Generation rate of electron–hole pairs (G_L: by light)", "cm⁻³s⁻¹")
add(S, r"(?<![A-Za-z_])R(?= =|_p|_n|·)|" + sym("R_th"), "R", "Recombination rate", "cm⁻³s⁻¹")
add(S, r"(?<![A-Za-z_])U(?= =| ≈|_s)", "U", "Net recombination rate, R − G", "cm⁻³s⁻¹")
add(S, r"τ(?![_m])|" + sym("τ_n") + "|" + sym("τ_p") + "|" + sym("τ_eff") + "|" + sym("τ_bulk"), "τ, τ_n, τ_p", "Minority-carrier lifetime (τ_eff: effective, including surfaces)", "s; Si 1 ns – 1 ms")
add(S, sym("N_t"), "N_t", "Density of traps (recombination centres)", "cm⁻³")
add(S, sym("σ_n") + "|" + sym("σ_p"), "σ_n, σ_p", "Capture cross-section of a trap for electrons, holes", "cm²")
add(S, r"n₁|p₁", "n₁, p₁", "SRH parameters n_ie^{(E_t − E_i)/kT} and n_ie^{(E_i − E_t)/kT}", "cm⁻³")
add(S, sym("L_n") + "|" + sym("L_p") + r"|(?<![A-Za-z_])L = √", "L, L_n, L_p", "Diffusion length √(Dτ): distance a minority carrier travels before recombining", "μm or cm")
add(S, r"(?<![A-Za-z_])S(?= =|Δ| \()|surface recombination velocity", "S", "Surface recombination velocity", "cm/s")
add(S, sym("N_st"), "N_st", "Density of surface traps", "cm⁻²")
add(S, sym("U_s"), "U_s", "Recombination rate per unit area at a surface", "cm⁻²s⁻¹")

# ---------------------------------------------------------------- junctions and contacts
add(S, sym("V_bi"), "V_bi", "Built-in potential of a junction or Schottky contact", "V; typically 0.5–1 V")
add(S, sym("V_a") + r"|(?<![A-Za-z_])V(?= > 0| < 0| =)", "V, V_a", "Applied voltage (positive for forward bias)", "V")
add(S, r"(?<![A-Za-z_])W(?= =| ≈|₀| \(|\))|depletion width W", "W", "Depletion-region width (in Week 13 W_B, W_E are base and emitter widths; in Week 14 W is channel width)", "μm or cm")
add(S, sym("x_n") + "|" + sym("x_p"), "x_n, x_p", "Parts of the depletion region on the n side and on the p side", "μm")
add(S, sym("E_max"), "E_max", "Peak electric field, at the junction", "V/cm")
add(S, sym("I_s") + "|" + sym("J_s") + "|" + sym("I_S"), "I_s, J_s (I_S)", "Saturation current (density) of a diode or transistor", "A; A/cm²")
add(S, r"(?<![A-Za-z_])I(?= =| ≈| \()|I-V", "I", "Current", "A")
add(S, r"(?<![A-Za-z_])A(?= =| \(| is the)|area A|diode area", "A (area)", "Device or contact area", "cm²")
add(S, r"η", "η", "Ideality factor of a diode, 1 (ideal) to 2", "dimensionless")
add(S, sym("C_j") + r"|(?<![A-Za-z_])C(?= = ε)|1/C²", "C, C_j", "Capacitance (junction or depletion capacitance)", "F (pF = 10⁻¹² F)")
add(S, sym("V_BR"), "V_BR", "Breakdown voltage", "V")
add(S, sym("Φ_m"), "Φ_m", "Work function of a metal", "eV; Al 4.28, Au 5.1")
add(S, sym("Φ_s"), "Φ_s", "Work function of a semiconductor, χ + (E_c − E_F)", "eV")
add(S, r"χ", "χ", "Electron affinity: energy from E_c up to the vacuum level", "eV; Si 4.05")
add(S, sym("Φ_B") + "|" + sym("Φ_Bp"), "Φ_B", "Schottky barrier height seen from the metal", "eV (or V)")
add(S, r"A∗∗", "A∗∗", "Effective Richardson constant", "A/(cm²·K²); n-Si ≈ 110")
add(S, sym("ρ_c"), "ρ_c", "Specific contact resistance", "Ω·cm²")
add(S, sym("E_vac") + r"|vacuum level", "E_vac", "Vacuum level: energy of an electron just free of the material", "eV")

# ---------------------------------------------------------------- BJT
add(S, sym("I_E") + "|" + sym("I_B") + "|" + sym("I_C"), "I_E, I_B, I_C", "Emitter, base and collector currents", "A (mA)")
add(S, sym("V_BE") + "|" + sym("V_CE") + "|" + sym("V_CB"), "V_BE, V_CE, V_CB", "Base–emitter, collector–emitter and collector–base voltages", "V")
add(S, r"angles α, β, γ", "α, β, γ (cell)", "Angles between the edges of a unit cell", "degrees; 90° for cubic")
add(S, r"(?<![A-Za-z_])(?<!angles )α(?![_a-z,])", "α", "Common-base current gain, I_C/I_E", "dimensionless; 0.98–0.999")
add(S, r"(?<![A-Za-z_])(?<!α, )β(?![_a-z])", "β", "Common-emitter current gain, I_C/I_B (also h_FE)", "dimensionless; 50–500")
add(S, r"(?<![A-Za-z_])(?<!β, )γ(?= = 1/| =|,| ≈|\))|injection efficiency", "γ (BJT)", "Emitter injection efficiency", "dimensionless, close to 1")
add(S, sym("α_T"), "α_T", "Base transport factor", "dimensionless, close to 1")
add(S, sym("N_E") + "|" + sym("W_E") + "|" + sym("D_E") + "|" + sym("W_B") + "|" + sym("D_B"), "N_E, W_E, D_E; N_B, W_B, D_B", "Doping, width and minority diffusion coefficient of the emitter; of the base", "cm⁻³; μm; cm²/s")
add(S, sym("V_A") + "|Early voltage", "V_A", "Early voltage", "V")
add(S, sym("r_o"), "r_o", "Output resistance", "Ω")
add(S, sym("τ_B"), "τ_B", "Base transit time, W_B²/2D_n", "s")
add(S, sym("f_T"), "f_T", "Transition (cut-off) frequency", "Hz")

# ---------------------------------------------------------------- MOS
add(S, sym("C_ox"), "C_ox", "Gate-oxide capacitance per unit area, ε_ox/t_ox", "F/cm²")
add(S, sym("t_ox"), "t_ox", "Gate-oxide thickness", "nm")
add(S, sym("φ_F") + "|" + sym("ψ_s") + "|" + sym("φ_s"), "φ_F, ψ_s (φ_s)", "Bulk Fermi potential (kT/q)ln(N_A/n_i); surface potential (band bending)", "V")
add(S, sym("W_d") + "|" + sym("W_dmax") + "|" + sym("Q_dmax"), "W_d, W_dmax, Q_dmax", "MOS depletion width, its maximum at inversion, and the depletion charge then", "μm; C/cm²")
add(S, sym("V_T") + "|" + sym("V_th"), "V_T (V_th)", "Threshold voltage of a MOSFET", "V")
add(S, sym("V_FB"), "V_FB", "Flat-band voltage", "V")
add(S, sym("Φ_ms") + "|" + sym("Q_f"), "Φ_ms, Q_f", "Gate–substrate work-function difference; fixed oxide charge", "V; C/cm²")
add(S, r"(?<![A-Za-z_])γ(?= = √| V\^|√)|body-effect", "γ (MOSFET)", "Body-effect coefficient √(2qε_siN_A)/C_ox", "V^{1/2}")
add(S, sym("V_GS") + "|" + sym("V_DS") + "|" + sym("V_SB") + "|" + sym("V_G") + "|" + sym("V_GD"), "V_GS, V_DS, V_SB, V_G", "Gate–source, drain–source, source–body and gate voltages", "V")
add(S, sym("I_D"), "I_D", "Drain current", "A (mA)")
add(S, r"W/L", "W/L", "Channel width-to-length ratio", "dimensionless")
add(S, sym("g_m"), "g_m", "Transconductance, ∂I_D/∂V_GS", "S (A/V)")
add(S, r"(?<![A-Za-z_])k(?= = μ| =\s*\d.*mA/V)|μ_nC_ox\(W/L\)", "k (MOSFET)", "Device parameter μ_nC_ox(W/L)", "A/V² (mA/V²)")
add(S, r"(?<![A-Za-z_])λ(?=V|I)", "λ (MOSFET)", "Channel-length modulation parameter", "V⁻¹")

# ---------------------------------------------------------------- added after checking every page
add(S, sym("λ_max"), "λ_max", "Longest wavelength a material absorbs, 1.24/E_g (μm, E_g in eV)", "μm")
add(S, sym("σ_i") + "|" + sym("σ_intrinsic") + "|" + sym("ρ_i") + "|" + sym("σ_doped"), "σ_i, ρ_i", "Conductivity and resistivity of intrinsic (undoped) material; σ_doped after doping", "S/cm; Ω·cm")
add(S, sym("a_layer") + "|" + sym("a_sub"), "a_layer, a_sub", "Lattice constants of the grown layer and of the substrate", "Å")
add(S, sym("N_total"), "N_total", "Total number of dopant atoms in a region", "atoms")
add(S, sym("ψ_k") + "|" + sym("u_k"), "ψ_k(x), u_k(x)", "Bloch wavefunction of an electron, and its part that repeats with the lattice", "—")
add(S, sym("F_n") + "|" + sym("F_p"), "F_n, F_p", "Particle flux of electrons and holes (carriers crossing 1 cm² per second)", "cm⁻²s⁻¹")
add(S, sym("B_z") + "|" + sym("I_x") + "|Hall (?:effect|voltage)", "B_z, I_x, V_H", "Hall effect: magnetic field (z), current (x) and Hall voltage", "T (tesla); A; V")
add(S, sym("R_H"), "R_H", "Hall coefficient, 1/qp (p-type) or −1/qn (n-type)", "cm³/C")
add(S, sym("v_dn") + "|" + sym("v_dp"), "v_dn, v_dp", "Drift velocity of electrons and holes", "cm/s")
add(S, sym("μ_i") + "|" + sym("τ_i") + "|" + sym("μ_I") + "|" + sym("μ_L") + "|" + sym("N_I"), "μ_i, τ_i (μ_L, μ_I, N_I)", "Mobility and scattering time for one scattering mechanism (L: lattice, I: ionised impurity); N_I = ionised-impurity density", "cm²/(V·s); s; cm⁻³")
add(S, sym("J_drift") + r"|J_\{[np],diff\}|" + sym("J_diff"), "J_drift, J_diff", "Drift and diffusion parts of the current density", "A/cm²")
add(S, sym("E_sat"), "E_sat", "Field at which the drift velocity saturates, v_sat/μ", "V/cm")
add(S, sym("G_th") + "|" + sym("R_th"), "G_th, R_th", "Thermal generation and recombination rates (equal in equilibrium)", "cm⁻³s⁻¹")
add(S, sym("G_n") + "|" + sym("G_p") + "|" + sym("R_n") + "|" + sym("R_p"), "G_n, G_p, R_n, R_p", "Generation and recombination rates of electrons and holes", "cm⁻³s⁻¹")
add(S, sym("f_t") + "|" + sym("e_n") + "|" + sym("e_p"), "f_t, e_n, e_p", "Probability a trap is occupied by an electron; emission rates of electrons and holes from traps", "dimensionless; s⁻¹")
add(S, sym("r_a") + "|" + sym("r_b"), "r_a, r_b, r_c, r_d", "SRH rates: electron capture, electron emission, hole capture, hole emission", "cm⁻³s⁻¹")
add(S, sym("τ_SRH") + "|" + sym("τ_radiative") + r"|τ_\{Auger\}", "τ_SRH, τ_radiative, τ_Auger", "Lifetimes set by trap (SRH), radiative and Auger recombination", "s")
add(S, sym("τ_bulk") + "|" + sym("τ_surface") + "|" + sym("τ_b"), "τ_b (τ_bulk), τ_surface", "Lifetime from bulk recombination only; from surface recombination only", "s")
add(S, sym("U_s") + "|" + sym("p_s") + "|" + sym("Δp_s"), "U_s, p_s, Δp_s", "Surface recombination rate; hole density and excess at the surface", "cm⁻²s⁻¹; cm⁻³")
add(S, sym("n_n0") + "|" + sym("p_p0") + "|" + sym("p_n0") + "|" + sym("n_p0"), "n_n0, p_p0, p_n0, n_p0", "Equilibrium densities: majority (n_n0, p_p0) and minority (p_n0 holes on n side, n_p0 electrons on p side)", "cm⁻³")
add(S, sym("Δp_n") + "|" + sym("Δn_p"), "Δp_n, Δn_p", "Excess minority carriers at the depletion edges (holes on n side, electrons on p side)", "cm⁻³")
add(S, sym("R_c"), "R_c", "Contact resistance", "Ω (specific: Ω·cm²)")
add(S, r"Φ_\{Bp\}|" + sym("Φ_Bn"), "Φ_Bn, Φ_Bp", "Schottky barrier height for electrons (n-type) and for holes (p-type)", "eV")
add(S, sym("V_junction"), "V_junction", "Part of the applied voltage that appears across the junction itself", "V")
add(S, r"I_\{[CE],[np]\}", "I_{E,n}, I_{E,p}, I_{C,n}", "Electron and hole parts of the emitter and collector currents", "A")
add(S, sym("n_B") + "|" + sym("p_E") + "|" + sym("n_C"), "n_B(x)", "Minority-electron density in the base of an NPN transistor", "cm⁻³")
add(S, sym("I_gen") + "|" + sym("J_gen"), "I_gen, J_gen", "Generation current (density) from carriers generated in the depletion region", "A; A/cm²")
add(S, r"(?<![A-Za-z_])p_n(?![0-9A-Za-z_])|(?<![A-Za-z_])n_p(?![0-9A-Za-z_])", "p_n, n_p", "Minority-carrier density: holes on the n side, electrons on the p side", "cm⁻³")
add(S, r"ΔI_D|ΔV_GS", "ΔI_D, ΔV_GS", "Small changes in drain current and gate voltage (their ratio is g_m)", "A; V")
add(S, sym("Q_charge"), "Q_charge", "Total charge delivered by the ion beam, I × t", "C")
add(S, r"ΔV_T", "ΔV_T", "Shift in threshold voltage (e.g. from body bias)", "V")

# ---------------------------------------------------------------- abbreviations
for w, m in [
 ("Si", "Silicon"), ("Ge", "Germanium"), ("GaAs", "Gallium arsenide"), ("GaN", "Gallium nitride"),
 ("SiC", "Silicon carbide"), ("InP", "Indium phosphide"), ("GaP", "Gallium phosphide"), ("SiO₂", "Silicon dioxide (silica), the oxide insulator"),
 ("CB", "Conduction band"), ("VB", "Valence band"), ("FCC", "Face-centred cubic lattice"), ("BCC", "Body-centred cubic lattice"),
 ("SC", "Simple cubic lattice"), ("APF", "Atomic packing factor"), ("III–V", "Compound of Group III and Group V elements (e.g. GaAs)"),
 ("MG-Si", "Metallurgical-grade silicon (≈ 98 % pure)"), ("EG-Si", "Electronic-grade silicon (99.9999999 % or better)"),
 ("CZ", "Czochralski crystal growth"), ("FZ", "Float-zone crystal growth"), ("CVD", "Chemical vapour deposition"),
 ("VPE", "Vapour-phase epitaxy"), ("LPE", "Liquid-phase epitaxy"), ("MBE", "Molecular-beam epitaxy"),
 ("MOCVD", "Metal-organic chemical vapour deposition"), ("UHV", "Ultra-high vacuum (≈ 10⁻¹⁰ Torr)"),
 ("RHEED", "Reflection high-energy electron diffraction (counts atomic layers during MBE)"),
 ("RTA", "Rapid thermal annealing"), ("SIMS", "Secondary-ion mass spectrometry"), ("TLM", "Transmission-line method (contact resistance)"),
 ("SRH", "Shockley–Read–Hall (trap-assisted) recombination"), ("LDD", "Lightly doped drain"),
 ("I-V", "Current–voltage (measurement or characteristic)"), ("C-V", "Capacitance–voltage (measurement or characteristic)"),
 ("LCR", "Inductance–capacitance–resistance meter"), ("SMU", "Source-measure unit"), ("MOS", "Metal–oxide–semiconductor"),
 ("MOSFET", "Metal–oxide–semiconductor field-effect transistor"), ("CMOS", "Complementary MOS (n- and p-channel MOSFETs together)"),
 ("FET", "Field-effect transistor"), ("JFET", "Junction field-effect transistor"), ("MESFET", "Metal–semiconductor field-effect transistor"),
 ("HEMT", "High-electron-mobility transistor"), ("BJT", "Bipolar junction transistor"), ("HBT", "Heterojunction bipolar transistor"),
 ("NPN", "BJT with n-type emitter, p-type base, n-type collector"), ("PNP", "BJT with p-type emitter, n-type base, p-type collector"),
 ("E–B", "Emitter–base (junction)"), ("C–B", "Collector–base (junction)"),
 ("IC", "Integrated circuit"), ("VLSI", "Very-large-scale integration"), ("LED", "Light-emitting diode"),
 ("RF", "Radio frequency"), ("IGBT", "Insulated-gate bipolar transistor"), ("MEMS", "Micro-electro-mechanical systems"),
 ("CAT", "Continuous Assessment Test"), ("PGD", "Postgraduate Diploma"), ("DC", "Direct current (steady)"), ("AC", "Alternating current (small signal)"),
 ("n⁺", "Very heavily doped n-type (similarly p⁺)"), ("LCM", "Lowest common multiple"), ("LHS", "Left-hand side (of an equation)"), ("MATLAB", "A numerical computing program (alternative to Python)"),
 ("KOH", "Potassium hydroxide (an anisotropic silicon etchant)"), ("UV", "Ultraviolet"), ("IR", "Infrared"),
 ("VCSEL", "Vertical-cavity surface-emitting laser"), ("PCD", "Photoconductive decay (lifetime measurement)"),
 ("TCAD", "Technology computer-aided design (device simulation software)"), ("FD", "Fermi–Dirac (distribution)"),
]:
    rx = (r"(?<![A-Za-z0-9])" + re.escape(w) + r"s?(?![A-Za-z0-9₂_])") if w not in ("n⁺",) else r"n⁺|p⁺"
    add(A, rx, w, m, "")

SECTION = "## Symbols and abbreviations used this week"
SECTION_OTHER = "## Symbols and abbreviations used on this page"
INTRO = ("Every symbol, constant and abbreviation on this page is listed here, even if an earlier week "
         "already defined it, so you can study this page on its own.")


def table(rows, units=True):
    if units:
        out = ["| Symbol | Meaning | Units / typical value |", "|---|---|---|"]
        out += [f"| {s} | {m} | {u} |" for s, m, u in rows]
    else:
        out = ["| Abbreviation | Meaning |", "|---|---|"]
        out += [f"| {s} | {m} |" for s, m, u in rows]
    return "\n".join(out)


def build_section(text, heading):
    body = re.sub(r"^## Symbols and abbreviations used.*?(?=^## (?!Symbols and)|^---\n|\Z)", "", text, flags=re.S | re.M)
    found = {C: [], S: [], A: []}
    for grp, rx, shown, meaning, units in G:
        if re.search(rx, body):
            found[grp].append((shown.replace("|", "\\|"), meaning.replace("|", "\\|"), units))
    parts = [heading, "", INTRO, ""]
    if found[C]:
        parts += ["**Constants and units**", "", table(found[C]), ""]
    if found[S]:
        parts += ["**Symbols**", "", table(found[S]), ""]
    if found[A]:
        parts += ["**Abbreviations**", "", table(found[A], units=False), ""]
    return "\n".join(parts) + "\n", sum(len(v) for v in found.values())


def place(path):
    s = open(path, encoding="utf-8").read()
    s = re.sub(r"^## Symbols and abbreviations used.*?(?=^## (?!Symbols and)|^---\n|\Z)", "", s, flags=re.S | re.M)
    heading = SECTION if os.path.basename(path)[3:7] == "week" else SECTION_OTHER
    sec, n = build_section(s, heading)
    m = re.search(r"^## Learning objectives.*?(?=^## )", s, flags=re.S | re.M)
    if m:
        i = m.end()
    else:                       # pages without objectives: after the opening paragraph
        m2 = re.search(r"^# [^\n]+\n(?:<!--[^\n]*-->\n)?\n[^\n]+\n\n", s, flags=re.M)
        i = m2.end()
    s = s[:i] + sec + "\n" + s[i:]
    open(path, "w", encoding="utf-8").write(s)
    return n


def glossary_page():
    lines = ["# Glossary — Symbols, Constants and Abbreviations", "<!-- group: Revision & Practicals -->", "",
             "Every symbol, constant and abbreviation used anywhere in the course, with its meaning and units. "
             "Each week also has its own shorter table near the top, listing only what that week uses.", ""]
    for grp, title in ((C, "Constants and units"), (S, "Symbols"), (A, "Abbreviations")):
        rows = [(s.replace("|", "\\|"), m.replace("|", "\\|"), u) for g, rx, s, m, u in G if g == grp]
        lines += [f"## {title}", "", table(rows, units=(grp != A)), ""]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    pages = sorted(glob.glob(os.path.join(ROOT, "[0-1][0-9]-*.md")))
    for p in pages:
        if os.path.basename(p).startswith("00-") or "glossary" in p:
            continue
        print(os.path.basename(p)[:40], place(p))
    open(os.path.join(ROOT, "18-glossary.md"), "w", encoding="utf-8").write(glossary_page())
    print("18-glossary.md", len(G), "entries")
