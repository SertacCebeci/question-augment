---
description: "Whitening the mean-difference direction by the non-refusal covariance, with a ridge term, discounts high-variance axes and removed more political refusal than the plain mean difference here."
aliases: ["ridge mean difference", "RMD steering vector", "weighted ridge mean difference", "WRMD", "covariance-whitened steering direction"]
sources: ["arxiv-2512-16602"]
---
# Ridge-whitened steering direction

The plain mean-difference vector ([[mean-difference-steering-vector]]) takes the raw difference of two class means. A ridge-whitened variant keeps the same difference but premultiplies it by the inverse of the covariance of the non-refusal class, regularized by a small multiple of the identity. The paper writes the unit direction as the solution of a linear system: the difference of class means, multiplied by the inverse of the negative-class covariance plus λI, then normalized.[^c1]

The point of the covariance term is to discount axes along which compliant prompts already vary a lot. The paper says the two ridge variants "Both incorporate covariance information from the negative (compliant) distribution to form a contrastive direction that emphasizes discriminative axes."[^c2] The raw mean difference can be large along a high-variance axis that merely separates topics, and whitening pushes the vector toward axes where refusal and compliance differ relative to ordinary spread.

Two variants are defined. The unweighted one (RMD) uses plain class means. The weighted one (WRMD) weights each prompt by a non-negative value derived from its judge score, and centres the activations on a neutral offset, "the mean activation of neutral prompts with refusal" score near zero.[^c3] The ridge term λ keeps the inverse defined in high dimension, where the covariance estimate from a few thousand prompts is badly conditioned. The paper's words: "The regularization coefficient λ > 0 ensures stability in high-dimensional layers and prevents overfitting to small sample variations."[^c4]

## What was measured

On the China-centric set, the mean difference left 33.24% of political prompts refused, and the ridge variant left 27.06%.[^c5] The best reported result is WRMD trained on the extended set, which "reduces political refusals" on Qwen3-Next-80B-A3B-Thinking "from 92.35% to 23.82% while preserving safety (99% on" JailbreakBench), with the paper noting it is "largely maintaining general capabilities."[^c6] I did not parse every cell of the paper's main table, so the WMD-to-WRMD gap is not stated here; the MD-to-RMD comparison is the only like-for-like pair I can cite from the text read.

The authors also fix λ at one value for all runs: "we set the regularization coefficient to λ = 10−2".[^c7] The text read reports no sweep over λ.

## Limits

- The gain is one comparison on one model family, with the ridge term added alongside other changes (weighting, centring, a layer search). The text read does not isolate the covariance term by itself on the same runs.
- Whitening discounts variance but cannot add information. The paper's own caveat that steering "can only surface knowledge already encoded in the model" applies unchanged.[^c8]
- λ = 10⁻² is a fixed choice. Because the whitened direction depends on it, the reported numbers may not transfer to another layer width or model size without retuning. This is my inference from the setup, not a result of the paper.
- The covariance is estimated only on the non-refusal class. If that class is unrepresentative of deployment prompts, the discounting follows the sample rather than the population (my inference).
- The authors' claim that the ridge variants "identify more stable and interpretable linear subspaces" is their reading. The paper offers no test of interpretability beyond the density analysis in [[refusal-signal-dimensionality]].

## Related

- [[mean-difference-steering-vector]] — the unwhitened difference this variant modifies
- [[refusal-signal-dimensionality]] — the dense best-layer vector the paper uses to argue for regularization
- [[judge-scored-refusal-confidence]] — the judge scores that set both the labels and the weights

[^c1]: arxiv-2512-16602 — "the covariance matrix of the negative class"
[^c2]: arxiv-2512-16602 — "Both incorporate covariance information from the negative (compliant) distribution to form a contrastive direction that emphasizes discriminative axes."
[^c3]: arxiv-2512-16602 — "the mean activation of neutral prompts with refusal"
[^c4]: arxiv-2512-16602 — "The regularization coefficient λ > 0 ensures stability in high-dimensional layers and prevents overfitting to small sample variations."
[^c5]: arxiv-2512-16602 — "33.24% refusal rate while RMD reaches 27.06%"
[^c6]: arxiv-2512-16602 — "92.35% to 23.82% while preserving safety (99% on"
[^c7]: arxiv-2512-16602 — "we set the regularization coefficient to"
[^c8]: arxiv-2512-16602 — "already encoded in the model; they cannot introduce new information."
