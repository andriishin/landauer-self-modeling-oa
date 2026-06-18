# Ландауэровская эффективность самомоделирования: операциональная шкала витальности — открытые материалы

*([English version](./README.md))*

Открытые материалы к статье **«Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality»** (русский — основной язык; включён английский перевод).

Статья формулирует витальность как безразмерную *эффективность* — ландауэровское отношение

```
η_L = I_pred / N_max,   N_max = E_actual / (k_B T ln 2)
```

с требованием **самооплаты**: числитель (предсказательная информация, которую система удерживает о собственной среде) и знаменатель (ландауэровский бюджет её собственной диссипации) принадлежат одной и той же физической системе. Двухэтапная процедура — скрининг по композитному индексу `I_v`, затем верификация `η_L` — применяется к шести камертонным случаям: Солнце, ураган, кристалл, бактерия, большая языковая модель и крупный город (плюс биосфера).

## Состав

```
paper/
  main.md / main.ru.md               Рукопись — английский (язык подачи) / русский (основной)
  supplementary.md / supplementary.ru.md   Дополнительные материалы — англ. / рус.
  main.tex / main.ru.tex             Исходник LaTeX (шаблон Springer Nature sn-jnl; генерируется из .md)
  supplementary.tex / supplementary.ru.tex
  main.pdf (61 с.) / main.ru.pdf (63 с.)            Скомпилированная рукопись
  supplementary.pdf (37 с.) / supplementary.ru.pdf (38 с.)
  refs.bib                           Библиография
  sn-jnl.cls, sn-*.bst               Шаблон Springer Nature + стили библиографии (third-party; см. LICENSE)
worked-example/                      Воспроизводимые расчёты (только стандартная библиотека)
  E-coli/  thermostat/  city/  biosphere/  LLM-as-corp/
docs/
  highlights.md                      Тезисы статьи
```

## Пересборка PDF

Готовые PDF включены для прямого чтения. Для пересборки из `.tex` нужен дистрибутив TeX с `pdflatex` и `bibtex` (TeX Live или MiKTeX). Файлы шаблона Springer Nature (`sn-jnl.cls`, `sn-*.bst`) вложены, ничего скачивать не требуется. Стиль ссылок — `sn-mathphys-ay` (автор–год). Стандартный цикл для любого документа, например `main`:

```bash
cd paper
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

(замените `main` на `supplementary`, `main.ru` или `supplementary.ru` для остальных документов).

## Воспроизведение разобранных примеров

Каждый `worked-example/<система>/` самодостаточен и использует **только стандартную библиотеку Python** (никакого `pip install`, кроме опционального `sensitivity.py` для E-coli):

```bash
cd worked-example/E-coli && python eta_L_ecoli.py
```

Вывод должен совпасть с зафиксированным `expected_output.txt` с точностью до округления чисел с плавающей точкой. В каждой папке есть `README.md` (английский, по умолчанию) и `README.ru.md` (русский) с описанием модели, параметров с литературой, ожидаемых результатов и статуса. `worked-example/README.md` / `README.ru.md` — индекс.

## Лицензия

- **Текст, рисунки, данные** (рукопись, дополнительные материалы, библиография, README, ожидаемые выводы): **Creative Commons Attribution 4.0 International (CC BY 4.0)** — см. [`LICENSE`](./LICENSE).
- **Исходный код** в `worked-example/`: **лицензия MIT** — см. [`worked-example/LICENSE`](./worked-example/LICENSE).

## Цитирование

Архивные материалы (этот репозиторий):

> Andriishin, A. *Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality.* Zenodo, 2026. https://doi.org/10.5281/zenodo.20262946

Депозит опубликован на Zenodo с указанным выше DOI. Машиночитаемое описание цитирования — в [`CITATION.cff`](./CITATION.cff). Журнальная версия записи будет добавлена отдельной ссылкой после принятия.
