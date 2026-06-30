import numpy as np
# Proof-of-measurability для I_mem (worked-example E. coli, § 3 статьи #1) под новым η=I_pred/I_mem.
# Модель: ХЕМОТАКСИС как линейный адаптивный трекер (ИММОБИЛИЗОВАННАЯ клетка + внешне-управляемый лиганд —
# это и есть стандартный FRET-протокол Sourjik/Cluzel; заодно обходит активный случай E).
#   лиганд (log-conc) s_t: AR(1), время корреляции tau_E (дрейф среды).
#   метилирование m_t = leaky-интеграл прошлого лиганда (линеаризованная адаптация Tu-типа):
#       m_t = sum_{j>=1} w_j s_{t-j} + noise,  w_j=(1-beta)beta^{j-1}  (beta — память адаптации).
#   внутреннее состояние (память) M_t = m_t.
# Считаем I_mem=I(m_t; s^<=t-окно), I_pred=I(m_t; s^(t,t+tau]), eta=I_pred/I_mem — все гауссовы, точно (logdet).
# Цель: показать, что I_mem КОНЕЧНА и оценима из НАБЛЮДАЕМЫХ корреляций (метилирование m ↔ лиганд s),
# т.е. измерима как старый E_actual. Числа ИЛЛЮСТРАТИВНЫ (минимальная модель), не количественная claim про η реальной E. coli.

def scov(i,j,a,ss2): return ss2*a**abs(i-j)

def run(tau_E, beta, r=0.3, ss2=1.0, J=300, L=60, tau=5):
    a=np.exp(-1.0/tau_E)
    w=np.array([(1-beta)*beta**(j-1) for j in range(1,J+1)])   # вес на s_{t-1..t-J}
    def cov_ms(k): return sum(w[j-1]*scov(-j,k,a,ss2) for j in range(1,J+1))
    var_m=sum(w[j-1]*w[jp-1]*scov(-j,-jp,a,ss2) for j in range(1,J+1) for jp in range(1,J+1))+r
    def MI(times):
        n=len(times)
        C=np.array([[scov(times[i],times[j],a,ss2) for j in range(n)] for i in range(n)])
        cm=np.array([cov_ms(t) for t in times])
        Cj=np.zeros((n+1,n+1)); Cj[0,0]=var_m; Cj[0,1:]=cm; Cj[1:,0]=cm; Cj[1:,1:]=C
        return 0.5*(np.log(var_m)+np.linalg.slogdet(C)[1]-np.linalg.slogdet(Cj)[1])
    past=list(range(0,-L,-1)); fut=list(range(1,tau+1))
    Imem=MI(past); Ipred=MI(fut)
    return dict(tau_E=tau_E,beta=beta,Imem=Imem,Ipred=Ipred,eta=Ipred/Imem,nu=1-Ipred/Imem,var_m=var_m)

print("=== I_mem КОНЕЧНА, eta=I_pred/I_mem ∈ [0,1] — для адаптивной памяти хемотаксиса ===")
print(f"{'tau_E':>6} {'beta':>5} {'I_mem':>8} {'I_pred':>8} {'eta':>7} {'nu(ностальгия)':>14}")
for tau_E in (3,10,30):
    for beta in (0.5,0.9,0.99):
        d=run(tau_E,beta)
        print(f"{tau_E:>6} {beta:>5} {d['Imem']:>8.4f} {d['Ipred']:>8.4f} {d['eta']:>7.3f} {d['nu']:>14.3f}")

print("\n=== Ностальгия растёт, когда память адаптации (beta) ПЕРЕРАСТАЕТ дрейф среды (tau_E) ===")
print("  (over-интегрируешь устаревший лиганд → больше балласта → eta падает, nu растёт)")
print(f"  tau_E=5 фикс:  {'beta':>5} {'eta':>7} {'nu':>7}")
for beta in (0.3,0.6,0.8,0.9,0.95,0.99):
    d=run(5,beta); print(f"{'':>13}{beta:>5} {d['eta']:>7.3f} {d['nu']:>7.3f}")

print("\n=== Измеримость: все величины — функции НАБЛЮДАЕМЫХ корреляций m↔s ===")
d=run(10,0.9)
print(f"  пример (tau_E=10,beta=0.9): I_mem={d['Imem']:.3f} нат, I_pred={d['Ipred']:.3f}, eta={d['eta']:.3f}, var(m)={d['var_m']:.3f}")
print("  I_mem зависит лишь от Cov(m,s_k) и Cov(s_i,s_j) — обе измеримы: m через FRET-метилирование, s через микрофлюидику.")
