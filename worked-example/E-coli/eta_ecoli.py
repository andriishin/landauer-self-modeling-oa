"""
eta_v = I_pred / I_mem for the E. coli chemotaxis loop — central worked example.

Reproduces the predictive-fraction estimate of § 3.5 / Supplementary § S3.5 of
the paper (Andriishin, in preparation for Theory in Biosciences) under the
refounded central quantity

    eta_v = I_pred / I_mem = 1 - nu  in [0, 1]   (data-processing inequality),

where
    I_mem  = I(M_t ; X_E^{<= t})   how much the internal state knows about the
                                   past/present environment trajectory,
    I_pred = I(M_t ; X_E^{(t, t+tau]}) how much it knows about the future,
    nu     = 1 - eta_v               nostalgia (the non-predictive ballast).

Both the numerator and the denominator are *informational* quantities, both
estimable from time series; there is no energetic denominator and no
dimensionless erasure-capacity ratio.

do-intervention (main § 2.1). The immobilised FRET protocol is NOT a
simplification but an operational realisation of Pearl's do(a) intervention:
exogenously clamping the cell's action severs the action->environment feedback
and restores the Markovianity the [0,1] bound presupposes. The passive quantity
computed here is therefore the interventional freshness
    eta_v^do = I(M_t ; X_E^{(t,t+tau]} | do(a)) / I_mem  in [0, 1],
numerator and denominator in the SAME do(a) regime; a freely swimming cell would
measure a different, active quantity not bounded by 1.

Model (Supplementary § S3.5). Chemotaxis as a linear adaptive tracker in the
passive (immobilised) FRET protocol Sourjik-Berg / Cluzel:
  - ligand log-concentration s_t: AR(1) with correlation time tau_E (environment
    drift), driven by microfluidics;
  - methylation m_t = sum_{j>=1} w_j s_{t-j} + noise, a leaky integral of the
    past ligand (linearised Tu-type adaptation) with weights w_j=(1-beta_v)beta_v^{j-1}
    (beta_v = adaptation memory); the internal state is M_t = m_t, read via FRET;
  - past window X_E^{<=t} of length L, future horizon tau.

Since (s_t, m_t) are jointly Gaussian, I_mem and I_pred are computed *exactly*
via log-determinants of covariance matrices (here through a pure-stdlib Cholesky
decomposition; no numpy). Key measurability point: I_mem depends ONLY on the
observable covariances Cov(m, s_k) and Cov(s_i, s_j) -- both estimable from time
series (m via FRET methylation, s via microfluidics) -- so the operational debt
of the informational denominator is no worse than that of a calorimetric
dissipation estimate.

The numbers are an ILLUSTRATIVE worked example (minimal linear model showing
measurability and order of magnitude), not a calibrated measurement of real
E. coli. Standard library only.

Run:
    python eta_ecoli.py

Expected output is captured in expected_output.txt.
"""

from __future__ import annotations

import math


# ---------------------------------------------------------------------------
# Pure-stdlib linear algebra: log|det A| for a symmetric positive-definite A
# via the Cholesky factorisation A = L L^T  ->  log det A = 2 * sum log L_ii.
# (Replaces numpy.linalg.slogdet; agrees to ~1e-12 for the covariance matrices
# used here, which are well-conditioned Kac-Murdock-Szego AR(1) matrices.)
# ---------------------------------------------------------------------------


def logdet_spd(a: list[list[float]]) -> float:
    n = len(a)
    chol = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = a[i][j] - sum(chol[i][k] * chol[j][k] for k in range(j))
            if i == j:
                chol[i][i] = math.sqrt(s)
            else:
                chol[i][j] = s / chol[j][j]
    return 2.0 * sum(math.log(chol[i][i]) for i in range(n))


# ---------------------------------------------------------------------------
# Gaussian chemotaxis tracker (Supplementary § S3.5)
# ---------------------------------------------------------------------------


def scov(i: int, j: int, a: float, ss2: float) -> float:
    """Stationary AR(1) ligand auto-covariance Cov(s_i, s_j) = ss2 * a^|i-j|."""
    return ss2 * a ** abs(i - j)


def run(tau_E: float, beta_v: float, r: float = 0.3, ss2: float = 1.0,
        big_j: int = 300, big_l: int = 60, tau: int = 5) -> dict:
    """
    Compute I_mem, I_pred, eta_v, nu (in nats) for one (tau_E, beta_v) setting.

    Parameters (Supplementary § S3.5):
        tau_E : environment-drift correlation time of the ligand AR(1)
        beta_v  : adaptation memory of the leaky methylation integral
        r     : methylation-readout noise variance
        ss2   : ligand variance (units)
        big_j : truncation of the leaky-integral cumulant (j = 1..big_j)
        big_l : past-window length L
        tau   : prediction horizon
    """
    a = math.exp(-1.0 / tau_E)
    w = [(1.0 - beta_v) * beta_v ** (j - 1) for j in range(1, big_j + 1)]  # s_{t-1..t-J}

    def cov_ms(k: int) -> float:
        return sum(w[j - 1] * scov(-j, k, a, ss2) for j in range(1, big_j + 1))

    var_m = r + sum(
        w[j - 1] * w[jp - 1] * scov(-j, -jp, a, ss2)
        for j in range(1, big_j + 1)
        for jp in range(1, big_j + 1)
    )

    def mutual_information(times: list[int]) -> float:
        n = len(times)
        cc = [[scov(times[i], times[j], a, ss2) for j in range(n)] for i in range(n)]
        cm = [cov_ms(t) for t in times]
        cj = [[0.0] * (n + 1) for _ in range(n + 1)]
        cj[0][0] = var_m
        for i in range(n):
            cj[0][i + 1] = cm[i]
            cj[i + 1][0] = cm[i]
            for j in range(n):
                cj[i + 1][j + 1] = cc[i][j]
        # I(m ; times) = 0.5 ( log var_m + logdet C - logdet Cj )
        return 0.5 * (math.log(var_m) + logdet_spd(cc) - logdet_spd(cj))

    past = list(range(0, -big_l, -1))     # X_E^{<= t}, window length L
    fut = list(range(1, tau + 1))         # X_E^{(t, t+tau]}
    i_mem = mutual_information(past)
    i_pred = mutual_information(fut)
    eta_v = i_pred / i_mem
    return dict(tau_E=tau_E, beta_v=beta_v, i_mem=i_mem, i_pred=i_pred,
                eta_v=eta_v, nu=1.0 - eta_v, var_m=var_m)


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


def main() -> None:
    print("=" * 72)
    print("eta_v = I_pred / I_mem for the E. coli chemotaxis loop -- worked example")
    print("=" * 72)
    print()
    print("I_mem is FINITE and eta_v = I_pred/I_mem in [0,1] by the data-processing")
    print("inequality; nu = 1 - eta_v is nostalgia. Values in nats. Horizon tau = 5,")
    print("past window L = 60, methylation-noise r = 0.3 (Supplementary S3.5).")
    print()
    print(f"  {'tau_E':>6} {'beta_v':>5} {'I_mem':>8} {'I_pred':>8} {'eta_v':>7}"
          f" {'nu (nostalgia)':>15}")
    print("  " + "-" * 54)
    table = {}
    for tau_E in (3, 10, 30):
        for beta_v in (0.5, 0.9, 0.99):
            d = run(tau_E, beta_v)
            table[(tau_E, beta_v)] = d
            print(f"  {tau_E:>6} {beta_v:>5} {d['i_mem']:>8.4f} {d['i_pred']:>8.4f}"
                  f" {d['eta_v']:>7.3f} {d['nu']:>15.3f}")
    print()

    print("Nostalgia grows when adaptation memory (beta_v) OUTPACES environment")
    print("drift (tau_E): the cell over-integrates stale ligand, so the pure-")
    print("ballast fraction rises -> eta_v falls, nu rises. Fixed tau_E = 5:")
    print()
    print(f"  {'beta_v':>6} {'eta_v':>7} {'nu':>7}")
    print("  " + "-" * 22)
    beta_v_scan = {}
    for beta_v in (0.3, 0.6, 0.8, 0.9, 0.95, 0.99):
        d = run(5, beta_v)
        beta_v_scan[beta_v] = d
        print(f"  {beta_v:>6} {d['eta_v']:>7.3f} {d['nu']:>7.3f}")
    print()

    d_meas = run(10, 0.9)
    print("Measurability: every quantity is a function of OBSERVABLE m<->s")
    print("covariances. Example (tau_E = 10, beta_v = 0.9):")
    print(f"  I_mem = {d_meas['i_mem']:.3f} nats, I_pred = {d_meas['i_pred']:.3f},"
          f" eta_v = {d_meas['eta_v']:.3f}, var(m) = {d_meas['var_m']:.3f}")
    print("  I_mem depends only on Cov(m, s_k) and Cov(s_i, s_j) -- both estimable:")
    print("  m via FRET methylation (Sourjik-Berg 2002; Cluzel et al. 2000),")
    print("  s via microfluidics. The informational denominator is no harder to")
    print("  measure than the calorimetric one.")
    print()

    print("Cross-check vs Supplementary S3.5 (eta_v ~ O(0.1); DPI gives eta_v<=1):")
    checks = [
        ("(tau_E=10, beta_v=0.5): I_mem~0.69, I_pred~0.32, eta_v~0.47",
         table[(10, 0.5)], 0.69, 0.32, 0.47),
        ("(tau_E=10, beta_v=0.9): I_mem~0.50, I_pred~0.14, eta_v~0.27",
         table[(10, 0.9)], 0.50, 0.14, 0.27),
        ("(tau_E=30, beta_v=0.9): I_mem~0.63, I_pred~0.34, eta_v~0.54",
         table[(30, 0.9)], 0.63, 0.34, 0.54),
        ("(tau_E= 3, beta_v=0.9): I_mem~0.30, I_pred~0.02, eta_v~0.07",
         table[(3, 0.9)], 0.30, 0.02, 0.07),
    ]
    for label, d, im, ip, et in checks:
        ok = (abs(d['i_mem'] - im) < 0.01 and abs(d['i_pred'] - ip) < 0.01
              and abs(d['eta_v'] - et) < 0.01)
        print(f"  {label}   {'OK' if ok else 'MISMATCH'}")
    eta_v_lo = beta_v_scan[0.3]['eta_v']
    eta_v_hi = beta_v_scan[0.99]['eta_v']
    ok_scan = abs(eta_v_lo - 0.29) < 0.01 and abs(eta_v_hi - 0.035) < 0.005
    print(f"  beta_v-scan at tau_E=5: eta_v {eta_v_lo:.3f} -> {eta_v_hi:.3f}"
          f" (paper 0.29 -> 0.035)   {'OK' if ok_scan else 'MISMATCH'}")
    ok_dpi = all(0.0 <= d['eta_v'] <= 1.0 for d in table.values())
    print(f"  all eta_v in [0,1] (data-processing inequality)   "
          f"{'OK' if ok_dpi else 'MISMATCH'}")
    print()
    print("Status: illustrative worked example (minimal linear model). It shows")
    print("the predictive fraction eta_v = I_pred/I_mem is finite, measurable, and")
    print("O(0.1) for chemotactic memory -- not a calibrated value for real")
    print("E. coli. Parameter sensitivity (tau, L, r) -- see sensitivity.py.")


if __name__ == "__main__":
    main()
