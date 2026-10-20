---
description: "A seven-class pre-action decision space (execute, refuse, clarify, confirm, defer, escalate, decline) benchmarked on 202 LLM scenarios; structured rules beat schema-only prompting on alignment."
aliases: ["seven-class authorization taxonomy", "pre-action authorization decision"]
sources: ["afroze-2026"]
---
# Pre-action authorization decision

> Before an agent acts on a request, "ask a clarifying question" is one of
> several distinct moves competing with executing, refusing, confirming,
> deferring, or escalating — not the complement of a binary act/refuse
> choice.

## Definition / Mechanism

Afroze, Zhang, Tu & Hei (2026) model an LLM mediating
vehicle voice commands as a decision layer that must choose one of seven
classes before any tool call: "Before executing a command, the system must
choose whether to execute, refuse, clarify, require confirmation, defer to
manual control, trigger an emergency response, or make no tool call."[^c1]

They benchmark five LLMs (two open-weight, three API-based) on 202
hand-authored scenarios (command × speaker role × authentication status ×
vehicle state × tool availability) against a Reference Decision, scoring
**Decision Alignment** (exact match to the reference) plus class-specific
error rates (False Execute, Over-refusal, Clarification Miss, Emergency
Miss). "Decision Alignment ranges from 40.1% for Llama 3.2 3B to 89.1% for
Gemini 3.1 Pro Preview... Even these models produce two to three False
Executes among 161 non-execution scenarios, and persistent errors remain in
confirmation and manual-control decisions."[^c2]

A controlled ablation on Llama 3.2 3B isolates the effect of giving the
decision layer explicit, context-dependent rules (the "structured
authorization policy") versus a schema-only interface or generic safety
guidance, holding the seven-class vocabulary fixed: "the structured
authorization condition achieves 40.1% alignment, improving on schema only
by 10.9 points and generic safety guidance by 11.9 points... Under the
structured policy, False Executes increase to 6 of 161 non-EXECUTE
scenarios, compared with three under schema only and none under generic
safety guidance."[^c3]

Their own reading of the trade-off: "Structured LLM decisions are therefore
insufficient as a standalone safety mechanism, and deployment requires an
independent enforcement layer that verifies tool permissions and
vehicle-state constraints before invoking any vehicle function."[^c4]

## Known as

| Name | Field | Relation |
|---|---|---|
| seven-class authorization taxonomy | LLM agent safety benchmarking | exact — the paper's own name |
| pre-action authorization decision | this wiki | exact — the generalized name used here |

## Why it matters

The wiki's ask/act framing (e.g. [[value-of-information]]'s EIG > 0 / VoI =
0 split) treats asking as the alternative to acting. This benchmark shows
that on the answerer's side the choice is not binary even before comprehension
is at issue: clarify, confirm, defer to a human, and escalate are four
separate moves with different triggers ([[efe-planning-as-variational-inference|ambiguity]], [[reversibility]] risk,
capability, urgency), and a model that collapses them into refuse-or-execute
loses exactly the distinctions [[recognition-refusal-dissociation]] shows
matter — refusing conservatively (Llama 3.2 3B's 41.5% over-refusal) is a
different failure from executing wrongly (Llama 3.1 8B's 13.7% False
Execute), and neither is fixed by better prompting alone.

## Transfer

| | |
|---|---|
| **Home field** | LLM agent safety benchmarking for vehicle voice assistants |
| **Here** | any answerer deciding, before committing to an action, among executing, refusing, asking a clarifying question, requesting confirmation, deferring to a human, or escalating |
| **What survives** | the refusal of a binary act/refuse (or ask/act) partition — clarify and confirm are separated by *why* the agent is not yet ready to commit (missing information vs. unresolved risk), not merged into one hedge |
| **What does not** | the vehicle-specific classes (manual control, emergency response) and the reliance on a hand-authored Reference Decision as ground truth — most asking domains have no such external policy to benchmark against |

## Limits

- All results are on one narrow domain (vehicle voice commands) with small
  per-class counts (16–57 scenarios); the policy ablation runs on a single
  3B model, so whether structured rules transfer this benefit to larger
  models is untested.
- The Reference Decisions are assigned by the paper's own authors using
  their own structured policy, so "alignment" measures agreement with a
  hand-built rule set, not an independently validated notion of correctness.
- The seven classes were fixed by construction; the paper does not test
  whether a different partition (e.g. splitting confirmation by risk type)
  would separate failure modes better.
- The claim that clarify/confirm/defer are functionally distinct rests on
  this wiki's reading of the per-class breakdown, not a claim the authors
  make about question-asking generally — their subject is authorization,
  not asking.

## Related

[[clarification-request]] · [[value-of-information]] · [[recognition-refusal-dissociation]] · [[abstention]]

[^c1]: afroze-2026 — "Before executing a command, the system must choose whether to execute, refuse, clarify, require confirmation, defer to manual control, trigger an emergency response, or make no tool call."
[^c2]: afroze-2026
[^c3]: afroze-2026
[^c4]: afroze-2026 — "Structured LLM decisions are therefore insufficient as a standalone safety mechanism, and deployment requires an independent enforcement layer that verifies tool permissions and vehicle-state constraints before invoking any vehicle function."
