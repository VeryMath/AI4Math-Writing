# Build And Layout Audit

## Build Commands

- English default:
  `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
- Chinese or mixed CJK default:
  `latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex`
- Clean generated files when needed:
  `latexmk -C main.tex`

Ask before installing TeX packages, enabling shell escape, using `minted`,
externalizing TikZ, or changing system fonts.

## Hard Failures

- Fatal LaTeX errors.
- Missing figures, `.sty`, `.cls`, `.bib`, or data files.
- Undefined references or citations after rerun.
- Duplicate labels.
- Bibliography backend mismatch.
- Absolute paths or files outside the deck tree.

## Layout Risks

- Overfull boxes, especially formulas and tables.
- Dense frames with too many bullets or proof steps.
- Frame titles that collide with navigation.
- Figures with unreadable labels or legends.
- Tables with more columns than the slide can support.
- Backup slides counted as part of the main talk when they should not be.

## Mathematical Meaning Risks

- Removed assumptions.
- Hidden domains, dimensions, or boundary conditions.
- Symbols reused for different objects.
- Proof sketch presented as proof.
- Numeric result copied without run, dataset, or metric source.
