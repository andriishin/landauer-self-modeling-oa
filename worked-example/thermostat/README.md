# Worked Example: η_L for a bimetallic thermostat

A computation of the Landauer efficiency of self-modeling $\eta_L$ for a household thermostat with a bimetallic strip. Companion to the paper «Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality» (§ 4.4 + Supplementary § S4.4).

## What it means

The thermostat is a **boundary case**, not a positive one. It *formally satisfies* Friston's free-energy principle (FEP) — it minimizes the error between the setpoint and the observation — but it *does not satisfy the self-payment requirement*: the predictive information about the room is physically paid for by the external power grid, not by the internal dissipation of the bimetal.

This is the **central anti-FEP argument** of the paper. In terms of the counterfactual-screening procedure (§ 2.2):

| Candidate | Inside the boundary? | Why |
|-----------|----------------------|-----|
| Bimetallic strip | yes | removing it breaks the loop |
| Relay contact group | yes | removing it breaks the loop |
| Heating element | no | removing it eliminates the heat source, not the decision loop |
| Electric grid | no | external energy source |
| External setpoint operator | no | removing it does not disrupt the regulation |

The boundary is `{bimetal, relay}`. Within it, $E_{\text{actual}} \sim 10^{-6}$ W.

## Contents

| File | Purpose |
|------|---------|
| `eta_L_thermostat.py` | Computation of the two readings of η_L (trivial vs. managing) |
| `expected_output.txt` | Reference output for verification |

## Running

```bash
python eta_L_thermostat.py
```

## Parameters

- $T_{\text{room}} = 295$ K — room temperature (the thermostat as a Landauer heat-receiver).
- $\Delta T_{\text{room}} = 10$ K — the range of variation of the room temperature.
- $\Delta T_{\text{hyst}} = 1$ K — the hysteresis of the bimetallic switch.
- $\tau_d = 1800$ s (30 min) — the characteristic dissipation window (thermal inertia).
- $P_{\text{int}} = 10^{-6}$ W — internal dissipation (elastic relaxation of the bimetal + relay).

## Expected results

- $I_{\text{pred}} \le \log_2(10/1) \approx 3.32$ bits (paper bound: ≤ 5 bits).
- $E_{\text{actual}}^{\text{int}} = 10^{-6} \cdot 1800 = 1.8 \cdot 10^{-3}$ J.
- $N_{\text{max}} = E_{\text{actual}}^{\text{int}} / (k_B T \ln 2) \approx 6.4 \cdot 10^{17}$ bits.
- $\eta_L^{\text{trivial}}$ (holding the bimetal's own shape) $\approx 5.2 \cdot 10^{-18}$ — vanishing, but positive.
- $\eta_L^{\text{managing}}$ (regulating the room) $= 0$ — the numerator refers to the environment "room + power supply", while the denominator refers only to the bimetal's own dissipation.

The difference between the two numbers is structural, not quantitative: it marks the transition from a Pearl-blanket to a Friston-blanket in the sense of Bruineberg, Dołęga, Dewhurst, Baltieri 2021/2022 ("The Emperor's New Markov Blankets", the mature formalization of the Pearl-/Friston-blanket distinction), as distinct from Bruineberg, Kiverstein, Rietveld 2018 (the ecological-enactive critique of pure FEP, "The anticipating brain is not a scientist"). One and the same physical system admits several self-consistent boundaries; the choice between them is the methodological discipline of self-payment.

## Literature

- **Bruineberg, J.; Dołęga, K.; Dewhurst, J.; Baltieri, M.** The Emperor's New Markov Blankets. *Synthese* **2022**, *199*, 13727–13772. (The mature formalization of the Pearl-/Friston-blanket distinction — `[Bruineberg2022]` in the paper.)
- **Bruineberg, J.; Kiverstein, J.; Rietveld, E.** The anticipating brain is not a scientist: the free-energy principle from an ecological-enactive perspective. *Synthese* **2018**, *195*, 2417–2444. (The ecological-enactive critique of pure FEP — `[Bruineberg2018]` in the paper.)
- **Friston, K.** The free-energy principle: a unified brain theory? *Nat. Rev. Neurosci.* **2010**, *11*, 127–138.
- **Aguilera, M.; Millidge, B.; Tschantz, A.; Buckley, C. L.** How particular is the physics of the free energy principle? *Phys. Life Rev.* **2022**, *40*, 24–50.

## Status

The computation is compact (10–15 lines of accounting); its role in the reproducibility of the paper is not quantitative but **demonstrative**: it shows that the counterfactual-screening procedure is trivially realizable, and that distinguishing the "trivial" vs. "managing" readings is computable, not rhetorical.
