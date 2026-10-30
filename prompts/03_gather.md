# Stage 3 — Gather

Canonical guide: `prompts/main.md`. If this file and main.md disagree, follow main.md.

Load `prompts/00_system.md`, `prompts/main.md`, the brief, and `data/raw/plan.md`.

## Goal

Collect real sources that can support findings. You are not extracting full findings yet.

## Method

1. Run the queries from the plan.
2. Open and read candidates. Do not add a source you have not actually inspected.
3. Keep only sources that can answer at least one sub-question.
4. Drop duplicates, thin SEO posts, and undated claims when a dated primary source exists.

## Write `data/raw/sources.md`

Use one block per source:

```md
## S001 — <title>
- url:
- type: web | docs | paper | news | dataset | other
- published:
- retrieved:
- sub_questions: [q1, q3]
- why_included:
- snippet: "<short quote or close paraphrase>"
```

Also keep a short **Rejected** section at the bottom for notable misses (paywall, off-topic, duplicate), one line each.

## Constraints

- Every URL must be real and complete.
- If a page cannot be fetched, say so and skip it. Do not guess the contents.
- Capture `published` when the page states it; otherwise leave it blank.
- For `quick` briefs, stop at 5–8 solid sources. For `standard`, 8–15. For `deep`, keep going until success criteria in the plan are met or you hit diminishing returns.
- For enrichment, visit About, Contact, and vendor/partnership pages on purpose. If phone and email are both missing on a web job, capture the contact page URL anyway. For LinkedIn, Facebook, and Instagram, still gather the official site when the profile will not load; phone and email are optional on those channels.

## Done when

- `data/raw/sources.md` exists
- Each kept source has a URL, type, and why_included
- You have enough coverage to start extract, or you have listed the exact gaps
