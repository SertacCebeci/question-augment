---
description: "Mutual information between a context and an LM's compression, estimated from sampled log-probabilities over N contexts, is bounded by log N and needs no full-vocabulary distribution."
aliases: ["Monte Carlo MI over compressions", "sampled MI estimator for LM outputs", "compression mutual information estimator"]
sources: ["arxiv-2512-21720"]
---
# Sampled mutual information estimator

The quantity is [[mutual-information|mutual information]] between a raw context X and a compression Z the model writes from it. Written as a KL divergence between the joint and the product of marginals, it needs p(z), the marginal over compressions, and that is intractable for a language model.[^c1] The estimator replaces the marginal with a sample. Draw M compressions from the encoder for each of N contexts; for each compression, compare its log-probability under its own context with the log of its average probability across the N contexts. The average over all samples of that difference is the estimate.[^c2]

Two properties make it usable as a diagnostic. First, it needs only the log-probabilities an inference engine already returns for sampled sequences: "With this estimator, we do not need access to the full probability distribution over the vocabulary, which allows us to use accelerated inference engines such as SGLang."[^c3] Second, the estimate is capped: it can be no larger than log N, reached when each compression is far more likely under its own context than under any other.[^c4] The paper draws that ceiling as a dotted line on its plots: "The black dotted line represents the theoretical maximum of the mutual information estimator at" log N.[^c5]

The paper conditions on a query, so the quantity is I(X; Z | Q). "each compression Z is generated conditioned on the query Q, so we estimate I(X; Z | Q)", and every term is conditioned on the same Q.[^c6] Negative values can appear from finite-sample variance; the paper clips them to zero.[^c7]

Used across compressors of different sizes, the estimator ranks them. The paper finds that "Larger compressors retain more mutual information and are more bit efficient."[^c8] Dividing by output length gives the per-token rate, treated in [[information-rate-per-token]].

## Limits

- The estimator is practical, not optimal. The paper says so directly: "We do not claim theoretical optimality with this estimator."[^c9] It is a plug-in Monte Carlo average, so it inherits finite-sample variance. Unlike counting-based estimates, its bias is not the usual histogram bias ([[information-estimation-bias]]), but the sampling error is real and is not characterised in the paper.
- Small models are a problem for the probabilities themselves. The paper finds that "LMs at 1–3B could assign high likelihoods to nonsensical token sequences," so it works mostly with proxy models of 7–8B from another family.[^c10] It notes that using the compressor's own log-probabilities gives similar results, but that is one reported check, not a general guarantee.[^c11]
- The ceiling log N limits what can be resolved. On FinanceBench "mutual information saturates already at the 3B scale", so the estimator cannot separate larger compressors there.[^c12]
- The marginal p(x) is approximated by the N contexts drawn from the dataset. The estimate therefore depends on which corpus those contexts come from, and the paper's values are specific to its five datasets. This is my inference from the formula, not something the paper measures.

## Related

- [[mutual-information]] — the quantity this estimator approximates; the KL form and its general definition live there.
- [[information-estimation-bias]] — the counting-based estimators whose bias the sampled form avoids by construction but does not remove.
- [[information-rate-per-token]] — the per-token rate built from this estimate, which the paper relates to accuracy.
- [[compressor-predictor-scaling]] — the setting in which the estimate is used to compare compressors.

[^c1]: arxiv-2512-21720 — "While computing p(z) is intractable, we can sample from and evaluate our encoder p(z|x), and take samples"
[^c2]: arxiv-2512-21720 — "where zij ∼ p(z|xi ), i = 1, . . . , N, j = 1, . . . , M and xl ∼ p(x), l = 1, . . . , N ."
[^c3]: arxiv-2512-21720 — "With this estimator, we do not need access to the full probability distribution over the vocabulary, which"
[^c4]: arxiv-2512-21720 — "the maximum is achieved when p(zij |xi ) ≫ p(zij |xl ) or p(zij |xi ) ≪"
[^c5]: arxiv-2512-21720 — "represents the theoretical maximum of the mutual information estimator at"
[^c6]: arxiv-2512-21720 — "each compression Z is generated conditioned on the query Q, so we estimate I(X; Z | Q)"
[^c7]: arxiv-2512-21720 — "produce small negative values due to finite-sample variance. We correct these artifacts by clipping MI to"
[^c8]: arxiv-2512-21720 — "Larger compressors retain more mutual information and are more bit efficient."
[^c9]: arxiv-2512-21720 — "We do not claim theoretical optimality with this estimator."
[^c10]: arxiv-2512-21720 — "we find that LMs at 1–3B could assign high likelihoods to nonsensical token sequences,"
[^c11]: arxiv-2512-21720 — "proxy models are not strictly necessary and similar results can be obtained by evaluating"
[^c12]: arxiv-2512-21720 — "By contrast, on FinanceBench, mutual information saturates already at the 3B scale."
