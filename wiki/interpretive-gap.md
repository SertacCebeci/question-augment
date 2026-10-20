---
description: "In a reflection-support dialog agent, the same observable behavior pattern was traced by users to 9 different self-reported reasons, so picking the next axis from the pattern alone is underdetermined."
aliases: ["interpretive gap"]
sources: ["tarvirdians-2026"]
---
# Interpretive gap

> The behavioral pattern an agent can observe (e.g. sustained focus on one
> topic) and the reason a user actually has for it are not the same thing —
> and in a 62-participant study the same pattern mapped to as many as 8 of 9
> distinct reasons.

## Definition / Mechanism

Tarvirdians, Hung & Oertel (2026) name the "interpretive
gap": the space between an agent's observable behavioral pattern and the
user's actual, often inaccessible, reason for it — "what we term the
interpretive gap, remains unstudied."[^c1]

They measured it by pausing a reflection-support agent (ReflectiMate) at
every point where it would otherwise silently redirect the conversation
toward a less-covered topic category, and asking the user to state their
interpretation before deciding what to do next. From 232 such moments
across 62 participants they "derive a taxonomy of nine interpretation
categories" — Deliberate Prioritisation, Self-Diagnosed Focus, Emotional
Driver, Decision Nature, Thinking Style, No Accessible Reason, Interaction
Attribution, Pattern Disputed, Content-Level Response.[^c2]

The gap is not a tail effect: moments that shared the same observable
system state (same dominant category, same observation type, comparable
coverage-score gap) still diverged in what users said caused it. The
largest such group — 19 moments the agent's policy treated identically —
"contained 19 moments spanning 8 of" the 9 categories.[^c3]

The three most frequent categories, led by Deliberate Prioritisation at
"n=64 (27.6%)", together account for "these three categories accounted
for 61.2% of all" collaborative moments — leaving more than a third of
moments in the other six categories.[^c4]

Downstream, whether the user's chosen next direction matched the agent's
silent default depended on which interpretation category they were in:
"Users selected the same action as the agent's default in 105 of 232
moments (45.3%)", and alignment by category ranged "from 22.2% to 60.0%
(Figure 2a)".[^c5]

## Why it matters

On stall 2 (which axis first), this is a measured case where the signal a
system already has (a coverage-asymmetry heuristic) determines which axis
*looks* under-explored, but not *why* it is under-explored — and the why
changes what the next question should be. A selection policy that reads
only the observable pattern is choosing under an [[efe-planning-as-variational-inference|ambiguity]] it cannot see
from its own state.

## Limits

The finding rests on one deployed agent (ReflectiMate, a reflection
support tool for personal decisions) and one population (62 Prolific
workers, English-fluent, recruited for an active life decision); the
taxonomy's inter-rater agreement between the human coder and four local
LLM coders was only moderate (κ 0.42–0.58), so the exact category
boundaries are softer than the headline percentages suggest. Whether the
same degree of interpretive diversity holds for axis-selection in
non-reflective, task-oriented dialog is untested here.

## Related
[[clarification-request]] · [[collaborative-reflection-pause]] · [[expected-information-gain]] · [[value-of-information]]

[^c1]: tarvirdians-2026 — "what we term the interpretive gap, remains unstudied."
[^c2]: tarvirdians-2026 — "derive a taxonomy of nine interpretation categories"
[^c3]: tarvirdians-2026 — "contained 19 moments spanning 8 of"
[^c4]: tarvirdians-2026 — "n=64 (27.6%)"
[^c5]: tarvirdians-2026
