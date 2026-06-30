# Worked Example: structural verdict for LLM-as-corporation

A structural verdict for a large language model under the nested counterfactual-
ablation boundaries $B_1 \subset B_2 \subset B_3 \subset B_4$, under the refounded
central quantity $\eta_v = I_{\text{pred}}/I_{\text{mem}} \in [0,1]$. Companion to
§ 3.4 + Supplementary § S3.4 (Andriishin, *Theory in Biosciences*, in preparation).

## What it means

The LLM is the strongest clean case of the new demarcation: a system with a
**strong predictive model and $S = 0$**. The trained model is predictively strong
(large $I_{\text{pred}}$), but its payment loop is open. Demarcation is carried by
the self-payment predicate $S$, **not** by any energetic-efficiency ratio; the old
$\eta^{\text{corp}}$ number is removed. Extending the boundary until $S = 1$ does
**not** make the *model* vital — it re-addresses the self-paying subject.

| Boundary | Components | Window | S | Self-paying subject |
|----------|-----------|--------|---|---------------------|
| $B_1$ | weights only | static | 0 | none (degenerate) |
| $B_2$ | weights + KV-cache + executing server | session | 0 | none (grid pays) |
| $B_3$ | $B_2$ + training pipeline (data + GPU park + RLHF) | model generation | 1 | pipeline (not model) |
| $B_4$ | $B_3$ + corporation (legal entity) | generations | 1 | firm (not model) |

- At $B_1, B_2$: $S = 0$ — the grid pays for holding/updating the model and there is no physical channel returning the model's error to its carrier.
- At $B_3, B_4$: the loop closes ($S = 1$), but the self-paying subject is no longer the model — it is the pipeline, then the firm.

So the **model is never vital**: where $S = 1$, the measured object is the
corporation, not the model. The value of $\eta_v = I_{\text{pred}}/I_{\text{mem}}$
for any of these loops is **not asserted** here — a number would require an MI
estimate of $I_{\text{pred}}$ and $I_{\text{mem}}$ of the respective loop (future
work). No $\eta^{\text{corp}}$ figure is claimed.

## Contents

| File | Purpose |
|------|---------|
| `eta_llm_corp.py` | Structural verdict over the nested boundaries $B_1$–$B_4$ (predicate $S$, self-paying subject) |
| `expected_output.txt` | Reference output (LF) for verification |

Uses only the Python standard library.

## Running

```bash
python eta_llm_corp.py
```

## Connection to the literature

The self-payment predicate $S$ offers a thermodynamic co-characterisation of the
structural tendency studied in AI-safety as instrumental convergence /
self-preservation (Omohundro 2008; Bostrom 2014) and as *embedded agency* (Demski
& Garrabrant 2019: an agent as a part of its environment paying for its own
computation). The pair $(S, \eta_v)$ is proposed as a necessary thermodynamic
condition for a physically realised embedded world-model with its own robustness
loop — not as a sufficient condition for any specific alignment property.

- **Patterson, D.; et al.** Carbon Emissions and Large Neural Network Training. *arXiv:2104.10350* **2021**. (Scale of frontier-model training infrastructure.)
- **Demski, A.; Garrabrant, S.** Embedded Agency. *arXiv:1902.09469* **2019**. (Agent as part of its environment, paying for its own computation.)

## Status

The verdict is **structural**: $S = 0$ on $B_1, B_2$ (weights / session), $S = 1$
on $B_3, B_4$ with the subject re-addressed to the pipeline / firm. No
$\eta^{\text{corp}}$ number is asserted; quantifying $\eta_v$ for the
pipeline/corporation loop requires a separate MI estimate. Self-contained:
standard library only.
