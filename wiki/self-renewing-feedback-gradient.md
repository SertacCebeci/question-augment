---
description: "Multi-turn follow-up questioning used as a feedback generator keeps producing new revision gradient across rounds where single-turn QA feedback saturates after one round."
aliases: ["self-renewing evolution gradient", "layered defect exposure", "multi-turn feedback generator"]
sources: ["yan-2026"]
---
# Self-renewing feedback gradient

> Whether an iterative improvement loop keeps improving depends on whether
> its feedback keeps exposing new defects — and a single question-answer
> exchange exposes only what that one exchange can reveal.

## Definition / Mechanism

Yan et al. (2026) evolve an LLM agent's "Skill" (a knowledge
document) over repeated rounds, each round driven by a simulated user
interacting with the agent and a feedback signal extracted from that
interaction. When the feedback comes from a single question-answer
exchange, only the gaps visible in the user's opening statement can be
patched: once those are fixed, the gradient decays. Measured on their
production benchmark, single-turn-QA-driven evolution raises task success
rate (TSR) from 58.9% (round 1) to no more than 66.4% (round 4) with
sharply diminishing marginal gains, because "a single question–answer pair
reaches only the gaps present in the user's opening statement; once those
are patched the gradient decays."[^c1]

Recasting the *same* multi-turn user simulation from an evaluation endpoint
into a feedback generator changes this: follow-up questions and
clarification expose defects layer by layer, so that "knowledge patched in
the current round lets the dialogue proceed further and reach the next
layer of defects, previously masked by shallower failures. Each round of
revision therefore not only consumes gradients but generates new ones, and
TSR rises steadily from 59.4 to 81.8."[^c2]

A no-evaluation baseline (blind self-reflection, no feedback signal at all)
shows the gradient is not free: "Self-Reflection possesses no gradient in
the absence of evaluation, so multi-round blind editing merely oscillates
around its first-round level."[^c3]

## Why it matters

The three conditions (no feedback, single-turn feedback, multi-turn
follow-up feedback) isolate one variable — the source of the feedback
signal — while holding the editor, the attribution step and the governance
step fixed. The difference is not "more iterations" or "a better editor";
it is whether the *next* round's question can still find something the
previous round could not see. For an asking system, this is a measured
answer to when repeated questioning keeps paying off across separate
episodes of interaction (not just within one dialogue): only when the
questioning method itself changes what becomes visible each round.

## Limits

- Single production benchmark (Tencent Cloud technical support, 9 Skills,
  98 reference files, 4 rounds); the round count at which single-turn QA
  saturates and the magnitude of the multi-turn gain are not shown to hold
  outside this domain or this editor.
- The "user" that supplies follow-up questions is itself a constrained
  LLM simulation reconstructed from real tickets, not a live human;
  whether real users expose the same layered structure of defects is
  untested here.
- TSR is judged by an automatic Verifier; the paper reports ≈90% agreement
  with human labels on a sampled subset, not full human verification of
  every round.
- The comparison holds attribution and governance fixed and varies only
  the feedback source (§4.1.2); it does not isolate how much of the
  81.8% ceiling is attributable to the multi-turn signal alone versus its
  interaction with the paper's attribution/governance machinery (see
  [[repairability-attribution]]).

## Related

[[multi-turn-clarification-plateau]] · [[on-demand-follow-up-generation]] · [[clarification-benchmarks]] · [[repairability-attribution]]

[^c1]: yan-2026
[^c2]: yan-2026 — "Follow-up questions and clarification expose defects layer by layer: knowledge patched in the current round lets the dialogue proceed further and reach the next layer of defects, previously masked by shallower failures. Each round of revision therefore not only consumes gradients but generates new ones, and TSR rises steadily from 59.4 to 81.8."
[^c3]: yan-2026 — "Self-Reflection possesses no gradient in the absence of evaluation, so multi-round blind editing merely oscillates around its first-round level."
