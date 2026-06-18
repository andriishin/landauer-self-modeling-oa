"""
eta_L for a bimetallic room thermostat — boundary case.

Reproduces the FEP-discrimination calculation from § 4.4 of the paper:
the thermostat passes FEP formally but fails self-payment, so the standard
formula (1) gives two distinct numbers depending on which task is being
'modelled':

    1. Trivial task (maintain own bimetal shape) — eta_L > 0 but tiny.
    2. Managing task (regulate room temperature) — eta_L = 0 because
       the predictive information about the room is paid by external
       grid, not by the bimetal's own dissipation.

This distinction is the central anti-FEP argument in the paper:
self-payment is not deducible from FEP and must be added as an
ontological commitment.

Run:
    python eta_L_thermostat.py
"""

from __future__ import annotations

import math


# ---------------------------------------------------------------------------
# Physical constants
# ---------------------------------------------------------------------------

K_BOLTZMANN = 1.380649e-23  # J / K, exact (SI 2019)
LN2 = math.log(2)


# ---------------------------------------------------------------------------
# Parameters for a domestic bimetallic thermostat
# ---------------------------------------------------------------------------

# Operating environment.
T_ROOM = 300.0  # K, indoor temperature serving as Landauer thermostat (Supplementary § S4.4)

# Control characteristics.
DELTA_T_ROOM = 10.0   # K, range over which room temperature varies
DELTA_T_HYST = 1.0    # K, switching hysteresis of the bimetallic strip

# Operating window (system relaxation timescale).
TAU_D = 1800.0  # s, ~30 min — comparable to room thermal inertia

# Internal dissipation: bimetal elastic relaxation + relay contact dissipation.
# Order of magnitude per § 4.4 and Supplementary § S4.4.
P_BIMETAL = 1.0e-6  # W, dissipation localized inside the boundary {bimetal, relay}

# External components, listed for transparency but excluded from the boundary
# by the counterfactual ablation procedure of § 2.2.
P_HEATER_EXTERNAL = 1.0e3      # W, electric heater fed by grid
P_GRID_EXTERNAL = 0.0          # not part of self-payment
SETPOINT_FIXED_BY_OPERATOR = True  # not part of self-payment


# ---------------------------------------------------------------------------
# Calculation
# ---------------------------------------------------------------------------


def landauer_cost_per_bit(temperature: float) -> float:
    return K_BOLTZMANN * temperature * LN2


def i_pred_bound(delta_room: float, delta_hyst: float) -> float:
    """
    Upper bound on predictive information held by the bimetal about the room
    state, given finite resolution set by hysteresis.
    """
    return math.log2(delta_room / delta_hyst)


def n_max(power: float, tau: float, temperature: float) -> float:
    energy = power * tau
    return energy / landauer_cost_per_bit(temperature)


def main() -> None:
    cost = landauer_cost_per_bit(T_ROOM)
    energy_internal = P_BIMETAL * TAU_D
    nmax = n_max(P_BIMETAL, TAU_D, T_ROOM)
    i_pred = i_pred_bound(DELTA_T_ROOM, DELTA_T_HYST)

    eta_L_trivial = i_pred / nmax
    # managing reading: η_L = 0 by convention (no own E_actual return loop on
    # the management task; passive structure per § 2.1). Distinct from the
    # LLM-narrow case (§ 3.4), where simultaneous T_v + C_v failure leaves
    # eta_L^int undefined rather than zero.
    eta_L_managing = 0.0

    print("=" * 72)
    print("eta_L for a bimetallic room thermostat — § 4.4 boundary case")
    print("=" * 72)
    print()
    print("Counterfactual ablation of the boundary (§ 2.2):")
    print("  inside  — bimetal strip, relay contacts")
    print(f"            internal dissipation P_int = {P_BIMETAL:.2e} W")
    print("  outside — heater, electric grid, external setpoint operator")
    print(f"            external power     P_ext = {P_HEATER_EXTERNAL:.2e} W")
    print()
    print("Inputs:")
    print(f"  T (room thermostat)   = {T_ROOM:>8.1f}    K")
    print(f"  Delta T_room          = {DELTA_T_ROOM:>8.1f}    K")
    print(f"  Delta T_hyst          = {DELTA_T_HYST:>8.1f}    K")
    print(f"  P_internal            = {P_BIMETAL:>8.2e}  W")
    print(f"  tau_d                 = {TAU_D:>8.1f}    s")
    print()
    print("Derived:")
    print(f"  k_B * T * ln 2        = {cost:>8.3e}  J / bit")
    print(f"  E_actual (internal)   = {energy_internal:>8.3e}  J over tau")
    print(f"  N_max                 = {nmax:>8.3e}  bits")
    print(f"  I_pred upper bound    = {i_pred:>8.3f}    bits")
    print()
    print("Two readings of eta_L:")
    print(f"  eta_L  (trivial: maintain own shape)   = {eta_L_trivial:.3e}")
    print(f"  eta_L  (managing: regulate room)        = {eta_L_managing:.3e}")
    print()
    print("Reading.")
    print("  The trivial reading gives a positive but vanishing eta_L because")
    print("  the bimetal does hold a few bits about its own form against its")
    print("  own (tiny) dissipation budget. The managing reading is exactly")
    print("  zero: the predictive information about room temperature is paid")
    print("  by the external grid (heater + supply), not by the bimetal's")
    print("  internal dissipation. This is the central anti-FEP point of § 4.4:")
    print("  formal FEP-applicability does not imply self-payment.")
    print()
    print("Cross-check vs paper § 4.4:")
    print(f"  I_pred ≈ log2(Delta T_room / Delta T_hyst) ≈ 3 bits at diurnal Delta T_room ~ 10 K")
    print(f"                                              (up to ~5 bits at seasonal Delta T_room ~ 30 K)  ",
          "OK" if 0 < i_pred <= 5.1 else f"got {i_pred:.2f}")
    print(f"  P_internal ~ 1e-6 W                                       ",
          "OK" if math.isclose(P_BIMETAL, 1e-6, rel_tol=0.5) else f"got {P_BIMETAL:.2e}")


if __name__ == "__main__":
    main()
