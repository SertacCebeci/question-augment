---
name: grow
description: Grow the wiki by one round (or N) - find works (search queue + arXiv sweep), let the selector decide what to read, fetch, read, review, keep what passes, commit. Use when the owner says "grow", "/grow", "run a round", "sweep", or wants the wiki to grow on its own. Never asks the owner anything mid-round.
---

# /grow [--rounds N]

One round, run by you with `tools/wiki.py` and four agents. Nothing in a
round asks the owner anything. Agent outputs go to `.claude/runs/`
(gitignored) with the Write tool.

## 1. Find

```bash
python3 tools/wiki.py harvest
```

Searches the next unsearched queries (OpenAlex, else arXiv), then walks
the arXiv sweep backwards from its cursor under the queries' vocabulary,
until a batch of candidates is pending. Skips both while the reading
backlog is full (reading first). If it says `"explore": true`, run the
**explorer** agent and queue its queries for the next round:

```bash
python3 tools/wiki.py query add --input .claude/runs/explore.json --origin explore
```

## 2. Decide what to read

If the batch has candidates: the **selector** agent with the batch path →
save its JSON as `.claude/runs/verdicts.json` →

```bash
python3 tools/wiki.py judge --input .claude/runs/verdicts.json
python3 tools/wiki.py fetch
```

## 3. Read and review

```bash
python3 tools/wiki.py next
```

One **reader** per listed work, all in one message (parallel), each given
key, title, text path. Then one **reviewer** per reader that returned
files (parallel), given key, text path and the files — say whether each
file is new or an enriched existing note. Readers and reviewers write
their JSON to `.claude/runs/round/<key>.package.json` / `.review.json`;
`apply` collects them:

```bash
python3 tools/wiki.py apply
```

`apply` keeps every note a review passed and the contract accepts,
reverts every other change under `wiki/`, marks the works read, and
queues the readers' queries. A reader that failed is read again next
round (set aside after two failures).

## 4. Commit

```bash
python3 tools/wiki.py commit
```

`commit` runs the check and commits the round with its numbers
(`grow: <date> | sweep a..b | select x/y | read n | notes +a ~b -c |
queries +q`). If the check fails it commits nothing and names the failing
notes: revert them (`git checkout -- <file>` or delete a new one) rather
than force them, and report what was lost.

## 5. Report

`python3 tools/wiki.py status`, then one short paragraph: found, selected,
read, notes new / enriched / dropped (with the reviewers' reasons), queries
added.

`--rounds N`: repeat; stop early when a round finds nothing, selects
nothing and has nothing to read.

## Unattended

Many rounds — the sweep over the horizon — run in the background as one
workflow that does exactly the steps above:

```text
Workflow({ scriptPath: ".claude/workflows/grow.js", args: { rounds: N } })
```

It stops at a round that does not commit or that finds and reads nothing.
