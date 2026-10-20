---
description: "Three fixed-role AI personas (clarify, organize, challenge) respond in parallel to diagnose a user's stance, trading single-question selection for role coverage at a measured coordination cost."
aliases: ["StanceLab", "three-persona mode", "multi-persona elicitation"]
sources: ["hong-2026"]
---
# Role-differentiated parallel elicitation

> Instead of choosing one next question, ask three role-fixed questions at
> once — and pay for the parallelism in the answerer's coordination load.

## Definition / Mechanism

StanceLab (Hong, Kuo, Chen & Wang (2026)) is a prototype for
preparing a personal stance before a discussion. Its three-persona mode
sends every user message to three fixed role-prompts in parallel, each
targeting one distinct preparatory move instead of a single ranked
question: "The Interviewer prompt asks one focused, non-[[leading-question-rule|leading question]] to
surface missing context; the Mentor prompt offers one organizing insight or
concrete suggestion; and the Opponent prompt gives one respectful but sharp
challenge or edge case."[^c1]

The user inspects all three responses, replies to any of them, and moves
selected points into a draft workspace — so axis selection is delegated to
the user choosing among three simultaneous candidates rather than the
system ranking and asking one.

## Findings

A within-subject formative pilot (6 participants, 12 sessions, a standalone
single-LLM mode as the comparison condition) found persona value was
conditioned on producing a usable move, not on having three responses
instead of one: "these cases suggest that multipersona AI should be
evaluated by whether at least one response produces an actionable
diagnosis: a missing context question, a weak assumption, an objection, or
a useful reframe."[^c2]

Parallel delivery itself carried a cost participants named directly. P06
described the three-persona mode as: "It felt a bit like having to talk to
three people at once... I normally cannot suddenly handle that many things
at once. I tend to reply to one at a time, and that can already take
70–80% of my attention."[^c3]

A second participant (P03) described the session as one question-answer
exchange becoming three, with "not much difference" felt overall —
coordination load, not novelty, was the dominant experience for at least
three of six participants. Role value was also uneven and asymmetric in
risk: the Interviewer failed by producing vague agreement or overlapping
the Mentor; the Mentor failed by becoming reassurance without changing the
argument; the Opponent was "high-risk and high-reward," failing when it
argued a point the user had already moved past (Table 2 of the source).

## Why it matters

Most of this stall's selection literature ([[mutual-information]],
[[expected-information-gain]], [[optimal-decision-tree]]) picks one next
question by a ranking criterion and asks it. StanceLab's three-persona mode
is a different bet: cover three named diagnostic moves (clarify, organize,
challenge) in parallel and let the person pick which one was useful,
instead of computing which one to ask first. The pilot's own finding is
that this bet has a real, named cost — coordination load on the person
receiving three simultaneous questions — which is the same kind of cost
[[question-budgets]] prices as the reason a user's attention is scarce,
here observed directly rather than assumed.

## Limits

- Formative pilot: 6 participants, 12 sessions, one within-subject design
  with topic and mode confounded; the source itself calls the mode
  comparison descriptive, not a controlled test, and reserves general
  claims for future controlled studies.
- The three roles are fixed, hand-authored prompts, not derived from any
  selection criterion — nothing in the source computes which of the three
  moves is worth asking for a given user state.
- The coordination-load finding rests on unstructured interview quotes from
  three of six participants, not a validated workload instrument (contrast
  [[question-budgets]]'s NASA-TLX measurement of interruption cost, which
  this pilot does not use).

## Related

[[multi-agent-clarification]] · [[question-budgets]] · [[mutual-information]] · [[expected-information-gain]]

[^c1]: hong-2026 — "The Interviewer prompt asks one focused, non-leading question to surface missing context; the Mentor prompt offers one organizing insight or concrete suggestion; and the Opponent prompt gives one respectful but sharp challenge or edge case."
[^c2]: hong-2026 — "these cases suggest that multipersona AI should be evaluated by whether at least one response produces an actionable diagnosis: a missing context question, a weak assumption, an objection, or a useful reframe."
[^c3]: hong-2026 — "It felt a bit like having to talk to three people at once... I normally cannot suddenly handle that many things at once. I tend to reply to one at a time, and that can already take 70–80% of my attention."
