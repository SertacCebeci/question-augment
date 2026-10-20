---
description: "A ground-truth retrieval measure that most queries reach at its ceiling, such as P@10, leaves little spread to predict, so the choice of measure can change which difficulty predictor appears best."
aliases: ["ceiling effect in query difficulty targets", "P@10 saturation", "measure ceiling in query performance prediction"]
sources: ["doi-10-48550-arxiv-2302-10126"]
---
# Saturated performance measure

Query performance prediction needs a target: the measured effectiveness of the retrieval on each query. The target is an ordinary retrieval measure, and measures differ in how much of their range the queries actually use. Precision at a small cut-off can sit at its maximum for many queries. In the image benchmark the authors "found that a high percentage of the test queries (between 29% and 82%, depending on the data set) have a P@10 score of 1."[^c1] They note that P@10 "is sometimes used in text QPP," and so the choice is not new to them.[^c2]

For that reason the iQPP authors use precision at 100 as the difficulty target: "query difficulty, we decided to use P@100."[^c3] They keep average precision as a second target and report both. The lesson they draw is that the choice matters for the ranking of predictors, not only for the size of the numbers. On Caltech-101 the best pre-retrieval predictor for AP is the fine-tuned ViT, but under P@100 "the fine-tuned ViT is surpassed by the classification head dispersion in one scenario."[^c4] The authors conclude that "is thus important to include more than a single measure to estimate ground-truth query performance."[^c5]

The mechanism I would infer from this is as follows. If a large share of queries sits at the ceiling, those queries share one target value. A correlation between predicted and measured performance is then fixed mostly by how the predictor orders the minority of queries below the ceiling, and the ordering among tied queries carries no information. This is my inference. The paper reports the proportion of ceiling queries, and it reports the change in ranking, but it does not measure the effect of saturation on the correlation itself.

## Limits

- The saturation figures are for four image collections and one retrieval family. The paper does not measure how often P@10 saturates for text QPP, where it is "sometimes used."[^c2]
- Only two cut-offs and one alternative measure are compared, P@10 against P@100, plus AP. No curve over k is shown, so the claim that P@100 is a better target is the authors' judgement, supported by the saturation proportion rather than by a test of predictive value.
- The paper does not show that the difficulty ranking it finds is the one a user needs. P@100 measures how many of the top 100 images are relevant, which is a benchmark choice and not a user's experience of the search.
- The mechanism of the tie effect above is my inference; it was not tested.

## Related

- [[query-performance-prediction]] — the target that these measures define for predictors.
- [[predictor-generalization-across-scenarios]] — the measure is one of the three axes, with collection and retrieval system, along which predictor rankings move.

[^c1]: doi-10-48550-arxiv-2302-10126 — "percentage of the test queries (between 29% and 82%, depending on the data set) have a P@10 score of 1."
[^c2]: doi-10-48550-arxiv-2302-10126 — "Although P@10 is sometimes used in text QPP [75], we found that a high"
[^c3]: doi-10-48550-arxiv-2302-10126 — "query difficulty, we decided to use P@100."
[^c4]: doi-10-48550-arxiv-2302-10126 — "the fine-tuned ViT is surpassed by the classification head dispersion in one scenario."
[^c5]: doi-10-48550-arxiv-2302-10126 — "is thus important to include more than a single measure to estimate ground-truth query performance."
