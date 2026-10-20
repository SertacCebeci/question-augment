---
description: "A stopping threshold tuned to one LLM snapshot goes stale as the model changes, and turning it further down does not reliably recover accuracy."
aliases: ["metacognitive threshold sensitivity", "confidence threshold sensitivity"]
sources: ["arxiv-2604-19899"]
---
# Threshold staleness

> A stopping threshold tuned to one model snapshot does not stay tuned — and
> tightening it further does not reliably buy more accuracy.

## Definition / Mechanism

MetaRAG Iturra Bocaz & Galuščáková (2026) gates its
metacognitive-critique loop on a single scalar: a similarity score between
the fast first-pass answer and a reference answer, compared against a fixed
threshold τ. "A similarity score between 𝑦 and 𝑦 ′ is computed, and
metacognitive evaluation is triggered only when this score falls below a
predefined threshold; otherwise, the answer is accepted directly." Below
τ the system reformulates the question and retrieves again; above it, the
first answer stands — τ *is* the stopping rule.

Re-running the original setup at the original τ=0.4 (tuned on an earlier
GPT-3.5 snapshot) reproduces the qualitative ranking of methods but not the
absolute scores. Sweeping τ over {0.4, 0.3, 0.2, 0.1} on the same 500-question
2WikiMultiHopQA subset shows the threshold no longer optimal at 0.4: "MetaRAG
is highly sensitive to this parameter, as lower thresholds reduce transitions
into the MS and additional retrieval calls, while improving answer quality.
In the original MetaRAG paper, the threshold is set to 0.4, which yields the
best results under their setup. In contrast, our reproduction, answer
quality (e.g., EM/F1) peaks at a threshold of 0.2, whereas further lowering
the threshold to 0.1 results in decreased performance, even though it
reduces retrieval and generation calls." Fewer retrieval calls is not the
same axis as better answers, and past τ=0.2 the two decouple.

Two explanations are offered, not mutually exclusive. First, the backbone
itself moved: "As a result, the original threshold configuration may no
longer be optimal, and repeatedly triggering metacognitive control may
provide limited additional benefit." Second, the diagnostic in the same
study shows an NLI critic already validates far more retrieved evidence as
sufficient than the LLM's own judgment does, so triggering the loop harder
mostly asks the model to relink evidence it already holds: "the necessary
evidence is often already present. The bottleneck therefore appears to lie
in how evidence is connected across hops rather than in its availability."[^c4]

## Why it matters

A stopping threshold is a property of the (task, model) pair, not of the
task alone. A silent backbone update — the common case for any
closed-source LLM deployed over time — can leave a previously-calibrated
threshold both wrong in magnitude and wrong in direction: an asker tuning
"how cautious should I be before I stop asking" cannot treat one sweep as a
permanent setting, and cannot assume that making the gate stricter is always
safe, since past some point stricter gating burns calls on evidence the
system already had rather than evidence it lacked.

## Limits

- The sweep runs on one dataset (2WikiMultiHopQA, 500-question dev subset)
  and one backbone (GPT-3.5) with the planner and max-iteration cap held
  fixed; whether the same non-monotone curve holds on HotpotQA or on
  Llama3.3 is unverified.
- The model-drift explanation is offered by the source as "one possible
  explanation," not confirmed causally — the original 2024 GPT-3.5 snapshot
  cannot be rerun to isolate drift from other implementation differences
  (unverified).
- Only the accept/critique gate is swept; the paper does not test whether a
  *relative* or adaptive threshold (rather than a fixed scalar) would avoid
  staleness.

## Related

[[verification-aware-stopping]] · [[stopping-rules]] · [[calibration]] · [[self-answer-driven-search-depth]]

[^c4]: arxiv-2604-19899 — "the necessary evidence is often already present. The bottleneck therefore appears to lie in how evidence is connected across hops rather than in its availability."
