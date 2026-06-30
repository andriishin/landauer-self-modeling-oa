# Worked Example: structural verdict for a bimetallic thermostat

A structural verdict for a household thermostat with a bimetallic strip, under
the refounded central quantity $\eta_v = I_{\text{pred}}/I_{\text{mem}} \in [0,1]$.
Companion to § 4.4 + Supplementary § S4.4 (Andriishin, *Theory in Biosciences*,
in preparation).

## Substantive meaning

The thermostat is a **boundary case**, not a positive one. It *formally satisfies*
Friston's free-energy principle (FEP) — it minimises the error between setpoint
and observation — but it **fails the self-payment predicate** $S$: the predictive
information about the room is physically paid for by the external power grid, not
by the internal dissipation of the bimetal, and no physical error-return loop
closes on the bimetal. So $S = 0$, and $\eta_v = I_{\text{pred}}/I_{\text{mem}}$ is
**not defined** (there is no self-paying subject to measure it for).

This is the **central anti-FEP argument** of the paper: formal FEP-applicability
does not imply self-payment. In terms of counterfactual ablation (§ 2.2):

| Candidate | Inside the boundary? | Why |
|-----------|----------------------|-----|
| Bimetallic strip | yes | removing it breaks the loop |
| Relay contacts | yes | removing it breaks the loop |
| Heating element | no | removes the heat source, not the decision loop |
| Electric grid | no | external energy source |
| External setpoint operator | no | removing it does not disrupt regulation |

The boundary is `{bimetal, relay}`, inside which the internal dissipation is
$P_{\text{int}} \sim 10^{-6}$ W.

## Contents

| File | Purpose |
|------|---------|
| `eta_thermostat.py` | Structural verdict: counterfactual ablation, surviving quantities, two readings (both $S=0$) |
| `expected_output.txt` | Reference output (LF) for verification |

Uses only the Python standard library (`math`).

## Running

```bash
python eta_thermostat.py
```

## Surviving quantities (these outlive the refounding; match § 4.4)

- $P_{\text{int}} \sim 10^{-6}$ W — internal dissipation (elastic relaxation of the bimetal + relay).
- Carrier bound on predictive information set by the hysteresis resolution:
  $I_{\text{pred}} \le \log_2(\Delta T_{\text{room}}/\Delta T_{\text{hyst}})$.
  Diurnal $\Delta T_{\text{room}} \sim 10$ K, $\Delta T_{\text{hyst}} = 1$ K
  $\Rightarrow I_{\text{pred}} \le 3.32$ bits ($\approx 3$); seasonal
  $\Delta T_{\text{room}} \sim 30$ K $\Rightarrow I_{\text{pred}} \le 4.91$ bits
  (up to $\sim 5$).

Everything tied to the earlier energetic-denominator ratio is removed: $P_{\text{int}}$
is reported as a physical dissipation, not as the denominator of an efficiency.

## Two self-consistent readings, both S = 0

- **Managing** ("regulate the room"): condition (i) of self-payment fails — the
  room heating is paid by the external grid, so $E_{\text{own}}$ about that task is
  zero ($T_v$ fails).
- **Trivial** ("hold the bimetal's own shape"): condition (ii) fails — passive
  thermo-mechanical coupling forms no error-return loop; a shape deviation is not
  corrected by the system's own dissipation ($S_v$ fails).

The divergence between the two readings does **not** mark an ontological
transition: Bruineberg et al. (2022) show formally that no such transition can be
made without smuggling in epistemic assumptions. It marks the **conventionality**
of boundary choice — one physical system admits several self-consistent
boundaries, and choosing between them is a methodological discipline.

## References

- **Bruineberg, J.; Dołęga, K.; Dewhurst, J.; Baltieri, M.** The Emperor's New Markov Blankets. *Behavioral and Brain Sciences* **2022**, *45*, e183. (Pearl- vs Friston-blanket; no ontological transition without epistemic assumptions.)
- **Friston, K.** The free-energy principle: a unified brain theory? *Nat. Rev. Neurosci.* **2010**, *11*, 127–138.
- **Aguilera, M.; Millidge, B.; Tschantz, A.; Buckley, C. L.** How particular is the physics of the free energy principle? *Phys. Life Rev.* **2022**, *40*, 24–50.

## Status

A compact structural accounting; its role is **demonstrative**, not quantitative:
it shows that the counterfactual-ablation procedure is trivially realisable, that
the "trivial" vs "managing" readings are computable rather than rhetorical, and
that both yield $S = 0$ — so $\eta_v$ is undefined. A numeric $\eta_v$ would require an
MI estimate of $I_{\text{pred}}$ and $I_{\text{mem}}$ of a self-paying loop, which
the thermostat does not possess.
