# Week 14 — Field-Effect Transistors (MOSFETs)
<!-- group: Module 5 · Advanced Device Technology -->

**Plan:** ideal MOS capacitor physics (accumulation, depletion, inversion); MOSFET threshold voltage; linear and saturation operating regions. This page follows your lecturer's note (sections 14.1–14.17) and solves its review questions 9–17.

## Learning objectives

By the end of this week you should be able to:

1. Describe the structure of an ideal MOS capacitor and calculate C_ox.
2. Explain accumulation, depletion and inversion.
3. Explain how a MOS capacitor becomes a MOSFET, and enhancement versus depletion mode.
4. Define the threshold voltage and calculate it.
5. Determine the operating region and calculate drain current.
6. Compare BJTs and MOSFETs.

## The big picture

A BJT is controlled by a current. A MOSFET is controlled by a **voltage**, and the control works through an electric field, without any current flowing into the control terminal.

The idea: put a metal plate (the **gate**) just above the silicon surface, separated by a very thin insulator. Put a positive voltage on the plate, and it attracts electrons to the silicon surface just beneath it, the same way a charged comb attracts bits of paper. With enough voltage, those electrons form a thin conducting sheet, a **channel**, connecting two contacts (source and drain). Remove the voltage and the channel disappears. The gate switches the channel on and off, and nothing flows into the gate. That is why billions of MOSFETs can sit on one chip without melting it.

## 14.1 Introduction to MOSFETs

A **metal-oxide-semiconductor field-effect transistor (MOSFET)** is a voltage-controlled semiconductor device. The **gate voltage** controls the conductivity of a channel between the **source** and **drain** terminals. The gate is separated from the semiconductor by a thin insulating oxide layer, so ideally the DC gate current is essentially zero.

The basic MOS structure is:

    gate (metal or polysilicon) / oxide (SiO₂ insulator) / semiconductor substrate

In an **n-channel** MOSFET the substrate is normally **p-type**, and an **electron inversion layer** forms when the gate voltage is sufficiently positive. In a **p-channel** MOSFET the polarities are reversed: n-type substrate, hole inversion layer, negative gate voltage.

## 14.2 The ideal MOS capacitor

A MOS capacitor can be viewed as a **parallel-plate capacitor**: one plate is the gate, the other is the semiconductor surface, and the oxide is the dielectric between them. The gate voltage creates an electric field through the oxide and changes the distribution of charge near the semiconductor surface.

    C_ox = ε_ox / t_ox

| Symbol | Meaning |
|---|---|
| C_ox | oxide capacitance per unit area (F/cm²) |
| ε_ox | oxide permittivity, ε_ox = ε_r ε₀ with ε_r ≈ 3.9 for SiO₂: ε_ox = 3.45×10⁻¹³ F/cm |
| t_ox | oxide thickness |

A **thinner oxide** gives a larger capacitance per unit area, so the same gate voltage induces more charge: stronger electrostatic control of the channel. For t_ox = 10 nm = 10⁻⁶ cm, C_ox = 3.45×10⁻¹³/10⁻⁶ = 3.45×10⁻⁷ F/cm².

"**Ideal**" means: no charge trapped in the oxide, no trap states at the interface, no difference between the gate and semiconductor work functions, and an oxide that conducts no current at all.

For the p-type substrate we also need the **bulk Fermi potential** φ_F, which is how far the Fermi level lies below the intrinsic level in the bulk (from Week 5, E_i − E_F = kT ln(N_A/n_i)):

    φ_F = (kT/q) ln(N_A/n_i)

For N_A = 10¹⁷ cm⁻³: φ_F = 0.0259 ln(10⁷) = 0.417 V.

## 14.3 Accumulation

Take a p-type silicon substrate and apply a **negative** gate voltage relative to it. The negative gate attracts the positive majority carriers, **holes**, towards the semiconductor–oxide interface. The surface now contains more holes than it does in equilibrium. This is **accumulation**.

- p-type substrate + negative gate voltage → hole accumulation.
- The surface majority-carrier concentration increases.
- The surface becomes more strongly p-type.
- In the band diagram the bands bend **upward** at the surface (E_v moves closer to E_F).

## 14.4 Depletion

Apply a **small positive** gate voltage. Holes are now **repelled** from the surface. The region near the oxide is depleted of mobile majority carriers. What remains is the fixed negative charge of the **ionised acceptor atoms**, which cannot move. This is the **depletion region**.

- p-type substrate + moderately positive gate voltage → depletion.
- Mobile holes are pushed away from the surface.
- A negative space-charge region of ionised acceptors remains, of width W_d.
- The bands bend **downward** at the surface by the surface potential ψ_s.

The depletion width grows with the band bending:

    W_d = √( 2ε_si ψ_s / qN_A )

## 14.5 Inversion

As the positive gate voltage is increased further, the surface potential becomes positive enough to attract **electrons** (the minority carriers of the p-type substrate) towards the surface. When the electron concentration at the surface becomes large enough that the surface behaves as **n-type**, the semiconductor is said to be **inverted**. This is **inversion**.

For an ideal p-type substrate, **strong inversion** is conventionally defined as the point where the surface is as strongly n-type as the bulk is p-type. That happens when the band bending is twice the bulk Fermi potential:

    ψ_s ≈ 2φ_F

Why 2φ_F? In the bulk, E_F is φ_F below E_i. Bending the bands down by φ_F brings E_i down to E_F (the surface is intrinsic). Bending by another φ_F puts E_i φ_F *below* E_F, which is exactly the mirror image of the bulk: n-type to the same degree.

Once strong inversion is reached, the depletion width stops growing at its maximum

    W_dmax = √( 4ε_si φ_F / qN_A )

and any further gate voltage simply adds electrons to the inversion layer. **This electron layer is the channel of the MOSFET.**

The exact sign conventions for φ_F and ψ_s differ between textbooks. The physical idea is what matters: the gate field first **depletes** the surface, then attracts minority carriers until an **inversion layer** forms.

@fig figures/mos-states.svg | Band diagrams of an ideal MOS capacitor on p-type silicon. Accumulation: bands bend up and holes gather at the surface. Depletion: bands bend down and holes are pushed away, leaving negative acceptor ions. Inversion: the bands bend so far that the surface becomes n-type.

## 14.6 From MOS capacitor to MOSFET

In an **n-channel enhancement MOSFET**, two heavily doped **n⁺ regions** form the **source** and **drain** inside a p-type substrate. The gate lies above the region between them, which has length L (channel length) and width W.

- With V_GS below threshold there is no channel. Source and drain are two n⁺ islands in p-type silicon, i.e. two back-to-back p-n junctions: no current flows.
- With a sufficiently positive gate-to-source voltage, an electron inversion channel forms and connects source to drain.
- Applying a drain-to-source voltage V_DS then makes electrons **drift** from source to drain. Conventional drain current flows from drain to source.

The gate voltage controls whether the channel exists and how strongly it conducts. This is the fundamental reason the MOSFET is a **field-effect** device.

**Enhancement and depletion mode.** In an **enhancement-mode** device (the normal kind) there is no channel at V_GS = 0; a gate voltage above V_T must be applied to create (enhance) one. A **depletion-mode** device is built with a channel already present at V_GS = 0 (by doping the surface n-type); a negative gate voltage is needed to remove (deplete) it, so its V_T is negative.

## 14.7 Threshold voltage

The **threshold voltage** V_T is the gate-to-source voltage at which a strong inversion channel forms and significant conduction begins in an enhancement-mode MOSFET.

A commonly used long-channel expression for an ideal nMOS is:

    V_T = V_FB + 2φ_F + γ √(2φ_F)

with the **body-effect coefficient**

    γ = √(2qε_si N_A) / C_ox

| Symbol | Meaning |
|---|---|
| V_FB | flat-band voltage: the gate voltage that makes the bands flat; zero for an ideal MOS, V_FB = Φ_ms − Q_f/C_ox in a real one |
| 2φ_F | the band bending needed for strong inversion |
| γ√(2φ_F) | the voltage dropped across the oxide to support the depletion charge, \|Q_dmax\|/C_ox |
| N_A | substrate acceptor concentration |
| ε_si | silicon permittivity, 11.7ε₀ = 1.04×10⁻¹² F/cm |

**Reading the formula.** The gate voltage has three jobs: get to flat bands (V_FB), bend the bands by 2φ_F, and hold up the charge of the depletion region across the oxide. **Heavier substrate doping** raises both φ_F and the depletion charge, so V_T rises. A **thinner oxide** (larger C_ox) lowers V_T.

(This γ is not the same as the emitter injection efficiency γ of Week 13; the same Greek letter is used for different things.)

For simplified ideal MOSFET problems, the threshold voltage may simply be given. Always use the convention and parameters supplied in the question.

#### Example 14.1: calculating the threshold voltage

**Question.** An n-channel MOSFET is built on p-type silicon with N_A = 1×10¹⁷ cm⁻³, a 10 nm SiO₂ gate oxide and an n⁺ polysilicon gate, for which V_FB = −0.98 V. There is no oxide charge. Calculate the threshold voltage at 300 K.

**Given:** N_A = 1×10¹⁷ cm⁻³, t_ox = 10 nm = 1×10⁻⁶ cm, V_FB = −0.98 V, ε_ox = 3.45×10⁻¹³ F/cm, ε_si = 1.04×10⁻¹² F/cm, n_i = 10¹⁰ cm⁻³, kT/q = 0.0259 V.

**Find:** V_T = V_FB + 2φ_F + γ√(2φ_F).

**Solution.**

Step 1. Bulk Fermi potential:

    φ_F = 0.0259 ln(10¹⁷/10¹⁰) = 0.417 V,   2φ_F = 0.834 V

Step 2. Oxide capacitance:

    C_ox = 3.45×10⁻¹³ / 10⁻⁶ = 3.45×10⁻⁷ F/cm²

Step 3. Body-effect coefficient:

    γ = √(2 × 1.6×10⁻¹⁹ × 1.04×10⁻¹² × 10¹⁷) / 3.45×10⁻⁷ = 1.824×10⁻⁷ / 3.45×10⁻⁷ = 0.529 V^{1/2}

    γ√(2φ_F) = 0.529 × √0.834 = 0.529 × 0.913 = 0.483 V

Step 4. Add the three terms:

    V_T = −0.98 + 0.834 + 0.483 = 0.34 V

**Answer:** **V_T ≈ 0.34 V.**

## 14.8 MOSFET regions of operation

For a long-channel enhancement nMOS transistor, the region depends on V_GS compared with V_T, and on V_DS compared with V_GS − V_T (called the **overdrive voltage**).

| Condition | Operating region | Physical condition |
|---|---|---|
| V_GS < V_T | Cut-off | No strong inversion channel |
| V_GS > V_T and V_DS < V_GS − V_T | Linear (triode) | Channel exists along the entire length |
| V_GS > V_T and V_DS ≥ V_GS − V_T | Saturation | Channel pinches off near the drain |

## 14.9 Cut-off region

When V_GS ≤ V_T, an enhancement nMOS has no strong inversion channel. Ideally the drain current is zero, apart from small leakage:

    I_D ≈ 0

## 14.10 Linear (triode) region

When V_GS > V_T and V_DS is smaller than V_GS − V_T, the channel exists all the way from source to drain. The long-channel drain current is:

    I_D = μ_n C_ox (W/L) [ (V_GS − V_T) V_DS − V_DS²/2 ]

| Symbol | Meaning |
|---|---|
| μ_n | electron mobility in the channel |
| C_ox | oxide capacitance per unit area |
| W, L | channel width and length |

**Where it comes from (in words).** The amount of electron charge in the channel per unit area is C_ox × (how far the gate is above threshold). At the source end that is C_ox(V_GS − V_T); at the drain end the channel is at V_DS, so the gate is only V_GS − V_DS above it and the charge is C_ox(V_GS − V_T − V_DS). The current is (charge per area) × (width) × (drift velocity μ × field). Adding this up along the channel gives the formula; the −V_DS²/2 term is the effect of the channel thinning towards the drain.

For **small V_DS** the V_DS² term is negligible, and

    I_D ≈ μ_nC_ox(W/L)(V_GS − V_T) V_DS

The current is proportional to V_DS: the transistor behaves as a **voltage-controlled resistor** whose resistance is set by the gate.

## 14.11 Saturation region

As V_DS is increased, the channel becomes progressively thinner near the drain. When

    V_DS = V_GS − V_T

the channel charge at the drain end falls to zero: this is the **onset of pinch-off**. For larger V_DS the device is in **saturation**. The extra voltage is dropped across a short pinched-off region near the drain, and the current stops rising. Ignoring channel-length modulation:

    I_D = ½ μ_n C_ox (W/L) (V_GS − V_T)²

This is one of the most important MOSFET equations for examination calculations. In saturation the current depends on V_GS but (ideally) not on V_DS: the MOSFET is a **voltage-controlled current source**, which is what an amplifier needs.

@fig figures/mosfet-iv.svg | Output characteristics of an n-channel MOSFET. Each curve rises (linear region) until V_DS = V_GS − V_T (dashed line), then flattens (saturation).

## 14.12 Transconductance

In saturation the small-signal **transconductance** is

    g_m = ∂I_D/∂V_GS

For the ideal long-channel saturation equation:

    g_m = μ_nC_ox (W/L)(V_GS − V_T) = 2I_D/(V_GS − V_T)

Transconductance measures how strongly the drain current responds to a small change in gate voltage (unit: siemens, A/V). It plays the role for a MOSFET that β plays for a BJT.

## 14.13 Worked example 1: determining the operating region

**Question.** An nMOS transistor has V_T = 1 V, V_GS = 3 V and V_DS = 1 V. Determine its operating region.

**Given:** V_T = 1 V, V_GS = 3 V, V_DS = 1 V. **Find:** the region of operation.

**Solution.**

    V_GS > V_T (3 > 1), so a channel exists.
    V_GS − V_T = 3 − 1 = 2 V
    V_DS = 1 V < 2 V

The transistor is in the **linear (triode) region**.

## 14.14 Worked example 2: saturation current

**Question.** An nMOS transistor has μ_nC_ox(W/L) = 2 mA/V², V_T = 1 V and V_GS = 4 V. Find the saturation drain current.

**Given:** k = μ_nC_ox(W/L) = 2 mA/V², V_T = 1 V, V_GS = 4 V. **Find:** I_D(sat).

**Solution.**

    I_D = ½ × 2 × (4 − 1)² mA = 1 × 9 = 9 mA

**I_D = 9 mA.**

## 14.15 Worked example 3: linear-region current

**Question.** An nMOS transistor has μ_nC_ox(W/L) = 1 mA/V², V_T = 1 V, V_GS = 3 V and V_DS = 0.5 V. Calculate the drain current.

**Given:** k = 1 mA/V², V_T = 1 V, V_GS = 3 V, V_DS = 0.5 V. **Find:** I_D.

**Solution.**

First check the region: V_GS − V_T = 2 V > V_DS = 0.5 V, so it is linear.

    I_D = 1 × [ (3 − 1)(0.5) − (0.5)²/2 ] mA = [1 − 0.125] mA = 0.875 mA

**I_D = 0.875 mA.**

## 14.16 Comparison of BJT and MOSFET

| Feature | BJT | MOSFET |
|---|---|---|
| Control | Mainly current-controlled (base current) | Voltage-controlled (gate voltage) |
| Input current | Requires base current | Ideally zero DC gate current |
| Carriers | Electrons and holes (bipolar) | Majority-carrier conduction in the channel (unipolar) |
| Input impedance | Moderate | Very high |
| Typical use | Amplification, switching, analogue | Digital logic, switching, amplification, power |
| Key gain parameter | β or α | g_m |

## 14.17 Summary of Week 14

- An ideal MOS capacitor has three electrostatic conditions: accumulation, depletion and inversion.
- On a p-type substrate: negative gate → accumulation; moderate positive gate → depletion; sufficiently positive gate → inversion.
- The MOSFET uses the inversion layer as a controllable channel between source and drain.
- Threshold voltage is the gate voltage at the onset of strong inversion, V_T = V_FB + 2φ_F + γ√(2φ_F).
- For an nMOS enhancement device: V_GS < V_T gives cut-off; V_GS > V_T and V_DS < V_GS − V_T gives the linear region; V_GS > V_T and V_DS ≥ V_GS − V_T gives saturation.
- Linear: I_D = μC_ox(W/L)[(V_GS − V_T)V_DS − V_DS²/2]. Saturation: I_D = ½μC_ox(W/L)(V_GS − V_T)².

---

## Review questions, Week 14, solved

### 9. What is a MOS capacitor? Draw and label its basic structure.

A MOS (metal-oxide-semiconductor) capacitor is a three-layer structure in which a conducting gate electrode is separated from a semiconductor substrate by a thin insulating oxide. It acts as a parallel-plate capacitor whose capacitance per unit area is C_ox = ε_ox/t_ox in accumulation; the gate voltage controls the charge at the semiconductor surface.

**Sketch (top to bottom):** a gate contact (metal or n⁺ polysilicon) labelled **G**; a thin layer of **SiO₂** with thickness **t_ox** marked; the **p-type Si substrate** (doping N_A); a metal **substrate (body) contact** at the bottom labelled **B**. Mark V_G applied between G and B.

### 10. Explain accumulation, depletion and inversion for a p-type silicon substrate.

- **Accumulation (V_G < 0):** the negative gate attracts the majority holes to the oxide–silicon interface. The surface becomes more strongly p-type; the bands bend upward.
- **Depletion (small V_G > 0):** the positive gate repels holes from the surface, leaving a layer of fixed negative acceptor ions of width W_d. There are almost no mobile carriers in this layer; the bands bend downward.
- **Inversion (V_G > V_T):** the downward band bending becomes large enough (ψ_s ≈ 2φ_F) to attract minority electrons to the surface in large numbers. The surface becomes n-type: an electron inversion layer forms, which is the MOSFET channel. The depletion width stops growing at W_dmax.

### 11. Why is an oxide layer used between the gate and the semiconductor?

1. It **insulates** the gate from the channel, so the gate draws essentially no DC current. This gives the MOSFET its very high input impedance and low power consumption.
2. It lets the gate control the surface through the **electric field** only, as the dielectric of a capacitor. A thin oxide gives a large C_ox and strong control.
3. SiO₂ forms a very **clean, stable interface** with silicon (few interface traps), so the surface carriers have good mobility and V_T is stable.
4. It **passivates** and protects the silicon surface.

### 12. Define threshold voltage.

The threshold voltage V_T is the gate-to-source voltage at which the semiconductor surface reaches strong inversion (surface potential ψ_s ≈ 2φ_F), so that a conducting inversion channel forms between source and drain and significant drain current begins to flow. For an ideal nMOS, V_T = V_FB + 2φ_F + γ√(2φ_F), with γ = √(2qε_siN_A)/C_ox.

### 13. State the conditions for cut-off, linear and saturation operation of an nMOS transistor.

- **Cut-off:** V_GS < V_T. No channel, I_D ≈ 0.
- **Linear (triode):** V_GS > V_T and V_DS < V_GS − V_T. I_D = μ_nC_ox(W/L)[(V_GS − V_T)V_DS − V_DS²/2].
- **Saturation:** V_GS > V_T and V_DS ≥ V_GS − V_T. I_D = ½μ_nC_ox(W/L)(V_GS − V_T)².

### 14. Derive the condition V_DS ≥ V_GS − V_T for saturation.

**Physical argument.** An inversion channel exists at a point in the channel only where the gate is more than V_T above the local channel voltage. At the source end the channel voltage is 0, so the gate–channel voltage is V_GS. At the drain end the channel voltage is V_DS, so the gate–channel voltage is V_GD = V_GS − V_DS. The channel at the drain end disappears (pinches off) when this falls to threshold:

    V_GS − V_DS = V_T   ⇒   V_DS = V_GS − V_T

For any V_DS larger than this, the drain end stays pinched off and the device is saturated. Hence saturation requires V_DS ≥ V_GS − V_T.

**Mathematical argument.** The linear-region equation I_D = k[(V_GS − V_T)V_DS − V_DS²/2] is a parabola in V_DS. Its maximum is where

    dI_D/dV_DS = k[(V_GS − V_T) − V_DS] = 0   ⇒   V_DS = V_GS − V_T

Beyond this point the equation would predict a falling current, which does not happen physically; instead the current stays at its maximum value, I_D = ½k(V_GS − V_T)². So saturation begins at V_DS = V_GS − V_T.

### 15. Calculate the saturation current when μ_nC_ox(W/L) = 1.5 mA/V², V_GS = 5 V and V_T = 2 V.

    I_D = ½ μ_nC_ox(W/L)(V_GS − V_T)² = ½ × 1.5 × (5 − 2)² = 0.75 × 9 = 6.75 mA

**I_D = 6.75 mA.**

### 16. Calculate the linear-region current for μ_nC_ox(W/L) = 2 mA/V², V_GS = 4 V, V_T = 1 V and V_DS = 0.8 V.

Check the region: V_GS − V_T = 3 V > V_DS = 0.8 V, so linear.

    I_D = 2 × [ (4 − 1)(0.8) − (0.8)²/2 ] = 2 × [2.4 − 0.32] = 2 × 2.08 = 4.16 mA

**I_D = 4.16 mA.**

### 17. Compare a BJT and a MOSFET in terms of input impedance and control mechanism.

- **Control mechanism.** A BJT is current-controlled: the collector current is set by the base current (I_C = βI_B), or equivalently by the base–emitter voltage through carrier injection across a forward-biased junction. A MOSFET is voltage-controlled: the gate voltage creates an electric field across the oxide that induces the channel charge, with no carrier injection from the gate.
- **Input impedance.** The BJT's base–emitter junction is forward biased and must be supplied with base current, so its input impedance is moderate (typically kΩ). The MOSFET's gate is insulated by the oxide and draws essentially no DC current, so its input impedance is extremely high (10¹² Ω or more), limited only by the gate capacitance at high frequency.

---

## Practice questions

These extra questions practise this week's ideas. Work each one on paper before reading the solution; the calculation questions follow the same Question, Given, Find, Solution, Answer layout as the worked examples.

#### Practice 14.1: oxide capacitance of a thin gate

**Question.** Find C_ox for a 3 nm SiO₂ gate oxide.

**Given:** t_ox = 3×10⁻⁷ cm, ε_ox = 3.45×10⁻¹³ F/cm.

**Find:** C_ox.

**Solution.**

    C_ox = ε_ox/t_ox = 3.45×10⁻¹³ / 3×10⁻⁷ = 1.15×10⁻⁶ F/cm²

**Answer:** **C_ox = 1.15 μF/cm².**

#### Practice 14.2: bulk potential and maximum depletion width

**Question.** For p-type silicon with N_A = 5×10¹⁶ cm⁻³, find φ_F and the maximum depletion width at strong inversion.

**Given:** N_A = 5×10¹⁶ cm⁻³, n_i = 10¹⁰ cm⁻³, ε_si = 1.04×10⁻¹² F/cm.

**Find:** φ_F and W_dmax.

**Solution.**

    φ_F = 0.0259 ln(5×10⁶) = 0.400 V
    W_dmax = √(4ε_siφ_F/qN_A) = √(4 × 1.04×10⁻¹² × 0.400 / (1.6×10⁻¹⁹ × 5×10¹⁶)) = 1.44×10⁻⁵ cm

**Answer:** **φ_F = 0.40 V, W_dmax = 0.144 μm.**

#### Practice 14.3: threshold voltage of an ideal MOSFET

**Question.** Using the substrate of Practice 14.2 with a 20 nm oxide and an ideal gate (V_FB = 0), find the threshold voltage.

**Given:** φ_F = 0.400 V, W_dmax = 1.44×10⁻⁵ cm, t_ox = 2×10⁻⁶ cm.

**Find:** V_T = V_FB + 2φ_F + qN_AW_dmax/C_ox.

**Solution.**

    C_ox = 3.45×10⁻¹³/2×10⁻⁶ = 1.725×10⁻⁷ F/cm²
    qN_AW_dmax = 1.6×10⁻¹⁹ × 5×10¹⁶ × 1.44×10⁻⁵ = 1.15×10⁻⁷ C/cm²
    V_T = 0 + 0.80 + 1.15×10⁻⁷/1.725×10⁻⁷ = 0.80 + 0.67 = 1.47 V

**Answer:** **V_T ≈ 1.47 V.** A thinner oxide or a real n⁺ poly gate (negative V_FB) would lower it.

#### Practice 14.4: current in both regions

**Question.** An nMOS has μ_nC_ox(W/L) = 0.5 mA/V² and V_T = 0.8 V, with V_GS = 2.0 V. Find I_D at V_DS = 0.4 V and at V_DS = 2.0 V.

**Given:** k = 0.5 mA/V², V_T = 0.8 V, V_GS = 2.0 V (overdrive 1.2 V).

**Find:** I_D at each V_DS.

**Solution.**

    V_DS = 0.4 V < 1.2 V → linear:  I_D = 0.5 × [1.2 × 0.4 − 0.4²/2] = 0.5 × 0.40 = 0.20 mA
    V_DS = 2.0 V ≥ 1.2 V → saturation: I_D = ½ × 0.5 × 1.2² = 0.36 mA

**Answer:** **0.20 mA (linear) and 0.36 mA (saturation).**

#### Practice 14.5: transconductance

**Question.** Find the transconductance of the transistor of Practice 14.4 in saturation.

**Given:** I_D = 0.36 mA, V_GS − V_T = 1.2 V.

**Find:** g_m.

**Solution.**

    g_m = 2I_D/(V_GS − V_T) = 2 × 0.36/1.2 = 0.60 mS
    (check: g_m = k(V_GS − V_T) = 0.5 × 1.2 = 0.60 mS)

**Answer:** **g_m = 0.60 mS.**

#### Practice 14.6: body effect

**Question.** A MOSFET has γ = 0.5 V^{1/2} and 2φ_F = 0.8 V. By how much does its threshold voltage rise when the source is 2 V above the body?

**Given:** γ = 0.5 V^{1/2}, 2φ_F = 0.8 V, V_SB = 2 V.

**Find:** ΔV_T.

**Solution.**

    ΔV_T = γ(√(2φ_F + V_SB) − √(2φ_F)) = 0.5 × (√2.8 − √0.8) = 0.5 × (1.673 − 0.894) = 0.39 V

**Answer:** **V_T rises by 0.39 V.**

#### Practice 14.7: sizing a transistor

**Question.** A MOSFET must carry 1 mA in saturation with an overdrive of 0.5 V. If μ_nC_ox = 200 μA/V², what W/L is needed?

**Given:** I_D = 1 mA, V_GS − V_T = 0.5 V, μ_nC_ox = 200×10⁻⁶ A/V².

**Find:** W/L.

**Solution.**

    W/L = 2I_D / (μ_nC_ox (V_GS − V_T)²) = 2 × 10⁻³ / (200×10⁻⁶ × 0.25) = 40

**Answer:** **W/L = 40.**

#### Practice 14.8: channel-length modulation

**Question.** Why does a real MOSFET's saturation current rise slightly with V_DS?

**Answer.** Beyond pinch-off, increasing V_DS moves the pinch-off point slightly towards the source, so the effective channel length becomes L − ΔL. Since I_D ∝ 1/L, the current rises a little. This is **channel-length modulation**, written I_D = I_D(sat)(1 + λV_DS). It is the MOSFET's equivalent of the BJT's Early effect and gives a finite output resistance r_o ≈ 1/(λI_D).

---

## Objectives check

Use this table to confirm you have met this week's objectives. Cover the Answer column and answer each check question from memory. If you cannot, go back to the section in the last column before moving on.

| # | Objective | Check yourself | Answer | Where it is taught |
|---|---|---|---|---|
| 1 | Describe the structure of an ideal MOS capacitor and calculate C_ox. | Find C_ox for a 5 nm SiO₂ layer. | 3.45×10⁻¹³/5×10⁻⁷ = 6.9×10⁻⁷ F/cm². | 14.2 |
| 2 | Explain accumulation, depletion and inversion. | On p-type Si, what forms at the surface in inversion? | A layer of electrons (the surface becomes n-type). | 14.3–14.5 |
| 3 | Explain how a MOS capacitor becomes a MOSFET, and enhancement versus depletion mode. | Does an enhancement-mode nMOS conduct at V_GS = 0? | No: a gate voltage above V_T is needed to create the channel. | 14.6 |
| 4 | Define the threshold voltage and calculate it. | What three contributions make up V_T? | V_FB, the band bending 2φ_F, and the depletion-charge term γ√(2φ_F). | 14.7; Example 14.1 |
| 5 | Determine the operating region and calculate drain current. | V_T = 1 V, V_GS = 2 V, V_DS = 3 V: which region? | Saturation (V_DS ≥ V_GS − V_T = 1 V). | 14.8–14.15 |
| 6 | Compare BJTs and MOSFETs. | Which has the higher input impedance, and why? | The MOSFET: its gate is insulated by the oxide and draws no DC current. | 14.16; review Q17 |
