# Research agent

This workspace is a Cursor research agent. `prompts/main.md` is the agent. The numbered files in `prompts/` are stage slices. Python is only for loading those prompts and writing CSV.

## How to run a research job

1. Copy `templates/research_brief.md` to `data/briefs/<slug>.md` and fill it in, or ask the user for a topic and write that brief first.
2. Follow `prompts/main.md`. Do not skip stages unless the user says to.
3. Write working files under `data/raw/` during gather/extract/verify.
4. Write the structured finding records to `data/raw/findings.json` using `templates/findings.schema.json`.
5. Export with:

```bash
python -m research_agent export --input data/raw/findings.json --output data/output/findings.csv
```

Use a job-specific `--output` when the brief names one. Do not overwrite `data/output/findings.csv` unless the user named that file.

## Rules

- Follow `prompts/main.md` on every stage, including enrichment jobs (owners, contacts, icebreakers, pitches).
- Classify each company before writing a compliment or pitch. Use the consignment, affiliate, wholesaler, or closeout template that matches the class.
- Compliments: say what you like about one particular thing the owner or business would actually be proud of, then why. Do not write canned lines like "The culinary medicine angle at 24 Karrot is rare."
- Web jobs: if phone and email are both missing, flag it and capture the contact page. LinkedIn, Facebook, and Instagram do not always need phone or email; owner and compliment still have to be specific.
- Do not invent sources, URLs, quotes, or dates.
- Every CSV row must map to a record in `data/raw/findings.json`.
- If the user has not set a topic yet, start at intake in `prompts/main.md`.
