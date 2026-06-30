# Worked Examples — vitality as self-paid self-modeling

Reproducible companions to the paradigm-case analysis of the paper (Andriishin,
*Theory in Biosciences*, in preparation). Each folder is a self-contained package
(Python script + README + expected output) keyed to a specific section.

The central quantity is the **predictive fraction**

$$\eta_v = \frac{I_{\text{pred}}}{I_{\text{mem}}} = 1 - \nu \in [0, 1],$$

a data-processing-inequality ratio of two *informational* quantities ($I_{\text{pred}}$
= how much the internal state knows about the future environment, $I_{\text{mem}}$ =
how much it knows about the past), with nostalgia $\nu = 1 - \eta_v$. There is **no**
energetic denominator: vitality is the conjunction

$$V(X) \;:=\; S \;\wedge\; (\eta_v > 0),$$

where $S \in \{0,1\}$ is the **self-payment predicate** (the system funds the
holding of its own model *and* a physical error-return loop closes on it). Demarcation
is carried by the rarity of a closed self-payment loop ($S = 1$), not by any smallness
of an efficiency. The numeric value of $\eta_v$ is computed in full only for *E. coli*;
for the other vital cases the grade is left to a future MI estimate.

## Index

| Folder | Section | Verdict | What it demonstrates |
|--------|---------|---------|----------------------|
| [`E-coli/`](./E-coli/) | § 3.5 | $S=1$, $\eta_v \sim O(0.1)$ **computed** | **Positive case**: $\eta_v = I_{\text{pred}}/I_{\text{mem}}$ computed exactly (Gaussian logdet); the central worked example |
| [`thermostat/`](./thermostat/) | § 4.4 | $S=0$, $\eta_v$ undefined | **FEP boundary**: formal FEP-applicability without self-payment; the central anti-FEP argument |
| [`city/`](./city/) | § 3.6 | $S=1$, $\eta_v>0$ (grade not asserted) | **Socio-technical system**: a closed self-payment loop; plus an $I_v$ structural-screening demo on synthetic data |
| [`biosphere/`](./biosphere/) | § 3.7 | $S=1$, $\eta_v>0$ (grade not asserted) | **Planetary system**: one Gaia (or a family); a carrier-capacity ladder, explicitly *not* a value of $\eta_v$ |
| [`LLM-as-corp/`](./LLM-as-corp/) | § 3.4 | $S=0$ on $B_1,B_2$; $S=1$ on $B_3,B_4$ | **Boundary extension**: where the loop closes, the self-paying subject is the firm, not the model |

## What is not covered by a separate computation

Cases that fail structurally need no worked example:

- **The Sun, neutron star, black hole** (§ 3.1): $\eta_v = 0$ through the **numerator** — no causally relevant environment, so $I_{\text{mem}} = 0$ and $I_{\text{pred}} = 0$.
- **Hurricane and flame** (§ 3.2): $\eta_v = 0$ through the **numerator** — dissipation without a held model (a stake without a model).
- **Belousov–Zhabotinsky / autocatalysis** (§ 3.2): $S = 0$ — fed but not corrected; the error-return loop (condition ii) does not close.
- **Crystal** (§ 3.3): $\eta_v = 0$ through the **numerator** — a stationary structure is homomorphic to its own lattice, not to a future environment signal ($I_{\text{mem}} \approx 0$).
- **LLM, narrow boundary "weights at inference"** (§ 3.4): $S = 0$ — a strong predictive model with an open payment loop; the intra-class value of $\eta_v$ is not defined on that boundary.

## Running all computations

```bash
for dir in E-coli thermostat city biosphere LLM-as-corp; do
    echo "=== $dir ==="
    (cd "$dir" && python eta_*.py)
done
# E-coli also ships a parameter-sensitivity script:
(cd E-coli && python sensitivity.py)
```

Each folder contains an `expected_output.txt` (LF line endings) for naive-diff
reproducibility verification.

## Dependencies

All computations use **only the Python standard library** (`math`; no `numpy`,
no `scipy`). No `pip install` is required. The *E. coli*
example computes the Gaussian mutual informations exactly through a pure-stdlib
Cholesky log-determinant, so the result is bit-for-bit reproducible.

## Structure of each folder

```
<system>/
├── README.md           — description (English, default): model, verdict, status
├── README.ru.md        — the same in Russian
├── eta_<system>.py     — main computation / structural verdict
├── sensitivity.py      — parameter sensitivity (E-coli only)
└── expected_output.txt — captured output for verification
```

## Status

The *E. coli* package is an **illustrative worked example** (minimal linear model)
showing that $\eta_v = I_{\text{pred}}/I_{\text{mem}}$ is finite, measurable, and
$O(0.1)$ — not a calibrated value for the real organism. The other four packages
print **structural verdicts** $(S, \eta_v)$ and the quantities that survive the
refounding (e.g. the thermostat's $I_{\text{pred}} \le 3$ bits, the biosphere's
carrier-capacity ceilings); numeric $\eta_v$ for those cases requires a separate
MI estimate of $I_{\text{pred}}$ and $I_{\text{mem}}$ (future work).
