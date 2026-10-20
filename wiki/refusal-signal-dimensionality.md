---
description: "A learned refusal vector at the best layer of an 80B model is dense, its magnitude decaying over many dimensions, which the paper reads against the one-direction account of refusal."
aliases: ["refusal subspace dimensionality", "multi-dimensional refusal", "distributed refusal signal"]
sources: ["arxiv-2512-16602"]
---
# Refusal signal dimensionality

A refusal is often modelled as a single direction in hidden activations. The reference for that view is Arditi et al. (2024), who found that refusal behaviour is "mediated by a one-dimensional subspace," and that "this subspace disables refusal capabilities" when removed.[^c1] The question this note asks is different from whether one direction can switch refusal off. It asks how many dimensions a learned refusal vector spreads over, and what that spread says about the signal.

The paper measures two things on Qwen3-Next-80B-A3B-Thinking. The first is where the signal sits in depth. For each layer it correlates the projection of each prompt's hidden state onto the learned vector with the judge's refusal score. The correlation "peaks in the deeper layers of the network (layer" 42 is the maximum, at 0.835).[^c2] The paper's reading is that refusal mechanisms operate primarily "in the upper transformer layers where high-level" semantic representations are formed.[^c3]

The second is how concentrated the vector is across its own coordinates. The paper sorts the magnitudes of the layer-42 vector and reports that the top 10 dimensions carry "only 1.9% of total magnitude," with magnitude decaying gradually. From this it concludes that "refusal information is distributed across many dimensions rather than concentrated in a single direction."[^c4] The vector analysed is the WRMD estimate trained on the extended dataset, so the density is a property of a regularized estimate, not of the raw activations alone.[^c5]

## How the claim is built

The argument has three steps. A correlation peak places the signal in deep layers. A correlation with the judge score is a reading of the signal's location, not of its dimension. Density of the learned vector is then the only evidence offered for distribution across dimensions. The paper draws the consequence that "effective steering requires careful regularization": if the signal is spread out, a plain estimate picks up noise along high-variance axes, which is the motivation for the ridge variant in [[ridge-whitened-steering-direction]].[^c6]

The paper states that its result is "a more nuanced picture" than Arditi et al.'s.[^c7] The two accounts are not directly contradictory. Arditi et al. ask whether removing a direction disables refusal; the density analysis asks whether the best linear estimate is concentrated. A vector can be dense yet carry most of its causal effect in one direction, and the paper runs no ablation that separates those.

## Limits

- One model, one layer. The density figure is from layer 42 of the 80B model. The correlation peak is shown for that model's layers; the text read gives no equivalent density numbers for the 4B models.
- Density is not dimensionality. A dense vector can be the sum of a few large components in a rotated basis, and "top 10 dimensions" depends on the coordinate system of the residual stream. The paper does not test rank or perform a subspace decomposition (my inference).
- The estimator shapes the result. The vector comes from a ridge-regularized, whitened estimate, which discounts high-variance axes by design. Some of the density may come from that choice rather than from the model. The paper does not compare densities across estimators on the same layer.
- The correlation is with judge scores, which are themselves a model's reading ([[judge-scored-refusal-confidence]]). The layer location inherits any bias in those scores.
- Distribution across dimensions does not by itself say how many directions are needed for control. The paper's own steering results use one vector per layer across several layers, so its control is not a test of the one-direction question either.

## Related

- [[recognition-refusal-dissociation]] — a separate linear direction for answerability, found nearly orthogonal to the safety-refusal direction; the two notes ask which direction and how many
- [[mean-difference-steering-vector]] — the unwhitened vector whose density the paper contrasts with its regularized one
- [[ridge-whitened-steering-direction]] — the regularized estimator the density finding motivates

[^c1]: arxiv-2512-16602 — "this subspace disables refusal capabilities"
[^c2]: arxiv-2512-16602 — "peaks in the deeper layers of the network (layer"
[^c3]: arxiv-2512-16602 — "primarily in the upper transformer layers where high-level"
[^c4]: arxiv-2512-16602 — "indicating that refusal information is distributed across many dimensions rather than concentrated in a single direction"
[^c5]: arxiv-2512-16602 — "vector (WRMD algorithm, trained in the extended"
[^c6]: arxiv-2512-16602 — "This density suggests that effective steering requires careful regularization"
[^c7]: arxiv-2512-16602 — "However, our analysis reveals a more nuanced picture."
