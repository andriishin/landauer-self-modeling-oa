<!--
  English version of the article (translated from the Russian primary source main.ru.md).
-->

# Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality

**Authors:** Alexander Andriishin ¹\*

¹ Independent Researcher, Moscow, Russia. ORCID: 0009-0000-4739-4017 (https://orcid.org/0009-0000-4739-4017)
\* Correspondence: alexander@andriishin.com

## Abstract

Complexity is ubiquitous, life is rare: stars, hurricanes, crystals, and language models are far from equilibrium, yet none closes a self-payment loop in which the model and the dissipation maintaining it belong to one physical boundary. A closed loop of *self-payment* separates the vital from the merely complex; we make it quantitative. We define vitality as the **Landauer efficiency of self-modeling**: the dimensionless ratio of the predictive information a system holds about its environment to the Landauer budget of its dissipation. Its upper bound is a conditional consequence of Landauer's principle under the stationary-accounting postulate. The decisive condition is *self-payment*: numerator and denominator belong to one physical system. Unlike assembly theory, integrated information, teleodynamics, and the free energy principle, the scale requires the model and its paying dissipation to share one boundary. A two-stage procedure—structural screening, then vital verification—is applied to six paradigm cases from a star to a metropolis, with *E. coli* chemotaxis computed in full. Structural potential is nearly universal; closed self-payment loops are rare. Three operational consequences follow: extraterrestrial-life searches must detect such loops beyond chemical biosignatures; the ethical status of an artificial system becomes whether it has begun to pay for its own model; and the boundary between the structurally complex and the vital is the positivity of the efficiency, a necessary condition. The theory addresses the stationary regime; a companion work treats the non-stationary case. The programme is open to refutation along eight independent lines, including a power-law dependence of adaptation rate on this efficiency.

## Keywords

definition of life; self-modeling; predictive information; Landauer's principle; origin of life;
thermodynamics of computation

## 1. Introduction

The concept of the "living organism" has no commonly accepted formal definition in modern biology. Historically it
rested on a cellular substrate—carbon chemistry, membrane organisation, metabolic closure—but its
boundaries are blurred both from below and from above. From below: viruses lack autonomous metabolism, yet participate in
evolutionary dynamics (Pradeu 2018); prions and replicator RNA systems reproduce without cellular
infrastructure; protocellular and abiogenetic transitional forms preclude a sharp boundary between
chemistry and biology (Plante 2025). From above: biospheres, symbiotic communities, and anthropogenic megastructures
display signs of collective self-regulation and evolutionary adaptation without a single cellular
referent (Mossio et al. 2016). In response to these difficulties, the philosophy of biology of the past two decades has
developed a robust **epistemological pluralism**:

- registries of a hundred or more competing definitions of life with no signs of convergence (Trifonov 2011);
- the argument for the need for a "theory of life" instead of a dictionary definition (Cleland 2019);
- the programme of cluster definitions (Mariscal and Doolittle 2020);
- the conception of the organism as a biologically individuated system (Bich and Green 2018; Pradeu 2018). 

No definition wins
unanimous acceptance; there is a growing demand for operational criteria capable of applying to non-standard
candidates—astrobiological findings, artificial systems of complex information processing traditionally
called cognitive, hybrid ecological complexes (Chirumbolo and Vella 2026).

Parallel to the philosophical work, a line of technical programmes has developed that formalise individual sides of
vitality:

- Schrödinger's formula "life feeds on negentropy" (Schrödinger 1944) isolates the thermodynamic aspect—
  the maintenance of order at the expense of dissipation into the environment;
- Friston's free energy principle (FEP) (Friston 2005, 2010)—the Bayesian side, the minimisation of
  variational free energy as a generalised sign of the living;
- the assembly theory of Walker and Cronin (Marshall et al. 2017; Sharma et al. 2023)—the combinatorial complexity of assembling a molecular
  object as a biosignature;
- Tononi's integrated information $\Phi$ (Tononi 2004; Tononi et al. 2016)—the causal closure of an informational
  structure;
- Deacon's teleodynamics (Deacon 2011)—the self-emergence of norms and goal-likeness from far-from-equilibrium constraints;
- Levin's cognitive light cone (Levin 2019)—the scale of goal-directed behaviour in state space.

The programmes listed form not a complete set of mutually exclusive hypotheses but a **landscape
of complementary perspectives**, each of which takes one side of vitality seriously and inevitably loses
discriminating power when crossing boundaries. FEP in its pure formulation is formally applicable to a household
thermostat—a fact acknowledged by Friston (2013) and used as diagnostic
in the works of Bruineberg et al. (2018, 2022); assembly theory does not distinguish a living cell from a fossil, $\Phi$
leaves the thermodynamic cost of modeling outside the apparatus. The narrow biocentric definition—
the NASA formula "a self-sustaining chemical system capable of Darwinian
evolution" (Joyce 1994; Cleland and Chyba 2002)—correctly describes terrestrial biology but does not answer the question of
substrate generality. A gap arises: at the level of general formulations all sides of
vitality are intuitively recognised as necessary, whereas at the level of a formal criterion one turns out to carry the
load and the rest dissolve into the background. From this landscape follows a bridge to our programme:
an operational measure that would join the thermodynamic payment and the quality of the maintained model into a single
dimensionless scale.

Parallel to the line of purely demarcational debates, a modern programme of research into the
**origin of life** has developed. It comprises the Eigen–Schuster hypercycle (Eigen 1971; Eigen and Schuster 1979),
autocatalytic sets and RAF networks (Hordijk and Steel 2004; Hordijk 2019), dissipative
adaptation (Perunov, Marsland, and England 2016), major transitions in evolution
(Maynard Smith and Szathmáry 1995), and geochemical
programmes (Pross 2012; Smith and Morowitz 2016; Kauffman 2019). This programme operationalises the abiotic→biotic transition
as the formation of a self-sustaining information–energy loop over a geochemical flow.
The $\eta_L$ programme does the same in a quantitative thermodynamic register: the positivity of $\eta_L$
is a necessary condition for the moment of the origin of life. The systematic comparison with the five lines of OoL is
in § 4.8; the consequences for the astrobiological search for the transition are in § 6.

The same limitations show through in astrobiology over the past three decades. Biosignatures based on chemical disequilibrium (the simultaneous
presence of $\text{O}_2$ and $\text{CH}_4$), on isotopic signatures ($\delta^{13}\text{C}$ beyond abiotic
ranges), on chirality all have abiotic alternatives. Three cases illustrate the pattern: the arsenate-substitution claim in the DNA of strain GFAJ-1 (*Halomonadaceae*) (Wolfe-Simon et al. 2011 [retracted by *Science* 2025]; Reaves et al. 2012), the methane
anomalies on Mars (Webster et al. 2018; Korablev et al. 2019), and phosphine on Venus (Greaves et al. 2021; Villanueva et al. 2021). Each shows that, without
a high-order vital criterion, the debate reduces to the interpretation of particular proxies. The same limit confronts the
discussion of the vitality of large language models: without an operational criterion, the discussion of "understanding" reduces to
an enumeration of functional capabilities and a comparison with the benchmark of human behaviour.

The AI alignment literature approaches the same structural question from another side: under what architectural conditions does
an optimising agent begin to optimise its own continuation (Bostrom 2014; Hubinger et al. 2019; Carlsmith 2022).
This article and the AI-safety literature share an overlapping structural object and differ in angle of view: AI-safety describes
the behavioural signs of an emerging loop, $\eta_L$ describes its thermodynamic root (the closure of the physical self-payment
loop); the detailed comparison is in § 3.4.

Here we define vitality as the efficiency with which a system maintains its own model through its own dissipation.

We use *self-modeling* in a sense distinct from Metzinger's phenomenal self-model: here it denotes a structural condition in which the model of the environment, the dissipation that pays for it, and the agent bearing its errors all belong to one physical system — the *self* is the bearer of the model and its cost, not the content of the model. Likewise, *vitality* here is a strictly operational, thermodynamic property (the Landauer efficiency $\eta_L$), not the *vis vitalis* of the vitalist tradition.

The central object is the dimensionless ratio

$$\eta_L = \frac{I_{\text{pred}}}{N_{\text{max}}}, \quad N_{\text{max}} = \frac{E_{\text{actual}}}{k_B T \ln 2}.$$

where $I_{\text{pred}}$ is the predictive information about its own environment, maintained by the system's internal structure.
The exact definition and the connection with the classical formulation of Bialek–Nemenman–Tishby (Bialek et al. 2001) are in § 2.1.
$E_{\text{actual}}$ is the total free energy (exergy) that physically pays for the maintenance of this information
over the characteristic dissipation window $\tau_d$. $T$ is the temperature of the receiving heat bath. The denominator $N_{\text{max}}$ is the Landauer
budget (Landauer 1961): the maximum number of bits that can be erased on the available free
energy under an ideal irreversible realisation. The ratio $\eta_L \in [0, 1]$ is an intensive characteristic, independent of substrate, environment, or size of the
system. The range holds in the irreversible computational regime, where Landauer's principle sets the lower
bound $k_B T \ln 2$ per bit of erasure. The Bennett regime of reversible computation (Bennett 1973, 1982) requires
a redefinition of the scale (see § 2.1).

The programme unfolds in three constructive steps. The first is the operational definition of the vital scale as $\eta_L$,
explicitly distinguished from indices of complexity (assembly index, $\Phi$, $I_v$ as a composite of three capacities): the scale remains
positive only for systems with self-payment, where the system's own model of the environment and its own dissipation are simultaneously separable.
The second is the separation of two methodological levels: structural screening through the composite index $I_v = \sqrt[3]{T_v C_v S_v}$
and vital verification through $\eta_L$ (a computational economy, not a logical strengthening). The third is the explicit
conventionality of the system boundary as a methodological instrument: $\eta_L$ depends on the choice of boundary, and this
dependence is productive—it allows one to distinguish "the vitality of an LLM as an agent" (equal to zero) from "the vitality of a corporation"
(non-zero, but referring to a different object).

The novelty lies not in the individual components. Predictive information (Bialek et al. 2001) and the Landauer bound (Landauer 1961)
have been known for more than half a century. Self-modeling traces back to Rosen's anticipatory systems (Rosen 1985); the requirement of one's own
payment for the model converges with Taleb's skin in the game (Taleb 2018) and the autopoiesis of Maturana–Varela (Maturana and Varela 1980). The novelty lies
in the architecture of their combination along three points. The specific ratio $I_{\text{pred}}/N_{\text{max}}$ as an independent
object has not appeared in the Bialek–Nemenman–Tishby literature. The requirement that numerator and denominator belong to one
physical system (self-payment) has not previously been formalised in explicit form as a criterion of vitality—both Landauer and
Bialek worked without it. The interpretation
of the resulting ratio as a vital scale is an independent step that none of the source frameworks took.

The proposed definition is not a metaphysical declaration. $\eta_L$ is an operational representation of vitality as a
mode of existence, not its definition in essence. The standard philosophical distinction between the referent of a theory
(a property of the system) and the operationalisation (a relation between the system and the measurement frame) is analogous to the distinction
between "temperature as a measure of thermal energy" and "the logarithm of the expansion of mercury over 100 graduations," or between "the strength of an earthquake" and
"the Richter scale." $\eta_L$ is an operational measure disciplined by a specific definition.

We deliberately restrict ourselves to the **stationary regime**, where the assumption of finite memory and ergodicity of the
environment allows the Bayesian update of the model to be reduced to instantaneous Landauer erasure. In this regime the formalism
gives sharp demarcational answers and testable predictions. The non-stationary regime—growing memory, drifting
environment, cumulative budget—lies beyond the scope of this work and is developed in the companion work (Andriishin 2026).
There, Lemma 2 is proved on the inevitability of informational nostalgia in the OU-class of slow drift under the technical conditions
enumerated there. A hypothesis is also formulated about the adiabatic asymptotics of
$\dot{\eta}_L^{\text{excess}}$ for systems without periodic memory reset.
The applicability of the apparatus of this work is restricted to systems with an ergodic environment and finite memory; for biospheres
on eon-scale windows, AI systems learning under drift, and civilisations with a growing archive, one should turn to the
non-stationary extension.

Structure of the article: § 2 unfolds the formal framework; § 3 applies the procedure to six paradigm-case systems; § 4
compares it with adjacent programmes (assembly theory, IIT, teleodynamics, FEP) and positions it relative to
the lines of organisational closure, the origin of life, and modern demarcational debates; § 5 formulates
the conditions of falsification; § 6 discusses the consequences for astrobiology, AI ethics, and complex systems; § 7 sums up.
## 2. Theoretical Framework

### 2.1 The central quantity

The vitality of a system $X$ over a window $\tau_d$ is defined as the ratio of two quantities. The numerator is the predictive
information held by the internal structure of $X$ about its own environment $X_E$; the denominator is the Landauer budget
of the system's own dissipation over the same window:

$$\eta_L(X, \tau_d) = \frac{I_{\text{pred}}(X; \tau_d)}{N_{\text{max}}(X; \tau_d)}, \quad N_{\text{max}} = \frac{E_{\text{actual}}}{k_B T \ln 2}. \tag{1}$$

Concretely, for a bacterium: the numerator is what the methylation pattern of the chemoreceptors "knows" about the future gradient; the denominator is the Landauer budget of the cell's metabolic dissipation, which pays for that knowledge (full computation in § 3.5).

The numerator is the predictive information held by the internal structure $M_X$ of system $X$ about a future window $\tau$ of its
own environment $X_E$:

$$I_{\text{pred}}(X, \tau) := I\!\left(M_t;\; X_E^{[t,\,t+\tau]}\right), \tag{1a}$$

where $M_t$ is the configuration of those internal degrees of freedom of $X$ at time $t$ that pass the counterfactual
ablation of § 2.2 as belonging to the modeling loop (a functional channel, not the full internal configuration),
and $X_E^{[t,\,t+\tau]}$ is the environmental trajectory over the window $[t, t+\tau]$. Not all of the configuration of $X$ belongs to $M_t$ in the sense of (1a):
the functional channel, identified through counterfactual ablation (§ 2.2) as carrying predictive information about the environment, is singled out from the overall configuration. For a bacterium, $M_t$ is the methylation pattern of the Tar receptors, not the full
internal configuration of the cell ($\sim 10^{10}$ DOF). This narrow proxy operator makes (1a) operational. The numerator
of $\eta_L$ is this functional channel, not the full mutual information (MI) $I(X; X_E)$ over all
degrees of freedom of the system. The latter would be many orders of magnitude larger because of **non-functional couplings** with
the environment — heat exchange, mechanical contact, diffusion. Such couplings statistically link $X$ and $X_E$ but carry no
predictive information about its future behaviour. This quantity differs from the classical predictive information
of Bialek, Nemenman and Tishby (Bialek et al. 2001),
defined as the mutual information between the past and the future of a single process:

$$I_{\text{pred}}^{\text{Bialek}}(X_E, \tau) := I\!\left(X_E^{[t-\tau,\,t]};\; X_E^{[t,\,t+\tau]}\right).$$

The link is given by the data processing inequality (DPI; information about a random variable
does not increase under deterministic processing): if $M_t$ is a function of the past environmental trajectory, then
$I(M_t;\, X_E^{[t,\,t+\tau]}) \le I(X_E^{[t-\tau,\,t]};\, X_E^{[t,\,t+\tau]})$. Here $M_t = f(\{x_s\}_{s \le t})$ is a
function of the past sensory channel. For systems with active sampling (motor feedback in a bacterium,
administrative intervention in a city) the bridge is formulated as
$I(M_t;\, X_E^{[t,\,t+\tau]} \mid \pi) \le I(X_E^{[t-\tau,\,t]};\, X_E^{[t,\,t+\tau]} \mid \pi)$ at a fixed
policy $\pi$. In the stationary regime the operating point $(p^*(s), \pi^*)$ is consistent;
the conditioning is technically realised through ergodic averaging over this consistent pair. The substantive step of the framework is the extension of
predictive information from the process's own memory to the information held by the system about its environment.

The denominator is the number of bits erased on the available free energy (exergy) of $X$ in the irreversible regime at the lower
Landauer bound (Landauer 1961). Two quantities are distinguished. $E_{\text{actual}}$ is the **free energy supplied**
over the window $\tau$ (the free energy of the catabolised substrates). In the stationary regime of the cell it equals the total
integral dissipation: in the stationary state all of the supplied free energy is ultimately dissipated —
the work of maintaining the non-equilibrium state, structural wear, ion gradients and direct heat release exhaust the
input. When estimating $E_{\text{actual}}$ by calorimetry, the standard energy balance
$E_{\text{actual}} \approx Q_{\text{heat}} / (1 - \eta_{\text{ATP}})$ is used, where $\eta_{\text{ATP}}$ is the fraction of free
energy retained as useful work (ATP) at the moment of measurement. Stucki's efficiency of oxidative
phosphorylation $\eta_{\text{ex}} \sim 0.4$–$0.6$ (Stucki 1980; the operational ratio of output power to
input power in the Kedem–Caplan formalism) is a constitutive characteristic of the oxphos machinery, related to
$\eta_{\text{ATP}}$ through the growth phase (see the unification paragraph below). For a bacterium in the stationary phase over a
generation window, $\eta_{\text{ATP}}$ is small, and calorimetry gives a good approximation to the total exergy. $E_{\text{comp}}$ is
the actual dissipation on irreversible information operations. For biological systems
$E_{\text{comp}}/E_{\text{actual}} \ll 1$: in a bacterium the information-operational fraction is estimated at the level of
$\sim 10^{-3}$, the rest of the exergy going to biomass, ion gradients and heat losses. It is precisely $E_{\text{actual}}$, as the supplied free
energy, that enters $N_{\text{max}}$: the lower Landauer bound is meaningful for free
energy, not for arbitrary heat. Accordingly, two denominators of $\eta_L$ are distinguished: the exergetic denominator
$E_{\text{actual}}$ — the total supplied free energy over the window $\tau$, paying for all forms of maintaining the
non-equilibrium state; and the computational denominator $E_{\text{comp}}$ — only its information-relevant part. A numerical illustration
of the difference on the chemotactic loop of *E. coli* is given in § 3.5 ($\eta_L \sim 3 \cdot 10^{-8}$ via the exergetic denominator
and $\eta_L^{\text{comp}} \sim 3 \cdot 10^{-5}$ via the computational denominator).

*Terminological note.* The "efficiency" index in the notation $\eta_L$ is conventional: this is not the Carnot efficiency of a heat engine, but the fraction of the Landauer budget $N_{\text{max}}$ actually occupied by the maintenance of predictive information about the environment. Accordingly, the normalisation $\eta_L \in [0, 1]$ is set by the Landauer principle (the lower bound on the irreversible erasure of one bit), not by the second law of thermodynamics.

*Biological relevance of $k_B T \ln 2$ as a normalisation.* The smallness of $\eta_L$ in *E. coli* — $[10^{-9}, 10^{-7}]$
exergetically, $[10^{-6}, 10^{-4}]$ computationally (§ 3.5) — means that the biological system is many orders of magnitude removed from
the Landauer ceiling. This does not undermine the biological relevance of $k_B T \ln 2$: this
scale figures here not as a biologically specific energy scale (biology does not operate "at the ceiling"),
but as a **universal lower bound** on the irreversible erasure of one bit. $\eta_L$ is a dimensionless ratio on
this universal scale, and cross-class comparison is meaningful through the sign and the within-class ordering, not through
proximity to unity. Alternative biological thermodynamic equivalents exist. $\sim 10\,k_B T$ is a characteristic of the
energetic price of a single act of receptor binding at the threshold of concentration discrimination (a lower bound on the capacity of
the concentration channel in the spirit of Berg and Purcell (1977), developed in Mehta and Schwab (2012)). $E_{\text{ATP}} \sim 20\,k_B T$ is
the "biological bit". These equivalents are fixed experimentally for a specific substrate and therefore are not suitable
as a universal normalisation for the cross-substrate scale on which a bacterium, the biosphere and an
LLM corporation are simultaneously comparable. The substantive biological relevance of the Landauer bound is not "biology operates at the
ceiling", but "a single substrate-independent scale makes it possible to pose the question of absolute self-payment between
fundamentally different physical carriers".

**Statement (domain of definition of $\eta_L$).** The scale is defined when three conditions hold. (a) $E_{\text{actual}}(\tau)$ includes **all of the supplied free energy (exergy)** of the system over the window $\tau$; in the stationary regime this quantity equals the total integral dissipation (the distinction $E_{\text{actual}}$ vs $E_{\text{comp}}$ — above). (b) The system operates in the irreversible regime, that is, it is not in the global Bennett asymptotics of reversible computation. (c) The assumptions of the stationary-erasure lemma hold (full formulation and proof — supplementary § S2.1), including the **stationary-accounting postulate**. A system with finite memory holding predictive information about the environment with a non-zero update rate is forced to continuously overwrite obsolete predictions with new ones. Each overwritten bit is paid for at the full Landauer price $k_B T \ln 2$: reversible compensation through globally reversible computation (Bennett 1989) is unavailable in the stationary biological regime.
When (a)–(c) hold, $\eta_L \le 1$ holds as a **conditional consequence** of the Landauer principle; the violation of any of the conditions takes the system out of the domain of definition of the scale. The bound $\eta_L \le 1$ is proved for the exergetic denominator $N_{\text{max}}$; for the computational $\eta_L^{\text{comp}}$ (denominator via $E_{\text{comp}} \le E_{\text{actual}}$) the $[0, 1]$ normalisation is not guaranteed by the Lemma — it is a diagnostic within-class quantity without an a priori ceiling of 1. Proving postulate (c) for an arbitrary refresh channel is an open technical problem (§ 5).

*Unification of $\eta_{\text{ex}}$ vs $\eta_{\text{ATP}}$.* The calorimetric energy balance above involves two different coefficients — the measured $\eta_{\text{ATP}}$ in the formula $E_{\text{actual}} \approx Q_{\text{heat}}/(1-\eta_{\text{ATP}})$ and Stucki's $\eta_{\text{ex}}$ as a constitutive characteristic of the oxphos. Their semantics must be distinguished and their relation fixed in order to justify the simplification $E_{\text{actual}} \approx Q_{\text{heat}}$ used in the worked example of § 3.5 for a bacterium in the stationary phase. $\eta_{\text{ex}} \sim 0.4$–$0.6$ is Stucki's efficiency of oxidative phosphorylation, a constitutive characteristic of the oxphos machinery; $\eta_{\text{ATP}}$ is the actual fraction of free-energy capture as ATP at the moment of measurement, depending on the growth phase. In the exponential phase $\eta_{\text{ATP}} \to \eta_{\text{ex}}$ owing to the accumulation of useful work; in the stationary phase $\eta_{\text{ATP}} \to 0$ owing to the amortisation of reserves on maintaining the non-equilibrium state, and $E_{\text{actual}} \approx Q_{\text{heat}}$. The worked example of § 3.5 develops the calorimetric regime of the stationary phase as the standard case of this unification.

*Domain-boundary convention.* When $E_{\text{actual}} = 0$ in the irreversible regime (a passive structure without dissipative
work), $\eta_L$ is set to zero by convention as the limit $\lim_{E_{\text{actual}} \to 0^+} \eta_L = 0$ with
simultaneous $I_{\text{pred}} \to 0$. The case $I_{\text{pred}} > 0$ at $E_{\text{actual}} = 0$ is impossible by the
stationary-erasure lemma.

Before the lemma is stated, the system's characteristic window is fixed: $\tau_d := I_{\text{pred}}/\dot{I}_{\text{pred}}$
— the memory turnover time (the system's predictive horizon), the ratio of the stationary stock of predictive information to the rate of
its inflow. Empirical windows (a generation for a bacterium, a year for a city, the response time of a biogeochemical cycle — a year to a decade —
for the biosphere; the aeon is a window of accumulation of genetic information, not a $\tau_d$, cf. the companion work) are
methodological proxies for $\tau_d$, whose consistency with the theoretical $\tau_d$ is a separate calibration question (§ 3.5).
The notation $\tau$, used above in the definition of $I_{\text{pred}}$ (formula (1a) and the DPI inequality),
and throughout the rest of the article, denotes the same characteristic window $\tau_d$; the only exception is § 5, Block 3 item 2,
where $\Delta\tau \ll \tau_d$ is explicitly introduced as a probing window for falsification.

**Stationary-erasure lemma.** A finite memory holding predictive information about the environment with a non-zero
flux of new information is forced to continuously erase old memory elements (typically *nostalgia* bits, not the
predictive bits themselves), paying for each bit at the Landauer price $k_B T \ln 2$. The volume erased over the
window $\tau_d$ is $\ge I_{\text{pred}}$ (the inequality $H(M_t) \ge I_{\text{pred}}$, see supp § S2.1), which gives a
lower bound on the dissipation and, as a consequence, $\eta_L \le 1$.

*Formal statement.* Let $X$, in a stationary ergodic regime, hold predictive information
$I_{\text{pred}}$ over a window $\tau$, with finite system memory ($M < \infty$ bits) and a strictly positive
flux of new predictive information ($\dot{I}_{\text{pred}} > 0$). Then the stationary balance of predictive information in the memory
is bounded on two sides: on the **inflow** — the rate of arrival of new predictions from the source into the memory (input), and
on the **outflow** — the rate of erasure of old memory elements from the memory (typically *nostalgia* bits, of volume $\ge I_{\text{pred}}$ over the window $\tau_d$), paid for at the Landauer price (output).
In the stationary regime both flows are matched (the memory neither overflows nor empties), and the Lemma states
both bounds:

(a) *Inflow bound:* the rate of predictive update is bounded above by the source's entropy rate:
$\dot I_{\text{pred}} \le h_\mu$. This is a direct consequence of the DPI: the memory cannot output predictive information faster
than the source generates it. In the derivation of the central lower bound on dissipation (part (b)) this estimate is not used
— it is given here as a bridge to the classical framework of Bialek, Nemenman and Tishby (Bialek et al. 2001), in which
$h_\mu$ plays the role of a fundamental scale of predictive information.

(b) *Outflow bound:* if the stationary-accounting postulate is true (see below), the update channel
$M_t \to M_{t+1}$ must erase $\ge I_{\text{pred}}$ bits over the window $\tau_d$ and dissipate
$\ge I_{\text{pred}} \cdot k_B T \ln 2$ of free energy. Hence $\eta_L \le 1$.

With finite memory ($M < \infty$) the system must release
$\dot I_{\text{pred}}$ bits per unit time — this follows from Brudno's theorem (1983) (the source's entropy rate
$h_\mu$ coincides with the Kolmogorov complexity of a typical trajectory) combined with the DPI; the Landauer principle
(Landauer 1961) gives the lower price of erasing one bit, $k_B T \ln 2$. What remains unproved is the step from "the memory
releases $\dot I_{\text{pred}}$ bits" to "this release is realised precisely as Landauer erasure, and not as a
globally reversible uncomputation (Bennett uncomputation) (Bennett 1989)" — this is the **stationary-accounting postulate** (step (iv) of the full
proof), fixed in condition (c) of the Statement. Accordingly, $\eta_L \le 1$ is a *conditional* consequence of the
Landauer principle, given the truth of the postulate, not an unconditional theorem. The closest formal results
delineating the space of *possible* counterexamples are Sagawa and Ueda (2010), Parrondo et al. (2015),
and the time/space trade-off of Bennett (1989); the full formalisation of an arbitrary update channel at $M < \infty$
and $\dot I_{\text{pred}} > 0$ is an open technical problem (§ 5). The full proof of the Lemma (parts (a)
and (b) with steps (i)–(v)) and the justification of the stationary-accounting postulate through the Brudno / Sagawa–Ueda / Bennett-1989
context — supplementary § S2.1.

*Remark on feedback-assisted erasure cost.* The generalised second law (Sagawa–Ueda / Parrondo–Horowitz–Sagawa),
$\langle W \rangle \ge k_B T(\Delta S - I_{\text{meas}})$, permits erasing memory *correlated* with the environment at a
per-bit cost below $k_B T \ln 2$. The retained predictive memory is by construction correlated with the environment
($I_{\text{pred}} = I(M_t; X_E) > 0$), so this mechanism must be explicitly neutralised rather than cited as support
for the bound: otherwise $N_{\text{max}} < I_{\text{pred}}$ would give $\eta_L > 1$. The saving, however, requires a
controller that *first* measures the correlated reference, acquiring mutual information $I_{\text{meas}}$; by the
measurement–erasure symmetry (Sagawa and Ueda 2009) that measurement itself costs $\ge k_B T \cdot I_{\text{meas}}$.
Over a full stationary cycle (acquiring the correlation plus spending it on cheap erasure) the total dissipation
remains $\ge k_B T \ln 2$ per bit — the local saving is offset by the measurement cost. In the self-payment loop all
accounting is internal: there is no external demon with free access to the correlation, and the correlation
$I_{\text{pred}}$ is itself maintained by the same self-paid budget. Hence the correlation in the numerator
($I_{\text{pred}}$) cannot simultaneously be "spent" to cheapen the denominator — that would be double-counting, i.e. a
Maxwell demon inside a closed system (a second-law violation). The stationary-accounting postulate is precisely what
formalises this closure of the cycle; the conditional status of $\eta_L \le 1$ is thereby preserved (extended
discussion — supplementary § S2.1).

**The Bennett regime and the redefinition of the scale.** The domain $\eta_L \in [0, 1]$ holds in the irreversible regime. Systems in the
Bennett asymptotics of reversible computation (Bennett 1973, 1982) are outside the domain of definition: in them the scale is redefined
through the number of logical, rather than erased, bits. This is operationally a different quantity (full discussion, the $E_{\text{actual}} \to 0$
divergence, the consequences for § 5 — supp § S2.1).

*Operationalisation of $I_{\text{pred}}$.* Direct measurement by (1a) is technically impossible for biological, urban and
cosmic systems. The standard procedure fixes four elements — the sensory channel, the internal channel, the choice of windows,
and the MI-estimation method (the full protocol by system class — supp § S2.1; the full computation for a bacterium — § 3.5 below).

The present framework inherits Still's precedent and adds the requirement of self-payment: the numerator and denominator of $\eta_L$
belong to one physical system — the model and the dissipation belong to $X$. This requirement separates $\eta_L$ from
the classical formulation of the thermodynamics of prediction, in which the model and the dissipator may be different loops. This premise
inherits Rosen's organisational closure (Rosen 1991): the organism is a system closed with respect to effective causation.
$\eta_L$ is its thermodynamic operationalisation, in which the closure is realised by the physical loop of
model↔dissipation itself, and not by a category-theoretic abstraction (the detailed distinction from the closure lineage — § 4.7).

*Ontological status of the "model".* $M_X$ in the sense of $\eta_L$ is a **functional kind, not a substance kind**
(functional kind, not substance kind). Membership of this kind is set by the **criterion of § 2.2**: physical
realisation, homomorphism over the causally relevant environmental variables, testability through action, where
causal relevance is set by the system's own causal damage $D_X$ (operationally, $D_X$ is measured by the counterfactual subtraction of § 2.2 as the drop in $-dF_X/dt$; full definition — below). This discipline is consistent with the redefinition of
$M_t$ in (1a) above: the functional channel passing counterfactual ablation is singled out from the overall configuration of $X$
precisely through the three listed criteria. Carriers satisfying all three
properties realise one and the same functional type multiply (multiply realised) — the methylation pattern of the
chemoreceptors in a bacterium, the organisational closure of biogeochemical cycles in the biosphere, and other cases
with a closed causal error-return channel.

Carriers in which one of the three criteria is absent **do not belong to the functional kind $M_X$** — even if
ordinary language applies the word "model" to them. Two important cases.

(i) The weight tensor of an LLM at the moment of inference (a stateless forward pass) — violates the criterion of its own causal damage.
The "environment" in the sense of § 2.1 is absent for the operating loop, and the training corpus is not an environment but a static parent sample
(§ 3.4). LLM weights are a **compressor of the training corpus**, a different categorial type.

(ii) The bimetal of a thermostat — violates the criterion of testability through action in the sense of its own budget. The correction cycle
is paid for by the external power grid, not by the strip itself (§ 4.4). The bimetal is an **externally calibrated transducer**,
a different categorial type.

In both cases the common name "model" in ordinary language is not an indication of functional kinship; formal
inclusion in $M_X$ requires passing counterfactual ablation (§ 2.2).

This is a substantive drawing of the boundary, not an evasion of the question of what counts as a model: $\eta_L$ singles out precisely the functional type that traditional
demarcation sought in substrate-specific terms (carbon chemistry, membrane organisation) and therefore lost
discriminating power when crossing boundaries. The lineage is Cleland's anti-essentialism (Cleland 2019), the cluster view of
Mariscal and Doolittle (2020) and Pradeu's process biology (Pradeu 2018): vitality is a property of a process, not a property of a substance.
The formal definition of $M_X$ through counterfactual ablation (§ 2.2) gives an ontological discipline of functional
identification and closes the charge of a category mistake without appeal to authority.

The denominator $N_{\text{max}}$ requires fixing the temperature of the receiving heat bath $T$ and the window $\tau_d$. $T$ is the temperature of the
heat bath into which $X$ dissipates $E_{\text{actual}}$; the choice of $T$ is a methodological convention, analogous to
fixing $T = 300\,\text{K}$ in the thermodynamics of computation. The window is standardised by the system's characteristic times:
a generation for a bacterium, a year for a city, the response time of a biogeochemical cycle (a year to a decade) for the biosphere, and the main-sequence evolutionary time for a star.

The standard choice of $T$ for the six paradigm cases is fixed as follows. A bacterium — $T \approx 310$ K
(physiological); a city — $T \approx 285$ K (the annual mean of a temperate climate); the biosphere — $T \approx 288$ K
(the equilibrium surface temperature); an LLM and a data centre — $T \approx 300$ K (the operating temperature of a server room). A star —
for the radiative channel of the Sun the final receiving heat bath is the cosmic microwave background,
$T_{\text{CMB}} \approx 2.725$ K. Local cold phases of the interstellar medium ($T \sim 10$ K for dense molecular
clouds, $\sim 50$–$100$ K for the cold neutral medium) give an $N_{\text{max}}$ differing by no more than a factor of $\sim 4$.
The photospheric $T_{\text{eff}} \approx 5800$ K is the temperature of the source, not of the receiver, and does not enter $N_{\text{max}}$,
cf. the explicit computation in § 3.1. For a star the diagnosis $\eta_L^\odot = 0$ through the structural zero of the numerator is independent of the
choice of $T$ in the range $[2.725;\, 5800]$ K.
For a crystal and a hurricane, $T$ is tied to the temperature of the immediately surrounding environment. A difference in $T$ between systems by 1–2 orders of magnitude does not disrupt cross-class comparison, since
$\eta_L$ is intensive and dimensionless, and the $1/T$ dependence is compensated by the choice of the characteristic window $\tau_d$. The limiting
case $T \to 0$ (ultracold astrophysical objects): $N_{\text{max}} = E_{\text{actual}}/(k_B T \ln 2) \to \infty$,
and formally $\eta_L \to 0$ remains in $[0, 1]$. However, the Landauer bound ceases to be binding and the scale loses its
physical content; the framework is restricted to $T > 0$ as the regime in which comparison between substrates is meaningful.

The logical status of $\eta_L$ is as follows. $\eta_L > 0$ is a necessary condition for **synchronic** vitality in
the sense of "does the system possess a closed self-payment loop for its own model over the window $\tau_d$". This is not a sufficient
condition for the full biological definition of life in the NASA sense (Joyce 1994) — the latter requires Darwinian dynamics at the
population level. The distinction between the synchronic and diachronic dimensions of vitality — § 2.7. The distinction between the scale domain $\eta_L \in [0, 1]$ and the vital
class $\eta_L \in (0, 1]$ is the standard distinction between the domain of a scale and a criterial threshold: zero remains in the domain
of definition as a point of structural failure. The binary test "alive or not" is done by $\eta_L$; the numerical value
within the positive range gives a comparative measure of efficiency.

$\eta_L$ is defined only on systems for which one can simultaneously isolate the predictive
information held by the system itself about its own environment and the Landauer budget of its own dissipation that pays for this
maintenance. The class of such systems — compressors with a stake — is narrow. This narrowness is substantive, not a defect: broad applicability without discrimination
of the non-living from the living is a characteristic property of complexity indices (assembly index, $\Phi$); overcoming it
constitutes the comparative contribution of $\eta_L$.

The precedent for the thermodynamic link between predictive information and dissipation was set by Still et al. (2012);
in their formalism the predictor demon **itself** dissipates for its predictions. The present framework inherits this and adds a
strict requirement: **the physical boundary of the system holding $I_{\text{pred}}$ coincides with the boundary paying for
$E_{\text{actual}}$**. In Still the identity of the boundaries of the model and the dissipator is not required (the demon and the environment are separate subsystems);
the $\eta_L$ programme makes their coincidence constitutive. This excludes the thermostat as a vital system (the bimetal holds
a "model", but the power grid pays) — a key substantive difference. A clarification: self-payment requires the co-location
of the maintenance of $I_{\text{pred}}$ and the paying dissipation within one boundary of $X$, and not that all of $E_{\text{actual}}$ go to
the maintenance of the model. The fraction of information-relevant dissipation $E_{\text{comp}}/E_{\text{actual}} \sim 10^{-3}$ (§ 3.5) —
this is the part of the budget that falls to the model; it is **not identical** to the fraction of own (vs external) payment
$E_{\text{actual}}^{\text{own}}/E_{\text{actual}}^{\text{total}}$ (§ 5, Prediction 3). In a bacterium the latter equals 1 (the whole
dissipation is paid for by the cell itself), which is what ensures self-payment; the smallness of $E_{\text{comp}}/E_{\text{actual}}$ is a separate
quantity, not comparable with the threshold $f^*$. The choice of predictive vs stored, non-stationary
*nostalgia* and the role of self-payment are discussed in more detail in the Supplementary referenced above.

*Technical definitions.* *The environment of a system $X$* is the causal zone $X_E$ with two properties: a sensory link with $X$ and
a causal effect on $X$ through a channel other than the sensory one (physical expenditure of resources, temperature
effect, destruction of structure). Systems without a causal channel (a star relative to a planetary system) have no
environment by definition; for them $\eta_L = 0$ by construction. *The model $M_X$* is an internal structure with three properties:
physical realisation with stability through continuous Landauer payment; homomorphism over the relevant
variables, where relevance is set by the causal damage of $X$, not by an outside observer; testability through action.
*The damage to the modeller* over the window $\tau_d$ is the negative derivative of the free energy of $X$ at which the internal
processes maintaining the non-equilibrium regime lose a sufficient budget. The chain "vitality $\leftarrow$ model ×
self-payment $\leftarrow$ model × loop (error $\to D_X$) $\leftarrow$ thermodynamics ($F_X$, $\tau_d$, $k_B T \ln 2$)"
reduces vitality to information-thermodynamic primitives without appeal to itself.

### 2.2 The system boundary as a methodological convention

The scale $\eta_L$ depends on the choice of the boundary of the measured system. This is a structural property, not a defect. For a large language
model, under the strict boundary "weights at the moment of inference" (a stateless forward pass), two conditions fail simultaneously:
the own dissipation $E_{\text{actual}}^{\text{own}} \to 0$ (the power grid is external) and the error-return channel into the operating
loop is absent. Under such a boundary the scale $\eta_L$ is **undefined** through the simultaneous failure of both conditions, not
"equal to zero through the numerator" (the formal count through the capacities $T_v$, $C_v$, $S_v$ — § 2.3; the distinction between the strict/operational
readings $\eta_L^{\text{int}}$ vs $\eta_L^{\text{op}}$ — § 2.5). Under a boundary that includes the data centre and the corporation,
$\eta_L > 0$, but the measured object is no longer the model.

The choice of boundary is methodologically disciplined. The boundary is drawn where the loop of decisions
paid for by the system's own loss of stability is closed. The conceptual predecessor is the *epistemic cut* and *semantic closure*
of Pattee (Pattee 1982, 2001): the boundary between the physico-dynamic level and the symbolic level, in which
the system closes within itself the processing of its own symbols. The bacterial cell is a natural boundary, since
the distortion of its internal model of the gradient leads to the loss of stability of precisely this cell. The city is so because the distortion of its model
of flows returns as a crisis to precisely this administrative unit. The identity of the question determines the boundary;
the choice of boundary sets what is measured.

The conventionality of the boundary is productive. The objection that "under the right choice of boundary any system will turn out to be vital"
is met as follows: the choice of boundary is the choice of whose vitality is measured, and an extension of the boundary extends the responsible
subject rather than dissolving the diagnosis.

*The boundary and the Markov blanket.* The Markov blanket of a system $X$ (Friston 2019) is a statistically separating layer of sensory and
active states. The proper construction of the self-payment boundary (§ 2.2) **does not inherit** the difficulties of the realist
interpretation of the Markov blanket diagnosed in BDDB-2022 (Bruineberg et al. 2022) and Aguilera et al. (2022).
The boundary in our framework is set by the **thermodynamic membership of the budget** $E_{\text{actual}}$, and not by a statistical
separation of the distribution along a Pearl- or Friston-blanket; it is therefore orthogonal to the Pearl/Friston-blanket dilemma. Conflating
the two notions leads to a category mistake in which informational separation is taken for energetic self-payment.

*Counterfactual ablation.* The discipline of the choice of boundary is operationalised by an interventional procedure in the spirit of
Pearl causality (terminologically — counterfactual ablation in the sense of mechanistic interpretability: remove a component, measure the effect; not to be confused with Reichenbach screening-off). For a candidate $c$ for inclusion in the boundary of $X$: $c$ is subtracted from the physical realisation; if
the change in the rate of free-energy depletion $-dF_X/dt$ over a response time $< \tau_d$ is significant, $c$ belongs to the boundary.
Quantitative threshold: $c$ belongs to the boundary when $|\Delta(-dF_X/dt)| / |-dF_X/dt|_{\text{base}} \ge \delta$, where
$\delta \in [0.05;\, 0.1]$ is a methodological convention, analogous to the significance threshold in regression analysis.
For systems with smoothly distributed membership (parasite–symbiont–host, corporation–employees) the procedure
returns a scale of degree of membership — the degree of membership $w_c = |\Delta(-dF_X/dt)| / \sum_i
|\Delta(-dF_{X,i}/dt)| \in [0, 1]$.

The procedure relies on a pre-theoretic candidate boundary — a minimal initial intuition (physical connectedness, the
biological cell as a unit, the engineering assembly as a unit). Counterfactual subtraction refines the boundary by measuring the
**relative** contribution of each component to the total dissipation of the connected system; convergence to a fixed point
with respect to permutations of the subtracted elements gives a justified boundary. This is not a complete elimination of conventionality
(for systems without a natural pre-theoretic candidate — a corporation, the biosphere — the procedure remains open), but
an operational discipline of choice in most physical and biological cases.

Application to LLMs — § 3.4 and Supplementary § S3.4; to the thermostat — § 4.4 and Supplementary § S4.4.
### 2.3 The triad of invariants

The positivity of $\eta_L$ requires the simultaneous presence of three capacities.

*Thermodynamic capacity $T_v$* is the price of maintaining the model against erosion. Irreversibly erasing one bit physically costs at least $k_B T \ln 2$ of free energy (Landauer 1961); the exergy flux is the payment against noise. The standard proxy is the specific exergy flux $P_D \cdot \eta_{\text{ex}}$, normalised per unit mass or volume; in the tradition of Chaisson (Chaisson 2001) it is measurable from molecules to galaxies.

*Informational capacity $C_v$* is the quality of compression: the adequacy of the model to its environment and its updatability. The proxies fall into two classes. The first class consists of entropy-rate proxies $h_\mu$ (normalised Lempel–Ziv complexity, Bandt–Pompe permutation entropy); these operationalise the rate of environmental novelty, not predictive information. The second class consists of proxies for $I_{\text{pred}}$:

- excess entropy $\mathbf{E} := \lim_{L\to\infty} I(X^{[t-L,\,t]};\, X^{[t,\,t+L]})$, the asymptotic value of predictive information in the formulation of Bialek–Nemenman–Tishby in the limit of infinite windows; for finite windows it is operationalised through block-entropy estimates $H(L)$ (Crutchfield and Feldman 2003);
- statistical complexity $C_\mu$ (Crutchfield's computational mechanics; Shalizi and Crutchfield 2001), the entropy of the minimal sufficient statistic for prediction; it satisfies $C_\mu \ge \mathbf{E}$ and serves as a complementary measure of structural memory;
- the PCI (perturbational complexity index) of Casali (Casali et al. 2013), an estimate of nonlinear integration on cortical-biological data. The parallel programme of Adami (Adami 2002) defines physical complexity as the mutual information between genome and environment, a biologically concrete special case of "the quality of the model of the environment," conceptually akin to $C_v$. Distinguishing the two classes is essential for a consistent operationalisation of $\eta_L$. In the stationary regime of the present work both classes serve as proxies for a single $C_v$; in the non-stationary extension (Andriishin, companion paper) they are formally separated as $C_v^{\text{static}}$ (structural complexity, a first-class proxy) and $C_v^{\text{predictive}}$ (dynamic predictive power, a second-class proxy), and their divergence serves as a diagnostic signal of informational nostalgia.

*Topological capacity $S_v$* is the connectivity architecture of the error-return loop. The standard proxies are Newman modularity $Q$ (Newman and Girvan 2004), with an indicative threshold of $Q > 0.3$ as a tentative guideline that requires calibration against a null model (see below on the resolution limit, rather than a hard criterion); the scale-free property $\gamma \in [2, 3]$ for the degree distribution (Barabási and Albert 1999; Newman 2010 for a review; the critique of its universality in Broido and Clauset 2019); and the hierarchical clustering coefficient $C(k) \sim k^{-1}$ (Ravasz and Barabási 2003). The algebraic connectivity $\lambda_2$ of Fiedler (1973), which indexes global diffusive connectivity, is a *secondary* proxy with an inverse interpretation: for modular architectures $\lambda_2$ is low (Mohar 1991), so it is used as an indicator of structural bottlenecks between modules, not as a measure co-directional with $Q$. A further class of proxy is structural controllability (Liu, Slotine, and Barabási 2011), a slice of the error-return-loop topology independent of modularity.

The efficiency of a hierarchical-modular architecture for maintaining predictive information over a structured environment is formalised through minimum description length (Mengistu et al. 2016): a hierarchical topology compresses the description of the adaptive policy by an amount proportional to the depth of the environment's hierarchy. The hierarchical structure is validated through the predictive power of the missing-links decomposition (Clauset, Moore, and Newman 2008), which empirically links the $S_v$ proxies to the $C_v$ criteria and prevents the two from collapsing into a single measure. The empirical correlate is the neural connectome (Bassett and Sporns 2017; Lynn and Bassett 2019), which exhibits hierarchical-modular organisation as a selective correlate of computational efficiency. Two limiting cases zero out $S_v$ by construction (§ 5, Direct-refutations block, item 3). The Erdős–Rényi random graph lacks any modular decomposition; its redundant short links provide no compression of the adaptive policy, despite a small-world diameter (Watts and Strogatz 1998). The regular lattice lacks cross-scale connectivity and fails at large-scale propagation of error correction.

The empirical status of scale-free behaviour as a universal pattern has been contested: across a corpus of roughly 1000 empirical networks, a strict power law with $\gamma \in (2, 3)$, tested by the statistical methodology of Clauset et al. (2009), is confirmed only in a minority of cases (Broido and Clauset 2019; Holme 2019). A power-law distribution is one of the regimes of the required architecture, not the only one; what is relevant is the more general condition of the absence of a characteristic scale together with a modular-hierarchical organisation. The Newman $Q$ metric depends on the algorithm (greedy Newman (2004), Louvain (Blondel et al. 2008), Leiden (Traag et al. 2019)); the resolution-limit problem (Fortunato and Barthélemy 2007) requires calibrating the threshold through a null model. Here $Q$ is computed with the Leiden algorithm; the numerical calculation for the *E. coli* chemotactic network is in supplementary § S3.5 ($Q \sim 0.5$). The evolutionary origin of hierarchical modularity (introduced above through $C(k) \sim k^{-1}$ of Ravasz–Barabási) lies in selection pressure for the minimisation of connection length (Mengistu et al. 2016) and in environmental variability (Kashtan and Alon 2005).

The triad is not assembled from independent disciplines—it is forced by the nature of maintaining compression over time. Zeroing out any capacity zeroes out vitality on any scale: without payment there is no self-payment, without quality there is no model, without architecture there is no error-return loop.

### 2.4 Capacity normalisation by a reference cohort

In their raw form the proxies do not lie in $[0, 1]$ and cannot be substituted into the composite index $I_v$ without normalisation. The specific exergy flux for $T_v$ has dimensions of W·kg$^{-1}$ and is unbounded above. Excess entropy and $C_\mu$ for $C_v$ are bits, unbounded above. Newman modularity for $S_v$ lies in $[-1/2, 1]$; the Ravasz–Barabási hierarchy measure is a power-law exponent. For a connected graph $\lambda_2 \in (0, n]$ (for a disconnected graph $\lambda_2 = 0$); as a secondary proxy it is not used within the $S_v$ normalisation. Without explicit normalisation, formula (2) and the stipulation "$T_v, C_v, S_v \in [0, 1]$" are formally incorrect.

In the present work we adopt percentile normalisation by a reference cohort. For each capacity a reference cohort of systems of the same structural class is fixed; the normalised value is the percentile within the cohort distribution:

$$\tilde{T}_v(X) = F_{T_v}^{\text{cohort}}\bigl(T_v(X)\bigr) \in [0, 1], \tag{2a}$$

where $F_{T_v}^{\text{cohort}}$ is the empirical distribution function of the proxy across the cohort; analogously for $\tilde{C}_v$ and $\tilde{S}_v$. The zeroth percentile is the weakest member, the first percentile is the strongest. This is a standard device in social indicators: the Human Development Index (United Nations Development Programme 2022) normalises its components in the same way. The specific cohorts for the six paradigm cases, and the treatment of edge cases (the biosphere without a cohort; the crystal and the hurricane with a constructive zero), are in Supplementary § S2.4.

The percentile procedure carries three limitations. First, the choice of cohort is a convention. Even so, the robustness of the sign of the difference between two systems of the same cohort does not depend on the choice of cohort provided the cohort is sufficiently wide; it is precisely this robustness of sign that is the substantive claim of § 3, not the specific numbers. Second, the procedure loses information about the absolute values of the proxies and works only for comparison within a class. Across classes, numerical $I_v$ values are not directly comparable. Third, the procedure is inapplicable to systems without a natural cohort, where normalisation by a theoretical upper bound is required. The sigmoidal alternative $\tilde{T}_v = T_v/(T_v + T_v^{\text{ref}})$ is in Supplementary § S2.4.

In what follows $T_v, C_v, S_v$ denote the normalised quantities $\tilde T_v, \tilde C_v, \tilde S_v$ unless explicitly stated otherwise; the tilde is omitted for readability.

### 2.5 The composite index $I_v$ as a structural-readiness index

The geometric mean of the three capacities

$$I_v = \sqrt[3]{\tilde{T}_v \cdot \tilde{C}_v \cdot \tilde{S}_v} \in [0, 1] \tag{2}$$

is defined as the structural composite. Geometric averaging is chosen for three reasons: it remains in $[0, 1]$; it is symmetric under permutations; and it vanishes when any capacity vanishes (the loss of a single capacity collapses vitality entirely). Additive averaging does not preserve this property—a sum would mask a failure. The weights $w_T = w_C = w_S = 1$ are a convention; for unequal weights, $I_v^{(w)} = (\tilde{T}_v^{w_T} \cdot \tilde{C}_v^{w_C} \cdot \tilde{S}_v^{w_S})^{1/(w_T + w_C + w_S)}$. No sensitivity analysis with respect to the weights is carried out, because $I_v$ is a methodological index of the structural prerequisites for vitality, not a self-standing vitality scale: it is $\eta_L$, not $I_v$, that performs the binary "alive or not" test. A positive $I_v$ is a necessary condition for a positive $\eta_L$; it is not sufficient. Through standard proxies (Lempel–Ziv, exergy, network metrics), $I_v$ yields nonzero values for any structurally complex dissipative system—the Sun, a hurricane, a black hole, an LLM. In its comparative position, $I_v$ coincides with the assembly index, Deacon's morphodynamics, and Tononi's $\Phi$: a composite complexity index that is necessary but not sufficient.

One objection to the status of $I_v$ might be that a composite of three necessary conditions would more naturally be interpreted as a self-standing scale. However, through any reasonable set of industrial proxies, $I_v$ yields robustly positive values for systems that are manifestly non-living. For example, the $I_v^{\text{op}}$ of the Sun is positive through any standard proxy. The normalised Lempel–Ziv complexity of the GOES X-ray flux over the 11-year cycle yields $\sim 0.5$–$0.7$ of the upper percentile of the main-sequence-star cohort; the hierarchy of the active-region network from SDO/HMI (Gheibi et al. 2017) is $\sim 0.4$. The specific number depends on the dataset and the cohort, but it stays robustly within $(0.3, 0.7)$. For this reason $I_v$ remains in the role of a _methodological_ index; this is formally fixed through a distinction between two readings. $I_v^{\text{op}}$ (the operational reading)—through standard proxies on observable data—is nonzero for any complex dissipative system. $I_v^{\text{int}}$ (the interpretive, strict reading)—with a strict check of $T_v$ as self-dissipation, $C_v$ as a model of the environment in the technical sense, and $S_v$ as the architecture of a closed loop—is zero for any non-living system by construction. The divergence of the two readings for a given system is a diagnostic signal: the system is structurally complex but not vital, and the divergence points to the capacity in which it fails.

### 2.6 The two-stage procedure

Vitality is established theoretically by a single test—the positivity of $\eta_L$. The two-stage procedure is a methodological convenience, not a logical necessity:

1. *Screening with $I_v$.* Cheap, through standard operational proxies; it screens out structurally unfit systems (a crystal—zeroing of $T_v$; thermal equilibrium—zeroing of all three capacities). A computational filter, not a separate test.
2. *Verification with $\eta_L$.* Expensive, requiring identification of the boundary and of the system's own self-payment loop; applied to candidates that pass the screening. The only logically substantive test.

The binary nature of the sign of $\eta_L$ does not make the numerical value merely decorative. The objection "if the sign alone provides the demarcation, the number is redundant—the counterfactual ablation of § 2.2 establishes the sign without any formula" is met by pointing to a content of the quantity that is not reducible to its sign. First, within the positive region $\eta_L$ is a comparative metric of the efficiency of the self-payment loop: the order of magnitude of $\eta_L$ for two systems of the same class carries content beyond the shared sign. Second, the magnitude enters the falsifiable quantitative prediction $r_{\text{adapt}} = A \cdot \eta_L^{\alpha}$ (§ 5), which the sign does not generate: the sign fixes neither the exponent $\alpha$ nor the testable monotonic dependence of the adaptation rate. The sign carries the cross-class demarcation, the magnitude the within-class metric and the risky prediction; the latter is not derivable from the former.

The structure of outcomes is as follows. Passing both thresholds: the vital systems (a bacterium, a forest, a brain, the biosphere, a city). Passing the screening but failing the verification: structurally rich but non-living systems (the Sun, a hurricane, a black hole). Failing the screening: structurally unfit systems (a crystal, thermal equilibrium; and an LLM under the strict boundary "the model as agent").

Refuting any capacity collapses both scales simultaneously: $\eta_L$ through the numerator or the denominator, $I_v$ through the geometric mean. Refutations of the two scales are one and the same diagnosis at two levels of resolution, not independent pieces of evidence.

The two-stage architecture carries a methodological risk. The class of structurally rich but non-living systems—the Sun, a hurricane, a crystal, an LLM, a black hole, the Belousov–Zhabotinsky reaction—risks turning into a protective belt in the Lakatosian sense: any refuting observation is absorbed by inclusion in the class. The programme imposes a minimal discipline: every zeroing of $\eta_L$ is accompanied by an indication of the specific capacity that failed. If the class expands without a structural explanation of each new inclusion, the programme shifts from a progressive into a degenerating regime.

A possible counter-argument: the asymmetry between the two levels is an artifact of the soft proxies of $I_v$ (Lempel–Ziv, permutation entropy). Were $C_v$ operationalised more strictly—for example, through Tononi's $\Phi$ with a filter on predictive power relative to the system's own environment—the Sun would yield $C_v \to 0$. The answer: the issue is not the choice of one proxy but the class of available industrial metrics. All proxies of network science, information theory, and non-equilibrium thermodynamics developed over the past forty years, when applied to a complex dissipative system, yield nonzero values. A proxy that deliberately zeros out the $C_v$ of the Sun requires post-hoc calibration against the vitality hypothesis itself—a circularity.

### 2.7 Epistemic status of the section's claims

The claims of this work differ in status: theoretical deduction from established principles, empirical verifiability, and speculative extrapolation with explicit falsification conditions. The claim about the domain $\eta_L \in [0, 1]$ (§ 2.1) is a deduction from Landauer's principle and the stationary-erasure lemma. The geometric averaging (2) is a formal choice based on symmetry and zeroing. The paradigm-case values of $\eta_L$ for a bacterium, the biosphere, and astrobiological candidates are theoretical order-of-magnitude estimates with an explicit dependence on the window and the proxy. The urban case (§ 3.6) is a paradigm-case order-of-magnitude estimate of $\eta_L$; structural urban metrics in the spirit of Bettencourt et al. (2007) and the empirical calibration of $I_v$ for specific cities are the subject of separate work and are not asserted here. The speculative consequences—the search for cosmological vitality, the moment at which an artificial system becomes vital—are discussed in §§ 5–6 with explicitly formulated falsification conditions.

The foundational **self-payment postulate**—that the numerator and the denominator of $\eta_L$ belong to one and the same physical system—stands apart from the statuses just listed: it is not a deduction from the FEP or from Landauer's principle, but an explicit ontological premise of the framework that neither Landauer nor Bialek made. Its epistemic status is that of a constructive choice, justified by its demarcating power (cf. § 4.4: self-payment offers an alternative, thermodynamic ontology that does not inherit the difficulties of the Pearl/Friston-blanket construction diagnosed by BDDB-2022), rather than by derivability from earlier principles.

The second foundational premise is the **stationary-accounting postulate** (§ 2.1, step (iv) of the stationary-erasure lemma). The content of the postulate: the release of $\dot I_{\text{pred}}$ bits per unit time is realised as Landauer erasure, not as globally reversible un-computation, for an arbitrary update channel with $M < \infty$ and $h_\mu > 0$. A proof of this postulate for an arbitrary update channel is an open technical problem. Accordingly, the bound $\eta_L \le 1$ is a conditional consequence of Landauer's principle given the truth of both foundational premises (self-payment together with the stationary-accounting postulate), not an unconditional theorem. Refuting the stationary-accounting postulate by demonstrating a globally reversible realisation of the update channel in a stationary regime with $\dot Q > 0$ is an independent line of falsification of the programme (§ 5, Block 1, item 1).

The falsification conditions of § 5 may be realised on two levels. The methodological level: the current operationalisation is untenable, and a different proxy, window, or mutual-information estimation procedure is required. The ontological level: the concept of vitality as the efficiency of self-modeling is untenable in substance. The programme takes the position of moderate operationalism: any observation that refutes $\eta_L$ through the failure of a specific operationalisation is first interpreted methodologically and is translated into ontological terms only after the alternative operationalisations have been exhausted.

**Asymmetry of falsification.** The programme is falsified through false-negative cases (a biological system conventionally recognised as alive, for which $\eta_L = 0$ under all sanctioned operationalisations—§ 5, Block 2, item 3) and through structural failures of progressive predictions (§ 5, Block 3, items 1–2). False-positive cases (a system non-living by conventional criteria yet with a stable $\eta_L > 0$) are formally excluded by construction: for systems without a closed error-return loop, the counterfactual ablation of § 2.2 returns $C_v^{\text{int}}$ as undefined, and $\eta_L$ is not defined. This asymmetry is a deliberately accepted cost that narrows the programme's falsification surface to two lines (false-negative intrusion, § 5 Block 2 item 3, and the failure of progressive predictions, § 5 Block 3 item 1): $\eta_L$ is a criterion for the closure of the self-payment loop, and systems without such a loop receive no positive score **by construction**. If neither of the two lines turns out to be empirically realisable, the scale risks reducing to a conventional re-description—this risk is acknowledged explicitly (cf. § 2.6) rather than masked. An alternative criterion—for example, informational complexity in assembly theory or $\Phi$—may assign a nonzero value even to a non-living system, which reflects the different content of those programmes (structural complexity vs. the closure of a thermodynamic loop). Refutation of the $\eta_L$ programme is therefore possible only through **symmetric intrusion**—the discovery of a conventionally living system for which the self-payment loop does not close (§ 5, Block 2, item 3)—or through the failure of progressive predictions on calibrated biological pairs (§ 5, Block 3, item 1).

*Heredity and major transitions: what $\eta_L$ does not close.* The $\eta_L$ scale formalises the **synchronic** side of vitality—the maintenance of a system's own model over the window $\tau_d$. This is a necessary condition for each moment in the life of a single organism. The **diachronic** side—heredity and evolvability in the sense of major transitions (Maynard Smith and Szathmáry 1995)—lies beyond the present stationary model. The stationary regime fixes finite memory and ergodicity of the environment (§ 2.1), which exclude population-evolutionary dynamics with drift and the accumulation of hereditary information. Positivity of $\eta_L$ is a necessary but not sufficient condition for a full biological "definition of life" in the sense of the NASA definition (Joyce 1994). A sterile worker bee or a mule has $\eta_L > 0$ (alive moment-to-moment) but is excluded from Darwinian dynamics at the population level. The scale is consistent with the biological convention regarding their aliveness and does not violate it. A full definition of life requires $\eta_L > 0$ **plus** Darwinian dynamics at the population level; these are two distinct scales—the individual synchronic and the population diachronic—and both are necessary. The connection with the companion work (Andriishin 2026): the non-stationary extension provides a thermodynamic apparatus on which the major-transitions programme (Maynard Smith and Szathmáry 1995) can be formulated as an open research problem (cf. § 4.8)—the joining of the two scales is not proved either in the present work or in (Andriishin 2026), but in their combination it acquires a formal basis.
## 3. Demarcation Tests

This section applies the procedure of § 2.6 to six paradigm cases — the Sun, a hurricane, a crystal, an LLM, a bacterium, and a large city — and records the diagnosis of each by indicating the capacity through which one of the scales is driven to zero. Each zeroing names a concrete physical or informational failure.

A full computation from $P(s_t \mid x_t)$ to the final number, with explicit sensitivity to the window and to interval binning, is carried out only for the chemotactic loop of *E. coli* (§ 3.5). For the remaining five paradigm cases we give order-of-magnitude estimates, methodologically consistent with this calibration; a complete reproducible computation across all six systems requires a separate study.

A comparative programme at the boundary of non-living / living collectives via informational architecture is developed in *Theory in Biosciences* (Kim et al. 2021); the six paradigm cases of the present section continue this line, adding to the informational axis of Kim–Valentini–Hanson–Walker the thermodynamic requirement of self-payment.

*Epistemic status of the numerical estimates of $\eta_L$.* Demarcation in the present work relies on the **sign** of $\eta_L$ ($> 0$ vs $= 0$ vs undefined through the simultaneous failure of the capacities), not on the absolute magnitude or on within-class ranking. The figures $\eta_L^{\text{biosphere}} \lesssim 10^{-22}$, $\eta_L^{\text{corp}} \lesssim 10^{-25}$, $\eta_L^{\text{city}} \lesssim 3 \cdot 10^{-28}$ are **upper bounds via capacity-bound numerators**, not measured predictive information. The substantive cross-class claim is a structural difference (the presence of a closed self-payment loop), not a quantitative one (a ratio of numbers). Numerical demarcation by sign requires an independent MI estimate for each paradigm case, which is an open operational task (see § S2.1 for the biosphere/city/corporation). All values $\eta_L < 1$ reported below are obtained under the stationary-accounting postulate of § 2.1. Should it be refuted by a demonstration of a globally reversible implementation of the update channel in the stationary regime, these values retain the status of the ratio $I_{\text{pred}}/N_{\text{max}}$ but lose their interpretation as fractions of the Landauer capacity.

### 3.1 The Sun

At a flux of order $\sim 4 \cdot 10^{26}$ W, a delicate gravitational–thermonuclear balance, and a structurally non-trivial history of stability, the $\eta_L$ of the Sun goes to zero through the numerator, since the internal organisation of the star contains no predictive information about its own environment in the sense of § 2.1. The variables of the planetary system are not mapped onto the internal degrees of freedom of the plasma with predictive power, and the relevance of these variables for the Sun is not set by its own causal harm.

The gravitational interaction of Jupiter with the Sun does exist: the barycentre of the Solar System is displaced relative to the centre of mass of the Sun by a solar radius, and a number of hypotheses about planetary forcing (Jose 1965; Charvátová 1990) link this displacement to the 11-year activity cycle. The causal chain, however, runs in one direction — from the planets to the Sun through gravity, not from an error of the solar model of the environment to harm to the Sun: the hypothetical disappearance of Jupiter does not return into the internal dynamics of the Sun as a perturbation of its non-equilibrium regime.

For completeness we give the denominator $N_{\text{max}}^{\odot}$. Since the zeroing proceeds through the numerator, we indicate only the order of magnitude of the Landauer budget of the denominator. With a solar luminosity $L_\odot = 3.8 \cdot 10^{26}$ W and a characteristic window $\tau \sim 10^{10}$ yr $\approx 3 \cdot 10^{17}$ s, $E_{\text{actual}}^{\odot} \sim 10^{44}$ J. The $T$ in the denominator is the temperature of the cosmic receiving heat bath for entropy, not of the source photosphere. $T_{\text{CMB}} \approx 2.725$ K (cosmic microwave background) is the asymptotic sink of photon entropy after re-emission by the interstellar medium; local reception by cold phases of the interstellar medium (ISM) at a scale of $\sim 10$ K changes $N_{\text{max}}$ by a factor of $\sim 4$, not by an order of magnitude. $k_B T_{\text{CMB}} \ln 2 \approx 2.6 \cdot 10^{-23}$ J/bit, whence $N_{\text{max}}^{\odot} \sim 4 \cdot 10^{66}$ bits — the hypothetical upper bound on the number of bits that a demon with a heat bath at $T_{\text{CMB}}$ could erase on the exergy of the Sun. Although this astronomical budget exceeds the unique genomic content of the biosphere ($I_{\text{cap}}^{\text{biosphere}} \lesssim 10^{20}$ bits) by 47 orders of magnitude and the copy-number DNA volume of the biosphere (Landenmark et al. 2015) by 30 orders, the absolute magnitude of the dissipative ceiling by itself does not generate vitality in the absence of a closed self-payment loop.

The $I_v^{\text{op}}$ of the Sun is positive through any standard proxy. Solar activity by sunspot number $R_z$ exhibits nonlinear-deterministic dynamics in a 5-dimensional embedding space with a finite Lyapunov time $\approx 4.8$ yr (Sello 2003) — a structural signal distinguishing it from trivial periodicity. The network of solar flares built from the LMSAL archive (14,395 events, 2006–2016, GOES classification; Gheibi et al. 2017) is scale-free ($\gamma > 3$) and small-world, with a hierarchical exponent $\alpha \approx 0.5$ for $C(k) \propto k^{-\alpha}$. The specific exergy flux of the Sun ($\sim 2$ erg/s/g, Chaisson 2001) is above the galactic background ($\sim 0.5$ erg/s/g) but many times below that of the biosphere and society. Normalising these proxies to a reasonably chosen cohort of complex dissipative systems yields $\tilde{T}_v^{\text{op}}, \tilde{C}_v^{\text{op}}, \tilde{S}_v^{\text{op}} > 0$ and a stable composite index $I_v^{\text{op}} \in (0.3;\, 0.7)$ under variation of dataset and cohort. The operational number confirms the structural complexity of the star and yet does not pass $\eta_L$-verification, whereas the interpretive reading $I_v^{\text{int}}$ drives the Sun to zero through $C_v$: there is no model of the environment in the technical sense, and hence no numerator. Diagnosis: structurally rich, non-living. The same applies to a neutron star, the interstellar medium, and the supermassive black hole at the centre of the Milky Way.

A black hole receives an analogous diagnosis, through the simultaneous failure of $T_v^{\text{int}}$ and $C_v^{\text{int}}$. The stationary classical horizon is described by the no-hair theorem (canonical formulations 1967–1975; the key work is Israel 1967). Three parameters ($M$, $J$, $Q$) fully specify the external metric, leaving no room for $I_{\text{pred}}$ about the environment; $C_v^{\text{int}}$ is undefined. Quantum and non-stationary corrections — thermal radiation and the information paradox it engenders (Hawking 1975, 1976), soft hair (Hawking et al. 2016) — reveal a richer informational structure of the horizon, but do not restore a model of the environment in the sense of § 2.1. The corresponding quantum degrees of freedom do not maintain $I_{\text{pred}}$ about the environment with a return of harm through their own dissipation. $T_v^{\text{int}}$ as proper dissipation in the sense of an information operation is also undefined: Hawking radiation is a globally reversible process. The accretion disc around a supermassive black hole (Sgr A*, $M \sim 4 \cdot 10^6 M_\odot$) gives the same diagnosis: the environmental variables do not return as harm through a causal channel to the plasma of the disc. Accordingly $\eta_L^{\text{int}}$ for these systems is undefined — a categorical difference from the diagnosis of the Sun, where $\eta_L^{\text{int}}$ equals zero through the numerator.

### 3.2 Hurricane and flame

A hurricane and a candle flame dissipate free energy at $\sim 10^{15}$ W for an average hurricane and $\sim 10^2$ W for a candle flame — their $T_v$ is high. They have no internal model of the environment paid for by this dissipation: the scattering of exergy is not accompanied by the maintenance of $I_{\text{pred}}$, so $\eta_L$ goes to zero through the numerator, and $I_v$ through $C_v$. The diagnosis is **a stake without a model**: the system pays but does not model, and in this the flame and the hurricane are the symmetric counterpart of the LLM: they pay without modeling, whereas the LLM models without paying (§ 3.4).

The Belousov–Zhabotinsky reaction oscillates stably and for a long time, but its oscillations do not form a correction loop in which an error of the model returns as a loss of the system's free energy, and so the diagnosis here is the zeroing of $C_v$ through the absence of accumulated memory: repetition without learning.

### 3.3 Crystal and thermal equilibrium

A crystal maintains its structure with a relative deformation $\lesssim 10^{-6}$ over times $\sim 10^9$ yr, but pays nothing for that maintenance. In the strict thermodynamic sense a crystal is close to equilibrium with respect to its lattice structure, so the current dissipation $E_{\text{actual}}$ that would actively pay for maintenance equals zero. Since this zeroes $T_v$, $I_v$ is zeroed through $T_v$ as well, and $\eta_L$ itself, with $E_{\text{actual}} = 0$, equals zero by the convention of § 2.1 — diagnosis: structure without payment.

Systems in thermal equilibrium (an isolated gas, a closed black cavity) zero all three capacities simultaneously — the canonical negative control point of the screening.

*Cairns-Smith and the crystal-as-replicator.* The Cairns-Smith programme (1982) treated clay crystals as pre-RNA replicators — heritable lattice defects are passed to daughter crystals upon growth and cleavage. When the boundary is extended to "crystal + solution phase" the accounting changes: counterfactual ablation of § 2.2 for (crystal + ionic solution) yields $T_v > 0$ (the ion flux pays for the replication of lattice defects). However, $C_v^{\text{int}}$ remains undefined: an error in defect replication does not return as physical harm to the lattice itself. There is no channel in which a distortion of the defect pattern would worsen the thermodynamic conditions for the maintenance of the crystal. The diagnosis is a reassignment of the measured object onto (crystal + solution), analogous to the LLM-corp ($B_4$, § 3.4), not the vitality of the crystal-as-object. $\eta_L^{\text{int}}$ for a finished crystal is undefined through the simultaneous failure of $T_v^{\text{int}}$ and $C_v^{\text{int}}$.

### 3.4 Large language model

The case of the LLM requires, following the analysis of the Sun, an explicit distinction between two readings.

*Operational reading.* Under the extended boundary "model + data centre" the operational proxies give non-zero values. $T_v^{\text{op}}$, via the specific exergy flux of the data centre, is non-zero; $C_v^{\text{op}}$, via the normalised Lempel–Ziv complexity of the parameters and the quality of token prediction, is high. But this is a compression of the training corpus — a static imprint of selection in the dataset, not a model of the environment of the operating loop in the sense of § 2.1.

*Interpretive reading.* Under the strict boundary "weights at the moment of inference" (stateless forward pass) the system has no causally relevant environment in the sense of § 2.1: the output tokens do not return as physical harm to the weights, an error of the model does not dissipate free energy of the operating loop. $E_{\text{actual}}^{\text{own}} \to 0$ (the power grid is external) $\to T_v^{\text{int}} = 0$; at the same time there is no channel for the return of error into the operating loop $\to C_v^{\text{int}}$ is undefined. $\eta_L^{\text{int}}$ is undefined through the simultaneous failure of $T_v^{\text{int}}$ and $C_v^{\text{int}}$.

*Extension of the boundary and reassignment of the measured object.* When extended to "model + data centre + corporation" $\eta_L > 0$, but the object being measured becomes the **corporation**, not the model. The numerical estimate is built on two inputs for frontier models of the 2024–2026 era (GPT-4-class, $\sim 1.7 \cdot 10^{12}$ parameters). $E_{\text{actual}}^{\text{corp}} \sim 3.5 \cdot 10^{16}$ J/yr — an amortised accounting of the data centre, office, and supply chain. $I_{\text{cap}}^{\text{corp}} \lesssim 10^{12}$ bits — a **capacity-bound** by the carrier capacity (training corpus, operational memory, market analytics). This is an upper bound on $I_{\text{pred}}$. A precise measurement of the predictive information requires an MI estimate through the corporation's sensory channel (market signals → decisions on model deployment), and is an open task. $\eta_L^{\text{corp}} = I_{\text{cap}}^{\text{corp}} / N_{\text{max}} \lesssim 10^{-25}$ (**upper bound**). As the size of the corporation increases (number of employees, size of data centres, etc.), the energy expenditure grows with a larger exponent than the maintained predictive information: the positivity of $\eta_L^{\text{corp}}$ does not imply a substantial engagement of the self-payment loop — the corporation maintains a voluminous model of the environment, but its own dissipation exceeds the informationally relevant part by many orders of magnitude. The characteristic window of the corporation is operationalised as $\tau_d \sim$ a quarter — see the accompanying work Andriishin (2026), § 2.6; the annual normalisation of $E_{\text{actual}}^{\text{corp}}$ is a conventional rescaling, $\eta_L^{\text{corp}}$ is intensive and does not change by orders of magnitude under a $4\times$ contraction of the window. A cross-class numerical comparison with biology is illegitimate (the sign and the within-class order are comparable, § 3.5); what is substantive here is precisely the sign $\eta_L^{\text{corp}} > 0$ under a reassignment of the measured object onto the corporation. The reproducible computation is in the Supplementary Materials.

*Counterfactual ablation of the LLM-as-agent.* The application of § 2.2 gives two verdicts depending on the window. On the session scale: boundary = {weights}; simultaneous failure of $T_v^{\text{int}}$ and $C_v^{\text{int}}$ — $\eta_L^{\text{int}}$ is undefined. On the evolutionary scale the boundary extends to the corporation. Four expanding boundaries:

- $B_1$ = {weights} — counterfactual-degenerate ($E_{\text{actual}}^{\text{own}} = 0$ when the server is off, a static object);
- $B_2$ = {weights + KV-cache + executing server} on the session window (the power grid is external, $T_v^{\text{int}} = 0$ + $C_v^{\text{int}}$ undefined);
- $B_3$ = $B_2$ + training pipeline (dataset + GPU fleet + RLHF operators) on the model-generation window ($E_{\text{actual}}^{\text{own}} > 0$ through dissipation on GPUs, but the error-return loop closes onto the corporate operators);
- $B_4$ = $B_3$ + corporation-legal-entity (the full LLM-corp with $\eta_L^{\text{corp}} \lesssim 10^{-25}$, **upper bound**).

A full component-by-component analysis of candidates for inclusion is in Supplementary § S3.4.

*Operational test for existing frontier LLMs.* Counterfactual ablation of § 2.2 gives a diagnostic protocol for contemporary stateless LLMs (GPT-4-class, Claude, Gemini). The protocol: (i) identify the power-supply component; (ii) apply counterfactual subtraction; (iii) measure **whether an error of the model returns as a physical exhaustion of the carrier** (the carrier of $I_{\text{pred}}$) over the window $\tau_d$. For a stateless LLM the "error → harm" loop is absent — a structural necessary condition for the undefinedness of $\eta_L^{\text{int}}$, reproducible without special equipment.

*Agentic LLM wrappers.* Agentic wrappers of the 2023–2026 era — from Auto-GPT/AutoGen/Voyager to Claude Computer Use, Devin, OpenAI Operator, MemGPT, and systems with persistent RAG memory — extend the boundary of the base LLM. Through persistent memory and external tools they partially close the decision-making loop. The self-payment loop, however, remains open: the funding of execution, the infrastructure, the energy budget — all are held by the corporate substrate from outside. The agent's errors return as reputational and commercial sanctions through the external substrate, not as physical harm to the system itself. An intermediate case is a model with continuous fine-tuning on its own interactions: $\theta_{t+1} = \theta_t + f(\text{own predictions}_t, \text{feedback}_t)$. The loop is partially closed, but the payment for the update is still paid by an external GPU fleet ($T_v^{\text{int}}$ remains external, $C_v^{\text{int}}$ becomes partially defined). Contemporary systems of 2025–2026 (Claude Computer Use, Devin, OpenAI Operator, MemGPT) implement various combinations, but (a) persistent state, (b) own payment, and (c) a physical channel for the return of error are not jointly realised. The structural barrier is not the absence of technology but the absence of architectural pressure from the economics of AI toward internalising the energy budget. The diagnosis is the same as for the base LLM: $\eta_L^{\text{int}}$ is undefined (simultaneous failure of $T_v^{\text{int}}$ and $C_v^{\text{int}}$), with $C_v^{\text{op}}$ preserved. Connection with the literature: mesa-optimisation (Hubinger et al. 2019), power-seeking (Carlsmith 2022), goal misgeneralisation (Shah et al. 2022), specification gaming (Krakovna et al. 2020), the alignment problem (Ngo et al. 2022). The line of instrumental convergence — the self-preservation drive (Omohundro 2008) and its formalisation in Bostrom (2014) — records the structural tendency of an optimising agent to preserve its own continuation; the $\eta_L$-programme offers a thermodynamic co-characterisation of it. AI safety describes the behavioural signature of closing the loop of optimising one's own continuation; $\eta_L$ is a candidate thermodynamic co-characterisation of the same structural loop, described in AI safety in behavioural terms (not a causal-generative connection but a structural parallel).

A close conceptual parallel in AI safety is the *embedded agency* programme (Demski and Garrabrant 2019): the formalisation of an agent as a **part** of the environment, paying for its own computation. Self-payment is a thermodynamic reading of the intersection of robust delegation and subsystem alignment (the agent pays for the maintenance of a model of the environment of which it is a part); embedded world-models specifies WHAT is modelled, self-payment WHO bears the cost. This is not the full Demski–Garrabrant programme: the paying channel must belong to one physical system with the modeling one. $\eta_L$ offers a thermodynamic **necessary** condition for a physically realised embedded world-model with its own robustness loop (subsystem alignment in the sense of Demski–Garrabrant requires $S_v > 0$ within the model; robust delegation requires $T_v > 0$ of the delegate's own dissipation). $\eta_L > 0$ is not, and does not claim to be, a sufficient condition for specific alignment properties (corrigibility, low-impact agency).

*Comparison with the Sun.* For the Sun the zeroing proceeds along the line "no causally relevant environment → no $I_{\text{pred}}$ → numerator of $\eta_L$ is zero". For the LLM it proceeds along the line "a model of the parameters exists and compresses the training corpus, but the loop of its own dissipation does not pay for the maintenance of a model of the environment of the operating loop, so $T_v^{\text{int}} = 0$ and $C_v^{\text{int}}$ is undefined". The final diagnosis is negative in both cases; the diagnostic richness of the procedure lies in indicating the concrete failed capacity.

*The operational question of the vitality of artificial systems.* The vitality of an artificial system arises with the appearance of a built-in self-payment loop. The signature of closure is twofold: predictive information about the environment is physically maintained by the system's own operating loop, and errors of the model return as physical harm to the system itself. A two-level distinction is required, separating the structural condition of the loop from the empirical dynamics of its appearance.

*The level of definition (structural).* Counterfactual ablation of § 2.2 gives a **binary** answer: either the procedure converges to a stable boundary with a closed loop, or it does not. For the current stateless-LLM architecture the loop is open, $\eta_L^{\text{int}}$ is undefined. There are no intermediate states *at the level of definition*: either a physical channel for the return of error exists, or it does not. *The level of measurement (empirical).* For systems that have passed the screening, $\eta_L > 0$ — the concrete value depends on $I_{\text{pred}}$ (MI estimate), $E_{\text{actual}}$ (calorimetry), $T$, and $\tau_d$.

*Empirical dynamics of the appearance of the loop in AI.* The transition from a system without a self-payment channel to a system with a closed loop is a **transition through a structural threshold**, not a gradient within the positive class. Before the simultaneous internalisation of (a) persistent state, (b) own payment for computation, and (c) a physical channel for the return of error, the loop does not exist as an object of measurement; afterward, $\eta_L^{\text{int}}$ becomes measurable-continuous. The operational proxy "fraction of own dissipation $f = E_{\text{actual}}^{\text{own}}/E_{\text{actual}}^{\text{total}}$" gives a signal of proximity to the structural threshold. The detection scheme requires: (a) a population of $\sim 10^2$–$10^3$ autonomous embodied agents with their own energy budget; (b) physical wear as a channel for the return of error; (c) a control group; (d) measurement of $f$ and a check of counterfactual ablation of § 2.2 on each unit. The numerical threshold is Prediction 3 in § 5.
### 3.5 Bacterium

A bacterial cell passes both thresholds. The chemotaxis of *E. coli* — the classic observation of biased random walks (Berg and Brown 1972) — realises the canonical model object of a closed error-return loop. The methylation pattern of the chemotactic receptors is physically realised in the internal degrees of freedom of the cell (Tu et al. 2008; Shimizu et al. 2010) and is homomorphic to the gradient over the relevant variables, with relevance set by causal damage: distortion of the methylation leads to poor adaptation and to the loss of stability of the cell. The same pattern generates chemotactic movements that are testable by comparison with the actual distribution of the carbon source, so that all three properties of the model are satisfied and the error-return loop is closed.

A quantitative estimate of $\eta_L$ for the bacterium over the "generation" window yields two orders of magnitude depending on the denominator (the distinction between the two denominators is fixed in § 2.1). Through the computational denominator $E_{\text{comp}}$ (the fraction of exergy spent on irreversible information operations), $\eta_L^{\text{comp}} \sim 10^{-5}$. Through the exergetic denominator $E_{\text{actual}}$ (the entire exergetic part of the metabolic dissipation), $\eta_L \sim 10^{-8}$. Both numbers are consistent and measure different things; the derivation of both is given in the worked example below. The small absolute magnitude, together with positivity and stability, is a substantive result: the bacterium as a "stake-bearing compressor" is efficient by many orders of magnitude above zero and by many orders of magnitude below the idealised upper bound.

We situate the bacterium in the context of a hierarchy of scales — from the Bennett demon to the biosphere — where the $\eta_L$ scale yields positive values that decrease as the boundary is widened. The idealised Bennett demon (Bennett 1973, 1982) is the theoretical boundary of the irreversible regime according to the Proposition of § 2.1: one bit of $I_{\text{pred}}$, one obligatory erasure cost, $\eta_L \to 1$ as a theoretical limit. The bacterium: $\eta_L^{\text{comp}} \sim 10^{-5}$, $I_v \sim 0.5$ by the percentile of the cohort of prokaryotic chemotactic systems ($n \sim 200$ from BiGG/KEGG models). The worked example of the step-by-step calculation yields $\tilde{T}_v \approx 0.6$, $\tilde{C}_v \approx 0.55$, $\tilde{S}_v \approx 0.4$ with geometric mean $I_v \approx 0.51$ — Supplementary § S2.4. The mycorrhizal network: $\eta_L^{\text{comp}} \sim 10^{-5}$, $I_v \sim 0.55$ (order-of-magnitude estimate; normalisation per unit of capacity is an open problem; the canonical literature on mycorrhizal networks is Simard et al. 1997; Beiler et al. 2010; for a critical revision of the resource-transfer claims see Karst et al. 2023). The biosphere over the yearly window: $\eta_L \lesssim 10^{-22}$ through the exergetic denominator $E_{\text{actual}} = \text{NPP} \cdot \tau_{\text{year}}$, $I_v \sim 0.3$ (order-of-magnitude estimate). The numerator here is an upper bound set by the unique genomic content of the biosphere without accounting for copy number. The volume is estimated as $\sim 10^{12}$ species $\times 5 \cdot 10^6$ bp $\times 2$ bits/bp $\approx 10^{19}$ bits; the epigenomic layer adds up to $\sim 10^{20}$ bits. This estimate is many orders of magnitude below the full copy-number volume of biosphere DNA, $\sim 10^{37}$ bits (Landenmark et al. 2015). This is not a measured predictive information, and its operationalisation remains an open problem. What matters here is that at each level the scale reproduces, above all, the *sign* $\eta_L > 0$ when the self-payment loop is closed. The absolute values of $\eta_L$ across classes of systems are not directly comparable, with the same caveat as for the numerical $I_v$ (§ 2.4): the numerator is operationalised by different proxies for different classes (a Markov model of methylation for the bacterium, carrier capacity for the biosphere), so that the sign and the within-class ordering are substantively comparable, not the across-class absolute magnitude.

**Worked example ($\eta_L$ for the chemotactic loop of *E. coli*).**

The worked example demonstrates that $\eta_L$ is an operational measure, not a rhetorical one. The information model is the Markov scheme of Tu–Shimizu–Berg (Tu et al. 2008; Shimizu et al. 2010) for the mutual information between the ligand concentration at the Tar receptors and the methylation state. The energetics are from microcalorimetry (Liu et al. 2020).

*Numerator.* For a single measurement channel in the adaptation window $\tau \approx 10$ s, $I_{\text{pred}} \approx 1$–$2$ bits per measurement (Cheong et al. 2011; Mehta and Schwab 2012). Integration over the $\sim 7\,000$ Tar receptors of *E. coli* (on the order of $10^3$–$10^4$ measurements/receptors per generation) yields $I_{\text{pred}} \sim 10^3$–$10^4$ bits per generation — an upper bound under the assumption of channel independence. Cooperative binding in the receptor clusters ($\sim 10^3$ clusters per cell, not one cluster per receptor) lowers the actual $I_{\text{pred}}$ by $\sim 1$ order of magnitude; this effect is included in the lower bound of the sensitivity interval $[10^{-9}, 10^{-7}]$. The full protocol is in Supplementary § S3.5.

*Denominator.* The heat output in the stationary phase is $\sim 1$–$3$ pW/cell (Liu et al. 2020), and over a generation $\tau_d \sim 30$ min, $Q_{\text{heat}} \sim 2 \cdot 10^{-9}$ J/cell. By the single definition of § 2.1, $E_{\text{actual}}$ is the free energy supplied over the window $\tau_d$, which in the stationary phase equals the full integrated dissipation. For a bacterium in the stationary phase, $\eta_{\text{ATP}}$ over the generation window is small, and calorimetry gives a good approximation of the total exergy: $E_{\text{actual}} \approx Q_{\text{heat}} \sim 2 \cdot 10^{-9}$ J/cell (of order $\sim 10^{-9}$ J/cell). At $T = 310$ K, $k_B T \ln 2 \approx 3 \cdot 10^{-21}$ J, whence

$$N_{\text{max}} = E_{\text{actual}}/(k_B T \ln 2) \sim 3 \cdot 10^{11} \;\text{bits per cell}.$$

Only a small fraction of the exergy — of order $\sim 10^{-3}$ — goes to irreversible information operations, the rest to biomass synthesis and ion gradients; the estimate of this fraction is obtained as the ratio of the power of the sensory-computational network (Mehta and Schwab 2012) to the full metabolic budget of the cell (Liu et al. 2020). The computational bound: $N_{\text{max}}^{\text{comp}} \sim 3 \cdot 10^{8}$ bits/cell.

*Result.* Through the exergetic denominator, $\eta_L \sim 3 \cdot 10^{-8}$; through the computational one, $\eta_L^{\text{comp}} \sim 3 \cdot 10^{-5}$. The first number measures the fraction of the available free energy spent on self-modeling; the second, the fraction of the already-allocated-to-computation free energy that maintains the predictive information. Both numbers are correct within their own definitions. $\eta_L^{\text{comp}}$ is the principal physical answer, consistent with the Proposition of § 2.1 (the part of the exergy that actually pays for $I_{\text{pred}}$); the exergetic $\eta_L$ is a weak lower bound, since $E_{\text{actual}}$ includes biomass, ions, and heat losses that do not formally pay for $I_{\text{pred}}$.

The sensitivity analysis (ranges of the window $\tau$, partitions into intervals, the number of sensory families, $\eta_{\text{ex}}$) is in Supplementary § S3.5. The final conservative estimate: exergetic $\eta_L \in [10^{-9}, 10^{-7}]$ and computational $\eta_L^{\text{comp}} \in [10^{-6}, 10^{-4}]$. The point estimates at the upper bound of the numerator are $\eta_L \sim 3 \cdot 10^{-8}$ and $\eta_L^{\text{comp}} \sim 3 \cdot 10^{-5}$, via $I_{\text{pred}} \approx 10^4$ bits. The geometric medians of the sensitivity intervals $[10^{-9}, 10^{-7}]$ and $[10^{-6}, 10^{-4}]$ are $10^{-8}$ and $10^{-5}$, respectively. In § 7 (Conclusions) the geometric median $\sim 10^{-8}$ is used as the reference value. The numbers do not claim precision better than an order of magnitude — this is a methodological calibration. The wide sensitivity interval (about four orders of magnitude under both denominators) does not undermine the demarcation. The demarcation rests on the sign ($\eta_L > 0$ versus $\eta_L = 0$) and the within-class ordering, not on the absolute magnitude of the numerator; the metrological uncertainty of the numerator is orthogonal to the structural distinction between the vital and the non-vital. The full reproducible calculation with code is provided in the Supplementary Materials.

**Contrastive case (*E. coli* versus *Synechocystis*).**

The absolute value $\eta_L \sim 3 \cdot 10^{-8}$ for *E. coli* by itself is a methodological calibration, not a prediction. The discriminating power of the scale appears in the *contrastive* comparison of two biologically distinct systems with a different structure of predictive information over a comparable exergetic budget. The substantive contrast is written formally as the ratio $\eta_L^{(A)} / \eta_L^{(B)} = (I_{\text{pred}}^{(A)} / I_{\text{pred}}^{(B)}) \cdot (E^{(B)} T^{(A)}) / (E^{(A)} T^{(B)})$. With comparable denominators ($E_{\text{actual}}$ and $T$ differ by a few per cent and cancel), the discriminating power of the scale falls entirely on the numerator. The cyanobacterium *Synechocystis* sp. PCC 6803 is a convenient contrastive referent: its photosynthetic flux per cell per generation gives an $E_{\text{actual}}$ of the same order, $\sim 10^{-9}$ J/cell, as that of *E. coli*; its information environment, however — diurnal cycles of illumination and slow temperature gradients — is structurally simpler than the chemotactic environment of *E. coli* with its thousands of Tar receptors tracking rapidly changing chemical gradients. The order-of-magnitude estimate: $I_{\text{pred}}^{\text{Synechocystis}} \sim 10^3$ bits per generation against $I_{\text{pred}}^{\textit{E. coli}} \sim 10^3$–$10^4$ bits — approximately one order lower in the upper part of the range. Accordingly, $\eta_L^{\text{Synechocystis}} \sim 10^3/(3 \cdot 10^{11}) \approx 3 \cdot 10^{-9}$ — one order below the central estimate for *E. coli*.

*Epistemic status of the contrastive.* The *E. coli* / *Synechocystis* contrastive in its present form is an **illustrative sketch**, not independent empirical support for the prediction $r_{\text{adapt}} \propto \eta_L^{\alpha}$. The estimate $I_{\text{pred}}^{\text{Synechocystis}} \sim 10^3$ bits is obtained through the structural intuition "simpler than the chemotaxis of *E. coli*", not through a calibrated MI estimate of the specific channels of the cyanobacterium (the circadian KaiABC oscillator, the PsbA repertoire, the photosystem regulators). The comparison is built on a lower bound for *Synechocystis* against a central estimate for *E. coli* — this is an artefact of the asymmetric choice of limits, not an independent calibration. A rigorous falsification of the $\alpha$-dependence requires an independent co-measurement of the numerator and the denominator for both systems within a single protocol — this is a direction for future work, not a result of the present one. The contrastive is retained in the text as a methodological illustration of the **form** of the discriminating power of the scale (a difference of orders of magnitude within the biological class), not as a quantitative confirmation.

The programme of progressive falsification (§ 5) formulates the risk wager $r_{\text{adapt}} \propto \eta_L^{\alpha}$ — the rate of adaptation to new niches depends monotonically on the self-payment scale. In the contrastive pair *E. coli* / *Synechocystis* this yields an order-of-magnitude prediction: at $\alpha \approx 0.3$ the adaptation rate of the cyanobacterium should be approximately twofold lower ($10^{0.3} \approx 2$), and at $\alpha \approx 1$ up to tenfold lower. Agreement with the existing data on the rates of directed evolution of cyanobacteria and with Lenski's LTEE experiments on *E. coli* remains a matter for separate empirical testing and is formulated here as a direction for future work, not as an already confirmed observation. An analogous contrastive with the minimal cell JCVI-syn3.0 (genome of $\sim 473$ genes against $\sim 4300$ in *E. coli*, with a sharply reduced repertoire of responsiveness to chemical signals) predicts an $\eta_L^{\text{syn3.0}}$ that is 1–2 orders below *E. coli* and a proportionally reduced rate of adaptation to new conditions. Methodologically essential: $\eta_L$ works as a contrastive scale with a discriminating power that is **not derivable** directly from the individual components of Tu–Shimizu–Berg–Mehta–Schwab, which operationalise a single numerator in a single system. The contrastive *E. coli* versus *Synechocystis* / syn3.0 is an illustration of the discriminating role of the scale; a rigorous empirical test of $r_{\text{adapt}} \propto \eta_L^{\alpha}$ likewise requires a co-measurement of the numerator and the denominator within a single protocol for both systems.

### 3.6 Large city

A large city is a strong candidate for vitality at the planetary scale. Its infrastructure and administrative regulations are physically realised and paid for out of its own budget; they are homomorphic to the flows of resources, people, and information; and they generate targeted decisions that are testable by crises and adaptation. The error-return loop is closed: a distortion of the city's model of flows returns as a crisis to the city itself.

The city is a socio-technical system with a rich structural potential and at the same time a negligible $\eta_L$ through the exergetic denominator of the full dissipation. For a large metropolis, $E_{\text{actual}} \sim 10^{17}$ J/year — direct energy consumption of $\sim 10$ GW over a year; the upper estimate, accounting for the exergy of imported resources and supply chains, is $\sim 10^{19}$ J/year. Accordingly, $N_{\text{max}} = E_{\text{actual}}/(k_B T \ln 2)$ lies in the range $3.7 \cdot 10^{37}$ to $3.7 \cdot 10^{39}$ bits at $T \approx 285$ K. The **upper bound** on the numerator is $I_{\text{cap}}^{\text{city}} \lesssim 10^{10}$ bits: a **capacity-bound** estimate through the limiting capacity of the actually-used administrative model of flows (normative regulations + operational reports), not through the volume of archival data, $\sim 10^{15}$ bits. A proper measurement of the predictive information requires an MI estimate through a sensory channel (resource flows → administrative decisions), which remains an open problem. What is substantively compared here is the sign ($\eta_L^{\text{city}} > 0$ vs $\eta_L = 0$ for structurally rich non-living systems), not the quantitative capacity-bound estimate. $\eta_L^{\text{city}} = I_{\text{cap}}^{\text{city}} / N_{\text{max}} \approx 3 \cdot 10^{-30}$ under the upper estimate of the energy budget ($E_{\text{actual}} \sim 10^{19}$ J/year); the conservative upper bound through direct energy consumption ($\sim 10^{17}$ J/year, the smallest $N_{\text{max}}$) is $\lesssim 3 \cdot 10^{-28}$. Through the computational denominator (the fraction of dissipation spent on irreversible information operations in a socio-technical system) the estimate is substantially closer to the biological range. $E_{\text{comp}}^{\text{city}}$ is estimated — the consumption of the administration's data centres plus the operational electricity of office floor space — to give a factor $E_{\text{comp}}/E_{\text{actual}} \sim 10^{-4}$ relative to the full urban dissipation, which requires a separate operationalisation of the exergy of managerial computation. The same estimate quantitatively: $\eta_L^{\text{city,comp}} \sim 3 \cdot 10^{-26}$. The reproducible calculation of $\eta_L$ (Singapore and Detroit — merely order-of-magnitude-distinct energy budgets) is provided as code in `worked-example/city/` (archived per Data availability). There too the composite index $I_v$ (structural prerequisites, formula (2)–(2a)) is illustrated on a demonstration set of profiles. The empirical calibration of $I_v$ for specific cities from open data (OECD FUA, CDP Cities, WIPO/OECD REGPAT, GDELT, OpenStreetMap) is the subject of a separate work. For the paradigm-case claim, all that is essential is that the structural complexity of the city is high while $\eta_L$ is negligible.

The divergence in the directions of the two scales $\eta_L$ and $I_v$ is substantive. A smaller resource, with the error-return loop maintained, yields a higher efficiency of payment per unit of dissipation. $I_v$ measures how far the structural prerequisites for vitality are unfolded; $\eta_L$, how far the self-payment loop is closed.

### 3.7 Gaia and boundary cases

Earth's biosphere regulates the atmosphere, the ocean, and the climate through biogeochemical cycles — compression in the strict sense, paid for by species collapses, mass extinctions, and ecosystem reorganisations. The question of the unity of the model is open: does the biosphere have a single internal representation of its own environment, or billions of partial models of organisms not stitched into a single circuit (Doolittle 2014; Lenton and Latour 2018)? The answer determines whether Gaia is to be counted as a single vital system with $I_v \sim 0.3$, $\eta_L \lesssim 10^{-22}$, or as a family of overlapping vital systems with a nullified aggregate $I_v$. The estimate of $\eta_L$ is taken through the exergetic denominator $E_{\text{actual}} = \text{NPP} \cdot \tau_{\text{year}}$ at NPP $\sim 10^{14}$ W ($E_{\text{actual}} \sim 10^{21}$ J/year; $N_{\text{max}} \sim 10^{42}$ bits). The numerator is $I_{\text{cap}}^{\text{biosphere}} \lesssim 10^{20}$ bits ($\sim 10^{12}$ species $\times 5 \cdot 10^6$ bp $\times 2$ bits/bp $\approx 10^{19}$ bits plus the epigenomic layer). This is an estimate through the unique genomic content without accounting for copy number (**capacity-bound**), an **upper bound** on $I_{\text{pred}}$. A properly measured predictive information requires an MI estimate through a biogeochemical sensory channel, which for the biosphere remains an open problem. Through the computational denominator, the factor $E_{\text{comp}}/E_{\text{actual}} \sim 10^{-3}$–$10^{-2}$ is estimated (the lower bound is the overall energy balance, the upper the ATP equivalent of the neuro-signalling systems of the planetary biomass), which gives $\eta_L^{\text{biosphere,comp}} \in [10^{-20}, 10^{-19}]$, 2–3 orders above the exergetic estimate. $E_{\text{comp}}^{\text{biosphere}}$ is estimated as the ATP equivalent of the neural and signalling systems of the planetary biomass: animal nervous systems — $\sim 10^{12}$ kg of total biomass at a mean specific power of $\sim 10$ W/kg; to this are added the biochemical signalling networks of the microbial and plant components. Both numbers are deep in the "$> 0$ but physically irrelevant" zone; the demarcation by sign is preserved. What is substantively compared here is the sign ($\eta_L^{\text{biosphere}} > 0$ vs $\eta_L = 0$ for the structurally rich non-living), not the quantitative capacity-bound estimate. The full copy-number volume of biosphere DNA, $\sim 10^{37}$ bits (Landenmark et al. 2015), is a different, substantially larger quantity; the estimate adopted here is not a measured predictive information, and its operationalisation through biogeochemical proxies remains an open problem. The operationalisation of the computational denominator through proxies of the matter- and signal-processing dissipation of the biosphere is a separate open problem. The reproducible calculation is provided as code in `worked-example/biosphere/` (archived per Data availability). The biosphere is the only paradigm case where the exergetic and computational readings of $\eta_L$ may substantively diverge.

The six paradigm cases demonstrate that the demarcation works not through a binary "alive/non-living" table but through identifying the capacity of the failure. In the crystal, $T_v$ is nullified; in the LLM, under the boundary "weights at the moment of inference", there is a simultaneous failure of $T_v^{\text{int}}$ and $C_v^{\text{int}}$; in the Sun, the hurricane, the flame, and the Belousov–Zhabotinsky reaction, the failure is of $C_v$. Each structural cause of non-vitality points to a change of architecture that would make the system vital. The summary result: the space of observable matter is structurally complex almost everywhere (most objects pass the $I_v$ screening), yet vital almost nowhere (the $\eta_L$ verification screens out the Sun, the hurricane, the black hole, the LLM). The search for life reduces not to the search for complexity but to the search for closed self-payment loops.
## 4. Comparison with Adjacent Programmes

This section compares $\eta_L$ with the four programmes that have come closest to an operational definition
of vitality: assembly theory, Tononi's integrated information, Deacon's teleodynamics, and Friston's FEP. The
comparative diagnosis is the following: each operates at the level of $I_v$ or of a single capacity, and none reaches
the discriminating power of $\eta_L$ as a criterion for a closed self-payment loop.

### 4.1 Assembly theory

Marshall et al. (2017) formalised the Pathway Complexity measure — the minimal number of recursive assembly steps
needed to build an object with reuse of parts. Experimental measurement via mass spectrometry of complex molecules and
an empirical threshold (assembly index $a$ of order 15 for biogenic molecules) were established in Marshall et al.
(2021), and the full programme was formulated in Sharma et al. (2023). An object with $a$ above this threshold is
interpreted as a biosignature: the depth of accumulated selection required to assemble such an object is not reached by
abiotic processes on observable time scales.

The assembly index operates on the denominator of the "model × stake" dyad — a measure of accumulated selection — but
does not define the numerator. Assembly theory assigns equally high $a$ to a fossil and to a living cell, without
distinguishing selection accumulated in matter from the actual maintenance of $I_{\text{pred}}$. The error-return
coefficient in the object's current behaviour does not figure in the scheme. On the $\eta_L$ scale the assembly index
occupies the position of an operational complexity index, not a vitality scale: a high $a$ is a necessary condition for
the positivity of $\eta_L$ in systems with complex molecular architecture, but not a sufficient one. The assembly index
is an operational proxy for $C_v$ or $S_v$ within $I_v$, not an independent scale.

### 4.2 Integrated information $\Phi$

Tononi and his school (Tononi 2004; Tononi et al. 2016) defined integrated information $\Phi$ as a measure of the
irreducibility of a whole to the sum of its parts. In the IIT 3.0 formalisation (Oizumi et al. 2014), $\Phi > 0$ is
interpreted as a sufficient condition for minimal phenomenal consciousness. In the context of vital demarcation, $\Phi$
is a strong candidate for formalising the informational capacity $C_v$: systems with high integrated information satisfy
the requirement of a model in which the parts are not decomposable into independent subsystems.

Tononi's programme imposes no constraint on the thermodynamic cost of maintaining this integrated information, nor does
it require that the cost belong to the system itself. A household thermostat, under the weak formulations of IIT, has a
non-zero $\Phi$ — hence the conclusions about the minimal "experience" of simple systems discussed in Tononi et al.
(2016). $\Phi$ is a necessary condition for the positivity of $C_v$, not a sufficient condition for the positivity of
$\eta_L$: the thermodynamic belonging of the cost to the system remains outside the IIT apparatus. The connection is
productive as a decomposition: $\Phi$ operationalises $C_v$, while $\eta_L$ adds the requirement that $T_v > 0$ and that
it belong to the same system.

### 4.3 Teleodynamics

In *Incomplete Nature* (Deacon 2011), Deacon constructed a hierarchy homeodynamics → morphodynamics → teleodynamics.
The third level is defined as the coupling of two morphodynamic systems that mutually constrain each other's
self-destruction; the notion of *absential causality* is introduced — causation by something that does not yet exist
(a virtual goal, not actually given). Teleodynamics is the programme closest to the "model × stake" dyad: model and stake
are both present in the scheme logically, and both axes are articulated.

The defect of the programme is the absence of an operational quantitative measure. Deacon's hierarchy is formulated in
qualitative philosophical terms, and reconstructing $\eta_L$ or the error-return coefficient through absential causality
is technically impossible without substantial formalisation, which the text of the programme does not offer.
Teleodynamics is a structural portrait in which both axes of the dyad are present, but a quantitative measure testable
on a bacterium or a metropolis is absent. Teleodynamics is a conceptual predecessor, and its operationalisation through
the $\eta_L$ scale is one of the contributions of the present work.

### 4.4 The Free Energy Principle

Friston's Free Energy Principle (Friston 2010) is the formalisation closest to the present framework. The FEP literature
distinguishes two quantities. The *variational free energy* (VFE)

$$F[q, o] = D_{KL}\bigl[q(s) \,\|\, p(s|o)\bigr] - \ln p(o) \quad \bigl(= \mathbb{E}_q[\ln q(s) - \ln p(o, s)]\bigr), \tag{3}$$

or equivalently $F = D_{KL}[q(s) \| p(s)] - \mathbb{E}_q[\ln p(o|s)]$ (complexity minus accuracy, $-\text{ELBO}$),
is minimised in perception: the distribution $q(s)$ over the hidden states of the environment approximates the true
posterior $p(s|o)$, and $-F$ is a lower bound on the log-evidence $\ln p(o)$. The *expected free energy* (EFE)

$$G[\pi] = \mathbb{E}_{q(o', s'|\pi)}\bigl[\ln q(s'|\pi) - \ln p(o', s')\bigr], \tag{4}$$

is minimised in the selection of action / active inference. Here $p(o', s')$ is the distribution of preferences (a
generative model with preferences over future outcomes and states), and $G$ canonically decomposes into epistemic value
(the information gain about hidden states) and pragmatic value (proximity to preferences). The distinction is
fundamental: $F$ describes belief updating, while $G$ describes action selection (Friston 2010, 2019). For a Gaussian
generative model in the stationary regime, $-F \lesssim I_{\text{pred}}$ — a conceptual correspondence linking the scale
and FEP in the perceptual part; the formal connection is an open technical problem.

The canonical FEP-as-life line ontologises the Markov blanket as the boundary of the living. The canonical works are
Kirchhoff et al. (2018), "The Markov blankets of life"; Constant et al. (2018); and Ramstead et al. (2020). The BDDB
critique (Bruineberg et al. 2022) is aimed precisely at this line.

The principal objection to FEP is formulated in Bruineberg et al. (2022, hereafter BDDB) — a target article in BBS
format with open peer commentary. Three blanket notions are distinguished: the *Markov blanket* is a statistical
screening condition; the *Pearl-blanket* is an object of causal statistics (Pearl 1988); and the *Friston-blanket* is
the ontologisation of the Markov blanket as an objective boundary of a living system (Friston 2019). The central thesis
of BDDB is that the Pearl-blanket and the Friston-blanket are indistinguishable without the covert importation of
epistemic assumptions; the transition from the former to the latter qualifies as an equivocation. For BDDB the
thermostat is a diagnostic substitution of the thesis, demonstrating that the FEP apparatus carries no ontological load
of its own. Parallel critiques are Aguilera et al. (2022, a formal analysis of examples without a stationary density)
and Bruineberg et al. (2018, the ecological-enactive line). The debate over whether the BDDB critique can be parried
remains open.

Our move — the introduction of the self-payment requirement — does not effect the transition from the Pearl-blanket to
the Friston-blanket through a thermodynamic channel. $\eta_L$ offers an **alternative ontology**: instead of the
statistical reality of the blanket partition, the thermodynamic belonging of dissipation to a single physical system.
Self-payment is an assumption independent of the BDDB critique: it shifts the question from "does the Friston-blanket
exist" to "is the maintenance of the model paid for by the system's own dissipation". $\eta_L$ does not inherit the
epistemic structure criticised by BDDB. The denominator $N_{\text{max}}$ is a physical quantity observable through
$\partial F_X / \partial c$ under counterfactual ablation (§ 2.2, § 2.5), not a statistical measure over hidden states.
The assumptions (the candidate boundary, the threshold $\delta$, the window $\tau_d$) are explicit and testable through
sensitivity analysis (§ S2.4). For a thermostat the predictive information about its own environment is negligible: the
set point is given externally, and the numerator of $\eta_L$ tends to zero regardless of whether the thermostat has a
Friston-blanket.

*Counterfactual ablation of the thermostat.* Applying the procedure of § 2.2 to a bimetallic thermostat with hysteresis
$\Delta T_{\text{hyst}} = 1$ K, controlling a room with thermal inertia $\tau_{\text{room}} \sim 30$ min, enumerates
five candidates for inclusion in the boundary:

- the bimetallic strip (sensor and actuator);
- the relay contact group (energy switching);
- the heating element;
- the electrical grid as the current source;
- the external set-point setter.

Counterfactual ablation leaves the first two inside the boundary — their removal breaks the regulation circuit. The
remaining three are identified as external: ablating the heater removes the heat source, not the decision loop; ablating
the grid is analogous; ablating the set-point setter does not disrupt regulation around a fixed set point. Inside the
boundary $E_{\text{actual}}$ is the elastic relaxation of the metal plus relay dissipation, $\sim 10^{-6}$ W (the
reproducible calculation of the two interpretations — the trivial and the regulatory — is in the Supplementary
Materials). The internal channel maintaining $I_{\text{pred}}$ about the room temperature is the deformation of the
bimetal. The estimate is
$I_{\text{pred}} \le \log_2(\Delta T_{\text{room}}/\Delta T_{\text{hyst}}) \approx 3$ bits for a daily $\Delta T_{\text{room}} \sim 10$ K
(up to $\sim 5$ bits for a seasonal range of $\sim 30$ K). This $I_{\text{pred}}$ pertains to the environment "room,"
not to the environment "thermostat + room + power source." The loop of decisions paid for by the system's own
exhaustion is incomplete in the thermostat: heating the room is paid for by the external electrical grid, not by the
bimetal's own free energy. $\eta_L^{\text{thermostat}}$ is not defined in either of the two self-consistent
interpretations, but through the failure of different capacities. In the regulatory task "regulate the room
temperature," $T_v^{\text{int}}$ fails: the heating is paid for by the grid, with $E_{\text{actual}}^{\text{own}} = 0$
relative to this task. In the trivial task "maintain the bimetal's own shape," $S_v^{\text{int}}$ fails: passive
thermo-mechanical coupling does not form an error-return loop — when the bimetal's shape deviates, no dissipation of its
own corrects it. The divergence between the interpretations points not to an ontological transition but to the
conventionality of the boundary choice as a methodological instrument: one and the same physical system admits several
self-consistent boundaries. Bruineberg et al. (2022) show formally that such an ontological transition cannot be made
without the covert importation of epistemic assumptions. The full component-by-component analysis of the five
candidates is in Supplementary § S4.4.

The relation between the classes of FEP-applicable and $\eta_L$-vital systems is asymmetric. The claim "FEP is a special
case of $\eta_L$" is wrong in direction. The correct relation is the following: the $\eta_L$ scale singles out, within
the class of FEP-applicable systems, a subclass in which the minimised $F$ is paid for by the system's own dissipation.
Outside this subclass — a thermostat, a pendulum with an external power supply, any self-regulating circuit with an
externalised cost — $\eta_L$ vanishes through either the numerator or the denominator. FEP retains its descriptive power
across the whole class but loses its discriminating power: it does not separate systems with a stake from systems
without one. $\eta_L$ presents a thermodynamic criterion that is operationally independent of the FEP formalism. Systems
satisfying FEP with a non-empty action–perception loop and non-trivial own dissipation, as a rule, pass
$\eta_L$-verification. Systems satisfying FEP in a purely formal sense with externalised energy (a thermostat) fail
$\eta_L$-verification.

*Active inference and the space of correspondences.* Active inference (Friston et al. 2017; Parr et al. 2022) is a
concrete computational scheme derivable from FEP under policy selection via EFE. In active-inference terms, the
numerator of $\eta_L$ is connected to predictive information in the sense of a generative model, while the denominator
is connected to the **physical cost of realising the generative model in the system's own degrees of freedom**. This is
a premise of the $\eta_L$ programme, added to standard AIF — it is not derived directly from EFE minimisation. The
pragmatic and epistemic value of policies are connected to the numerator (predictive information) through the structure
of the generative model, not directly to the denominator. A detailed mapping of vocabularies (action, policy, pragmatic
value, epistemic value vs $I_{\text{pred}}$, $E_{\text{actual}}$, $T_v$, $S_v$) is a task for a separate work; what is
essential here is that the correspondence is technically possible and does not require revising either of the original
frameworks.

*Andrews 2021 and Williams 2020.* Andrews (2021) attacks FEP for the non-derivability of empirical content from the
formalism; the critique is parried in $\eta_L$ by anchoring the numerator and denominator to measurable quantities.
Williams (2020) attacks predictive coding as a neural mechanism, not predictive information as a formal measure; the
critique is neutral toward $\eta_L$. A detailed discussion and the distinction between predictive coding (Rao and
Ballard 1999; Clark 2013) and predictive information (Bialek et al. 2001) are in Supplementary § S4.4a.

Summary position: the free-energy-minimisation formalism becomes a substantive criterion of vitality only under the
condition of self-payment. Without this condition, FEP describes any self-regulating circuit and loses its
discriminating power. With this condition, FEP is refined into its $\eta_L$-discipline. For systems where FEP is
applicable with a non-empty action–perception loop and non-trivial own dissipation, $\eta_L$ and FEP give consistent
characterisations. For systems where FEP is applicable only in a purely formal sense with externalised energy, $\eta_L$
vanishes through the numerator.

### 4.5 Demarcation from adjacent programmes: a comparative diagnosis

The summary comparative diagnosis of the principal programmes is collected in the table below, and it reveals a single
structural pattern of defect: each programme takes seriously exactly one side of vitality and leaves the others outside
its apparatus. The organisational-closure line (Maturana–Varela, Rosen, Mossio–Montévil–Longo) and the line of OoL
programmes are analysed at length in § 4.7 and § 4.8 respectively; in the table they appear as one-line positional
summaries.

| Programme | Axis taken seriously | What is left outside the apparatus |
|-----------|---------------------|-------------------------------------|
| Walker–Cronin (assembly theory) | the denominator of the dyad — selection accumulated in matter (assembly index $a$) | the numerator is implicit; $a$ is identical for a fossil and a living cell — vital discrimination requires an external intuition about the error-return loop |
| Tononi (IIT) | the measure of informational integration $\Phi$ | the thermodynamic cost; the $\Phi$-positive thermostat is a known critical point of the theory |
| Deacon (teleodynamics) | the structural dyad (absential causality) | a quantitative measure: absential causality is not reconstructed through measurable quantities |
| Friston (FEP) | the free-energy-minimisation formalism | the requirement that model and dissipation belong to one system; the robust critique of Bruineberg et al. 2022 calls into question the path of ontologising the Friston-blanket (an open debate without an established consensus), while $\eta_L$ offers an alternative thermodynamic ontology independent of the outcome of that debate (see § 4.4) |
| Maturana–Varela / Rosen / Mossio–Montévil–Longo (organisational closure) | the requirement that the loop belong to one system | a quantitative thermodynamic discipline: qualitative closure without a Landauer budget (see § 4.7) |
| Hordijk–Steel / England / Maynard Smith–Szathmáry / Pross / Smith–Morowitz (OoL programmes) | each operationalises one side of the abiotic→biotic transition | a unifying operational measure of self-payment as a single thermodynamic criterion for the moment of the origin of life (see § 4.8) |

The listed defects are not accidental: they reflect different ways of taking one side of vitality seriously and leaving
the others outside the apparatus. $\eta_L$, as a ratio that requires both components to belong to one system, is an
operationalisation that does not allow any of the four axes to dissolve into the background.

### 4.6 Connection to the tradition: a brief positional summary

The $\eta_L$ programme is located at the intersection of classical traditions. The line of Schrödinger (1944, aperiodic
crystal + negative-entropy formula) and Szilard–Landauer–Bennett (1929–1989, the thermodynamic cost of information
operations) is the direct inheritance of the numerator and denominator. The non-equilibrium thermodynamics of
Prigogine–Nicolis (Nicolis and Prigogine 1977) is a predecessor of $T_v$. Wiener–Ashby–Foerster (Wiener 1948;
Ashby 1952; von Foerster 2003) is second-order cybernetics. To this also belong Rosen's anticipatory systems
(Rosen 1985) and Taleb's skin-in-the-game (Taleb 2018, the stake concept formalised in § 2.1). Kolmogorov's algorithmic
information (Kolmogorov 1965) is a predecessor of $C_v$. Kauffman's autocatalytic closures (Kauffman 1993, 2000) and the
Walker–Davies–Ellis programme framework (Walker et al. 2017a) complete the list. $\eta_L$ is not the heir of any one of
them but a juxtaposition: a thermodynamic framework plus predictive content plus a structural accounting of capacities
through counterfactual ablation (§ 2.2). The scale gathers both axes of the "model × stake" dyad into a single measurable
quantity and explicitly introduces the requirement of own dissipation. Each classical programme is operationalised through
one of the capacities within $I_v$; the unification into a single vitality scale is an independent step that none of the
original frameworks took. An extended positional map is in § S4.7–S4.9 of the supplementary.

### 4.7 The organisational-closure line

The *organisational-closure line* (autopoiesis, Maturana–Varela 1980; M,R-systems, Rosen 1991; constraint closure,
Mossio–Montévil–Longo 2016; organisational closure, Bich–Green 2018; plus the epistemic cut, Pattee 1982) formulates
life through the closure of causal processes. Closure is taken relative to efficient causation or the constraint network
that produces the system's components. The $\eta_L$ programme is categorially distinct: organisational closure formalises
the production of components and qualitative circularity; self-payment formalises the thermodynamic belonging of the
model's budget to a single physical system together with the modeler. A *differential test* on the pair *E. coli* /
JCVI-syn3.0 (Hutchison et al. 2016) distinguishes scales within a single class of organisational closure: qualitative
criteria do not distinguish these systems, whereas $\eta_L$ ranks them through the product of the informational and
thermodynamic components. Self-payment does not claim to rebrand or replace organisational closure — it adds to its
qualitative conceptual work a quantitative thermodynamic discipline through the Landauer budget. The full analysis of
the four lines (Pattee, Maturana–Varela, Rosen, Mossio–Montévil–Longo) with categorial distinctions and the
differential test is in § S4.7 of the supplementary.

### 4.8 The origin-of-life line

The *origin-of-life line* is represented in *Theory in Biosciences* and adjacent journals by five relatively autonomous
traditions. The Eigen–Schuster hypercycle (Eigen 1971; Eigen and Schuster 1979) is a replicator-level autocatalytic
closure with a template carrier. RAF networks (Hordijk and Steel 2004) are a formalism of collective autocatalysis.
Dissipative adaptation (Perunov, Marsland, and England 2016; the statistical foundation in England 2013, *Statistical
physics of self-replication*) is a thermodynamic predecessor of the denominator of $\eta_L$. The major transitions
(Maynard Smith and Szathmáry 1995; Szathmáry 2015) are a hierarchy of evolutionary levels with a reassignment of the
subject. The geochemical programmes (Pross 2012; Smith and Morowitz 2016; Kauffman 2019; Martin and Russell 2003) detect a
closed loop on top of a geochemical flow. Each operationalises one side of the abiotic→biotic transition. In
$\eta_L$ terms, all five articulate one and the same phase transition. The moment of the origin of life is the moment
when a geochemical system passes from external payment to self-payment: part of the free energy closes within its own
circuit and physically pays for the maintenance of the model of the environment. The positivity of $\eta_L$ is a
**necessary condition** for this moment in each of the programmes; sufficient conditions include Darwinian dynamics at the
population level (§ 2.7). An operational procedure for measuring $\eta_L$ on a pre-biotic geochemical substrate is not
defined and constitutes an open problem of the programme. A detailed analysis of the five traditions, indicating points of
contact and the parallel programme of Chirumbolo–Vella (2026), is in § S4.8 of the supplementary.

### 4.9 Positioning within contemporary demarcation debates

The $\eta_L$ programme is methodologically compatible with six robust lines of contemporary philosophy of biology. These
are the anti-definitionism of Cleland (2019), the cluster definitions of Mariscal–Doolittle (2020), the operational
frontiers of Bich–Green (2018), the process biology of Pradeu (2018), the information-theoretic individuality of
Krakauer et al. (2020), and the basic autonomy of Ruiz-Mirazo–Moreno (2004). The programme acts not as an alternative to
them but as a formal quantitative scale on which these lines can work jointly. $\eta_L$ does not offer yet another
definition of life through lists of features, but it contributes an operational discriminator with an explicit
falsification regime (§ 5) and a processual ontology (the scale is computed over the window $\tau_d$, § 2.6). On the
borderline cases (virus-in-isolation, minimal cell, LLM-as-corporation), the scale behaves in agreement with biological
convention through counterfactual ablation (§ 2.2). This is a contribution to the ongoing demarcation discussion, not a
proposal for a new definition of "what life is." A detailed positional diagnosis of each of the six lines is in § S4.9
of the supplementary.
## 5. Falsification Criteria

The programme admits falsification along eight independent lines, grouped into three blocks. A procedural rule
common to all of them: the system boundary and the proxies $I_{\text{pred}}$, $E_{\text{actual}}$ are fixed prior to
verification of $\eta_L$ and are not revised in order to obtain the desired sign (§ 2.2). Falsification operates at
two levels — methodological (a defect of the current operationalisation) and ontological (the failure of the concept
itself); the distinction is fixed post hoc for each line that is actually realised.

### Block 1 — Direct refutations of the scale

These attack the structure of $\eta_L$ by nullifying one of the three capacities.

1. **$T_v$ failure.** Observation: stationary maintenance of $I_{\text{pred}} > 0$ at $E_{\text{actual}}$ below the
   Landauer bound in an irreversible regime ($\dot Q > 0$ — an operational test of irreversibility). Refutes: either
   the postulate of stationary accounting (c) of the Proposition in § 2.1, or one of conditions (a)–(b); nullifies
   $T_v$ as a necessary condition.
2. **$C_v$ failure.** Observation: a system with positive $C_v^{\text{op}}$ at $\dot{H}_{\text{erasure}} = 0$ over
   the window $\tau_d$ — maintenance of predictive information without paying for Landauer erasure per predictive bit.
   Refutes: $C_v$ as a necessary condition.
3. **$S_v$ failure.** Observation: a system with $\eta_L > 0$ under simultaneous $Q < Q_{\text{null}} + 2\sigma$
   (modularity indistinguishable from a degree-preserving null model — the configuration model, which preserves the
   degree distribution) and $C(k) \not\sim k^{-\beta}$ with $\beta \in [0.5,\, 1.5]$ (absence of a hierarchical
   signature in the sense of Ravasz–Barabási 2003). Refutes: $S_v$ as a necessary condition.

Refuting any single capacity simultaneously collapses both scales — $\eta_L$ through the numerator/denominator, $I_v$
through the geometric mean. This is one falsification via capacity, not a double one.

### Block 2 — Tests of proxies and operationalisation

These attack not the structure of the scale but its anchoring to measurable quantities.

1. **Violation of the monotonicity of the adaptation rate in $\eta_L$.** Observation: in a controlled experimental
   evolution, systems whose $\eta_L$ differs by an order of magnitude yield adaptation rates that are statistically
   indistinguishable over long windows. Refutes: the central relation loses its numerical meaning (the constructive
   form is Prediction 1 below).
2. **Vitality along three independent channels at $\eta_L = 0$.** Observation: a system with positive vitality by
   adaptation rate, self-repair speed, and biochemical markers of self-reproduction (Joyce 1994), but with
   $\eta_L = 0$ under all sanctioned operationalisations. Refutes: the numerator as an operational proxy
   (methodological level, § 2.7) or the concept of vitality as efficiency of self-modeling (ontological level).
3. **A conventionally living system with $\eta_L = 0$.** Observation: a biological system, unquestionably alive by
   conventional criteria, with strictly zero $\eta_L$ under all reasonable operationalisations. Refutes: the adequacy
   of the scale as an operational discriminator of vitality.

### Block 3 — Progressive predictions

Excess empirical consequences of the programme that are not derivable from competing frameworks.

1. **Prediction 1 — power-law dependence of the adaptation rate.** Observation: across 45 lineages of *E. coli* in a
   chemostat, $r_{\text{adapt}} = A \cdot \eta_L^{\alpha}$ with $\alpha \in [0.3,\, 1.0]$ and a correlation
   coefficient $\rho \in [0.4,\, 0.7]$ (Pearson between $\log r_{\text{adapt}}$ and $\log \eta_L$). Refutes:
   $\hat{\alpha}$ significantly outside $[0.3,\, 1.0]$ at $p < 0.01$ (wrong exponent); $\hat{\rho} < 0.2$ (no
   detectable trend); $\hat{\rho} < 0$ (a trend in the opposite direction — a qualitative refutation).
2. **Prediction 2 — monotonicity of $\eta_L$ in the matching window.** Observation: in the regime of approach to
   stationarity at normalised dissipation, a monotonic increase of $\eta_L(\Delta\tau)$ is expected over the interval
   $\Delta\tau \ll \tau_d$. Refutes: a decrease of $\eta_L$ with $\Delta\tau$ — a counter-argument to the stationary
   framework as such.
3. **Prediction 3 — empirical threshold of energy-budget internalisation $f^*$** (where
   $f = E_{\text{actual}}^{\text{own}}/E_{\text{actual}}^{\text{total}}$ is the fraction of own energy in the total
   budget). The structural predicate of self-payment loop closure is **binary** (counterfactual ablation, § 2.2: the
   error-return channel either self-pays or it does not); $f$ is a continuous proxy of this closure, not the deciding
   threshold itself. Observation: for hypothetical autonomous embodied agents, the fraction passing the screen
   ($\eta_L^{\text{int}} > 0$) rises sharply above an empirical threshold $f^* \in [0.1,\, 0.5]$ — a statistical
   regularity of joint internalisation (persistent state + own payment + a physical error-return channel), not a
   structural definition. Refutes: systematic observation of a system with $f \in [0,\, 0.1]$ that passes the screen,
   or with $f > 0.5$ that fails it. Differential prediction relative to AI safety (Hubinger et al. 2019; Carlsmith
   2022): the threshold of *capabilities* is independent of the *thermodynamic budget* $f^*$; the scope is not
   applicable to present-day cloud-hosted stateless LLMs ($f = 0$ by construction).

*Condition confirming the uniqueness of the operationalisation (not a falsification criterion).* The discovery of an
alternative proxy that yields the same demarcation discrimination but is not reducible to $\eta_L$ through an identity
or a monotone transformation does not refute the programme — it confirms the substantive content of the demarcation.

The full operational protocols (numerical criteria, p-values, sample sizes, pre-registration requirements, the
Bennett-regime caveat for Block 1 item 1, the NASA referent for Block 2 item 2, the scope scenarios of Prediction 3)
are in § S5 of the Supplementary. The consolidated Lakatosian dossier of the programme is in § S5.4.

## 6. Discussion and Open Problems

*Astrobiology.* The principal consequence is a reformulation of the programme for the search for life. Most objects
pass the $I_v$ screen (structural potential is universally high) and fail $\eta_L$ verification (the actual closure of
the self-payment loop is rare). Operationally: in the design of biosignature search missions (Europa Clipper, JUICE,
Dragonfly, exoplanet spectroscopy) the priority shifts from chemical disequilibrium to the search for a triple
simultaneity — non-equilibrium chemistry ($T_v$), a biogenic-like informational signature ($C_v$, through isotopic
fractionation and chirality), and a hierarchically modular topology of the medium ($S_v$). Each is a necessary
condition; the simultaneity of all three is an operational candidate for a biosignature. The connection to the
existing methodological framework of the Ladder of Life Detection (Neveu et al. 2018): $\eta_L$ is positioned as one
of the slices of operational criteria for life detection, complementing the chemical-structural rungs of the ladder
with a thermodynamic requirement of self-payment.

*The origin of life as closure of the self-payment loop.* The biosignature search programme fixes **where** life
exists; a parallel question is **when** it arises on an evolving geochemical substrate. Here, as in § 3.4 for AI
systems, an explicit two-level distinction is required.

*Structural level.* The positivity of $\eta_L$ is a **necessary condition** of the moment of the origin of life
(consistent with § 4.8 and the formulation of the "necessary, not sufficient" thermodynamic requirement of
self-payment). Sufficient conditions include Darwinian dynamics (§ 2.7), which entered the working NASA definition of
life as a "self-sustaining chemical system capable of Darwinian evolution" (Joyce 1994); $\eta_L > 0$ fixes the
thermodynamic slice, evolutionary dynamics the selective one. Structurally, the moment of passing the counterfactual
ablation of § 2.2 is the moment when the geochemical network first constitutes itself as a closed catalytic loop with
self-payment: part of the free energy ceases to pass through in transit and begins to pay for the maintenance of its
own predictive information about the environment. Before this moment $\eta_L$ is **undefined** (there is no loop as an
object of measurement); after it, $\eta_L$ is continuously measurable. The boundary between "before" and "after" is a
binary structural predicate of counterfactual ablation, not a gradient within the positive class.

*Empirical level.* The operational procedure for measuring $\eta_L$ on a pre-biotic geochemical substrate is not
defined and constitutes an open problem of the programme — a programmatic promise / direction of research that
requires the development of proxies for $I_{\text{pred}}$ and self-payment in an evolving geochemical network. The
counterfactual ablation of the boundary in § 2.2 and the MI estimate of $I_{\text{pred}}$ through the sensory channel
apply to already-formed biological systems; their transfer to the pre-biotic register is a concrete direction of
operational extension. Possible steps: (a) RAF sets (Hordijk and Steel 2004; Hordijk 2019) as a structural proxy of
the closure of the catalytic loop — counterfactual subtraction of individual network components is an operational
realisation of § 2.2 on the geochemical graph. (b) Isotopic signatures (fractionation of $\delta^{13}\mathrm{C}$,
$\delta^{34}\mathrm{S}$) and chiral signatures — a proxy for $C_v$ (the network's memory of the state of the
environment). (c) An integrated thermodynamic-network test of the positivity of self-payment through the measured
free-energy balance of a RAF-closed subnetwork relative to its reactive surroundings. The development of such proxies
and their calibration on contemporary biological miniatures (minimal cells, synthetic protocells) is future work.

The connection to hydrothermal hypotheses is direct. This includes the alkaline-vent scenarios of Martin and Russell
(2003), the metabolic-core programmes of Smith and Morowitz (2016), dynamic kinetic stability (Pross 2012), and
Kauffman's adjacent-possible (Kauffman 2019); the general physical framework of OoL is Walker (2017b). Each of these
programmes articulates the same structural transition from its own side, without a unifying thermodynamic measure.
The constructive diagnostic is formulated as a direction of development, not as an already-available protocol. It
requires the simultaneous appearance of three components: catalytic closure through RAF analysis of the geochemical
network (Hordijk and Steel 2004; Hordijk 2019), informational memory through isotopic and chiral signatures, and a
positive thermodynamic account along the scheme of § 5. This is an operational reformulation of the task of
astrobiology: not only "to find where life is," but also "to detect the structural transition to it" — falsifiable in
the case of the discovery of geochemical systems with a stable $\eta_L > 0$ lacking the characteristic triad, once
the methodology has been operationally fully developed.

*Artificial-intelligence ethics.* The shift from the question "is the model complex enough to be a moral subject" to
the question "will the model begin to physically bear the cost of its own errors." The appearance of an own
dissipative payment for the model maintained in the own degrees of freedom of the operating loop is the structural
condition under which $\eta_L$ leaves the region of indeterminacy and enters positive values. The phase character
pertains to the definition of the self-payment loop (the structural predicate of counterfactual ablation, § 2.2, is
binary), not to the empirical transition of the system; the empirical dynamics of the loop's appearance in a real
population of AI systems is an open question with an expected continuous profile along the fraction of internalised
payment. The current standard LLM architecture (a stateless forward pass with externalised payment of infrastructure)
precludes satisfaction of the structural condition. The path to positive $\eta_L^{\text{int}}$ for an artificial
system requires the simultaneous internalisation of (a) persistent state, (b) own payment of computation, and (c) a
physical error-return channel — not jointly realised in any existing system at the time of writing. This is a
structural condition, not a calendar forecast. Formal mapping to the triad. (a) Persistent state operationalises
$C_v^{\text{int}} > 0$ (a memory channel for maintenance). (b) Own payment of computation — $T_v^{\text{int}} > 0$
(an own thermodynamic budget). (c) A physical error-return channel — $S_v^{\text{int}} > 0$ (closure of the loop's
topology). The simultaneity of all three yields $\eta_L^{\text{int}} > 0$.

To "bear its own errors" — in the technical sense of § 2.1: the model's errors return as a physical loss of the
system's own free energy, not as reputational sanctions through an external corporate substrate. A decline in the
usage frequency of an LLM and its retraining by the corporation are a payment of the corporation, entering the
$\eta_L$ of the corporation; the $\eta_L^{\text{int}}$ of the model as an agent remains zero. Regulatory fines, legal
sanctions against the developer, and market reputational losses return the harm not to the system that maintains the
model but to its external substrate.

*Complex systems and social dynamics.* In application to cities and civilisations, the scale opens two thresholds:
structural screening ($I_v$) and verification ($\eta_L$). A civilisation with high $I_v$ and a sagging $\eta_L$ —
structurally rich, failing the maintenance of the loop — is diagnostically distinct from a civilisation with a
sagging screen (destruction of infrastructure). This differentiation is useful for studies of the resilience of
social systems; it requires empirical verification.

*The Fermi paradox and the externalisation filter.* The paper's hypothesis applied to the Fermi paradox: the silence
of the Universe is explained not by the rarity of life but by the **collapse of technological civilisations at the
threshold of energy-budget externalisation**. In the terms of the framework: a civilisation passes the "filter" if
and only if its $\eta_L$ is positive through its own dissipation ($T_v$ maintained within its loop). Technological
development directed at the use of external sources (the power grid → reactors → megastructures) increases
$E_{\text{actual}}^{\text{external}}$ without increasing $E_{\text{actual}}^{\text{own}}$ — most civilisations pass
the $I_v$ screen (visible structural complexity: radio signals, megastructures) but **fail $\eta_L$ verification** by
the same mechanism as a stateless LLM under the boundary "the weights at the moment of inference." Such civilisations
are unstable on evolutionary timescales and do not persist as stationary SETI sources. This claim has the status of a
speculative extrapolation and is subject to independent empirical verification. A testable statistical prediction
about observable SETI signals: transient, non-repeating, a power-law distribution over duration with a cutoff — an
indicator of the filter; a stationary spectrum with an infrared excess, holding over decadal windows — an indicator
of passing both thresholds. The existing null results of Dyson-sphere searches (the G-HAT survey over ~10⁵ WISE
galaxies, Griffith et al. 2015; the justification of the programme — Wright et al. 2014) are consistent with the
prediction of the filter but do not refute alternative scenarios (rare-Earth-class hypotheses, technological maturity
below astrophysical resolution). Condition of refutation: the discovery of three or more independent stationary SETI
sources with a confirmed infrared signature of megastructures over intervals $\gtrsim 50$ years is incompatible with
the prediction of the externalisation filter in its current formulation.

*Status of the consequence.* The reformulation has the status of a speculative extrapolation: neither the NASA
Astrobiology Strategy, nor the ESA Cosmic Vision, nor the planetary Decadal Survey operates with the category of a
"self-payment loop." If the standard programmes achieve a reliable demarcation of extraterrestrial life without
recourse to $\eta_L$, the framework will bring no astrobiologically new discriminating power and will reduce to the
existing agnostic biosignatures.

*Open problems.* A non-stationary version of the lemma on stationary erasure (§ 2.1) for systems with growing memory
— biospheres on aeonic windows, learning artificial systems — requires a rigorous proof that accounts for the cost of
expanding memory. The catalogue of operational proxies for $I_{\text{pred}}$ requires extension with numerical
examples and bounds of applicability. The Gaia case — the question of the unity of the biosphere's model — is open
empirically and depends on data about the consistency of biogeochemical cycles on aeonic windows. The operational
protocol for detecting vital AI requires precise thresholds for population-level experiments. The philosophical
status of $\eta_L$ — a position of moderate operationalism with a distinction between the ontological referent and
the operational measure — is the task of a separate work.

*Dormant states.* Biological states of reversible arrest — spores, a tardigrade in cryptobiosis, frozen embryos, the
lysogenic cycle of a phage — formally give $\dot{I}_{\text{pred}} = 0$ and $E_{\text{actual}} \to 0$, which takes
$\eta_L$ out of the domain of definition of the scale (see § 2.1, "Convention on the domain boundary"). Reconciliation
with biological convention ("spores are alive") is achieved through the averaging window $\tau_d$: with a choice of
$\tau_d$ on the evolutionary scale (the full cycle sporulation $\to$ activity $\to$ sporulation) the sign of $\eta_L$
returns to positive. A formal extension of the scale to regimes of temporary sign reversibility is a direction of the
accompanying work (Andriishin 2026).

*Boundary conditions of applicability.* The $\eta_L$ scale does not make three types of claims.

1. It does not assert the identity of vitality and consciousness. High $\eta_L$ is a necessary condition of complex
   cognitive activity (without the maintenance of own predictive information, neither prediction, nor planning, nor
   reflection is possible), but not a sufficient one. The question of phenomenal experience, discussed within the
   framework of integrated information (Tononi et al. 2016) and the hard problem of consciousness, lies beyond the
   $\eta_L$ scale.
2. It does not entail biocentrism by a reverse move. High $\eta_L$ is possible in systems of a non-biological
   substrate — large cities, planetary-scale biospheres, hypothetical artificial embodied agents with a closed
   self-payment loop. This is a substantive prediction, not a calibrational fit.
3. It does not reduce to a moral criterion. A civilisation that fails $\eta_L$ verification while retaining the $I_v$
   screen is diagnosed as structurally rich but non-living — a diagnosis of a structural state, not an ethical
   verdict. The ethical consequences of the programme are a separate topic, resting on the structural diagnosis but
   not derivable from it by direct implication.

*The stationary regime as an explicit limitation of the domain of applicability.* All the presented results —
definitions, lemmas, demarcation tests on paradigm cases, falsification conditions — are formulated under the
assumption of stationarity of the environment and finiteness of the system's memory. This is not a default
simplification: stationarity yields an operationally precise Bayesian update, reducible to instantaneous Landauer
erasure, and therefore permits sharp formulations of demarcation answers. In the non-stationary regime — with growing
memory, a drifting environment, and a non-empty archival layer — the formalism requires extension: a cumulative
Landauer budget, accounting for the cost of maintaining historical bits, and the phenomenon of informational
nostalgia. This extension is the content of the accompanying work (Andriishin 2026). There, a conditional
lemma on the inevitability of nostalgia is proved in the canonical class of slow drift (OU parametrisation with
FIFO-refresh and $c < 1$). The quantitative adiabatic asymptotics $\dot{\eta}_L^{\text{excess}}$ for systems without
periodic memory reset is formulated there as an open hypothesis supported by a parametric scan. The informational
capacity $C_v$ of the present work is there methodologically refined through a partition into $C_v^{\text{static}}$
(a first-class structural proxy, § 2.3) vs $C_v^{\text{predictive}}$ (a second-class predictive proxy, § 2.3),
related by $C_v^{\text{predictive}} = (1 - \nu) \cdot C_v^{\text{static}}$, where $\nu$ is the fraction of nostalgic
bits; in the stationary limit $\nu \to 0$ the distinction vanishes, which reconciles the two works. The applicability
of the stationary $\eta_L$ developed in the present article is limited to systems with an ergodic environment and
finite memory; for biospheres on aeonic windows, learning AI systems under drift, and civilisations with a growing
archive — refer to the non-stationary extension.
## 7. Conclusions

This work has defined vitality operationally, as the Landauer efficiency of self-modeling: the dimensionless ratio
$\eta_L = I_{\text{pred}} / N_{\text{max}}$ of the predictive information a system maintains about its own environment to
the Landauer budget of its own dissipation in the irreversible regime. Positivity requires the simultaneous presence of three capacities — $T_v$, $C_v$, $S_v$ —
assembled into a composite index of structural prerequisites $I_v$. The index is a necessary but not sufficient condition
for vitality; it occupies the same positional place as the assembly index, $\Phi$, and Deacon's morphodynamics. $\eta_L$ itself is
an operational criterion of synchronic vitality in the sense of a binary sign ($\eta_L > 0$ when the self-payment loop is closed).
The criterion distinguishes structurally rich but non-living systems (the Sun, a hurricane, an LLM at the "weights
at inference time" boundary — where $\eta_L^{\text{int}}$ is undefined) from systems with a structurally closed self-payment loop under the
counterfactual ablation of § 2.2. Among systems with a closed loop, the bacterium has a reproducibly measured $\eta_L > 0$
via § 3.5. The city, the biosphere, and the LLM-as-corporation have a structurally positive sign under a capacity-bound upper
bound on the numerator; a measured MI-estimate of the numerator is an open problem (§ 3.4, § 3.6, § 3.7). What is comparable across classes
is the sign, not the absolute magnitude (§ 3.5).

Applying the two-stage procedure to the six paradigm cases yields sharp demarcation answers and makes explicit the structural
asymmetry: complexity is ubiquitous, closed self-payment loops are rare. Comparison with assembly theory, IIT,
teleodynamics, and the FEP positions $\eta_L$ as an operational complement to each of these programmes. Concrete
falsification conditions are formulated, tied to testable physical, informational, and evolutionary predictions.

The programme is open to refutation along eight independent lines (with a separately stated confirmation condition for the uniqueness
of the operationalisation) and is disciplined against ad hoc rescues by the requirement to name the specific failed capacity
at each instance where the value goes to zero (§ 2.6): refuting one capacity collapses both scales. This discipline limits, but does not
eliminate, the Lakatosian risk of a protective belt (§ 2.6, § 2.7). Herein lies its scientific status — not a claim to a final
definition of life, but a testable research programme with explicitly articulated limits of applicability.

*Biological implications.* The principal substantive effects of the $\eta_L$ programme lie within theoretical biology,
not at the astrobiological or AI periphery. (a) The synchronic/diachronic decomposition of vitality (§ 2.7) gives a new
formulation of the "what is an organism" question in the spirit of Pradeu (2018) and Bich and Green (2018): synchronic
$\eta_L > 0$ is a necessary condition for the individuation of the living, while diachronic Darwinian dynamics is its
complementary dimension. (b) Minimal cells (JCVI-syn3.0, Hutchison et al. 2016) and viruses acquire an
operationalisable boundary through the counterfactual ablation of § 2.2: the pair (WT *E. coli* / syn3.0) is distinguished not
by the qualitative criterion of organisational closure but by the quantitative scale of $\eta_L$ through both components (§ 4.7, § S4.7),
while viral particles fall under the reassignment of the subject to (virion + host) — a diagnosis structurally homologous to
the LLM-corp case ($B_4$, § 3.4). (c) The major transitions in evolution (§ 4.8, § S4.8 — following the hypercycle and the major transitions
of Maynard Smith and Szathmáry) are reformulated as events of reassignment of the subject of self-payment, with a thermodynamic
criterion for detecting the event. A new aggregate actor emerges with its own $I_{\text{pred}}^{\text{new}}$,
paid for by dissipation at the new level. (d) Symbiotic systems — plant–mycorrhiza (Simard et al. 1997),
coral–zooxanthellae — set up a test bed for the discipline of the conventionality of the boundary in § 2.2: whose $\eta_L$ increases under
symbiosis, how the sign depends on the choice of boundary between partners, and under what conditions the symbiotic circuit forms a
new subject of self-payment. (e) Bioelectric morphogenesis (Levin 2019) — bioelectric patterns as $M_X$
(a physical realisation of the model of morphology), paid for by ionic currents across cell membranes — gives a direct
candidate for an $\eta_L$ measurement in the morphogenetic field. The power-law dependence of the rate of evolutionary adaptation on
$\eta_L$ (Prediction 1, § 5) is testable on a single microbial lineage in ordinary experimental evolution, requiring no
astrobiological or AI context, and constitutes the central empirical prediction of the programme for
theoretical biology.

*Speculative implications (astrobiology, AI ethics, demarcation).* Beyond the biological core, the programme offers a
reformulation of traditionally metaphysical questions. The search for extraterrestrial life acquires a thermodynamic
requirement of closed self-payment loops on top of existing chemical biosignatures (a complement to the Ladder of Life
Detection, not a replacement). The ethical status of artificial systems is posed as a question of the emergence of a system's own
dissipative payment for its model (alongside the traditional lines of sentience / welfare / functionalism). The boundary between
the structurally complex and the vital acquires an operational *necessary* cut: $\eta_L > 0$ is a necessary condition for
synchronic vitality (§ 2.7); the upper bound $\eta_L \le 1$ is a conditional consequence of Landauer's principle under
the truth of the stationary-accounting postulate of § 2.1, not an unconditional theorem (a proof for an arbitrary
update channel is an open problem). A full definition of life in the sense of the NASA formula (Joyce 1994) also requires
Darwinian dynamics at the population level, and both dimensions — synchronic and diachronic — are
mutually complementary. None of these reformulations is an automatic solution to the corresponding question;
each is a pointer to a specific measurable quantity with respect to which the question can be formulated
in a disciplined way.

For theoretical biology, $\eta_L$ opens a quantitative bridge between the tradition of organisational closure
(autopoiesis, (M,R)-systems) and predictive models of adaptation.

## Author Contributions

Conceptualisation, methodology, formal analysis, writing — preparation of the original draft, writing —
review and editing: A.A. The author has read and agreed to the published version of the manuscript.

## Funding

The research received no external funding.

## Ethics declarations

Ethical approval, consent to participate, and consent to publish are not applicable: the present work is a
theoretical study with numerical simulations that did not involve humans, animals, biological material, or
related data as subjects.

## Data availability

No primary empirical data were generated for this work. The reproducible code of the worked examples (§§ 3.4–3.7, 4.4: *E. coli* chemotaxis, a bimetallic thermostat, the Singapore/Detroit city pair, the biosphere-as-compressor, and the LLM-as-corporation in `worked-example/`) is openly available in the GitHub repository `andriishin/landauer-self-modeling-oa` (https://github.com/andriishin/landauer-self-modeling-oa) and is archived on Zenodo together with a preprint of this manuscript (DOI: 10.5281/zenodo.20262946).

## Use of AI Tools

In accordance with the Springer Nature editorial policy on AI tools in scholarly writing, AI is not listed as a co-author and the author retains full responsibility for all content of the manuscript. In preparing the present manuscript and supporting materials, the author used Anthropic Claude (Opus 4.6, 4.7, 4.8) for five tasks. (i) Generation and verification of reproducible Python code for the worked examples in `worked-example/` (§§ 3.4–3.7, 4.4). (ii) Cross-checking bibliographic metadata against local copies of the cited sources. (iii) Editorial revision of human-generated text at the level of readability, grammar, and style (copy-editing); per the Springer Nature guidance, such use does not require a separate declaration but is stated here for full transparency. (iv) Translation of the manuscript and supporting materials (including the `worked-example/` READMEs) from the Russian primary source into English — the journal's submission language — with subsequent terminological and stylistic revision; the author checked the translation and bears full responsibility for it. (v) Assistance with the derivation and verification of the formal apparatus (the proof of the stationary-erasure lemma and the $\eta_L \le 1$ bound) under the author's direction; the author independently checked all proofs and bears full responsibility for them. All scientific statements — the formulation of $\eta_L$, the self-payment requirement, the paradigm-case diagnoses, and the falsification criteria — were conceived by the author; their formal write-up was carried out with AI assistance under the author's control. The AI tools did not autonomously generate scientific content. The author checked every AI-assisted fragment and accepts full responsibility for the content of the manuscript and supporting materials.

## Competing interests

The author declares the absence of any relevant financial or non-financial interests that could be
perceived as influencing the content of this article (over the three years prior to manuscript submission).

## References

The reference list is generated automatically from `paper/refs.bib` at LaTeX compile time using a
Springer **Author-Year** bibliography processor (`sn-mathphys-ay.bst` or the journal-specific
Author-Year style — verify at submission). In-text citations follow the name-and-year convention
(`Author Year`; `Author and Coauthor Year`; `Author et al. Year`), and the reference list is ordered
**alphabetically by the first author's surname**, as required by *Theory in Biosciences* submission
guidelines (`docs/biosciences-requirements.md` § 8).
