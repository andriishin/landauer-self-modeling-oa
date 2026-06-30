import numpy as np

# Гауссова AR(1)-среда: X_{t+1}=a X_t + xi,  Cov(X_i,X_j)=sx2 a^{|i-j|}.
# Память M: L зашумлённых наблюдений последних L шагов. M_k ~ X_{-k}+noise(r), k=0..L-1 (k=0 — текущий).
# Относительные времена: прошлое/настоящее 0,-1,..,-(L-1); будущее 1..tau.
# Все величины — совместно гауссовы; MI(A;B)=0.5(logdet C_A + logdet C_B - logdet C_AB).

def cov_entry(u, v, a, sx2, r):
    # u,v: ('X',i) или ('M',k); M_k отслеживает X_{-k}
    tu = -u[1] if u[0]=='M' else u[1]
    tv = -v[1] if v[0]=='M' else v[1]
    c = sx2 * a**abs(tu-tv)
    if u[0]=='M' and v[0]=='M' and u[1]==v[1]:
        c += r
    return c

def build_cov(vs, a, sx2, r):
    n=len(vs); C=np.empty((n,n))
    for i in range(n):
        for j in range(n):
            C[i,j]=cov_entry(vs[i],vs[j],a,sx2,r)
    return C

def sld(vs,a,sx2,r):
    s,v=np.linalg.slogdet(build_cov(vs,a,sx2,r)); 
    return v

def MI(A,B,a,sx2,r):
    return 0.5*(sld(A,a,sx2,r)+sld(B,a,sx2,r)-sld(A+B,a,sx2,r))

def analyze(L, tauE, r=0.5, sx2=1.0):
    a=np.exp(-1.0/tauE)
    M=[('M',k) for k in range(L)]
    Xwin=[('X',-i) for i in range(L)]          # окно, которое память наблюдает: X_0..X_{-(L-1)}
    X0=[('X',0)]; X1=[('X',1)]
    I_mem_cum = MI(M, Xwin, a,sx2,r)            # инфо памяти о наблюдаемом окне (кумулятивная память)
    I_mem_inst= MI(M, X0,  a,sx2,r)            # о текущем (мгновенная память, Still)
    I_pred1   = MI(M, X1,  a,sx2,r)            # одношаговый прогноз
    # горизонтный прогноз I_pred(tau)=I(M; X_1..X_tau)
    Ipred=[]
    for tau in (1,2,3,5):
        Xf=[('X',j) for j in range(1,tau+1)]
        Ipred.append(MI(M,Xf,a,sx2,r))
    I_nonpred_inst = I_mem_inst - I_pred1
    nu_cum = 1 - Ipred[-1]/I_mem_cum            # операциональная ностальгия (гориз., кум. норм.)
    c = tauE / L                               # FIFO-оценка: refresh=1/шаг, |M|=L набл., tau_E шагов
    return dict(L=L,tauE=tauE,a=a, I_mem_cum=I_mem_cum, I_mem_inst=I_mem_inst,
                I_pred1=I_pred1, Ipred=Ipred, I_nonpred_inst=I_nonpred_inst,
                nu_cum=nu_cum, c=c, floor_1mc=max(0,1-c))

print("=== 1) Горизонт ничего не добавляет для марковской среды: I_pred(tau)=I_pred(1)? ===")
d=analyze(L=10,tauE=5)
print("  I_pred(tau=1,2,3,5) =", [f'{x:.4f}' for x in d['Ipred']], " (ожидаем равенство — Марков)")

print("\n=== 2) Мгновенная непредсказательная инфо (термо, per-step) ~ const по L; ню_cum -> 1 ===")
print(f"  tau_E=5 шагов, r=0.5")
print(f"  {'L':>4} {'I_mem_inst':>11} {'I_pred1':>9} {'I_nonpred_inst':>15} {'I_mem_cum':>10} {'nu_cum':>7} {'1-tauE/L':>9}")
for L in (2,5,10,20,40,80):
    d=analyze(L=L,tauE=5)
    print(f"  {L:>4} {d['I_mem_inst']:>11.4f} {d['I_pred1']:>9.4f} {d['I_nonpred_inst']:>15.4f} {d['I_mem_cum']:>10.3f} {d['nu_cum']:>7.3f} {d['floor_1mc']:>9.3f}")

print("\n=== 3) Термо-пол (per-step nonpred) задаётся средой (tau_E), не размером памяти L ===")
print(f"  {'tau_E':>6} {'a':>7} {'I_nonpred_inst(L=40)':>20} {'~H(X_t|X_t+1)':>14}")
for tauE in (2,5,10,20):
    d=analyze(L=40,tauE=tauE)
    a=d['a']; HxtgivenNext=0.5*np.log(2*np.pi*np.e* (1.0*(1-a**2)))  # энтропия X_t|X_{t+1} для стац. AR(1), sx2=1
    print(f"  {tauE:>6} {a:>7.4f} {d['I_nonpred_inst']:>20.4f} {HxtgivenNext:>14.4f}")
