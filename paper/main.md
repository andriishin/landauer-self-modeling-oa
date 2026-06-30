<!--
  English translation of the article. Russian source — main.ru.md.
-->

# Vitality as the Efficiency of Self-Paid Self-Modeling

**Authors:** Alexander Andriishin ¹\*

¹ Independent Researcher, Moscow, Russia. ORCID: 0009-0000-4739-4017 (https://orcid.org/0009-0000-4739-4017)
\* Correspondence: alexander@andriishin.com

## Abstract

Complexity is ubiquitous, the living rare: stars, hurricanes, crystals, and language models are richly
structured, far from equilibrium, yet none pays, through its own dissipation, for its world-model.
Closed *self-payment* separates the vital from the merely complex; here we propose its quantitative
operationalization. Vitality requires two conditions: the predictive efficiency of self-modeling — the
fraction of retained environmental memory still predicting the future — and self-payment, whereby holding
obsolete memory carries a thermodynamic cost, so a corrupted model returns as the
system's own decay.
Requiring the model and its paying dissipation to share one physical boundary distinguishes the scale from
established programs — assembly theory, integrated information, teleodynamics, the free energy principle —
each taking one axis seriously, none demanding this identity of boundaries. A two-stage
procedure — structural screening by a triad of invariants, then vitality verification — covers six paradigm
cases from star to metropolis, with the biosphere as a control limit and a reproducible *Escherichia coli*
chemotaxis computation. The picture is asymmetric: structural potential is nearly universal, closed
self-payment loops rare. Consequences follow: extraterrestrial-life searches must detect such loops atop
chemical biosignatures; artificial systems' ethical status turns on when one begins paying for its model;
the complex–vital boundary falls at positive efficiency under a closed loop. Developed for the stationary
regime, it generalizes to non-stationary dynamics in companion work (Andriishin 2026). It is open to refutation along several independent lines, including a predicted power-law dependence
of evolutionary-adaptation rate on self-modeling efficiency.

## Keywords

definition of life; vitality; self-payment; nostalgia; predictive information; thermodynamics of computation

## 1. Introduction

The concept of a "living organism" has, in contemporary biology, no generally accepted formal definition. Historically it
rested on a cellular substrate — carbon chemistry, membrane organization, metabolic closure — but its
boundaries are blurred both from below and from above. From below: viruses lack autonomous metabolism, yet they participate in
evolutionary dynamics (Pradeu 2018); prions and replicator RNA systems reproduce without cellular
infrastructure; protocellular and abiogenetic transitional forms make it impossible to draw a sharp boundary between
chemistry and biology (Plante 2025). From above: biospheres, symbiotic communities, and anthropogenic megastructures
display marks of collective auto-regulation and evolutionary adaptation without any single cellular
referent (Mossio et al. 2016). In response to these difficulties, the philosophy of biology of the last two decades
has developed a robust **epistemological pluralism**:

- registries of a hundred or more competing definitions of life with no signs of convergence (Trifonov 2011);
- the argument for the need of a "theory of life" instead of a dictionary definition (Cleland 2019);
- the anti-definitionist line of "life-as-historical-lineage": life as a single monophyletic branch from LUCA, rather than a list of marks (Mariscal and Doolittle 2020);
- the conception of the organism as a biologically individuated system (Bich and Green 2018; Pradeu 2018).

No definition gains
unanimous acceptance; there is a growing demand for operational criteria capable of applying to nonstandard
candidates — astrobiological findings, artificial systems of complex information processing traditionally
called cognitive, and hybrid ecological complexes (Chirumbolo and Vella 2026).

The present work proposes for this role an operational measure — the dimensionless predictive efficiency of
self-modeling $\eta_v = I_{\text{pred}}/I_{\text{mem}}$, and a vitality verdict as the pair $(S, \eta_v)$ of
the self-payment predicate $S$ and positive efficiency $\eta_v > 0$. Before unfolding this construction (§ 2),
we outline the landscape of programs against which it is built.

Vitality is formalized by a line of technical programs, each taking up one of its sides: the thermodynamic ("life
feeds on negentropy", Schrödinger 1944), the Bayesian (FEP: Friston 2005, 2010), the combinatorial complexity of assembly
(assembly theory: Marshall et al. 2017; Sharma et al. 2023), the causal closure of information ($\Phi$: Tononi
2004; Tononi et al. 2016), the self-emergence of norms (teleodynamics: Deacon 2011), the scale of goal-like behavior
(cognitive light cone: Levin 2019). These are not mutually exclusive hypotheses: each loses discriminating power at
the boundaries — FEP applies to a household thermostat (Baltieri and Buckley 2019) and to a Watt governor (Bruineberg et al.
2022), while the narrow NASA definition (Joyce 1994; Cleland and Chyba 2002) is silent about substrate commonality (a detailed
comparison — § 4). Hence the bridge to our measure: to join the thermodynamic payment and the quality of the retained model
into a single dimensionless scale.

The parallel **origin-of-life** program — the hypercycle (Eigen 1971; Eigen and Schuster 1979), autocatalytic
sets and RAF networks (Hordijk and Steel 2004; Hordijk 2019), dissipative adaptation (Perunov, Marsland, and England
2016), major transitions (Maynard Smith and Szathmáry 1995), geochemical scenarios (Pross 2012; Smith and
Morowitz 2016; Kauffman 2019) — operationalizes the abiotic→biotic transition as a self-sustaining
informational-energetic loop over a geochemical flux; $\eta_v$ does the same in the thermodynamic register,
where the positivity of $\eta_v$ is a necessary condition for the moment of the origin of life (§ 4.8; § 6).

The same limits appear in astrobiology: biosignatures based on disequilibrium ($\text{O}_2$/$\text{CH}_4$), isotopes
($\delta^{13}\text{C}$), and chirality have abiotic alternatives, and the debates over the arsenate claim for strain GFAJ-1
(*Halomonadaceae*) (Wolfe-Simon et al. 2011 [retracted by *Science* 2025]; Reaves et al. 2012), over methane on Mars
(Webster et al. 2018; Korablev et al. 2019), and over phosphine on Venus (Greaves et al. 2021; Villanueva et al. 2021), absent a
vitality criterion, reduce to the interpretation of particular proxies — just as the dispute over the vitality of language models does.

From another side, the same question is approached by AI alignment: under what architectural conditions an optimizing agent
begins to optimize its own continuation (Bostrom 2014; Hubinger et al. 2019; Carlsmith 2022). The object is
overlapping, the angles different: AI safety describes the behavioral marks of the loop, whereas $\eta_v$ and the predicate $S$ describe its
thermodynamic co-characteristic (a structural parallel, not a causal-generative connection; § 3.4).

The present work defines vitality as the efficiency of retaining one's own model by one's own dissipation.

*Self-modeling* is used here in a sense distinct from the phenomenal self-model of Metzinger (Metzinger 2003): it denotes the structural condition under which the model of the environment, the dissipation that pays for it, and the carrier that suffers from its errors belong to one physical system — the "self" is the carrier of the model and of its price, not the content of the model. Likewise, *vitality* here is a strictly operational informational-thermodynamic property (the predictive efficiency of self-modeling $\eta_v$), not the *vis vitalis* of the vitalist tradition.

The central object is the dimensionless ratio

$$\eta_v = \frac{I_{\text{pred}}}{I_{\text{mem}}} \in [0, 1],$$

where $I_{\text{pred}}$ is the predictive information about the future of one's own environment, retained by the internal structure of the
system, and $I_{\text{mem}}$ is the total information of that same structure about the past and current trajectory of the environment (precise
definitions and the link to the classical formulation of Bialek–Nemenman–Tishby (Bialek et al. 2001) — § 2.1).
The ratio $\eta_v$ is the fraction of retained memory that is still predictive; the complementary fraction
$\nu = 1 - \eta_v$ is *informational nostalgia*, the ballast of outdated memory. The bound $\eta_v \in [0, 1]$ for
**passive** self-modeling is a consequence of the data processing inequality (DPI), not an energetic normalization
and not a convention about scale (the active case is an open item, § 2.1). Thermodynamics enters as a **separate anchor**: by the thermodynamics of prediction (Still et al. 2012, § 2.2)
retaining non-predictive memory commits the system to a dissipation of no less than $k_B T$ per such bit — here
and only here does the Landauer scale $k_B T \ln 2$ appear, as the coefficient of a strict bound rather than as an exchange
rate of energy for bits. Vitality is a pair of conditions: positive efficiency $\eta_v > 0$ **together with** a closed
self-payment loop (§ 2.7).

The program unfolds in three constructive steps. The first is the operational definition of the vital scale as $\eta_v = I_{\text{pred}}/I_{\text{mem}}$ (the freshness
of the retained model), explicitly distinguished both from indices of complexity (assembly index, $\Phi$, $I_v$ as a composite of three
capacities) and from the self-payment predicate $S$: a positive $\eta_v$ is possible even for a system without its own payment (as for a
language model), but vitality requires the conjunction of $\eta_v > 0$ and $S = 1$.
The second is the separation of two methodological levels: structural screening through the composite $I_v = \sqrt[3]{T_v C_v S_v}$ (the thermodynamic $T_v$, the informational $C_v$,
and the topological $S_v$ capacities; § 2.3)
and vital verification through $\eta_v$ (a computational economy, not a logical strengthening). The third is the explicit
conventionality of the system boundary as a methodological instrument: $\eta_v$ depends on the choice of boundary, and this
dependence is productive — it allows one to distinguish "the vitality of an LLM as an agent" (equal to zero) from "the vitality of a corporation"
(distinct from zero, but referring to a different object).

The novelty lies not in the separate components. Predictive information (Bialek et al. 2001) and the Landauer limit (Landauer 1961)
have been known for more than half a century. Self-modeling goes back to Rosen's anticipatory systems (Rosen 1985); the requirement of one's own
payment for the model converges with Taleb's skin-in-the-game (Taleb 2018) and Maturana–Varela autopoiesis (Maturana and Varela 1980). The novelty lies
in the architecture of their joining along three points. The specific ratio $I_{\text{pred}}/I_{\text{mem}}$, to the best of
our knowledge, has not been used as a measure of vitality in the Bialek–Nemenman–Tishby line. The requirement that the model
and the dissipation that pays for it belong to one physical boundary (self-payment), with a closed error-return
loop, in explicit form as a criterion of vitality, has, to the best of our knowledge, not previously been formalized — and neither Landauer
nor Bialek worked with it. The interpretation
of the resulting ratio as a vital scale is an independent step that none of the source frameworks took.

The nearest contemporary line — the thermodynamics of prediction and learning — needs to be set apart separately, since
it operates with kindred quantities. Goldt and Seifert (Goldt and Seifert 2017) formalize the thermodynamics of
learning a rule in a neural network, introducing a learning efficiency as the ratio of acquired information to its
thermodynamic cost, bounded by unity; Takahashi and Hayashi (Takahashi and Hayashi 2026) develop a
yield of acquiring structural information about the environment ($\eta_E$, bits-per-joule) and a requirement of boundary closure —
payment for the low-entropy resource crossing the system boundary. Both works share with the present one a common foundation
(Landauer 1961; Still et al. 2012; Goldt and Seifert 2017), and therefore the demarcation is conducted not on the foundation, but on
subject, dimension, and interpretation, and the lines are complementary rather than competing. Dimension: their $\eta_E$ is
bits-per-joule about the *environment*, the efficiency of acquiring external structure; $\eta_v = I_{\text{pred}}/I_{\text{mem}}$
is dimensionless, that is: the fraction of the retained *self-model* still remaining predictive — a measure of retention and
obsolescence (nostalgia), not of acquisition. The status of self-payment: their boundary closure is a convention of accounting
in the choice of boundary, whereas the predicate $S$ (the co-location of the model, of the dissipation that pays for it, and of the error-return
loop; § 2.7) is a constitutive criterion of vitality with an independent thermodynamic support on the Still bound.
Finally, the bound $\eta_v \in [0, 1]$ follows from the data processing inequality, not from a stochastic-thermodynamic
bits-per-joule balance, and the thermodynamics of learning offers no vital interpretation of the pair $(S, \eta_v)$.

The proposed definition is not a metaphysical declaration. $\eta_v$ is an operational representation of vitality as a
mode of existence, not its definition in essence. The standard philosophical distinction between the referent of a theory
(a property of the system) and an operationalization (a relation between the system and the measuring frame) is analogous to the distinction
"temperature as a measure of thermal energy" versus "the logarithm of the expansion of mercury by 100 graduations", or "the strength of an earthquake" versus
"the Richter scale". $\eta_v$ is an operational measure, disciplined by a concrete definition.

The present work deliberately restricts itself to the **stationary regime**, where the assumption of finite memory and ergodicity of the
environment stabilizes the volume of retained memory and makes informational nostalgia stationary. In this regime the formalism
yields sharp demarcation answers and testable predictions. The nonstationary regime — growing memory, a drifting
environment, a cumulative budget — lies beyond the scope of this work and is developed in the companion work (Andriishin 2026).
There, Lemma 2 is proved on the inevitability of informational nostalgia in the OU class (Ornstein–Uhlenbeck) of slow drift under the technical conditions
listed there. A conjecture is also formulated about the adiabatic asymptotics of
$\dot{\eta_v}^{\text{excess}}$ for systems without periodic memory reset.
The applicability of the apparatus of the present work is limited to systems with an ergodic environment and finite memory; for biospheres
on eonic windows, AI systems learning under drift, and civilizations with a growing archive — consult the
nonstationary extension.

The structure of the paper: § 2 unfolds the formal framework; § 3 applies the procedure to six paradigm-case systems (diagnostic test cases, each isolating one load-bearing condition); § 4
compares with neighboring programs (assembly theory, IIT, teleodynamics, FEP) and positions it relative to the
lines of organisational closure, the origin of life, and contemporary demarcation debates; § 5 formulates
the falsification conditions; § 6 discusses the consequences for astrobiology, AI ethics, and complex systems; § 7 sums up.

## 2. Theoretical Framework

### 2.1 The Central Quantity: Predictive Efficiency of Self-Modeling

A living system holds in its internal structure an implicit model of its environment. Part of what is memorized still predicts
the environment's future — it is useful; the remainder is a trace of a past from which the environment has already moved on — ballast. Vitality
is measured by **what fraction of the retained memory remains predictive**: the higher the fraction, the more "alive" the loop
of self-modeling, whereas pure ballast without prediction is no longer a working model.

The formalization of this intuition rests on two information quantities. Let $M_t$ be the configuration of those internal
degrees of freedom of the system $X$ at time $t$ that pass counterfactual ablation (§ 2.2) as belonging to the
modeling loop (a functional channel, not the full internal configuration — for a bacterium this is the methylation pattern
of the Tar receptors, not all $\sim 10^{10}$ degrees of freedom of the cell), and let $X_E$ be the signal of its environment. In the spirit of
Still, Sivak, Bell, and Crooks (2012) we introduce

$$I_{\text{mem}}(t) := I\!\left(M_t;\; X_E^{\le t}\right), \qquad
  I_{\text{pred}}(t,\tau) := I\!\left(M_t;\; X_E^{[t,\,t+\tau]}\right). \tag{1a}$$

Here $I_{\text{mem}}$ is **memory**: how much the internal state knows about the past and current trajectory of the environment (and this
memory is rightly called a *model*, rather than a raw correlation, only when $M_t$ is a minimally sufficient statistic
of the past for predicting the future — the model-hood criterion: § 2.3);
$I_{\text{pred}}$ is **predictiveness**: what part of this knowledge pertains to the environment's future over the horizon $\tau$. The narrow
proxy operator $M_t$ is a functional channel, not the full mutual information $I(X; X_E)$ over all
degrees of freedom: the latter would be many orders of magnitude larger owing to **nonfunctional couplings** with the environment
(heat exchange, mechanical contact, diffusion) that statistically bind $X$ and $X_E$ but carry no
predictive information about its future behavior. The predictive component also differs from the classical
predictive information of Bialek–Nemenman–Tishby (Bialek et al. 2001), defined as the mutual information between the
past and the future of a single process, $I(X_E^{[t-\tau,\,t]};\, X_E^{[t,\,t+\tau]})$; the relation between them is given by the
data processing inequality (see below) and is discussed further as a bridge to the Bialek framework.

The central quantity of the article — the **predictive efficiency of self-modeling** — is defined as the ratio of
these two quantities:

$$\eta_v(t,\tau) := \frac{I_{\text{pred}}(t,\tau)}{I_{\text{mem}}(t)} = 1 - \nu(t,\tau), \qquad
  \nu(t,\tau) := \frac{I_{\text{mem}}(t) - I_{\text{pred}}(t,\tau)}{I_{\text{mem}}(t)}, \tag{1}$$

where $\nu$ is **informational nostalgia**, the fraction of retained memory that has ceased to be predictive. *That is:*
$\eta_v$ is not "bits of prediction per joule," but the fraction of what the system remembers that actually pertains to the future;
$\nu$ is its complementary fraction of pure ballast.

The bound on this quantity is a theorem, not a normalization convention. Memory is formed from the past with internal noise,
$M_t = f(X_E^{\le t}, \zeta_v)$, where the noise carries no information about the environment's future beyond what is already contained in the
past: $\zeta_v \perp X_E^{[t,\,t+\tau]} \mid X_E^{\le t}$ (it is precisely this conditional independence, and not the stronger
requirement of "no feedback," that is the exact premise needed; disentangling these two conditions — supplementary
§ S2.1). Then the chain $M_t \to X_E^{\le t} \to X_E^{[t,\,t+\tau]}$ is Markov, and by the data processing inequality
(DPI; information about a random variable does not increase under deterministic processing)
$I_{\text{pred}} \le I_{\text{mem}}$. Hence

$$\eta_v \in [0, 1], \qquad \nu \in [0, 1] \qquad \text{— by construction (DPI).}$$

*That is:* the $[0, 1]$ normalization is a consequence of an information inequality.

The bound $\eta_v \le 1$ is derived for **passive** self-modeling, in which the Markov property of the chain
$M_t \to X_E^{\le t} \to X_E^{[t,\,t+\tau]}$ holds. The active case (freely-swimming *E. coli*; active-inference agents, § 7),
in which $M_t$ causally drives the environment's future through action and thereby breaks the DPI chain, remains
**an open item**: conditioning on a fixed policy does not restore the Markov property (the action $a = \pi(M_t)$
makes $M_t$ dependent on the environment's future), and the bound requires a transition to **directed** (transfer) information
$T_{M \to X_E}$ — how much the model's own state $M$ causally contributes to the environment's future beyond its past —
a feedback generalization via the Sagawa–Ueda bound (2010); the setup — § 2.7 below.

*Interventional (do) legitimacy of the passive measurement.* The openness of the active case does not render the
operational measurement of $\eta_v$ meaningless: the immobilized protocol of § 3 fixes not a "simplified" but a strictly defined
quantity, because it realizes a **do-intervention** in Pearl's sense (Pearl 2009). The exogenous clamping of the action
$\mathrm{do}(a)$ — a controlled perturbation that fixes $a$ by an external hand — severs the causal arrow
$M_t \to a \to X_E$ and restores the Markov property $M_t \to X_E^{\le t} \to X_E^{[t,\,t+\tau]}$; by the DPI

$$\eta_v^{\mathrm{do}} := \frac{I\!\left(M_t;\; X_E^{[t,\,t+\tau]} \,\middle|\, \mathrm{do}(a)\right)}{I_{\text{mem}}}
  \in [0, 1]. \tag{1b}$$

*That is:* under an intervention that clamps the action exogenously (and **not** conditioning on the observed policy — these are
different operations: passive conditioning leaves the path $X_E^{\text{past}} \to M_t \to a \to X_E^{\text{fut}}$
open, whereas $\mathrm{do}(a)$ cuts the arrow entering $a$ from $M_t$), the loop is passive again and the ratio
lies correctly in $[0, 1]$. The denominator meanwhile remains the observational $I_{\text{mem}}$, not an interventional one: the
clamp $\mathrm{do}(a)$ in the present and future does not change the **already-formed** correlation of $M_t$ with the environment's past
(the past segment $X_E^{\le t}$ on which $I_{\text{mem}}$ is evaluated is formed **before** the clamp),
so $I\!\left(M_t;\, X_E^{\le t}\,\middle|\,\mathrm{do}(a)\right) = I_{\text{mem}}$, and the DPI under intervention closes
$\eta_v^{\mathrm{do}} \le 1$ with numerator and denominator in **one** interventional regime (the immobilized
protocol of § 3 fixes both). For *E. coli* the physical realization of $\mathrm{do}(a)$ is **immobilization**: a
cell pinned to a substrate does not swim, its state does not move the ligand concentration, and the arrow $M \to a \to X_E$ is
severed. The immobilized FRET protocol of Sourjik–Berg (§ 3) is therefore **not a simplification but an operational realization** of
$\mathrm{do}(a)$, making $\eta_v$ a proper $[0, 1]$ quantity; a freely-swimming cell measures a different, active
quantity, not bounded by unity. At the same time, $\eta_v^{\mathrm{do}}$ is **not a new theorem**, but a standard
do-reduction of the active loop to a passive one, fixing only the precise sense of the legitimacy of the passive measurement. One must
not conflate $\eta_v^{\mathrm{do}}$ with the thermodynamic efficiencies of the same feedback literature: a feedback efficiency bounded
by unity does exist — the thermodynamic $\eta_X = \dot I/\dot S_r^X \le 1$ (Horowitz and Esposito 2014,
eq. (18)) and the sensory capacity $C = \dot I/T_{y\to x} \in [0, 1]$ (Hartich, Barato, and Seifert 2016), with definitions in § 2.7 —
but this is a **thermodynamic/sensory** quantity (information flow against entropy production, sensor precision),
**not** the predictive freshness $\eta_v$; they cannot be identified.

*Reconciliation of $S$ and $\mathrm{do}(a)$.* The clamp $\mathrm{do}(a)$, which suspends the **action branch** of the error-return loop (ii) for the
duration of the $\eta_v^{\mathrm{do}}$ measurement, does not conflict with the assignment $S = 1$. The self-payment predicate $S$ requires that the information retained by the
model and the dissipation that pays for retaining it belong to one physical boundary of the system — self-feeding
(condition (i)) and the return of model error into its own loop (condition (ii)); the full definition — § 2.7. This is a
**dispositional** predicate of the *native* (freely-swimming) organism, established by a **separate** intervention —
counterfactual ablation (§ 2.2) — and not by the do-clamp. The loop (ii) has **two branches** — the action channel (sensorimotor
error return) and the dissipative Still branch; $\mathrm{do}(a)$ suspends **only the action branch** for the duration of the evaluation of
$\eta_v^{\mathrm{do}}$ and does not cancel the dispositional $S$; that is, $S$ and $\eta_v^{\mathrm{do}}$ assess one
system by **different** protocols, and the apparent conflict "with $a$ clamped, how is $S = 1$ asserted?" does not arise — the verdict
$V(X) := S \wedge (\eta_v > 0)$ joins two different functions of the system, measured by two different interventions. For the
immobilized preparation the **dissipative branch (ii) remains active** and holds $S = 1$: instantiated not through the
severed action channel but through the **dissipative mechanism** of Still — distortion of the model → growth of the nonpredictive correlation $I_{\text{nonpred}}$ → a larger
Still tax, paid by the cell's **own ATP** (condition (ii) of § 2.7 already admits "growth of obligatory
dissipation **or** disintegration of $X$").

Before binding $\eta_v$ to a fixed horizon, we introduce the system's characteristic window. The horizon
$\tau_d := I_{\text{pred}}/\dot I_{\text{pred}}$ is the memory turnover time, the ratio of the stock of predictive information
to the rate of its arrival; it is defined for **non-Markov** (memory-bearing) environments. For Markov environments
$\dot I_{\text{pred}} = 0$ (the horizon adds no predictive information beyond a single step), and the characteristic
horizon is set by the environment correlation time $\tau_E$. The empirical windows — the adaptation time of the signaling loop (seconds to minutes, within the life of a single cell) for a
bacterium, a year for a city, the response time of a biogeochemical cycle (a year to a decade) for the biosphere — are
methodological proxies for $\tau_d$, whose consistency with the theoretical horizon is a separate calibration
question (§ 3.5). Henceforth everywhere $\eta_v := \eta_v(t, \tau_d)$.

The quantity $\eta_v$ has the status of a **within-class grade** of the freshness of the self-model — it measures how outdated the
model of a given system is — **and not** of a cross-system absolute scale. The ratio $I_{\text{pred}}/I_{\text{mem}}$
penalizes the volume of memory, so it cannot be used to compare "a bacterium against a brain" directly: the cross-system demarcation
of (synchronic) vitality is the work of the predicate $S$ (§ 2.7): the binary test "vital or not" is performed by the predicate, while the numerical
value of $\eta_v$ within the positive region gives a comparative measure of the efficiency of model retention.
Why self-payment specifically (rather than autopoiesis, RAF, or organisational closure) serves as the membership criterion, and
why $S$ is a deliberate ontological premise rather than an arbitrary definition, is examined in § 2.7
(epistemic status): information theory is responsible only for the **efficiency** of the model and does not itself determine
**who pays** for its retention; the predicate $S$ adds precisely this physical membership criterion, with a
positive necessity argument (within-system culling of errors) and complementarity — not competition —
with the line of organisational closure.

*On the measurability of the denominator.* The denominator $I_{\text{mem}} = I(M_t; X_E^{\le t})$ is measurable from time series in the same
way as the actual dissipation $E_{\text{actual}}$ — a quantity accessible through calorimetry: for the chemotactic
loop of *E. coli* in the passive (immobilized) FRET protocol of Sourjik–Berg it depends only on the
covariances of methylation (a latent variable recovered from the FRET readout of kinase activity) and of the ligand
(microfluidics); in the Gaussian approximation of the linear model it is estimated via the logdet of these covariances (the full proof-of-measurability and worked example — § 3).

**The thermodynamic anchor (Still 2012).** Memory ballast is not free: for a system to maintain a correlation with
an already-irrelevant past, the thermostat must receive heat. Still proved the exact lower price of this ballast, and it
serves in the present framework as a **separate thermodynamic anchor**, not part of definition (1). At the memory-update step
$t \to t+1$, for the instantaneous quantities $I_{\text{mem}}^{\text{inst}} = I(M_t; X_{E,t})$ and
$I_{\text{pred}}^{\text{inst}} = I(M_t; X_{E,t+1})$, Still proves an **equality** (his equation (14)),
$\langle W_{\text{diss}}^{t\to t+1}\rangle = k_B T\,(I_{\text{mem}}^{\text{inst}} - I_{\text{pred}}^{\text{inst}})$;
for the full protocol (work and the subsequent relaxation) a nonnegative relaxation term turns it into a
**lower bound** of Still — henceforth bound (2) (his equation (18)). The Still price is reckoned step by step — each step of memory
update is paid for separately, and over a window these payments add up; therefore we distinguish the instantaneous nostalgia
$\nu^{\text{inst}}$ (the payment of a single step) from the horizon nostalgia $\nu(t,\tau)$ (the fraction of ballast over the whole window):

$$\langle W_{\text{diss}} \rangle \;\ge\; k_B T\,\big(I_{\text{mem}}^{\text{inst}} - I_{\text{pred}}^{\text{inst}}\big)
  \;=\; k_B T\,\nu^{\text{inst}}\,I_{\text{mem}}^{\text{inst}}. \tag{2}$$

*That is:* each bit of instantaneous nostalgia costs the system no less than $k_B T \ln 2$ of dissipated heat — this is the strict
thermodynamic meaning of retaining an aging model. Two caveats fix the precise status of the bound. First, (2)
carries **instantaneous** nostalgia $\nu^{\text{inst}} = 1 - I_{\text{pred}}^{\text{inst}}/I_{\text{mem}}^{\text{inst}}$
(the Still layer), not the horizon nostalgia $\nu(t,\tau)$ from (1); the cumulative dissipation over a window is the **sum** of the step-wise
contributions, and not the product $k_B T\,\nu^{\text{cum}} I_{\text{mem}}^{\text{cum}}$ (the step-wise structure of dissipation
and its relation to the horizon $\nu(t,\tau)$ — supplementary § S2.1.1). Second, $k_B T$ enters here as the **coefficient of a bound from a theorem** —
a multiplier in the inequality — and **not** as an exchange rate of energy for bits; the only legitimate appearance of the
Landauer scale $k_B T \ln 2$ is the cost of erasing one bit inside (2). This anchor clarifies the connection of vitality with irreversibility — but in a subtle sense that is easily distorted by inversion. The living apparatus is selected **toward** the Landauer limit **stepwise** (Still 2012): biomolecular machines are near-reversible per step (on the order of $20\,k_B T$ per operation — Bennett 1982), and this stepwise efficiency is a **mark** of vitality, not its negation. What is excluded is only **global** reversibility of the whole operation: the load-bearing condition (ii) of the predicate $S$ is the correction of model error, and correction (kinetic proofreading; Hopfield 1974; Ninio 1975) is thermodynamically necessarily dissipative (Bennett 1982; Landauer 1961: a perpetually-working useful machine cannot store its entire history), so a strictly reversible self-modeling loop **is unable** to correct error and therefore does not satisfy (ii) — both of its branches, "growth of obligatory dissipation" and "disintegration of $X$" (itself irreversible), trace back to one prohibition. That is, $S = 0$ here follows **by construction of the predicate**, and not from a nulled magnitude of dissipation (the informational $\eta_v$ meanwhile survives — the bound is from the DPI, not from erasure); in this limited sense vitality is plausibly **constitutively irreversible** — a thesis whose formal demonstration remains an open problem (the rigorous route and the stepwise/global distinction — supplementary § S2.1.1; the domain of definition of the $T_v$-anchor — § S5.1).

The connection of predictive information with dissipation runs through the **change in entropy and mutual information** (the Still bound (2);
the generalized Landauer principle, Sagawa 2014, P03025), and not through a conversion of free energy into bits. In definition (1)
there is no $k_B T \ln 2$ scale; the "Landauer" line appears legitimately — through bound (2), where and only where $k_B T$ enters. When
$\dot I_{\text{mem}} \to 0$ (memory is stabilized, $I_{\text{mem}} \approx \text{const}$) and under stationary drift the
nostalgia $\nu$ reaches a constant level, while the cumulative dissipation grows linearly with a positive specific
rate $\ge k_B T \varepsilon$ — the strict thermodynamic meaning of the ineliminability of drift in the stationary regime
(supplementary § S2.1.1); the non-stationary regime is examined in the companion work (Andriishin 2026).

### 2.2 The System Boundary as a Methodological Convention

The scale $\eta_v$ depends on the choice of the boundary of the measured system. This is a structural property, not a defect. For a large language
model under the strict boundary "the weights at the moment of inference" (a forward pass without state retention) two conditions fail simultaneously:
the own dissipation $E_{\text{actual}}^{\text{own}} \to 0$ (the power grid is external) and the channel of error return into the working
loop is absent. The scale $\eta_v$ under such a boundary is **undefined** through the simultaneous failure of both conditions, not
"equal to zero through the numerator" (the formal count via the capacities $T_v$, $C_v$, $S_v$ — § 2.3; the distinction between the strict and the operational
reading of $I_v^{\text{int}}$ versus $I_v^{\text{op}}$ — § 2.5). Under a boundary that includes the data center and the corporation,
$\eta_v > 0$, but the measured object is no longer the model.

The choice of boundary is methodologically disciplined. The boundary is drawn where the loop of decisions
paid for by the system's own disintegration is closed. The conceptual predecessor is Pattee's *epistemic cut* and *semantic closure*
(Pattee 1982, 2001): the boundary between the physico-dynamical level and the symbolic level, at which the
system closes within itself the processing of its own symbols. A bacterial cell is a natural boundary, since
distortion of its internal model of the gradient leads to the disintegration of precisely that cell. A city — because distortion of its model
of flows returns as a crisis to precisely that administrative unit. The identity of the question determines the boundary;
the choice of boundary sets what is measured.

The conventionality of the boundary is productive. The objection "with the right choice of boundary any system will turn out to be vital"
is parried thus: the choice of boundary is the choice of whose vitality is being measured, and widening the boundary widens the responsible
subject rather than dissolving the diagnosis.

*The boundary and the Markov blanket.* The Markov blanket of a system $X$ (Friston 2019) is a statistically separating layer of sensory and
active states. The framework's own construction of the self-payment boundary (§ 2.2) **does not inherit** the difficulties of the realist
interpretation of the Markov blanket diagnosed in BDDB-2022 (Bruineberg et al. 2022) and Aguilera et al. (2022).
The boundary in our framework is set by the **thermodynamic membership of the budget** $E_{\text{actual}}$, and not by a statistical
partitioning of the distribution along a Pearl- or Friston-blanket; it is therefore orthogonal to the Pearl/Friston-blanket dilemma. Conflating
the two notions leads to a category error in which informational separation is taken for energetic self-payment.

*Counterfactual ablation.* The discipline of the choice of boundary is operationalized by an interventional procedure in the spirit of
Pearlian causality (terminologically — counterfactual ablation in the sense of mechanistic interpretability: remove a component, measure the effect; not to be confused with Reichenbachian screening-off). For a candidate $c$ for inclusion in the boundary of $X$: $c$ is subtracted from the physical realization; if the
change in the rate of free-energy depletion $-dF_X/dt$ over a response time $< \tau_d$ is significant, $c$ belongs to the boundary.
The quantitative threshold: $c$ belongs to the boundary when $|\Delta(-dF_X/dt)| / |-dF_X/dt|_{\text{base}} \ge \delta$, where
$\delta \in [0.05,\, 0.1]$ is a methodological convention analogous to the significance threshold in regression analysis.
For systems with smoothly distributed membership (parasite–symbiont–host, corporation–employees) the procedure
returns a scale of degree of membership — the degree of membership $w_c = |\Delta(-dF_X/dt)| / \sum_i
|\Delta(-dF_{X,i}/dt)| \in [0, 1]$.

An essential caveat about *what* the intervention measures: the effect of subtracting $c$ is taken as the contribution to the **closed
corrective regulation loop** — topologically, by whether $c$ lies on the path "perturbation of the regulated
variable → corrective action" with a response within time $< \tau_d$ — and **not** as a raw energy flow in itself.
Without this refinement, a pure power source with the largest $|\Delta(-dF_X/dt)|$ (the thermostat's power grid, whose removal
nulls all dissipation) would fall **inside** the boundary; the topological distinction of the loop leaves it outside — it
*feeds* the dissipation but does not enter the loop responding to perturbation of the regulated variable (the bimetal and the relay
enter, the power grid and the heater do not).

The procedure relies on a pre-theoretic candidate boundary — a minimal initial intuition (physical connectedness,
the biological cell as a unit, an engineered assembly as a unit). Counterfactual subtraction refines the boundary by measuring the
**relative** contribution of each component to the total dissipation of the connected system; convergence to a fixed point
with respect to permutations of the subtracted elements yields a justified boundary. This is not a complete elimination of conventionality
(for systems without a natural pre-theoretic candidate — a corporation, the biosphere — the procedure remains open), but
an operational discipline of choice in most physical and biological cases.

*Boundary membership ≠ self-payment.* The two operations are separated and applied in strict order. The membership of a candidate
$c$ in the boundary is decided **solely** by $c$'s contribution to the regulation loop ($|\Delta(-dF_X/dt)| \ge \delta$ under perturbation of the
regulated variable — by breaking the loop upon subtraction of $c$, topologically, and not by raw energy flow) — prior to and
independently of the question of the payer (i); the self-payment predicate $S$ (§ 2.7) is assessed **afterward**, on the already-fixed
boundary. The order "boundary → then $S$" breaks precisely the vicious circle "the boundary is chosen so that $S$
comes out as desired": for the thermostat, ablation assigns the bimetal and the relay to the boundary (their subtraction breaks the regulation loop), and
leaves the heater and the power grid outside — and this is decided without any appeal to self-payment; only **after** fixing the
boundary does it emerge that $S = 0$, because the obligatory dissipation is borne by the grid, not the bimetal (full treatment — § 4.4). The residual
conventionality (the choice of the candidate boundary, the threshold $\delta$) is thereby retained (§ 2.7): the mechanism is disciplined,
but not eliminated.

Application to the LLM — § 3.4 and Supplementary § S3.4; to the thermostat — § 4.4 and Supplementary § S4.4.

### 2.3 The Triad of Invariants

The positivity of $\eta_v$ requires the simultaneous presence of three capacities.

*Thermodynamic capacity $T_v$* — the price of holding the model against erosion. Irreversible erasure of a bit physically costs no
less than $k_B T \ln 2$ of free energy (Landauer 1961); the exergy flux is the payment against noise. The standard proxy is the
specific exergy flux $P_D \cdot \eta_{\text{ex}}$, normalized to mass or volume; in the tradition of
Chaisson (Chaisson 2001) it is measurable from molecules to galaxies.

*Informational capacity $C_v$* — the quality of compression: the adequacy of the model to the environment and its updatability. The proxies divide into
two classes. The first — entropy-rate proxies $h_\mu$ (normalized Lempel–Ziv complexity, Bandt–Pompe permutation
entropy) — operationalizes the rate of environmental novelty, not predictive information. The second — proxies for $I_{\text{pred}}$:

- excess entropy $\mathbf{E} := \lim_{L\to\infty} I(X^{[t-L,\,t]};\, X^{[t,\,t+L]})$ — the asymptotic value of
  predictive information in the Bialek–Nemenman–Tishby formulation in the limit of infinite windows; on finite windows it is
  operationalized through block-entropy estimates $H(L)$ (Crutchfield and Feldman 2003);
- statistical complexity $C_\mu$ (Crutchfield's computational mechanics; Shalizi and Crutchfield 2001) — the entropy of the minimally sufficient
  statistic for prediction, satisfies $C_\mu \ge \mathbf{E}$ and serves as a complementary measure of structural memory;
- PCI (perturbational complexity index) of Casali (Casali et al. 2013) — an estimate of nonlinear integration on cortico-biological
  data. Adami's parallel program (Adami 2002) defines physical
complexity as the mutual information between the genome and the environment — a biologically concrete special case of the "quality of the
model of the environment," conceptually akin to $C_v$. The distinction of classes is essential for a consistent
operationalization of $\eta_v$. In the stationary regime of the present work both classes serve as proxies for one $C_v$. The identity
$\eta_v = C_v^{\text{predictive}}/C_v^{\text{static}}$ is correct only within the **second** class (computational
mechanics), where both quantities are bits of retained structure: $C_v^{\text{static}}$ is identified with the statistical
complexity $C_\mu$ (structural memory, a proxy for $I_{\text{mem}}$), and $C_v^{\text{predictive}}$ with the excess entropy
$\mathbf{E}$ (the predictive part, a proxy for $I_{\text{pred}}$). The theorem $C_\mu \ge \mathbf{E}$ then yields
$\eta_v = \mathbf{E}/C_\mu \in [0, 1]$ consistently with the DPI. The proxies of the **first** class ($h_\mu$, Lempel–Ziv) measure the
rate of environmental novelty — this is a **separate** index, not the denominator of $\eta_v$. Thereby the central quantity of § 2.1
acquires a triadic form: the predictive efficiency is the fraction of retained structural memory ($C_\mu$),
remaining predictive ($\mathbf{E}$) — $\eta_v = I_{\text{pred}}/I_{\text{mem}} = 1 - \nu =
C_v^{\text{predictive}}/C_v^{\text{static}}$; the identity is exact when $M_t$ is a causally-sufficient (minimally
sufficient) representation, and is a proxy-approximation for an arbitrary functional channel $M_t$. It is precisely this
caveat that carries the **model-hood criterion**, separating a *model* from raw memory: what is retained is a model of the environment, not an
arbitrary correlation, exactly when $M_t$ is a causally-sufficient (minimally sufficient) statistic of the past
for predicting the future, that is, when $I_{\text{mem}}$ is identifiable with $C_\mu$ (the entropy of the causal states,
Shalizi and Crutchfield 2001), rather than with the raw $I(X; X_E)$ inflated by nonfunctional couplings (§ 2.1). Then
$\eta_v = \mathbf{E}/C_\mu$ measures exactly that fraction of the minimally-sufficient memory which carries predictive structure
($\mathbf{E}$); this is the basis for calling $I_{\text{mem}}$ a **model**, rather than mere memory — and its legitimacy is the more
complete the closer the functional channel $M_t$ is to the minimally sufficient statistic. In the
non-stationary extension (Andriishin, companion work) the divergence of $C_v^{\text{static}}$ and
$C_v^{\text{predictive}}$ serves as a diagnostic signal of informational nostalgia (the full relation
$C_v^{\text{predictive}} = (1-\nu)\,C_v^{\text{static}}$ — § 6).

*Topological capacity $S_v$* — the architecture of the connectivity of the error-return loop. The standard proxies are Newman
modularity $Q$ (Newman and Girvan 2004) with the indicative threshold $Q > 0.3$ as a conditional benchmark, requiring
calibration by a null model (see below on the resolution limit, rather than a hard criterion), scale-freeness $\gamma \in [2, 3]$
for the degree distribution (Barabási and Albert 1999; Newman 2010 review; a critique of its universality in Broido and
Clauset 2019), the hierarchical clustering coefficient $C(k) \sim k^{-1}$ (Ravasz and Barabási 2003). The algebraic
connectivity $\lambda_2$ of Fiedler (1973), indexing the global diffusive connectivity, is a *secondary* proxy with an inverse
interpretation: for modular architectures $\lambda_2$ is low (Mohar 1991), so it is used as an
indicator of structural bottlenecks between modules, not as a measure co-directed with $Q$. An additional class of proxy —
structural controllability (Liu, Slotine, and Barabási 2011) — is an independent-of-modularity slice of the topology of the error-return
loop.

The efficiency of a hierarchically-modular architecture for retaining predictive information over a structured environment
is formalized through the minimum description length (Mengistu et al. 2016): the hierarchy of topology compresses the description
of the adaptive policy by an amount proportional to the depth of the environment's hierarchy. The hierarchical structure is validated through
the predictive power of the missing-links decomposition (Clauset, Moore, and Newman 2008), which empirically links the
$S_v$-proxies with the $C_v$-criteria and prevents their degeneration into a single measure. The empirical correlate is the neural
connectome (Bassett and Sporns 2017; Lynn and Bassett 2019), demonstrating hierarchically-modular organization as a
selective correlate of computational efficiency. Two extreme cases null $S_v$ constructively (§ 5, Block 1 "Direct Refutations," item 3). The Erdős–Rényi random graph — the
absence of a modular decomposition; redundant short links do not yield compression of the adaptive policy, despite
the small-world diameter (Watts and Strogatz 1998). The regular lattice — the absence of cross-scale connection, a loss
on large-scale propagation of error correction.

The empirical status of scale-free as a universal pattern is contested: on a corpus of ~1000
empirical networks a strict power law with $\gamma \in (2, 3)$, tested by the statistical methodology of Clauset et al. (2009), is confirmed in a minority of cases (Broido and Clauset 2019; Holme 2019).
The power-law distribution is one of the regimes of the required architecture, not the only one; the more general condition of the
absence of a characteristic scale and the presence of a modular-hierarchical organization is what is relevant. The $Q$ metric of Newman depends on the
algorithm (greedy Newman (2004), Louvain (Blondel et al. 2008), Leiden (Traag et al. 2019)); the resolution limit
problem (Fortunato and Barthélemy 2007) requires calibration of the threshold through a null model. In the present work $Q$ is computed by the
Leiden algorithm; the numerical calculation for the chemotactic network of *E. coli* — supplementary § S2.4 ($Q \sim 0.5$). The evolutionary origin of hierarchical modularity (introduced above through $C(k) \sim k^{-1}$ of
Ravasz–Barabási) is selection pressure for the minimization of connection length (Mengistu et al. 2016) and environmental variability
(Kashtan and Alon 2005).

The triad is not assembled from independent disciplines — it is forced by the nature of holding compression over time. Nulling any
capacity nulls vitality on any scale: without payment there is no stake — the system's own price for the quality of the
retained model, which makes its errors significant to the system itself (skin-in-the-game, § 2.7) — without quality there is no
model, without architecture there is no return loop.

### 2.4 Normalization of Capacities by a Reference Cohort

The proxies in direct form do not lie on $[0, 1]$ and are not substitutable into the composite $I_v$ without normalization. The specific exergy flux for
$T_v$ has the dimension W·kg$^{-1}$ and is unbounded above. Excess entropy and $C_\mu$ for $C_v$ are bits, unbounded
above. Newman modularity for $S_v$ lies in $[-1/2, 1]$; the Ravasz–Barabási hierarchicalness is a power-law exponent.
$\lambda_2$ for a connected graph $\in (0, n]$ (for a disconnected one $\lambda_2 = 0$); as a secondary proxy it is not used in the
makeup of the $S_v$-normalization. Without explicit normalization the formula (2b) and the caveat "$T_v, C_v, S_v \in [0, 1]$" are formally
incorrect.

In the present work, percentile normalization by a reference cohort is adopted. For each capacity a reference
cohort of systems of the same structural class is fixed; the normalized quantity is the percentile in the cohort's distribution:

$$\tilde{T}_v(X) = F_{T_v}^{\text{cohort}}\bigl(T_v(X)\bigr) \in [0, 1], \tag{2a}$$

where $F_{T_v}^{\text{cohort}}$ is the empirical distribution function of the proxy over the cohort; similarly for $\tilde{C}_v$,
$\tilde{S}_v$. The zeroth percentile is the weakest representative, the unit percentile the strongest. This is a standard device of social
indicators: the Human Development Index (United Nations Development Programme 2022) normalizes its components in the same way. The concrete cohorts for the six
paradigm cases and the handling of edge cases (the biosphere without a cohort; the crystal and the hurricane with a constructive zero) — Supplementary
§ S2.4.

The percentile procedure carries three limitations. First: the choice of cohort is a convention. At the same time, the robustness of the difference by
sign between two systems of one cohort does not depend on the choice of cohort given sufficient cohort breadth; it is precisely this
robustness by sign — the substantive claim of § 3, not the concrete numbers. Second: the procedure loses information about the
absolute values of the proxies and works only for comparison within a class. Across classes the numerical $I_v$ are directly
incomparable. Third: the procedure is inapplicable to systems without a natural cohort, where normalization by a
theoretical upper limit is required. The sigmoid alternative $\tilde{T}_v = T_v/(T_v + T_v^{\text{ref}})$ — Supplementary
§ S2.4.

Henceforth in the text $T_v, C_v, S_v$ denote the normalized quantities $\tilde T_v, \tilde C_v, \tilde S_v$, unless explicitly
stated otherwise; the tilde is dropped for readability.

### 2.5 The Composite $I_v$ as an Index of Structural Readiness

The geometric mean of the three capacities

$$I_v = \sqrt[3]{\tilde{T}_v \cdot \tilde{C}_v \cdot \tilde{S}_v} \in [0, 1] \tag{2b}$$

is defined as the structural composite. Geometric averaging is chosen for three reasons: it remains in $[0, 1]$;
it is symmetric under permutations; it vanishes when any one capacity vanishes (the dropping out of a single capacity
collapses vitality entirely). Additive averaging does not preserve this property — a sum would mask the failure. The
weights $w_T = w_C = w_S = 1$ are a convention; for unequal weights $I_v^{(w)} = (\tilde{T}_v^{w_T} \cdot \tilde{C}_v^{w_C}
\cdot \tilde{S}_v^{w_S})^{1/(w_T + w_C + w_S)}$. A sensitivity analysis with respect to the weights is not carried out,
since $I_v$ is a methodological index of structural readiness for vitality, not a standalone vitality scale:
the binary "alive or not" test is performed by $\eta_v$, not $I_v$.
A positive $I_v$ is a necessary condition for a positive $\eta_v$; it is not a sufficient one. Through standard proxies
(Lempel–Ziv, exergy, network metrics), $I_v$ yields nonzero values for any structurally complex dissipative
system — the Sun, a hurricane, a black hole, an LLM. In its positional place, $I_v$ coincides with the assembly index,
Deacon's morphodynamics, and Tononi's $\Phi$: a composite index of complexity, necessary but not sufficient.

An objection to the status of $I_v$ might be that a composite of three necessary conditions would more naturally be
interpreted as a standalone scale. However, through any reasonable set of industrial proxies $I_v$ yields stably positive
values for systems that are unmistakably non-vital. For example, the $I_v^{\text{op}}$ of the Sun is positive through any
standard proxy. The normalized Lempel–Ziv complexity of the GOES X-flux over the 11-year cycle gives $\sim 0.5$–
$0.7$ of the upper percentile of the cohort of main-sequence stars; the hierarchicality of the active-region network from
SDO/HMI (Gheibi et al. 2017) is $\sim 0.4$. The specific number depends on the dataset and cohort, but stably $\in (0.3,\, 0.7)$.
Hence $I_v$ remains in the role of a _methodological_ index; formally this is secured by a distinction between two
ways of reading it: $I_v^{\text{op}}$ (operational reading) — through standard proxies on
observational data — is nonzero for any complex dissipative system. $I_v^{\text{int}}$
(interpretive / strict reading) — with a strict check of $T_v$ as own dissipation, $C_v$ as a model of the
environment in the technical sense, $S_v$ as the architecture of a closed loop —
is zero for any non-vital system by construction. A divergence of the two readings for a particular system is a diagnostic
signal: the system is structurally complex but not vital, and the divergence points to the failing capacity.

### 2.6 The Two-Stage Procedure

Vitality is theoretically established by a single test — for the positivity of $\eta_v$. The two-stage procedure is a
methodological convenience, not a logical necessity:

1. *Screening by $I_v$.* Cheap, through standard operational proxies; it culls structurally unsuitable systems
   (the crystal — vanishing of $T_v$; thermal equilibrium — vanishing of all three capacities). A computational filter, not
   a separate test.
2. *Verification of $\eta_v$.* Expensive, requiring identification of the boundary and of the system's own self-payment
   loop; applied to candidates that have passed the screening. The only logically substantive test.

The binary nature of the sign of $\eta_v$ does not make the numerical value decorative. The objection "if the sign already
delivers the demarcation, the number is redundant — the counterfactual ablation of § 2.2 establishes the sign without a
formula" is parried by pointing to content of the magnitude that is irreducible to the sign. First, $\eta_v$ within the
positive region is a comparative metric of the efficiency of the self-payment loop: the order of magnitude of $\eta_v$ for
two systems of the same class carries content beyond the shared sign. Second, the magnitude enters the falsifiable
quantitative prediction $r_{\text{adapt}} = A \cdot \eta_v^{\alpha}$ (§ 5), which the sign does not generate: the sign fixes
neither the slope $\alpha$ nor the testable monotone dependence of the adaptation rate. The sign of $\eta_v$ separates only
the class without a model ($\eta_v = 0$); the binary demarcation of (synchronic) vitality among model-bearing systems is
carried by the predicate $S$ (§ 2.7), while the magnitude of $\eta_v$ within $S = 1$ is an intra-class metric and a risky
prediction; the latter is not derivable from the sign.

The structure of outcomes: passed both thresholds — vital (the bacterium, a forest, the brain, the biosphere, a city);
passed the screening, failed the verification — structurally rich but non-vital (the Sun, a hurricane, a black hole; the
LLM under the strict boundary "model as agent" — failure with $S = 0$); failed the screening — structurally unsuitable
(the crystal, thermal equilibrium).

Refutation of any one capacity collapses both scales simultaneously: $\eta_v$ through $I_{\text{mem}}$ or $I_{\text{pred}}$,
the predicate $S$ through failure of $T_v$/the error-return loop, $I_v$ through the geometric mean. Refutations of the two
scales are one and the same diagnostic at two levels of resolution, not independent pieces of evidence.

The two-stage architecture carries a methodological risk. The class "structurally rich but non-vital" — the Sun, a hurricane,
a crystal, an LLM, a black hole, the Belousov–Zhabotinsky reaction — risks turning into a Lakatosian protective belt: any
refuting observation is absorbed by inclusion into the class. The program fixes a minimal discipline: every vanishing of
$\eta_v$ is accompanied by an indication of the specific capacity that failed. If the class expands without a structural
explanation of each new inclusion, the program shifts from a progressive to a degenerating regime.

A possible counter-argument: the asymmetry of the two levels is an artifact of the soft proxies of $I_v$ (Lempel–Ziv,
permutation entropy). Were $C_v$ operationalized more strictly — for example, through Tononi's $\Phi$ with a filter on
predictive power relative to the system's own environment — the Sun would yield $C_v \to 0$. The answer: the matter is not
the choice of one proxy but the class of available industrial metrics. All the proxies of network science, information
theory, and non-equilibrium thermodynamics developed over the last forty years, when applied to a complex dissipative
system, yield nonzero values. A proxy that unmistakably zeroes out the $C_v$ of the Sun requires post-hoc calibration on
the vitality hypothesis itself — a circle.

### 2.7 Self-Payment and Epistemic Status

The magnitude $\eta_v$ tells how fresh the model is, but does not answer the program's central question — **who pays** for
its retention. The bimetallic strip in a thermostat also "models" temperature, but the dissipation of maintenance is paid
by the power grid; *E. coli* extracts its ATP itself. Vitality arises when a system **itself pays** the mandatory — per
Still — price of retaining its own model. This is a thermodynamic form of organisational closure (Rosen 1991; § 4.7), in
which the closure is realized by the physical loop model ↔ dissipation itself, and not by a category-theoretic abstraction.

Formally, bound (2) makes the retention of non-equilibrium predictive memory dissipatively **mandatory**:
$\langle W_{\text{diss}} \rangle \ge k_B T\,I_{\text{nonpred}}$, where $I_{\text{nonpred}} =
I_{\text{mem}}^{\text{inst}} - I_{\text{pred}}^{\text{inst}}$.
We introduce the **self-payment predicate** $S(X) \in \{0, 1\}$, carrying
error-return closure (the error-return loop, not merely "feeding"). It is essential that the boundary of the system $X$
is fixed **independently of the question of the payer (i)** — by the counterfactual ablation of § 2.2 through the
contribution to the regulation loop (a topological discrimination of the loop, not raw energy flux) — and is not chosen
so as "to make $S$ come out as desired"; this disciplines the circle "boundary ↔ self-payment", though it does not
eliminate it entirely — the choice of the candidate boundary and the criterion of membership in the regulation loop remain
conventional (§ 2.2), and this conventionality is productive: the choice of boundary is the choice of whose vitality is
being measured. At the fixed boundary, $S(X) = 1$ if and only if **both** conditions hold:

- **(i)** the mandatory dissipation of bound (2) is fueled by free energy that $X$ **itself** extracts within
  its boundary (there is no external payer);
- **(ii)** distortion of the retained model **returns** as a rise of this mandatory dissipation or as the disintegration of
  $X$ — a closed **error-return loop** (model distortion → bad action → loss of free energy by the system itself),
  operationalized by the counterfactual ablation of § 2.2.

Condition (ii) is load-bearing: it cuts off dissipative structures that merely *feed* but are not *corrected*
(the flame, the Belousov–Zhabotinsky reaction, simple autocatalysis). Vitality is defined as a **pair**:

$$V(X) \;:=\; S(X) \;\wedge\; \big(\eta_v(X) > 0\big),$$

that is, the system **retains a predictive self-model** ($\eta_v > 0$) **and pays for its maintenance itself**
($S = 1$). *That is:* $\eta_v$ answers the question "how good is the model", $S$ answers the question "does the system pay
for it itself"; the living is both. Here $\eta_v$ **grades** vitality among vital systems
(in the non-stationary case — through the dynamics of nostalgia $\nu(t)$, companion work Andriishin 2026), while $S$ carries
the **demarcation** of (synchronic) vitality (the full one — synchronic plus diachronic — being the "alive/life" convention
of § 2.7, § 4.8).

The logical status of the conjunction. The conjunct $\eta_v > 0$ carries an independent demarcation only for systems
**without a model** (the structural zero of the numerator: the Sun and the crystal are cut off before the check of $S$).
Among systems **with** a model, a closed error-return loop (ii) already presupposes nonzero predictive content, so that
$S = 1$ practically entails $\eta_v > 0$; hence here the demarcation of (synchronic) vitality is carried by $S$, while
$\eta_v$ functions as a **grade**, not as a second independent condition. The conjunction is nonetheless not empty:
$\eta_v = 0$ cuts off a class (systems without a model) inaccessible to the predicate $S$ (a system may fail **both**
axes at once — the structural zero of the numerator *and* the absence of self-payment: thus the virion-in-isolation carries
$\eta_v = 0$ and $S = 0$ as a double failure, stronger than the single-axis cases). Therefore, in the demarcation table
below, $\eta_v$ for systems with $S = 0$ **and a retained model** is marked "undefined" — as a
vitality grade it is meaningful only after passing the $S = 1$ screening, whereas as the formal ratio
$I_{\text{pred}}/I_{\text{mem}}$ it is computable everywhere $I_{\text{mem}} > 0$.

It is precisely the self-payment condition that distinguishes the present framework from Still's. In Still's, the predictor
and the dissipator may be **different** circuits (the demon and the environment being separate subsystems); here $S$
**requires their coincidence** — the dissipation mandatory per Still must be borne by the same physical boundary $X$ that
bears the model. This "beyond-Still" requirement (co-location of model ↔ dissipator) is the program's original contribution:
the co-location of model ↔ dissipator is expressed by an **explicit predicate on the dissipation of bound (2)** with the
error-return loop (ii).

*Active thermodynamic accounting of the $S$-side: a borrowed bound, not a discriminator of self-payment.* The Still anchor
(bound (2)) is derived for passive memory updating; in the active (feedback) form, where $M$ acts causally on the
environment, the active **accounting of work and dissipation** is carried by the strict inequalities of the information
thermodynamics of bipartite systems — a borrowed apparatus, not a contribution of the present work (and, as clarified
below, one that by itself does **not** discriminate self-payment). The local second law for the modeling circuit $M$
(Horowitz and Esposito 2014, eq. (11)),

$$\dot S_i^{M} = d_t S_M + \dot S_r^{M} - \dot I^{M} \ge 0,$$

*that is:* the entropy production of the circuit $M$ itself is non-negative, but its entropy balance is modified by the
**information flow** $\dot I^{M}$ — the time derivative of the **symmetric** mutual information $I(M; X_E)$
(Horowitz and Esposito 2014), a term that redistributes entropy between $M$ and the environment. This HE flow $\dot I^{M}$
**should not be identified** with the directed transfer-bound $T_{M \to X_E}$ below (Hartich–Barato–Seifert): these are
two **different** borrowed objects — the symmetric flow in the HE entropy balance versus the directed
transfer-entropy HBS on extractable work, not synonyms. Reading $\dot I^{M}$ as the active form of the "Still tax on
$I_{\text{nonpred}}$" (the non-predictive correlation now being paid for not by the impersonal non-negativity of entropy,
but by the term $\dot I^{M}$) is an **interpretive heuristic** of the present framework, not a result of HE (as is, below,
the identification $I \leftrightarrow I_{\text{pred}}$ of Sagawa–Ueda, strictly correct only in the bipartite limit of
directed information). The work extractable on the predictive side is bounded not by raw mutual information but by the
**directed** transfer-entropy (Hartich, Barato, and Seifert 2014, eq. (37)),

$$-\sigma_{M} \le T_{M \to X_E},$$

*that is:* here $\sigma_{M}$ is the entropy production of the **thermal reservoir** of the circuit $M$ (the heat dissipated
into that reservoir; $-\sigma_{M}$ is the work extracted from it, divided by $T$; in the stationary regime, $d_t S_M = 0$,
it coincides with the full subsystem production of HBS, for which $\sigma^M = \dot S_r^M + d_t S_M$), and **not** the
entropy of the environment $X_E$; and this work extracted by the dynamics of $M$ does not exceed the flow $T_{M \to X_E}$
that the own state of $M$ causally contributes to the future of the environment beyond its past. It is precisely the
**actuator** direction $M \to X_E$ that is taken, since the matter concerns the feedback regime: here $M$ causally
**drives** the future of the environment, whereas the demonic extractable work in the purely **sensory** regime (the
environment drives $M$) is conventionally bounded by the reverse flow $T_{X_E \to M}$, consistent with the sensory capacity
$C = \dot I / T_{y \to x}$ above; for the active self-paying loop the former is relevant. The full feedback floor on
dissipation is given by the generalized second law $\langle W\rangle \ge \Delta F - k_B T\,I$ (Sagawa and Ueda 2010,
eq. (3)). The conclusion is more honestly formulated thus: in the transition to the active case the **pair framework**
$(S, \eta_v)$ remains meaningful, but its load-bearing parts change status rather than being "preserved" intact.
Feedback thermodynamics (Horowitz–Esposito; Hartich–Barato–Seifert; Sagawa–Ueda) keeps the active **accounting of work and
dissipation** determinate — it gives a bound on the work extractable by the self-paying circuit in the feedback regime as
well — however, these inequalities hold for **any** bipartite system (a thermostat with $S = 0$ satisfies HE/HBS/SU exactly
as *E. coli* with $S = 1$ does) and therefore **do not discriminate self-payment**: by themselves they do not distinguish
$S = 1$ from $S = 0$. The demarcation is still carried by the predicate $S$ — the presence of a payer (i) and of the
error-return loop (ii), fixed by the counterfactual ablation (§ 2.2) — and **not** by these borrowed bounds. The magnitude
$\eta_v$ thereby **retreats** to the passively-defined $\eta_v^{\mathrm{do}}$ (under the intervention $\mathrm{do}(a)$,
§ 2.1); in the full active form its $[0, 1]$ bound is **not guaranteed** (supplementary § S2.1.1). It is therefore correct
to speak not of a "strict support" but of an active thermodynamic **accounting** (a bound on work/dissipation), borrowed
and by itself not discriminating self-payment; the novelty of the program remains in the ratio
$I_{\text{pred}}/I_{\text{mem}}$ itself and in the predicate of co-location of model ↔ dissipator, not in this
thermo-apparatus (Horowitz–Esposito; Hartich–Barato–Seifert).

The demarcation table:

| System | $\eta_v$ | $S$ | Verdict |
|---|---|---|---|
| Thermostat / bimetallic strip | undefined ($S=0$) | $0$ (the grid pays) | not vital |
| LLM (weights at inference) | undefined ($S=0$) | $0$ (external compute) | not vital |
| Sun / flame / hurricane | $= 0$ (no $I_{\text{pred}}$) | — | not vital — a stake without a model |
| BZ reaction / simple autocatalysis | undefined ($S=0$) | (i) yes, **(ii) no** | not vital — *feeds* but is not *corrected* |
| Virion (outside the host) | $= 0$ (no $I_{\text{pred}}$ / no autonomous model) | $0$ (does not pay itself) | not vital; virus + host — a reassignment of the subject |
| *E. coli* | $> 0$ ($\eta_v^{\mathrm{do}}$, § 2.1) | $1$ (its own ATP) | vital |
| Biosphere / city / corporation | $> 0$ (magnitude undefined) | $1$ (self-funded) | vital (the grade requires MI-estimation — of mutual information) |

When $I_{\text{mem}} = 0$, the convention $\eta_v := 0$ is adopted — no model, no vitality; the diagnosis of the Sun is a
**structural zero of the numerator**, not a $0/0$ indeterminacy. For grey zones (a cyborg, a managed ecosystem, a partially
subsidized firm) self-payment can be graded by the share of own maintenance
$\chi = E_{\text{maint}}^{\text{own}}/E_{\text{maint}}^{\text{total}} \in [0, 1]$ (energy for energy, without a
bit ↔ joule conversion), with a threshold $S = \mathbb{1}[\chi > \chi_0]$; the primary object, however, is the binary $S$,
while $\chi$ is its extension.

For active agents the predicate $S$ additionally accounts for the energy of **action** (the sensorimotor loop), and bound
(2) is taken in feedback form (Sagawa–Ueda 2010): for the active loop $I_{\text{pred}}$ is what the agent can
*cash out* into work (the Sagawa–Ueda gain is bounded by $k_B T\,I$ in terms of the measurement information $I$; the
identification of $I$ with $I_{\text{pred}}$ is a heuristic, strictly correct only in the bipartite limit of directed
information), while $I_{\text{nonpred}}$ is the pure nostalgia tax (Still); the error-return loop (ii) is here naturally
read as "model distortion → bad action → loss of the agent's free energy". The full formulation of the active case is a
direction of future work (the feedback generalization, Sagawa–Ueda 2010).

**Epistemic status of the section's claims.** The claims of the work differ in status: theoretical deduction from
established principles, empirical verifiability, speculative extrapolation with explicit falsification conditions. The
claim about the domain of definition $\eta_v \in [0,1]$ (§ 2.1) is a **deduction from the data processing inequality**
(DPI) for passive self-modeling; the bound $\eta_v \le 1$ is an **unconditional theorem** of an information inequality, not
a conditional consequence of Landauer's principle. The geometric averaging of capacities (§ 2.4) is a formal choice based
on symmetry and vanishing. The paradigm-case values of $\eta_v$ for the bacterium, the biosphere, and astrobiological
candidates are order-of-magnitude theoretical estimates with an explicit dependence on the window and the proxy. The city
case (§ 3.6) is a paradigm-case order-of-magnitude estimate of $\eta_v$; the structural urban metrics in the spirit of
Bettencourt et al. (2007) and the empirical calibration of $I_v$ for specific cities are the subject of separate work and
are not asserted here. The speculative consequences — the search for cosmological vitality, the moment of vitality of an
artificial system — are discussed in §§ 5–6 with explicitly formulated falsification conditions.

The load-bearing **self-payment postulate** — the model and the dissipation that pays for it belong to one physical
boundary $X$ (the predicate $S$, conditions (i)+(ii) above) — stands apart from the statuses listed: it is not a deduction
from FEP or from Landauer's principle, but an explicit ontological premise of the framework, which neither Landauer nor
Bialek made. Its epistemic status is a constructive choice; but this choice is not arbitrary and does not rest on
demarcation force alone (cf. § 4.4: self-payment offers an alternative, thermodynamic ontology that does not inherit the
difficulties of the Pearl/Friston-blanket construction diagnosed by BDDB-2022). Behind it stands a **positive necessity
argument**. A retained model culls its own errors only where the stake on its quality — skin-in-the-game
(Taleb 2018; § 1) — lies **inside** the same boundary that bears the model. If the price of retention is paid by an
external circuit ($S = 0$), distortion of the model does not return as selective pressure on the system: the error-return
loop (ii) is open, and the correction, if it happens at all, is performed by an external agent, not by $X$ itself.
Therefore self-payment is a **necessary** condition for the errors of the retained model to be culled inside the system
itself. It is precisely this that separates the three classes: "feeds-and-is-corrected" (the living),
"feeds-but-is-not-corrected" (the flame, the BZ reaction — (ii) open) and "models-but-another-pays" (the thermostat, the
LLM — (i) open). The pair of conditions is thereby **minimal**: amputating (ii) leaves a dissipative structure without
correction, amputating (i) — an externally-paid model; both yield the non-vital, so both conditions are necessary and
together minimally sufficient for the thermodynamic side of vitality. The postulate asserts nothing stronger: $V(X)$
remains a discriminator of (synchronic) vitality, compatible with anti-definitionism (§ 4.9), not a definition of life.

This same argument sets the **relation to the organisational closure line** (autopoiesis, Maturana–Varela 1980;
M,R-systems, Rosen 1991; constraint closure, Mossio–Montévil–Longo 2016; RAF, Hordijk–Steel 2004; § 4.7): all of them
point to a **qualitative** closure — the loop produces and maintains its own components or constraints — without fixing its
measurable thermodynamic condition. Self-payment does not compete with them and does not introduce "yet another
definition": it is a **complementary measurable thermodynamic cross-section** of the same closure — a **necessary**
thermodynamic condition, fixed in the physical loop model ↔ dissipation itself (the Still bound (2); the active accounting
above) — that is, a translation of their qualitative circularity into the operational predicate $S$ with an independently
fixed boundary (§ 2.2).

This postulate is the **only** load-bearing ontological premise of the $(S, \eta_v)$ demarcation: the bound $\eta_v \le 1$
follows from the DPI unconditionally (§ 2.1), without any additional premise. The independent thermodynamic mandatoriness
of retaining ballast, in turn, is secured by the Still bound (2) — a separate anchor, not a postulate.

The falsification conditions of § 5 may be realized at two levels. Methodological: the current operationalization is
untenable, a different proxy, window, or mutual-information estimation procedure is required. Ontological: the concept of
vitality through the efficiency of self-modeling is untenable in substance. The program takes the position of moderate
operationalism: any observation refuting $\eta_v$ through the failure of a particular operationalization is first
interpreted methodologically and is translated into the ontological only after the alternative operationalizations have
been exhausted.

**The asymmetry of falsification.** The program is falsified through false-negative cases (a biological system
conventionally recognized as alive for which $\eta_v = 0$ under all sanctioned operationalizations — § 5, Block 2, item 3)
and through structural failures of the progressive predictions (§ 5, Block 3, items 1–2). False-positive cases (a system
non-vital by conventional criteria with a stable $\eta_v > 0$) are formally excluded by construction: the counterfactual
ablation of § 2.2, for systems without a closed error-return loop, returns $C_v^{\text{int}}$ as undefined, and $\eta_v$ is
undefined. This asymmetry is a deliberately accepted price, narrowing the falsification surface of the program to two lines
(false-negative penetration § 5 Block 2 item 3, and failure of the progressive predictions § 5 Block 3 item 1):
$\eta_v$ is a criterion of closure of the self-payment loop, and systems without such a loop receive no positive score
**by construction**. If neither of the two lines turns out to be empirically realizable, the scale risks reducing to a
conventional redescription — this risk is acknowledged explicitly (cf. § 2.6), not masked. An alternative criterion
— for example, informational complexity per assembly theory or $\Phi$ — may assign a nonzero value to a non-vital system as
well, which reflects the different content of these programs (structural complexity versus closure of the thermodynamic
loop). Hence refutation of the $\eta_v$-program is possible only through **symmetric penetration** — the discovery of a
system, conventionally alive, for which the self-payment loop does not close (§ 5, Block 2, item 3), or through failure of
the progressive predictions on calibrated biological pairs (§ 5, Block 3, item 1).

*Heredity and major transitions: what $\eta_v$ does not close.* The $\eta_v$ scale formalizes the **synchronic** side of
vitality — the retention of one's own model over the window $\tau_d$. This is a necessary condition for every moment of the
life of a single organism. The **diachronic** side — heritability and evolvability in the sense of major transitions
(Maynard Smith and Szathmáry 1995) — lies beyond the present stationary model. The stationary regime fixes finite memory
and ergodicity of the environment (§ 2.1), which exclude population-evolutionary dynamics with drift and the accumulation
of hereditary information. The positivity of $\eta_v$ is a necessary but not sufficient condition for a full biological
"definition of life" in the sense of the NASA definition (Joyce 1994). A sterile worker bee or a mule have $\eta_v > 0$
(alive moment-to-moment) but are excluded from Darwinian dynamics at the population level. The scale is consistent with the
biological convention about their being alive and does not violate it. A full definition of life requires $\eta_v > 0$
**plus** Darwinian dynamics at the population level; these are two distinct scales — the individual synchronic and the
population diachronic — and both are necessary. The connection with the companion work (Andriishin 2026): the
non-stationary extension provides the thermodynamic apparatus on which the major-transitions program
(Maynard Smith and Szathmáry 1995) can be formulated as an open research problem (cf. § 4.8) — the joining of the two
scales is not proved either in the present work or in (Andriishin 2026), but in their combination it acquires a formal
basis.

## 3. Demarcation Tests

The two-stage procedure — structural screening by the triad of invariants (§ 2.3–2.6) and vitality
verification by the pair $(S, \eta_v)$ (§ 2.7) — is applied below to six paradigm cases ranging from a
star to a metropolis, with the biosphere as a control limit. Each paradigm case is chosen so as to fail
exactly one of the load-bearing conditions and thereby show **which** one. The load-bearing **positive**
paradigm case is biological: the bacterium *E. coli* (§ 3.5), the only example with a computed estimate of
$\eta_v$ and a verdict of $S = 1$; the astrophysical and AI paradigm cases (§ 3.1–3.4) serve as **negative
controls**, each isolating which of the two conditions of the pair $(S, \eta_v)$ fails. The vitality verdict
is formulated as a pair: $S(X) \in \{0, 1\}$ answers the question "does the system pay for the retention of
its own model itself, and does the model's error return through its own dissipation" (§ 2.7, conditions
(i)+(ii)), while $\eta_v(X) \in [0, 1]$ answers the question "what fraction of the retained memory is still
predictive." Vitality is the conjunction $S \wedge (\eta_v > 0)$. The demarcation is carried by the
**closure of the self-payment loop** $S$, not by the absolute smallness of efficiency. Taken as the predictive
fraction $\eta_v = I_{\text{pred}}/I_{\text{mem}}$, the magnitude of $\eta_v$ for most paradigm cases is
quantitatively **undetermined** and requires MI-estimation of $I_{\text{pred}}$ and $I_{\text{mem}}$ of the
corresponding loop; a computed illustrative estimate is given only by the bacterial example (§ 3.5). The
smallness of $\eta_v$ is by itself not a discriminating feature — and does **not** mean that $\eta_v$ is
large: the ballast fraction may be large, but this does not fix the magnitude of the predictive fraction.
What distinguishes the vital from the non-vital is precisely the predicate $S$. A comparative program on the
boundary of non-living/living collectives through informational architecture is developed in *Theory in
Biosciences* (Kim et al. 2021); the six paradigm cases of the present section continue that line, adding to
the informational axis of Kim–Valentini–Hanson–Walker the thermodynamic requirement of self-payment.

### 3.1 The Sun, the Neutron Star, and the Black Hole

The Sun is rich in structure — convective cells, magnetic loops, differential rotation — and passes the
structural screening on the $T_v$ side (dissipation $\sim 4 \cdot 10^{26}$ W) with room to spare. Vitality
verification, however, zeros it out through $\eta_v$: the Sun has **no model of the environment** in the
technical sense of § 2.1 — there is no functional loop $M_t$ whose state would carry mutual information about
the future of the environmental signal. At $I_{\text{mem}} = 0$, the convention of § 2.7 is adopted,
$\eta_v := 0$: no memory of the environment — hence no predictive fraction of it either. Diagnosis: a
structurally rich, non-vital system. The same applies to the neutron star, the interstellar medium, and the
supermassive black hole at the center of the Milky Way. Here $\eta_v = 0$ is a **structural zero of the
numerator** ($I_{\text{pred}} = 0$ in the absence of $I_{\text{mem}}$), not a $0/0$ indeterminacy — this is
important to distinguish from cases where it is not $\eta_v$ that is zeroed but the predicate $S$ (the LLM,
the thermostat).

The black hole yields the same negative verdict for a deeper reason: the very carrier of a model is absent.
The stationary classical horizon is described by the no-hair theorem (canonical formulations 1967–1975; the
key work Israel 1967): three parameters ($M$, $J$, $Q$) fully specify the external metric, leaving no room
for $I_{\text{pred}}$ about the environment. Quantum and non-stationary corrections — thermal radiation and
the information paradox it engenders (Hawking 1975, 1976), soft hair (Hawking et al. 2016) — reveal a richer
informational structure of the horizon, but do not restore a model of the environment in the sense of § 2.1:
the corresponding degrees of freedom do not retain $I_{\text{pred}}$ about the environment with a return of
the damage through their own dissipation. The status of the unitarity of evaporation remains open (the
information paradox: Hawking 1976 proves a *violation* of predictability, while modern resolutions — the
Page curve, the islands program — restore unitarity), but for demarcation it is inconsequential: a model of
the environment in the sense of § 2.1 is absent independently of its resolution.
The accretion disk around Sgr A* ($M \sim 4 \cdot 10^6 M_\odot$) yields the same diagnosis: the environmental
variables do not return as damage through a causal channel to the disk plasma. For all these systems
$\eta_v = 0$ structurally (no $I_{\text{mem}}$, no $I_{\text{pred}}$); the question of $S$ does not even
arise — there is nothing to self-pay for.

### 3.2 The Hurricane, the Flame, and Autocatalytic Oscillators

A hurricane and a candle flame dissipate free energy — $\sim 10^{15}$ W for an average hurricane,
$\sim 10^2$ W for a candle flame — and pass the $T_v$ screening. But they have no internal model of the
environment paid for by this dissipation: the dissipation of exergy is not accompanied by retention of
$I_{\text{pred}}$, so $\eta_v = 0$ through the numerator ($I_{\text{mem}} = 0$, no functional loop $M_t$).
The diagnosis is a **stake without a model**: the system pays but does not model. In this, the flame and the
hurricane are the mirror case of the LLM, for which the ratio is the reverse (§ 3.4): there is a model there,
but no own payment.

The Belousov–Zhabotinsky reaction and simple autocatalysis are a subtler case, and it is precisely on it
that the load-bearing **condition (ii)** of the predicate $S$ operates (§ 2.7). The BZ reaction oscillates
stably and for a long time, feeding on supplied free energy — that is, it formally satisfies condition (i)
of self-payment. But its oscillations **do not form a correction loop**: there is no channel in which a
distortion of the retained pattern would return as a growth of obligatory dissipation or as a breakdown of
the system. The error-return loop (ii) is not closed. The diagnosis is $S = 0$ through the failure of
condition (ii): the system **feeds but does not correct itself**, repetition without correction. This
separates dissipative structures that merely maintain themselves from those that retain and repair a model
of the environment. (Epistemically: it is premature to speak of the magnitude of $\eta_v$ here — there is no
substantive loop $M_t$ for which $I_{\text{pred}}$ would be defined; the verdict is carried by $S = 0$.)

### 3.3 The Crystal and Thermal Equilibrium

A crystal retains its structure with a relative strain $\lesssim 10^{-6}$ over times $\sim 10^9$ years — but
does not hold a **model of the environment**. Its internal configuration is homomorphic to its own lattice,
not to the future of the environmental signal: $I_{\text{mem}} \approx 0$ in the sense of § 2.1 (mutual
information between the state and the environment's trajectory, not between the state and itself). And the
crystal does not actively pay for the retention of this structure: in the strict thermodynamic sense it is
close to equilibrium relative to the lattice, the current dissipation of retention $\approx 0$. Thus the
crystal fails both axes at once — there is no model of the environment ($\eta_v := 0$ at $I_{\text{mem}} = 0$)
**and** there is no own payment for its retention ($S = 0$, there is nothing to feed). Diagnosis: structure
without a model and without payment.

Systems in full thermal equilibrium (an isolated gas, a closed black cavity) zero out everything
simultaneously — the canonical negative control point of the screening.

*Cairns-Smith and the crystal-as-replicator.* The Cairns-Smith program (1982) regarded clay crystals as
pre-RNA replicators: heritable lattice defects are passed to daughter crystals upon growth and splitting.
Upon widening the boundary to "crystal + solution phase," the counterfactual ablation of § 2.2 for
(crystal + ionic solution) yields $T_v > 0$ — the ion flux pays for the replication of defects. However, the
error-return loop remains open: an error in the replication of defects **does not return** as physical
damage to the lattice itself; there is no channel in which a distortion of the defect pattern would worsen
the thermodynamic conditions of the crystal's retention. This is a failure of condition (ii) — $S = 0$. The
diagnosis is a re-addressing of the object to (crystal + solution), analogously to the LLM-corp (§ 3.4), not
vitality of the crystal-as-object.

### 3.4 The Large Language Model

The LLM is the strongest pure case of the new demarcation: a system with a **strong predictive model and
$S = 0$**. A trained model is predictively strong — it compresses the regularities of its training
distribution and predicts the next token with a quality far surpassing chance (large $I_{\text{pred}}$); the
exact fraction $\eta_v = I_{\text{pred}}/I_{\text{mem}}$ of the retained representation, however, is not
measured and is not asserted here. What is essential for the demarcation is not the value of $\eta_v$ but the
fact that the model exists and is predictive, whereas the loop of its payment is open. This is exactly why
the LLM is the mirror of the hurricane: there, payment without a model; here, a model without own payment.

The decisive factor is the predicate $S$. Under the strict boundary "the weights at the moment of inference"
(a forward pass without saving state), the obligatory dissipation of retaining and updating the model is paid
for by the **external** power grid, not by the system itself: condition (i) of self-payment is violated. At
the same time, there is no physical channel of error return into the working loop — the output tokens do not
return as physical damage to the weights, the model's error does not deplete the carrier of $I_{\text{pred}}$:
condition (ii) is violated as well. The result: $S = 0$ with the predictive model intact. The diagnosis is a
**strong predictive model with an open payment loop**. This is a categorically different negative verdict
than that of the Sun: there the numerator is zeroed ($\eta_v = 0$, structurally no model), here it is the
predicate of self-payment, with the model intact and predictively strong.

*Widening the boundary and re-addressing the object.* Upon widening to "model + data center + corporation,"
the predicate $S$ may become positive — the corporation extracts its own free energy and bears commercial
sanctions for errors — but **the measured object becomes the corporation, not the model**. The counterfactual
ablation of § 2.2 yields here several nested boundaries: $B_1 = \{$weights$\}$ (counterfactual-degenerate, a
static object with the server off); $B_2 = \{$weights $+$ KV-cache $+$ executing server$\}$ over a session
window (the power grid is external, $S = 0$); $B_3 = B_2 + $ the training pipeline over a model-generation
window (own dissipation on the GPUs appears, but the error-return loop closes onto the corporate operators);
$B_4 = B_3 + $ the corporation as a legal entity (the full LLM-corp, $S = 1$ through self-funding, but the
subject becomes the firm). A component-by-component analysis of the candidates for inclusion is in
Supplementary § S3.4.

The structural diagnosis of the corporation does not require a numerical value of $\eta_v$ — it is carried by
the predicate $S$ (for $B_4$ — $S = 1$ with a re-addressing of the subject to the firm). A quantitative
estimate of the predictive fraction $\eta_v = I_{\text{pred}}/I_{\text{mem}}$ for the LLM or the corporation
requires MI-estimation of $I_{\text{pred}}$ and $I_{\text{mem}}$ of the corresponding loop and is left to
future work.

*An operational test for existing frontier LLMs.* The counterfactual ablation of § 2.2 yields a diagnostic
protocol for contemporary stateless LLMs (GPT-4-class, Claude, Gemini): (i) identify the power-supply
component; (ii) apply the counterfactual subtraction; (iii) check whether **the model's error returns as
physical depletion of the carrier** of $I_{\text{pred}}$ over a window $\tau_d$. For stateless LLMs the
"error → damage" loop is absent — a structural condition $S = 0$, reproducible without special equipment.

*Agentic LLM wrappers.* The wrappers of the 2023–2026 era — from Auto-GPT/AutoGen/Voyager to Claude Computer
Use, Devin, OpenAI Operator, MemGPT, and systems with persistent RAG memory — widen the boundary of the base
model and, through persistent memory, partially close the decision-making loop. But self-payment remains
open: the funding of execution, the infrastructure, the energy budget are held by the corporate substrate
from outside; the agent's errors return as reputational and commercial sanctions through the external
substrate, not as physical damage to the system itself. An intermediate case is a model with continual
fine-tuning on its own interactions, $\theta_{v,t+1} = \theta_{v,t} + f(\text{own predictions}_t,
\text{feedback}_t)$: the loop is partially closed (condition (ii) becomes partially defined), but the payment
for the update still comes from the external GPU fleet (condition (i) is violated). Contemporary systems of
2025–2026 implement various combinations, but (a) persistent state, (b) own payment, (c) a physical channel
of error return are not jointly realized — $S = 0$ with the predictive model intact. The structural barrier
is not the absence of technology but the absence of architectural pressure from the AI economy toward the
internalization of the energy budget.

Connection to the literature: mesa-optimization (Hubinger et al. 2019), power-seeking (Carlsmith 2022), goal
misgeneralization (Shah et al. 2022), specification gaming (Krakovna et al. 2020), the alignment problem (Ngo
et al. 2022). The line of instrumental convergence — the self-preservation drive (Omohundro 2008) and its
formalization in Bostrom (2014) — fixes the structural tendency of an optimizing agent to preserve its own
continuation; the predicate $S$ offers its thermodynamic co-characteristic: AI safety describes the
behavioral mark of closing the loop of optimizing one's own continuation, while $S$ is a candidate
thermodynamic co-characteristic of a related but not identical structural loop (a structural parallel, not a
causally-generative connection). **Vitality $(S, \eta_v)$ is neither a safety certificate nor an alignment
criterion:** a system non-vital by $S$ (externally funded) may be behaviorally power-seeking and dangerous,
and $S = 0$ is not a safety certificate. Along the self-preservation axis, $S$ is the thermodynamic shadow of
the same self-preservation loop (above: a candidate co-characteristic of instrumental convergence) and is
therefore **structurally positively correlated** with the core of risk; but this structural correlation is
logically independent of the behavioral prediction of danger — the pair $(S, \eta_v)$ remains a criterion of
vitality, not a criterion of alignment. A close conceptual parallel is *embedded agency* (Demski and
Garrabrant 2019): the formalization of an agent as a **part** of the environment that pays for its own
computation (embedded world-models). The pair $(S, \eta_v)$ offers a thermodynamic **necessary** condition
for a physically realized embedded world-model with its own loop, without claiming to reconstruct specific
subproblems (robust delegation, subsystem alignment) or to be a sufficient condition for alignment
properties.

*Comparison with the Sun.* For the Sun, the negative verdict follows the line "no causally-relevant
environment → no $I_{\text{mem}}$ → $\eta_v = 0$." For the LLM, it follows the line "a model exists and is
predictive, but the loop of its own dissipation does not pay for its retention and does not return the error,
hence $S = 0$." The final diagnosis is negative in both cases; the diagnostic richness of the procedure lies
in indicating **which** condition of the pair $(S, \eta_v)$ failed.

*The dynamics of the loop's emergence in AI.* The vitality of an artificial system arises with the closing of
the embedded self-payment loop — the simultaneous internalization of (a) persistent state, (b) own payment
for computation, (c) a physical channel of error return. The counterfactual ablation of § 2.2 yields a
**binary** answer at the level of the definition: either $S = 1$ or not; there are no intermediate states at
the level of the definition. At the level of measurement, for systems that have passed the screening with
$S = 1$, $\eta_v > 0$ becomes a measurable continuous quantity (depending on $I_{\text{pred}}$ and
$I_{\text{mem}}$ — both via MI-estimation). An operational proxy of proximity to the threshold is the
fraction of own dissipation $f = E_{\text{actual}}^{\text{own}}/E_{\text{actual}}^{\text{total}}$ (energy per
energy, without conversion of bit ↔ joule). The detection scheme requires a population of $\sim 10^2$–$10^3$
autonomous embodied agents with their own energy budget, physical wear as a channel of error return, a
control group, and a measurement of $f$ with a verification of the counterfactual ablation on each unit. The
numerical threshold is Prediction 3 in § 5.

### 3.5 The Bacterium — A Worked Example

The bacterial cell passes **both** axes. The chemotaxis of *E. coli* — the classic observation of biased
random walks (Berg and Brown 1972) — realizes the canonical model object of a closed error-return loop. The
picture of methylation of the chemotactic receptors is physically realized in the internal degrees of freedom
of the cell (Tu et al. 2008; Shimizu et al. 2010), is homomorphic to the gradient along the relevant
environmental variables, and generates chemotactic movements verifiable against the real distribution of the
carbon source. Relevance is set by **causal damage**: a distortion of methylation leads to poor chemotaxis
and a metabolic loss. Therefore here $S = 1$ — the cell extracts its own ATP (condition (i)) and the
error-return loop is closed: distortion of the model → poor chemotaxis → loss of free energy by the cell
itself (condition (ii)).

*Estimate of $\eta_v = I_{\text{pred}}/I_{\text{mem}}$.* For the bacterium, $\eta_v$ is the predictive
**fraction** of the adaptive memory of methylation — a quantity of order $O(0.1)$, the only paradigm case
where it is computed as an illustration. The estimate is obtained from a minimal **linear adaptive model** of
chemotaxis in the passive (immobilized) FRET protocol of Sourjik–Berg / Cluzel: the ligand $s_t$ as an AR(1)
process with correlation time $\tau_E$, the methylation $m_t = \sum_{j \ge 1} w_j s_{t-j} + \text{noise}$ with
leaky weights $w_j = (1-\beta_v)\beta_v^{j-1}$ ($\beta_v$ — the adaptation memory). In the Gaussian
approximation $I_{\text{mem}}$ and $I_{\text{pred}}$ are computed exactly (logdet), and
$\eta_v = I_{\text{pred}}/I_{\text{mem}} \in [0, 1]$ by construction. For characteristic parameters
$\eta_v \sim O(0.1)$; nostalgia grows ($\eta_v$ falls) when the adaptation memory $\beta_v$ **outgrows** the
drift of the environment $\tau_E$ — the system integrates an already-stale ligand, and the fraction of pure
ballast increases (at $\tau_E = 5$: $\beta_v = 0.3 \to 0.99$ yields $\eta_v \approx 0.29 \to 0.035$). This
gives nostalgia a concrete falsifiable reading: faster drift or slower adaptation → more ballast. The full
protocol is in Supplementary § S3.5; the code is available in the data repository (see the "Data
Availability" section).

*Measurability.* It is essential that $I_{\text{mem}} = I(M_t; X_E^{\le t})$ is **measurable** from time
series: it depends only on the covariances of the ligand $\text{Cov}(s_i, s_j)$ (directly observable) and the
covariances $\text{Cov}(m, s_k)$ of the **reconstructed** methylation $m$ with the ligand, where the **output
of the signaling loop (kinase activity)** is read via FRET (Sourjik–Berg 2002), while the methylation $m$ is
a latent adaptation variable reconstructed from the dynamics of this activity (single-cell monitoring of
signaling proteins — Cluzel et al. 2000); the ligand $s$ is set by microfluidics. The operational liability
of the informational quantity is **no worse** than that of the thermodynamic one: $I_{\text{mem}}$ is
estimated from the same available observables as the calorimetric $E_{\text{actual}}$ (proof-of-measurability
— Supplementary § S3.5).

*Epistemic status of the number.* The estimate $\eta_v \sim O(0.1)$ is **an illustration of form**, not a
quantitative claim about real *E. coli*: it is obtained from a minimal linear model whose purpose is to show
measurability and order of magnitude, not to fix a value. An exact experimental mapping (which FRET readout
to identify with $M_t$; the window for $X_E^{\le t}$; truncation of the cumulative to a finite
$\tau_{\text{mem}}$) requires calibration against experimental chemotaxis data (Tu et al. 2008; Cluzel et al.
2000; Sourjik–Berg 2002) and remains a direction for future work. The passive protocol bypasses the active
case: a freely-swimming *E. coli* is in the feedback regime (the open item of § 2.1, the Sagawa–Ueda 2010
bound).

**Contrastive case (*E. coli* versus *Synechocystis* / syn3.0).** The discriminating power of the scale
manifests not in the absolute value of $\eta_v$, but in the **contrastive** comparison of systems with
different structure of predictive memory — as a difference of orders of magnitude **within** the class of
biology, read as a ratio of predictive fractions. The cyanobacterium *Synechocystis* sp. PCC 6803 (diurnal
illumination cycles, slow temperature gradients) and chemotactic *E. coli* (thousands of Tar receptors
tracking fast chemical gradients) differ not only in the complexity of the environment but also in the
characteristic time of its drift $\tau_E$. By the formalism of the worked example, the sign of the
$\eta_v$-contrast is set **not** by the complexity of the environment as such, but by the memory/drift ratio:
slow drift (large $\tau_E$) keeps the model fresh for longer and **raises** $\eta_v$, fast drift lowers it.
Therefore the direction *E. coli* ↔ *Synechocystis* here is **not** asserted as a prediction — it depends on
the memory/drift ratio of each organism and is itself part of what is to be tested. The minimal cell
JCVI-syn3.0 (a genome of $\sim 473$ genes versus $\sim 4300$ in *E. coli*, a sharply curtailed repertoire of
responsiveness to chemical signals) lies on a separate axis — of impoverished repertoire capacity of the
model, not of the drift time of the environment. The qualitative residue of the contrastive is a falsifiable
link of $\eta_v$ with the rate of adaptation to new niches (§ 5), not a fixed ordering of the three systems.

*Epistemic status of the contrastive.* The contrastive is **an illustrative sketch of the form** of the
scale's discriminating power, not an independent empirical support for the prediction
$r_{\text{adapt}} \propto \eta_v^{\alpha}$ (§ 5). No specific ordering of the three systems is derived here
from the complexity of the environment: the sign of the $\eta_v$-contrast is set by the memory/drift ratio,
and it requires calibrated MI-estimates of specific channels (the circadian KaiABC oscillator and the
photosystem regulators of *Synechocystis*), not structural intuition. A strict falsification of the
$\alpha$-dependence requires an independent co-measurement of $I_{\text{pred}}$ and $I_{\text{mem}}$ for both
systems in an identical protocol — a direction for future work, not a result of the present one. The
contrastive is retained as a methodological illustration of form, not as a quantitative confirmation. (Exact
new numbers for *Synechocystis* / syn3.0 are deliberately **not** given here: under the new $\eta_v$ they
require a separate MI-estimate, and the substitution of numbers would be the same sin of unwarranted
precision that the present work avoids.)

### 3.6 The Large City

A large city is a strong candidate for vitality on a planetary scale, and under the new framework this is
seen more distinctly. The infrastructure and administrative regulations are physically realized and **paid
for by the city's own budget**; are homomorphic to the flows of resources, people, and information; and
generate targeted decisions verifiable by crises and adaptation. The error-return loop is closed: a
distortion of the city's model of flows returns as a crisis to the city itself. Therefore $S = 1$ — the city
is self-funded (condition (i)) and bears the model's error through its own dissipation (condition (ii)).

*Scope of the city case.* The article gives strictly two results for the city and deliberately **does not**
give a third. The positive ones: (i) the structural screening — a demonstration of the **form** of the
composite $I_v$ (2b) (a reproducible computation on synthetic order-of-magnitude-distinct archetypes —
below), and (ii) the verdict of the pair $(S, \eta_v)$ — $S = 1$ at $\eta_v > 0$. **The numerical value of
$\eta_v$ for the city is not computed**: it requires a full MI-pipeline — a co-measurement of $I_{\text{pred}}$
and $I_{\text{mem}}$ of the administrative loop (resource flows → decisions) — and is **deferred to future
work** (a separate urbanistic node of the program). This is a justified "out of scope," not an excuse: the
pipeline would require instrumented urban observables — time series of resource and human flows, budgetary
and regulatory decisions — with a nonparametric MI-estimation on them (k-NN estimators of the KSG type,
neural-network ones of the MINE type; a catalog of MI-estimators is in Supplementary § S2.1); the present
work presents neither such series nor their MI-calibration. Here a structural diagnosis and a sign are given,
not a number.

Verdict: the city is **vital** — it passes $S = 1$ and $\eta_v > 0$. The grade (the relative magnitude of
$\eta_v$ among vital systems) requires MI-estimation and is not asserted here. The paradigm-case claim about
the city is carried by **the closure of the loop $S = 1$ and the positivity of $\eta_v$**, not by the
quantitative smallness of efficiency. A reproducible computation of the structural index $I_v$ on synthetic
archetypal profiles (order-of-magnitude-distinct configurations, not real cities) is given in the code of the
worked examples (see the "Data Availability" section); an empirical calibration of $I_v$ of concrete cities
against open data (OECD FUA, CDP Cities, WIPO/OECD REGPAT, GDELT, OpenStreetMap) is the subject of a separate
work.

### 3.7 Gaia and Boundary Cases

The Earth's biosphere regulates the atmosphere, the ocean, and the climate through biogeochemical cycles — a
compression in the strict sense, paid for by collapses of species, mass extinctions, restructurings of
ecosystems. Self-payment is evident here: biogeochemistry feeds on its own flux (condition (i)), and a
distortion of regulation returns as collapses of species to the biosphere itself (condition (ii)) — $S = 1$.
What remains open is the **question of the model's unity**: does the biosphere have a single internal
representation of its own environment, or billions of private models of organisms not stitched into one loop
(Doolittle 2014; Lenton and Latour 2018)? On the answer depends whether to count Gaia as **one** vital system
or as a **family** of overlapping vital systems with a zeroed aggregate $I_v$ — this question is retained as
substantively open.

A quantitative estimate of the predictive fraction $\eta_v = I_{\text{pred}}/I_{\text{mem}}$ for the
biosphere is quantitatively undetermined: it requires MI-estimation through the biogeochemical sensory
channel and is left to future work. The estimate through unique genomic content
($\sim 10^{12}$ species $\times 5 \cdot 10^6$ bp $\times 2$ bits/bp $\approx 10^{19}$ bits, against a total
copy volume of $\sim 10^{37}$ bits, Landenmark et al. 2015) is a bound on the capacity of the carrier, not a
measured predictive information, and does not serve as a value of $\eta_v$.

Verdict: the biosphere is **vital** (or a family of vital ones): $S = 1$, $\eta_v > 0$ — the control limit of
the scale at the upper scale. The grade (the magnitude of $\eta_v$) requires MI-estimation and is not asserted
here. The paradigm-case claim is carried by the closure of the loop and the positivity of the predictive
fraction, not by the quantitative magnitude of $\eta_v$.

### Summary across the Paradigm Cases

The six paradigm cases demonstrate: the demarcation works not through a binary "alive/non-alive" table, but
through indicating **which** condition of the pair $(S, \eta_v)$ failed and why. For the Sun, the hurricane,
the flame, and the crystal the numerator is zeroed — there is no model of the environment, $\eta_v = 0$
structurally. For the BZ reaction, autocatalysis, the crystal-as-replicator, and the LLM the predicate of
self-payment is zeroed, $S = 0$: either the error-return loop is not closed (condition (ii) — BZ, the
crystal), or the obligatory dissipation is borne by an external payer (condition (i) — the LLM). *E. coli*,
the city, and the biosphere pass both axes: $S = 1$ and $\eta_v > 0$, differing in grade. Each structural
cause of non-vitality indicates the change of architecture that would make the system vital.

The summary result and the **new asymmetry thesis**: the space of observable matter is structurally complex
almost everywhere (most objects pass the $I_v$ screening), and for systems with a model of the environment the
predictive fraction $\eta_v$ is positive (its exact magnitude for most paradigm cases requires MI-estimation)
— but **closed self-payment loops ($S = 1$) are rare**. The demarcation is carried precisely by this rarity of
the closed loop, not by the magnitude of efficiency: the $\eta_v$-verification does **not** reject the city,
the biosphere, or the LLM by the smallness of the number — the rejection of the LLM, the thermostat, the
hurricane, and the Sun proceeds through the failure **$\eta_v = 0$** (no model) or **$S = 0$** (the loop is
open). The search for life reduces not to a search for structural complexity, nor to the magnitude of
efficiency, but to a search for **closed self-payment loops** — systems that themselves pay for the retention
of their own predictive model and themselves bear the damage from its obsolescence.

## 4. Comparison with Alternatives

This section compares $\eta_v$ with the four programs that have come closest to an operational definition of
vitality: assembly theory, Tononi's integrated information, Deacon's teleodynamics, Friston's FEP. Positional
diagnostics: each operates at the level of $I_v$ or of a single capacity; none reaches $\eta_v$ as a criterion of the
closed self-payment loop.

### 4.1 Assembly Theory

Marshall et al. (2017) formalized the Pathway Complexity measure — the minimal number of recursive assembly steps for
an object with reuse of parts; experimental measurement through mass spectrometry of complex molecules and an empirical
threshold (assembly index $a$ of order 15 for biogenic molecules) were established in Marshall et al. (2021), and the
full program was formulated by Sharma et al. (2023). An object with $a$ above this threshold is interpreted as a
biosignature: the depth of accumulated selection required to assemble such an object is not reached by abiotic processes
on observable timescales.

The assembly index operates on the denominator of the "model × stake" dyad — the measure of accumulated selection —
but does not define the numerator. Assembly theory assigns a high $a$ equally to a fossil and to a living cell, without
distinguishing the selection accumulated in matter from the actual retention of $I_{\text{pred}}$. The error-return
coefficient in the object's current behavior does not figure in the scheme. On the $\eta_v$ scale the assembly index
occupies the position of an operational complexity index, not a vitality scale: a high $a$ is a necessary condition for
the positivity of $\eta_v$ for systems with a complex molecular architecture, but not a sufficient one. The assembly
index is an operational proxy for $C_v$ or $S_v$ within $I_v$, not a standalone scale.

### 4.2 Integrated Information $\Phi$

Tononi and his school (Tononi 2004; Tononi et al. 2016) defined integrated information $\Phi$ as a measure of the
irreducibility of the whole into a sum of parts. In the IIT 3.0 formalization (Oizumi et al. 2014), $\Phi > 0$ is
interpreted as a sufficient condition for minimal phenomenal consciousness. In the context of the demarcation of the
vital, $\Phi$ is a powerful candidate for formalizing the informational capacity $C_v$: systems with high integrated
information satisfy the requirement of a model in which the parts are not decomposable into independent subsystems.

Tononi's program imposes no constraint on the thermodynamic payment for retaining this integrated information and does
not require that the payment belong to the system itself. A household thermostat, under weak formulations of IIT, has a
nonzero $\Phi$ — hence the conclusions discussed in Tononi et al. (2016) about the minimal "experience" of simple
systems. $\Phi$ is a necessary condition for the positivity of $C_v$, not a sufficient condition for the positivity of
$\eta_v$: the thermodynamic ownership of the payment by the system remains outside the IIT apparatus. The relation is
productive as a decomposition: $\Phi$ operationalizes $C_v$, $\eta_v$ adds the requirement $T_v > 0$ with belonging to
the same system.

### 4.3 Teleodynamics

Deacon in *Incomplete Nature* (Deacon 2011) constructed the hierarchy homeodynamics → morphodynamics → teleodynamics.
The third level is defined as the coupling of two morphodynamic systems that mutually constrain each other's
self-destruction; the notion of *absential causality* is introduced — causation by that which does not yet exist (by a
virtual goal not actually given). Teleodynamics is the program closest to the "model × stake" dyad: the model and the
stake are present in the scheme logically, both axes are articulated.

The defect of the program is the absence of an operational quantitative measure. Deacon's hierarchy is formulated in
qualitative philosophical terms, and a reconstruction of $\eta_v$ or of the error-return coefficient through absential
causality is technically impossible without substantial formalization, which the text of the program does not offer.
Teleodynamics is a structural portrait in which both axes of the dyad are present, but a quantitative measure testable
on a bacterium or a megacity is absent. Teleodynamics is a conceptual predecessor whose operationalization through the
$\eta_v$ scale is one of the contributions of the present work.

### 4.4 The Free Energy Principle

Friston's free energy principle (Friston 2010) is the formalization closest to the present framework. In the FEP
literature two quantities are distinguished. *Variational free energy* (VFE)

$$F[q, o] = D_{KL}\bigl[q(s) \,\|\, p(s|o)\bigr] - \ln p(o) \quad \bigl(= \mathbb{E}_q[\ln q(s) - \ln p(o, s)]\bigr), \tag{3}$$

or equivalently $F = D_{KL}[q(s) \| p(s)] - \mathbb{E}_q[\ln p(o|s)]$ (complexity minus accuracy, $-\text{ELBO}$). It is
minimized in perception: the distribution $q(s)$ over the hidden states of the environment approximates the true
posterior $p(s|o)$; $-F$ is a lower bound on the log-evidence $\ln p(o)$. *Expected free energy* (EFE)

$$G[\pi] = \mathbb{E}_{q(o', s'|\pi)}\bigl[\ln q(s'|\pi) - \ln p(o', s')\bigr], \tag{4}$$

is minimized in action selection / active inference. Here $p(o', s')$ is the preference distribution (a generative
model with preferences over future outcomes and states), and $G$ canonically decomposes into epistemic value
(information gain about hidden states) and pragmatic value (proximity to preferences). The distinction is fundamental:
$F$ describes belief updating, $G$ describes the selection of actions (Friston 2010, 2019). For a Gaussian generative
model in the stationary regime, $-F \lesssim I_{\text{pred}}$ — a conceptual correspondence linking the scale and FEP in
the perceptual part; the formal connection is an open technical problem.

The canonical FEP-as-life line ontologizes the Markov blanket as the boundary of the living. The canonical works are
Kirchhoff et al. (2018) "The Markov blankets of life"; Constant et al. (2018); Ramstead et al. (2020). The BDDB
critique (Bruineberg et al. 2022) targets precisely this line.

The principled objection to FEP is formulated in Bruineberg et al. (2022, hereafter BDDB) — a target article in the
BBS format with open peer commentary. The *Markov blanket* (Pearl 1988) — a statistical screening-off condition —
admits two readings: an instrumental one (the *Pearl-blanket*) and a realist one — its ontologization as an objective
boundary of the living system (the *Friston-blanket*, Friston 2019). The central thesis of BDDB: the Pearl-blanket and
the Friston-blanket are indistinguishable without the covert importation of epistemic assumptions; the move from the
former to the latter qualifies as an equivocation. In BDDB the Watt governor is a diagnostic example demonstrating that
the FEP apparatus carries no ontological load of its own (the thermostat as trivial active inference — Baltieri and
Buckley 2019). Parallel critiques are Aguilera et al. (2022, a formal analysis of examples without a stationary
density) and Bruineberg et al. (2018, the ecological-enactive line). The discussion of whether the BDDB critique can be
rebutted remains open.

Our move — the introduction of the self-payment requirement — does not effect a transition from the Pearl- to the
Friston-blanket through a thermodynamic channel. $\eta_v$ offers an **alternative ontology**: instead of the statistical
reality of the blanket separation — the thermodynamic ownership of dissipation by a single physical system.
Self-payment is an assumption independent of the BDDB critique: it shifts the question from "does the Friston-blanket
exist" to "is the retention of the model paid for by the system's own dissipation". $\eta_v$ does not inherit the
epistemic structure criticized by BDDB. Thermodynamic ownership is carried by the predicate $S$: the obligatory
dissipation of model retention is paid for by the same physical boundary $X$ (counterfactual ablation
$-dF_X/\partial t$, § 2.2, § 2.7), not by a statistical separation of hidden states. The assumptions (the candidate
boundary, the threshold $\delta$, the window $\tau_d$) are explicit and testable through sensitivity analysis
(§ S2.4). For the thermostat the predictive information about its own environment is small but **positive** (the bimetal
tracks the autocorrelated room temperature, $I_{\text{pred}} \approx 3$ bits, see below); the demarcation is carried not
by the smallness of the $\eta_v$ numerator, but by the failure of self-payment ($S = 0$): the obligatory dissipation is
paid for by the power grid and the error-return loop is open — regardless of whether the thermostat has a
Friston-blanket.

*Counterfactual ablation of the thermostat.* Applying the procedure of § 2.2 to a bimetallic thermostat with hysteresis
$\Delta T_{\text{hyst}} = 1$ K controlling a room with thermal inertia $\tau_{\text{room}} \sim 30$ min iterates over
five candidates for inclusion in the boundary:

- the bimetallic strip (sensor and actuator);
- the relay contact group (energy switching);
- the heating element;
- the power grid as the current source;
- the external setpoint controller.

Counterfactual subtraction leaves the first two inside the boundary — their removal breaks the regulation loop. The
remaining three are identified as external: subtracting the heater removes the heat source, not the decision loop;
subtracting the power grid likewise; subtracting the setpoint controller does not disrupt regulation around a fixed
setpoint. Inside the boundary, $E_{\text{actual}}$ is the elastic relaxation of the metal plus the dissipation of the
relay, $\sim 10^{-6}$ W (a reproducible computation of the two interpretations — the trivial and the control one — in
the Supplementary Materials). The internal channel retaining $I_{\text{pred}}$ about the room temperature is the
deformation of the bimetal. Estimate: $I_{\text{pred}} \le \log_2(\Delta T_{\text{room}}/\Delta T_{\text{hyst}})
\approx 3$ bits for a diurnal $\Delta T_{\text{room}} \sim 10$ K (up to $\sim 5$ bits for a seasonal range $\sim 30$ K).
This $I_{\text{pred}}$ pertains to the environment "room", not to the environment "thermostat + room + power source".
The loop of decisions paid for by its own decay is incomplete in the thermostat: heating the room is paid for by the
external power grid, not by the bimetal's own free energy. $\eta_v^{\text{thermostat}}$ is undefined in both
self-consistent interpretations, but through the failure of different capacities. In the control task "regulate the
room temperature", $T_v^{\text{int}}$ fails: the heating is paid for by the power grid, $E_{\text{actual}}^{\text{own}}
= 0$ relative to this task. In the trivial task "maintain the bimetal's own shape", $S_v^{\text{int}}$ fails: the
passive thermo-mechanical coupling does not form an error-return loop — under a deviation of the bimetal's shape no own
dissipation corrects it. The divergence between the interpretations points not to an ontological transition, but to the
conventionality of the boundary choice as a methodological instrument: one and the same physical system admits several
self-consistent boundaries. Bruineberg et al. (2022) show formally that such an ontological transition cannot be made
without the covert importation of epistemic assumptions. A full component-by-component analysis of the five candidates
is in Supplementary § S4.4.

The relation between the classes of FEP-applicable and $\eta_v$-vital systems is asymmetric. The claim "FEP is a special
case of $\eta_v$" is wrong in its direction. The correct relation: the $\eta_v$ scale singles out, within the class of
FEP-applicable systems, the subclass in which the minimized $F$ is paid for by the system's own dissipation. Outside
this subclass — the thermostat, an externally powered pendulum, any self-regulating loop with externalized payment —
**self-payment** fails ($S = 0$): the minimized $F$ is paid for from outside, even when the $\eta_v$ numerator is
positive. FEP retains its descriptive power across the whole class but loses its discriminative power: it does not
separate systems with a stake from systems without one. $\eta_v$ supplies a thermodynamic criterion that is
operationally independent of the FEP formalism. Systems satisfying FEP with a non-empty action–perception loop and
nontrivial own dissipation generally pass $\eta_v$-verification. Systems satisfying FEP in a purely formal notation with
externalized energy (the thermostat) fail $\eta_v$-verification.

*Active inference and the space of correspondences.* Active inference (Friston et al. 2017; Parr et al. 2022) is a
concrete computational scheme derivable from FEP when policy is selected through EFE. In active-inference terms the
$\eta_v$ numerator is related to predictive information in the sense of the generative model, and the denominator to
the **informational cost of retaining** the generative model in its own degrees of freedom ($I_{\text{mem}}$); the
physical cost of retention enters as a separate thermodynamic anchor (the Still bound), not into the $\eta_v$
denominator. This is a premise of the $\eta_v$ program, added to standard AIF — it is not derived from EFE minimization
directly. The pragmatic and epistemic value of policies are linked to the numerator (predictive information) through
the structure of the generative model, not to the denominator directly. A detailed mapping of the vocabularies (action,
policy, pragmatic value, epistemic value versus $I_{\text{pred}}$, $E_{\text{actual}}$, $T_v$, $S_v$) is a task for a
separate work; what matters here is that the correspondence is technically possible and does not require revising
either of the source frameworks.

*Andrews 2021 and Williams 2020.* Andrews (2021) attacks FEP for the non-derivability of empirical content from the
formalism; the critique is rebutted in $\eta_v$ by anchoring the numerator and denominator to measurable quantities.
Williams (2020) attacks predictive coding as a neural mechanism, not predictive information as a formal measure; the
critique is neutral with respect to $\eta_v$. A detailed analysis and the distinction between predictive coding (Rao
and Ballard 1999; Clark 2013) and predictive information (Bialek et al. 2001) is in Supplementary § S4.4a.

Summary position: the free-energy-minimization formalism becomes a substantive criterion of vitality only under the
condition of self-payment. Without this condition FEP describes any self-regulating loop and loses its discriminative
power. With this condition FEP is refined into its $\eta_v$-discipline. For systems where FEP applies with a non-empty
action–perception loop and nontrivial own dissipation, $\eta_v$ and FEP give concordant characterizations. For systems
where FEP applies only in a purely formal notation with externalized energy, self-payment fails ($S = 0$): the
demarcation is carried by the predicate $S$, not by the vanishing of $\eta_v$.

### 4.5 Demarcation from Neighboring Programs: Summary Diagnostics

The summary positional diagnostics of the main programs is collected in the table below and reveals a single structural
pattern of defect: each program takes seriously exactly one side of vitality and leaves the rest outside its apparatus.
The organisational closure line (Maturana–Varela, Rosen, Mossio–Montévil–Longo) and the line of OoL programs are
analyzed in detail in § 4.7 and § 4.8 respectively; in the table they appear as one-line positional summaries.

| Program | Axis taken seriously | What is left outside the apparatus |
|---------|----------------------|-------------------------------------|
| Walker–Cronin (assembly theory) | the denominator of the dyad — accumulated selection in matter (assembly index $a$) | the numerator is implicit; $a$ is the same for a fossil and a living cell — vital discrimination requires an external intuition about the error-return loop |
| Tononi (IIT) | the measure of informational integration $\Phi$ | thermodynamic payment; the $\Phi$-positive thermostat is a known critical point of the theory |
| Deacon (teleodynamics) | the structural dyad (absential causality) | a quantitative measure: absential causality is not reconstructible through measurable quantities |
| Friston (FEP) | the free-energy-minimization formalism | the requirement that the model and the dissipation belong to one system; the robust critique of Bruineberg et al. 2022 calls into question the path of ontologizing the Friston-blanket (an open discussion without a settled consensus); $\eta_v$ offers an alternative thermodynamic ontology independent of the outcome of this discussion (see § 4.4) |
| Maturana–Varela / Rosen / Mossio–Montévil–Longo (organisational closure) | the requirement that the loop belong to one system | quantitative thermodynamic discipline: qualitative closure without the thermodynamic discipline of bound (2) (see § 4.7) |
| Hordijk–Steel / England / Maynard Smith–Szathmáry / Pross / Smith–Morowitz (OoL programs) | each operationalizes one side of the abiotic→biotic transition | a unifying operational measure of self-payment as a single thermodynamic criterion for the moment of the origin of life (see § 4.8) |

The listed defects are not accidental: they reflect different ways of taking one side of vitality seriously and leaving
the rest outside the apparatus. $\eta_v$, as a ratio requiring that both components belong to one system, is an
operationalization that does not allow any of the four axes to dissolve into the background.

### 4.6 Relation to the Tradition: A Brief Positional Summary

The $\eta_v$ program is located at the intersection of classical traditions. The Schrödinger line (1944, aperiodic
crystal + negative-entropy-formula) and Szilard–Landauer–Bennett (1929–1989, the thermodynamic cost of information
operations) are the direct inheritance of the numerator–denominator. The nonequilibrium thermodynamics of
Prigogine–Nicolis (Nicolis and Prigogine 1977) is a predecessor of $T_v$. Wiener–Ashby–Foerster (Wiener 1948; Ashby
1952; von Foerster 2003) — second-order cybernetics. Adjoining these are Rosen's anticipatory systems (Rosen 1985) and
Taleb's skin-in-the-game (Taleb 2018, the concept of the stake, formalized in § 2.1). Kolmogorov's algorithmic
information (Kolmogorov 1965) is a predecessor of $C_v$. Kauffman's autocatalytic closures (Kauffman 1993, 2000) and
the programmatic framework of Walker–Davies–Ellis (Walker et al. 2017a) complete the list. $\eta_v$ is not the heir of
any single one of them but a juxtaposition: a thermodynamic frame plus predictive content plus a structural accounting
of capacities through counterfactual ablation (§ 2.2). The scale gathers both axes of the model/stake dyad into a
single measurable quantity and explicitly introduces the requirement of own dissipation. Each classical program is
operationalized through one of the capacities within $I_v$; the unification into a single vitality scale is an
independent step that none of the source frameworks took. The extended positional map is in § S4.7–S4.9 supplementary.

### 4.7 The Organisational Closure Line

*The organisational closure line* (autopoiesis, Maturana–Varela 1980; M,R-systems, Rosen 1991; constraint closure,
Mossio–Montévil–Longo 2016; organisational closure, Bich–Green 2018; plus the epistemic cut, Pattee 1982) formulates
life through the closure of causal processes. Closure is taken with respect to efficient causation or the constraint
network that produces the system's components. The $\eta_v$ program is categorically distinct: organisational closure
formalizes the production of components and qualitative circularity; self-payment formalizes the thermodynamic
ownership of the model's budget by the single physical system that does the modeling. A *differential test* on the pair
*E. coli* / JCVI-syn3.0 (Hutchison et al. 2016) distinguishes the scales within a single class of organisational
closure: the qualitative criteria do not distinguish these systems, whereas $\eta_v$ ranks them through the product of
the informational and thermodynamic components. Self-payment does not claim to rebrand or replace organisational
closure — it adds to its qualitative conceptual work a quantitative thermodynamic discipline through the Still bound
(2). A full analysis of the four lines (Pattee, Maturana–Varela, Rosen, Mossio–Montévil–Longo) with categorial
distinctions and the differential test is in § S4.7 supplementary.

### 4.8 The Origin-of-Life Line

*The origin-of-life line* is represented in Theory in Biosciences and adjacent journals by five relatively autonomous
traditions. The Eigen–Schuster hypercycle (Eigen 1971; Eigen and Schuster 1979) is a replicator-level autocatalytic
closure with a template carrier. RAF networks (Hordijk and Steel 2004) are a formalism of collective autocatalysis.
Dissipative adaptation (Perunov, Marsland, and England 2016; the statistical basis — England 2013, *Statistical physics
of self-replication*) is a thermodynamic predecessor of the self-payment anchor (the Still bound) and of the capacity
$T_v$, not of the $\eta_v$ denominator. Major transitions (Maynard Smith and Szathmáry 1995; Szathmáry 2015) are a
hierarchy of evolutionary levels with a re-addressing of the subject. The geochemical programs (Pross 2012; Smith and
Morowitz 2016; Kauffman 2019; Martin and Russell 2003) detect a closed loop atop a geochemical flux. Each
operationalizes one side of the abiotic→biotic transition. In $\eta_v$ terms, all five articulate one and the same
phase transition. The moment of the origin of life is the moment when a geochemical system moves from external payment
to self-payment: part of the free energy is closed within its own loop and physically pays for the retention of the
model of the environment. The positivity of $\eta_v$ is a **necessary condition** of this moment in each of the
programs; sufficient conditions include Darwinian dynamics at the population level (§ 2.7). An operational procedure for
measuring $\eta_v$ on a pre-biotic geochemical substrate is not defined and constitutes an open problem of the program.
A detailed analysis of the five traditions with the points of contact and the parallel program of Chirumbolo–Vella
(2026) is in § S4.8 supplementary.

### 4.9 Positioning within Contemporary Demarcation Debates

The $\eta_v$ program is methodologically compatible with six robust lines of contemporary philosophy of biology. These
are the anti-definitionism of Cleland (2019), the life-as-lineage of Mariscal–Doolittle (2020), the
operational-frontiers of Bich–Green (2018), the process-biology of Pradeu (2018), the information-theoretic
individuality of Krakauer et al. (2020), and the basic-autonomy of Ruiz-Mirazo–Moreno (2004). The program appears not
as an alternative to them but as a formal quantitative scale on which these lines can work together. $\eta_v$ does not
propose yet another definition of life through lists of features but contributes an operational discriminator with an
explicit falsification regime (§ 5) and a processual ontology (the scale is computed over the window $\tau_d$, § 2.6).
On the boundary cases (virus-in-isolation, the minimal cell, LLM-as-corporation) the scale behaves in agreement with
biological convention through counterfactual ablation § 2.2. This is a contribution to the ongoing demarcation
discussion, not a proposal of a new definition of "what life is". A detailed positional diagnostics for each of the six
lines is in § S4.9 supplementary.

## 5. Falsification Criteria

The program lists below nine testable consequences in three blocks. The actual falsification surface,
however, is narrower (§ 2.7, "The asymmetry of falsification"): false-positive cases are excluded by construction, and the empirical
risk concentrates in false-negative penetration (Block 2 item 3) and in the failure of the progressive predictions
(Block 3 item 1, which carries Prediction 1). A procedural rule common
to all: the system boundary and the proxies $I_{\text{pred}}$, $I_{\text{mem}}$ are fixed before the verification of $\eta_v$ and are not
revised in order to obtain the desired sign (§ 2.2). Falsification operates on two levels — the methodological
(a defect of the current operationalization) and the ontological (the unsoundness of the concept itself); the distinction is fixed
post hoc for each line that is realized.

### Block 1 — Direct Refutations of the Scale

These attack the structure of $\eta_v$ by zeroing out one of the three capacities.

1. **$T_v$ failure (self-payment of the thermodynamic floor).** Observation: a vitally-credited ($S = 1$) system,
   whose Still-mandatory dissipation of retention is demonstrably supplied **from beyond** its
   counterfactual-ablation boundary (§ 2.2) — floor (2) is paid externally. Refutes: the thesis of self-payment
   of the thermodynamic floor (not the Still bound itself, which is a theorem of stochastic thermodynamics); zeroes out $T_v$
   as a necessary condition.
2. **$C_v$ failure.** Observation: a vitally-credited system that retains predictive information about a drifting
   environment over a window $\tau_d$, for which the bound-(2)-mandatory cost of retaining nonpredictive memory **is not
   attributed** to its own budget (under the verdict $S = 1$ it is paid externally). Refutes:
   the consistency of the self-payment predicate $S$ with $C_v$ as a necessary condition.
3. **$S_v$ failure.** Observation: a system with $\eta_v > 0$ together with both $Q < Q_{\text{null}} + 2\sigma$
   (modularity indistinguishable from a degree-preserving null model — a configuration model preserving the degree distribution) and $C(k) \not\sim k^{-\beta_h}$ with $\beta_h \in [0.5,\, 1.5]$
   (absence of the hierarchical signature per Ravasz–Barabási 2003). Refutes: $S_v$ as a necessary condition.

Refutation of any capacity simultaneously collapses both scales — $\eta_v$ through the numerator/denominator, $I_v$ through
the geometric mean. This is one falsification through capacity, not a double one.

### Block 2 — Tests of Proxies and Operationalization

These attack not the structure of the scale but its anchoring to measurable quantities.

1. **Violation of the monotonicity of the adaptation rate in $\eta_v$.** Observation: in controlled experimental evolution,
   systems with $\eta_v$ differing by an order of magnitude yield adaptation rates statistically indistinguishable over long windows.
   Refutes: the central relation is deprived of numerical meaning (constructive form — Prediction 1 below).
2. **Vitality along three independent channels with $\eta_v = 0$.** Observation: a system with positive vitality
   by adaptation rate, self-repair speed, and biochemical markers of self-production (Joyce 1994), yet
   $\eta_v = 0$ under all sanctioned operationalizations. Refutes: the numerator as an operational proxy
   (the methodological level, § 2.7), or the concept of vitality as the efficiency of self-modeling (the ontological level).
3. **A conventionally living system with $\eta_v = 0$.** Observation: a biological system, unquestionably alive by
   conventional criteria, with strictly zero $\eta_v$ under all reasonable operationalizations. Refutes:
   the adequacy of the scale as an operational discriminator of vitality.

### Block 3 — Progressive Predictions

The program's excess empirical consequences, not derivable from competing frameworks.

1. **Prediction 1 — a power law of the adaptation rate.** Here $\eta_v \equiv \eta_v^{\mathrm{do}}$ is the passive
   (interventional) freshness of the model measured **for each line**: the immobilized FRET of each strain
   ($\mathrm{do}(a) =$ immobilization, § 2.1), and **not** the active freshness of freely-swimming cells. The prediction is therefore
   **correctly posed** (the predictor $\eta_v^{\mathrm{do}}$ is defined and measurable by immobilized FRET) independently of the
   open status of the active boundary of $\eta_v$: strains with greater passive freshness of the model adapt faster. It is
   moreover **assumed that $\eta_v^{\mathrm{do}}$ is a monotone proxy for the active predictive freshness** driving the
   adaptation of freely-swimming cells, and **the adequacy of this proxy is part of what Prediction 1 tests/falsifies**. An additional **cross-scale bridge** is assumed: the synchronic freshness of the signaling loop (seconds–minutes, within a single cell) monotonically tracks the rate at which a line re-fits its model under selection over generations; this transition from the intracellular rate to the intergenerational rate is likewise part of the falsifiable content of Prediction 1. Observation: across 45 *E. coli* lines in a chemostat,
   $r_{\text{adapt}} = A \cdot \eta_v^{\alpha}$ with $\alpha \in [0.3,\, 1.0]$ and correlation coefficient
   $\rho \in [0.4,\, 0.7]$ (Pearson between $\log r_{\text{adapt}}$ and $\log \eta_v$). Refutes:
   $\hat{\alpha}$ significantly outside $[0.3,\, 1.0]$ at $p < 0.01$ (the wrong exponent);
   $\hat{\rho} < 0.2$ (no detectable trend); $\hat{\rho} < 0$ (a trend in the opposite direction —
   a qualitative refutation).
2. **Prediction 2 — monotonicity of $\eta_v$ in the matching window.** Observation: in the regime of approach to stationarity
   at normalized dissipation, a monotone increase of $\eta_v(\Delta\tau)$ is expected over the interval $\Delta\tau \ll \tau_d$.
   Refutes: a decrease of $\eta_v$ with $\Delta\tau$ — a counterargument to the stationary framework as such.
3. **Prediction 3 — an empirical threshold for internalization of the energy budget $f^*$** (where $f = E_{\text{actual}}^{\text{own}}/E_{\text{actual}}^{\text{total}}$ is the fraction of own energy in the total budget). The structural predicate of closure of the self-payment loop is **binary** (counterfactual ablation § 2.2: the error-return channel either is self-paid or is not); $f$ is a continuous proxy of this closure, not the deciding boundary itself. Observation: for hypothetical autonomous
   embodied agents, the fraction passing the screening ($\eta_v^{\text{int}} > 0$) rises sharply above the
   empirical threshold $f^* \in [0.1,\, 0.5]$ — a statistical regularity of joint internalization
   (a persistent state + own payment + a physical error-return channel), not a structural definition. Refutes:
   the systematic observation of a system with $f \in [0,\, 0.1]$ that passes the screening, or with $f > 0.5$ that fails it.
   A differential prediction relative to AI-safety (Hubinger et al. 2019; Carlsmith 2022): the *capability* threshold is
   independent of the *thermodynamic* budget $f^*$; the scope is not applicable to present-day cloud-hosted LLMs without state retention
   ($f = 0$ by construction).

*A condition confirming the uniqueness of the operationalization (not a falsification criterion).* The discovery of an alternative proxy
yielding the same demarcational discrimination, but not reducible to $\eta_v$ by an identity or a monotone transformation,
does not refute the program — it confirms the substantiveness of the demarcation.

Full operational protocols (numerical criteria, p-values, samples, pre-registration requirements,
the Bennett-regime caveat for Block 1 item 1, the NASA referent for Block 2 item 2, the scope scenarios of Prediction 3) — § S5
of the supplementary. A summary Lakatosian passport of the program — § S5.4.

## 6. Discussion and Open Questions

*Astrobiology.* The principal consequence is a reformulation of the search-for-life program. Most objects pass the
$I_v$-screening (structural potential is universally high) and fail the $\eta_v$-verification (actual closure of the
self-payment loop is rare). Operationally: in the design of biosignature-search missions (Europa Clipper, JUICE, Dragonfly,
exoplanet spectroscopy), priority shifts from chemical disequilibrium to the search for a triple simultaneity —
nonequilibrium chemistry ($T_v$), a biogenic-like informational signature ($C_v$, via isotopic fractionation and
chirality), and a hierarchically-modular topology of the environment ($S_v$). Each is a necessary condition; the simultaneity of all three
is an operational candidate for a biosignature. The connection with the already-existing methodological framework of the Ladder of Life Detection
(Neveu et al. 2018): $\eta_v$ is positioned as one cross-section of the operational criteria for life detection, complementing the
chemical-structural rungs of the ladder with a thermodynamic requirement of self-payment.

*The origin of life as closure of the self-payment loop.* The biosignature-search program fixes **where** life
exists; the parallel question is **when** it arises on an evolving geochemical substrate. Here, as
in § 3.4 for AI systems, an explicit two-level distinction is required.

*The structural level.* Positivity of $\eta_v$ is a **necessary condition** of the moment of the origin of life
(consistent with § 4.8 and with the "necessary, not sufficient" formulation of the thermodynamic requirement of self-payment).
Sufficient conditions include Darwinian dynamics (§ 2.7), which entered the working NASA definition of life
as a "self-sustaining chemical system capable of Darwinian evolution" (Joyce 1994); $\eta_v > 0$
fixes the thermodynamic cross-section, evolutionary dynamics the selective one. Structurally, the moment of passing the
counterfactual ablation of § 2.2 is the moment when a geochemical network first constitutes itself as a closed
catalytic loop with self-payment: part of the free energy ceases to pass through in transit and begins to
pay for the retention of the loop's own predictive information about the environment. Before this moment $\eta_v$ is
**undefined** (there is no loop as an object of measurement); after it, $\eta_v$ is continuously measurable. The boundary between "before" and "after" is the
binary structural predicate of counterfactual ablation, not a gradient within the positive class.

*The empirical level.* The operational procedure for measuring $\eta_v$ on a pre-biotic geochemical substrate
is undefined and constitutes an open problem of the program — a programmatic promise / direction of research,
requiring the development of proxies for $I_{\text{pred}}$ and self-payment in an evolving geochemical
network. The counterfactual ablation of the boundary of § 2.2 and the MI-estimation of $I_{\text{pred}}$ via the sensory channel apply
to already-formed biological systems; their transfer into the pre-biotic register is a concrete direction
of operational extension. Possible steps: (a) RAF networks (Hordijk and Steel 2004; Hordijk 2019) as a structural
proxy of closure of the catalytic loop — counterfactual subtraction of individual components of the network is an operational
realization of § 2.2 on the geochemical graph. (b) Isotopic signatures (fractionation of $\delta^{13}\mathrm{C}$,
$\delta^{34}\mathrm{S}$) and chiral signatures — a proxy for $C_v$ (the network's memory of the state of the environment).
(c) An integrated thermodynamic-network test for positivity of self-payment via the measured free-energy
balance of a RAF-closed subnetwork relative to its reactive surroundings. The development of such proxies and their calibration
on contemporary biominiatures (minimal cells, synthetic protocells) is future work.

The connection with hydrothermal hypotheses is direct. These include the alkaline-vent scenarios of Martin and Russell (2003),
the metabolic-core programs of Smith and Morowitz (2016), the dynamic kinetic stability of Pross (2012), and Kauffman's adjacent-possible
(Kauffman 2019); the general physical framework of OoL is Walker (2017b). Each of these programs articulates the same
structural transition from its own side, without a unifying thermodynamic measure. The constructive diagnostic is formulated as a direction of development, not as an already-available protocol.
It requires the simultaneous appearance of three components: catalytic closure via RAF analysis of the geochemical
network (Hordijk and Steel 2004; Hordijk 2019), informational memory via isotopic and chiral signatures,
and a positive thermodynamic account by the scheme of § 5. This is an operational
reformulation of the task of astrobiology: not only to "find where life is" but also to "detect the structural transition to
it" — falsifiable in the event of discovering geochemical systems with a stable $\eta_v > 0$ without the characteristic triad,
once the methodology is operationally further developed.

*The ethics of artificial intelligence.* The shift from the question "is the model complex enough to be a moral subject" to the
question "will the model begin to bear its own errors itself." The appearance of one's own dissipative payment for the model,
retained in the own degrees of freedom of the working loop, is the structural condition under which $\eta_v$
emerges from the region of indeterminacy into positive values. The phasing pertains to the definition of the self-payment loop
(the structural predicate of counterfactual ablation § 2.2 is binary), not to the empirical transition of the system; the empirical
dynamics of the loop's appearance in a real population of AI systems is an open question with an expectedly continuous profile in the fraction
of internalized payment. The current standard LLM architecture (a stateless forward pass with externalized payment
of the infrastructure) excludes the fulfillment of the structural condition. The path to a positive $\eta_v^{\text{int}}$ for an artificial
system requires the simultaneous internalization of (a) a persistent state, (b) own payment of computation, (c) a physical
error-return channel — not jointly realized in any existing system at the time of writing. This is a
structural condition, not a calendar forecast. The formal anchoring to the triad. (a) A persistent state
operationalizes $C_v^{\text{int}} > 0$ (a memory channel for retention). (b) Own payment of computation —
$T_v^{\text{int}} > 0$ (one's own thermodynamic budget). (c) A physical error-return channel — $S_v^{\text{int}} > 0$
(closure of the loop's topology). The simultaneity of all three yields $\eta_v^{\text{int}} > 0$.

"To bear one's own errors" — in the technical sense of § 2.1: the model's errors return as a physical loss of free
energy of the system itself, not as reputational sanctions through an external corporate substrate. A drop in the frequency of an LLM's usage and its
retraining by the corporation's efforts is the corporation's payment, entering the $\eta_v$ of the corporation; the $\eta_v^{\text{int}}$ of the model as an
agent remains zero. Regulator fines, legal sanctions against the developer, market reputational losses —
return the damage not to the system retaining the model but to its external substrate.

*Complex systems and social dynamics.* In application to cities and civilizations, the scale opens two thresholds: the structural
screening ($I_v$) and the verification ($\eta_v$). A civilization with high $I_v$ and a sagging $\eta_v$ — structurally rich,
failing the retention of the loop — is diagnostically distinct from a civilization with a sagging screening (destruction
of infrastructure). The differentiation is useful for studies of the resilience of social systems; it requires empirical verification.

*The Fermi paradox and the externalization filter.* The paper's hypothesis applied to the Fermi paradox: the silence of the Universe
is explained not by the rarity of life but by **the collapse of technological civilizations at the threshold of externalization of the energy budget**.
In the terms of the framework: a civilization passes the "filter" if and only if its $\eta_v$ is positive through its own
dissipation ($T_v$ retained within its loop). Technological development directed toward the use of external sources
(the power grid → reactors → megastructures) increases $E_{\text{actual}}^{\text{external}}$ without increasing
$E_{\text{actual}}^{\text{own}}$ — most civilizations pass the $I_v$-screening (visible structural complexity:
radio signals, megastructures) but **fail the $\eta_v$-verification** by the same mechanism as a stateless LLM under the
boundary "weights at the moment of inference." Such civilizations are unstable on evolutionary timescales and do not persist as
stationary SETI sources. The claim has the status of a
speculative extrapolation and is subject to independent empirical verification. A testable statistical prediction about
observable SETI signals: transient, non-repeating, a power-law distribution by duration with a cutoff — an indicator of the
filter; a stationary spectrum with an IR excess, persisting over decade-long windows — an indicator of passing both
thresholds. The existing null results of Dyson-sphere searches (the G-HAT survey over ~10⁵ WISE galaxies, Griffith et al. 2015; the rationale for the
program — Wright et al. 2014) are consistent with the filter prediction but do not refute alternative scenarios (rare-Earth-class hypotheses, technomaturity below the astrophysical
resolution). The refutation condition: the discovery of three or more independent stationary SETI sources with a confirmed
IR signature of megastructures over intervals $\gtrsim 50$ years is incompatible with the externalization-filter prediction in its
current formulation.

*The status of the consequence.* The reformulation has the status of a speculative extrapolation: neither the NASA Astrobiology Strategy,
nor the ESA Cosmic Vision, nor the planetary Decadal Survey operates with the category of "self-payment loop." If the standard programs
achieve reliable demarcation of extraterrestrial life without recourse to $\eta_v$, the framework will bring no astrobiologically new
discriminative power and reduces to the existing agnostic biosignatures.

*Open questions.* The non-stationary generalization of the stationary result on memory drift (§ 2.1) for systems with growing memory — biospheres
over eonic windows, learning artificial systems — requires a rigorous proof that accounts for the cost of expanding
memory (developed in the companion work, Andriishin 2026). The catalog of operational proxies for $I_{\text{pred}}$ requires expansion with numerical examples and limits of
applicability. The case of Gaia — the question of the unity of the biosphere's model — is open empirically and depends on data on the consistency
of biogeochemical cycles over eonic windows. The operational protocol for detecting vital AI requires precise
thresholds for population experiments. The philosophical status of
$\eta_v$ — a position of moderate operationalism with a demarcation between the ontological referent and the operational measure —
is the task of a separate work.

*Dormant states.* Biological states of reversible arrest — spores, a tardigrade in cryo-anabiosis, frozen embryos,
the lysogenic cycle of a phage — formally give $\dot{I}_{\text{pred}} = 0$ and $E_{\text{actual}} \to 0$, which takes $\eta_v$
out of the domain of definition of the scale (§ 2.7). Reconciliation with biological convention
("spores are alive") is achieved through the averaging window $\tau_d$: with a choice of $\tau_d$ on the evolutionary scale (the full cycle
sporulation $\to$ activity $\to$ sporulation) the sign of $\eta_v$ returns to positive. A formal extension of the
scale to regimes of temporary reversibility of the sign is a direction of the companion work (Andriishin 2026).

*Boundary conditions of applicability.* The $\eta_v$ scale does not make three types of claim.

1. It does not assert the identity of vitality and consciousness. High $\eta_v$ is a necessary condition for complex cognitive
   activity (without retention of one's own predictive information, neither prediction, nor planning, nor
   reflection is possible), but not a sufficient one. The question of phenomenal experience, discussed within integrated
   information (Tononi et al. 2016) and the hard problem of consciousness, lies beyond the $\eta_v$ scale.
2. It does not presuppose biocentrism by the reverse gesture. High $\eta_v$ is possible in systems of a non-biological substrate —
   large cities, planetary-scale biospheres, hypothetical artificial embodied agents with a closed self-payment
   loop. This is a substantive prediction, not a calibration fit.
3. It does not reduce to a moral criterion. A civilization that fails the $\eta_v$-verification while retaining the $I_v$-screening is
   diagnosed as structurally rich but non-vital — a diagnosis of a structural state, not an ethical verdict.
   The ethical consequences of the program are a separate topic, resting on the structural diagnosis but not derivable from it by direct
   implication.

*The stationary regime as an explicit limitation of the domain of applicability.* All the results presented — definitions,
demarcation tests on the paradigm cases, conditions of falsification — are formulated under the assumption of stationarity of the environment
and finiteness of the system's memory. This is not a default simplification: stationarity stabilizes $I_{\text{mem}}$ and renders the stepwise cost of retention
(the Still bound (2)) stationary, and therefore permits sharply formulated demarcation answers.
In the non-stationary regime — with growing memory, a drifting environment, and a nonempty archival layer — the formalism requires
extension: a cumulative dissipative cost, accounting for the cost of retaining historical bits, and the phenomenon of
informational nostalgia. This extension is the content of the companion work (Andriishin 2026). There a
conditional lemma on the inevitability of nostalgia is proved in the canonical class of slow drift (OU-parameterization with FIFO-refresh
and $c < 1$). The quantitative adiabatic asymptotics of $\dot{\eta_v}^{\text{excess}}$ for systems without periodic
memory reset is formulated there as an open hypothesis, supported by a parametric scan. The informational capacity
$C_v$ of the present work is there methodologically refined through a partition of $C_v^{\text{static}}$ (statistical complexity
$C_\mu$, structural memory — § 2.3) against $C_v^{\text{predictive}}$ (excess entropy $\mathbf{E}$,
the predictive part — § 2.3), related by
$C_v^{\text{predictive}} = (1 - \nu) \cdot C_v^{\text{static}}$, where $\nu$ is the fraction of nostalgic bits; in the stationary
regime of the present work the divergence of $C_v^{\text{static}}$ and $C_v^{\text{predictive}}$ ceases to grow
($\dot\nu \to 0$, $\nu$ levels off at a constant value) and serves as a diagnostic of drift only in the non-stationary
extension, which reconciles the two works. The applicability of the
stationary $\eta_v$ developed in the present article is limited to systems with an ergodic environment and finite
memory; for biospheres over eonic windows, learning AI systems under drift, and civilizations with a growing archive —
consult the non-stationary extension.

## 7. Conclusion

The work has defined vitality operationally as the pair $(S, \eta_v)$: the predictive efficiency of self-modeling
$\eta_v = I_{\text{pred}} / I_{\text{mem}} \in [0,1]$ — the fraction of the memory retained by the system about the environment that still
predicts its future — **given** a closed self-payment loop $S$ (§ 2.7). The bound $\eta_v \le 1$ for passive
self-modeling is a consequence of the data processing inequality (without a separate thermodynamic premise; the active
case — § 2.1), not an energetic normalization; the thermodynamic cost of retaining
aging memory is borne by a separate anchor — the Still bound (2). Structural screening requires the simultaneous presence of three capacities — $T_v$, $C_v$, $S_v$ —
assembled into the composite index of structural readiness $I_v$. The index is a necessary but not sufficient condition of
vitality; it occupies the same positional place as the assembly index, $\Phi$, Deacon's morphodynamics. $\eta_v$ itself is an
operational criterion of synchronic vitality in the sense of a binary sign ($\eta_v > 0$ given a closed self-payment
loop). The criterion distinguishes structurally rich but non-vital systems (the Sun, a hurricane, an LLM under the boundary "weights
at the moment of inference" — $\eta_v^{\text{int}}$ undefined) from systems with a structurally closed self-payment loop by
the counterfactual ablation of § 2.2. Among systems with a closed loop, the bacterium has a reproducibly measured $\eta_v > 0$
via § 3.5. The city, the biosphere, the LLM-as-corporation — with a structurally positive sign ($S = 1$) at a quantitatively
undefined magnitude of $\eta_v$ (MI-estimation of $I_{\text{pred}}$ and $I_{\text{mem}}$ — an open problem, § 3.4, § 3.6, § 3.7). What is substantive across classes is
precisely the sign, not the absolute magnitude (§ 3.5).

The application of the two-stage procedure to the six paradigm cases yields sharp demarcation answers and makes explicit the structural
asymmetry: complexity is ubiquitous, closed self-payment loops are rare. The comparison with assembly theory, IIT,
teleodynamics, and FEP positions $\eta_v$ as an operational complement to each of the programs. Concrete
conditions of falsification have been formulated, anchored to testable physical, informational, and evolutionary predictions.

The program is open to refutation along several independent lines, with the empirical risk concentrated in
false-negative penetration and the carrying Prediction 1 (§ 5; § 2.7, the asymmetry of falsification; with a separately
fixed condition confirming the uniqueness of the operationalization), and is disciplined against rescue
maneuvers by the requirement to name the concrete failed capacity
at each zeroing (§ 2.6): refutation of one capacity collapses both scales. This discipline limits but does not
eliminate the Lakatosian risk of a protective belt (§ 2.6, § 2.7). In this lies its scientific status — not a claim to a final
definition of life, but a testable research program with explicitly articulated limits of applicability.

*Biological consequences.* The principal substantive effects of the $\eta_v$-program are within theoretical biology,
not on the astrobiological or AI periphery. (a) The synchronic/diachronic decomposition of vitality (§ 2.7) gives a new
formulation of the question "what is an organism" in the spirit of Pradeu (2018) and Bich and Green (2018): synchronic
$\eta_v > 0$ is a necessary condition of the individuation of the living, while diachronic Darwinian dynamics is its
complementary dimension. (b) Minimal cells (JCVI-syn3.0, Hutchison et al. 2016) and viruses receive an
operationalizable boundary via the counterfactual ablation of § 2.2: the pair (WT *E. coli* / syn3.0) is distinguishable not by a
qualitative criterion of organisational closure but by the quantitative scale $\eta_v$ through both components (§ 4.7, § S4.7),
while viral particles fall under the readdressing of the subject to (virion + host) — a diagnosis structurally homologous to the
LLM-corp ($B_4$, § 3.4). (c) Major transitions in evolution (§ 4.8, § S4.8 — after the hypercycle and the major transitions
of Maynard Smith–Szathmáry) are reformulated as events of readdressing the subject of self-payment with a thermodynamic
criterion for detecting the event. A new aggregate actor appears, with its own $I_{\text{pred}}^{\text{new}}$,
paid for by dissipation at the new level. (d) Symbiotic systems — plant–mycorrhiza (Simard et al. 1997; cf. the critical reassessment of Karst et al. 2023),
coral–zooxanthellae — set up a test bench for the discipline of the conventionality of the boundary of § 2.2: whose $\eta_v$ grows under
symbiosis, how the sign depends on the choice of boundary between partners, under what conditions the symbiotic loop forms a
new subject of self-payment. (e) Bioelectric morphogenesis (Levin 2019) — bioelectric patterns as $M_X$
(the physical realization of the model of morphology), paid for by ionic currents through cell membranes — gives a direct
candidate for $\eta_v$-measurement in the morphogenetic field. The power-law dependence of the rate of evolutionary adaptation on
$\eta_v$ (Prediction 1, § 5) is testable on a single microbial line in ordinary experimental evolution, without requiring an
astrobiological or AI context, and constitutes the program's central empirical prediction for
theoretical biology.

*Speculative consequences (astrobiology, AI ethics, demarcation).* Beyond the biological core, the program offers a
reformulation of traditionally metaphysical questions. The search for extraterrestrial life acquires a thermodynamic
requirement of closed self-payment loops on top of the existing chemical biosignatures (a complement to the Ladder of Life
Detection, not a replacement). The ethical status of artificial systems is posed as a question about the appearance of one's own
dissipative payment for the model (alongside the traditional lines of sentience / welfare / functionalism). The boundary between
the structurally complex and the vital receives an operational *necessary* cross-section: $\eta_v > 0$ is a necessary condition of
synchronic vitality (§ 2.7); the upper bound $\eta_v \le 1$ is an **unconditional theorem** (a consequence of the data processing
inequality, § 2.1) for passive self-modeling; the active case (sensorimotor feedback) is an
open problem (directed information, the Sagawa–Ueda 2010 bound). A full definition of life in the sense of the NASA formula (Joyce 1994) also requires
Darwinian dynamics at the population level, and both dimensions — synchronic and diachronic —
are complementary. Each of these reformulations is not an automatic solution of the corresponding question;
it is a pointer to a concrete measurable quantity relative to which the question can be formulated
in a disciplined way.

For theoretical biology, $\eta_v$ opens a quantitative bridge between the tradition of organisational closure
(autopoiesis, M,R-systems) and predictive models of adaptation.

## Author Contributions

Conceptualization, methodology, formal analysis, writing — original draft preparation, writing —
review and editing: A.A. The author has read and agreed to the published version of the manuscript.

## Funding

This research received no external funding.

## Ethics Declarations

Ethics approval, consent to participate, and consent for publication are not applicable: the present work is a
theoretical study with numerical simulations that involved no humans, animals, biological material, or
associated data as subjects.

## Data Availability

No primary empirical data were generated for this work. The reproducible code for the worked examples
(§§ 3.4–3.7, 4.4: *E. coli* chemotaxis, the bimetallic thermostat, synthetic city profiles,
the biosphere-as-compressor, and the LLM-as-corporation) is openly available in the GitHub repository
`andriishin/landauer-self-modeling-oa` (https://github.com/andriishin/landauer-self-modeling-oa) and, together
with the preprint of this manuscript, is archived on Zenodo (DOI: 10.5281/zenodo.21039160).

## Use of AI Tools

In accordance with the Springer Nature editorial policy on AI tools in scholarly writing, AI is not listed as
a co-author, and the author retains full responsibility for all content of the manuscript. In preparing the
present manuscript and the supplementary materials, the author used Anthropic Claude (Opus 4.6, 4.7, 4.8) for
five tasks. (i) Generation and verification of the reproducible Python code for the worked examples
(§§ 3.4–3.7, 4.4; the code is in the data repository, see the "Data Availability" section). (ii) Cross-checking
of bibliographic metadata against local copies of the cited sources. (iii) Editorial revision of
human-generated text at the level of readability, grammar, and style (copy-editing); per the Springer Nature
guidance, such use does not require a separate declaration but is noted here for full transparency.
(iv) Translation of the manuscript and the supplementary materials (including the accompanying code README)
from the Russian source into English — the journal's submission language — followed by terminological and
stylistic revision; the author verified the translation and bears full responsibility for it. (v) Assistance
in deriving and verifying the formal apparatus (the derivation of the bound $\eta_v \le 1$ as a consequence of
the DPI and of the thermodynamic Still bound (2)) under the author's direction; the author independently
verified all proofs and bears full responsibility for them. All scientific claims — the formulation of
$\eta_v$, the self-payment requirement, the diagnoses of the paradigm cases, and the falsification criteria —
were conceived by the author; their formal rendering was carried out with AI assistance under the author's
supervision. The AI tools did not generate scientific content autonomously. The author verified every
AI-assisted fragment and accepts full responsibility for the content of the manuscript and the supplementary
materials.

## Competing Interests

The author declares no relevant financial or non-financial interests that could be perceived as influencing
the content of this article (over the three years prior to manuscript submission).

## References

The reference list is generated automatically from `paper/refs.bib` at LaTeX compilation time by the Springer
bibliography processor in the **author–year** style (`sn-mathphys-ay.bst` or the journal's Author-Year style).
In-text citations follow the author–year convention (`Author Year`; `Author and Coauthor Year`;
`Author et al. Year`), and the list is ordered **alphabetically by the surnames of first authors**, as required
by the submission rules of *Theory in Biosciences*.

