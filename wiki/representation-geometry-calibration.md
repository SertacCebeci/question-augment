---
description: "Calibrates LLM confidence for abstention from three geometric signals of each layer's MLP update: its contribution, its rotation, and its cone alignment."
aliases: ["geometric signals for abstention calibration", "knowledge contribution", "embedding rotation", "anisotropic alignment"]
sources: ["arxiv-2604-27914"]
---
# Representation-geometry calibration

> The same MLP contribution can leave a token representation almost where
> it was or send it into a different cone entirely; only the second case
> means the model actually used what it knows.

## Definition / Mechanism

Xu, Chen, Xie & Xiong (2026) calibrate an uncertainty
score for [[conformal-abstention]] using three geometric signals of how each
layer's MLP update moves a token's hidden representation, since MLPs are
the primary locus of stored factual knowledge: "we quantify this influence
using three geometric signals: 1. proximity ω, measuring the MLP's
contribution via its distance to the post-MLP embedding; 2. embedding
rotation θ, capturing the extent to which the update alters the prediction
direction; 3. alignment ϕ, measuring consistency with the dominant
anisotropic direction."[^c1]

**Knowledge contribution ($\Omega$)** decomposes the MLP's write into a
direct component (its proximity to the last token's post-MLP embedding)
and a component propagated to later layers via self-attention, using an
information-flow proximity measure. **Embedding rotation ($\Theta$)**
tracks the angle each layer's update turns the last token's embedding
through; because the model's top-ranked token is invariant to rescaling
but not to rotation past a data-dependent margin, "large rotations can
violate Eq. (15) and change the model's decision."
[^c2]

So a large contribution that does not rotate the embedding did not change
the decision, and the two signals are only loosely coupled. **Anisotropic
alignment ($\Phi$)** is a static complement to the first two dynamic
signals: transformer embeddings concentrate in a narrow in-distribution
cone, and "in-distribution queries induce hidden states that closely align
with η̃ l,in and η l,in , remaining within the anisotropic cone and leading
to more reliable predictions. In contrast, out-of-distribution queries
deviate from this cone."
[^c3]

This is measured as the angle to that cone's dominant direction, separately
for in- and out-of-distribution reference directions.

Concatenating $(\Omega,\Theta,\Phi^{in},\Phi^{out})$ per generated token
into a feature vector, the Mahalanobis distance to the empirical
correct-prediction distribution and to the incorrect-prediction
distribution are combined with uncalibrated confidence to train a
calibrator, whose per-token outputs are aggregated (by perplexity) into
the response-level score that [[conformal-abstention]] thresholds. Across
six QA datasets and three inference models this raised conditional
correctness over strong uncertainty-estimation baselines: "the proposed
method consistently outperforms a broad set of strong baselines, achieving
the highest average conditional correctness of 75.0% under conformal
abstention"[^c4]

## Why it matters

It supplies the missing half of [[conformal-abstention]]'s guarantee: the
theorem bounds correctness given a good ranking of confident-vs-unconfident
answers, but does not produce one, and default confidence signals
(softmax probability, perplexity) are shown elsewhere to be poorly aligned
with correctness for open-ended generation. This gives stall 10 a
mechanism-grounded reason a signal should track correctness — genuine use
of stored knowledge, not surface fluency — rather than a purely empirical
fit.

## Limits

A permutation ablation found the three signal families roughly
interchangeable in contribution: "perturbing each component leads to
comparable degradation, suggesting that they contribute similarly to the
overall effectiveness."
[^c5]

The paper does not identify which signal
matters for which failure mode, only that a calibrator using all of them
outperforms baselines using none. The method requires white-box access to
per-layer hidden states and the unembedding matrix (it is inapplicable to
an API-only model), and, like [[trajectory-geometry-uncertainty-probe]],
its features are validated on one family of tasks (open-ended QA here vs.
multiple-choice there) rather than shown to transfer across generation
settings.

## Related

[[conformal-abstention]] · [[trajectory-geometry-uncertainty-probe]] · [[calibration]] · [[abstention]] · [[semantic-entropy]]

[^c1]: arxiv-2604-27914
[^c2]: arxiv-2604-27914
[^c3]: arxiv-2604-27914 — "In-distribution queries induce hidden states that closely align with η̃ l,in and η l,in , remaining within the anisotropic cone and leading to more reliable predictions. In contrast, out-of-distribution queries deviate from this cone"
[^c4]: arxiv-2604-27914 — "the proposed method consistently outperforms a broad set of strong baselines, achieving the highest average conditional correctness of 75.0% under conformal abstention"
[^c5]: arxiv-2604-27914
