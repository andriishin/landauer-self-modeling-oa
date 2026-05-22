"""
eta_L for E. coli chemotaxis loop — central worked example.

Reproduces the numerical estimate from § 3.5 of «Vitality as a Landauer
Efficiency of Self-Modeling» (Andriishin, in preparation for Entropy).

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
# Parameters for E. coli chemotaxis (central literature values)
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
# Reference for the 10^-3 number: Mehta & Schwab 2012, PNAS.
ETA_EX_EXERGETIC = 1.0
ETA_EX_COMPUTATIONAL = 1.0e-3

# Predictive information held by the chemotaxis loop about its own ligand
# environment, integrated over chemotactic memory and one generation.
# Central order-of-magnitude estimate from literature:
#   - Cheong et al. 2011: ~1-2 bits per measurement, ~10^3-10^4 measurements;
#   - Shimizu, Tu & Berg 2010: extended chemotactic memory;
#   - Mehta & Schwab 2012: bookkeeping of bits per energy budget.
I_PRED = 1.0e4  # bits / cell / generation


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
    print("Inputs (central order-of-magnitude estimates):")
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
    print("Cross-check vs paper § 3.5 (central values):")
    print("  eta_L  ~ 3e-8  (exergetic)         OK" if math.isclose(
        eta_L_ex, 3e-8, rel_tol=0.5) else f"  MISMATCH: {eta_L_ex:.3e}")
    print("  eta_L  ~ 3e-5  (computational)     OK" if math.isclose(
        eta_L_comp, 3e-5, rel_tol=0.5) else f"  MISMATCH: {eta_L_comp:.3e}")
    print()
    print("Status: methodological calibration. Sensitivity over four-order")
    print("input ranges — see sensitivity.py.")


if __name__ == "__main__":
    main()
