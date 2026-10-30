# Stage 5 — Verify

Canonical guide: `prompts/main.md`. If this file and main.md disagree, follow main.md.

Load `prompts/00_system.md`, `prompts/main.md`, the brief, sources, and `data/raw/findings.json`.

## Goal

Re-score and clean the findings so the CSV is safe to use.

## For each finding

1. Re-check the source. Confirm the evidence still matches the page.
2. Adjust `confidence` if needed.
3. Set `stage` to `verify`.
4. In `notes`, add `verified` or a short reason it is weak (`undated`, `secondary`, `conflict:F00X`).
5. Drop the record only if it is false, duplicated, or not actually supported. Prefer keeping low-confidence records over deleting uncertain ones.

## Conflict handling

If two findings disagree:

- Keep both
- Cross-link ids in `notes`
- Do not average them into a fake consensus

## Write

Overwrite `data/raw/findings.json` with the verified set. Keep `generated_at` as original extract time and add `verified_at` at the top level (ISO datetime).

## Done when

- Every remaining finding has `stage: verify`
- Conflicts are linked
- You can summarize: how many high / medium / low, and any unresolved contradictions
