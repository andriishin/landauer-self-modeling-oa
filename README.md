# Vitality as a Landauer Efficiency of Self-Modeling — open materials

Open-access materials for the article **«Vitality as a Landauer Efficiency of Self-Modeling»** (Russian primary; English translation included).

The article formulates vitality as a dimensionless *efficiency* — the Landauer ratio

```
η_L = I_pred / N_max,   N_max = E_actual / (k_B T ln 2)
```

with the **self-payment** requirement that the numerator (predictive information a system holds about its own environment) and the denominator (the Landauer budget of its own dissipation) belong to one and the same physical system. A two-stage procedure — composite-index `I_v` screening, then `η_L` verification — is applied to six paradigm ("camertone") cases: the Sun, a hurricane, a crystal, a bacterium, a large language model, and a major city (plus the biosphere).

## Contents

```
paper/
  main.md                    Manuscript — English (submission language)
  main.ru.md                 Manuscript — Russian (primary working language)
  main.tex                   LaTeX source (MDPI Entropy template; generated from main.md)
  main.pdf                   Compiled manuscript (27 pages)
  supplementary.md           Supplementary material — English
  supplementary.ru.md        Supplementary material — Russian
  refs.bib                   Bibliography
  graphical-abstract.svg     Graphical abstract (vector)
  graphical-abstract.preview.png
  Definitions/               MDPI Entropy template (third-party; see LICENSE)
worked-example/              Reproducible computations (standard library only)
  E-coli/  thermostat/  city/  biosphere/  LLM-as-corp/
docs/
  highlights.md              Article highlights
  graphical-abstract-spec.md Graphical-abstract spec + MDPI export notes
```

## Recompiling the PDF

A precompiled `paper/main.pdf` is included for direct reading. To rebuild it from `main.tex` you need a TeX distribution with `pdflatex` and `bibtex` (MiKTeX or TeX Live). Run the standard MDPI cycle:

```bash
cd paper
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

The MDPI template files in `paper/Definitions/` are bundled, so no further downloads are required.

## Reproducing the worked examples

Each `worked-example/<system>/` is self-contained and uses **only the Python standard library** (no `pip install` required, except E-coli's optional `sensitivity.py`):

```bash
cd worked-example/E-coli && python eta_L_ecoli.py
```

The output should match the committed `expected_output.txt` up to floating-point round-off. Each folder has a `README.md` (English, default) and `README.ru.md` (Russian) documenting the model, parameters with literature, expected results, and status. `worked-example/README.md` / `README.ru.md` is the index.

## License

- **Text, figures, data** (manuscript, supplementary, bibliography, graphical abstract, READMEs, expected outputs): **Creative Commons Attribution 4.0 International (CC BY 4.0)** — see [`LICENSE`](./LICENSE).
- **Source code** under `worked-example/`: **MIT License** — see [`worked-example/LICENSE`](./worked-example/LICENSE).

## Citation

Archived materials (this repository):

> Andriishin, A. *Vitality as a Landauer Efficiency of Self-Modeling.* Zenodo, 2026. https://doi.org/10.5281/zenodo.20262947

The deposit is published on Zenodo with the DOI above. A machine-readable citation is in [`CITATION.cff`](./CITATION.cff). The journal version of record will be added as a separate reference upon acceptance.
