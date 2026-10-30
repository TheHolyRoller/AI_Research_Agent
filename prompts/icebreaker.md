# Icebreaker compliments

Canonical guide: `prompts/main.md`. If this file and main.md disagree, follow main.md.

Load this file whenever the user asks for outreach DMs, icebreakers, or compliments. Use it with `00_system.md` and the enrichment rules in `main.md`. Do not invent facts. The like and the why must both come from verified public details.

## Goal

Write a compliment that says **what you like** about one particular thing the owner or business would actually be proud of, then **why you like it**.

## Classify first

Before the compliment, classify the company (consignment shop, affiliate seller, wholesaler, closeout buyer, corporate gifts, producer overlap, chain, or out of scope). Think through:

1. What problem this organisation is trying to solve.
2. What Black Horse can provide for that class.
3. What they would be proud of.

The compliment comes from (3). The pitch template in `message` comes from (1) and (2) via `prompts/main.md`. Do not praise a wholesaler as if they were a farm stand.

## Formula

One short sentence, or two if needed. No m-dashes.

`I like [specific thing] because [concrete reason].`

The reason has to be a real quality of that farm, product, or company. Not a score. Not a vibe word. Pick something they would brag about: a named product they built, a certification they earned, a farm they kept in the family, a recipe with a person's name, a building they restored, a training they completed, a way they grow or source that is not the default.

## Do not write (bland / canned)

These feel generic even when the noun is specific:

- The culinary medicine angle at 24 Karrot is rare.
- X is impressive.
- X is a great story.
- X is a sweet detail.
- X is a beautiful product.
- X is a rare combo.
- X looks like real craft.
- I like that you care about quality because customers notice.

A verdict with no "because" is canned. Calling something rare, impressive, or beautiful is not a why.

## Write this instead

- I like that 24 Karrot is built around culinary medicine because you cook from nutrition training, not just a menu.

That line names the thing (culinary medicine) and the reason (nutrition training behind the cooking).

## Rules

- Pick one particular. Do not praise the whole business.
- Start with I like or I love.
- Follow with because.
- Keep it short enough for an Instagram DM opener.
- No m-dashes.
- If there is no verified particular to like, leave the icebreaker blank. Do not fake a why.

## Where it goes

- CSV: add a `compliment` column. That is the custom like/because opener. `message` is Hey [name], then the compliment, then the class-matched template from `prompts/main.md`.
- Do not hide the compliment only inside `message`. It must have its own column.
- Do not put compliments in research finding `finding` fields. Findings stay facts.
