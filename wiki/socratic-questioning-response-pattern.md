---
description: "An AI's Socratic-Questioning response pattern raised time-on-task but produced no significant accuracy gain, and was the least-liked question-asking style in a controlled study."
aliases: ["Socratic Questioning rhetorical pattern", "Socratic Questioning response pattern"]
sources: ["sabouri-2026"]
---
# Socratic Questioning response pattern

> An AI advisory system that answers a fact-check request with a single
> probing question about missing evidence, instead of information, does not
> thereby make its user more accurate — it makes them slower and less
> satisfied.

## Definition / Mechanism

Sabouri et al. (2026) operationalise **[[staged-socratic-hint-policy|Socratic]] Questioning** as one of
eight response rhetorics an AI advisor can use when a user requests help
verifying a claim: instead of supplying missing evidence, the system asks a
single probing question about the gap (e.g., for the claim "Phil Knight
created ASICS," the system asks "How are Nike and ASICS connected?") rather
than stating the connection.[^c1]

In a within-subject online study (n = 98, hint-on-demand fact verification,
40 claims), this pattern was the only one of the eight whose before/after
accuracy change was not significant: "Socratic Questioning yielded no
improvement at all (p = 0.57)."[^c2]

It was also the only pattern that significantly slowed participants
relative to the direct-answer baseline: "only Socratic Questioning was
significantly slower (+18.3s, p < 0.001)."[^c3]

Participants also changed their initial answer least often after seeing it
(62.8%, against a 71.5% average across the eight patterns), and it ranked
among the least preferred, worse liked than the study's direct-answer
baseline: "Participants especially disliked patterns who asked questions
like Socratic Questioning."[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Ancient philosophy (elenchus) | Socratic method | not this concept — see [[socratic-method]]: refutative, no accuracy outcome is measured |
| CBT / education | Socratic questioning, guided discovery | not this concept — constructive guided discovery toward a new belief, not an AI-response rhetoric with a measured accuracy/time/preference outcome |
| This paper (HCI) | Socratic Questioning (rhetorical pattern) | exact |

## Transfer

| | |
|---|---|
| **Home field** | Philosophy / CBT: probing questions about missing premises or evidence are assumed to induce reflection ([[socratic-method]]). |
| **Here** | A single scripted probing question inserted into an AI's advisory response, in place of the missing information itself. |
| **What survives** | The mechanism — naming a gap in the evidence as a question rather than as a stated fact — and the behavioural signature: users spend measurably longer engaged with it than with a direct answer. |
| **What does not** | The assumption that probing improves the outcome: no significant accuracy gain, and it was the pattern users named as most disliked among the question-asking styles; there is no multi-turn dialogue or interlocutor-elicited premise chain, only one question per claim. |

## Why it matters

The study's own baseline for comparison, Oracle (a direct, confident
answer), produced one of the largest measured accuracy gains and, unlike
Socratic Questioning, did not slow users down — a direct empirical case
where a directive answer outperforms a probing question on the outcome a
practitioner would optimise for (correctness), while costing the user less
time.

## Limits

- One study, one task domain (fact verification with hint-on-demand), one
  operationalisation of Socratic Questioning as a single scripted probing
  question — not a multi-turn dialogue; the paper itself flags its
  accuracy deltas as "directional signals rather than stable effect
  sizes." [?]
- n = 98, within-subject; the null accuracy result (p = 0.57) is a failure
  to reject, not evidence that probing questions never help — the same
  study finds other, non-question patterns (e.g. Scaffold Explanation) do
  produce significant gains under the same design.
- The claim's evidence is a single question per claim; whether a
  different or longer chain of probing questions changes the result is
  not tested here.

## Related

[[socratic-method]] · [[information-gathering-interview-style]] · [[value-of-information]]

[^c1]: sabouri-2026 — "Socratic Questioning: This pattern encourages deep reflection and self-examination through probing questions about missing information or assumptions, leading individuals to reconsider their beliefs."
[^c2]: sabouri-2026 — "Socratic Questioning yielded no improvement at all (p = 0.57)."
[^c3]: sabouri-2026 — "only Socratic Questioning was significantly slower (+18.3s, p < 0.001)."
[^c4]: sabouri-2026 — "Participants especially disliked patterns who asked questions like Socratic Questioning"
