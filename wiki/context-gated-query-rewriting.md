---
description: "Rewrite only when history supports it: a trained reject outcome, labelled from reformulation behaviour, is proposed against intent drift on functional queries."
aliases: ["when-to-rewrite gate", "demand-aware query rewriting", "personalized query rewriting with reject", "posterior-gated rewriting"]
sources: ["arxiv-2602-17667"]
---
# Context-gated query rewriting

A personalised rewriter that rewrites every query lets the user's history leak into queries that did not need it. The remedy in this work is to make the rewrite conditional. A first decision asks whether the user's context supports a rewrite at all. The model is trained to answer either with a rewritten query or with a special reject outcome that keeps the original query.[^c1] The authors name the failure intent drift: "rewriting risks intent drift," as when a functional query such as "Air fryer" is biased by entertainment history and should not be rewritten from it.[^c2][^c3]

## How the gate is labelled

The labels are mined from behaviour, not written by hand. The starting signal is that user dissatisfaction "is typically signaled by rapid query reformulations."[^c4] A candidate pair is a failed query followed by a successful reformulation. The origin query must show minimal interaction, and the next query must show valid consumption (longer than 10 seconds of watching).[^c5]

Two filters then decide whether the reformulation was personal. The first is a rule-based overlap test: "We retain samples only if gain words" (the terms the reformulation adds) intersect with the user's history, such as titles of videos already watched.[^c6] The second is an LLM check: "Qwen3-32B acts as an expert annotator," asked whether the reformulation is explicitly supported by the user's context.[^c7]

Negatives come from two sources. One is direct satisfaction, where the original query yielded long consumption with no reformulation after it. The other is personalization redundancy: "Instances rejected by the aforementioned" context-overlap or LLM filters.[^c8][^c9] Both kinds are trained to the reject outcome, so the gate and the rewrite share one training target.[^c10]

## What was measured

The gate is not separated from the rewriter in the results. The one ablation on the labelling side is that adding LLM intent verification on top of the rule-based filter raised accuracy for the SFT model from 0.500 to 0.535, on the paper's offline set.[^c11] The authors read this as semantic reasoning giving better training signals than fixed rules. My reading is narrower: one ablation on one dataset, showing that the label filter matters.

The deployed model reports a 1.07% increase in click-through video volume with stay time above 10 seconds, and a 2.97% decrease in query reformulation rate, in an online A/B test.[^c12][^c13] These numbers measure the whole rewriter. They do not isolate what the reject outcome contributed.

## Limits

- The text I read reports no ablation that removes the gate while keeping the rewriter, and no comparison with a rewrite-always or no-personalization policy. The effect of the gate alone is not measured.
- The labels depend on LLM judgment. The text gives no human agreement check on the annotator, so the gate inherits any errors the annotator makes (that absence is my reading).
- Negatives are partly defined by the same filters that define positives. The gate may learn the filter's boundary rather than the underlying need, and whether it transfers beyond the mined distribution is not shown.
- The satisfaction signals are proxies: a time threshold and a reformulation. A quick reformulation is not evidence of dissatisfaction in general (my inference).
- The setting is one video platform with a rich user profile (gender, location, watched videos, past queries). With sparse history a gate of this kind would reject most queries; this is my inference and was not tested.
- Offline training used 20 consecutive days of logs, with the next day as test. Whether the gate stays calibrated as the user base changes is not shown.

## Related

- [[identity-neutral-query-rewriting]] — removes identity terms a question does not need; the same concern about surplus personal context, handled by deletion rather than a reject outcome.
- [[history-conditioned-intent-reconstruction]] — uses history to recover the intent of a vague request; here history is the source of drift, not of information.
- [[query-expansion-harm-asymmetry]] — the same asymmetry for pseudo-relevance feedback: expansion helps few queries and harms more, so selecting when to expand matters.
- [[query-to-question-reformulation]] — the rewrite itself, turning a vague input into an explicit one; the gate decides whether that step should run.
- [[abstention]] — declining to answer; the reject outcome is a declined rewrite.
- [[indexability-conditioned-rewrite-reward]] — the other half of the same work: the reward that shapes what a rewrite looks like once the gate says yes.

[^c1]: arxiv-2602-17667 — "otherwise, output <reject>"
[^c2]: arxiv-2602-17667 — "rewriting risks intent drift"
[^c3]: arxiv-2602-17667 — "rewritten based on entertainment history"
[^c4]: arxiv-2602-17667 — "User dissatisfaction is typically signaled by rapid query reformulations"
[^c5]: arxiv-2602-17667 — "Origin Failure: Minimal interaction"
[^c6]: arxiv-2602-17667 — "We retain samples only if gain words"
[^c7]: arxiv-2602-17667 — "Qwen3-32B acts as an expert annotator"
[^c8]: arxiv-2602-17667 — "Direct Satisfaction"
[^c9]: arxiv-2602-17667 — "Instances rejected by the aforementioned"
[^c10]: arxiv-2602-17667 — "The model is thus trained to output a special <reject> token"
[^c11]: arxiv-2602-17667 — "boosts Acc from 0.500 to 0.535"
[^c12]: arxiv-2602-17667 — "a 1.07% statistically significant increase"
[^c13]: arxiv-2602-17667 — "a 2.97% decrease"
