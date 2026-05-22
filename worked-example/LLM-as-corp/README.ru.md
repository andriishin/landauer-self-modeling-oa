# Worked Example: η_L для LLM-as-corporation

Расчёт ландауэровского КПД самомоделирования $\eta_L$ для LLM в расширенной границе «модель + дата-центр + корпорация». Прилагается к § 3.4 статьи «Vitality as a Landauer Efficiency of Self-Modeling».

## Содержательный смысл

Paper § 3.4 различает три прочтения LLM:

1. **Операциональное** «модель + дата-центр»: $\eta_L > 0$ по внешним метрикам, но не self-payment.
2. **Интерпретативное** «веса в момент inference»: $\eta_L = 0$ — нет каузально-релевантной среды.
3. **Расширение границы** «модель + дата-центр + корпорация»: $\eta_L > 0$, но измеряемый объект — корпорация, не модель.

Этот worked example операционализирует третье прочтение: корпорация трактуется как социо-техническая система, и вычисляется $\eta_L^{\text{corp}}$ через формулу (1).

## Содержимое

| Файл | Назначение |
|------|------------|
| `eta_L_llm_corp.py` | Расчёт $\eta_L^{\text{corp}}$ через эксергический и computational знаменатели |
| `expected_output.txt` | Эталонный вывод |

## Запуск

```bash
python eta_L_llm_corp.py
```

## Параметры

### Энергетический бюджет (frontier-AI lab, годовой)
- **Дата-центр:** $\sim 100$ МВт непрерывно $= 3.15 \cdot 10^{15}$ Дж/год.
- **Офис и операции:** $\sim 10$ МВт $= 3.15 \cdot 10^{14}$ Дж/год.
- **Supply chain** (производство hardware, логистика, амортизация): $\sim 1$ ГВт $= 3.15 \cdot 10^{16}$ Дж/год.
- **Итого:** $E_{\text{actual}}^{\text{total}} \sim 3.5 \cdot 10^{16}$ Дж/год.

### Predictive information
- **Training corpus**, сжатый в веса: $\sim 10^{12}$ бит (энтропия обучающих данных $\times$ компрессия).
- **Operational memory** (логи, customer interactions, документы): $\sim 10^{11}$ бит.
- **Market intelligence** (research, competitive, regulatory): $\sim 10^{10}$ бит.
- **Итого:** $I_{\text{pred}} \sim 1.1 \cdot 10^{12}$ бит.

### Computational знаменатель
- $\eta_{\text{ex}}^{\text{comp}} \sim 10^{-2}$ — доля энергии, фактически попадающая в необратимые bit-flip операции (преимущественно дата-центр; остальное — cooling overhead и инфраструктура).

### Прочее
- $T = 300$ К (operating temperature; стандартизированное $T$ для LLM/дата-центра, статья § 2.1).
- $k_B T \ln 2 \approx 2.87 \cdot 10^{-21}$ Дж/бит.

## Ожидаемые результаты

- $N_{\text{max}}^{\text{ex}} = 3.5 \cdot 10^{16}/2.87 \cdot 10^{-21} \approx 1.22 \cdot 10^{37}$ бит/год.
- $N_{\text{max}}^{\text{comp}} = N_{\text{max}}^{\text{ex}} \cdot 10^{-2} \approx 1.22 \cdot 10^{35}$ бит/год.
- $\eta_L^{\text{corp}} \text{(exergetic)} \approx 9 \cdot 10^{-26}$ — порядок $10^{-25}$.
- $\eta_L^{\text{corp}} \text{(computational)} \approx 9 \cdot 10^{-24}$ — порядок $10^{-23}$.

## Содержательный вывод

1. Расширение границы LLM до корпорации даёт **положительный, но катастрофически малый** $\eta_L^{\text{corp}}$.
2. Парадокс расширения границы: чем больше система, тем меньше $\eta_L$ — масштабирование $E_{\text{actual}}$ обгоняет $I_{\text{pred}}$. Корпорация имеет на много порядков больше абсолютной predictive information, чем бактериальная клетка, но её энергетический бюджет растёт ещё быстрее: бóльшая часть джоулей уходит на логистику, производство, HVAC и cooling overhead, не на bit-flip операции, поддерживающие удержание собственной модели.
3. Это содержательный результат, не дефект процедуры: «расширение ответственного субъекта» (paper § 3.4) количественно не делает крупную социо-техническую систему витально-сравнимой с биологическим уровнем.

## Литература

- **Patterson, D.; Gonzalez, J.; Le, Q.; Liang, C.; Munguia, L.-M.; Rothchild, D.; So, D.; Texier, M.; Dean, J.** Carbon Emissions and Large Neural Network Training. *arXiv preprint* **2021**, arXiv:2104.10350. (Energy footprint of frontier model training.)
- **Bender, E. M.; Gebru, T.; McMillan-Major, A.; Shmitchell, S.** On the Dangers of Stochastic Parrots. *FAccT* **2021**. (Scale and infrastructure of major LLM operations.)

## Статус

Methodological calibration. Точные значения параметров $I_{\text{pred}}^{\text{corp}}$ и $\eta_{\text{ex}}^{\text{comp}}$ для корпоративных систем — задача отдельной работы; устойчивость порядка $\eta_L^{\text{corp}} \sim 10^{-25}$ удерживается при варьировании входов в правдоподобных диапазонах.
