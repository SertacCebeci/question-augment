# question-augment

A self-growing, multi-disciplinary scientific wiki about **asking good
questions and giving good answers**, task-agnostically. The only output
is the wiki in `wiki/`; it grows on its own. The goal and its
constraints are in [`INTENT.md`](INTENT.md); the whole machine is
described in [`CLAUDE.md`](CLAUDE.md).

One question decides what enters:

> *Does this knowledge change how a question is generated, selected,
> formulated, answered or evaluated?*

## What is here

```text
INTENT.md          the goal and its constraints
wiki/              the notes, flat — open it as an Obsidian vault
meta/              the state: config, every work seen, the search queue, the arXiv sweep cursor, archived texts
tools/wiki.py      the one tool (python3 stdlib + curl + pdftotext)
.claude/           the agents (selector, reader, reviewer, explorer), the skills (grow, chat), the workflow
```

Each note is one concept: a one-line claim, the mechanism in prose, its
limits, links to related notes, and footnotes that quote the source
work verbatim. `python3 tools/wiki.py check` enforces this contract;
quotes are checked against the archived text in `meta/archive/`.
Fetched PDFs stay out of git; their extracted text is committed.

## How it grows

The loop runs in [Claude Code](https://claude.com/claude-code) as
`/grow` (one round) or as the `grow` workflow (N rounds unattended):

1. **Find** — search the query queue (OpenAlex, else arXiv) and walk
   the arXiv sweep backwards day by day.
2. **Decide** — the selector judges each candidate from title and
   abstract against the filter question.
3. **Read** — one reader per selected work writes a new note or
   enriches an existing one, grounded in the work's own text.
4. **Review** — one reviewer per reading passes or drops each note;
   everything else is reverted.
5. **Commit** — the check, then one commit with the round's numbers.

The loop only adds and enriches; the history is `git log`.

`/chat` answers from the notes alone, citing them; what the wiki cannot
answer becomes a new search.

## Requirements

- Python 3 (standard library only), `curl`, `pdftotext` (poppler)
- Claude Code, for the agents and the loop

```sh
python3 tools/wiki.py status   # one screen: notes, works, queue, sweep
python3 tools/wiki.py check    # the note contract; prints ok
```
