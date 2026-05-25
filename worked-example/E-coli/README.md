# Worked Example: η_L for the *E. coli* chemotaxis loop

A reproducible computation of the Landauer efficiency of self-modeling $\eta_L$ for the bacterial chemotaxis loop of *E. coli*. Companion to the paper «Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality» (§ 3.5 + Supplementary § S3.5).

## Contents

| File | Purpose |
|------|---------|
| `eta_L_ecoli.py` | Central computation: $\eta_L$ and $\eta_L^{\text{comp}}$ via the exergetic and the computational denominators; prints a results table |
| `sensitivity.py` | Monte Carlo sensitivity analysis: spread of $\eta_L$ over the ranges of $I_{\text{pred}}, E_{\text{actual}}, \eta_{\text{ex}}, T$ |
| `expected_output.txt` | Reference output of `eta_L_ecoli.py` for reproducibility verification |
| `requirements.txt` | Minimal dependency set (numpy, matplotlib) |

## Running

```bash
pip install -r requirements.txt
python eta_L_ecoli.py
python sensitivity.py
```

The output of `eta_L_ecoli.py` should match `expected_output.txt` up to floating-point round-off. Numerical anchors:

- $N_{\text{max}}^{\text{ex}} \approx 3 \cdot 10^{11}$ bits per cell (exergetic budget);
- $N_{\text{max}}^{\text{comp}} \approx 3 \cdot 10^{8}$ bits per cell (computational, $\eta_{\text{ex}}^{\text{comp}} = 10^{-3}$);
- $\eta_L \approx 3 \cdot 10^{-8}$ through the exergetic denominator;
- $\eta_L^{\text{comp}} \approx 3 \cdot 10^{-5}$ through the computational denominator.

## Model

The computation follows the protocol of Supplementary § S2.1 (the four elements of operationalizing $I_{\text{pred}}$).

**(a) Sensory channel $x_t$** — the concentration of the ligand (attractant or repellent) at the cell's chemotaxis receptors. The estimate uses an order-of-magnitude range from [Sourjik2002, Endres2008].

**(b) Internal channel $s_t$** — the methylation level of the receptor clusters (Tar, Tsr, Trg, Tap, Aer). The methylation states act as a short-term adaptation memory with a characteristic time of seconds to minutes [Korobkova2004].

**(c) Past/future windows with $\tau$** — a characteristic memory window $\tau \approx 10$–$100$ s (the characteristic methylation/demethylation time) $\times$ a generation window of $\sim 30$–$60$ min.

**(d) Mutual-information estimate $I_{\text{pred}}$** — literature estimates converge on $I_{\text{pred}} \in [10^{3}, 10^{5}]$ bits per cell per generation, with a central estimate of $10^{4}$ bits [ShimizuTuBerg2010, Cheong2011, MehtaSchwab2012]. In the sensitivity analysis it is varied over the full range.

## Denominator

$N_{\text{max}}$ is defined via equation (1) of the main text:

$$N_{\text{max}} = \frac{E_{\text{actual}}}{k_B T \ln 2}$$

where

- $E_{\text{actual}} = E_{\text{actual}}^{\text{total}} \cdot \eta_{\text{ex}}$ — the exergetic fraction of the total free energy that physically pays for holding $I_{\text{pred}}$;
- $E_{\text{actual}}^{\text{total}} \sim 10^{-9}$ J/cell/generation (the metabolic budget, an ATP equivalent on the order of $10^{10}$ molecules);
- $\eta_{\text{ex}} \approx 1$ for the exergetic denominator (all available free energy);
- $T = 310$ K (physiological temperature);
- $k_B T \ln 2 = 2.967 \cdot 10^{-21}$ J/bit at $T = 310$ K.

The computational denominator uses $\eta_{\text{ex}}^{\text{comp}} \approx 10^{-3}$ — the fraction of exergy that goes to irreversible information operations; the rest is spent on biomass synthesis and ion gradients [MehtaSchwab2012, Lan2012].

## Literature

- **Berg, H. C.; Brown, D. A.** Chemotaxis in *Escherichia coli* analysed by three-dimensional tracking. *Nature* **1972**, *239*, 500–504.
- **Sourjik, V.; Berg, H. C.** Receptor sensitivity in bacterial signaling. *PNAS* **2002**, *99*, 123–127.
- **Korobkova, E.; Emonet, T.; Vergassola, M.; Cluzel, P.** From molecular noise to behavioural variability in a single bacterium. *Nature* **2004**, *428*, 574–578.
- **Endres, R. G.; Wingreen, N. S.** Accuracy of direct gradient sensing by single cells. *PNAS* **2008**, *105*, 15749–15754.
- **Shimizu, T. S.; Tu, Y.; Berg, H. C.** A modular gradient-sensing network for chemotaxis in *Escherichia coli* revealed by responses to time-varying stimuli. *Mol. Syst. Biol.* **2010**, *6*, 382.
- **Cheong, R.; Rhee, A.; Wang, C. J.; Nemenman, I.; Levchenko, A.** Information transduction capacity of noisy biochemical signaling networks. *Science* **2011**, *334*, 354–358.
- **Lan, G.; Sartori, P.; Neumann, S.; Sourjik, V.; Tu, Y.** The energy–speed–accuracy trade-off in sensory adaptation. *Nat. Phys.* **2012**, *8*, 422–428.
- **Mehta, P.; Schwab, D. J.** Energetic costs of cellular computation. *PNAS* **2012**, *109*, 17978–17982.
- **Landauer, R.** Irreversibility and heat generation in the computing process. *IBM J. Res. Dev.* **1961**, *5*, 183–191.

## Status

The computation is a *methodological calibration*: it does not claim accuracy better than one order of magnitude per parameter and three orders of magnitude in the resulting $\eta_L$. The substantive claim is the robustness of the difference $\eta_L \ll 1$ and the qualitative relation $\eta_L^{\text{comp}} / \eta_L \sim 10^{3}$, which reflects the fraction of free energy directed to irreversible information operations. The full sensitivity map is in `sensitivity.py`.
