---
description: "An LLM's attention on an ambiguous prompt is measurably diffuse; explicit pre-inference disambiguation concentrates it on the correct referent, tracking a 3-8pt accuracy gain."
aliases: ["DisambiguSLM", "semantic risk"]
sources: ["arxiv-2604-23263"]
---
# Attention-entropy signature of prompt ambiguity

> A prompt's ambiguity is not only a property of its words — it shows up as diffusion in the reader's own attention, before it ever produces a wrong answer.

## Definition / Mechanism

Huang, Zhang, Puspitasari, Zhang, Zhou & Chen (2026) motivate their method from a specific mechanism of failure: "This stems from high-entropy diffusion in the attention matrix AQ that leads to the expansion of the inference path BQ . We define this input semantic risk as a measure of the inference uncertainty of the LLM." They give this risk a conceptual form, `R(Q) = H(AQ) + γ|BQ|`, "where H(AQ ) is the attention entropy that characterizes the degree of dispersion in attention distribution, |BQ | is the number of competing thinking branches, and γ defines the coefficient that penalizes the branch expansion." They name three risk types a prompt can carry: "Referential ambiguity refers to the presence of unclear referents. Missing or implicit assumption refers to the omission of key premises or background assumptions in the input. Temporal ambiguity refers to the unclear temporal relationship or sequence of events."[^c3]

Their pipeline, DisambiguSLM, resolves this without ever asking the user: a small language model (SLM) scans the prompt for risk points, two independent SLMs each produce an interpretation of a flagged point, and a cosine-similarity check against a threshold decides whether to fuse the two readings by concatenation or to run a conflict-resolution pass; the resolved points are then aggregated into an enhanced context fed to the answering LLM in place of the original prompt.[^c4]

The signature this note names is what happens inside the *answering* model, not the SLM, when it reads the resolved prompt instead of the original: on Llama-3-8B, across the layers, "Focus ratio of Q′ exhibits immense growth in the early layer (e.g., 8 to 15) with a maximum increase of approximately eight to ten times. Meanwhile, the focus ratio of Q is relatively constant focus across all layers." Entropy over the same attention distribution shifts correspondingly toward the low-entropy, high-focus region once the prompt is disambiguated, and a token-type breakdown shows attention pulled away from sink and stop-word tokens onto the tokens that actually carry the answer.

## Why it matters

This gives an instrument for "has the answerer resolved this reading" that does not depend on asking it, or on the output being wrong: the entropy and focus ratio of its own attention on the disputed token are readable before generation. The behavioral payoff tracks it — "we can increase the LLM's reasoning performance by about 8 points of accuracy against naïve prompting and 3 points of accuracy against state-of-the-art prompt optimization methods," with the largest gains on ambiguity-sensitive benchmarks (WSC, BBH-Navigate). The comprehension work happens entirely upstream of the answerer's own read — a second model resolves the referent before the first one ever attends to it — which is a different division of labor from the clarification-question and candidate-back-translation mechanisms this wiki otherwise holds for c9, both of which put the disambiguation work in a dialogue with the asker.

## Limits

- The risk function `R(Q)` is decorative, not operative: "We do not compute the risk function at any stage of DisambiguSLM, and the weight parameters are not instantiated, adjusted, or used for any inference decision-making... the prompt repair process of DisambiguSLM does not depend on the numerical value or the minimized result of this function." The formula explains the phenomenon; it does not drive the mechanism that fixes it.
- The method resolves semantic uncertainty, not missing facts: on tasks limited by absent evidence rather than ambiguous wording, the authors state its benefit "may be limited."
- The attention-entropy validation is a single worked example (a pronoun "it" with two candidate referents) on one model family (Llama-3-8B); whether the focus-ratio signature generalizes across architectures, risk types (temporal, missing-assumption) and languages is unverified here.
- Consistency verification is a single cosine-similarity threshold between two SLM-generated interpretations — no report of how often two genuinely different but individually plausible readings are wrongly fused, or how the threshold was set.

## Related

[[false-premise-question]] · [[interpretation-space]] · [[candidate-back-translation-disambiguation]] · [[logical-conflict-ambiguity]] · [[ambiguity-taxonomy]]

[^c3]: arxiv-2604-23263 — "• Referential ambiguity refers to the presence of unclear referents. • Missing or implicit assumption refers to the omission of key premises or background assumptions in the input. • Temporal ambiguity refers to the unclear temporal relationship or sequence of events."
[^c4]: arxiv-2604-23263 — "we pass each risk point pi to two independent SLMs that generate two semantic interpretations ri,1 and ri,2 . We then check the consistency ci of these two interpretations by calculating their semantic embedding similarity"
