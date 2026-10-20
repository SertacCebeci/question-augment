---
description: "A non-LLM policy core sets a per-turn ceiling on an eight-rung help ladder from trusted state alone; a detector and an LLM judge enforce it outside the answering model."
aliases: ["supervisor architecture", "eight-rung help ladder", "hint ladder", "per-turn withholding contract"]
sources: ["pisan-2026"]
---
# Answer-withholding supervisor architecture

> Withholding is not asked of the answering model; it is computed by
> components the model cannot see or talk past, then checked against the
> model's own output before the student ever reads it.

## Definition / Mechanism

Pisan (2026) reports a deployed LLM tutor built around a
supervisor layer that surrounds a single "actor" model the student talks
to. A non-LLM policy core, fed only trusted learner state and never the
student's own words, computes a per-turn contract: a ceiling on an
eight-rung help ladder (H0 acknowledge, through H7 full compilable
solution), which goals are in scope, whether the turn must be grounded in
retrieved material, and whether a risky reply needs extra judging. A
non-LLM policy core, reading only trusted learner state, sets a per-turn
ceiling on an eight-rung help ladder; a deterministic detector strips
solution code; and a separate LLM judge checks each risky reply against the
contract.[^c1]

The ceiling is set from named factors, not prose: lower mastery raises the
ceiling and higher mastery lowers it to force productive struggle, with the
most permissive of several in-scope goals winning; a student showing buggy
code floors the ceiling at H4 (a verbal nudge, no code) because they are
stuck on execution rather than concept; an active mastery exam caps the
ceiling near zero; conduct restrictions apply last so nothing can lift
them.[^c2]

Enforcement is layered and ordered by trust, not by model confidence: a
deterministic code-reveal detector removes solution code independently of
any model judgment, running in a strict mode that strips even a bare
function signature when the contract allows no code at all; only then does
a separate LLM judge check a risky draft against the contract, seeing only
the contract, the draft and the retrieved sources — never the raw student
message — which the paper calls collusion-resistant by construction,
because a judge that shares the student's channel could be talked into
excusing a leak the same prompt produced.[^c3]

## Why it matters

This gives the wiki's selection stall a concrete instance of an *ordered,
typed* answer space (the eight rungs) whose next-step decision is made by a
component structurally separated from the thing being asked — the
opposite of a prompt asking one model to be simultaneously warm, [[staged-socratic-hint-policy|Socratic]]
and non-revealing. The ceiling computation is itself a selection rule: it
chooses how far up the ladder the next turn may go from state the student
cannot edit, before any question is asked.

## Transfer

| | |
|---|---|
| **Home field** | LLM safety's refusal-of-content pattern, and access-control's separation of a decision plane from the thing it constrains (least-privilege, trust boundaries). |
| **Here** | The decision of *how much to reveal this turn* is computed by code with no model call and no access to the student's text, then handed to the answering model as an instruction it cannot renegotiate from within the conversation. |
| **What survives** | The trust-boundary argument: a component that never reads untrusted input cannot be talked past by anything said to it — the paper reports the ceiling held against a scripted social-engineering persona and a scripted injection persona in its offline simulation. |
| **What does not** | Classical refusal targets content the model should not produce at all; here the model already knows the answer and the student can see that it knows, so the reachable-but-blocked case is not covered by ordinary safety-refusal training or evaluation. |

[^c4]

## Limits

- Reported on one deployed system (two undergraduate data-structures
  courses, C++), evaluated by scripted personas and an LLM auditor, not by
  a controlled study of student outcomes; the paper explicitly declines to
  claim a learning-outcomes result and names the delayed, tool-removed
  assessment as future work.[^c5]
- The architecture's compliance numbers (G1-G4) are measured against the
  system's own judge and a stronger auditing model, not against human
  raters; the paper documents three classes of reveal (split-fence,
  plain-prose, cross-language) known by design to be missed by the
  deterministic detector.
- `pisan-2026` is an unreviewed arXiv preprint (harvested 2026-09-18) —
  `[?]` pending verifier confirmation.

## Related

[[gated-socratic-scaffolding]] · [[non-advisory-dialogue]] · [[socratic-method]] · [[answer-withholding-learning-tradeoff]]

[^c1]: pisan-2026 — "A non-LLM policy core, reading only trusted learner state, sets a per-turn ceiling on an eight-rung help ladder; a deterministic detector strips solution code; and a separate LLM judge checks each risky reply against the contract."
[^c2]: pisan-2026 — "Mastery band: lower mastery raises the ceiling (more scaffolding), higher mastery lowers it to force the productive struggle that drives durable learning"
[^c3]: pisan-2026
[^c4]: pisan-2026 — "a student cannot talk past a ceiling computed from data they cannot edit"
[^c5]: pisan-2026 — "We deliberately do not claim a learning-outcomes result; the decisive test, a delayed, tool-removed assessment in a controlled"
