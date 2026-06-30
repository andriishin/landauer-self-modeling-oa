# Worked Example: structural verdict for a large city + I_v screening demo

Companion to § 3.6 (Andriishin, *Theory in Biosciences*, in preparation), under
the refounded central quantity $\eta_v = I_{\text{pred}}/I_{\text{mem}} \in [0,1]$.
Self-contained (Python standard library only) with two clearly separated parts:
a structural verdict, and an $I_v$ screening-index demonstration.

## Structural verdict (the § 3.6 claim)

A city **passes both axes**:

- $S = 1$ — it self-funds from its own municipal budget (condition i) and bears a
  closed error-return loop: a distorted flow-model returns as a crisis to the city
  itself (condition ii);
- $\eta_v > 0$ — it holds predictive structure about its own flows.

So the city is **vital**. The **grade** — the numeric value of
$\eta_v = I_{\text{pred}}/I_{\text{mem}}$ among vital systems — is **not asserted**
here: it requires an MI estimate of $I_{\text{pred}}$ and $I_{\text{mem}}$ of the
administrative loop (resource flows → decisions), left to future work. The
paradigm-case claim is the **closed self-payment loop**, not any smallness of an
efficiency. The old energetic-denominator computation is removed.

## I_v screening-index demonstration (formula 2b + 2a)

$$I_v = \sqrt[3]{\tilde{T}_v \cdot \tilde{C}_v \cdot \tilde{S}_v} \in [0,1], \tag{2b}$$

where $\tilde{T}_v, \tilde{C}_v, \tilde{S}_v$ are the percentile-normalised
(formula 2a) capacities within a cohort. Per main § 2.5, $I_v$ is a **structural
screening** composite — it does **not** make the alive/not call (that is $\eta_v$'s
job); it only screens structural readiness. The demo runs on an explicitly
**synthetic** set of archetype profiles and shows two things:

- (2a) percentile normalisation maps a raw proxy to a $[0,1]$ rank relative to the cohort;
- (2b) the cube-root (geometric) mean drags the composite toward **any** weak capacity (a profile with one failed axis gets a low $I_v$ even if the other two are high).

This is **not** an empirical ranking of real cities. The empirical calibration of
$I_v$ for specific cities from open data (OECD FUA, CDP Cities, WIPO/OECD REGPAT,
GDELT, OpenStreetMap) is separate work and is deliberately not asserted here.

## Contents

| File | Purpose |
|------|---------|
| `eta_city.py` | Structural verdict ($S=1$, $\eta_v>0$) + $I_v$ screening-index demo on synthetic data |
| `expected_output.txt` | Reference output (LF) for verification |

## Running

```bash
python eta_city.py
```

The output reproduces `expected_output.txt`.

## Status

The city's verdict is **structural** ($S = 1$, $\eta_v > 0$); no $\eta_v$ number is
asserted. The $I_v$ demo exercises formula (2b)+(2a) on synthetic profiles to show
the mechanics of the screening composite; no empirical $I_v$ ranking of real cities
is claimed. Self-contained: standard library only.

## Literature

- **Bettencourt, L. M. A.; Lobo, J.; Helbing, D.; Kühnert, C.; West, G. B.** Growth, innovation, scaling, and the pace of life in cities. *PNAS* **2007**, *104*, 7301–7306. (Scaling of urban metrics — context for the separate empirical $I_v$ work.)
