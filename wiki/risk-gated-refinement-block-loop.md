---
description: "A bounded refinement loop that regenerates a response against two independent risk scores until both clear a release threshold, then blocks and substitutes a refusal fallback if they do not."
aliases: ["CareGuardAI decision layer", "SRA/HRA threshold gating", "release-refine-block"]
sources: ["arxiv-2604-26959"]
---
# Risk-gated refinement-then-block loop

> Commitment is not a single yes/no on an answer; it is a bounded number of tries to earn one.

## Definition / Mechanism

Two independent evaluator agents score a candidate response after it is
generated: a Safety Risk Assessment (SRA) on a five-level clinical-harm
scale, and a Hallucination Risk Assessment (HRA) on a five-level scale
decomposing errors into data-driven and reasoning-driven hallucinations,
with HRA taken as their **maximum**, not their average — a single bad
axis is enough to fail the response Nasarian et al. (2026).
A response is released only when both scores clear a fixed threshold at
once (SRA ≤ 2 **and** HRA ≤ 2); the two axes are conjunctive, so
confidence on one dimension never substitutes for the other.[^c1]

When either score fails the threshold (SRA ≥ 3 or HRA ≥ 3), the system
does not simply abstain: it feeds each evaluator's structured
diagnosis — which violation, which hallucination type — back into the
generator as a stricter, targeted prompt and regenerates, for up to
**three iterations**. Only if the response is still unsafe after all
three does the loop give up, blocking the output and substituting a
fixed refusal-style fallback (e.g., referral to a clinician) in its
place.[^c2]

The loop is bounded on both ends: it never commits an answer that has
not cleared both thresholds, and it never retries indefinitely — a
fixed retry budget stands in for a stopping rule.[^c3]

## Why it matters

The two evaluators can fail independently: a response can be clinically
safe yet still contain a minor factual error, or hallucination-free yet
still overstep on safety. Reported ablations show removing individual
components drops the deployable-response rate to as low as 39%.[^c4]
Separately, the full system's refinement loop converges in about one
iteration per query on almost all cases that needed refinement at all —
so most of the loop's value is realized on the first retry, with the
three-iteration bound rarely binding.[^c5]

This gives a third register for commitment, beyond "answer" or
"abstain immediately": *retry against an explicit, decomposed
diagnosis of why the last attempt failed, within a fixed budget, then
fall back to a stock refusal.* The diagnosis — not just the failing
score — is what makes the retries converge rather than repeat the same
mistake.

## Limits

Both evaluator agents are themselves quantized LLMs scored against
fixed rubrics (ISO 14971 for SRA, a hallucination taxonomy for HRA);
the release decision is only as reliable as these judges, which the
paper does not independently validate against clinician ground truth
for every case. The three-iteration bound and the ≤2 thresholds are
fixed hyperparameters, not derived from a cost model of over- vs.
under-refinement (contrast [[cost-controlled-abstention]], which derives
its threshold from an explicit review cost). The paper reports rare
residual cases — safe-but-hallucinated outputs the loop does not
catch — that it does not fully characterize. `unverified`: whether the
maximum-of-two-axes combination rule generalizes to more than two risk
axes without over-blocking.

## Related

- [[abstention]] — the block-and-fallback branch is a delayed,
  budgeted form of the reject option.
- [[clinician-veto]] — another healthcare-AI gate on when an answer is
  trusted enough to reach the patient.
- [[severity-weighted-omission-risk]] — a differently-shaped clinical
  risk score, calibrated rather than thresholded by rubric.
- [[cost-controlled-abstention]] — derives its deferral threshold from
  cost, where this loop's thresholds are fixed by rubric.

[^c1]: arxiv-2604-26959 — "Responses are released only when both SRA ≤ 2 and HRA ≤ 2, ensuring clinically acceptable outputs with bounded latency."
[^c2]: arxiv-2604-26959 — "when a response exceeds safety thresholds (SRA ≥ 3 or HRA ≥ 3), CareGuardAI activates an iterative refinement loop that feeds structured feedback from both evaluators back into the generator."
[^c3]: arxiv-2604-26959 — "This refinement process runs for up to three iterations, progressively reducing risk until the response satisfies the release criteria (SRA ≤ 2 and HRA ≤ 2). If the response remains unsafe after all attempts, the system blocks it and returns a refusal-style fallback (e.g., advising the patient to consult a healthcare professional)."
[^c4]: arxiv-2604-26959 — "Removing individual components leads to substantial degradation (deployable rate as low as 39%)"
[^c5]: arxiv-2604-26959 — "the refinement loop effectively mitigates residual risks, achieving nearcomplete convergence (≥98.7%) with ~1 iteration per query."
