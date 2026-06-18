"""
eta_L for E. coli chemotaxis loop — central worked example.

Reproduces the numerical estimate from § 3.5 of «Vitality as a Landauer
Efficiency of Self-Modeling» (Andriishin, in preparation for Theory in Biosciences).

Run:
    python eta_L_ecoli.py

Expected output is captured in expected_output.txt.
"""

from __future__ import annotations

import math


# ---------------------------------------------------------------------------
# Physical constants
# ---------------------------------------------------------------------------

K_BOLTZMANN = 1.380649e-23  # J / K, exact (SI 2019 redefinition)
LN2 = math.log(2)


# ---------------------------------------------------------------------------
# Parameters for E. coli chemotaxis (point estimates via upper-bound I_pred;
# see § 3.5 for the distinction between point estimates and geometric medians
# of the sensitivity intervals).
# ---------------------------------------------------------------------------

T_PHYSIOLOGICAL = 310.0  # K, body / lab temperature for E. coli

# Total exergetic budget of one E. coli cell over one generation.
# Order-of-magnitude estimate: metabolic power ~10^-12 W, generation ~30 min.
# Equivalently: ~10^10 ATP molecules per generation × ΔG_ATP ≈ 50 kJ/mol.
E_ACTUAL_TOTAL = 1.0e-9  # J / cell / generation

# Exergetic efficiency factor:
#   = 1.0 for the "exergetic" denominator (full thermodynamic budget),
#   ≈ 1e-3 for the "computational" denominator — the fraction of dissipation
#   actually spent on irreversible information operations.
# The 10^-3 fraction is our own order-of-magnitude estimate: ratio of the
# sensory-computational network power (Mehta & Schwab 2012) to the full
# metabolic budget (Liu et al. 2020) — not a number taken from Mehta & Schwab.
ETA_EX_EXERGETIC = 1.0
ETA_EX_COMPUTATIONAL = 1.0e-3

# Predictive information held by the chemotaxis loop about its own ligand
# environment, integrated over chemotactic memory and one generation.
# Point estimate via upper bound (independence-of-channels assumption);
# cooperative coupling in receptor clusters reduces the effective I_pred
# by ~1 order. Geometric medians of the sensitivity intervals
# [1e-9, 1e-7] / [1e-6, 1e-4] are 1e-8 / 1e-5 (used as reference values
# in § 7 of the paper). Literature support:
#   - Cheong et al. 2011: ~1-2 bits per measurement, ~10^3-10^4 measurements;
#   - Shimizu, Tu & Berg 2010: extended chemotactic memory;
#   - Mehta & Schwab 2012: bookkeeping of bits per energy budget.
I_PRED = 1.0e4  # bits / cell / generation, upper-bound point estimate


# ---------------------------------------------------------------------------
# Core calculation
# ---------------------------------------------------------------------------


def landauer_cost_per_bit(temperature: float) -> float:
    """Landauer minimum dissipation per erased bit (J/bit) at given T."""
    return K_BOLTZMANN * temperature * LN2


def n_max(e_actual_total: float, eta_ex: float, temperature: float) -> float:
    """
    Maximum number of bits that can be erased irreversibly on the available
    exergy E_actual = E_actual_total * eta_ex at temperature T.

    Implements equation (1) of the paper.
    """
    e_actual = e_actual_total * eta_ex
    return e_actual / landauer_cost_per_bit(temperature)


def eta_L(i_pred: float, n_max_value: float) -> float:
    """Landauer efficiency of self-modeling: dimensionless ratio in [0, 1]."""
    return i_pred / n_max_value


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


def main() -> None:
    cost = landauer_cost_per_bit(T_PHYSIOLOGICAL)

    n_max_ex = n_max(E_ACTUAL_TOTAL, ETA_EX_EXERGETIC, T_PHYSIOLOGICAL)
    n_max_comp = n_max(E_ACTUAL_TOTAL, ETA_EX_COMPUTATIONAL, T_PHYSIOLOGICAL)

    eta_L_ex = eta_L(I_PRED, n_max_ex)
    eta_L_comp = eta_L(I_PRED, n_max_comp)

    print("=" * 72)
    print("eta_L for E. coli chemotaxis loop — worked example")
    print("=" * 72)
    print()
    print("Inputs (point estimates via upper-bound I_pred = 10^4 bits;")
    print("geometric medians of [1e-9,1e-7] / [1e-6,1e-4] sensitivity")
    print("intervals are 1e-8 / 1e-5, used as reference in § 7):")
    print(f"  T                     = {T_PHYSIOLOGICAL:>8.1f}    K")
    print(f"  E_actual^total        = {E_ACTUAL_TOTAL:>8.2e}  J / cell / generation")
    print(f"  I_pred                = {I_PRED:>8.2e}  bits / cell / generation")
    print(f"  eta_ex (exergetic)    = {ETA_EX_EXERGETIC:>8.2e}")
    print(f"  eta_ex (computational)= {ETA_EX_COMPUTATIONAL:>8.2e}")
    print()
    print("Derived:")
    print(f"  k_B * T * ln 2        = {cost:>8.3e}  J / bit")
    print(f"  N_max  (exergetic)    = {n_max_ex:>8.3e}  bits / cell")
    print(f"  N_max  (computational)= {n_max_comp:>8.3e}  bits / cell")
    print()
    print("Result:")
    print(f"  eta_L  (exergetic)    = {eta_L_ex:>8.3e}")
    print(f"  eta_L  (computational)= {eta_L_comp:>8.3e}")
    print()
    print("Cross-check vs paper § 3.5 (point estimates via upper-bound")
    print("I_pred = 10^4 bits; geometric medians of [1e-9,1e-7] / [1e-6,1e-4]")
    print("ranges are 1e-8 / 1e-5):")
    print("  eta_L  ~ 3e-8  (exergetic)         OK" if math.isclose(
        eta_L_ex, 3e-8, rel_tol=0.5) else f"  MISMATCH: {eta_L_ex:.3e}")
    print("  eta_L  ~ 3e-5  (computational)     OK" if math.isclose(
        eta_L_comp, 3e-5, rel_tol=0.5) else f"  MISMATCH: {eta_L_comp:.3e}")
    print()
    print()
    print("Cooperative-coupling scan (formula 1 with I_pred / k):")
    print("-" * 72)
    print(f"  {'factor k':>10} {'I_pred/k (bits)':>18} {'eta_L (exer.)':>16}"
          f" {'eta_L (comp.)':>16}")
    print("-" * 72)
    for k_factor in (1.0, 3.0, 10.0):
        ipred_eff = I_PRED / k_factor
        eta_ex_k = eta_L(ipred_eff, n_max_ex)
        eta_co_k = eta_L(ipred_eff, n_max_comp)
        print(f"  {k_factor:>10.1f} {ipred_eff:>18.2e} {eta_ex_k:>16.3e}"
              f" {eta_co_k:>16.3e}")
    print()
    print("Note: cooperative coupling in receptor clusters reduces effective")
    print("I_pred by ~1 order; lower bound of sensitivity interval [1e-9, 1e-7]")
    print("is reached at factor k = 10 (matches § 3.5 lower bound).")
    print()
    print("Status: methodological calibration. Sensitivity over four-order")
    print("input ranges — see sensitivity.py.")


if __name__ == "__main__":
    main()
