# Vitality as the Efficiency of Self-Paid Self-Modeling — open materials

*([Русская версия](./README.ru.md))*

Open-access materials for the article **«Vitality as the Efficiency of Self-Paid Self-Modeling»** (Russian primary; English translation included).

The article makes vitality measurable as a dimensionless *efficiency* — the predictive fraction of a system's self-model

```
V(X) = S ∧ (η_v > 0),    η_v = I_pred / I_mem = 1 − ν ∈ [0, 1]
```

where `η_v` is the fraction of the environmental memory a system retains that still predicts the future (its complement `ν` is *informational nostalgia*), and `S` is the **self-payment** predicate: the model, the dissipation that pays to hold it, and the error-return loop all belong to one and the same physical system. A two-stage procedure — composite-index `I_v` structural screening, then vitality verification by `(S, η_v)` — is applied to six paradigm cases: the Sun, a hurricane, a crystal, a bacterium (*E. coli*), a large language model, and a major city (plus the biosphere as a control limit). The bound `η_v ≤ 1` follows unconditionally from the data-processing inequality; the only fully computed case is the bacterium.

## Contents

```
paper/
  main.md / main.ru.md               Manuscript — English (submission language) / Russian (primary)
  supplementary.md / supplementary.ru.md   Supplementary material — English / Russian
  main.tex / main.ru.tex             LaTeX source (Springer Nature sn-jnl; generated from the .md)
  supplementary.tex / supplementary.ru.tex
  main.pdf (62 pp) / main.ru.pdf (64 pp)            Compiled manuscript
  supplementary.pdf (41 pp) / supplementary.ru.pdf (42 pp)
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

Each `worked-example/<system>/` is self-contained and uses **only the Python standard library** (no `pip install` required):

```bash
cd worked-example/E-coli && python eta_ecoli.py
```

The output should match the committed `expected_output.txt` up to floating-point round-off. The bacterium is the one numerically computed case (`η_v = I_pred / I_mem` via an exact Gaussian log-determinant), with `sensitivity.py` sweeping the model parameters (pinned in `expected_output_sensitivity.txt`); the other folders print **structural verdicts** `(S, η_v)` — the magnitude of `η_v` there requires mutual-information estimation and is not asserted. Each folder has a `README.md` (English, default) and `README.ru.md` (Russian) documenting the model, parameters with literature, expected results, and status. `worked-example/README.md` / `README.ru.md` is the index.

## License

- **Text, figures, data** (manuscript, supplementary, bibliography, READMEs, expected outputs): **Creative Commons Attribution 4.0 International (CC BY 4.0)** — see [`LICENSE`](./LICENSE).
- **Source code** under `worked-example/`: **MIT License** — see [`worked-example/LICENSE`](./worked-example/LICENSE).

## Citation

Archived materials (this repository):

> Andriishin, A. *Vitality as the Efficiency of Self-Paid Self-Modeling.* Zenodo, 2026. https://doi.org/10.5281/zenodo.21039160

The deposit is published on Zenodo with the DOI above. A machine-readable citation is in [`CITATION.cff`](./CITATION.cff). The journal version of record will be added as a separate reference upon acceptance.
