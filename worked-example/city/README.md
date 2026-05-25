# Worked Example: η_L of a large city + I_v formula demonstration

Companion to § 3.6 of the paper «Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality». The script is self-contained (Python standard library only; no external, empirical, or unpublished dependency) and has two **clearly separated** parts.

## Part 1 — η_L (the camertone claim of § 3.6)

A city is a socio-technical system with a rich structural potential and yet a **vanishing $\eta_L$** through the exergetic denominator of its total dissipation. $\eta_L$ is computed from first principles via formula (1):

$$N_{\text{max}} = \frac{E_{\text{actual}}}{k_B T \ln 2}, \qquad \eta_L = \frac{I_{\text{pred}}}{N_{\text{max}}}.$$

Singapore and Detroit are used **only** as order-of-magnitude-distinct energy budgets. No cohort and no $I_v$ are needed for this — every number reproduces from the inputs in this file.

- $T = 285$ K; $k_B T \ln 2 \approx 2.73 \cdot 10^{-21}$ J/bit.
- Singapore: $E_{\text{actual}} \sim 10^{19}$ J/year $\Rightarrow$ $N_{\text{max}} \approx 3.67 \cdot 10^{39}$ bits; with $I_{\text{pred}} \lesssim 10^{10}$ bits $\Rightarrow$ $\eta_L \approx 2.7 \cdot 10^{-30}$.
- Detroit: $E_{\text{actual}} \sim 5 \cdot 10^{18}$ J/year $\Rightarrow$ $N_{\text{max}} \approx 1.83 \cdot 10^{39}$ bits; $\eta_L \approx 5.5 \cdot 10^{-30}$ (2× higher — smaller budget).

$I_{\text{pred}} \lesssim 10^{10}$ bits is an upper bound from the capacity of the administrative-infrastructural carrier, **not a measured** predictive information (the operationalization is open, as for the biosphere / LLM-corp). Via the computational denominator the estimate is closer to the biological range, but requires a separate operationalization of the exergy of managerial computation (§ 3.6).

**Substantive camertone claim:** a city is structurally complex yet $\eta_L$ is negligible (~$3 \cdot 10^{-30}$) — vitally negligible.

## Part 2 — I_v composite, formula (2)+(2a): a method demonstration

$$I_v = \sqrt[3]{\tilde{T}_v \cdot \tilde{C}_v \cdot \tilde{S}_v},$$

where $\tilde{T}_v, \tilde{C}_v, \tilde{S}_v$ are the percentile-normalized (formula 2a) capacities within a cohort. This part runs on an **explicitly synthetic** set of archetype profiles. Its purpose is to show the mechanics of the composite:

- (2a) percentile normalization maps a raw proxy to a $[0,1]$ rank relative to the cohort;
- (2) the geometric mean drags the composite toward **any** weak capacity (a profile with one failed axis gets a low $I_v$ even if the other two are high).

This is **not** an empirical ranking of real cities. The raw numbers in `SYNTHETIC_COHORT` are illustrative placeholders, not measurements. The empirical calibration of $I_v$ for specific cities from open data (OECD FUA, CDP Cities, WIPO/OECD REGPAT, GDELT, OpenStreetMap) is separate work and is deliberately not asserted here.

## Contents

| File | Purpose |
|------|---------|
| `eta_L_city.py` | Part 1 ($\eta_L$ of real cities) + Part 2 ($I_v$ formula demo on synthetic data) |
| `expected_output.txt` | Reference output for reproducibility verification |

## Running

```bash
python eta_L_city.py
```

The output should match `expected_output.txt` up to floating-point round-off.

## Status

Part 1 ($\eta_L$) is the reproducible § 3.6 camertone: a city is structurally complex but vitally negligible; the computation is self-contained, with no cohort and no $I_v$. Part 2 demonstrates the $I_v$ composite formula on synthetic profiles; no empirical ranking of real cities by $I_v$ is asserted (that is separate work). No dependency beyond the standard library.

## Literature

- **Bettencourt, L. M. A.; Lobo, J.; Helbing, D.; Kühnert, C.; West, G. B.** Growth, innovation, scaling, and the pace of life in cities. *PNAS* **2007**, *104*, 7301–7306. (Scaling of urban metrics — context for the separate empirical $I_v$ work.)
