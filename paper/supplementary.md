<!--
  Supplementary Materials for the article «Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality».
  Extended discussions, full counterfactual analyses, and sensitivity analyses moved out of the main text.
  Cross-references in the main text take the form «see Supplementary § SX.Y».
-->

# Supplementary Materials for «Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality»

This document collects the extended materials that are not included in the main text in order to respect the length corridor. It contains expanded material on selected points of the main text — § S2.1, § S2.4, § S3.4, § S3.5, § S4.4, § S4.4a, § S4.7, § S4.8, § S4.9 — to which the main text gives explicit cross-references. Convention: each § SX.Y extends main § X.Y. The complete source code of the reproducible computation is in the Zenodo archive (see main § Data availability).

## S2.1 Operationalisation of $I_{\text{pred}}$: full protocol

Direct measurement of $I_{\text{pred}}$ in the sense of formula (1a) of the main text requires access to all internal degrees of freedom of the system and is technically impossible for biological, urban, and space systems. The standardised operationalisation fixes four elements for each class of systems.

(a) *Sensory channel* $x_t$ — the observable input states. For a bacterium, the ligand concentration at the chemotaxis receptors; for a city, the flow of resources through the infrastructure (energy, matter, information); for the biosphere, the flow of solar radiation and the geochemical fluxes.

(b) *Internal channel* $s_t$ — the measurable summaries of the configuration $M_t$. For a bacterium, the methylation level of the adaptation system; for a city, the administrative and infrastructural parameters (density of communications, density of decisions, budget profile); for the biosphere, the atmospheric composition and the biomass pools.

(c) *Choice of past/future windows* with specification of $\tau$. For a bacterium, the characteristic reaction time, of the order of several generations; for a city, a quarter or a year; for the biosphere, a geological eon.

(d) *Method of estimating the mutual information.* Direct computation of $I(s_t; x_{t+\tau})$ requires knowledge of the joint distribution $p(s, x)$, which is unavailable for biological, urban, and space systems. Finite-sample estimators are used; the choice of estimator depends on the nature of the data (discrete/continuous, low-/high-dimensional, sample size $N$). The three classes of methods employed in the present work are as follows.

*Plug-in estimate with bias correction.* The empirical frequencies $\hat p(s, x) = N(s, x)/N$ are substituted into the formula $\hat I = \sum_{s, x} \hat p(s, x) \log[\hat p(s, x)/(\hat p(s) \hat p(x))]$. The principal problem is the systematic overestimation of MI at small samples (*finite-sample bias*) of the order of $(m-1)/(2N \ln 2)$ bits, where $m$ is the number of occupied cells in the histogram. The standard corrections are: **Miller–Madow** (Miller 1955) — adding the term $(m-1)/(2N \ln 2)$ to the naive empirical entropy estimate in order to remove the systematic underestimation, valid when $m \ll N$; **Grassberger–Schürmann** (Grassberger 2003) — an entropy estimate via the digamma function, $\hat H_{\text{GS}} = \log N - \frac{1}{N} \sum_s n_s \psi(n_s)$, which yields a smaller bias at intermediate values of $m/N$. The plug-in estimator is optimal for **discrete biological data** of low/intermediate dimension (receptor methylation statuses, discrete cellular states, $\dim \le 10$, sample $N \sim 10^3$–$10^5$): the naturally discrete nature of the signal, and the absence of binning problems.

*Kraskov–Stögbauer–Grassberger (KSG; Kraskov et al. 2004).* A $k$-nearest-neighbour estimator for **continuous data** that does not require binning. Formula: $\hat I_{\text{KSG}} = \psi(k) + \psi(N) - \langle \psi(n_x + 1) + \psi(n_y + 1) \rangle$, where $\psi$ is the digamma function and $n_x$ and $n_y$ are the numbers of neighbours in the marginal $L_\infty$-neighbourhoods, whose size is set by the $k$-th nearest neighbour in the joint space. It adaptively accounts for the local density of the distribution. The parameter $k$ controls the *bias–variance trade-off*: smaller $k$ → less bias, more variance; the authors' recommendation is $k = 4$. It is applicable to **continuous time series of intermediate dimension** ($\dim \le 50$), sample $N \sim 10^3$–$10^6$ — the standard for neurophysiological, physiological, and econometric time series.

*Mutual Information Neural Estimation (MINE; Belghazi et al. 2018).* It uses the **Donsker–Varadhan dual representation** of the KL divergence: $I(X; Y) = \sup_T \{\mathbb{E}_{p_{XY}}[T(x, y)] - \log \mathbb{E}_{p_X \otimes p_Y}[\exp T(x, y)]\}$, where the supremum is taken over all measurable functions $T: \mathcal{X} \times \mathcal{Y} \to \mathbb{R}$. The function $T$ (the "critic") is parameterised by a neural network and is trained by stochastic gradient descent over mini-batches, with the identity that the MI equals the lower bound for any $T$. It is applicable to **high-dimensional continuous data** (images, LLM embeddings, dimension $> 10^2$), where KSG suffers from the curse of dimensionality (the volume of the $L_\infty$-neighbourhood grows as $r^d$, and the density estimate via kNN degrades). The price is the absence of guarantees of exact convergence when the critic is undertrained, and substantial computational cost (hours to days on a GPU for a typical sample $N \sim 10^5$, $\dim \sim 10^3$).

**The recommended default method for each class of data is as follows.**

| Data class | Method | Default parameters |
|---|---|---|
| Discrete biological ($\dim \le 10$) | Plug-in with Miller–Madow correction | sanity check via KSG with $k = 4$ |
| Continuous time series ($\dim \le 50$) | KSG | $k = 4$ |
| High-dimensional continuous ($\dim > 10^2$) | MINE | critic — MLP with 3 hidden layers of 512 neurons each, training $\ge 10^4$ batch updates |

**Sensitivity diagnostics.** When two methods diverge by more than 30% on the same sample, vary the estimator-specific parameters:

- *KSG:* vary $k \in \{3, 5, 8, 10\}$ and check for a *plateau* — a stable value of the estimate in the intermediate range of $k$. The absence of a plateau (a monotonic drift of the estimate with $k$) indicates an insufficient sample size or a strong local inhomogeneity of the density.
- *Plug-in:* vary the bin size in the binning of continuous data, and compare the Miller–Madow and Grassberger–Schürmann corrections. A divergence between the corrections of $> 10\%$ is a signal that $m/N$ is too large and that KSG or MINE is needed.
- *MINE:* vary the critic architecture (number of layers, width), check the *convergence of the bound* over training epochs (a stable value in the last $\sim 10^3$ batch updates), and the regularisation (gradient clipping against the blow-up of the gradients in the exp term). A non-converging bound, negative estimates, or a strong dependence on the random seed are a signal to change the architecture or to switch to KSG for the lower-dimensional subprojections.

For systems with active sampling (a bacterium with motor feedback on the gradient, a city with administrative intervention), the operational MI estimate is carried out at a fixed policy $\pi$: $I_{\text{pred}}(\pi) = I(s_t; x_{t+\tau} \mid \pi)$. Without conditioning, the DPI inequality $I(s_t; x_{t+\tau}) \le I(x_{t-\tau:t}; x_{t:t+\tau})$ is not guaranteed, and the MI estimate would mix predictive information with the effect of active control (see main § 2.1, the DPI condition).

The proxies are not the definition of $I_{\text{pred}}$ — they are an operationalisation. The same discipline operates in standard physical measurement practice: temperature is measured not by directly counting molecular velocities, but through a calibrated proxy — the expansion of mercury. A divergence between different proxies for the same system is a signal to refine the proxy, not to abandon the concept.

*Why predictive, and not stored information.* The precedent for the thermodynamic connection of predictive information with dissipation is set in the work of Still, Sivak, Bell, and Crooks on the thermodynamics of prediction (Still et al. 2012). There the term **nostalgia** is introduced for the past information that is uselessly retained by the system and has no predictive power: $I_{\text{nostalgia}} := I_{\text{stored}} - I_{\text{pred}} \ge 0$ by DPI; equality is attained when the internal statistic $M_t$ is minimally sufficient for prediction (the Information Bottleneck (Tishby et al. 1999) optimum). Still et al. show that $I_{\text{nostalgia}}$ sets a lower bound on the total dissipation of the system. In a non-stationary environment the gap $I_{\text{nostalgia}} > 0$ is typical and is associated with excess dissipation; in a stationary environment with fixed $M < \infty$ the gap persists, but is bounded above by the memory capacity (Still et al. 2012). The present framework inherits Still's precedent and adds a key requirement: both the numerator and the denominator of $\eta_L$ refer to one and the same physical system — the model and the dissipation belong to $X$. This requirement of self-payment separates $\eta_L$ from the classical setting of the thermodynamics of prediction, where the model and the dissipator may be distinct circuits.

### The stationary-erasure lemma: full proof

Main § 2.1 contains an informal summary of the Lemma and a brief formal statement with two parts (the flux bound and the sink bound), plus a dense meta-paragraph on the relation between what is proved and what is postulated. Here we give the full proof sketch with a detailed treatment of the algorithmic part (steps (i)–(iii), (v)) and a discussion of the postulate of stationary accounting (step (iv)).

**Conditions of the Lemma.** $X$, in a stationary ergodic regime, retains predictive information $I_{\text{pred}}$ over a window $\tau$; the system's memory is finite ($M < \infty$ bits); the flux of new predictive information is strictly positive ($\dot{I}_{\text{pred}} > 0$). The Lemma contains two logically independent bounds.

**Part (a): the flux bound (reference).** The rate of predictive updating is bounded above by the entropy rate of the source: $\dot I_{\text{pred}} \le h_\mu$, where $h_\mu$ is the entropy rate of the source. A direct consequence of the data processing inequality with $M_t = f(X_E^{(-\infty, t]})$ as a function of the past sensory channel, and of stationarity (with conditioning on the policy in the case of active sampling — see below). Equality is attained in the limit of optimal prediction, when all of the source entropy is predictively relevant. An i.i.d. source (independent and identically distributed — a sequence of independent identically distributed samples, in which the past carries no information about the future) realises the opposite limit: $h_\mu > 0$ at $I_{\text{pred}} = 0$ and $\dot{I}_{\text{pred}} = 0$. Bound (a) is a reference upper estimate on $\dot I_{\text{pred}}$ for the connection with the classical line of Bialek–Nemenman–Tishby (Bialek et al. 2001); **it is not used in the derivation of the lower bound on dissipation** and is given only for context.

**Part (b): the sink bound (central).** When $M < \infty$ and the entropy flux through the system over the window $\tau_d$ is positive — under the truth of the postulate of stationary accounting (step (iv) below) — the obligatory erasure is $\ge I_{\text{pred}}$ bits and the dissipation is $\ge I_{\text{pred}} \cdot k_B T \ln 2$ of free energy. The sink bound is conditional. The algorithmic part (steps (i)–(iii)) proves that the memory must release $\dot I_{\text{pred}}$ bits per unit time. The transition from this release to the Landauer cost (step (iv)) is accepted as the postulate of stationary accounting, in the absence of global reversible uncomputation (Bennett uncomputation) (Bennett 1973, 1982).

*Proof sketch of (b):*

(i) Stationarity of the distribution.

(ii) With the choice of window $\tau = \tau_d$, the identity $\dot I_{\text{pred}} \cdot \tau_d = I_{\text{pred}}$ holds by the definition of $\tau_d$ — this is a renaming, not a substantive step. Ergodicity ensures the existence of stationary values of both quantities.

(iii) *Algorithmic lower bound on the memory content.* The connection of the Shannon mutual information $I_{\text{pred}}$ with the algorithmic complexity of $M_t$ requires two steps. **Step 1** (Shannon level): by the inequality $I(X; Y) \le \min(H(X), H(Y))$, where $H(\cdot)$ is the Shannon entropy of a discrete random variable ($H(X) = -\sum_x p(x) \log_2 p(x)$, in bits with the base-2 logarithm; Shannon 1948), we have $H(M_t) \ge I(M_t; X_E^{[t, t+\tau_d]}) = I_{\text{pred}}$. **Step 2** (algorithmic lower bound on $M_t$): the standard connection between the average Kolmogorov complexity and the Shannon entropy of the source (Cover and Thomas 2006; Li and Vitányi 2008) gives
$$\langle K(M_t) \rangle \ge H(M_t) + O(\log) \ge I_{\text{pred}} + O(\log)$$
for typical realisations of the memory state, where $\langle \cdot \rangle$ is the average over the invariant measure $\mu$ of the source. The lower bound $\langle K(M_t)\rangle \ge H(M_t) - O(1)$ is the standard coding-theory inequality (the expected Kolmogorov complexity is not below the entropy, up to an additive constant); the second inequality is Step 1 (DPI). The load-bearing derivation of the memory lower bound does not use the Brudno equality: it relies only on $H(M_t) \ge I_{\text{pred}}$ (Step 1) and on this standard coding inequality. Notational clarification: $O(\log)$ is a correction of the order of $\log \tau_d$ (a term bounded above by $C \cdot \log \tau_d$ for some constant $C$), associated with the algorithmic description of the decompressor itself. Accordingly, the minimal physical representation of $M_t$ requires no fewer than $I_{\text{pred}}$ bits of memory.

**The Brudno bridge (to the $h_\mu$ scale, part (a)).** Separately from the derivation of the memory lower bound, by Brudno's theorem (1983) for an ergodic source with $h_\mu > 0$, a typical trajectory has Kolmogorov complexity $K(\cdot)$:
$$K(X_E^{[t-\tau_d, t]}) = h_\mu \cdot \tau_d + o(\tau_d) = H(X_E^{[t-\tau_d, t]}) + o(\tau_d)$$
for $\mu$-almost all trajectories. Notational clarification: $o(\tau_d)$ is the standard Landau notation for a term with $o(\tau_d)/\tau_d \to 0$ as $\tau_d \to \infty$, i.e., a term that is asymptotically small compared with the window length. This equality connects the algorithmic complexity of the *source* trajectory with the entropy rate $h_\mu$ and serves as a bridge to the classical Bialek–Nemenman–Tishby scale (part (a) of the Lemma), not as a premise of the derivation of the lower bound on the memory $M_t$. When $M < \infty$ and there is a stationary inflow of new predictive information at a rate $\dot I_{\text{pred}} > 0$, the memory capacity saturates in a time $\sim M/\dot I_{\text{pred}}$; further operation of the channel requires the release of **no fewer than** $\dot I_{\text{pred}}$ bits of predictively relevant information per unit time (more may arrive — non-predictive noise is also subject to erasure, which only strengthens the result).

(iv) *The postulate of stationary accounting.* The release in (iii) is realised as Landauer erasure of $\ge I_{\text{pred}}$ bits over the window $\tau_d$ in any realisation that does not use global reversible uncomputation (Bennett 1973, 1982). The Bennett route is not formally forbidden. Bennett's time/space trade-off (1989) gives: any irreversible computation requiring time $t$ (number of logical steps) and memory $S$ (bits) is emulated reversibly with memory $S_R \sim S(1 + \log(t/S))$ at time $T_R \sim t^{1+\epsilon}/S^\epsilon$, where $S_R$, $T_R$ are the memory and time of the reversible simulation and $\epsilon > 0$ is a free, arbitrarily small parameter (smaller $\epsilon$ — faster, but with a larger time prefactor). In substance: a logarithmic growth of the simulation memory, unbounded as $t \to \infty$ at fixed $M$. Sagawa and Ueda (2010) and Parrondo et al. (2015) formalise the generalised second law $\langle\Sigma\rangle \ge -\langle\Delta I\rangle$ for feedback-controlled systems (Sagawa and Ueda 2009 — the special case of the measurement + erasure cost). This same framework points to a potential counterexample to the bound: erasing memory *correlated* with the environment is admissible at a cost $\langle W \rangle \ge k_B T(\Delta S - I_{\text{meas}})$, i.e. below $k_B T \ln 2$ per bit. Since the retained predictive memory is correlated with the environment by construction ($I_{\text{pred}} = I(M_t; X_E) > 0$), such a channel could in principle give $N_{\text{max}} < I_{\text{pred}}$ and $\eta_L > 1$. The mechanism, however, requires a controller that *first* measures the correlated reference, acquiring $I_{\text{meas}}$; by the measurement–erasure symmetry (Sagawa and Ueda 2009) that measurement itself costs $\ge k_B T \cdot I_{\text{meas}}$, so that over a full stationary cycle (acquiring the correlation plus spending it on cheap erasure) the total dissipation remains $\ge k_B T \ln 2$ per bit. In the self-payment loop the accounting is internal: there is no external demon with free access to the correlation, and $I_{\text{pred}}$ is itself maintained by the same self-paid budget, so the correlation in the numerator cannot simultaneously be spent to cheapen the denominator without double-counting (a Maxwell demon inside a closed system). The stationary-accounting postulate formalises precisely this closure of the cycle; the conditional status of the bound is thereby preserved. However, the complete accounting of an arbitrary refresh channel $M_t \to M_{t+1}$ at $M < \infty$ and $\dot I_{\text{pred}} > 0$ is an open technical problem. In the present work, the transition from (iii) to the Landauer cost is accepted as the **postulate of stationary accounting**. Statement: at $M < \infty$ and $h_\mu > 0$, outside the global Bennett asymptotics, the refresh channel dissipates no fewer than $\dot I_{\text{pred}} \cdot k_B T \ln 2$ of free energy per unit time. What is erased are the old memory elements — typically *nostalgia* bits in the sense above, not the predictive bits themselves. The boundary case of a globally reversible realisation is separated by the regime caveat *Bennett regime and redefinition of the scale* in main § 2.1, and is explicitly transferred to condition (c) of the Domain-of-Definition Statement.

(v) Lower bound on a single erasure (Landauer 1961). Under the truth of the postulate of stationary accounting (iv), the total dissipation over the window $\tau_d$ amounts to $\ge I_{\text{pred}} \cdot k_B T \ln 2$, and $\eta_L \le 1$.

For non-stationary systems with growing memory (the biosphere, a learning artificial system), the lemma requires accounting for the cost of retaining the old information, of expanding the memory, and of absorbing the new; the complete sum with the Landauer bound is an open technical problem. The context of more general results is Sagawa and Ueda (2010), Parrondo et al. (2015), Still et al. (2012).

**Extended status of the Lemma.** Part (a) of the Lemma and steps (i)–(iii), (v) of part (b) are demonstrative. Steps (i)–(ii) are identities by the definition of $\tau_d$ and stationarity. Step (iii) is an *asymptotic* consequence relying on (1) the Shannon-level inequality $H(M_t) \ge I(M_t; \cdot) = I_{\text{pred}}$ (DPI) and (2) the standard coding-theory lower bound $\langle K(M_t)\rangle \ge H(M_t) - O(1)$ (Cover and Thomas 2006; Li and Vitányi 2008) to the effect that the expected Kolmogorov complexity is not below the entropy. The Brudno equality (1983) on the coincidence of the average Kolmogorov complexity and the entropy rate of the source enters separately — as a bridge to the $h_\mu$ scale (part (a) of the Lemma), not as a premise of the derivation of the memory lower bound. The relation $\langle K(M_t)\rangle = H(M_t) + O(\log)$ holds for typical realisations of the memory state; a formal accounting of the admissible memory-compression regimes is beyond the scope of the present work. Step (v) is the classical Landauer principle. **What remains substantively unproved is step (iv)** — the transition from "the memory must release $\dot I_{\text{pred}}$ bits per unit time" to "this release is realised precisely as Landauer erasure, not as reversible uncomputation." The current literature formalises this for feedback-controlled systems (Sagawa and Ueda 2010; Parrondo et al. 2015) and for the time/space trade-off of reversible simulation (Bennett 1989), but not for an arbitrary refresh channel in the stationary regime. In the present work, step (iv) is accepted as the **postulate of stationary accounting** and is fixed in condition (c) of the Domain-of-Definition Statement. Accordingly, $\eta_L \le 1$ is a conditional statement: a consequence of the Landauer principle under the truth of postulate (iv), not an unconditional theorem. The proof of (iv) for an arbitrary refresh channel is deferred to the open-problems section (main § 5).

**Bennett regime and redefinition of the scale: extended discussion.** Main § 2.1 contains a condensed scope statement on the Bennett regime. The full argument: for systems in the Bennett asymptotics of reversible computation (Bennett 1973, 1982), the cost per bit drops below Landauer, and $N_{\text{max}}$ loses its interpretive meaning. As $E_{\text{actual}} \to 0$ and $I_{\text{pred}}$ finite, the ratio $\eta_L$ formally diverges. In the Bennett regime, the scale is redefined through the number of logical, rather than erased, bits — an operationally different quantity requiring separate calibration. In the present work, we remain in the irreversible regime as the standard idealisation of biological and engineered systems.

A direct consequence for main § 5 (Falsification Criteria): a "violation of the Landauer lower bound" refutes the framework only in the irreversible regime. The detection of a system in the Bennett regime points to the boundary of the domain of definition, not to a refutation of the programme. The corresponding operationalisation (a test for $\dot Q > 0$ as a marker of the irreversible regime, conversion to the number of logical bits upon detection of the Bennett asymptotics) is a task for additional research, not covered by the present work. The Bennett regime as "does not serve as a refuting scenario" is fixed in main § 5, Block 1, item 1.
## S2.4 Cohort normalisation: extended discussion and the sigmoid alternative

### Extended discussion of reference cohorts

The specific reference cohorts for the six paradigm cases of Section 3 are fixed as follows.

*Bacteria* (§ 3.5): a cohort of prokaryotic chemotactic systems, $n \sim 200$ from BiGG/KEGG models (*E. coli*,
*B. subtilis*, *V. cholerae* and the like).

*Cities* (§ 3.6): 120–500 large cities from the Bettencourt dataset (Bettencourt et al. 2007).

*Biosphere* (§ 3.7): the only case for which percentile normalisation is impossible owing to the absence of a cohort.
In its place, normalisation by a theoretical upper bound is used. The biosphere-as-a-whole is normalised through the specific exergy flux: NPP $\sim 10^{14}$ W divided by the total living biomass $\sim 5 \cdot 10^{14}$ kg (Bar-On et al. 2018) → specific $P_D \sim 0.2$ W/kg as the normalisation scale $T_v^{\text{ref}}$. Alternatively: for the biosphere-as-a-whole, normalisation through the $N_{\text{max}}$-equivalent over the window $\tau_{\text{year}}$ (see § 3.7).

*Large language model* (§ 3.4): a cohort of the latest generations of foundation models, $n \sim 50$ from the year 2020.

*Stars* (§ 3.1): a main-sequence cohort, $n \sim 10^4$ from the Hipparcos catalogue.

*Crystal and hurricane* (§§ 3.2–3.3): normalisation to zero. The structural zero $T_v = 0$ or $C_v = 0$ is set not by the
position within a cohort but by the constructive failure of the corresponding capacity (absence of intrinsic dissipation paying for
maintenance; absence of retained predictive information). Formally: $\tilde{T}_v(X) := 0$ is adopted by convention
for $X$ with $T_v(X) = 0$, and $\tilde{T}_v(X) := 1$ for $X$ with $T_v(X) \ge \max_{\text{cohort}} T_v$; within the carrier of the
reference cohort, formula (2a) of the main text applies.

### The sigmoid alternative

An alternative to percentile normalisation is the sigmoid normalisation $\tilde{T}_v = T_v / (T_v + T_v^{\text{ref}})$ through an
independent choice of the reference value $T_v^{\text{ref}}$ for each capacity. The sigmoid procedure yields an absolute
scale and is applicable to unique systems, but it requires justifying $T_v^{\text{ref}}, C_v^{\text{ref}}, S_v^{\text{ref}}$
from independent physical considerations. In the present work, the percentile procedure is used. The sigmoid one is retained
as an alternative for applications that require an absolute scale or that work with unique systems.

### Worked example: $I_v$ for *E. coli* by percentile normalisation

An illustrative step-by-step calculation of $I_v(\textit{E. coli})$ closes the gap between the formal definition (2)–(2a)
of the main text and the operational procedure. The calculation is given as a **worked example, not a calibrated measurement**:
the numbers are a methodological illustration of the procedure, consistent with the value stated in § 3.5, "$I_v \sim 0.5$ by the percentile
of the cohort of prokaryotic chemotactic systems," and are not independent empirical claims.

*(a) The $T_v$ proxy — specific exergy flux $P_D \cdot \eta_{\text{ex}}$ in W/kg.* The heat output of *E. coli* in the
stationary phase is $\sim 1$–$3$ pW/cell (Liu et al. 2020), the dry cell mass is $\sim 3 \cdot 10^{-13}$ g, $P_D \sim 3$–$10$
W/kg. With an exergetic efficiency $\eta_{\text{ex}} \sim 0.4$, the specific exergy flux $P_D \cdot \eta_{\text{ex}} \sim 1$–$4$
W/kg — the proxy for $T_v(\textit{E. coli})$.

*(b) Distribution of the proxy across the cohort.* The cohort of prokaryotic chemotactic systems — $n \sim 200$ from BiGG/KEGG.
The heat output varies from $\sim 0.1$ pW/cell in autotrophic chemolithotrophs with slow metabolism
(*Nitrosomonas*, methanogens) to $\sim 10$ pW/cell in fast-growing heterotrophs (*V. natriegens*). The specific exergy
flux at a comparable cell mass yields a distribution of $P_D \cdot \eta_{\text{ex}}$ with a median of $\sim 1$ W/kg and an
interquartile range of $[0.3;\, 3]$ W/kg.

*(c) The rank of *E. coli* in the distribution.* At $P_D \cdot \eta_{\text{ex}}(\textit{E. coli}) \sim 2$ W/kg, the rank falls into the
upper-middle part of the distribution, $\tilde{T}_v \approx 0.6$.

*(d) The $C_v$ and $S_v$ proxies.* $\tilde{C}_v$ — the normalised excess entropy $E$ (Crutchfield and Feldman 2003) or statistical complexity $C_\mu$ (Shalizi and Crutchfield 2001) on the time series of methylation (see main § 2.3: LZ complexity belongs to the class of entropy-rate proxies $h_\mu$, not $I_{\text{pred}}$; for $C_v$ as a measure of model quality, $I_{\text{pred}}$-class proxies are required). For *E. coli*, with its adaptive reactivity to chemical gradients, the proxy
is estimated somewhat above the cohort median, $\tilde{C}_v \approx 0.55$ — an illustrative point; the formal distribution of excess entropy across the cohort of $n \sim 200$ requires separate work. $\tilde{S}_v$ — the Leiden modularity of the
chemotactic-regulation network (Tar–CheA–CheY–FliM–motor axially symmetric assembly); the architecture is
hierarchically modular, $Q \sim 0.5$ by the Leiden algorithm (Traag et al. 2019), which in the cohort distribution yields
$\tilde{S}_v \approx 0.4$.

$\tilde C_v$ and $\tilde S_v$ for *E. coli* are given as illustrative points in the cohort of $n \sim 200$ prokaryotic chemotactic systems (BiGG/KEGG); the full distribution of excess entropy / Leiden $Q$ across this cohort is an open operationalisation problem not included in the present worked example. The numerical illustration is methodological, not a calibrated measurement.

*(e) Geometric mean.* $I_v = \sqrt[3]{0.6 \cdot 0.55 \cdot 0.4} = \sqrt[3]{0.132} \approx 0.51$ —
consistent with the value stated in § 3.5, "$I_v \sim 0.5$." The sensitivity to the choice of proxy within a single class is estimated
by varying each $\tilde{\cdot}_v$ within a range of $\pm 0.1$: the resulting $I_v$ remains within the corridor $[0.4;\, 0.6]$,
and the width of the corridor is an indicator of the stability of the percentile procedure within the carrier of the reference cohort.

The epistemic status of each number is illustrative. An analogous step-by-step calculation for the remaining five paradigm cases
would require fixing a cohort with equal discipline, which is beyond the scope of the present work; the paradigm-case values of $I_v$ in
§ 3 are order-of-magnitude estimates, methodologically consistent with the present worked example.

## S3.4 Counterfactual ablation of the LLM: full component-by-component analysis

Let us apply the counterfactual procedure of § 2.2 of the main text to a concrete case of a large language model. The candidates for
inclusion in the boundary are examined sequentially.

*Parametric weights (static after training).* Subtraction: the model does not respond; a clean failure of the loop. They belong to the
boundary of the generator but do not belong to the working circuit at the moment of inference (the weights are not updated by error).

*KV-cache (context memory during execution).* Subtraction: the model loses the context of the conversation; over a window $\tau \sim$ session duration,
$\Delta(-dF_X/dt) > 0$. Belongs to the boundary on session timescales.

*Executing server (GPU + OS).* Subtraction: computation is impossible. Belongs to the boundary of the mechanism, but the energy is supplied by
the external power grid.

*Owner corporation (making decisions about training, deployment, payment).* Subtraction: the model in its current form ceases to be
updated (no new versions), but the current version continues to operate on the residual infrastructure. An external component
relative to the current version of the model; it is included in the boundary when considering the evolution of the model lineage over time.

Counterfactual ablation distinguishes four nested boundaries $B_1 \subset B_2 \subset B_3 \subset B_4$ (see main § 3.4). For $B_1$ (weights only) and $B_2$ (weights + KV-cache + server) on the session window, $\eta_L^{\text{int}}$ is **undefined** through the simultaneous failure of $T_v^{\text{int}}$ (the power grid is external, $E_{\text{actual}}^{\text{own}} = 0$) and $C_v^{\text{int}}$ (there is no channel returning the error into the working circuit). For $B_3$ (the training pipeline: dataset + GPU farm + RLHF operators) on the model-generation window, the decision loop closes on the corporate operators, $\eta_L$ is positive, but the subject is the pipeline, not the model. For $B_4$ (the corporation as a legal entity), $\eta_L^{\text{corp}} \lesssim 10^{-25}$ as an **upper bound** through the capacity-bound on the numerator ($I_{\text{cap}}^{\text{corp}} \lesssim 10^{12}$ bits as an upper estimate of $I_{\text{pred}}$, not a measured predictive information). Counterfactual ablation thus does not grant the LLM
vital status on any of the chosen scales. It operationalises the intuition on which the diagnosis of
§ 3.4 of the main text rests: widening the boundary widens the responsible subject (model → pipeline → corporation) without dissolving the diagnosis.

## S3.5 Worked example, E. coli: detailed sensitivity analysis

### Full calculation parameters

*Numerator.* The sensory channel $x_t \in \{0, 1\}$ — the binarised sign of the temporal gradient of aspartate concentration
(positive/negative) with a step $\delta t \sim 0.1$ s (the characteristic response time of a single receptor cluster).
The internal channel $s_t \in \{0, 1, 2, 3, 4\}$ — the number of methyl groups on a Tar receptor (the five discrete states
of the adaptation system). The prediction window $\tau \approx 10$ s — the characteristic adaptation time of the methylation system.
The transition probabilities $P(s_{t+\delta t} \mid s_t, x_t)$ are given analytically in the model of Tu et al. (2008)
(Tu et al. 2008; Shimizu et al. 2010) on the stationary distribution of the Markov process. Alternatively, $I(s_t; x_{t+\tau})$
is estimated numerically through the KSG (Kraskov–Stögbauer–Grassberger) estimator on simulated trajectories.

For a single measurement channel within the window $\tau$, one obtains $I_{\text{pred}} \approx 1$–$2$ bits per measurement (Mehta and Schwab 2012; Cheong et al. 2011) —
an order of magnitude consistent with the information-theoretic analysis of biochemical signalling. Integration over $\sim 10^3$–$10^4$ measurements/receptors yields $10^3$–$10^4$ bits per generation. A typical *E. coli* carries
$\sim 7000$ chemoreceptors (Tar+Tsr+Trg+Tap+Aer), organised into $\sim 10^3$ clusters with allosteric
coupling (Monod–Wyman–Changeux-like organisation). The upper bound under the assumption of channel independence
is $I_{\text{pred}} \sim 10^3$–$10^4$ bits per generation; **cooperative coupling within clusters
reduces the actual $I_{\text{pred}}$ by $\sim 1$ order of magnitude** (see main § 3.5), which is included in the lower
bound of the sensitivity interval $[10^{-9}, 10^{-7}]$ of the resulting $\eta_L$. A policy-conditioned
MI estimate for the chemotactic cascade taking receptor clusters into account is an open
problem (Tostevin and ten Wolde 2009; Govern and ten Wolde 2014).

*Denominator.* The heat output of *E. coli* in the stationary growth phase is $\sim 1$–$3$ pW per cell
(Liu et al. 2020). Over a generation $\tau_d \sim 30$ min $\approx 1.8 \cdot 10^3$ s, the total
heat output is $Q_{\text{heat}} \sim 10^{-9}$ J/cell (an order-of-magnitude estimate).
The exact substitution $2 \cdot 10^{-9}$ gives $N_{\text{max}} \approx 6 \cdot 10^{11}$, but
for consistency with the rounded numbers of main § 3.5 the order $10^{-9}$ is adopted here. By § 2.1
of the main text, $E_{\text{actual}}$ is the free energy supplied over the window $\tau_d$, which in the stationary phase
equals the total integral dissipation. At small $\eta_{\text{ATP}}$ over the generation window, calorimetry
provides a good approximation of the supplied exergy: $E_{\text{actual}} \approx Q_{\text{heat}} \sim 10^{-9}$ J/cell
(the overall energy balance $E_{\text{actual}} \approx Q_{\text{heat}}/(1-\eta_{\text{ATP}})$ in
the limit $\eta_{\text{ATP}} \to 0$ of the stationary phase). At $T = 310$ K, $k_BT\ln 2 \approx 3 \cdot 10^{-21}$ J:

$$N_{\text{max}} = \frac{E_{\text{actual}}}{k_B T \ln 2} \sim \frac{10^{-9}}{3 \cdot 10^{-21}} \sim 3 \cdot 10^{11} \;\text{bits per cell}.$$

This is the first, *exergetic*, bound: the number of bits that the cell could theoretically erase if all of its
free energy went into irreversible information operations. In reality, only a small fraction of the exergy — of order $10^{-3}$,
as the ratio of the power of the sensory-computational network (Mehta and Schwab 2012) to the total metabolic budget of the cell
(Liu et al. 2020) — is directed into irreversible information operations; the rest goes into biomass synthesis,
the maintenance of ion gradients, and thermal losses. The corresponding *computational* bound:
$E_{\text{comp}} \sim 10^{-3} \cdot E_{\text{actual}} \sim 10^{-12}$ J/cell and
$N_{\text{max}}^{\text{comp}} = E_{\text{comp}}/(k_B T \ln 2) \sim 3 \cdot 10^{8}$ bits/cell.

### Sensitivity analysis

The window $\tau$ is varied over the range $1$–$100$ s — this shifts $I_{\text{pred}}$ by $\pm 1$ order of magnitude. On short windows
the Markov model yields less information; on long ones it saturates owing to the limit set by adaptation memory.

The binning of $x_t$ (binary versus 4-level) changes $I_{\text{pred}}$ by $\sim 30\%$ — substantially less than the
uncertainty in the number of receptor clusters.

Including all five receptor families (Tar, Tsr, Trg, Tap, Aer) scales $I_{\text{pred}}$ approximately linearly with the
number of sensors, leaving $\eta_L$ within one order of magnitude.

The estimate of $\eta_{\text{ATP}}$ ($< 0.1$ over the generation window per the bioenergetics literature) changes $E_{\text{actual}}$ by $\sim 10\%$ — not an order of magnitude.

The resulting conservative estimate accounting for all sources of uncertainty:
$\eta_L \in [10^{-9}, 10^{-7}]$ through the exergetic denominator and
$\eta_L^{\text{comp}} \in [10^{-6}, 10^{-4}]$ through the computational denominator.

### Bottleneck of the calculation

The bottleneck is the estimation of $I_{\text{pred}}$ for the full sensory system: the number of receptors in clusters varies across
different strains and conditions and is taken here from literature estimates, not from first principles. The exact value requires
simultaneous MI measurements on all known sensory channels of a single population, which defines the content of
the accompanying experimental programme. The full reproducible calculation with code is provided as part of the Supplementary
Materials (Python sources, saved outputs, parameter documentation).
## S4.4 Counterfactual ablation of the thermostat: full component-by-component analysis

We apply the counterfactual procedure of § 2.2 to a bimetallic thermostat $X$ with hysteresis $\Delta T_{\text{hyst}} = 1$ K,
controlling a room with thermal inertia $\tau_{\text{room}} \sim 30$ min. The candidates for inclusion in the boundary of $X$
are examined one by one.

*Bimetallic strip (sensor and actuator).* Ablation: the loop is broken, no regulation whatsoever.
$\Delta(-dF_X/dt) > 0$ on timescales $< \tau_d$. Belongs to the boundary.

*Relay contact set (energy switching).* Ablation: the same — the loop is broken. Belongs to the boundary.

*Heating element (the actuating link, powered by the external electrical grid).* Ablation: the heat source
disappears; the bimetallic strip and the relay remain. However, $-dF_X/dt$ of the remaining system tends to zero not through a failure of the loop
but through exhaustion of its own free energy (the bimetallic strip slowly cools to the ambient). It does not belong to the decision-making loop; an external component.

*Electrical grid as current source.* Analogous to the heater: external.

*Setpoint operator (external operator).* Ablation: the setpoint is held fixed, regulation is preserved. External.

The boundary of the thermostat under counterfactual ablation is {bimetallic strip, relay}. Within this boundary $\dot{E}_{\text{actual}} \sim 10^{-6}$ W — elastic relaxation of the metal plus dissipation in the relay. Over the window $\tau_d \sim 30$ min $\approx 1.8 \cdot 10^3$ s: $E_{\text{actual}} = \dot{E}_{\text{actual}} \cdot \tau_d \sim 2 \cdot 10^{-3}$ J. The temperature of the receiving heat bath is room temperature, $T \approx 300$ K; $k_B T \ln 2 \approx 3 \cdot 10^{-21}$ J/bit; $N_{\text{max}} \sim 6 \cdot 10^{17}$ bits. With $I_{\text{pred}} \approx 3$ bits for the trivial task of "holding the bimetallic strip's own shape" under a diurnal $\Delta T \sim 10$ K, we obtain $\eta_L^{\text{trivial}} \approx 5 \cdot 10^{-18}$. This is the central estimate; up to $\sim 10^{-17}$ for a seasonal $\Delta T \sim 30$ K and $I_{\text{pred}} \approx 5$ bits. The internal channel that holds predictive information about
the room temperature is the deformation of the bimetallic strip. Estimate:
$I_{\text{pred}} \le \log_2(\Delta T_{\text{room}}/\Delta T_{\text{hyst}}) \approx 3$ bits for a diurnal $\Delta T_{\text{room}} \sim 10$ K (up to $\sim 5$ bits for a seasonal $\Delta T_{\text{room}} \sim 30$ K). The key observation: this $I_{\text{pred}}$ pertains to the environment "room", not to the environment "thermostat +
room + power supply". The loop of decisions paid for by one's own decay is, for the thermostat, incomplete — the heating
of the room is paid for by the external electrical grid, not by the bimetallic strip's own free energy. Counterfactual ablation yields
an $\eta_L^{\text{thermostat}}$ that is undefined in both self-consistent interpretations, but through the failure of different capacities.
In the control task "regulate the room temperature" it is $T_v^{\text{int}}$ that fails: the heating is paid for by the grid,
$E_{\text{actual}}^{\text{own}} = 0$ relative to this task. In the trivial task "hold the bimetallic strip's own
shape" it is $S_v^{\text{int}}$ that fails: the passive thermo-mechanical coupling does not form an error-return loop —
upon a deviation of the strip's shape no dissipation of its own corrects it; the strip simply remains in the new
shape as a function of the current temperature. The divergence between the interpretations does not point to an ontological transition —
Bruineberg et al. (2022) show formally that no such transition can be drawn without a covert smuggling-in of epistemic assumptions. It points
to the conventionality of the choice of boundary as a methodological instrument: one and the same physical
system admits several self-consistent boundaries, and the choice between them is a methodological, not an ontological,
discipline.

## S4.4a Rebutting the critiques of Andrews 2021 and Williams 2020

Well-known critiques of the FEP bear on $\eta_L$ asymmetrically.

Andrews (2021) — "The math is not the territory" — attacks the FEP for the non-derivability of empirical content from
the formalism: without additional hypotheses an $F$ can be constructed post hoc for any system. In $\eta_L$ this critique is rebutted
by anchoring both numerator and denominator to measurable quantities — predictive information via the proxy $C_v$, exergy
via thermodynamic measurements; the freedom of post hoc construction is removed by the requirement of a concrete operationalisation.

Williams (2020) — "Predictive coding and thought" — attacks predictive coding as a neural mechanism, not the FEP
as a principle. This critique is neutral with respect to $\eta_L$: the programme does not assert predictive coding as a mechanism but
uses predictive information as a formal measure, methodologically independent of any particular neural architecture.
Distinguishing predictive coding (Rao and Ballard 1999; Clark 2013 — a neuroarchitectural hypothesis)
from predictive information (Bialek et al. 2001 — an information-theoretic measure) is essential
for a coherent defence of the programme against conflated critique.

## S4.7 Organisational closure: autopoiesis, (M,R)-systems, constraint closure

An objection deserving separate treatment: is self-payment not a rebranding of the classical line of
organisational closure — the autopoiesis of Maturana–Varela, the (M,R)-systems of Rosen, the constraint closure of Mossio–Montévil–Longo,
the epistemic cut of Pattee? The direct answer: the four lines capture different sides of closure at the qualitative level;
$\eta_L$ adds to this tradition one thing — a quantitative thermodynamic discipline through the Landauer budget.
It is neither an alternative nor a replacement, but a separate analytical register laid over the qualitative conceptual work.

Pattee (1982, 2001) introduces the *epistemic cut* as the boundary between the physical-dynamical level and the symbolic
level of a system, and *semantic closure* as the closure of a system upon its own processing of its own symbols.
Hoffmeyer's biosemiotic programme (Hoffmeyer 1996) unfolds this line over the sign processes of the living, casting
semiosis as a constitutive feature of the biological. Our construction of the counterfactual ablation of the boundary (§ 2.2 main) is
a thermodynamic operationalisation of this line: the epistemic cut is drawn not phenomenologically but interventionally,
through distinguishing components by their contribution to the Landauer budget; the biosemiotic territory of sign processes
remains beyond the scale of $\eta_L$.

Maturana and Varela (1980) define an autopoietic system as a network of processes producing components
that recursively realise the same network and determine a topological boundary through their own production. Self-payment
operates in a complementary register: the payment for maintaining predictive information physically belongs to the same system
that maintains the information. Maturana–Varela describe organisational closure qualitatively, through the circular
structure "production of components by components"; self-payment supplies the quantitative thermodynamic part of the same discipline through
a Landauer budget for the maintenance of the model.

The categorial difference of self-payment from autopoiesis: autopoiesis formalises the **component** of closure (production of
components by components); self-payment formalises the **information-thermodynamic identity** of what is maintained and
what is paid for. An autopoietic system can in theory maintain predictive information through an external
thermodynamic supply (maintenance of a cell culture in vitro: metabolically autopoietic, but maintained by an external
supply); $\eta_L$ will withdraw its vital status through the denominator. This is a concrete categorial shift, not merely a
quantitative one.

Rosen's (M,R)-systems (Rosen 1991) are a category-theoretic abstraction of closure with respect to efficient causation:
an organism is a system in which every causal role (Aristotle's efficient cause) is closed within the network. The self-payment of
$\eta_L$ is its thermodynamic reading: closure is realised through the physical loop model↔dissipation, and not through a
categorial abstraction. An important substantive distinction: in *Life Itself* Rosen argues that closure-to-efficient-causation
is non-computable and non-formalisable in machine-theoretic terms. $\eta_L$ does not contradict this claim. It does not
assert that biology is reducible to computation; it asserts that the thermodynamic cost of maintaining a model is a necessary
condition of vitality, formally measurable and not pretending to exhaust the phenomenon of life. The scale fixes one
obligatory thermodynamic cross-section, leaving open the question of the non-computable aspects of organisational closure.

The constraint closure of Mossio–Montévil–Longo (Mossio et al. 2016) captures the closure of biological constraints: each
biological constraint is closed through the production of another constraint, and the network of such constraints is closed upon itself.
Self-payment operates at the level of the information-energy loop (predictive information ↔ Landauer dissipation),
and not at the level of the network of constraints; the constructions are orthogonal, not alternatives. Constraint closure describes the topology
of the mutual production of constraints; self-payment supplies the thermodynamic payment that this topology must defray
through its own decay.

*A differential test of the scale relative to organisational closure.* Consider the pair WT *E. coli* / the minimal cell
JCVI-syn3.0. Both systems are autopoietic in the Maturana–Varela sense, possess (M,R)-closure in Rosen's sense, and constraint closure
in the Mossio–Montévil–Longo sense: the qualitative criteria of organisational closure do not distinguish them. The $\eta_L$ scale yields
a differential result: $\eta_L^{\textit{E. coli}}$ and $\eta_L^{\text{syn3.0}}$ differ by 1–2 orders of magnitude through **both components**. The denominator: $E_{\text{actual}}^{\text{syn3.0}}$ is substantially smaller (a smaller metabolic flux, ~473 genes versus ~4300). The numerator: $I_{\text{pred}}^{\text{syn3.0}}$ is smaller (a sharply truncated sensory repertoire, the absence of two-component chemotactic cascades). $\eta_L$ ranks the systems within the class of organisational closure through the product of the informational and thermodynamic components; the specific sign of the ratio $\eta_L^{\textit{E. coli}} / \eta_L^{\text{syn3.0}}$ is an illustrative estimate from the available literature (Hutchison et al. 2016, for the genome; metabolic calorimetry for $E_{\text{actual}}$), requiring independent empirical verification.

Summary along the closure line. The four conceptual predecessors fix different aspects of closure: epistemic-symbolic
in Pattee, production-component in Maturana–Varela, efficient-causation in Rosen, constraint-network in Mossio–Montévil–Longo.
$\eta_L$ adds to this tradition a quantitative thermodynamic discipline: a Landauer budget for the maintenance of
predictive information in the system's own degrees of freedom. This is not a rebranding of the four lines, but the construction of a
quantitative scale over their qualitative conceptual work. The positional relation is symmetric to the six lines of
§ 4.6 main: each classical programme operationalises one side of the phenomenon; $\eta_L$ collects the thermodynamic payment
into a single measurable quantity, without pretending to replace the corresponding qualitative analytics.
## S4.8 The origin-of-life line and conceptual predecessors

The line of organisational closure (§ S4.7) captures the synchronic aspect of vitality—how an already-formed living system
maintains itself. Running parallel to it is the contemporary research programme on the **origin of life** (OoL), which captures the diachronic aspect—under what conditions a closed loop first arises in a geochemical system.
In Theory in Biosciences and adjacent journals this programme is represented by five relatively autonomous traditions;
each operationalises one side of the abiotic→biotic transition, and each is a conceptual predecessor
of one facet of the $\eta_L$ postulate. This subsection articulates that relationship explicitly—not as a claim to close the
OoL problem, but as a mapping of the place of $\eta_L$ within an already existing field.

*The Eigen–Schuster hypercycle.* The hypercycle (Eigen 1971; Eigen and Schuster 1979) is autocatalytic closure at the level of replicators with an informational template carrier. A set of replicators is organised into a catalytic cycle in which
each member catalyses the replication of the next; closure of the error-return loop occurs through cross-catalytic dependencies among the members of the cycle. **Error catastrophe** (Eigen 1971) marks the threshold between preservation and loss of
information in the replicator loop as the mutation rate increases. This threshold is conceptually homologous to the structural transition
$\eta_L = 0 \to \eta_L > 0$ through the stationary-accounting postulate (§ 2.1 main, step iv): in both cases what is at stake is a threshold below which an information-bearing structure loses the ability to maintain its own model against a noisy channel.
The hypercycle provides a pre-cellular unfolding of the numerator of $\eta_L$: $I_{\text{pred}}$ is encoded in the repertoire of replicators, $T_v$ in the catalytic turnover of the hypercycle, and closure of the error-return loop through cross-catalytic dependencies.
$\eta_L$ supplements the hypercycle with a quantitative Landauer discipline: to the structural condition of replicator closure with a template carrier it adds the requirement that the free energy maintaining this closure be physically
paid for by the system's own catalytic turnover, rather than being subject to purely external driving.

*The Hordijk–Steel RAF networks.* The formalism of reflexively autocatalytic and food-generated (RAF) networks (Hordijk and Steel 2004; Hordijk 2019) describes the conditions under which a set of chemical reactions forms a collectively autocatalytic
closed network over a given food set. Each reaction in the network is catalysed by at least one of its own
products. The entire network can be assembled from the food set in a finite number of steps. RAF is a structural predecessor
of the composite $C_v$ (informational capacity through the topology of the catalytic network) and $S_v$ (systemic capacity as
hierarchical modularity): collective autocatalysis is the structural condition for the emergence of a closed loop.
However, RAF is a criterion of **network closure**, not a criterion of **who pays for its maintenance** in the sense of § 2.1 main. A RAF network
may satisfy the conditions of closure and at the same time be paid for by an external chemical flux, not paid for
by the system's own dissipative work. $\eta_L$ supplements RAF with the thermodynamic discipline of self-payment: to the
structural condition of autocatalytic closure it adds the requirement that the free energy maintaining this
closure physically belong to the network itself.

*England's dissipative adaptation.* The term "dissipative adaptation" was introduced in Perunov, Marsland, and England (2016),
"*Statistical physics of adaptation*" (Phys. Rev. X 6:021036); its statistical-physics basis is England (2013),
"*Statistical physics of self-replication*" (J. Chem. Phys. 139:121923), which derives a lower bound on
heat production for self-replicating systems (through growth rate, internal entropy, durability). The Perunov–Marsland–England formalism describes dissipative adaptation
as a process in which, in systems far from equilibrium subjected to an external driving force,
macrostates that are especially efficient at absorbing and dissipating
energy from the environment become statistically fixed. This is a direct thermodynamic predecessor of the **denominator**
of $\eta_L$—the $T_v$ side of the programme (thermodynamic capacity as the system's ability to participate in non-equilibrium
exchange). However, dissipative adaptation captures the adaptation of the dissipative structure as such, not a prediction about the
environment maintained by this structure: England's formalism has no $I_{\text{pred}}$ numerator. $\eta_L$ adds to
dissipative adaptation the requirement that the adapted state maintain its own model of the
environment—moving from a pure dissipative structure to a structure that pays for its own modeling.

*Set-inclusion {P-M-E adapted} ⊃ {$\eta_L$ vital}.* The Perunov–Marsland–England programme is broader than
$\eta_L$ vitality: any system far from equilibrium that reliably absorbs and dissipates the energy of an external
driving field qualifies as "physical adaptation"—independently of the presence of a self-payment loop. Perunov and
colleagues are explicit: "there may be many examples of `well-adapted' structures that did not have parents" (P-M-E 2016,
p. 21)—physical adaptation as a universal phenomenon, separate from the Darwinian one. The empirical illustration of P-M-E 2016 itself
is silver nanorods in a light field (Ito et al. 2013), which statistically "learn" to match their surface plasmon resonances to the frequency of the driving field; examples of similar adapted but non-replicator dynamics are also documented in polar actin patterns and active liquid crystals. In $\eta_L$ terms these systems are **adapted but not vital**: they
pass the P-M-E "physical adaptation" test (reliable matching of absorption-dissipation to external driving), but fail the
counterfactual ablation of § 2.2—payment comes from outside (light field, ATP influx), there is no self-payment loop. Likewise the thermostat of
§ 4.4: P-M-E-adapted to being powered from the electrical grid, but $\eta_L^{\text{int}}$ is undefined through the simultaneous failure of
$T_v^{\text{int}}$ and $C_v^{\text{int}}$. The set-inclusion formalises the separation: P-M-E adaptation is a **necessary but
not sufficient** condition for $\eta_L$ vitality. $\eta_L$ singles out within the P-M-E-adapted class the subset with thermodynamic
closure of the self-payment budget.

*Major transitions in evolution.* The programme of Maynard Smith and Szathmáry (1995)—updated in Szathmáry (2015) with
the explicit inclusion of information-evolutionary arguments—captures
a sequence of key evolutionary transitions. These are the transitions from molecular replicators to chromosomes and cells,
from prokaryotes to eukaryotes, from unicellular to colonial and multicellular forms, from individuals to social groups.
Each of them introduces a **new level of subject of the evolutionary process** with a re-addressing of replication and error
load. In $\eta_L$ terms a major transition is the event of the emergence of a **new subject of self-payment**:
after the transition the free energy maintaining predictive information about the environment closes onto a new aggregate
actor (the cell as an actor over molecules, the multicellular organism as an actor over cells). The correspondence opens
a research programme: does each major transition in the sense of Maynard Smith–Szathmáry qualify as a phase
transition in the subject of $\eta_L$—with its own numerator $I_{\text{pred}}^{\text{new}}$, paid for by dissipation at
a new level of organisation? This question imposes a concrete thermodynamic criterion on the hierarchy of evolutionary
levels and remains an open task for future work.

*Geochemical OoL programmes.* The programmes of Pross (2012), Smith and Morowitz (2016) and Kauffman (Kauffman 2019)
treat the abiotic→biotic transition as the discovery of a closed loop over a geochemical flux. Hydrothermal systems, alkaline vents, metabolic catalysts form a circuit in which part of the free energy of the external geochemical driving force begins to be maintained within the circuit's own structure. Pross formulates this as a
transition from thermodynamic stability to dynamic kinetic stability. Smith–Morowitz—as a phase transition
in a geochemical network with the emergence of a metabolic core. Kauffman—as the discovery of the adjacent
possible through the spontaneous accumulation of catalytic closures. The alkaline-vent OoL programme of Martin–Russell
(Martin and Russell 2003) frames the geochemical transition to chemoautotrophic prokaryotes as a line parallel to
the metabolism-first lines of Smith–Morowitz and Pross. Walker (2017b), in a review in *Reports on Progress in Physics*, maps
OoL as a problem in physics, framing the context of these programmes as a landscape.

In $\eta_L$ terms all three geochemical programmes (Pross, Smith–Morowitz, Kauffman) articulate one and the same phase transition. The moment of origin of life is the moment
when a geochemical system passes from *external payment* (the full free energy passes through the system
in transit, without being maintained) to *self-payment*. Part of the free energy closes within its own circuit and
physically pays for the maintenance of the model of the environment. This formulation has the status of a risky prediction for the future
extension of the methodology beyond the stationary regime; within the present work the operational procedure for measuring
$\eta_L$ on a pre-biotic geochemical substrate is undefined and constitutes an open task. The counterfactual ablation of the
boundary (§ 2.2 main) and the MI estimate of $I_{\text{pred}}$ through a sensory channel are applicable to already-formed biological
systems. Their transfer to the pre-biotic register requires the development of proxies for $I_{\text{pred}}$ and self-payment in
an evolving geochemical network.

*The parallel programme of Chirumbolo–Vella 2026.* Chirumbolo and Vella (2026) in *Theory in Biosciences*
formulate the origin of life as an informational-dissipative process with water-mediated informational entropy gradients.
Their framework is a conceptual neighbour of ours through a shared ontology of informational dissipation; the difference lies in the operational
measure: they leave the scale qualitative, $\eta_L$ imposes a quantitative Landauer discipline on top of the same intuition
about self-organising dissipative systems.

*Summary paragraph.* The five programmes—the Eigen–Schuster hypercycle, RAF networks, dissipative adaptation, major transitions,
geochemical OoL—each operationalise one side of the phenomenon of the emergence and maintenance of living systems.
The corresponding sides are: replicator-level autocatalytic closure with a template carrier (hypercycle), structural
closure of the catalytic network (RAF), dissipative adaptation, the evolutionary subject, the geochemical phase transition. $\eta_L$ does not
compete with any of them and does not claim to close the origin-of-life problem; instead the scale unifies
them into a single dimensionless measure through the self-payment postulate. This is a thermodynamic operationalisation of the condition that
each of the five programmes articulates from its own side: the positivity of $\eta_L$ is a necessary condition for the moment of
origin of life in any of them. Further refinement of each of these correspondences is an open research task.

## S4.9 Positioning within contemporary demarcation debates

Beyond the lines of organisational closure (§ S4.7) and origin of life (§ S4.8), the $\eta_L$ programme is explicitly related
to four enduring lines of contemporary philosophy of biology that capture the demarcation difficulty of the concept of
"life". These lines are articulated in the first paragraph of § 1 main; here is a comparative diagnosis of how each of them
relates to the operational scale $\eta_L$. The principal methodological thesis of the subsection: $\eta_L$ does not propose
yet another definition of life, but contributes to the ongoing debate a formal quantitative scale on which the
indicated lines can work jointly.

*Cleland's anti-definitionism.* Cleland (2019) argues that the search for a definition of life through lists of features is
methodologically barren and has failed to converge over decades. Instead of a dictionary definition, what is needed is a "theory of
life"—a theoretical framework in which life occupies a position determined by explanatory structure, rather than by
list-based demarcation. The empirical background of the line is
the Trifonov (2011) registry, which documented a lexical analysis of 123 definitions of life without convergence to a
common core; Cleland's anti-definitionism is a methodological reaction to this material. The $\eta_L$ programme
*joins* this diagnosis: definitions through features break down at boundary crossings—the biosphere, LLM-corp,
the city, the minimal cell present different combinations of features, not reducible to a single assortative registry.
$\eta_L$ is not yet another definition, but an operational discriminator: a dimensionless scale on which each system
receives a position through the measurable ratio of predictive information to the Landauer budget, without claiming
to exhaust the phenomenon of life. The difference. Cleland's anti-definitionism declares the methodological barrenness of the
feature-based criterion; $\eta_L$ proposes not a definition through features, but an operational discriminator with an explicit falsification regime. It is not a theory of life in the full sense, but one of the obligatory dimensions of such a theory.

*Cluster definitions of Mariscal–Doolittle.* The "life and life only" programme of Mariscal and Doolittle (2020)
treats life as a cluster of related concepts not reducible to a single definition. Different approaches
illuminate different sides of the phenomenon; the attempt to reduce them to one formula loses analytical substance.
This position is substantively compatible with $\eta_L$ as a process-property. The positivity $\eta_L > 0$ is not an essential
definition of "life as such", but a property of the process of self-payment for predictive information, realisable **multiply**
—by the chemical loop of a bacterium, the biogeochemical circuit of the biosphere, a synthetic minimal cell, a hypothetical
non-biological architecture with a closed model↔dissipation loop. The cluster nature of the concept is preserved; $\eta_L$
contributes to the cluster one common thermodynamic dimension. The difference: cluster-definitions allow that not all
life-like phenomena have a single thermodynamic invariant; $\eta_L$ proposes one single thermodynamic
invariant for the synchronic dimension of vitality. The programme does not claim to unify diachronic
(population-evolutionary) aspects (§ 2.7 main). This is a risky claim, falsifiable by the observation of a life-like
system across three independent synchronic channels with a stable $\eta_L = 0$ (§ 5 main).

*Operational definitions at frontiers of Bich–Green.* Bich and Green (2018) directly discuss how operational
criteria should behave at the frontiers of biology—on viruses, protocells, synthetic constructs. $\eta_L$ is
an operational criterion of exactly this form. For a viral system that does not maintain a closed self-payment loop and
parasitises on a host, the numerator and denominator are defined such that the virus's own predictive information is not
paid for by its own dissipation independently of the host. The scale gives $\eta_L = 0$ for the virus-in-isolation and is consistent
with the biological convention that ordinarily does not assign autonomous vitality to a virus. This point is methodological,
not phenomenological: $\eta_L$ behaves in boundary cases as the Bich–Green programme requires of an operational definition, without reproducing the dilemmas of definitions through lists. The difference: on a viral system $\eta_L = 0$
through the numerator; the virus-in-host changes status—the programme must say **whose** $\eta_L$ increases upon infection
(re-addressing of the object, § 2.2 main). Bich–Green leave the question of the conventionality of the virus boundary open; $\eta_L$
fixes it through counterfactual ablation.

*Pradeu's process biology.* Pradeu (2018) argues that it is methodologically more productive to think of the organism as a
**process**, not as an object—biological individuality is set through temporal dynamics, not through static
object-identity. $\eta_L$ operationalises exactly this: the scale is computed over a window $\tau_d$ of stability and
is maintained over the window (§ 2.6 main); vitality is defined not as a property of the system-as-object, but as a characteristic of
the system's dynamics over a temporal window. The window $\tau_d$, the counterfactual ablation of the boundary, and the stationarity
of the triad of invariants (§ 2.3 main)—all three constructions operationalise Pradeu's processual ontology in
a thermodynamic register. The difference: Pradeu's process view excludes an identifiable substrate at all moments of time; $\eta_L$
requires fixation of the boundary $X$ through counterfactual ablation on each window $\tau_d$. This is not a reintroduction of objecthood—counterfactual ablation does not presuppose the persistence of an object, but only local causal-selective
closure on the window.

*Information-theoretic individuality of Krakauer et al.*
The information-theoretic operationalisation of individuality by Krakauer et al. in Theory in Biosciences itself
(Krakauer et al. 2020) proposes a decomposition of the system-environment through channels of information propagation with three forms of individuality
(organismal/colonial/driven). $\eta_L$ is complementary to their framework: their apparatus captures the informational side of demarcation
without thermodynamic payment; self-payment adds the Landauer denominator, making the three-form typology dependent
on **who pays** for the maintenance of the information.

*Basic autonomy of Ruiz-Mirazo–Moreno.* The basic autonomy programme of Ruiz-Mirazo and Moreno (2004) is
the line that connects autopoiesis with thermodynamic constraint-logic closest to self-payment. The difference:
$\eta_L$ is positioned as a thermodynamic disciplining on top of basic autonomy through the explicit identity of the boundaries of the
model and the dissipation that pays for it.

*Summary paragraph.* The $\eta_L$ programme is methodologically compatible with Cleland's anti-definitionist line,
the cluster-definition programme of Mariscal–Doolittle, the operational-frontiers approach of Bich–Green, Pradeu's process-biology
position, the information-theoretic framework of Krakauer et al. and the basic-autonomy programme of
Ruiz-Mirazo–Moreno—not as an alternative to them, but as a formal quantitative scale on which these lines can
work jointly. This is a contribution to the ongoing demarcation debates, not a proposal of a new definition of "what
life is". The programme is an operational discriminator that preserves the processual ontology, realisable multiply
through different proxies of the numerator and denominator, and behaving at the boundaries in accordance with biological convention.
## S5 Falsification criteria: full operational protocols

Main § 5 contains condensed formulations of eight lines of falsification, grouped into three blocks. Here we give the
full operational protocols with numerical criteria, p-values, sample sizes, pre-registration requirements
and conditional caveats. The structure of S5.1–S5.3 parallels Blocks 1–3 of main § 5; S5.4 contains the consolidated
Lakatosian dossier of the programme.

*Note on numbering.* The nine numbered items of the three blocks reduce to eight substantively
independent lines. Item 1 of Block 2 (the statistical aspect — violation of monotonicity) and item 1 of Block 3
(the constructive aspect — power-law dependence, Prediction 1) are two formulations of a single risky stake about the rate
of evolutionary adaptation.

### S5.1 Block 1: direct refutations of the scale (operational details)

*Block 1, item 1 — $T_v$ failure (full protocol).* Observation: stationary maintenance of $I_{\text{pred}} > 0$ at
$E_{\text{actual}}$ below the Landauer bound $I_{\text{pred}} \cdot k_B T \ln 2$ in an irreversible implementation regime.
Operational test of irreversibility: measurable heat dissipation $\dot Q > 0$ during execution of the information operation
(a reversible Bennett implementation yields $\dot Q \to 0$ in the limit of a slow protocol). Fixing $T$: the temperature
of the heat bath into which the system actually discharges $E_{\text{actual}}$ — not of the source environment and not of the control set-point.
Such an observation realises $\eta_L > 1$; it refutes either the postulate of stationary accounting in (c) of the Statement of § 2.1 main,
or one of conditions (a)–(b); it eliminates $\eta_L \le 1$ as a boundary of the scale and nullifies $T_v$ as a necessary condition.

*Bennett regime: caveat.* The Bennett regime of reversible computation (Bennett 1973, 1982) does not serve as a refuting scenario:
it lies outside the domain of definition and requires a separate operationalisation through the number of logical bits. The Bennett regime is a pre-existing physical limitation of Landauer's principle, recognised long before the present programme (Bennett 1973);
its exclusion is not specific to the $\eta_L$-programme (any Landauer measure faces the same question of the domain of definition).
A refutation via a Bennett demonstration is counted if the author of the counter-example first operationalises the "number of
logical bits" as the canonical numerator and shows $\eta_L^{\text{log}} > 1$.

*Block 1, item 2 — $C_v$ failure (full protocol).* Observation: a system with positive $C_v^{\text{op}}$ at
$\dot{H}_{\text{erasure}} = 0$ over the window $\tau_d$ — an example of a system maintaining predictive information without
needing to pay the Landauer erasure cost for each predictive bit. Nullifies $C_v$ as a necessary condition.

*Block 1, item 3 — $S_v$ failure (full protocol).* Observation: a system with a closed self-payment loop
($\eta_L > 0$ by the counterfactual ablation of § 2.2 main) that simultaneously satisfies two conditions:
$Q < Q_{\text{null}} + 2\sigma$ (modularity indistinguishable from a degree-preserving null model — configuration model, preserving the degree distribution) and
$C(k) \not\sim k^{-\beta}$ with $\beta \in [0.5; 1.5]$ (absence of a hierarchical signature per Ravasz–Barabási 2003). An ensemble of $\ge 10$ independent biological subjects is required. A refutation
is counted at $p < 0.01$ against the null hypothesis of random topology at the stated power and with pre-registration
of the protocol. Nullifies $S_v$ as a necessary condition.

### S5.2 Block 2: tests of proxies and operationalisation (operational details)

*Block 2, item 1 — violation of monotonicity (full protocol).* Observation: systematic violation of the monotonic
dependence of the rate of evolutionary learning on $\eta_L$. If, in a controlled experimental
evolution experiment (bacterial cultures in a chemostat with varying temperature, population density and carbon
source), systems with $\eta_L$ differing by an order of magnitude yield adaptation rates that are statistically indistinguishable over
sufficiently long windows, the central relation loses its numerical meaning. The constructive test coincides
with the protocol of S5.3 (Prediction 1).

*Block 2, item 2 — vitality across three channels at $\eta_L = 0$ (full protocol).* Observation: a system that indicates
vitality across three independent channels — rate of adaptation, rate of self-repair, independent biochemical
markers of self-production (in the sense of Darwinian evolution; cf. the NASA definition of life as a "chemical system
capable of Darwinian evolution" (Joyce 1994) — here invoked as a conventional external referent, not
as a competing theory of vitality; the shift of substrate-bound register at this step is deliberate). At the same time,
$\eta_L = 0$ under all operationalisations of $I_{\text{pred}}$ and $E_{\text{actual}}$ via standard domain-specific
proxies. This is a criterion independent of $\eta_L$: rate of adaptation, rate of self-repair and biochemical markers
of self-production are operationalised through measurable quantities not reducible to the numerator of $\eta_L$. A systematic
divergence would point either to a defect of the numerator as an operational proxy for predictive information
(the methodological level of falsification, see § 2.7 main), or to the failure of the very concept of vitality through
the efficiency of self-modeling (the ontological level).

*Block 2, item 3 — a conventionally living system with $\eta_L = 0$ (full protocol).* Observation: a biological
system that is unquestionably living by conventional criteria, for which $\eta_L$ is strictly equal to zero under all reasonable
operationalisations. Refutes the adequacy of the scale as an operational discriminator of vitality.

### S5.3 Block 3: progressive predictions (operational details)

*Block 3, item 1 — Prediction 1, power-law dependence of the adaptation rate (full protocol).* The rate of decay of the divergence of the
internal model from the environment, normalised to the complexity of the environment, should scale with $\eta_L$ as a monotonically
increasing function. The concrete protocol: a culture of *E. coli* in a chemostat with controlled carbon flux (glucose,
lactose, acetate); $\eta_L$ is varied through temperature (25–42 °C, five levels) and population density (three
levels); adaptation is the decay of the divergence between the encoded methylation level and the observed gradient over 50
generations. Positive prediction: the correlation coefficient (Pearson between $\log r_{\text{adapt}}$ and $\log \eta_L$)
$\rho \in [0.4;\, 0.7]$ over 45 lines; $r_{\text{adapt}} = A \cdot \eta_L^{\alpha}$ with $\alpha \in [0.3;\, 1.0]$. The range is narrow relative to the null hypothesis $\alpha = 0$ and
relative to the hypothesis $\alpha \ge 2$ (strong nonlinearity); the expected independent test point is the LTEE data
of Lenski, not used for deriving the lower bound. The upper bound $\alpha = 1$ is direct proportionality of the
adaptation rate to the flux $I_{\text{pred}}$; the lower bound $\alpha = 1/3$ is derived from the structure of (2) main: $I_v$ is the cube
root of the product of three capacities, and the minimal dependence $r_{\text{adapt}} \propto \sqrt[3]{\eta_L}$ corresponds to the
contribution of one capacity out of three. The scale is calibrated on the worked example of § 3.5 main ($\eta_L^{\text{comp}} \in
[10^{-6}, 10^{-4}]$). Refutation: $\hat{\alpha}$ significantly outside $[0.3;\, 1.0]$ at $p < 0.01$ (incorrect exponent);
$\hat{\rho} < 0.2$ at the stated power (no detectable trend); or $\hat{\rho} < 0$ (trend in the opposite
direction — qualitative refutation).

*Block 3, item 2 — Prediction 2, monotonicity over the matching window (full protocol).* In the regime of approach to stationarity,
when $I_{\text{pred}}$ is not yet saturated and accumulates faster than the integrated dissipation, the stationary formulation
predicts: under normalisation to a unit dissipation rate ($\dot{E}_{\text{actual}} = \text{const}$ over the
pre-stationary transient with window $\Delta\tau \ll \tau_d$) a monotonic growth of $\eta_L(\Delta\tau)$ is expected over the
matching interval. Test on the same 45 *E. coli* lines: measure $\eta_L(\Delta\tau)$ for $\Delta\tau$ from
an hour to a generation with independent fixing of $\dot{E}_{\text{actual}}$. A decrease of $\eta_L$ with $\Delta\tau$ in this
regime is a counter-argument to the stationary framework as such, not a delegation to the accompanying work.

*Block 3, item 3 — Prediction 3, structural threshold $f^*$ (full protocol).* We consider a class of hypothetical
autonomous embodied agents with photovoltaic or battery power supply and a physical actuator with its own
thermodynamic budget. For this class a structural threshold $f^*$ of the fraction of internalisation
of the energy budget (the ratio $E_{\text{actual}}^{\text{own}}/E_{\text{actual}}^{\text{total}}$) is predicted. Below the threshold
the counterfactual ablation of § 2.2 main yields $\eta_L^{\text{int}}$ undefined (structural failure of the self-payment loop);
above it, a measurable $\eta_L^{\text{int}} > 0$. The numerical localisation $f^* \in [0.1;\, 0.5]$ is a research hypothesis of the programme; a formal derivation of the bounds via counterfactual ablation is an open problem. Under the two-level formulation of § 3.4 main
the structural predicate of counterfactual ablation is **binary** (a self-paying error-return channel either exists or does not), whereas
$f^*$ is an **empirical** threshold on a continuous proxy $f$, above which closure of the loop is statistically stable; $f^*$ is
a regularity of joint internalisation, not the structural decision boundary itself.

*Caveat on the domain of applicability.* The prediction is not applicable to current cloud-hosted stateless LLMs, where $E_{\text{actual}}^{\text{own}}
= 0$ constructively (the power grid and infrastructure are external to the forward pass), $f = 0$ by construction.

*Differential prediction relative to the AI-safety literature.* AI-safety programmes (Hubinger et al. 2019; Carlsmith
2022) predict behavioural emergence of a self-preservation drive at a *capability* threshold —
independently of the energetic architecture; the $\eta_L$-programme predicts the structural emergence of a self-payment loop
at a *thermodynamic-budget* threshold $f^*$ — independently of the behavioural profile. Possible separation scenarios:
(a) the capability threshold is reached, the self-payment threshold is not (behavioural power-seeking without structural
self-payment); (b) the self-payment threshold is reached, capability is not (structural closure of the loop without a behavioural
drive). Differential observation: behavioural absence of power-seeking under observation of $f \ge f^*$ refutes the coincidence of
the two threshold conditions and confirms $\eta_L$ as an independent predictor.

*Refutation of Prediction 3.* A systematic observation of a system in the indicated class with $f \in [0; 0.1]$ that passes
counterfactual ablation with $\eta_L^{\text{int}} > 0$, or of a system with $f > 0.5$ that fails the screening (undefined $\eta_L^{\text{int}}$). A population of $\ge 10^2$ autonomous embodied agents with their own
energy budgets is required, at the stated power and with pre-registration of the protocol (the detection scheme — § 3.4 main).

### S5.4 Consolidated Lakatosian dossier of the programme

Relative to assembly theory, IIT, teleodynamics and FEP, the $\eta_L$-programme is a progressive shift along three independent
lines of predictions:

- monotonic correlation of the adaptation rate with $\eta_L$ (Prediction 1, S5.3);
- a transient pattern of SETI signals as a signature of the externalisation filter of the cost (§ 6 main);
- the existence of a structural threshold $f^*$ of internalisation of the energy budget of an AI system (Prediction 3, S5.3).

The SETI signature is a progressive prediction OVER AND ABOVE the eight lines of falsification of § 5, having the status of a speculative extrapolation (§ 6), and not of a sanctioned operationalisation on a calibrated system; for this reason it is not counted among the "eight lines."

The programme sustains the progressive regime as long as these predictions admit independent empirical verification.
