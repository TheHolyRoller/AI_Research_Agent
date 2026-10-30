# AI Research Agent

Markdown prompt pipeline for a Cursor research agent. Python stitches the prompts and writes findings to CSV.

The operating file is `prompts/main.md`. Numbered files in `prompts/` are stage slices. Enrichment jobs (owners, contacts, icebreakers, pitches) follow that main guide: classify each company, then pick consignment, affiliate, wholesaler, or closeout copy.

## Layout

- `prompts/main.md` — full research + enrichment guide
- `prompts/` — stage-by-stage slices
- `templates/` — brief and findings JSON schema
- `src/research_agent/` — prompt loader + CSV export
- `data/briefs/` — filled research briefs
- `data/raw/` — sources and `findings.json`
- `data/output/` — exported rows and synthesis

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

## Commands

Print the main guide (or one stage):

```bash
python -m research_agent prompts
python -m research_agent prompts --stage extract
python -m research_agent prompts --stage main
```

Start a brief:

```bash
python -m research_agent init-brief --topic "Your topic here"
```

Export findings JSON to CSV:

```bash
python -m research_agent export --input data/raw/findings.json --output data/output/findings.csv
```

In Cursor, open a chat in this repo and give it a topic. It will follow `AGENTS.md` and `prompts/main.md`.
