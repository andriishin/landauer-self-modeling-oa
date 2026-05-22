<!--
  Supplementary Materials for "Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality".
  Extended discussions, full counterfactual analyses, and sensitivity analyses moved out of the main text.
  References in the main text take the form "see Supplementary § SX.Y".
-->

# Supplementary Materials for "Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality"

This document collects the extended material omitted from the main text to keep it within the Entropy
length corridor (8000–10000 words). The structure mirrors the main-text sections with an "S" prefix: each block
addresses the same topic as its main-text counterpart, but in expanded form.

## S2.1 Operationalizing $I_{\text{pred}}$: the full protocol

Measuring $I_{\text{pred}}$ directly in the sense of Equation (1a) of the main text requires access to all internal
degrees of freedom of the system and is technically impossible for biological, urban, and cosmic systems. The
standardized operationalization fixes four elements for each class of system.

(a) *Sensory channel* $x_t$ — the observable input states. For a bacterium, the ligand concentration at the
chemotactic receptors; for a city, the flow of resources through the infrastructure (energy, matter, information); for
the biosphere, the flux of solar radiation and the geochemical flows.

(b) *Internal channel* $s_t$ — measurable summaries of the configuration $M_t$. For a bacterium, the methylation level
of the adaptation system; for a city, administrative-infrastructural parameters (communication density, decision
density, budget profile); for the biosphere, atmospheric composition and biomass pools.

(c) *Choice of past/future windows* with the value of $\tau$ specified. For a bacterium, the characteristic response
time, of the order of a few generations; for a city, a quarter or a year; for the biosphere, a geological eon.

(d) *Mutual-information estimation method*: Kraskov–Stögbauer–Grassberger; plug-in with bias correction; neural-MI
estimation via a critic.

The proxies are not the definition of $I_{\text{pred}}$; they are its operationalization. The same discipline applies
throughout physical measurement: temperature is measured not by directly counting molecular velocities but
through a calibrated proxy — the expansion of mercury. A discrepancy between different proxies for one system is a
signal to refine the proxies, not to abandon the concept.

*Why predictive rather than stored information.* Still, Sivak, Bell, and Crooks set the precedent for a thermodynamic
link between predictive information and dissipation in their work on the thermodynamics of prediction [Still2012].
In the stationary regime with optimal coding, the information $I_{\text{stored}}$ that the system retains about its own
past and the predictive information $I_{\text{pred}}$ it holds coincide. In the non-stationary regime their difference
(information-irrelevant memory, *nostalgia*) is diagnostically meaningful and is associated with excess dissipation.
The present framework inherits Still's precedent and adds a key requirement: both the numerator and the denominator of
$\eta_L$ refer to one and the same physical system — the model and the dissipation belong to $X$. This self-payment
requirement separates $\eta_L$ from the classical setting of the thermodynamics of prediction, where the model and the
dissipator may be distinct circuits.

## S2.4 Cohort normalization: extended discussion and the sigmoidal alternative

### Extended discussion of reference cohorts

The specific reference cohorts for the six paradigm cases of Section 3 are fixed as follows.

*Bacteria* (§ 3.5): a cohort of prokaryotic chemotactic systems, $n \sim 200$ from BiGG/KEGG models (*E. coli*,
*B. subtilis*, *V. cholerae*, and the like).

*Cities* (§ 3.6): 120–500 large cities from the Bettencourt dataset [Bettencourt2007].

*Biosphere* (§ 3.7): the only case for which percentile normalization is impossible owing to the absence of a cohort;
in its place, normalization by a theoretical upper limit is used — the planetary net primary production NPP
$\sim 10^{14}$ W is taken as the $T_v$ norm.

*Large language model* (§ 3.4): a cohort of the most recent generations of foundation models, $n \sim 50$ since 2020.

*Stars* (§ 3.1): a main-sequence cohort, $n \sim 10^4$ from the Hipparcos catalogue.

*Crystal and hurricane* (§§ 3.2–3.3): normalization by zero — the structural zero $T_v = 0$ or $C_v = 0$ is set not by
position within a cohort but by a constructive failure of the corresponding capacity (absence of own dissipation
paying for the maintenance; absence of held predictive information). Formally: $\tilde{T}_v(X) := 0$ is adopted by
convention for $X$ with $T_v(X) = 0$, and $\tilde{T}_v(X) := 1$ for $X$ with $T_v(X) \ge \max_{\text{cohort}} T_v$;
within the support of the reference cohort — Equation (2a) of the main text.

### The sigmoidal alternative

An alternative to percentile normalization is sigmoidal normalization $\tilde{T}_v = T_v / (T_v + T_v^{\text{ref}})$,
with an independently chosen reference value $T_v^{\text{ref}}$ for each capacity. The sigmoidal procedure yields
an absolute scale and applies to unique systems, but it requires justifying $T_v^{\text{ref}}$,
$C_v^{\text{ref}}$, and $S_v^{\text{ref}}$ from independent physical considerations. This work uses the percentile
procedure and retains the sigmoidal one as an alternative for applications that require an absolute scale or
that operate on unique systems.

## S3.4 Counterfactual screening of the LLM: full component-by-component analysis

We apply the counterfactual procedure of § 2.2 of the main text to the concrete case of a large language model. The
candidates for inclusion in the boundary are examined in sequence.

*Parametric weights (static after training).* Removal: the model does not respond; outright failure of the loop. They
belong to the boundary of the generator, but not to the operating circuit at the moment of inference (the weights are
not updated by the error).

*KV-cache (runtime context memory).* Removal: the model loses the conversation context; over a window
$\tau \sim$ the session time, $\Delta(-dF_X/dt) > 0$. It belongs to the boundary on session timescales.

*Runtime server (GPU + OS).* Removal: computation is impossible. It belongs to the mechanism boundary, but the energy
is supplied by the external power grid.

*Owner corporation (decision-maker over training, deployment, payment).* Removal: the model in its current form ceases
to be updated (no new versions), but the current version keeps running on the residual infrastructure. The corporation
is external relative to the current version of the model; it enters the boundary when one considers the evolution of
the model lineage over time.

Counterfactual screening yields two different verdicts depending on the chosen window. On the short session scale, the
LLM boundary = {weights + KV-cache + runtime server}: $\eta_L > 0$ through the numerator, but $\eta_L \to 0$
through the denominator, because the external power grid, not own dissipation within the boundary, pays for the
computation. On the evolutionary scale (generations of models) the boundary expands to the corporation, and
$\eta_L$ is then assigned to the corporate system — with its own financial flows, errors, and survival — not to the
model as an agent. Counterfactual screening therefore grants the LLM vital status on neither scale; it
operationalizes the intuition on which the diagnosis of § 3.4 of the main text rests.

## S3.5 Worked example E. coli: detailed sensitivity analysis

### Full calculation parameters

*Numerator.* The sensory channel $x_t \in \{0, 1\}$ is the binarized sign of the temporal gradient of the aspartate
concentration (positive/negative) at a step of $\delta t \sim 0.1$ s (the characteristic response time of a single
receptor cluster). The internal channel $s_t \in \{0, 1, 2, 3, 4\}$ is the number of methyl groups on the Tar receptor
(five discrete states of the adaptation system). The prediction window $\tau \approx 10$ s is the characteristic
adaptation time of the methylation system. The model of Tu et al. 2008 [Tu2008, ShimizuTuBerg2010] gives the
transition probabilities $P(s_{t+\delta t} \mid s_t, x_t)$ analytically from the stationary distribution of the Markov
process. Alternatively, $I(s_t; x_{t+\tau})$ is estimated numerically with the KSG (Kraskov–Stögbauer–Grassberger)
estimator on simulated trajectories.

For a single receptor cluster within the window $\tau$ one obtains $I_{\text{pred}} \approx 1$–$10$ bits
[MehtaSchwab2012, Cheong2011], an order of magnitude consistent with the information-theoretic analysis of biochemical
signaling. A typical *E. coli* carries $\sim 7\,000$ Tar receptors organized into clusters, and integrating over all
clusters yields $I_{\text{pred}} \sim 10^3$–$10^4$ bits per generation. This is an estimate for a single sensory
module; including Tsr, Trg, Tap, and Aer scales $I_{\text{pred}}$ approximately linearly with the number of sensors.

*Denominator.* The heat output of *E. coli* in the stationary growth phase is $\sim 1$–$3$ pW per cell [Liu2020]. Over
a generation $\tau_d \sim 30$ min $\approx 1.8 \cdot 10^3$ s, the total dissipation is
$E_{\text{actual}}^{\text{total}} \sim 2 \cdot 10^{-9}$ J/cell. The exergetic efficiency of metabolism — the fraction
of the free energy of glucose representable as an ATP equivalent — is estimated at
$\eta_{\text{ex}} \sim 0.4$–$0.6$. The exergetic part physically able to pay for Landauer erasures is
$E_{\text{actual}} = E_{\text{actual}}^{\text{total}} \cdot \eta_{\text{ex}} \sim 10^{-9}$ J/cell. At $T = 310$ K the
minimal cost per bit is $k_B T \ln 2 \approx 3 \cdot 10^{-21}$ J, whence

$$N_{\text{max}} = \frac{E_{\text{actual}}}{k_B T \ln 2} \sim \frac{10^{-9}}{3 \cdot 10^{-21}} \sim 3 \cdot 10^{11} \;\text{bits per cell}.$$

This is the first, *exergetic*, bound: the number of bits the cell could in principle erase if all its free energy
went into logically irreversible information operations. In reality only a small fraction of the exergy — of order
$10^{-3}$ [MehtaSchwab2012] — goes into irreversible information operations; the rest goes to biomass
synthesis, the maintenance of ionic gradients, and thermal losses. The corresponding *computational* bound is
$E_{\text{comp}} \sim 10^{-3} \cdot E_{\text{actual}} \sim 10^{-12}$ J/cell, and
$N_{\text{max}}^{\text{comp}} = E_{\text{comp}}/(k_B T \ln 2) \sim 3 \cdot 10^{8}$ bits/cell.

### Sensitivity analysis

Varying the window $\tau$ over $1$–$100$ s shifts $I_{\text{pred}}$ by $\pm 1$ order of magnitude:
on short windows the Markov model yields less information, and on long ones it saturates at the limit imposed by
the adaptation memory.

The binning of $x_t$ (binary versus 4-level) changes $I_{\text{pred}}$ by $\sim 30\%$ — substantially less than the
uncertainty in the number of receptor clusters.

Including all five receptor families (Tar, Tsr, Trg, Tap, Aer) scales $I_{\text{pred}}$ approximately linearly with
the number of sensors, leaving $\eta_L$ within one order of magnitude.

The estimate of $\eta_{\text{ex}}$ ($0.4$ versus $0.6$) changes the denominator — and the resulting $\eta_L$ — by a
factor of $\sim 1.5$.

The resulting conservative estimate, accounting for all sources of uncertainty:
$\eta_L \in [10^{-9}, 10^{-7}]$ through the exergetic denominator and
$\eta_L^{\text{comp}} \in [10^{-6}, 10^{-4}]$ through the computational denominator.

### The bottleneck of the calculation

The bottleneck is estimating $I_{\text{pred}}$ for the full sensory system: the number of receptor clusters
varies across strains and conditions and is taken here from literature estimates, not from first principles. The
precise value requires simultaneous MI measurements on all known sensory channels of a single population, and this
defines the content of the accompanying experimental program. The full reproducible calculation with code is provided
as part of the Supplementary Materials (Python sources, captured outputs, parameter documentation).

## S4.4 Counterfactual screening of the thermostat: full component-by-component analysis

We apply the counterfactual procedure of § 2.2 to a bimetallic thermostat $X$ with hysteresis
$\Delta T_{\text{hyst}} = 1$ K, controlling a room with a thermal inertia $\tau_{\text{room}} \sim 30$ min. The
candidates for inclusion in the boundary of $X$ are enumerated in sequence.

*Bimetallic strip (sensor + actuator).* Removal: the loop is broken, no regulation at all.
$\Delta(-dF_X/dt) > 0$ on timescales $< \tau_d$. It belongs to the boundary.

*Relay contact group (energy gating).* Removal: the same — the loop is broken. It belongs to the boundary.

*Heating element (effector via the external power grid).* Removal: the heat source disappears; the bimetallic strip
and the relay remain, but the $-dF_X/dt$ of the remaining system tends to zero not through a failure of the loop but
through the exhaustion of its own free energy (the bimetallic strip slowly cools to ambient). It does not belong
to the decision loop and is an external component.

*Power grid as a current source.* Analogous to the heater: external.

*Set-point operator (external operator).* Removal: the set-point is fixed, regulation is preserved. External.

The boundary of the thermostat under counterfactual screening is {bimetallic strip, relay}. Within the boundary,
$E_{\text{actual}}$ is the elastic relaxation of the metal plus the dissipation of the relay, $\sim 10^{-6}$ W. The
internal channel that holds predictive information about the room temperature is the deformation of the
bimetallic strip, with $I_{\text{pred}} \le \log_2(\Delta T_{\text{room}}/\Delta T_{\text{hyst}}) \sim 5$ bits.
Crucially, this $I_{\text{pred}}$ refers to the environment "the room," not to the environment "thermostat + room +
power supply." The loop of decisions paid for by the system's own decay is incomplete for the thermostat: the
room is heated by the external power grid, not by the bimetallic strip's own free energy.
Counterfactual screening yields $\eta_L^{\text{thermostat}} > 0$ only for the trivial task of "maintaining the
bimetallic strip's own shape," not for the control task of "regulating the room temperature." The discrepancy between
these two interpretations is exactly what Bruineberg et al. call the transition from a Pearl blanket to a
Friston blanket: one and the same physical system admits several self-consistent boundaries, and the choice between
them is a methodological, not an ontological, discipline.

## S4.4a Rebutting the critiques of Andrews 2021 and Williams 2020

The well-known critiques of the FEP bear on $\eta_L$ asymmetrically.

Andrews [Andrews2021] — "The math is not the territory" — attacks the FEP for the non-derivability of empirical content
from the formalism: without additional hypotheses, $F$ can be constructed post hoc for any system. $\eta_L$ rebuts this
critique by anchoring the numerator and the denominator to measurable quantities — predictive information
through the proxy $C_v$, exergy through thermodynamic measurements — so that the requirement of a concrete
operationalization removes the freedom of post hoc construction.

Williams [Williams2020] — "Predictive coding and thought" — attacks predictive coding as a neural mechanism, not the
FEP as a principle; this critique is neutral to $\eta_L$, because the program does not assert predictive coding as a
mechanism but uses predictive information as a formal measure, methodologically independent of any specific neural
architecture. The distinction is fundamental for a coherent defense against conflated critique: predictive coding
[RaoBallard1999, Clark2013] is a neuroarchitectural hypothesis, whereas predictive
information [Bialek2001] is an information-theoretic measure.
