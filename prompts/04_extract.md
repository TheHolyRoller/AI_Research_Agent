# Stage 4 — Extract

Load `prompts/00_system.md`, the brief, `data/raw/plan.md`, and `data/raw/sources.md`.

## Goal

Turn sources into atomic finding records that can be written to CSV later.

## Write `data/raw/findings.json`

Top-level shape:

```json
{
  "brief_slug": "<slug>",
  "topic": "<topic>",
  "question": "<core question>",
  "generated_at": "<ISO datetime>",
  "findings": []
}
```

Each item in `findings` must match `templates/findings.schema.json` and `templates/finding.example.json`.

## Extraction rules

- One claim per record. If a paragraph contains three facts, write three records.
- `finding` is a standalone sentence.
- `evidence` must be traceable to `source_url`. Quote when the wording matters; paraphrase when it does not.
- Reuse source ids from gather in `notes` like `source:S001` so records stay joinable.
- `id` values are `F001`, `F002`, … in the order you extract.
- `stage` is `extract`.
- `confidence` at this stage is your read of source quality, not final verification:
  - `high` — official/primary, specific, dated
  - `medium` — credible but secondary or partly implicit
  - `low` — useful but thin, undated, or second-hand
- `tags` are short slugs (`pricing`, `limits`, `api`), not sentences.

## Constraints

- No finding without a `source_url` that appears in `data/raw/sources.md`.
- Do not copy marketing language as fact.
- If sources conflict, extract both claims as separate records and note the conflict in `notes`. Do not pick a winner yet.

## Done when

- `data/raw/findings.json` exists and is valid JSON
- Every record has the required fields
- Coverage of the plan's sub-questions is either complete or explicitly gapped in a `notes` record is not needed — list gaps in your chat reply instead
