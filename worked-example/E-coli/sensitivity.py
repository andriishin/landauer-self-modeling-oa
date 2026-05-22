"""
Sensitivity analysis for eta_L of E. coli chemotaxis loop.

Sweeps four parameters over their plausible literature ranges and reports
the resulting distribution of eta_L (both exergetic and computational).

Run:
    python sensitivity.py
"""

from __future__ import annotations

import math
import statistics

from eta_L_ecoli import (
    K_BOLTZMANN,
    LN2,
    eta_L,
    landauer_cost_per_bit,
    n_max,
)


# ---------------------------------------------------------------------------
# Parameter ranges (literature plausibility intervals)
# ---------------------------------------------------------------------------

# Predictive information: 10^3 to 10^5 bits per cell per generation.
# Lower bound: minimal chemotactic memory of ~10^3 bits (basic adaptation);
# upper bound: aggressive estimate from Cheong et al. 2011.
I_PRED_RANGE = (1.0e3, 1.0e5)

# Total exergetic budget per cell per generation:
# 10^-10 (slow growth, minimal medium) to 10^-8 (rapid growth, rich medium).
E_ACTUAL_RANGE = (1.0e-10, 1.0e-8)

# Exergetic efficiency for computational denominator:
# 10^-4 to 10^-2 (fraction of dissipation on irreversible information ops).
ETA_EX_COMP_RANGE = (1.0e-4, 1.0e-2)

# Temperature: 25-42 °C (lab/physiological extremes for E. coli growth).
T_RANGE = (273.15 + 25.0, 273.15 + 42.0)

# Number of grid points per parameter (full grid for reproducibility,
# replace with random sampling for higher-dimensional sweeps).
N_GRID = 7


# ---------------------------------------------------------------------------
# Sweep
# ---------------------------------------------------------------------------


def log_grid(low: float, high: float, n: int) -> list[float]:
    """Logarithmically spaced grid from low to high (inclusive)."""
    if n == 1:
        return [math.sqrt(low * high)]
    log_low, log_high = math.log10(low), math.log10(high)
    step = (log_high - log_low) / (n - 1)
    return [10.0 ** (log_low + i * step) for i in range(n)]


def linear_grid(low: float, high: float, n: int) -> list[float]:
    if n == 1:
        return [(low + high) / 2.0]
    step = (high - low) / (n - 1)
    return [low + i * step for i in range(n)]


def sweep_exergetic() -> list[float]:
    results: list[float] = []
    for i_pred in log_grid(*I_PRED_RANGE, N_GRID):
        for e_actual in log_grid(*E_ACTUAL_RANGE, N_GRID):
            for temperature in linear_grid(*T_RANGE, N_GRID):
                nmax = n_max(e_actual, eta_ex=1.0, temperature=temperature)
                results.append(eta_L(i_pred, nmax))
    return results


def sweep_computational() -> list[float]:
    results: list[float] = []
    for i_pred in log_grid(*I_PRED_RANGE, N_GRID):
        for e_actual in log_grid(*E_ACTUAL_RANGE, N_GRID):
            for eta_ex_comp in log_grid(*ETA_EX_COMP_RANGE, N_GRID):
                for temperature in linear_grid(*T_RANGE, N_GRID):
                    nmax = n_max(e_actual, eta_ex_comp, temperature)
                    results.append(eta_L(i_pred, nmax))
    return results


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def report(label: str, results: list[float]) -> None:
    log_results = [math.log10(x) for x in results if x > 0]
    log_min, log_max = min(log_results), max(log_results)
    log_med = statistics.median(log_results)
    log_geom_mean = statistics.mean(log_results)
    spread_orders = log_max - log_min

    print(f"--- {label} ---")
    print(f"  N samples           = {len(results):d}")
    print(f"  min                 = 10^{log_min:>+6.2f}  = {10 ** log_min:.2e}")
    print(f"  geometric median    = 10^{log_med:>+6.2f}  = {10 ** log_med:.2e}")
    print(f"  geometric mean      = 10^{log_geom_mean:>+6.2f}  = {10 ** log_geom_mean:.2e}")
    print(f"  max                 = 10^{log_max:>+6.2f}  = {10 ** log_max:.2e}")
    print(f"  spread              = {spread_orders:>5.2f} orders of magnitude")
    print()


def main() -> None:
    print("=" * 72)
    print("Sensitivity analysis — eta_L for E. coli chemotaxis loop")
    print("=" * 72)
    print()
    print(f"Parameter ranges (log-uniform sweep, {N_GRID} grid points each):")
    print(f"  I_pred         : {I_PRED_RANGE[0]:.1e} ... {I_PRED_RANGE[1]:.1e} bits")
    print(f"  E_actual^total : {E_ACTUAL_RANGE[0]:.1e} ... {E_ACTUAL_RANGE[1]:.1e} J")
    print(f"  eta_ex (comp.) : {ETA_EX_COMP_RANGE[0]:.1e} ... {ETA_EX_COMP_RANGE[1]:.1e}")
    print(f"  T              : {T_RANGE[0]:.1f} ... {T_RANGE[1]:.1f} K")
    print()

    exergetic = sweep_exergetic()
    computational = sweep_computational()

    report("eta_L (exergetic denominator)", exergetic)
    report("eta_L (computational denominator)", computational)

    print("Paper §3.5 ranges for comparison:")
    print("  eta_L  in [1e-9, 1e-7]   (exergetic)")
    print("  eta_L  in [1e-6, 1e-4]   (computational)")


if __name__ == "__main__":
    main()
