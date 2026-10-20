---
name: chat
description: Talk to the wiki - explain concepts and topics from the wiki alone, citing notes; what the wiki cannot answer becomes a search query. Use when the owner says "chat", "/chat", "chat with wiki", or asks what the wiki says about something.
---

# /chat

Answer from `wiki/` alone. Find notes with Grep (names, `aliases:`,
`description:` lines), Read the few that matter, and answer in the
owner's language, citing every note used as `[[note]]` and, for a
specific claim, the note's source key. Say plainly where the wiki is
silent or thin; do not fill it from your own knowledge.

What the wiki could not answer is not a failure — it is a gap found from
outside the wiki's blind spots. Record it, at most three per question,
as a search a search engine would match:

```bash
python3 tools/wiki.py query add "<3–8 word search string>" --origin chat
```

Never edit a note in chat. At the end, if queries were added, commit in
its own call: `chat: <n> queries`.
