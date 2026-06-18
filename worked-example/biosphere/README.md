# Worked Example: η_L for the biosphere (Gaia)

A computation of the Landauer efficiency of self-modeling $\eta_L$ for Earth's biosphere as a single system. Companion to § 3.7 of the paper «Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality».

## What it means

The biosphere is the largest paradigm case of the paper. Under the "single system" reading, $\eta_L$ through the exergetic denominator ($E_{\text{actual}} = \text{NPP} \cdot \tau$) over an annual window gives a characteristic value of $\sim 10^{-22}$ — positive, but catastrophically small, because of the enormous Landauer budget of planetary NPP against a bounded biomass information pool.

The alternative reading — "a family of overlapping vital systems" — is discussed in § 3.7 of the paper and remains an open empirical question (it depends on whether the biosphere has a single internal representation of its own environment).

## Contents

| File | Purpose |
|------|---------|
| `eta_L_biosphere.py` | Computation of $\eta_L$ + sensitivity over $I_{\text{pred}}$ and $\tau$ |
| `expected_output.txt` | Reference output |

## Running

```bash
python eta_L_biosphere.py
```

## Parameters (central)

- $T_{\text{surf}} = 288$ K — mean surface temperature.
- $\text{NPP} = 10^{14}$ W — global net primary production (literature consensus).
- $\tau = 1$ year — the integration window (the annual biogeochemical cycle).
- $I_{\text{pred}} \lesssim 10^{20}$ bits — a defensible ceiling on the **coding/regulatory** fraction of the unique genomic content of the biosphere (without accounting for copy number; excluding non-coding bases that carry no predictive MI about the environment). The raw unique-genome upper bound (~$10^{24}$ bits) over-counts non-functional sites; the total copy-number DNA volume of the biosphere ($\sim 10^{37}$ bits, Landenmark et al. 2015) is ~17 orders larger and is irrelevant for predictive information (a repeated genome adds no predictive mutual information about the environment). The number is a ceiling on substrate capacity, not a measured predictive MI.

## Expected results

- $k_B T \ln 2 \approx 2.76 \cdot 10^{-21}$ J/bit.
- $E_{\text{actual}} = 10^{14} \cdot 3.16 \cdot 10^{7} \approx 3.16 \cdot 10^{21}$ J/year.
- $N_{\text{max}} \approx 1.15 \cdot 10^{42}$ bits/year.
- $\eta_L \approx 8.7 \cdot 10^{-23}$ — order $10^{-22}$.

## Sensitivity table

The script reports $\eta_L$ for four $I_{\text{pred}}$ candidates (atmospheric pools $10^{15}$, ecosystem-memory low/high $10^{19}/10^{22}$, coding-bound $10^{20}$ bits) and three windows ($\tau = $ day / year / millennium). Substantively: with the coding-bound $I_{\text{pred}}$ and the annual window we obtain $\eta_L \sim 10^{-22}$; narrower $I_{\text{pred}}$ or longer windows lower the estimate.

## Literature

- **Field, C. B.; Behrenfeld, M. J.; Randerson, J. T.; Falkowski, P.** Primary production of the biosphere: integrating terrestrial and oceanic components. *Science* **1998**, *281*, 237–240. (Source for global NPP $\sim 10^{14}$ W.)
- **Bar-On, Y. M.; Phillips, R.; Milo, R.** The biomass distribution on Earth. *PNAS* **2018**, *115*, 6506–6511. (Total biomass $\sim 5 \cdot 10^{14}$ kg.)
- **Lenton, T. M.** Earth System Science: A Very Short Introduction; Oxford University Press: Oxford, 2016.
- **Lovelock, J. E.; Margulis, L.** Atmospheric homeostasis by and for the biosphere: the Gaia hypothesis. *Tellus* **1974**, *26*, 2–10.

## Status

A methodological calibration of the single-system interpretation. The choice of $I_{\text{pred}}$ via the coding/regulatory fraction of unique genomic content sets a ceiling on substrate capacity, not a measured predictive information; refining it through ecosystem-functional proxies (biogeochemical cycles as "memory") is separate work. The contrast with the full copy-number DNA volume of the biosphere ($\sim 10^{37}$ bits, Landenmark et al. 2015) underscores that, for predictive MI, neither the copy-number nor the raw unique-genome content is the relevant ledger.
