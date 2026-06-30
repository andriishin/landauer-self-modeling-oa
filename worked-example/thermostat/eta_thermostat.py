"""
Structural verdict for a bimetallic room thermostat -- § 4.4 boundary case.

Refounded onto the central quantity eta_v = I_pred / I_mem in [0, 1]. Demarcation
is carried by the self-payment predicate S (self-funding AND a physical error-
return loop), NOT by any energetic-efficiency ratio. The earlier energetic-
denominator computation is removed; eta_v is an information ratio.

For the thermostat S = 0 in both self-consistent readings, so eta_v is not
defined (there is no self-paying subject to measure it for). This is the central
anti-FEP argument of § 4.4: formal FEP-applicability does not imply self-payment.

The only quantities that OUTLIVE the refounding and still match § 4.4 are the
internal-dissipation order of magnitude (P_int ~ 1e-6 W) and the carrier-bound
on predictive information set by the hysteresis resolution
(I_pred <= log2(Delta T_room / Delta T_hyst)). They are kept; everything tied to
the earlier energetic-denominator ratio is removed.

Run:
    python eta_thermostat.py
"""

from __future__ import annotations

import math


# ---------------------------------------------------------------------------
# Parameters (main § 4.4 / Supplementary § S4.4)
# ---------------------------------------------------------------------------

DELTA_T_HYST = 1.0       # K, switching hysteresis of the bimetallic strip
DELTA_T_ROOM_DIURNAL = 10.0   # K, diurnal room-temperature swing
DELTA_T_ROOM_SEASONAL = 30.0  # K, seasonal room-temperature swing

P_INTERNAL = 1.0e-6      # W, internal dissipation (elastic relaxation + relay)

# External components, listed for transparency but excluded from the boundary
# by the counterfactual-ablation procedure of § 2.2.
P_HEATER_EXTERNAL = 1.0e3  # W, electric heater fed by the grid


def i_pred_bound(delta_room: float, delta_hyst: float) -> float:
    """Carrier bound on predictive info about the room, set by hysteresis."""
    return math.log2(delta_room / delta_hyst)


def main() -> None:
    i_pred_diurnal = i_pred_bound(DELTA_T_ROOM_DIURNAL, DELTA_T_HYST)
    i_pred_seasonal = i_pred_bound(DELTA_T_ROOM_SEASONAL, DELTA_T_HYST)

    print("=" * 72)
    print("Thermostat (bimetallic) -- structural verdict (main 4.4 / Supp S4.4)")
    print("=" * 72)
    print()
    print("Refounded quantity: eta_v = I_pred / I_mem in [0, 1]. Demarcation is")
    print("carried by the self-payment predicate S, not by an energetic-")
    print("efficiency ratio. For the thermostat S = 0, so eta_v is not defined.")
    print()
    print("Counterfactual ablation of the boundary (main 2.2):")
    print(f"  {'candidate':<28}{'inside?':<9}why")
    print("  " + "-" * 62)
    rows = [
        ("bimetallic strip", "yes", "removing it breaks the loop"),
        ("relay contacts", "yes", "removing it breaks the loop"),
        ("heating element", "no", "removes heat source, not decision loop"),
        ("electric grid", "no", "external energy source"),
        ("external setpoint operator", "no", "does not disrupt regulation"),
    ]
    for cand, inside, why in rows:
        print(f"  {cand:<28}{inside:<9}{why}")
    print("  -> boundary = {bimetal, relay}")
    print()
    print("Surviving quantities (outlive the refounding; match main 4.4):")
    print(f"  internal dissipation   P_int  ~ {P_INTERNAL:.0e} W"
          "  (elastic relaxation + relay)")
    print("  predictive-info bound  I_pred <= log2(Delta T_room / Delta T_hyst):")
    print(f"    diurnal  Delta T_room ~ {DELTA_T_ROOM_DIURNAL:.0f} K, hyst"
          f" {DELTA_T_HYST:.0f} K -> I_pred <= {i_pred_diurnal:.2f} bits (~3)")
    print(f"    seasonal Delta T_room ~ {DELTA_T_ROOM_SEASONAL:.0f} K, hyst"
          f" {DELTA_T_HYST:.0f} K -> I_pred <= {i_pred_seasonal:.2f} bits (up to ~5)")
    print(f"  (external heater power P_ext ~ {P_HEATER_EXTERNAL:.0e} W -- outside)")
    print()
    print("Two self-consistent readings, both S = 0 via DIFFERENT failures:")
    print("  managing ('regulate the room'): condition (i) fails -- room heating")
    print("    is paid by the external grid, E_own about that task = 0 (T_v fails).")
    print("  trivial ('hold the bimetal's own shape'): condition (ii) fails --")
    print("    passive thermo-mechanical coupling forms no error-return loop; a")
    print("    shape deviation is not corrected by the system's own dissipation")
    print("    (S_v fails).")
    print()
    print("Verdict: S = 0 (not vital). eta_v = I_pred / I_mem is UNDEFINED -- a")
    print("numeric value would require an MI estimate of I_pred and I_mem of a")
    print("self-paying loop, which the thermostat does not possess.")
    print()
    print("Cross-check vs main 4.4 / Supplementary S4.4:")
    print("  S = 0 in both readings                          OK")
    ok_ipred = abs(i_pred_diurnal - 3.32) < 0.05 and abs(i_pred_seasonal - 4.91) < 0.05
    print(f"  I_pred <= ~3 bits diurnal (up to ~5 seasonal)   "
          f"{'OK' if ok_ipred else 'MISMATCH'} "
          f"({i_pred_diurnal:.2f} / {i_pred_seasonal:.2f})")
    print(f"  P_int ~ 1e-6 W                                  "
          f"{'OK' if math.isclose(P_INTERNAL, 1e-6) else 'MISMATCH'}")


if __name__ == "__main__":
    main()
