# CLAUDE.md

A self-growing scientific wiki about asking and answering well
(`INTENT.md`). This file is the whole machine: three things — **notes**,
**three state files**, **one loop**.

Start a session with `python3 tools/wiki.py status` (also the
SessionStart hook).

## Layout

```text
INTENT.md                 the goal and its constraints — the owner's
wiki/<concept>.md         the notes, flat; open wiki/ as the Obsidian vault
meta/config.json          the owner's settings: question, filter, budgets (reads, candidates, queries per round, the sweep's share of a batch), the sweep (arXiv cats, from, months)
meta/sources.jsonl        every work ever seen, one line each: ids, title, verdict (pending|select|null), why, read, notes, file
meta/queries.jsonl        the search queue: q, origin (chat|owner|reader|explore|seed), searched, found, selected
meta/sweep.json           the arXiv sweep's cursor (a day; it walks backwards)
meta/archive/<key>.pdf|html, <key>.txt    the fetched work and its text — what readers read and quotes are checked against
tools/wiki.py             the one tool (python3 stdlib + curl + pdftotext)
.claude/agents/           selector · reader · reviewer · explorer
.claude/skills/           grow · chat
.claude/workflows/grow.js the same loop, N rounds unattended (`args: {rounds: N}`)
```

`meta/` is written by `tools/wiki.py` only. Notes are written by the
reader agent only, inside the loop.

## The note

```markdown
---
description: "the claim in one line, 80–200 characters"
aliases: ["other names"]
sources: ["key", …]
---
# Concept

Mechanism, concretely, in prose.[^c1]

## Limits

## Related

- [[other-note]] — how

[^c1]: key — "exact quote from meta/archive/key.txt"
```

`python3 tools/wiki.py check` enforces, on every Write/Edit (hook) and
before every commit:
- exactly these three frontmatter keys, and a description of 80–200
  characters;
- a `# title` and a `## Limits` section;
- a `## Related` section with at least one link, and every `[[link]]`
  resolving to a note;
- at least one footnote, every `[^ref]` defined;
- every footnote `key` or `key — "quote"`, with the key in `sources:`
  and in `sources.jsonl`, and the quote found verbatim (normalized) in
  the work's text.

What a script cannot check is the reviewer's to judge: mechanism, not
advice; an honest voice (a conjecture never in a theorem's); real
limits; one object, new.

## The loop — `/grow`

1. **Find**: `wiki.py harvest`.
   - It searches the next unsearched queries (OpenAlex, else arXiv).
   - Every round it also walks the arXiv sweep back from its cursor,
     day by day, until the sweep alone added `sweep_share` of a batch. A listed work passes
     if it carries ≥ 75 % of one query's stems. The sweep spans
     `sweep.months` months back from `sweep.from`.
   - A work without an abstract is `null` ("no abstract"): there is
     nothing to judge it from.
   - It does nothing while `3 × reads_per_round` selected works are
     unread or a batch of candidates is pending: reading and judging
     come first.
   - When the queue runs dry, the **explorer** proposes queries.
2. **Decide**: the **selector** judges each candidate from title and
   abstract by the filter alone (`select` or `null`, with why) →
   `wiki.py judge` → `wiki.py fetch`. The wiki decides what it reads.
3. **Read**: `wiki.py next` → one **reader** per work, in parallel.
   - A concept the wiki lacks becomes a new note.
   - A concept it holds is enriched with an Edit.
   - Each reader returns the files it touched and ≤ 3 queries.
4. **Review**: one **reviewer** per reading, pass or drop per note →
   `wiki.py apply`.
   - It keeps what passed and what the check accepts.
   - It reverts every other change under `wiki/`.
   - It marks the works read and queues the readers' queries.
5. **Commit**: `wiki.py commit` — the check, then one commit with the
   round's numbers: `grow: <date> | sweep a..b | select x/y | read n | notes +a ~b -c | queries +q`.

The loop only adds and enriches. It never deletes or rewrites an
accepted note and never asks the owner anything. The history is `git
log`.

## Chat — `/chat`

Answer from the notes alone, citing them. What the wiki cannot answer
becomes a search: `wiki.py query add "…" --origin chat`.

## The owner's levers

- `INTENT.md`;
- `meta/config.json` (filter, budgets, sweep);
- `wiki.py query add "…"` (a search);
- `wiki.py null --key K --why "…"` (refuse a work);
- `/grow`, `/chat`.

Nothing else. Notes are not written or edited by hand.

## Rules

- Everything in the repository is **English**; conversation with the
  owner is in **Turkish**.
- No branches; everything is committed to `main`.
- Changes to the machine commit as `machine: …`.
- `python3 tools/wiki.py check` must print `ok` before every commit (the
  Stop hook runs it too).
