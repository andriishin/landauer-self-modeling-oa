# Worked Examples for «Vitality as a Landauer Efficiency of Self-Modeling»

Reproducible computations of $\eta_L$ and $I_v$ for the five paradigm ("tuning-fork") systems of the paper. Each folder is a self-contained package (Python script + README + expected output) cross-referenced to a specific section of the paper.

## Index

| Folder | Paper section | $\eta_L$ (central estimate) | What it demonstrates |
|--------|---------------|------------------------------|----------------------|
| [`E-coli/`](./E-coli/) | § 3.5 | $3 \cdot 10^{-8}$ (ex.), $3 \cdot 10^{-5}$ (comp.) | **Positive case**: the bacterium clears both thresholds — the central worked example of the paper |
| [`thermostat/`](./thermostat/) | § 4.4 | $5 \cdot 10^{-18}$ trivial / $0$ managing | **FEP boundary**: formal FEP-applicability without self-payment; the central anti-FEP argument |
| [`city/`](./city/) | § 3.6 | $\sim 3 \cdot 10^{-30}$ (Singapore, Detroit) | **Socio-technical system**: structurally complex, $\eta_L$ negligible; $I_v$ formula (2)+(2a) on synthetic profiles (no empirical city ranking) |
| [`biosphere/`](./biosphere/) | § 3.7 | $\sim 10^{-18}$ (annual window, biomass-equiv. $I_{\text{pred}}$) | **Planetary system**: a single Gaia with an enormous Landauer budget from NPP |
| [`LLM-as-corp/`](./LLM-as-corp/) | § 3.4 | $\sim 10^{-25}$ (corp boundary) | **Boundary extension**: "model + data center + corporation" yields a positive but catastrophically small $\eta_L$ |

## What is not covered by a separate computation

The paradigm cases for which $\eta_L = 0$ structurally (through the numerator or the denominator) require no worked example:

- **The Sun** (§ 3.1): $\eta_L = 0$ through the numerator — there is no causally relevant environment.
- **Hurricane and flame** (§ 3.2): $\eta_L = 0$ through the numerator — there is no $I_{\text{pred}}$.
- **Crystal** (§ 3.3): $\eta_L = 0$ through the denominator — there is no $E_{\text{actual}}$ for a stationary structure.
- **LLM (narrow boundary "weights at inference")** (§ 3.4): $\eta_L = 0$ through *both* the numerator and the denominator.

A full reproducible sweep over all six paradigm cases is future work (see paper § 3).

## Running all computations

```bash
for dir in E-coli thermostat city biosphere LLM-as-corp; do
    echo "=== $dir ==="
    cd "$dir"
    python eta_L_*.py
    cd ..
done
```

Each folder also contains an `expected_output.txt` for reproducibility verification.

## Dependencies

All computations use **the Python standard library only** (`math`, `statistics`). No `pip install` is required.

(Optional extensions — sensitivity dashboards, KSG mutual-information estimation, plotly visualizations — are noted as out-of-scope at the iter-010 pre-submission stage.)

## Layout of each folder

```
<system>/
├── README.md           — description (English, default): model, parameters, expected results, status
├── README.ru.md        — the same in Russian
├── eta_L_<system>.py         — main computation
├── sensitivity.py            — Monte Carlo sensitivity analysis (where applicable)
└── expected_output.txt       — captured output for verification
```

## Status

The computations are a **methodological calibration** demonstrating the reproducibility of the paradigm-case estimates. A detailed experimental design, KSG estimation of $I_{\text{pred}}$ from measurable time series, and a full sensitivity map of the sweep (§ 3.5, § 3.6) are future work.
