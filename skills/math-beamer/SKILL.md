---
name: math-beamer
description: Use when creating, revising, or auditing source-grounded mathematical Beamer slide decks from papers, notes, proofs, lectures, experiments, or existing LaTeX slides across pure mathematics, applied mathematics, computational mathematics, statistics, optimization, geometry, topology, algebra, number theory, combinatorics, graph theory, logic, foundations, category theory, analysis, PDEs, dynamical systems, control theory, information theory, coding theory, cryptography, and teaching contexts.
---

# Math Beamer

Build and audit mathematical Beamer decks that are meant to be presented,
compiled, and traced back to source material. This skill covers mathematical
slide structure, not generic slide decoration.

## Use When

Use this skill when the user wants to:

- turn a mathematical paper, lecture note, proof sketch, experiment log, or
  theorem outline into a Beamer deck;
- revise an existing `.tex` Beamer project for mathematical clarity,
  source-grounded claims, or build reliability;
- select a reusable template for a seminar, reading group, defense, course,
  workshop, poster, or domain-specific math talk;
- audit theorem/proof/algorithm/formula/figure slides for notation,
  assumptions, overclaiming, and layout risks;
- build a Chinese, English, or bilingual mathematics deck with reproducible
  LaTeX commands.

Do not use this skill to invent results, prove unverified theorems, fabricate
citations, or make institutional-branded templates public without checking
license and logo rights.

## Inputs

- Required: presentation goal, source packet, target audience, language, talk
  duration or slide count, and preferred output folder.
- Optional: existing Beamer source, bibliography, figures, data files,
  institutional style constraints, template choice, handout/poster mode,
  speaker notes, and compile command.

If the source packet is missing, produce a source request or an outline of
needed evidence. Do not produce a full deck with unsupported claims.

## Guided Interaction Contract

Default to guided mode unless the user explicitly requests autonomous
execution or has already supplied an approved brief, template, outline, and
sample direction.

- Work on one stage at a time. Ask only for decisions needed by the current
  stage.
- End every guided response with a checkpoint containing:
  - current stage;
  - what was completed;
  - the decision needed from the user;
  - available responses: `approve`, `revise`, `reject`, `skip`, or `stop`;
  - what will happen after approval.
- Do not interpret silence, a new attachment, or a general acknowledgement as
  approval for a later stage.
- A user may combine stages only by explicitly providing the decisions for
  each skipped checkpoint.

The following gates are mandatory in guided mode:

1. **Brief gate**: confirm audience, language, duration, purpose, source of
   truth, and output form.
2. **Style gate**: show two or three suitable template candidates with cover
   and content previews; wait for the user to choose one.
3. **Outline gate**: present the talk thesis, section map, and slide budget;
   wait for approval or revision.
4. **Sample gate**: compile one or two representative frames and show the
   result; wait for approval of typography, density, colors, and formula
   treatment.

Do not build the full deck before all four gates have been approved or
explicitly skipped.

For the first response:

1. inspect the available source packet;
2. report the source inventory, likely mathematical genre, and missing
   evidence;
3. ask only for missing brief-gate decisions;
4. state the next checkpoint.

Do not select a final template, write a full outline, or generate a full deck
in the first response unless the user explicitly requests autonomous execution.

## Outputs

- Beamer source tree, usually `main.tex` plus figures, bibliography, and local
  style files when needed.
- PDF build output when compilation is approved and tools are available.
- `slide-source-ledger.md` mapping slide claims, theorem statements, formulas,
  algorithms, figures, and numeric results to sources.
- Build and layout report covering command, engine, warnings, errors,
  references, citations, missing assets, fonts, and overfull boxes.
- Revision notes that distinguish mathematical meaning risks from mechanical
  layout fixes.

## Template Selection

Start from `templates/preview-gallery.md`, then confirm metadata in
`templates/catalog.yaml`. Inspect both the cover and first-content preview.
Filter the catalog to two or three candidates and present each candidate with:

- template name and preview paths;
- visual character and mathematical genre fit;
- strengths, density risks, language, and build engine;
- a recommendation without silently making the final choice.

Wait for the style-gate decision before drafting the outline. Select the
smallest template that matches the mathematical genre:

| Need | Template family |
| --- | --- |
| General seminar | `seminar-minimal-en`, `seminar-minimal-zh` |
| Theorem-heavy talk | `theorem-proof-talk` |
| Paper reading group | `reading-group-paper` |
| Optimization | `optimization-talk` |
| Numerical analysis / scientific computing | `numerical-analysis-talk` |
| Algorithms / complexity | `algorithm-talk` |
| Probability / statistics | `probability-statistics-talk` |
| Geometry / topology | `geometry-topology-talk` |
| Algebra / number theory | `algebra-number-theory-talk` |
| Combinatorics / graph theory | `combinatorics-graph-talk` |
| Logic / foundations / category theory | `logic-foundations-category-talk` |
| Core analysis | `analysis-core-talk` |
| PDE | `pde-analysis-talk` |
| Dynamical systems | `dynamical-systems-talk` |
| Control systems | `control-systems-talk` |
| Information / coding / cryptography | `information-coding-crypto-talk` |
| Experiment or data report | `data-experiment-results` |
| Chinese course lecture | `course-lecture-zh` |
| Thesis defense | `thesis-defense` |
| Workshop tutorial | `workshop-tutorial` |
| Backup-heavy research talk | `backup-heavy-talk` |
| Poster | `beamerposter-a0` |

Institutional or downloaded templates are references until their license,
branding, personal data, and build status are checked.

## Guided Workflow

### Stage 0: Source Intake

Inspect the source packet and identify the mathematical genre: theorem, proof,
algorithm, computation, experiment, survey, lecture, defense, or poster.
Separate confirmed sources from missing or conflicting evidence.

### Stage 1: Brief Gate

Confirm audience, language, duration or slide count, presentation purpose,
authoritative source, output folder, build permission, and institutional
branding constraints. Recommend sensible defaults, but wait for approval.

### Stage 2: Style Gate

Show two or three template candidates from the preview gallery. Explain the
tradeoffs and wait for the user to select or revise the shortlist.

### Stage 3: Outline Gate

Create a talk thesis, section map, and slide budget. Keep most talks to two to
four main sections unless the user requests a long lecture. Identify the role
of each planned theorem, proof, algorithm, figure, or experiment frame. Wait
for approval.

### Stage 4: Sample Gate

Draft and compile one or two representative frames. Prefer a content-dense
mathematical frame over title-only samples. Show the rendered result and wait
for approval of typography, density, colors, notation, and formula treatment.

### Stage 5: Full Deck

Build the full deck from source-grounded claims. Preserve assumptions, domains,
quantifiers, theorem status, proof status, citations, and numeric results.
Write or update `slide-source-ledger.md` while drafting, not after the fact.

### Stage 6: Build And Audit

Compile with the appropriate engine:
   - English default: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
   - Chinese or mixed CJK default:
     `latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex`

Audit the log, PDF, references, citations, figures, fonts, overfull boxes,
navigation, and frame density. Fix mechanical failures and report any change
that could affect mathematical meaning.

### Stage 7: Delivery

Return the deck, evidence ledger, build report, unresolved risks, and focused
revision options.

## Mathematical Coverage Rules

- Pure mathematics: separate definitions, examples, theorem statements,
  proof ideas, key lemmas, proof sketches, and limitations.
- Algebra and number theory: track notation, object categories, field/ring
  assumptions, examples, and dependency diagrams.
- Geometry and topology: prefer diagrams and local-to-global structure maps;
  record conventions for orientation, metrics, charts, homology, or bundles.
- Core analysis: preserve spaces, norms, operators, constants, convergence
  modes, regularity, limiting arguments, and counterexamples.
- PDE: preserve function spaces, boundary conditions, regularity, constants,
  domains, estimates, and weak/strong formulation choices.
- Combinatorics and graph theory: state finite/infinite setting, graph
  conventions, extremal parameters, random model, and dependency method.
- Logic, foundations, and category theory: state formal system, semantics,
  universe/size conventions, functorial direction, and coherence assumptions.
- Probability and statistics: state sample spaces, filtrations, distributions,
  estimators, sample sizes, confidence or concentration statements, and
  simulation conditions.
- Optimization: state variables, feasible sets, assumptions, algorithm steps,
  convergence claims, rates, solver/data conditions, and failure modes.
- Numerical analysis and scientific computing: include discretization, error
  metrics, stability conditions, implementation settings, and reproducibility.
- Dynamical systems: record phase space, invariant sets, stability notions,
  bifurcation parameters, and qualitative diagrams.
- Control systems: record state/input/output spaces, controllability or
  observability assumptions, stability notion, controller class, and robustness
  margins.
- Information, coding, and cryptography: record alphabets, channel or adversary
  model, rate/security parameter, asymptotic regime, and theorem status.
- Teaching decks: optimize for one concept per slide, worked examples, recap
  frames, and exercises rather than paper-style claim density.

## Review Rules

- Do not remove assumptions or quantifiers to fit a slide.
- Do not upgrade conjectures, heuristics, experiments, or proof sketches into
  proved statements.
- Do not invent citations, theorem names, lemma dependencies, or numeric
  results.
- Keep formulas readable using `align`, `split`, `multline`, `cases`, and
  short prose anchors; avoid raw `$$`.
- Use overlays only when they help the argument. Overlays must not change
  equation numbering or hide assumptions.
- Prefer relative paths for figures and data. Do not reference local absolute
  paths.
- Treat institutional logos, school colors, and downloaded templates as
  license-gated assets.

## Failure Modes

- Missing source packet: list required sources and provide only a deck outline.
- Conflicting sources: identify the conflict and ask which source is
  authoritative.
- Compile failure: report root file, command, engine, first fatal error,
  missing files, unresolved references/citations, and the smallest next fix.
- Layout failure: identify overloaded frames, long formulas, overfull boxes,
  unreadable figures, and title/navigation collisions.
- License or branding uncertainty: keep the template in the reference index and
  do not vendor it into public templates.

## References

Read only the relevant files:

- `references/math-domain-patterns.md`
- `references/build-and-layout-audit.md`
- `references/template-source-index.md`
- `references/template-policy.md`
- `templates/preview-gallery.md`
- `templates/previews/`
- `templates/catalog.yaml`
