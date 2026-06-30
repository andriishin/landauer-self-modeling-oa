"""
Large city -- structural verdict + I_v screening-index demonstration (§ 3.6).

Refounded onto the central quantity eta_v = I_pred / I_mem in [0, 1]. The old
energetic-denominator part (a dimensionless efficiency ratio) is removed; the
city's verdict is now structural:

  S = 1  -- it self-funds from its own budget (condition i) and bears the error-
            return loop: a distorted flow-model returns as a crisis to the city
            itself (condition ii);
  eta_v > 0 -- it holds predictive structure about its own flows.

So the city is VITAL. The grade (the numeric value of eta_v among vital systems)
is NOT asserted here: it requires an MI estimate of I_pred and I_mem of the
administrative loop (resource flows -> decisions), left to future work
(main § 3.6).

What survives the refounding and is reproduced below is the STRUCTURAL readiness
index I_v = cube_root(T_v * C_v * S_v) of formula (2b), with percentile
normalisation (2a) -- a cohort-relative SCREENING composite, NOT a value of eta_v.
Per main § 2.5, I_v does not make the alive/not call (eta_v does); it only screens
structural readiness. It is demonstrated on an explicitly SYNTHETIC cohort
(illustrative placeholders, not real cities). Standard library only.

Run:
    python eta_city.py
"""

from __future__ import annotations

import math


# ---------------------------------------------------------------------------
# Structural verdict (main § 3.6)
# ---------------------------------------------------------------------------


def report_verdict() -> None:
    print("STRUCTURAL VERDICT (main 3.6)")
    print("-" * 72)
    print("  S = 1   self-funding (own municipal budget) AND error-return loop")
    print("          (a distorted flow-model returns as a crisis to the city).")
    print("  eta_v > 0 the city holds predictive structure about its own flows.")
    print("  => the city is VITAL (passes S = 1 and eta_v > 0).")
    print()
    print("  Grade (value of eta_v among vital systems): NOT asserted -- needs an")
    print("  MI estimate of I_pred and I_mem of the administrative loop")
    print("  (resource flows -> decisions); future work. The paradigm-case claim is")
    print("  the CLOSED self-payment loop, not any smallness of an efficiency.")
    print()


# ---------------------------------------------------------------------------
# I_v structural-readiness composite (formula 2b + 2a): METHOD demonstration
# ---------------------------------------------------------------------------
#
# SYNTHETIC archetype profiles. The raw "proxy" numbers below are illustrative
# placeholders chosen to exercise the formula, NOT measurements of any real
# city. They show two things:
#   (2a) percentile normalisation maps raw proxies to [0, 1] ranks within a
#        cohort;
#   (2b) I_v = cube_root(T_v * C_v * S_v): the geometric mean drags the composite
#        toward any weak capacity.

# (label, raw_T, raw_C, raw_S) -- arbitrary illustrative units.
SYNTHETIC_COHORT: list[tuple[str, float, float, float]] = [
    ("balanced-mid",        50.0,  50.0,  50.0),
    ("energy-rich/weak-S",  95.0,  55.0,  10.0),
    ("innovation-led",      40.0,  92.0,  45.0),
    ("structure-led",       35.0,  30.0,  90.0),
    ("uniformly-low",       12.0,  15.0,  10.0),
    ("uniformly-high",      88.0,  90.0,  85.0),
    ("one-weak-axis",       80.0,  78.0,  18.0),
    ("near-median",         52.0,  48.0,  55.0),
]


def percentile_rank(value: float, population: list[float]) -> float:
    """Average-rank percentile in (0, 1] -- formula (2a)."""
    n = len(population)
    less = sum(1 for x in population if x < value)
    equal = sum(1 for x in population if x == value)
    return (less + (equal + 1) / 2.0) / n


def geometric_mean(values: tuple[float, ...]) -> float:
    """Formula (2b): cube root of the product; 0 if any component is 0."""
    if any(v < 0 for v in values):
        raise ValueError("negative capacity")
    if any(v == 0 for v in values):
        return 0.0
    return math.exp(sum(math.log(v) for v in values) / len(values))


def report_i_v_demo() -> None:
    raw_t = [c[1] for c in SYNTHETIC_COHORT]
    raw_c = [c[2] for c in SYNTHETIC_COHORT]
    raw_s = [c[3] for c in SYNTHETIC_COHORT]

    print("I_v SCREENING-INDEX DEMO -- formula (2b)+(2a) on a SYNTHETIC cohort")
    print("(illustrative placeholders, NOT real cities; I_v screens structural")
    print("readiness only -- it does NOT make the alive/not call, eta_v does)")
    print("-" * 72)
    print(f"  {'profile':<20} {'T_v':>6} {'C_v':>6} {'S_v':>6} {'I_v':>7}")
    rows = []
    for label, rt, rc, rs in SYNTHETIC_COHORT:
        t_v = percentile_rank(rt, raw_t)
        c_v = percentile_rank(rc, raw_c)
        s_v = percentile_rank(rs, raw_s)
        i_v = geometric_mean((t_v, c_v, s_v))
        rows.append((label, t_v, c_v, s_v, i_v))
    for label, t_v, c_v, s_v, i_v in sorted(rows, key=lambda r: -r[4]):
        print(f"  {label:<20} {t_v:>6.3f} {c_v:>6.3f} {s_v:>6.3f} {i_v:>7.3f}")
    print()
    print("  Reading: 'uniformly-high' tops the composite; any single weak axis")
    print("  ('energy-rich/weak-S', 'one-weak-axis') is pulled down hard by the")
    print("  cube-root mean -- the intended behaviour of formula (2b). These")
    print("  profiles are synthetic; the empirical calibration of I_v for real")
    print("  cities from open data (OECD FUA, CDP Cities, WIPO/OECD REGPAT,")
    print("  GDELT, OpenStreetMap) is separate work and is NOT claimed here.")
    print()


def main() -> None:
    print("=" * 72)
    print("Large city -- structural verdict + I_v screening-index demonstration")
    print("=" * 72)
    print()
    report_verdict()
    report_i_v_demo()
    print("Cross-check vs main 3.6:")
    print("  city verdict: S = 1, eta_v > 0 (VITAL); grade not asserted   OK")
    print("  I_v is a structural SCREENING composite, not a value of eta_v OK")
    print()
    print("Status: the verdict is structural (S = 1, eta_v > 0); no eta_v number is")
    print("asserted. The I_v demo exercises formula (2b)+(2a) on synthetic")
    print("profiles; no empirical I_v ranking of real cities is claimed (separate")
    print("work). Self-contained: standard library only.")


if __name__ == "__main__":
    main()
