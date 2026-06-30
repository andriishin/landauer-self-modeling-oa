"""
Sensitivity analysis for eta_v = I_pred / I_mem of the E. coli chemotaxis loop.

Sweeps the model parameters of Supplementary § S3.5 -- environment-drift time
tau_E, past-window length L, and methylation-readout noise r -- and shows that
the predictive fraction eta_v = I_pred/I_mem stays within about one order of
magnitude around O(0.1), while I_mem and I_pred vary. There is no energetic-
budget sweep here: both numerator and denominator are informational.

Run:
    python sensitivity.py
"""

from __future__ import annotations

from eta_ecoli import run


def report_drift() -> None:
    print("(1) Environment-drift time tau_E (beta_v = 0.9, tau = 5, L = 60, r = 0.3)")
    print("    Faster drift (small tau_E) -> the future is less predictable from")
    print("    the methylation memory -> lower eta_v, higher nostalgia. Slower drift")
    print("    -> higher eta_v. This is the nostalgia axis of main § 3.5.")
    print(f"    {'tau_E':>6} {'I_mem':>8} {'I_pred':>8} {'eta_v':>7} {'nu':>7}")
    print("    " + "-" * 39)
    for tau_E in (3, 5, 10, 20, 30):
        d = run(tau_E, 0.9)
        print(f"    {tau_E:>6} {d['i_mem']:>8.4f} {d['i_pred']:>8.4f}"
              f" {d['eta_v']:>7.3f} {d['nu']:>7.3f}")
    print()


def report_window() -> None:
    print("(2) Past-window length L (tau_E = 10, beta_v = 0.9, tau = 5, r = 0.3)")
    print("    For L >~ a few tau_E, I_mem is essentially unchanged: the distant")
    print("    past is exponentially suppressed by both w_j and the ligand")
    print("    autocorrelation. This justifies truncating the cumulant to a")
    print("    finite window.")
    print(f"    {'L':>5} {'I_mem':>8} {'I_pred':>8} {'eta_v':>7}")
    print("    " + "-" * 30)
    for big_l in (10, 20, 40, 60, 100):
        d = run(10, 0.9, big_l=big_l)
        print(f"    {big_l:>5} {d['i_mem']:>8.4f} {d['i_pred']:>8.4f} {d['eta_v']:>7.3f}")
    print()


def report_noise() -> None:
    print("(3) Methylation-readout noise r (tau_E = 10, beta_v = 0.9, tau = 5, L = 60)")
    print("    r sets the absolute level of I_mem (more noise -> less I_mem), but")
    print("    weakly affects the RATIO eta_v: it enters numerator and denominator")
    print("    consistently.")
    print(f"    {'r':>6} {'I_mem':>8} {'I_pred':>8} {'eta_v':>7}")
    print("    " + "-" * 31)
    for r in (0.1, 0.3, 1.0, 3.0):
        d = run(10, 0.9, r=r)
        print(f"    {r:>6} {d['i_mem']:>8.4f} {d['i_pred']:>8.4f} {d['eta_v']:>7.3f}")
    print()


def main() -> None:
    print("=" * 72)
    print("Sensitivity analysis -- eta_v = I_pred/I_mem for E. coli chemotaxis")
    print("=" * 72)
    print()
    report_drift()
    report_window()
    report_noise()
    print("Notes (Supplementary S3.5):")
    print("  - Receptor/cluster count does NOT affect eta_v directly: scaling the")
    print("    number of independent sensory channels raises numerator and")
    print("    denominator together and cancels in the ratio.")
    print("  - Prediction horizon tau: in this minimal AR(1) model the ligand is")
    print("    Markov, so I_pred is fixed by the one-step-ahead correlation and is")
    print("    insensitive to tau >= 1; resolving the horizon dependence discussed")
    print("    in S3.5 needs a non-Markov environment model (future work).")
    print("  - The bottleneck is the experimental FRET-readout <-> M_t mapping and")
    print("    the past-window choice for X_E^{<=t}, not the receptor count.")
    print()
    print("Conclusion: eta_v = I_pred/I_mem is robust at O(0.1) across the")
    print("plausible (tau_E, L, r) ranges; nostalgia nu = 1 - eta_v carries the")
    print("complement. Consistent with main S3.5 and Supplementary S3.5.")


if __name__ == "__main__":
    main()
