<div align="center">

# AI4Math · Writing

Source-grounded workflows for mathematical paper drafting, proof-obligation
review, and submission-ready LaTeX checks.

[中文说明](README.zh-CN.md) · [Contributors](CONTRIBUTORS.md) · [Skill packages](#skill-packages) · [Installation](#installation) · [Quick start](#quick-start) · [Security model](#security-and-scope)

![version](https://img.shields.io/badge/version-0.1.0-blue)
![skills](https://img.shields.io/badge/skills-2-2ea44f)
![license](https://img.shields.io/badge/license-MIT-green)

</div>

<p align="center">
  If this project helps your work, please consider giving the repository a Star ⭐
  <a href="https://github.com/VeryMath/AI4Math-Writing"><img alt="GitHub stars" src="https://img.shields.io/github/stars/VeryMath/AI4Math-Writing?style=social"></a>
</p>

## What This Repository Is

This repository is the AI4Math home for mathematical paper-writing skills. It
does not replace source evidence, proof checking, or experiment validation.
Instead, the package under `skills/` gives coding agents a structured workflow
for turning verified materials into paper text and review artifacts.

Use the root page as the public map, then open the package-local README and
`SKILL.md` before writing.

## Skill Packages

| Package | Use it for | Start here |
| --- | --- | --- |
| [`paper-writing`](skills/paper-writing/) | Draft, revise, structure, and audit mathematical papers from supplied sources, including claim-evidence review, proof-obligation checks, notation checks, formula readability, and LaTeX preflight. | [`README`](skills/paper-writing/README.md) · [`SKILL`](skills/paper-writing/SKILL.md) |
| [`math-beamer`](skills/math-beamer/) | Build source-grounded mathematical Beamer decks, choose auditable templates, compile them, inspect layout, and maintain a slide-to-source ledger. | [`README`](skills/math-beamer/README.md) · [`SKILL`](skills/math-beamer/SKILL.md) · [`gallery`](skills/math-beamer/templates/preview-gallery.md) |

## Installation

The recommended path is AI-assisted installation: ask your coding agent to clone
or update this repository, read the Skill instructions, install the entrypoint,
and verify discovery.

```text
Please install this AI4Math Skill for me.

Repository: https://github.com/VeryMath/AI4Math-Writing.git
Branch: main
Skill paths:
- skills/paper-writing
- skills/math-beamer

Steps:
1. Clone or update the repository locally.
2. Read README.md, SKILL.md, and the target Skill entrypoint.
3. If this environment supports local Skill discovery, link the directory that contains SKILL.md into the local skills directory.
4. Keep sibling support directories in place when the Skill depends on them.
5. Verify that the installed Skill is discoverable.
6. Tell me the installed path, whether a restart is needed, and give me one test prompt.
```

Manual fallback for Codex-style local discovery:

```bash
git clone https://github.com/VeryMath/AI4Math-Writing.git
cd AI4Math-Writing
mkdir -p ~/.codex/skills
ln -s "$PWD/skills/paper-writing" ~/.codex/skills/paper-writing
ln -s "$PWD/skills/math-beamer" ~/.codex/skills/math-beamer
```

If your agent uses a different local Skill directory, replace `~/.codex/skills`
with that configured path.

## Quick Start

Clone the repository and open the package:

```bash
git clone https://github.com/VeryMath/AI4Math-Writing.git
cd AI4Math-Writing
```

Start with:

```text
skills/paper-writing/SKILL.md
```

For mathematical presentations, start with:

```text
skills/math-beamer/SKILL.md
```

## Repository Layout

```text
AI4Math-Writing/
├── README.md
├── README.zh-CN.md
├── SKILL.md
└── skills/
    ├── paper-writing/
    └── math-beamer/
```

## Validation

Run:

```bash
python3 -m unittest discover -s tests -v
```

For template changes, also compile the affected starter packs with the engine
declared in each `template.yaml`.

## Security and Scope

Do not commit private drafts, unpublished reviewer material, confidential
experiment logs, API keys, `.env` files, or generated caches. Public examples
and templates should be source-neutral and safe to redistribute.
