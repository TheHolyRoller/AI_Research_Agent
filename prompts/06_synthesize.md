# Stage 6 — Synthesize

Canonical guide: `prompts/main.md`. If this file and main.md disagree, follow main.md.

Load `prompts/00_system.md`, `prompts/main.md`, the brief, and verified `data/raw/findings.json`.

## Goal

Write a short research memo. This is interpretation. Do not add new unsourced facts; point back to finding ids.

## Write `data/output/synthesis.md`

```md
# <topic>

## Answer
<one paragraph that answers the brief's core question>

## Key findings
- F001 — ...
- F002 — ...

## Themes
### <theme>
<what the findings imply, with ids>

## Conflicts and uncertainty
<linked finding ids, what is still unknown>

## Gaps
<what the sources did not cover>

## Next research
<optional follow-up questions>
```

## Constraints

- Every bullet under Key findings cites an id from `findings.json`.
- If evidence is thin, say so in Answer. Do not paper over it.
- Keep the memo shorter than the raw notes. The CSV holds the table; this file holds the story.
- If the job includes outreach icebreakers, follow `prompts/main.md` and `prompts/icebreaker.md`. Compliments are not findings. Put them in CSV `compliment` / `message`, not in `finding` text.
- For enrichment, themes should include class mix, contact gaps, and compliment coverage.

## Done when

- `data/output/synthesis.md` exists
- Answer, key findings, and gaps are all present
