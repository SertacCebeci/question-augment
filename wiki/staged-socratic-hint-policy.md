---
description: "A tutor withholds a full answer and instead escalates through three fixed hint stages — reorientation, procedural hint, partial worked example — advancing only when the learner stalls."
aliases: ["three-stage Socratic hint policy", "Socratic hint policy", "Socratic", "scaffolded hint policy"]
sources: ["ferrara-2026"]
---
# Staged Socratic hint policy

> Instead of choosing between "answer" and "no answer," fix an ordered
> ladder of increasingly specific hints and climb one rung only when the
> learner is stuck at the current one.

## Definition / Mechanism

Ferrara & Sami (2026) build SYNAPSE, a multi-LLM tutoring
platform for secure software development, and constrain every tutor
response under one rule enforced at the orchestration layer, not inside any
single model: all tutor responses are constrained by a uniform Socratic hint
policy enforced at the MCP coordinator rather than within any single model.
The policy organises guidance into three progressively more specific
stages: (i) conceptual reorientation, which redirects the learner to the
underlying idea without naming the solution; (ii) procedural hint,
suggesting an approach or structural direction; and (iii) partial worked
example transferred from a different context, requiring the learner to
adapt the pattern.[^c1]

The stage advances only on evidence the learner is stuck, not on a fixed
turn count: in the paper's traced example the tutor responds under the
three-stage Socratic hint policy: first a conceptual reorientation towards
what the application does with the supplied filename, then, when the
learner stalls, a procedural hint on how user input might reach the file
system.[^c2]

The top stage is capped below a full solution: the policy explicitly
prohibits the generation of complete exploit code in ShopSecure
interactions.[^c3]

The design cites prior HCI evidence for graduated release over direct
answers rather than establishing it itself: a design supported by
Kazemitabaar et al. [8], who observed learner dissatisfaction with AI
systems that returned direct answers instead of graduated guidance.[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| software-engineering education (this paper, abstract/contributions) | three-stage Socratic hint policy | `exact` |
| software-engineering education (this paper, §III-B) | Socratic hint policy | `exact` |
| software-engineering education (this paper, introduction) | Socratic, scaffolded hint policy | `exact` |

## Why it matters

This is a selection rule for *how much of an answer to reveal per turn*
rather than for which axis to question next: a fixed, ordered ladder of
specificity with an explicit ceiling (never the full answer) and an
advance condition (visible stall), applied uniformly across three different
underlying LLM providers so the ceiling holds regardless of which model
composed the response.

## Limits

- The claim rests on one worked usage trace in the paper (the CWE-22
  path-traversal exercise), not a controlled measurement of the policy
  itself: the pilot's SUS (76.4) and engagement (4.2/5) scores are reported
  for the whole platform — multi-LLM routing, accessibility layer,
  ShopSecure — and are not isolated to the hint policy, so this note makes
  no effect claim for the staged escalation on its own.
- "When the learner stalls" is illustrated by one traced example, not
  specified as a measurable trigger (e.g. a turn count or an evaluator
  agent's judgement, as in [[gated-socratic-scaffolding]]); how the stage
  boundary is detected in general is not stated in the slices read here.
- n = 19 pilot completers, unincentivised convenience sample, no control
  condition; the authors call the pilot feasibility evidence, not a test of
  this policy against an alternative.
- `ferrara-2026` is unverified `[?]` in this wiki pending the verifier.

## Related

[[gated-socratic-scaffolding]] · [[tree-of-thought-socratic-teaching]] · [[socratic-method]] · [[non-advisory-dialogue]]

[^c1]: ferrara-2026
[^c2]: ferrara-2026 — "the tutor responds under the three-stage Socratic hint policy: first a conceptual reorientation towards what the application does with the supplied filename, then, when the learner stalls, a procedural hint on how user input might reach the file system."
[^c3]: ferrara-2026 — "The policy explicitly prohibits the generation of complete exploit code in ShopSecure interactions."
[^c4]: ferrara-2026 — "a design supported by Kazemitabaar et al. [8], who observed learner dissatisfaction with AI systems that returned direct answers instead of graduated guidance."
