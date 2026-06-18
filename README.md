# Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality — open materials

*([Русская версия](./README.ru.md))*

Open-access materials for the article **«Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality»** (Russian primary; English translation included).

The article formulates vitality as a dimensionless *efficiency* — the Landauer ratio

```
η_L = I_pred / N_max,   N_max = E_actual / (k_B T ln 2)
```

with the **self-payment** requirement that the numerator (predictive information a system holds about its own environment) and the denominator (the Landauer budget of its own dissipation) belong to one and the same physical system. A two-stage procedure — composite-index `I_v` screening, then `η_L` verification — is applied to six paradigm ("camertone") cases: the Sun, a hurricane, a crystal, a bacterium, a large language model, and a major city (plus the biosphere).

## Contents

```
paper/
  main.md / main.ru.md               Manuscript — English (submission language) / Russian (primary)
  supplementary.md / supplementary.ru.md   Supplementary material — English / Russian
  main.tex / main.ru.tex             LaTeX source (Springer Nature sn-jnl; generated from the .md)
  supplementary.tex / supplementary.ru.tex
  main.pdf (61 pp) / main.ru.pdf (63 pp)            Compiled manuscript
  supplementary.pdf (37 pp) / supplementary.ru.pdf (38 pp)
  refs.bib                           Bibliography
  sn-jnl.cls, sn-*.bst               Springer Nature template + bibliography styles (third-party; see LICENSE)
worked-example/                      Reproducible computations (standard library only)
  E-coli/  thermostat/  city/  biosphere/  LLM-as-corp/
docs/
  highlights.md                      Article highlights
```

## Recompiling the PDFs

Precompiled PDFs are included for direct reading. To rebuild from the `.tex` you need a TeX distribution with `pdflatex` and `bibtex` (TeX Live or MiKTeX). The Springer Nature template files (`sn-jnl.cls`, `sn-*.bst`) are bundled, so no further downloads are required. The reference style is `sn-mathphys-ay` (author–year). Standard cycle for any document, e.g. `main`:

```bash
cd paper
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

(replace `main` with `supplementary`, `main.ru`, or `supplementary.ru` for the other documents).

## Reproducing the worked examples

Each `worked-example/<system>/` is self-contained and uses **only the Python standard library** (no `pip install` required, except E-coli's optional `sensitivity.py`):

```bash
cd worked-example/E-coli && python eta_L_ecoli.py
```

The output should match the committed `expected_output.txt` up to floating-point round-off. Each folder has a `README.md` (English, default) and `README.ru.md` (Russian) documenting the model, parameters with literature, expected results, and status. `worked-example/README.md` / `README.ru.md` is the index.

## License

- **Text, figures, data** (manuscript, supplementary, bibliography, READMEs, expected outputs): **Creative Commons Attribution 4.0 International (CC BY 4.0)** — see [`LICENSE`](./LICENSE).
- **Source code** under `worked-example/`: **MIT License** — see [`worked-example/LICENSE`](./worked-example/LICENSE).

## Citation

Archived materials (this repository):

> Andriishin, A. *Landauer Efficiency of Self-Modeling: An Operational Scale of Vitality.* Zenodo, 2026. https://doi.org/10.5281/zenodo.20262946

The deposit is published on Zenodo with the DOI above. A machine-readable citation is in [`CITATION.cff`](./CITATION.cff). The journal version of record will be added as a separate reference upon acceptance.
