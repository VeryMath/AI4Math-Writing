# Math Beamer

Chinese guide: [README.zh-CN.md](README.zh-CN.md)

`math-beamer` is an AI4Math Skill for source-grounded mathematical Beamer
presentations. It helps coding agents turn papers, notes, proofs, lectures,
experiments, and existing slide decks into compilable LaTeX Beamer sources,
PDFs, review reports, and slide-to-source ledgers.

## When To Use It

Use this Skill when:

- you need a mathematical seminar, lecture, reading-group, defense, workshop,
  poster, or experiment-results deck;
- the slides must preserve theorem assumptions, proof status, notation,
  citations, formulas, algorithms, figures, and numeric results;
- you want a Beamer template selected from a curated template catalog and
  checked with a reproducible build command.

The template catalog spans general seminars, theorem/proof talks, paper
reading, optimization, numerical analysis, algorithms, probability/statistics,
geometry/topology, algebra/number theory, combinatorics/graph theory, logic and
category theory, core analysis, PDE, dynamical systems, control systems,
information/coding/cryptography, teaching, defense, workshop, backup-heavy
talks, data reports, and posters.

Do not use this Skill to make generic marketing slides, fabricate unsupported
mathematics, or publish third-party institutional templates without license and
branding review.

## What It Produces

The agent should produce a Beamer source tree, optional compiled PDF, build and
layout report, `slide-source-ledger.md`, and revision notes. It should also
name the selected template, build engine, unresolved mathematical risks, and
any license or branding constraints.

## Skill Entry Points

The shared workflow lives in:

| File | Purpose |
| --- | --- |
| `SKILL.md` | main workflow and review rules |
| `templates/catalog.yaml` | curated template catalog |
| `templates/preview-gallery.md` | visual template picker |
| `templates/previews/*.png` | compiled cover and content previews |
| `templates/packs/*/` | starter Beamer templates |
| `templates/slide-source-ledger.md` | source-grounding ledger |
| `templates/review-report.md` | build and review report |
| `references/` | source index, domain patterns, and policy notes |
| `agents/openai.yaml` | OpenAI/Codex metadata |

## Installation

Copy this to your coding agent:

```text
Please install the `math-beamer` skill from https://github.com/VeryMath/AI4Math-Writing.git (branch: main). Read the package README and SKILL.md, install the declared Skill entrypoint `math-beamer`, verify that `$math-beamer` is discoverable, and tell me whether I need to restart the agent.
```

If this package is used from the AI4Math Skill Library mirror, install the
directory containing this `SKILL.md`.

## Quick Start

```text
Use this repository's math-beamer workflow.

Read:
- SKILL.md
- templates/preview-gallery.md
- templates/catalog.yaml
- references/template-policy.md

Goal:
Create a 25-minute mathematical talk from the supplied paper notes.

Target:
<paper source, notes folder, or existing Beamer project>

Constraints:
- inspect first;
- inspect the visual gallery, then choose a template and slide budget before drafting;
- ask before compiling or using institutional branding;
- keep a slide-source ledger.
```

## How To Interact

Use the normal checkpoint loop:

| Decision | Meaning |
| --- | --- |
| `approve` | run the proposed next step |
| `revise` | update the plan before running |
| `reject` | stop this path |
| `skip` | skip this phase |
| `stop` | end the session and summarize state |

Recommended first interaction:

```text
First inspect the source packet and template catalog only. Then tell me:
1. which Beamer workflow applies;
2. which template you recommend;
3. which files or commands you would use;
4. what checkpoint needs my approve / revise / reject / skip decision.
```

## Workflow And Outputs

```text
source packet
  -> genre and audience analysis
  -> template selection
  -> talk thesis and section map
  -> representative sample frames
  -> full deck
  -> latexmk build
  -> PDF/log/source audit
  -> revision report
```

Durable artifacts should usually live under:

```text
outputs/<run_id>/
```

## Safety And Review Rules

- Keep theorem assumptions, quantifiers, domains, and proof status intact.
- Mark conjectures, heuristics, examples, experiments, and future work
  explicitly.
- Do not fabricate citations, theorem dependencies, or experiment numbers.
- Do not use local absolute paths or private files in public templates.
- Do not vendor downloaded templates unless license, branding, and personal
  data have been reviewed.
- Build with `latexmk` when compilation is approved and report the exact
  command.

## Repository Layout

```text
SKILL.md
README.md
README.zh-CN.md
LICENSE
requirements-preview.txt
agents/openai.yaml
references/
templates/
  catalog.yaml
  packs/
```

## Dependencies

Using the Skill instructions and existing previews has no Python runtime
dependency. Regenerating previews requires:

- Python 3.9 or newer with the package listed in
  `requirements-preview.txt`;
- `latexmk`, `pdflatex`, and `xelatex`;
- Poppler's `pdftoppm`;
- TeX packages used by the starter packs: Beamer, CTeX/`ctexbeamer`,
  AMSMath, AMS symbols/theorem support, Booktabs, PGF/TikZ, PGFPlots, and
  `beamerposter`.

Install the Python dependency with:

```bash
python3 -m pip install -r requirements-preview.txt
```

The bundled templates do not require network access, shell escape, or local
absolute paths.

## Maintainer Checks

Run from the `AI4Math-Writing` repository root:

```bash
python3 -m unittest discover -s tests -v
```

For template work, also compile changed starter decks with `latexmk` using the
engine listed in each `template.yaml`.

## License

The package is distributed under the MIT License in `LICENSE`. This statement
applies to package content for which VeryMath has redistribution authority.
Third-party templates remain reference sources unless their license, branding,
and personal-data rules allow redistribution.

## Contributor

Course contributor: **Conan Xu**. See
[`PROVENANCE.yaml`](PROVENANCE.yaml) and
[`NORMALIZATION.md`](NORMALIZATION.md) for the course-edition record.
