# Slide Source Ledger

Store source attribution here by default. Keep this ledger separate from the
rendered slides; do not repeat its entries as per-slide source footers unless
the user explicitly requests visible citations.

| Slide | Claim / object | Source | Status | Risk | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | Title, authors, event | User-provided metadata | confirmed | low | Replace placeholders before release. |
| 2 | Talk outline | Generated from approved section map | draft | medium | Confirm timing and audience. |

## Status Values

- `confirmed`: directly supported by provided source.
- `needs-citation`: claim is plausible but citation is missing.
- `needs-proof`: mathematical statement needs proof or proof reference.
- `experimental`: supported only by experiment or computation.
- `conjectural`: should be labeled as conjecture, heuristic, or future work.
- `remove-or-soften`: unsupported or overstated.

## Required Checks

- Every theorem, lemma, proposition, corollary, and conjecture has a source.
- Every numeric result names the run, table, log, or dataset.
- Every figure names its source file and whether it was generated or copied.
- Every assumption omitted from a slide is listed in speaker notes or backup.
