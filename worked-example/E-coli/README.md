# Worked Example: η_v = I_pred / I_mem for the *E. coli* chemotaxis loop

The central worked example of the paper: an exact computation of the predictive
fraction

$$\eta_v = \frac{I_{\text{pred}}}{I_{\text{mem}}} = 1 - \nu \in [0, 1]$$

for the bacterial chemotaxis loop of *E. coli*. Companion to § 3.5 + Supplementary
§ S3.5 (Andriishin, *Theory in Biosciences*, in preparation). Both numerator and
denominator are **informational** quantities; there is no energetic denominator.
The bacterium is the one paradigm case where $\eta_v$ is computed in full
($S = 1$, $\eta_v \sim O(0.1)$).

## Contents

| File | Purpose |
|------|---------|
| `eta_ecoli.py` | Central computation: exact Gaussian $I_{\text{mem}}, I_{\text{pred}}, \eta_v, \nu$ via a pure-stdlib Cholesky log-determinant; prints the $(\tau_E,\beta_v)$ table, the nostalgia $\beta_v$-scan, and a measurability example |
| `sensitivity.py` | Parameter sensitivity: how $\eta_v$ responds to drift $\tau_E$, past-window $L$, and methylation noise $r$ |
| `expected_output.txt` | Reference output of `eta_ecoli.py` (LF) for reproducibility verification |
| `expected_output_sensitivity.txt` | Reference output of `sensitivity.py` (LF) |

Uses only the Python standard library (`math`); no `numpy`, no external dependency.

## Running

```bash
python eta_ecoli.py
python sensitivity.py
```

The output of `eta_ecoli.py` reproduces `expected_output.txt` bit-for-bit (and
`sensitivity.py` reproduces `expected_output_sensitivity.txt`).
Numerical anchors (in nats; matching Supplementary § S3.5):

- $I_{\text{mem}}$ is **finite** (0.03–0.72 over the sweep) and $\eta_v \in [0,1]$ by the data-processing inequality;
- characteristic $\eta_v \sim O(0.1)$ (e.g. $\tau_E=10, \beta_v=0.9$: $I_{\text{mem}}=0.50$, $I_{\text{pred}}=0.14$, $\eta_v=0.27$);
- nostalgia $\beta_v$-scan at $\tau_E = 5$: $\eta_v \approx 0.29 \to 0.035$ as $\beta_v = 0.3 \to 0.99$.

## Model (Supplementary § S3.5)

Chemotaxis is modelled as a **linear adaptive tracker** in the passive
(immobilised) FRET protocol of Sourjik–Berg / Cluzel — the cell is fixed and the
ligand is driven externally. Per main § 2.1 the immobilisation is **not a
simplification but an operational realisation of Pearl's $\mathrm{do}(a)$
intervention**: exogenously clamping the cell's action severs the
action→environment feedback and restores the Markovianity that the $[0,1]$ bound
presupposes. The passive quantity the protocol measures is therefore the
**interventional** predictive freshness
$$\eta_v^{\mathrm{do}} = \frac{I\!\left(M_t;\, X_E^{(t,t+\tau]} \,\middle|\, \mathrm{do}(a)\right)}{I_{\text{mem}}} \in [0,1],$$
with numerator and denominator in the *same* $\mathrm{do}(a)$ regime (a freely
swimming cell would measure a different, active quantity not bounded by 1). Three
elements:

**(a) Sensory channel** — the ligand log-concentration $s_t$ as an AR(1) process
with correlation time $\tau_E$ (environment drift), driven by microfluidics.

**(b) Internal channel (memory)** — the methylation level
$m_t = \sum_{j \ge 1} w_j\, s_{t-j} + \text{noise}$, a leaky integral of the past
ligand (linearised Tu-type adaptation) with weights $w_j = (1-\beta_v)\beta_v^{j-1}$,
where $\beta_v$ is the adaptation memory. The internal state is $M_t = m_t$, read
via FRET (Sourjik–Berg 2002; Cluzel et al. 2000).

**(c) Windows** — a past window $X_E^{\le t}$ of length $L$ and a future horizon
$X_E^{(t,t+\tau]}$.

Since $(s_t, m_t)$ are jointly Gaussian,

$$I_{\text{mem}} = I(M_t; X_E^{\le t}), \qquad I_{\text{pred}} = I(M_t; X_E^{(t,t+\tau]})$$

are computed **exactly** through log-determinants of covariance matrices (here a
pure-stdlib Cholesky factorisation replacing `numpy.linalg.slogdet`). By the
data-processing inequality $I_{\text{pred}} \le I_{\text{mem}}$, hence
$\eta_v \in [0,1]$ by construction, and $\nu = 1 - \eta_v$. The $\eta_v$ computed
below is thus $\eta_v^{\mathrm{do}}$ — the passive, $\mathrm{do}(a)$-conditioned
freshness — not the unconstrained active value.

## Measurability

The key point is that $I_{\text{mem}}$ depends **only** on the observable
covariances $\text{Cov}(m, s_k)$ and $\text{Cov}(s_i, s_j)$ — both estimable from
time series ($m$ via FRET methylation, $s$ via microfluidics). The operational
debt of the informational denominator is therefore **no worse** than that of a
calorimetric dissipation estimate (the direct answer to the worry that an
informational quantity is harder to measure than calorimetry).

## Nostalgia

Nostalgia $\nu = 1 - \eta_v$ grows ($\eta_v$ falls) when the adaptation memory $\beta_v$
**outpaces** the environment drift $\tau_E$: the cell over-integrates stale
ligand, so the pure-ballast fraction rises. This gives nostalgia a concrete
falsifiable reading — faster drift or slower adaptation → more ballast → lower
predictive fraction. The receptor/cluster count does **not** affect $\eta_v$
directly: scaling the number of independent sensory channels raises numerator and
denominator together and cancels in the ratio.

## Epistemic status of the number

$\eta_v \sim O(0.1)$ is an **illustration of the form**, not a quantitative claim
about real *E. coli*: it comes from a minimal linear model whose purpose is to
show measurability and order of magnitude. The exact experimental mapping (which
FRET readout to identify with $M_t$; the window for $X_E^{\le t}$; truncation of
the cumulant to a finite $\tau_{\text{mem}}$) requires cross-checking against the
primary sources and is left to future work.

## References

- **Berg, H. C.; Brown, D. A.** Chemotaxis in *Escherichia coli* analysed by three-dimensional tracking. *Nature* **1972**, *239*, 500–504.
- **Sourjik, V.; Berg, H. C.** Receptor sensitivity in bacterial signalling (FRET readout of methylation). *PNAS* **2002**, *99*, 123–127.
- **Cluzel, P.; Surette, M.; Leibler, S.** An ultrasensitive bacterial motor revealed by monitoring signaling proteins in single cells. *Science* **2000**, *287*, 1652–1655.
- **Tu, Y.; Shimizu, T. S.; Berg, H. C.** Modeling the chemotactic response of *E. coli* to time-varying stimuli. *PNAS* **2008**, *105*, 14855–14860. (Tu-type adaptation linearised into the leaky integrator.)
- **Shimizu, T. S.; Tu, Y.; Berg, H. C.** A modular gradient-sensing network for chemotaxis in *E. coli* revealed by responses to time-varying stimuli. *Mol. Syst. Biol.* **2010**, *6*, 382.
- **Mehta, P.; Schwab, D. J.** Energetic costs of cellular computation. *PNAS* **2012**, *109*, 17978–17982.

## Status

A **methodological calibration / proof-of-measurability**: it does not claim a
calibrated $\eta_v$ for real *E. coli*, but shows that the predictive fraction
$\eta_v = I_{\text{pred}}/I_{\text{mem}}$ is finite, measurable from observable
correlations, and $O(0.1)$ for chemotactic memory. The bottleneck is the
experimental FRET-readout ↔ $M_t$ mapping and the past-window choice, not the
receptor count. Parameter sensitivity is in `sensitivity.py`.
