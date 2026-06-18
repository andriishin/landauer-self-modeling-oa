# Worked Example: η_L for LLM-as-corporation

A computation of the Landauer efficiency of self-modeling $\eta_L$ for an LLM under the extended boundary "model + data centre + corporation". Companion to § 3.4 of the paper «Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality».

## What it means

Paper § 3.4 distinguishes three readings of an LLM:

1. **Operational** "model + data centre": $\eta_L > 0$ by external metrics, but not self-payment.
2. **Interpretive** "weights at the moment of inference": $\eta_L^{\text{int}}$ **undefined** — a simultaneous failure of $T_v^{\text{int}}$ (no causally relevant model of its own environment) and $C_v^{\text{int}}$ (no internal dissipation paying for the weights).
3. **Boundary extension** "model + data centre + corporation": $\eta_L > 0$, but the measured object is the corporation, not the model.

This worked example operationalises the third reading: the corporation is treated as a socio-technical system, and $\eta_L^{\text{corp}}$ is computed via equation (1).

## Contents

| File | Purpose |
|------|---------|
| `eta_L_llm_corp.py` | Computation of $\eta_L^{\text{corp}}$ via the exergetic denominator |
| `expected_output.txt` | Reference output |

## Running

```bash
python eta_L_llm_corp.py
```

## Parameters

### Energy budget (frontier-AI lab, annual)
- **Data centre:** $\sim 100$ MW continuous $= 3.15 \cdot 10^{15}$ J/year.
- **Office and operations:** $\sim 10$ MW $= 3.15 \cdot 10^{14}$ J/year.
- **Supply chain** (hardware manufacturing, logistics, amortization): $\sim 1$ GW $= 3.15 \cdot 10^{16}$ J/year.
- **Total:** $E_{\text{actual}}^{\text{total}} \sim 3.5 \cdot 10^{16}$ J/year.

### Predictive information
- **Training corpus**, compressed into weights: $\sim 10^{12}$ bits (entropy of the training data $\times$ compression).
- **Operational memory** (logs, customer interactions, documents): $\sim 10^{11}$ bits.
- **Market intelligence** (research, competitive, regulatory): $\sim 10^{10}$ bits.
- **Total:** $I_{\text{pred}} \sim 1.1 \cdot 10^{12}$ bits.

### Other
- $T = 300$ K (operating temperature; the standardised $T$ for the LLM / data centre, paper § 2.1).
- $k_B T \ln 2 \approx 2.87 \cdot 10^{-21}$ J/bit.

## Expected results

- $N_{\text{max}}^{\text{ex}} = 3.5 \cdot 10^{16}/2.87 \cdot 10^{-21} \approx 1.22 \cdot 10^{37}$ bits/year.
- $\eta_L^{\text{corp}} \text{(exergetic)} \approx 9 \cdot 10^{-26}$ — order $10^{-25}$ (upper bound, capacity-bound numerator).

## Substantive conclusion

1. Extending the LLM boundary to the corporation yields a **positive but catastrophically small** $\eta_L^{\text{corp}}$.
2. The boundary-extension paradox: the larger the system, the smaller the $\eta_L$ — the scaling of $E_{\text{actual}}$ outpaces $I_{\text{pred}}$. The corporation has many orders of magnitude more absolute predictive information than a bacterial cell, but its energy budget grows even faster: most of the joules go to logistics, manufacturing, HVAC, and cooling overhead, not to the bit-flip operations that support holding its own model.
3. This is a substantive result, not a defect of the procedure: "extending the responsible subject" (paper § 3.4) does not, quantitatively, make a large socio-technical system vitally comparable to the biological level.

## Literature

- **Patterson, D.; Gonzalez, J.; Le, Q.; Liang, C.; Munguia, L.-M.; Rothchild, D.; So, D.; Texier, M.; Dean, J.** Carbon Emissions and Large Neural Network Training. *arXiv preprint* **2021**, arXiv:2104.10350. (Energy footprint of frontier model training.)
- **Bender, E. M.; Gebru, T.; McMillan-Major, A.; Shmitchell, S.** On the Dangers of Stochastic Parrots. *FAccT* **2021**. (Scale and infrastructure of major LLM operations.)

## Status

Methodological calibration. The exact value of $I_{\text{pred}}^{\text{corp}}$ for corporate systems is a matter for separate work; the robustness of the order $\eta_L^{\text{corp}} \sim 10^{-25}$ holds while varying the inputs over plausible ranges. Paper § 3.4 gives, for the corporation, only the exergetic denominator (sign / capacity-bound upper bound); a computational reading for the corporation is not introduced in § 3.4.
