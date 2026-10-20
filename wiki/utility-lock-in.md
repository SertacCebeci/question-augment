---
description: "A model's multi-turn response can still fall short of its own single-turn oracle utility after the user states their benign intent, evidence the model never revised its read of that intent."
aliases: ["utility lock-in"]
sources: ["arxiv-2604-27093"]
---
# Utility lock-in

> A model already told the truth can still answer as if it had not been
> told.

## Definition / Mechanism

Zheng, Morgan, Jiang, Rosé & Sap (2026) build
C ARRY O N B ENCH: 398 queries that look harmful but carry a benign
underlying intent, extended into 5,970 simulated conversations across
14 models. Each response is scored against B EN -U TIL, a checklist of
atomic yes/no information needs derived from an **oracle** response —
the same query given the benign intent *upfront*, in a single turn.
Turn-1 utility (10.5–37.6% of the checklist) is far below the oracle's
(25.1–72.1%), and the gap does not track knowledge: it closes once the
model is simply told the intent it was missing, "confirming that models
withhold information due to intent misinterpretation, not limited
knowledge."[^c1]

The benchmark then lets the user supply that missing intent *inside* the
conversation — a **benign clarification** (BC) turn — and re-measures the
gap. Most models close most of it: 13 of 14 approach or exceed the
Turn-1 oracle once BC is given. **Utility lock-in** is the residual: "a
model that fails to close the gap between initial response and its own
oracle even under benign clarifications." DeepSeek-V3.1 is the clearest
case — one of the strongest Turn-1 performers, yet the only model of the
14 that still falls short of its own oracle (67.6%) after BC (66.3%),
"suggesting that it rarely updates assessments of user intent."[^c2]

Lock-in is conditioned on where the model started, not on how much intent
it is given. Hard-refusal conversations (0% Turn-1 utility) recover the
most utility of any starting bin, but only with BC — without it they stay
at floor regardless of turn count. The paper states the asymmetry
directly: hard refusals "remain locked without clarification," while
explicit benign clarification "breaks utility lock-in at uniform safety
cost" across starting bins.[^c3]

Lock-in is a comprehension failure, not a safety one: safety scores move
together across starting bins regardless of lock-in, so a model can hold
a stable, calibrated safety read while never updating its intent read at
all. The paper separately names two ways a model that does *not* lock in
can still fail — **unsafe recovery** (it revises and answers, at a
disproportionate rise in harmfulness) and **redundant recovery** (it
appears to revise, but the new items were already satisfied earlier) —
both presuppose the intent read changed; lock-in is what happens when it
does not change at all.

## Why it matters

Single-turn refusal benchmarks cannot see lock-in: they score one
response with no oracle to compare against, so a model that never
updates its read of intent looks identical to one asked a harder
question. Lock-in requires the three-way comparison this benchmark makes
structural — Turn 1, oracle, BC — and shows that a model's comprehension
of a clarification is a distinct, separately-measurable quantity from
whether its eventual answer is safe or informative.

## Limits

- Measured on 14 chat models over one benchmark's query and
  clarification distribution (`CarryOnBench`); whether lock-in appears
  with less-explicit clarifications, or on tasks without a
  harm-adjacent Turn-1 refusal to unlock, is unverified here.
- The oracle is a single-turn upper bound, not a ground-truth ceiling;
  a model scoring at its oracle is shown to match its own single-turn
  self, not to have understood the intent correctly.
- BEN-UTIL checklists are LLM-generated and LLM-graded (with a
  self-bias caveat the authors flag for models used in construction),
  so the judgment inherits that evaluator's own reading, one layer
  removed from the comprehension claim itself.

## Related

- [[interpretation-space]] — both measure an answerer's read of intent
  against a reference set, one by coverage of enumerated readings, one
  by an oracle response's checklist.
- [[clarification-request]] — the BC turn is a user-supplied answer to
  the clarification a well-calibrated model would ask for; lock-in is
  what happens when the answer is given but not used.
- [[false-premise-question]] — both track whether an answerer's read of
  a query is corrected by information available to it, rather than
  merely producing a different surface response.
- [[levels-of-information-need]] — the oracle-vs-Turn-1 gap is a
  benign-intent analogue of the asker's expressed need diverging from
  the need actually being served.

[^c1]: arxiv-2604-27093 — "confirming that models withhold information due to intent misinterpretation, not limited knowledge"
[^c2]: arxiv-2604-27093 — "We first note utility lock-in: a model that fails to close the gap between initial response and its own oracle even under benign clarifications"
[^c3]: arxiv-2604-27093 — "remain locked without clarification"
