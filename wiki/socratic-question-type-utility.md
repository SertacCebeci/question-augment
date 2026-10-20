---
description: "An ablation on one multi-agent optical-discovery system finds causal-probing and counterexample questions raise hypothesis quality far more than clarification or constraint-checking."
aliases: ["Socratic question-type utility ranking"]
sources: ["zeng-2026"]
---
# Socratic question-type utility ranking

> Four classes of question, scored against the same hypothesis-revision task,
> do not carry equal value — and a question-only critic beats a
> correction-giving one on the same task.

## Measurement

In AHOIS (a five-agent system interrogating hypotheses about a real
multimode-fibre optical platform), a hypothesis agent's account was scored
on three axes — physics consistency, hypothesis completeness, uncertainty
[[calibration]] — before and after each of four classes of question. "Clarification
produced a mean utility of 0.42 by removing ambiguous terminology and
forcing Boxue to state what was measured, inferred or assumed. Constraint
checking produced a larger gain of 0.58 by excluding explanations that
conflicted with optical principles or hardware constraints. Causal probing
produced the largest improvement, 0.83, because it forced the agent to
connect individual observations to a complete physical pathway rather than
rely on qualitative association. Counterexample challenge also produced a
strong gain of 0.74" Zeng et al. (2026).[^c1]

All three scores rose over repeated rounds of questioning rather than after
a single pass: "All three scores increased over seven rounds of [[staged-socratic-hint-policy|Socratic]]
questioning (Fig. 5b). Physics consistency rose from approximately 2 to
above 4.5 on the 0–5 scale, while hypothesis completeness and uncertainty
calibration showed similar monotonic improvements."[^c2]

A separate four-way ablation — the hypothesis agent alone, paired with a
generic reviewer, paired with a critic that gives direct corrections, and
paired with the question-only critic — found the question-only condition
best on every downstream metric measured: "The Socratic configuration
achieved the highest normalized physics consistency, plan validity,
planning efficiency and final task performance (Fig. 5d). It also produced
the lowest invalid-plan rate and required fewer steps to reach a valid
plan."[^c3]

## Why it matters

This is a measured ordering of question types by value on a single fixed
task, not a general claim about question types in the abstract: causal and
counterexample questions here outscore clarification and constraint
questions by roughly 2x. It is a concrete answer to "which axis first"
inside a critique loop — spend the interrogation budget on causal-chain and
generalisation questions before terminology or local-constraint questions —
but the ranking was produced under one scoring rubric, one task, one model
family, and is not shown to hold outside it.

## Limits

- One paper, one task family (physical hypothesis revision on a multimode-
  fibre platform), one scoring rubric defined by the same paper — `zeng-2026`
  `[?]` until the verifier confirms; no independent replication or held-out
  domain is cited for the ranking or for the four-way ablation.
- The utility scores (0.42, 0.58, 0.74, 0.83) are LLM- or rubric-judged
  deltas in an internal "understanding score," not an external ground-truth
  measure of hypothesis correctness; the paper does not report inter-rater
  or inter-run reliability for these numbers.
- The four question classes were applied in a fixed protocol (all four,
  every round); the ablation does not test whether the ranking would hold if
  a single class were used alone from the start, so the finding supports a
  relative priority inside the existing protocol, not a proof that dropping
  clarification and constraint-checking would keep the same gains.

## Related

[[socratic-physics-critic]] · [[socratic-method]]

[^c1]: zeng-2026 — "Clarification produced a mean utility of 0.42 by removing ambiguous terminology and forcing Boxue to state what was measured, inferred or assumed. Constraint checking produced a larger gain of 0.58 by excluding explanations that conflicted with optical principles or hardware constraints. Causal probing produced the largest improvement, 0.83, because it forced the agent to connect individual observations to a complete physical pathway rather than rely on qualitative association. Counterexample challenge also produced a strong gain of 0.74"
[^c2]: zeng-2026 — "All three scores increased over seven rounds of Socratic questioning (Fig. 5b). Physics consistency rose from approximately 2 to above 4.5 on the 0–5 scale, while hypothesis completeness and uncertainty calibration showed similar monotonic improvements."
[^c3]: zeng-2026
