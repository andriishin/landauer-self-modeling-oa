"""
eta_L for an LLM as embedded in a corporate operator — § 3.4 boundary.

The paper § 3.4 distinguishes three readings of LLM as a candidate for
positive eta_L:

  - operational: 'model + data center'  → eta_L > 0 by external metrics
  - interpretive: 'weights at inference' → eta_L undefined (simultaneous
    T_v + C_v failure: no causally relevant own environment AND no
    internal dissipation paying for the weights)
  - extension: 'model + data center + corporation' → eta_L > 0 but the
    measured object is the corporation, not the model.

This worked example operationalizes the third reading: corporation as a
socio-technical system with an annual energy budget (data center + office
+ supply chain) and an aggregate predictive information held about its
operating environment (training corpus + operational memory + market
intelligence).

Run:
    python eta_L_llm_corp.py
"""

from __future__ import annotations

import math


# ---------------------------------------------------------------------------
# Physical constants
# ---------------------------------------------------------------------------

K_BOLTZMANN = 1.380649e-23  # J / K
LN2 = math.log(2)


# ---------------------------------------------------------------------------
# Corporation parameters (mid-size frontier-AI lab, order-of-magnitude)
# ---------------------------------------------------------------------------

T_OFFICE = 300.0  # K, server-room operating temperature (paper § 2.1 standardized T for LLM / data center)
WINDOW_YEAR_SEC = 3.156e7  # s

# Annual energy budget. Components:
#   - data center training & inference: ~100 MW continuous = 3.15e15 J/year
#   - office HVAC, lighting, equipment: ~10 MW = 3.15e14 J/year
#   - supply chain (manufacturing, logistics, employees commute): ~1 GW
#     amortized = 3.15e16 J/year
# Total ~ 3.5e16 J/year for a major lab.
E_DATACENTER = 3.15e15
E_OFFICE = 3.15e14
E_SUPPLY_CHAIN = 3.15e16
E_ACTUAL_TOTAL_PER_YEAR = E_DATACENTER + E_OFFICE + E_SUPPLY_CHAIN

# Predictive information held by the corporation about its operating
# environment. Components:
#   - training corpus compressed in weights: ~1e12 bits (entropy of training
#     data times compression factor)
#   - operational memory (logs, customer interactions, internal docs): ~1e11
#   - market intelligence (research, competitive analysis, regulatory): ~1e10
# Total ~ 1.1e12 bits of predictive structure relevant to corporate operation.
I_PRED_TRAINING = 1.0e12
I_PRED_OPERATIONS = 1.0e11
I_PRED_MARKET = 1.0e10
I_PRED_TOTAL = I_PRED_TRAINING + I_PRED_OPERATIONS + I_PRED_MARKET


# ---------------------------------------------------------------------------
# Calculation
# ---------------------------------------------------------------------------


def landauer_cost_per_bit(temperature: float) -> float:
    return K_BOLTZMANN * temperature * LN2


def n_max(e_actual: float, eta_ex: float, temperature: float) -> float:
    return e_actual * eta_ex / landauer_cost_per_bit(temperature)


def eta_L(i_pred: float, n_max_value: float) -> float:
    return i_pred / n_max_value


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def main() -> None:
    cost = landauer_cost_per_bit(T_OFFICE)

    nmax_ex = n_max(E_ACTUAL_TOTAL_PER_YEAR, eta_ex=1.0, temperature=T_OFFICE)

    eta_L_ex = eta_L(I_PRED_TOTAL, nmax_ex)

    print("=" * 78)
    print("eta_L for LLM-as-corporation — § 3.4 extended boundary")
    print("=" * 78)
    print()
    print("Energy budget (annual, frontier-AI lab order-of-magnitude):")
    print(f"  data center                 {E_DATACENTER:.2e} J/year")
    print(f"  office & operations         {E_OFFICE:.2e} J/year")
    print(f"  supply chain (amortized)    {E_SUPPLY_CHAIN:.2e} J/year")
    print(f"  total E_actual              {E_ACTUAL_TOTAL_PER_YEAR:.2e} J/year")
    print()
    print("Predictive information:")
    print(f"  training corpus in weights  {I_PRED_TRAINING:.2e} bits")
    print(f"  operational memory          {I_PRED_OPERATIONS:.2e} bits")
    print(f"  market intelligence         {I_PRED_MARKET:.2e} bits")
    print(f"  total I_pred                {I_PRED_TOTAL:.2e} bits")
    print()
    print("Derived:")
    print(f"  T (office)                  {T_OFFICE:.1f} K")
    print(f"  k_B * T * ln 2              {cost:.3e} J/bit")
    print(f"  N_max  (exergetic)          {nmax_ex:.3e} bits")
    print()
    print("Result:")
    print(f"  eta_L^corp  (exergetic)     {eta_L_ex:.3e}")
    print()
    print("Reading.")
    print("  Through the exergetic denominator, eta_L^corp is positive but")
    print("  vanishingly small. The corporation has a much larger absolute predictive")
    print("  structure than a bacterial cell, but its energy budget scales")
    print("  much faster than its information-relevant operations: most of")
    print("  the joules go to logistics, manufacturing, HVAC, and cooling")
    print("  overhead, not to bit-flipping in support of self-model maintenance.")
    print()
    print("Cross-check vs paper § 3.4:")
    print(f"  eta_L^corp ~ 10^-25 (exergetic)                         ",
          "OK" if 1e-26 < eta_L_ex < 1e-24 else f"got {eta_L_ex:.2e}")


if __name__ == "__main__":
    main()
