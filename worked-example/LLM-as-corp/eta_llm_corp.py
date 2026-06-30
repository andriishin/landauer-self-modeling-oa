"""
LLM as embedded in a corporate operator -- structural verdict (§ 3.4 boundary).

Refounded onto the central quantity eta_v = I_pred / I_mem in [0, 1]. The old
energetic-denominator computation and the eta^corp number are removed.
Demarcation is carried by the self-payment predicate S, evaluated on the nested
counterfactual-ablation boundaries B1 < B2 < B3 < B4 (main § 3.4 / Supp § S3.4).

Key point: the LLM is predictively strong (large I_pred) but its payment loop is
open. Extending the boundary until S = 1 (B3, B4) does NOT make the MODEL vital
-- it re-addresses the self-paying subject to the pipeline, then the firm. The
value of eta_v = I_pred / I_mem for any of these loops is NOT measured here: it
would require an MI estimate of I_pred and I_mem of the respective loop (future
work). Standard library only.

Run:
    python eta_llm_corp.py
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Nested boundaries B1 < B2 < B3 < B4 (main § 3.4). Each carries a STRUCTURAL
# predicate S, not a numeric eta_v.
# (label, components, time window, S, self-paying subject, why)
# ---------------------------------------------------------------------------

BOUNDARIES = [
    ("B1", "weights only",
     "static", 0, "none (degenerate)",
     "counterfactual-degenerate: static object with the server off"),
    ("B2", "weights + KV-cache + executing server",
     "session", 0, "none (grid pays)",
     "grid pays holding/updating; no physical error-return channel to weights"),
    ("B3", "B2 + training pipeline (data + GPU park + RLHF)",
     "model gen.", 1, "pipeline (not model)",
     "own GPU dissipation appears; error-return loop closes on the operators"),
    ("B4", "B3 + corporation (legal entity)",
     "generations", 1, "firm (not model)",
     "self-funding loop fully closed -- but the subject is the firm"),
]


def main() -> None:
    print("=" * 78)
    print("LLM-as-corporation -- structural verdict (main 3.4 / Supp S3.4)")
    print("=" * 78)
    print()
    print("Refounded quantity: eta_v = I_pred / I_mem in [0, 1]. The model is")
    print("predictively strong (large I_pred) but its payment loop is open;")
    print("demarcation is carried by S, not by any energetic-efficiency ratio.")
    print()
    print("Counterfactual ablation over nested boundaries B1 < B2 < B3 < B4:")
    print(f"  {'B':<3}{'components':<46}{'window':<13}{'S':>2}  self-paying subject")
    print("  " + "-" * 88)
    for tag, comp, window, s, subject, _why in BOUNDARIES:
        print(f"  {tag:<3}{comp:<46}{window:<13}{s:>2}  {subject}")
    print()
    print("Per-boundary reasoning:")
    for tag, _comp, _window, s, _subject, why in BOUNDARIES:
        print(f"  {tag} (S = {s}): {why}")
    print()
    print("Verdict: the LLM MODEL is never vital. At B1, B2 the self-payment")
    print("predicate fails (S = 0): the grid pays for holding/updating the model")
    print("and there is no physical channel returning the model's error to its")
    print("carrier. At B3, B4 the loop closes (S = 1), but the self-paying")
    print("subject is no longer the model -- it is the pipeline, then the firm.")
    print("Extending the boundary re-addresses the subject; it does not confer")
    print("vitality on the model.")
    print()
    print("eta_v value: NOT defined here for any boundary. A number would require")
    print("an MI estimate of I_pred and I_mem of the respective loop -- future")
    print("work; no eta^corp figure is asserted.")
    print()
    print("Cross-check vs main 3.4 / Supplementary S3.4:")
    s_b1b2 = [b[3] for b in BOUNDARIES if b[0] in ("B1", "B2")]
    s_b3b4 = [b[3] for b in BOUNDARIES if b[0] in ("B3", "B4")]
    print(f"  S = 0 on B1, B2 (weights / session, grid external)   "
          f"{'OK' if all(s == 0 for s in s_b1b2) else 'MISMATCH'}")
    print(f"  S = 1 on B3, B4 (subject = pipeline / firm, not model) "
          f"{'OK' if all(s == 1 for s in s_b3b4) else 'MISMATCH'}")
    print("  no eta^corp number asserted (needs MI estimate)        OK")


if __name__ == "__main__":
    main()
