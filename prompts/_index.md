# Prompt pipeline

Run these stages in order. Each file is a complete instruction for that stage. The system rules in `00_system.md` apply to every stage.

| Order | File | Purpose | Writes |
| --- | --- | --- | --- |
| 0 | `00_system.md` | Identity, rules, output contracts | — |
| 1 | `01_intake.md` | Lock the research question and constraints | `data/briefs/<slug>.md` |
| 2 | `02_plan.md` | Search plan, source types, success criteria | `data/raw/plan.md` |
| 3 | `03_gather.md` | Collect sources | `data/raw/sources.md` |
| 4 | `04_extract.md` | Turn sources into structured findings | `data/raw/findings.json` |
| 5 | `05_verify.md` | Score confidence, flag contradictions | `data/raw/findings.json` (updated) |
| 6 | `06_synthesize.md` | Themes, gaps, recommended next steps | `data/output/synthesis.md` |
| 7 | `07_export.md` | Hand off to Python CSV export | `data/output/findings.csv` |
| — | `icebreaker.md` | How to write outreach compliments (what you like, and why) | CSV `icebreaker` / `message` when asked |

## Operator notes

- One research job at a time unless the user says otherwise.
- Keep the brief slug stable across stages (example: `cursor-agent-pricing`).
- If a stage cannot finish, write what you have, list blockers, and stop. Do not invent the missing pieces.
- After extract, the CSV is the system of record for tabular data. Markdown files stay as working notes.
