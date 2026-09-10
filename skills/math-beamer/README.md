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
- use guided mode and stop at every checkpoint;
- show two or three visual template candidates and wait for my choice;
- build on the selected template source and preserve its visual framework;
- wait for outline approval and compiled sample approval before the full deck;
- ask before compiling or using institutional branding;
- keep a slide-source ledger.
```

## How To Interact

The default interaction is guided. The agent must complete one stage at a time
and stop at four mandatory checkpoints:

| Gate | Agent presents | User decides |
| --- | --- | --- |
| Brief | audience, language, duration, purpose, source, output | approve or revise the brief |
| Style | two or three templates with cover and content previews | choose or revise the style |
| Outline | talk thesis, section map, and slide budget | approve or revise the outline |
| Sample | compiled cover when present and representative content; the poster page for a poster | review content layout within the selected template |

The full deck starts only after these gates are approved or explicitly
skipped. Use the checkpoint responses:

| Decision | Meaning |
| --- | --- |
| `approve` | run the proposed next step |
| `revise` | update the plan before running |
| `reject` | stop this path |
| `skip` | skip this phase |
| `stop` | end the session and summarize state |

Recommended first interaction:

```text
Use guided mode. First inspect the source packet only. Then tell me:
1. what sources are present or missing;
2. which mathematical genre applies;
3. which brief decisions you need from me;
4. the current checkpoint and what happens after approval.

Do not choose the final template or generate the full outline yet.
```

## After Template Selection

The selected template defines the cover, typography, colors, page structure,
navigation, and block styles. The agent fills its source with your content,
then extends the approved samples into the full deck. Requests to polish the
slides keep that framework; only explicitly requested or chosen style changes
alter it. Existing choices also carry over to autonomous work and revisions.

Samples and the final deck are compared with the selected previews. Content
that does not fit is reworded, reflowed, or split across frames while preserving
mathematical meaning. See **Preserve The Selected Template** in
[`SKILL.md`](SKILL.md) for the full rules.

## Workflow And Outputs

```text
source packet
  -> source intake
  -> brief gate
  -> style gate with previews
  -> outline gate and slide budget
  -> compiled sample gate
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
