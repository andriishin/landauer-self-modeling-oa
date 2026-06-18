"""
eta_L for a large city + I_v composite-formula demonstration — § 3.6.

Two clearly separated parts, both self-contained (standard library
only; no external, empirical, or unpublished dependency):

  PART 1 — eta_L (the camertone claim of § 3.6).
      For a major city, eta_L through the exergetic denominator is
      computed from first principles via formula (1):
          N_max = E_actual / (k_B T ln 2),   eta_L = I_pred / N_max.
      Singapore and Detroit are used only as order-of-magnitude
      energy-budget examples. This needs no cohort and no I_v; every
      number is reproducible from the inputs in this file. The
      substantive § 3.6 statement is: a city is structurally complex
      yet eta_L is vanishing (~3e-30).

  PART 2 — I_v composite, formula (2)+(2a), as a METHOD demo.
      I_v = cube_root(T_v * C_v * S_v), with T_v/C_v/S_v the
      percentile-normalized (formula 2a) capacities within a cohort.
      This part runs on an explicitly SYNTHETIC set of archetype
      profiles — it demonstrates the mechanics of the composite
      (geometric mean punishes any weak capacity; percentile rank is
      cohort-relative). It is NOT an empirical ranking of real cities:
      the empirical calibration of I_v for specific cities from open
      data (OECD FUA, CDP Cities, WIPO/OECD REGPAT, GDELT,
      OpenStreetMap) is a separate piece of work and is deliberately
      not asserted here.

Run:
    python eta_L_city.py
"""

from __future__ import annotations

import math

# ---------------------------------------------------------------------------
# Physical constants
# ---------------------------------------------------------------------------

K_BOLTZMANN = 1.380649e-23  # J / K
LN2 = math.log(2)

T_TEMPERATE = 285.0  # K, mean annual surface temperature, temperate climate
WINDOW_YEAR_SEC = 3.156e7  # s, one calendar year (~365.25 d)

# ---------------------------------------------------------------------------
# PART 1 — eta_L: real cities, reproducible from the energy/info budget
# ---------------------------------------------------------------------------
#
# Order-of-magnitude estimates: full metropolitan dissipation; I_pred
# an upper bound by administrative-infrastructure carrier capacity
# (not a measured predictive information — operationalization open,
# as for the biosphere and the LLM-corporation). Consistent with
# paper § 3.6. No cohort, no I_v involved here.

CITY_ENERGY: dict[str, dict] = {
    "Singapore": {
        "population": 5.7e6,
        "E_actual_total_per_year": 1.0e19,  # J/year, full metropolitan dissipation
        "I_pred_admin": 1.0e10,             # bits, upper bound by carrier capacity
    },
    "Detroit": {
        "population": 3.5e6,                # metro area
        "E_actual_total_per_year": 5.0e18,  # J/year, post-industrial dissipation
        "I_pred_admin": 1.0e10,             # bits, same carrier-capacity upper bound
    },
}

# Computational-denominator fraction for the city: share of metropolitan
# dissipation funding irreversible information operations of administrative
# computation (data centres + operational electrics of admin offices),
# main § 3.6 central estimate ~1e-4. Sensitivity scan over [1e-5, 1e-3].
E_COMP_FRACTION_CITY = 1.0e-4
E_COMP_FRACTION_CITY_RANGE = (1.0e-5, 1.0e-3)

# Conservative upper bound on eta_L (main § 3.6): direct municipal electricity
# consumption only (~10 GW * 1 year ~ 1e17 J/year) is the smallest plausible
# E_actual and hence yields the largest (loosest) upper bound on eta_L. This
# gives eta_L <~ 3e-28, vs ~3e-30 at the full ~1e19 J/year supply-chain budget.
E_DIRECT_CONSUMPTION_PER_YEAR = 1.0e17  # J/year, direct electricity only
I_PRED_ADMIN_BOUND = 1.0e10             # bits, carrier-capacity upper bound


def landauer_cost_per_bit(temperature: float) -> float:
    return K_BOLTZMANN * temperature * LN2


def n_max_year(e_actual_year: float, temperature: float) -> float:
    return e_actual_year / landauer_cost_per_bit(temperature)


def eta_L(i_pred: float, n_max_value: float) -> float:
    return i_pred / n_max_value


def report_eta_L() -> dict[str, float]:
    print("PART 1 — eta_L (formula 1), reproducible from the energy budget")
    print("-" * 72)
    print(f"  T (temperate climate) = {T_TEMPERATE:>8.1f}    K")
    print(f"  k_B * T * ln 2        = {landauer_cost_per_bit(T_TEMPERATE):>8.3e}  J/bit")
    print(f"  Window                = 1 year ({WINDOW_YEAR_SEC:.2e} s)")
    print()
    out: dict[str, float] = {}
    for name, e in CITY_ENERGY.items():
        nmax = n_max_year(e["E_actual_total_per_year"], T_TEMPERATE)
        eta = eta_L(e["I_pred_admin"], nmax)
        out[name] = eta
        print(f"  {name}:")
        print(f"    population          = {e['population']:>8.2e}  people")
        print(f"    E_actual/year       = {e['E_actual_total_per_year']:>8.2e}  J/year")
        print(f"    I_pred (admin, <=)  = {e['I_pred_admin']:>8.2e}  bits")
        print(f"    N_max (per year)    = {nmax:>8.3e}  bits")
        print(f"    eta_L (exergetic)   = {eta:>8.3e}")
    ratio = out["Detroit"] / out["Singapore"]
    print()
    print(f"  eta_L(Detroit)/eta_L(Singapore) = {ratio:.2f}x")
    print("  Camertone claim: a city is structurally complex yet eta_L")
    print("  is vanishing (~3e-30) — vitally negligible. No cohort or")
    print("  I_v is needed for this; every number above is reproducible")
    print("  from the inputs in this file.")
    print()
    nmax_direct = n_max_year(E_DIRECT_CONSUMPTION_PER_YEAR, T_TEMPERATE)
    eta_direct = eta_L(I_PRED_ADMIN_BOUND, nmax_direct)
    ok_bound = "OK" if 1e-28 < eta_direct < 1e-27 else f"got {eta_direct:.2e}"
    print("  Conservative upper bound (direct municipal electricity only,")
    print(f"  E_actual ~ {E_DIRECT_CONSUMPTION_PER_YEAR:.0e} J/year -> smallest N_max):")
    print(f"    N_max (per year)    = {nmax_direct:>8.3e}  bits")
    print(f"    eta_L <=              {eta_direct:>8.3e}")
    print(f"    cross-check vs main § 3.6 (<~ 3e-28): {ok_bound}")
    print()
    print("  Computational-denominator branch")
    print("  (E_comp = f * E_actual, f ~ 1e-4 central, see main § 3.6):")
    print("  " + "-" * 70)
    print(f"  {'city':<12} {'f = E_comp/E_actual':>22} {'eta_L^comp':>18}")
    print("  " + "-" * 70)
    for name, eta_ex_value in out.items():
        for f in (1.0e-5, 1.0e-4, 1.0e-3):
            eta_comp = eta_ex_value / f
            print(f"  {name:<12} {f:>22.1e} {eta_comp:>18.3e}")
    print()
    print("  Note: with f ~ 1e-4 (Singapore), eta_L^comp ~ 3e-26 — matches")
    print("  the main § 3.6 statement that the computational denominator")
    print("  brings the city ~4 orders closer to the biological range,")
    print("  yet still ~21 orders below the bacterial reference.")
    print()
    return out


# ---------------------------------------------------------------------------
# PART 2 — I_v composite (formula 2 + 2a): METHOD demonstration only
# ---------------------------------------------------------------------------
#
# SYNTHETIC archetype profiles. The raw "proxy" numbers below are
# illustrative placeholders chosen to exercise the formula, NOT
# measurements of any real city. They show two things:
#   (2a) percentile normalization maps raw proxies to [0, 1] ranks
#        relative to the cohort;
#   (2)  I_v = cube_root(T_v * C_v * S_v): the geometric mean drags
#        the composite toward any weak capacity.

# (label, raw_T, raw_C, raw_S) — arbitrary illustrative units.
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
    """Average-rank percentile in (0, 1] — formula (2a)."""
    n = len(population)
    less = sum(1 for x in population if x < value)
    equal = sum(1 for x in population if x == value)
    return (less + (equal + 1) / 2.0) / n


def geometric_mean(values: tuple[float, ...]) -> float:
    """Formula (2): n-th root of the product; 0 if any component is 0."""
    if any(v < 0 for v in values):
        raise ValueError("negative capacity")
    if any(v == 0 for v in values):
        return 0.0
    return math.exp(sum(math.log(v) for v in values) / len(values))


def report_i_v_demo() -> None:
    labels = [c[0] for c in SYNTHETIC_COHORT]
    raw_t = [c[1] for c in SYNTHETIC_COHORT]
    raw_c = [c[2] for c in SYNTHETIC_COHORT]
    raw_s = [c[3] for c in SYNTHETIC_COHORT]

    print("PART 2 — I_v composite, formula (2)+(2a): METHOD demo on a")
    print("SYNTHETIC cohort (illustrative placeholders, NOT real cities)")
    print("-" * 72)
    print(f"  {'profile':<20} {'T_v':>6} {'C_v':>6} {'S_v':>6} {'I_v':>7}  phase")
    rows = []
    for label, rt, rc, rs in SYNTHETIC_COHORT:
        t_v = percentile_rank(rt, raw_t)
        c_v = percentile_rank(rc, raw_c)
        s_v = percentile_rank(rs, raw_s)
        i_v = geometric_mean((t_v, c_v, s_v))
        rows.append((label, t_v, c_v, s_v, i_v))
    for label, t_v, c_v, s_v, i_v in sorted(rows, key=lambda r: -r[4]):
        phase = ("hyper-vital" if i_v >= 0.85 else "vital" if i_v >= 0.5
                 else "transitional" if i_v >= 0.4 else "proto-vital"
                 if i_v >= 0.1 else "abiotic")
        print(f"  {label:<20} {t_v:>6.3f} {c_v:>6.3f} {s_v:>6.3f} {i_v:>7.3f}  {phase}")
    print()
    print("  Reading: 'uniformly-high' tops the composite; any single")
    print("  weak axis ('energy-rich/weak-S', 'one-weak-axis') is pulled")
    print("  down hard by the geometric mean — that is the intended")
    print("  behaviour of formula (2). These profiles are synthetic; the")
    print("  empirical calibration of I_v for specific real cities from")
    print("  open data is separate work and is NOT claimed here.")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    print("=" * 72)
    print("eta_L for a large city + I_v composite-formula demonstration")
    print("=" * 72)
    print()

    eta = report_eta_L()
    report_i_v_demo()

    print("Cross-check vs paper § 3.6:")
    print("  eta_L ~ 3e-30 (exergetic, large city)                  ",
          "OK" if all(1e-30 < e < 1e-28 for e in eta.values()) else "MISMATCH")
    print("  eta_L(Detroit) > eta_L(Singapore) (smaller budget)     ",
          "OK" if eta["Detroit"] > eta["Singapore"] else "MISMATCH")
    eta_comp_singapore = eta["Singapore"] / E_COMP_FRACTION_CITY
    print("  eta_L^comp ~ 3e-26 (Singapore, f = 1e-4)               ",
          "OK" if 1e-26 < eta_comp_singapore < 1e-25
          else f"got {eta_comp_singapore:.2e}")
    print()
    print("Status: PART 1 (eta_L) is the reproducible § 3.6 camertone —")
    print("a city is structurally complex but vitally negligible. PART 2")
    print("demonstrates the I_v composite formula on synthetic profiles;")
    print("no empirical I_v ranking of real cities is asserted (that is")
    print("separate work). Self-contained: standard library only.")


if __name__ == "__main__":
    main()
