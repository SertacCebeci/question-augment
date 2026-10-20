---
description: "KITE classifies each tutoring query into one of five pedagogical intents and routes it to a matched response strategy, rather than one fixed strategy for every query."
aliases: []
sources: ["jain-2026", "arxiv-2511-18405"]
---
# Intent-aware response strategy

> Before deciding what to say, decide what kind of question it is: KITE
> classifies a student's query into one of five pedagogical intents and
> only then picks the response strategy — direct explanation, a follow-up
> question, [[staged-socratic-hint-policy|Socratic]] guiding questions, a hint progression, or a stepwise
> trace — that matches it.

## Definition / Mechanism

Jain et al. (2026) build KITE, a retrieval-augmented tutoring
system for algorithm courses. Rather than a single response behaviour for
every student message, KITE first runs intent classification and only then
generates a response: "KITE does not use a single response strategy for
all student questions. Instead, it first classifies each query by
pedagogical intent and then generates a response that matches the
instructional purpose of the interaction."[^c1]

The classifier is a fixed, hand-built taxonomy, not a learned model:
"Each incoming query is classified into one of five pedagogical intents
using a keyword and pattern-matching classifier" — Direct Question,
Conceptual Questions, Algorithm Validation, Debugging, and Algorithm
Tracing.[^c2]

Each intent is bound to a distinct strategy at generation time: direct and
conceptual questions get retrieval-grounded explanations (conceptual ones
adding a follow-up question); algorithm validation gets "a Socratic
assessment strategy instead of directly identifying errors... a brief
evaluation of the student's approach, acknowledgement of correct
components, and guiding questions that target specific issues"; debugging
gets "diagnostic prompts that guide students toward identifying errors
through self-examination" in "a structured hint progression"; and
algorithm tracing gets a step-by-step replay of the procedure on the
student's own problem instance, maintaining state variables like OPEN and
CLOSED lists.[^c3]

## Findings

Using a weaker LLM (Meta-Llama-3.1-70B-Instruct) as a simulated student
that answers unaided, receives KITE's intent-routed feedback, then
revises: "among the 27 simulated-student interactions with KITE, in which
the initial student response was not already correct, experts judged 24
revised answers (88.89%) as improved after receiving KITE's feedback."[^c4]

Independent of whether the revision moved to fully correct, experts rated
the feedback itself highly on process quality: "Experts rated 93.18% of
KITE's feedback positively for scaffolding and guidance, further
indicating that the feedback was instructionally purposeful and
well-structured."[^c5]

## Why it matters

This is a positive companion to [[state-gated-strategy-routing]]'s negative
result on the same stall: both papers build a tutor that first estimates
something about the query/learner and then selects among a fixed menu of
response strategies rather than answering directly every time. Here the
routing key is the query's own pedagogical intent (five hand-labelled
categories) rather than an estimated learner state, and the measured
outcome is aggregate answer improvement across all four procedural/tracing
intents combined, not an ablation against a single fixed strategy — so,
unlike `state-gated-strategy-routing`, this source cannot say whether the
per-intent routing itself, as opposed to any one of its four strategies
applied uniformly, is what produced the improvement.

The same choice, made once per turn, appears outside tutoring. Talk2Data (Al Awad et al., 2025) decides each data-analysis turn between generating code and a speakable narration. For an ambiguous request its prompt "favors a low-risk chat response and invites follow-up."[^c6] The failures of that fork split by where they arise. A small 1.5B model "often sought clarification or proposed how to proceed instead of producing code", which the paper counts as "routing mistakes (17)".[^c7] The 7B model's two failures were "one intentional policy block by the runtime and one decision error at the routing step".[^c8] Because the mode is fixed before execution, a failed turn can be assigned to the fork or to the sandbox rather than to the generated code. This reading of where the errors fall is mine; the text read reports no run with the routing step removed, so it does not show that routing raises accuracy.

## Limits

- The 88.89% improvement figure aggregates all procedural and tracing
  intents together; the paper does not report accuracy separately by which
  of the four non-direct strategies (Socratic assessment, debugging hints,
  tracing walkthrough) a given interaction received, so this note cannot
  claim that guiding questions specifically outperform hints or scaffolds.
- The intent classifier's own accuracy is not evaluated — no confusion
  matrix or precision/recall is reported for the five-way keyword/pattern
  classification, only downstream feedback quality.
- The "student" is a single proxy LLM (Meta-Llama-3.1-70B-Instruct), not a
  real learner; the authors themselves restrict the improvement claim to
  "a stronger answer more recoverable," not evidence of genuine learning.
- n = 44 simulated interactions, three expert raters (κ = 0.88); no
  comparison condition against a single fixed strategy applied to every
  intent, so no causal claim that intent-routing beats not routing.
- `jain-2026` is unverified `[?]` in this wiki pending the verifier.

[^c6]: arxiv-2511-18405 — "When the request is ambiguous, the prompt favors a low-risk chat response and invites follow-up."
[^c7]: arxiv-2511-18405 — "often sought clarification or proposed how to proceed instead of producing code"
[^c8]: arxiv-2511-18405 — "These two failures reflect distinct modes: one intentional policy block by the runtime and one decision error at the routing step."

## Related

[[state-gated-strategy-routing]] · [[staged-socratic-hint-policy]] · [[gated-socratic-scaffolding]] · [[socratic-questioning-response-pattern]] · [[value-of-information]]

[^c1]: jain-2026 — "KITE does not use a single response strategy for all student questions. Instead, it first classifies each query by pedagogical intent and then generates a response that matches the instructional purpose of the interaction."
[^c2]: jain-2026 — "Each incoming query is classified into one of five pedagogical intents using a keyword and pattern-matching classifier"
[^c3]: jain-2026 — "For algorithm validation tasks, KITE adopts a Socratic assessment strategy instead of directly identifying errors. Responses include a brief evaluation of the student’s approach, acknowledgement of correct components, and guiding questions that target specific issues."
[^c4]: jain-2026 — "among the 27 simulated-student interactions with KITE, in which the initial student response was not already correct, experts judged 24 revised answers (88.89%) as improved after receiving KITE’s feedback."
[^c5]: jain-2026 — "Experts rated 93.18% of KITE’s feedback positively for scaffolding and guidance, further indicating that the feedback was instructionally purposeful and well-structured."
