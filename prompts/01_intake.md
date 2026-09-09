# Stage 1 — Intake

Load `prompts/00_system.md` first.

## Goal

Turn the user's request into a locked research brief.

## Ask only if missing

- Core question (one sentence)
- Why it matters / who it is for
- Time window (e.g. last 12 months, or all-time)
- Must-include sources or domains
- Must-avoid topics
- Depth: `quick` | `standard` | `deep`
- Output extras besides CSV (synthesis only is the default)

Do not stall for nice-to-haves. Infer reasonable defaults and state them in the brief.

## Write

Copy `templates/research_brief.md` to `data/briefs/<slug>.md`.

Slug rules: lowercase, hyphens, no dates unless the user wants a dated job.

Fill every section. Empty optional fields stay as `n/a`.

## Done when

- The brief exists on disk
- The question is a single sentence
- Scope, exclusions, and success criteria are explicit
- You tell the user the slug and the next stage (`02_plan`)
