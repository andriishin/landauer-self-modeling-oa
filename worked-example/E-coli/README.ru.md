# Worked Example: η_L для хемотаксической петли *E. coli*

Воспроизводимый расчёт ландауэровского КПД самомоделирования $\eta_L$ для бактериальной хемотаксической петли *E. coli*. Прилагается к статье «Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality» (§ 3.5 + Supplementary § S3.5).

## Содержимое

| Файл | Назначение |
|------|------------|
| `eta_L_ecoli.py` | Центральный расчёт: $\eta_L$ и $\eta_L^{\text{comp}}$ через эксергический и computational знаменатели; печатает таблицу результатов |
| `sensitivity.py` | Sensitivity-анализ через Monte Carlo: разброс $\eta_L$ по диапазонам $I_{\text{pred}}, E_{\text{actual}}, \eta_{\text{ex}}, T$ |
| `expected_output.txt` | Эталонный вывод `eta_L_ecoli.py` для верификации воспроизводимости |
| `requirements.txt` | Минимальный набор зависимостей (numpy, matplotlib) |

## Запуск

```bash
pip install -r requirements.txt
python eta_L_ecoli.py
python sensitivity.py
```

Вывод `eta_L_ecoli.py` должен совпадать с `expected_output.txt` с точностью до floating-point round-off. Числовые узлы:

- $N_{\text{max}}^{\text{ex}} \approx 3 \cdot 10^{11}$ бит на клетку (эксергический бюджет);
- $N_{\text{max}}^{\text{comp}} \approx 3 \cdot 10^{8}$ бит на клетку (computational, $\eta_{\text{ex}}^{\text{comp}} = 10^{-3}$);
- $\eta_L \approx 3 \cdot 10^{-8}$ через эксергический знаменатель;
- $\eta_L^{\text{comp}} \approx 3 \cdot 10^{-5}$ через computational знаменатель.

## Модель

Расчёт следует протоколу из Supplementary § S2.1 (четыре элемента операционализации $I_{\text{pred}}$).

**(а) Сенсорный канал $x_t$** — концентрация лиганда (атрактанта или репеллента) у хемотаксических рецепторов клетки. Для оценки берётся диапазон порядков по [Sourjik2002, Endres2008].

**(б) Внутренний канал $s_t$** — уровень метилирования рецепторных кластеров (Tar, Tsr, Trg, Tap, Aer). Состояния метилирования действуют как краткосрочная адаптационная память с характерным временем секунд—минут [Korobkova2004].

**(в) Окна past/future с $\tau$** — характерное окно памяти $\tau \approx 10$–$100$ с (характерное время метилирования/деметилирования) $\times$ окно поколения $\sim 30$–$60$ мин.

**(г) Оценка взаимной информации $I_{\text{pred}}$** — литературные оценки сходятся на $I_{\text{pred}} \in [10^{3}, 10^{5}]$ бит на клетку за поколение, центральная оценка $10^{4}$ бит [ShimizuTuBerg2010, Cheong2011, MehtaSchwab2012]. В sensitivity-анализе варьируется по полному диапазону.

## Знаменатель

$N_{\text{max}}$ определяется через формулу (1) основного текста:

$$N_{\text{max}} = \frac{E_{\text{actual}}}{k_B T \ln 2}$$

где
- $E_{\text{actual}} = E_{\text{actual}}^{\text{total}} \cdot \eta_{\text{ex}}$ — эксергическая часть полной свободной энергии, физически оплачивающей удержание $I_{\text{pred}}$;
- $E_{\text{actual}}^{\text{total}} \sim 10^{-9}$ Дж/клетку за поколение (метаболический бюджет, ATP-эквивалент порядка $10^{10}$ молекул);
- $\eta_{\text{ex}} \approx 1$ для эксергического знаменателя (вся доступная свободная энергия);
- $T = 310$ К (физиологическая температура);
- $k_B T \ln 2 = 2{,}967 \cdot 10^{-21}$ Дж/бит при $T = 310$ К.

Computational знаменатель использует $\eta_{\text{ex}}^{\text{comp}} \approx 10^{-3}$ — долю эксергии, идущую на необратимые информационные операции; остальное расходуется на синтез биомассы и ионные градиенты [MehtaSchwab2012, Lan2012].

## Литература

- **Berg, H. C.; Brown, D. A.** Chemotaxis in *Escherichia coli* analysed by three-dimensional tracking. *Nature* **1972**, *239*, 500–504.
- **Sourjik, V.; Berg, H. C.** Receptor sensitivity in bacterial signaling. *PNAS* **2002**, *99*, 123–127.
- **Korobkova, E.; Emonet, T.; Vergassola, M.; Cluzel, P.** From molecular noise to behavioural variability in a single bacterium. *Nature* **2004**, *428*, 574–578.
- **Endres, R. G.; Wingreen, N. S.** Accuracy of direct gradient sensing by single cells. *PNAS* **2008**, *105*, 15749–15754.
- **Shimizu, T. S.; Tu, Y.; Berg, H. C.** A modular gradient-sensing network for chemotaxis in *Escherichia coli* revealed by responses to time-varying stimuli. *Mol. Syst. Biol.* **2010**, *6*, 382.
- **Cheong, R.; Rhee, A.; Wang, C. J.; Nemenman, I.; Levchenko, A.** Information transduction capacity of noisy biochemical signaling networks. *Science* **2011**, *334*, 354–358.
- **Lan, G.; Sartori, P.; Neumann, S.; Sourjik, V.; Tu, Y.** The energy–speed–accuracy trade-off in sensory adaptation. *Nat. Phys.* **2012**, *8*, 422–428.
- **Mehta, P.; Schwab, D. J.** Energetic costs of cellular computation. *PNAS* **2012**, *109*, 17978–17982.
- **Landauer, R.** Irreversibility and heat generation in the computing process. *IBM J. Res. Dev.* **1961**, *5*, 183–191.

## Статус

Расчёт носит характер *методологической калибровки*: не претендует на точность лучше одного порядка по каждому параметру и трёх порядков по итоговому $\eta_L$. Содержательное утверждение — устойчивость различия $\eta_L \ll 1$ и качественное соотношение $\eta_L^{\text{comp}} / \eta_L \sim 10^{3}$, отражающее фракцию свободной энергии, направляемую на необратимые информационные операции. Полная sensitivity-карта — `sensitivity.py`.
