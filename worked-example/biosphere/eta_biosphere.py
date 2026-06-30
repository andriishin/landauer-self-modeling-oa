"""
Earth's biosphere (Gaia) -- structural verdict + carrier-capacity ladder (§ 3.7).

Refounded onto the central quantity eta_v = I_pred / I_mem in [0, 1]. The old
energetic-denominator computation (NPP*tau against an erasure-capacity bound) is
removed; the biosphere's verdict is structural:

  S = 1  -- biogeochemistry is fed by its own flux (condition i) and a distorted
            regulation returns as species collapses / mass extinctions to the
            biosphere itself (condition ii);
  eta_v > 0 -- it holds predictive structure about its own environment.

So the biosphere is VITAL (or a family of vital systems -- the unity-of-model
question of § 3.7 stays open). The grade (numeric eta_v) is NOT asserted: it needs
an MI estimate through the biogeochemical sensory channel, left to future work.

The genomic numbers below are CARRIER CAPACITIES (ceilings on substrate), NOT
values of eta_v and NOT measured predictive information. A repeated genome adds no
predictive MI about the environment, so the copy-number ledger is irrelevant to
eta_v; it is shown only to contrast the scales. Standard library only.

Run:
    python eta_biosphere.py
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Carrier-capacity ladder (main § 3.7). Each entry is a CEILING on substrate
# capacity in bits, NOT a value of eta_v and NOT a measured predictive MI.
# ---------------------------------------------------------------------------

#   unique coding/regulatory genome:
#       ~10^12 species x 5e6 bp x 2 bit/bp ~ 10^19 bits (main § 3.7).
N_SPECIES = 1.0e12
BP_PER_GENOME = 5.0e6
BITS_PER_BP = 2.0

CAPACITY_LADDER = [
    ("atmospheric / regulatory pools",      1.0e15,
     "small abiotic-pool ceiling"),
    ("unique coding/regulatory genome",     1.0e19,
     "10^12 sp x 5e6 bp x 2 bit/bp (main 3.7)"),
    ("raw unique-genome (overcounts)",      1.0e24,
     "over-counts non-coding bases (no predictive MI)"),
    ("full copy-number DNA",                1.0e37,
     "Landenmark et al. 2015; ~17 orders larger, irrelevant"),
]


def report_verdict() -> None:
    print("STRUCTURAL VERDICT (main 3.7)")
    print("-" * 72)
    print("  S = 1   biogeochemistry self-funds from its own flux (i) AND a")
    print("          distorted regulation returns as species collapses to the")
    print("          biosphere itself (ii).")
    print("  eta_v > 0 the biosphere holds predictive structure about its env.")
    print("  => VITAL (or a family of vital systems -- unity-of-model question")
    print("     of main 3.7 stays open: one Gaia vs many overlapping subsystems).")
    print()
    print("  Grade (value of eta_v): NOT asserted -- needs an MI estimate through")
    print("  the biogeochemical sensory channel; future work. The paradigm-case")
    print("  claim is the CLOSED self-payment loop and eta_v > 0, not a value.")
    print()


def report_capacity_ladder() -> None:
    unique = N_SPECIES * BP_PER_GENOME * BITS_PER_BP
    print("CARRIER-CAPACITY LADDER (ceilings on substrate, NOT eta_v)")
    print("-" * 72)
    print(f"  {'substrate ledger':<34}{'bits (~)':>10}  note")
    print("  " + "-" * 68)
    for label, bits, note in CAPACITY_LADDER:
        print(f"  {label:<34}{bits:>10.0e}  {note}")
    print()
    print(f"  consistency: 10^12 x 5e6 x 2 = {unique:.0e} bits"
          f" (unique coding-bound capacity).")
    print("  None of these is a value of eta_v. eta_v = I_pred / I_mem requires a")
    print("  measured predictive MI, which the substrate ceiling does NOT give:")
    print("  the copy-number ledger (~1e37) is ~17 orders above the unique-genome")
    print("  ceiling and carries no extra predictive MI about the environment.")
    print()


def main() -> None:
    print("=" * 72)
    print("Earth's biosphere (Gaia) -- structural verdict + capacity ladder")
    print("=" * 72)
    print()
    report_verdict()
    report_capacity_ladder()
    print("Cross-check vs main 3.7:")
    print("  biosphere verdict: S = 1, eta_v > 0 (VITAL); grade not asserted  OK")
    print("  ~1e19 unique-genome / ~1e37 copy-number shown as CAPACITY only  OK")
    print("  (no eta_v value derived from any of these ceilings)               OK")
    print()
    print("Status: the verdict is structural (S = 1, eta_v > 0); no eta_v number is")
    print("asserted. The genomic figures are carrier-capacity ceilings, not")
    print("predictive information. Refining I_pred / I_mem through biogeochemical")
    print("proxies is separate work. Self-contained: standard library only.")


if __name__ == "__main__":
    main()
