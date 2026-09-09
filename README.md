# AI Research Agent

Markdown prompt pipeline for a Cursor research agent. Python stitches the prompts and writes findings to CSV.

## Layout

- `prompts/` — stage-by-stage agent instructions
- `templates/` — brief and findings JSON schema
- `src/research_agent/` — prompt loader + CSV export
- `data/briefs/` — filled research briefs
- `data/raw/` — sources and `findings.json`
- `data/output/findings.csv` — exported rows

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

## Commands

Print the full prompt chain (or one stage):

```bash
python -m research_agent prompts
python -m research_agent prompts --stage extract
```

Start a brief:

```bash
python -m research_agent init-brief --topic "Your topic here"
```

Export findings JSON to CSV:

```bash
python -m research_agent export --input data/raw/findings.json --output data/output/findings.csv
```

In Cursor, open a chat in this repo and give it a topic. It will follow `AGENTS.md` and `prompts/_index.md`.
