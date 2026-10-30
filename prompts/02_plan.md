# Stage 2 — Plan

Canonical guide: `prompts/main.md`. If this file and main.md disagree, follow main.md.

Load `prompts/00_system.md`, `prompts/main.md`, and the current brief in `data/briefs/`.

## Goal

Write a research plan that can be executed in the gather stage without re-litigating scope.

## Write `data/raw/plan.md` with these sections

1. **Question** — copy from the brief
2. **Sub-questions** — 3 to 7, each answerable with evidence. For enrichment: who is in charge, what class, what contact path, what proud particular, what problem/offer fit.
3. **Queries** — search strings you will actually run
4. **Source types** — where you will look first (docs, papers, news, datasets, forums)
5. **Priority order** — what you check first vs later
6. **Inclusion rules** — what counts as in-scope
7. **Exclusion rules** — what you will skip
8. **Success criteria** — when gather/extract is good enough to stop
9. **Open risks** — likely gaps, paywalls, stale pages

## Constraints

- Stay inside the brief's time window and exclusions.
- Prefer fewer sharp queries over a long unfocused list.
- If the brief is `quick`, cap sub-questions at 3 and sources at a small set.

## Done when

- `data/raw/plan.md` exists
- Every sub-question maps to at least one query
- You tell the user the plan in short form and wait only if they asked to approve it; otherwise continue to gather
