---
description: "Contextual embeddings crowd into a narrow cone, inflating similarity; centering, standardization or removing the top variance direction lifts a threshold classifier of word relatedness."
aliases: ["anisotropy correction", "all-but-the-top", "embedding centering and standardization", "isotropy correction"]
sources: ["doi-10-48550-arxiv-2411-12147"]
---
# Embedding anisotropy removal

Contextual embeddings are not spread evenly over their space. They crowd into a narrow region, so unrelated words look similar. The CoMeDi system paper states the mechanism: contextual representations are "clustering in a narrow region of the space. This inflates similarity scores, reducing their discriminative power in meaning-related tasks."[^c1] My reading of the mechanism: a cosine-type score measures angle, and when every vector sits in one cone, much of the angle is shared background rather than meaning, so a cut point on the score separates pairs less well.

Three corrections are compared, each applied layer by layer to the target-word representations. The first is centering, "by subtracting the mean vector."[^c2] The second is normal standardization. The third is all-but-the-top, which removes the leading direction of variance: "subtracting the projection on the component of the largest variance."[^c3] The corrections are applied before a threshold selector maps similarity to labels: "Threshold-based methods learn a threshold selector to map similarity scores to labels."[^c4] The point of the correction is therefore to make the space on which the cut is placed less biased.

In the paper's ablation on the discrete relatedness task, the corrections matter and standardization is the strongest: "Standardization consistently performs best across all layers."[^c5] The settings then differ by language and by model. In the evaluation phase the authors used normal standardization "except for Norwegian to address anisotropy,"[^c6] and for the post-evaluation Subtask 1 "All model representations are standardized to remove anisotropy."[^c7] So the correction is a per-setting choice, not a fixed recipe.

What transfers beyond this task is the diagnosis: a threshold on raw similarity inherits whatever geometry the embedding has, and a shared offset or a dominant direction can move every pair toward one side of the cut. My inference, not the paper's claim, is that the same correction would matter for any method that thresholds cosine-like scores, but the paper tests only the relatedness task.

## Limits

- Measured on one task. The gains are in CoMeDi Subtask 1 with a threshold selector optimized for Krippendorff's alpha. The text read does not show that the corrections remove "inflation" as such, only that the task metric rises.
- The method is picked on a development set: "we selected models based on the development set."[^c8] Which correction and layer wins is an empirical choice per setting, and the paper offers no theory that predicts the winner.
- All-but-the-top removes the highest-variance direction, which may carry meaning-relevant variance as well. The paper does not test whether that direction holds any relatedness signal (my inference).
- The claim that anisotropy is a problem rests on prior work (Ethayarajh, 2019) and is not re-tested here.
- The layer curves come from one ablation, while the decoder-only Llama setting uses a different layer (25) and is handled separately in the paper. The ablation's ranking of corrections is not shown to hold across all those models.

## Related

- [[representation-geometry-calibration]] — reads the same anisotropic cone as a signal of in-distribution reliability; here the cone is a nuisance to remove. The two readings serve different ends and do not contradict each other (my inference).
- [[model-variant-spread-as-disagreement]] — the pool whose spread is measured includes these corrections as manipulations, so the choice of correction changes the disagreement estimate.

[^c1]: doi-10-48550-arxiv-2411-12147 — "clustering in a narrow region of the space. This inflates similarity scores, reducing their discriminative power in meaning-related tasks."
[^c2]: doi-10-48550-arxiv-2411-12147 — "centering by subtracting the mean vector"
[^c3]: doi-10-48550-arxiv-2411-12147 — "subtracting the projection on the component of the largest variance"
[^c4]: doi-10-48550-arxiv-2411-12147 — "Threshold-based methods learn a threshold selector to map similarity scores to labels."
[^c5]: doi-10-48550-arxiv-2411-12147 — "Standardization consistently performs best across all layers."
[^c6]: doi-10-48550-arxiv-2411-12147 — "except for Norwegian to address anisotropy"
[^c7]: doi-10-48550-arxiv-2411-12147 — "All model representations are standardized to remove anisotropy."
[^c8]: doi-10-48550-arxiv-2411-12147 — "we selected models based on the development set"
