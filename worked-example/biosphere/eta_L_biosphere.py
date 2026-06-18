"""
eta_L for Earth's biosphere (Gaia case) — § 3.7 worked example.

Computes the Landauer efficiency of self-modeling for the biosphere
treated as a single planetary-scale compressor: NPP-driven exergetic
budget integrated over an annual window, with predictive information
estimated by the unique (non-copy-number) genomic content.

Run:
    python eta_L_biosphere.py
"""

from __future__ import annotations

import math


# ---------------------------------------------------------------------------
# Physical constants
# ---------------------------------------------------------------------------

K_BOLTZMANN = 1.380649e-23  # J / K
LN2 = math.log(2)


# ---------------------------------------------------------------------------
# Biosphere parameters (literature order-of-magnitude estimates)
# ---------------------------------------------------------------------------

T_SURFACE = 288.0  # K, mean global surface temperature

# Net primary production: total chemical free energy fixed by photosynthesis
# per unit time, globally (paper § 3.7 reference value).
NPP_POWER = 1.0e14  # W

# Integration window: annual biogeochemical cycle.
TAU_YEAR_SEC = 3.156e7  # s

# Predictive information held by the biosphere about its own environment.
# Upper bound by UNIQUE genomic content (NOT copy-number) corrected for the
# fraction of bases plausibly carrying predictive MI about the environment
# (regulatory + protein-coding sites; not the whole nucleotide ledger):
# ~10^20 bits as a defensible ceiling on substrate capacity, not a measured
# predictive MI.
# This is deliberately NOT the total copy-number DNA of the biosphere
# (~1e37 bits, Landenmark, Forgan & Cockell 2015) — copy-number is ~17
# orders larger and irrelevant to predictive mutual information (a
# repeated genome adds no predictive MI about the environment). Likewise,
# the raw unique-genome upper bound (~10^24 bits) over-counts non-coding
# bases that carry no predictive MI about the abiotic environment.
I_PRED = 1.0e20

# Computational denominator: fraction of NPP-driven dissipation that funds
# irreversible information operations (signalling, regulation, neural and
# biochemical computation across the biosphere). Central order-of-magnitude
# estimate ~1e-3 (main § 3.7); sensitivity scan over [1e-3, 1e-2].
E_COMP_FRACTION = 1.0e-3
E_COMP_FRACTION_RANGE = (1.0e-3, 1.0e-2)


# ---------------------------------------------------------------------------
# Calculation
# ---------------------------------------------------------------------------


def landauer_cost_per_bit(temperature: float) -> float:
    return K_BOLTZMANN * temperature * LN2


def n_max(npp_power: float, tau: float, temperature: float) -> float:
    e_actual = npp_power * tau
    return e_actual / landauer_cost_per_bit(temperature)


def eta_L(i_pred: float, n_max_value: float) -> float:
    return i_pred / n_max_value


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def main() -> None:
    cost = landauer_cost_per_bit(T_SURFACE)
    e_actual = NPP_POWER * TAU_YEAR_SEC
    nmax = n_max(NPP_POWER, TAU_YEAR_SEC, T_SURFACE)
    eta_L_value = eta_L(I_PRED, nmax)

    print("=" * 72)
    print("eta_L for Earth's biosphere — § 3.7 (annual window)")
    print("=" * 72)
    print()
    print("Inputs:")
    print(f"  T (surface)           = {T_SURFACE:>8.1f}    K")
    print(f"  NPP                   = {NPP_POWER:>8.2e}  W")
    print(f"  tau (annual cycle)    = {TAU_YEAR_SEC:>8.3e}  s")
    print(f"  I_pred (biomass eq.)  = {I_PRED:>8.2e}  bits")
    print()
    print("Derived:")
    print(f"  k_B * T * ln 2        = {cost:>8.3e}  J/bit")
    print(f"  E_actual = NPP * tau  = {e_actual:>8.3e}  J/year")
    print(f"  N_max                 = {nmax:>8.3e}  bits/year")
    print()
    print("Result:")
    print(f"  eta_L (exergetic)     = {eta_L_value:>8.3e}")
    print()
    print("Sensitivity over alternative I_pred and tau choices:")
    print("-" * 72)
    print(f"  {'I_pred (bits)':>15} {'tau':>22} {'eta_L':>15}")
    print("-" * 72)
    for ipred_label, ipred in [
        ("1e15 (atm. pools)", 1.0e15),
        ("1e19 (eco. memory low)", 1.0e19),
        ("1e20 (coding-bound)", 1.0e20),
        ("1e22 (eco. memory high)", 1.0e22),
    ]:
        for tau_label, tau in [
            ("1 day", 86400.0),
            ("1 year", TAU_YEAR_SEC),
            ("1 millennium", 3.156e10),
        ]:
            nm = n_max(NPP_POWER, tau, T_SURFACE)
            eta = eta_L(ipred, nm)
            print(f"  {ipred_label:>20} {tau_label:>15} {eta:>15.2e}")
    print()
    print("Cross-check vs paper § 3.7 (annual window, coding-bound I_pred):")
    print(f"  eta_L (exergetic) ~ 1e-22                              ",
          "OK" if 1e-23 < eta_L_value < 1e-21 else f"got {eta_L_value:.2e}")
    print()
    # -------------------------------------------------------------------
    # Computational-denominator branch: eta_L^comp = I_pred / N_max^comp
    # with N_max^comp = E_comp / (k_B T ln 2),  E_comp = f * NPP * tau.
    # -------------------------------------------------------------------
    print("Computational-denominator branch (E_comp = f * NPP * tau):")
    print("-" * 72)
    print(f"  {'f = E_comp/E_actual':>22} {'N_max^comp (bits/year)':>26}"
          f" {'eta_L^comp':>14}")
    print("-" * 72)
    eta_comp_central = None
    for f in (1.0e-3, 3.0e-3, 1.0e-2):
        e_comp = f * NPP_POWER * TAU_YEAR_SEC
        nmax_comp = e_comp / cost
        eta_comp = I_PRED / nmax_comp
        if abs(f - E_COMP_FRACTION) < 1e-12:
            eta_comp_central = eta_comp
        print(f"  {f:>22.1e} {nmax_comp:>26.3e} {eta_comp:>14.3e}")
    print()
    print("Cross-check vs paper § 3.7 (computational, central f = 1e-3):")
    if eta_comp_central is None:
        eta_comp_central = I_PRED / (E_COMP_FRACTION * NPP_POWER * TAU_YEAR_SEC / cost)
    print(f"  eta_L^comp <~ 1e-19                                    ",
          "OK" if 1e-20 < eta_comp_central < 1e-18
          else f"got {eta_comp_central:.2e}")
    print()
    print("Status: methodological calibration. Single-compressor reading; the")
    print("alternative reading (biosphere as overlapping family of subsystems)")
    print("is discussed in § 3.7 and remains an open empirical question.")


if __name__ == "__main__":
    main()
