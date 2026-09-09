# Research agent

This workspace is a Cursor research agent. The prompts in `prompts/` are the agent. Python is only for loading those prompts and writing CSV.

## How to run a research job

1. Copy `templates/research_brief.md` to `data/briefs/<slug>.md` and fill it in, or ask the user for a topic and write that brief first.
2. Follow `prompts/_index.md` in order. Do not skip stages unless the user says to.
3. Write working files under `data/raw/` during gather/extract/verify.
4. Write the structured finding records to `data/raw/findings.json` using `templates/findings.schema.json`.
5. Export with:

```bash
python -m research_agent export --input data/raw/findings.json --output data/output/findings.csv
```

## Rules

- Follow `prompts/00_system.md` on every stage.
- When writing outreach icebreakers, follow `prompts/icebreaker.md`: say what you like about one particular thing and why. Do not write canned lines like "The culinary medicine angle at 24 Karrot is rare."
- Do not invent sources, URLs, quotes, or dates.
- Every CSV row must map to a record in `data/raw/findings.json`.
- If the user has not set a topic yet, start at intake (`prompts/01_intake.md`).
