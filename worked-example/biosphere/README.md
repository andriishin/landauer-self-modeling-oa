# Worked Example: structural verdict for the biosphere (Gaia)

A structural verdict for Earth's biosphere as a single system, under the
refounded central quantity $\eta_v = I_{\text{pred}}/I_{\text{mem}} \in [0,1]$.
Companion to § 3.7 (Andriishin, *Theory in Biosciences*, in preparation).

## Structural verdict

The biosphere **passes both axes**:

- $S = 1$ — biogeochemistry is fed by its own flux (condition i) and a distorted
  regulation returns as species collapses / mass extinctions to the biosphere
  itself (condition ii);
- $\eta_v > 0$ — it holds predictive structure about its own environment.

So the biosphere is **vital** — or a **family** of vital systems: the
unity-of-model question of § 3.7 (one Gaia with a single internal representation,
or billions of organism-scale models not stitched into one loop) stays open. The
**grade** (numeric $\eta_v$) is **not asserted**: it requires an MI estimate through
the biogeochemical sensory channel, left to future work. The old energetic-
denominator computation is removed.

## Carrier-capacity ladder (ceilings on substrate, NOT η_v)

The genomic figures are **carrier capacities** (ceilings on substrate, in bits),
**not** values of $\eta_v$ and **not** measured predictive information. A repeated
genome adds no predictive mutual information about the environment, so the
copy-number ledger is irrelevant to $\eta_v$; it is shown only to contrast scales.

| Substrate ledger | bits (~) | note |
|------------------|----------|------|
| atmospheric / regulatory pools | $10^{15}$ | small abiotic-pool ceiling |
| unique coding/regulatory genome | $10^{19}$ | $10^{12}$ sp × $5\cdot10^{6}$ bp × 2 bit/bp (main § 3.7) |
| raw unique-genome (overcounts) | $10^{24}$ | over-counts non-coding bases (no predictive MI) |
| full copy-number DNA | $10^{37}$ | Landenmark et al. 2015; ~17 orders larger, irrelevant |

None of these is a value of $\eta_v$. $\eta_v = I_{\text{pred}}/I_{\text{mem}}$
requires a measured predictive MI, which a substrate ceiling does not give.

## Contents

| File | Purpose |
|------|---------|
| `eta_biosphere.py` | Structural verdict ($S=1$, $\eta_v>0$) + carrier-capacity ladder |
| `expected_output.txt` | Reference output (LF) for verification |

Uses only the Python standard library.

## Running

```bash
python eta_biosphere.py
```

## Literature

- **Field, C. B.; Behrenfeld, M. J.; Randerson, J. T.; Falkowski, P.** Primary production of the biosphere. *Science* **1998**, *281*, 237–240. (Global NPP scale.)
- **Bar-On, Y. M.; Phillips, R.; Milo, R.** The biomass distribution on Earth. *PNAS* **2018**, *115*, 6506–6511.
- **Landenmark, H. K. E.; Forgan, D. H.; Cockell, C. S.** An estimate of the total DNA in the biosphere. *PLoS Biol.* **2015**, *13*, e1002168. (Copy-number DNA ledger $\sim 10^{37}$ bits.)
- **Lovelock, J. E.; Margulis, L.** Atmospheric homeostasis by and for the biosphere: the Gaia hypothesis. *Tellus* **1974**, *26*, 2–10.

## Status

The verdict is **structural** ($S = 1$, $\eta_v > 0$); no $\eta_v$ number is asserted.
The genomic figures are carrier-capacity ceilings, not predictive information.
Refining $I_{\text{pred}}/I_{\text{mem}}$ through biogeochemical proxies (cycles
as "memory") is separate work. The single-system vs family-of-subsystems reading
remains an open empirical question (§ 3.7). Self-contained: standard library only.
