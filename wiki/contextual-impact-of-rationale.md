---
description: "Sufficiency read as contextual impact: how far a model's confidence drops when non-rationale context is ablated; a high score signals interfering context, not a strong rationale."
aliases: ["rationale sufficiency", "contextual impact", "CI", "contrast-example sufficiency"]
sources: ["arxiv-2511-16353"]
---
# Contextual impact of a rationale

A human rationale is a binary mask over the input: the tokens an annotator marked as the reason for a label. Sufficiency measures how much of the model's confidence in a class survives when only the rationale is kept. For an input x_i and its counterexample r_i, in which the non-rationale context tokens are ablated, the sufficiency for class j is the difference of the two probabilities, M(x_i)j − M(r_i)j, averaged over a dataset.[^c1] The ablation is done by removal or by masking; the paper reports that the two give similar scores and analyses removal only.[^c2]

The paper's contribution is a reading of the sign. A value of zero means the rationale alone is strictly sufficient for the correct label.[^c3] Higher values mean the other context tokens also contribute to the prediction.[^c4] The authors therefore propose to call the quantity contextual impact (CI): as it approaches zero, the context adds nothing beyond the rationale, and a high CI is expected to mean low rationale informativeness.[^c5] "Contextual impact appropriately renames sufficiency," they write.[^c6]

Read this way, the score does not measure how strong the rationale is. It measures how much the context interferes with the rationale in the same input. The paper's instance-level analysis points the unexpected way: higher CI goes with better predictions, visible at the extremes of the CI spectrum.[^c7] The reading offered is that high-CI inputs draw on both rationale and context, so a high score reflects the context's relative weakness at interfering "with rationale information in the same input," not the rationale's absolute strength.[^c8] A model that performs well through shortcuts in the context can also have high CI despite informative rationales, so the score can hide the process that produced it.[^c9]

Across models the dataset-average CI differs sharply on the same data. The e-SNLI gap between BERT and the other models is large.[^c10] BERT is overall positive, while ModernBERT is characterised by an overall negative CI.[^c11] The sign of the average is thus a property of the model as much as of the rationale.

The practical conclusion the paper draws is negative: "sufficiency is not a good indicator of how to prioritise information in training a model."[^c12]

## Limits

The ablation creates inputs unlike those the model sees in use: the paper notes that sufficiency may lead to out-of-distribution examples "when non-rationales are removed or masked."[^c13] The evidence for a link between low CI and high rationale informativeness is thin: the authors write "there are signs, although thin," for regularised BERT only.[^c14] Four models, three seeds and six datasets were used, with "default hyperparameters" and "only slight adaptations."[^c15] The models use different tokenisers, so the alignment between subword tokens and rationales "may also differ."[^c16] The authors name extension to other languages as future work.[^c17] Whether the same picture holds for comprehensiveness, the removal-based counterpart, is left open.

## Related

- [[sufficiency-criterion-strictness]] — shares the word "sufficiency" but not the object: there a verdict on whether a context suffices for an answer depends on how lenient the criterion is; here a faithfulness proxy computed on human rationales.
- [[alpha-gameability-of-faithfulness-metrics]] — another intervention-based family of faithfulness metrics; the out-of-distribution caveat above is the kind of issue that bears on both (my reading, not the paper's claim).
- [[rationale-token-learnability]] — the other measure in the same work; the paper finds it unrelated to CI.
- [[attention-regularization-from-rationales]] — the training paradigm in which the same rationales enter a model.

[^c1]: arxiv-2511-16353 — "We calculate sufficiency as the confidence change of the model M"
[^c2]: arxiv-2511-16353 — "As the two implementations produce similar scores"
[^c3]: arxiv-2511-16353 — "the rationale alone is strictly"
[^c4]: arxiv-2511-16353 — "Higher values indicate that the other context tokens also contribute important information to the prediction"
[^c5]: arxiv-2511-16353 — "High CI is expected to entail low"
[^c6]: arxiv-2511-16353 — "contextual impact appropriately renames sufficiency"
[^c7]: arxiv-2511-16353 — "pointing to higher CI, better predictions"
[^c8]: arxiv-2511-16353 — "with rationale information in the same input"
[^c9]: arxiv-2511-16353 — "sufficiency can mask underlying"
[^c10]: arxiv-2511-16353 — "the large difference between CI for BERT"
[^c11]: arxiv-2511-16353 — "a model characterised by an overall negative CI"
[^c12]: arxiv-2511-16353 — "indicator of how to prioritise information in training a model"
[^c13]: arxiv-2511-16353 — "examples when non-rationales are removed or masked"
[^c14]: arxiv-2511-16353 — "There are signs, although thin,"
[^c15]: arxiv-2511-16353 — "default hyperparameters were used with only slight adaptations"
[^c16]: arxiv-2511-16353 — "As different models are pre-trained using different tokenisers"
[^c17]: arxiv-2511-16353 — "We would like to extend our analyses to more datasets including other languages"
