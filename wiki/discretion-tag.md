---
description: "MAIA's DISCRETION tag marks an axis as deliberately left to the downstream artist's judgement, protected from further questioning, unlike an axis nobody has addressed yet."
aliases: ["DISCRETION tag"]
sources: ["wang-2026"]
---
# Discretion tag

> Two axes can both carry no recorded value, one still owes a question, the other is closed on purpose. MAIA gives the brief a way to say which.

## Definition / Mechanism

Of MAIA's four per-axis tags, full definitions in [[verification-over-invention]], two mean "nothing here yet": UNADDRESSED and INFERRED. DISCRETION means something structurally different: the system, on the commissioner's behalf, decides not to constrain this axis at all, deferring it to the professional artist who later executes the brief.[^c1]

The distinction is enforced, not just labelled: an INFERRED tag is by construction a hypothesis awaiting the user's ratification, while a DISCRETION tag is protected from re-interrogation, the system may not go back and ask about it again.[^c2]

Wang, Lu, Chen & McGraw (2026) name the design property the tag implements constructive [[efe-planning-as-variational-inference|ambiguity]]: leaving room for it in the requirement is a design goal, not a residue of failed elicitation.[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Requirements engineering / multi-agent LLM systems (Wang et al. 2026) | DISCRETION (tag) | exact — the state-object label |
| Requirements engineering / multi-agent LLM systems (Wang et al. 2026) | constructive ambiguity | close — the design property the tag implements, not the state-object label; the term also has an established home in diplomacy, so it is not an alias of this note |

## Why it matters

Stall 10 asks how much an answer commits and how it signals the rest. In MAIA the brief is the system's committed answer to its downstream reader, the artist; DISCRETION is how that answer says "deliberately not committing here" as a named category, distinct from "nothing settled". UNADDRESSED and DISCRETION share the same surface, no value recorded against the axis, but opposite futures: one is still owed a question, the other is closed. Downstream, the system reports this to the artist as creative agency preserved via intentional blanks, in contrast to the visual anchors the brief does fix, an explicit design choice rather than an omission.[^c4]

## Transfer

| | |
|---|---|
| In its home field | one tag among four, applied per-axis inside a pre-declared eight-dimension checklist, read downstream by a professional artist |
| Here | any asker/answerer exchange where one party must signal "deliberately not constraining this" as distinct from "not yet asked" |
| What survives | splitting silence into a protected, intentional non-constraint versus an open, re-askable gap |
| What does not | the specific downstream reader (a human artist) and the claim that this protects "creative agency", that reading is the system's design intent, not something separately measured |

## Limits

- The "preserves creative agency" reading is design intent, not a separately measured outcome: the study's artist-autonomy scale did not move and was unreliable in the final briefs (negative ICC), so the authors draw no conclusion from it, including about DISCRETION's effect on agency.[^c5]
- The tag is self-reported by the system's own Diagnostician/Validator pipeline; nothing external checks that a DISCRETION tag was applied to an axis the user would in fact want deferred, rather than one the system simply failed to elicit. This reading is the wiki's own inference from the tagging scheme, not a finding of the paper.
- Evidenced in one domain (bespoke visual-art commissioning), with a small sample (N=16) and a single model (MiniMax M2.5), so cross-model transfer remains open.

## Related

[[verification-over-invention]] · [[axis-tag-completion]] · [[abstention]] · [[elicitation-protocols]]

[^c1]: wang-2026 — "D ISCRETION (deferred to the artist)."
[^c2]: wang-2026 — "spectable: an I NFERRED tag is by construction a hypothesis,"
[^c3]: wang-2026 — "requirements while leaving room for constructive ambiguity."
[^c4]: wang-2026 — "Creative agency preserved via"
[^c5]: wang-2026 — "† Autonomy scale unreliable in 𝐵"
