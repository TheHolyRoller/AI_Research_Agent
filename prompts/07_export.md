# Stage 7 — Export

Canonical guide: `prompts/main.md`. If this file and main.md disagree, follow main.md.

Load `prompts/00_system.md`, `prompts/main.md`, and confirmed `data/raw/findings.json`.

## Goal

Write the CSV that is the tabular deliverable.

## Do this

1. Confirm `data/raw/findings.json` is valid JSON and every finding has required fields.
2. From the repo root, run:

```bash
python -m research_agent export --input data/raw/findings.json --output data/output/findings.csv
```

3. Read the command output. Confirm the row count matches `findings.length`.
4. Open the output CSV and spot-check 2–3 rows against the JSON.
5. For enrichment, write the outreach CSV from verified findings plus class, contacts, compliment, and the matching pitch template in `prompts/main.md`. Use a job-specific `--output` when the brief names one. Do not overwrite `data/output/findings.csv` unless the user named that file.

## If export fails

Fix the JSON (types, missing fields, invalid `source_type` / `confidence`) and run export again. Do not hand-edit the CSV unless the user asks; the JSON is the source of truth.

## Done when

- The named output CSV exists (job-specific path, or `data/output/findings.csv`)
- Row count matches verified findings
- Enrichment outreach rows use the class-matched pitch from `prompts/main.md`
- You report the output path, row count, and where the synthesis lives
