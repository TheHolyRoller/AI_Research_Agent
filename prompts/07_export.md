# Stage 7 — Export

Load `prompts/00_system.md` and confirmed `data/raw/findings.json`.

## Goal

Write the CSV that is the tabular deliverable.

## Do this

1. Confirm `data/raw/findings.json` is valid JSON and every finding has required fields.
2. From the repo root, run:

```bash
python -m research_agent export --input data/raw/findings.json --output data/output/findings.csv
```

3. Read the command output. Confirm the row count matches `findings.length`.
4. Open `data/output/findings.csv` and spot-check 2–3 rows against the JSON.

## If export fails

Fix the JSON (types, missing fields, invalid `source_type` / `confidence`) and run export again. Do not hand-edit the CSV unless the user asks; the JSON is the source of truth.

## Done when

- `data/output/findings.csv` exists
- Row count matches verified findings
- You report the output path, row count, and where the synthesis lives
