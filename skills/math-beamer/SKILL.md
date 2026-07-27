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
`templates/catalog.yaml`. Inspect both the cover and first-content preview and
select the smallest template that matches the mathematical genre:

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

## Workflow

1. Inspect the source packet and identify the mathematical genre: theorem,
   proof, algorithm, computation, experiment, survey, lecture, defense, or
   poster.
2. Ask only for blocking choices: audience, language, duration, template,
   authoritative source, build permission, and whether institutional branding
   is allowed.
3. Create a talk thesis, section map, and slide budget. Keep most talks to two
   to four main sections unless the user requests a long lecture.
4. Choose a template from `templates/catalog.yaml` and explain why it fits.
5. Draft one or two representative frames before a full deck when the visual
   direction or mathematical density is uncertain.
6. Build the full deck from source-grounded claims. Preserve assumptions,
   domains, quantifiers, theorem status, proof status, citations, and numeric
   results.
7. Write or update `slide-source-ledger.md` while drafting, not after the fact.
8. Compile with the appropriate engine when approved:
   - English default: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
   - Chinese or mixed CJK default:
     `latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex`
9. Audit the log, PDF, references, citations, figures, fonts, overfull boxes,
   navigation, and frame density.
10. Return the deck, evidence, unresolved risks, and next revision options.

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
