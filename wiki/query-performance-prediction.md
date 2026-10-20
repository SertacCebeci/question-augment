---
description: "Query performance prediction estimates how well a system will serve a text prompt, scored against human relevance judgments; a text-only predictor is competitive with image-based ones."
aliases: ["prompt performance prediction", "query difficulty prediction", "QPP", "pre- and post-retrieval performance prediction", "query difficulty estimation"]
sources: ["doi-10-48550-arxiv-2406-04746", "doi-10-48550-arxiv-2204-11489", "doi-10-48550-arxiv-2302-10126", "doi-10-48550-arxiv-2310-11405", "doi-10-48550-arxiv-2302-09947"]
---
# Query performance prediction

Query performance prediction (QPP) estimates how well a system will serve a query, either before it runs (pre-retrieval) or after it has produced output (post-retrieval). In text-to-image work the query is a prompt, and its performance is what human judges make of the images produced for it. The PQPP benchmark makes that measure concrete. For each of 10,200 prompts, two diffusion models each produce images, and annotators label every image as high relevance, low relevance, no relevance or unrealistic, mapped to 2, 1, 0 and -1.[^c1][^c2] A prompt's human-based prompt performance (HBPP) is the average relevance score over its generated images.[^c3] On the retrieval side the same texts are scored by precision at 10 (P@10) and by reciprocal rank, over images retrieved by CLIP and BLIP-2.[^c4][^c5]

The predictors come in two families. Pre-generation predictors see only the text: a BERT encoder with a regression head fine-tuned on the labelled prompts,[^c6] and simple counts such as the number of WordNet synsets and words. Post-generation predictors see the output: a CLIP model fine-tuned to score each image's relevance and aggregated over the images,[^c7] and a CNN that reads the matrix of CLIP image-image similarities.[^c8] Evaluation is by Pearson and Kendall correlation between predicted and measured performance on a held-out test split.[^c9]

The results show that supervision helps and that the text alone carries much of the signal. For image generation the post-generation fine-tuned CLIP has the highest correlation with performance.[^c10] Its Pearson coefficient is 0.649 on GLIDE.[^c11] The second-best predictor is the fine-tuned BERT, "which does not even see the generated/retrieved images".[^c12] For retrieval the top correlations are split among BERT, fine-tuned CLIP and the CNN, so there is no clear winner. The authors call the pre-retrieval BERT "a worthy competitor for the post-retrieval predictors".[^c13] Lexical counts do not do the job. The authors' finding is that simple features "are not able to capture the complexity of prompts/queries in text-to-image tasks".[^c14]

The approach differs from earlier work in one respect. Bizzozzero et al. introduced prompt performance prediction, but their ground truth is generated automatically, and the authors write that this "may introduce a significant bias in the evaluation".[^c15] PQPP instead uses human relevance judgments, and it measures the same prompts in both generation and retrieval. That joint measurement is what makes the comparison in [[generation-retrieval-difficulty-divergence]] possible. The idea of predicting difficulty from history also appears in RL post-training, as in [[shared-history-prompt-difficulty-prediction]]. There the difficulty is the success rate of a changing policy, inferred from its own training record. Here it is the human-judged quality of a frozen generator's output, predicted from the text before generation. That contrast is my inference, not a claim the paper makes.

The name also covers ad hoc text retrieval, where the measure is average precision rather than human relevance. Chen, He and Sun predict AP@1000 for queries run through query likelihood on three TREC collections, and score each predictor by how well its predicted ordering matches the actual ordering of AP.[^c18][^c19] Their predictor reads several queries at once, which is a different design from the single-prompt predictors above; see [[groupwise-query-performance-prediction]]. Because the measure differs, the correlations reported here and there are not directly comparable.

The same measurement problem appears for images. The iQPP benchmark places the problem in query-by-example image retrieval, "where images have to be retrieved given an image query."[^c20] It presents itself as "the first benchmark for image query performance prediction in the query-by-example CBIR setting."[^c21] Its predictors come in the same two kinds. Three of its pre-retrieval predictors are unsupervised, and "the first three pre-retrieval predictors are unsupervised, while the last one is supervised on labeled" training queries.[^c22] Post-retrieval predictors "take into account the returned list of" results,[^c23] and they "generally obtain higher" correlations than the pre-retrieval ones.[^c24] The authors conclude that "the image QPP task is far from being solved, since none of the" predictors they test reaches a Kendall 𝜏 of 0.65 or above.[^c25][^c26] Here the measure is average precision or precision at 100 over a fixed image database, not a human relevance label.[^iqpp-measure]

Neural text retrieval is a harder target for the same predictor family. Faggioli et al. apply nineteen QPP methods to seven lexical retrievers and seven BERT-based first-stage retrievers, on Robust '04 and TREC Deep Learning '19, and find that the predictors "perform statistically significantly worse on neural IR systems".[^c33] The gap shows in the mean Pearson correlation between predictor and nDCG@10. On Deep Learning '19 it is 38.1% for lexical runs, "On TIR runs, almost all predictors perform particularly well (mean",[^c34] against 13.1% for neural ones: "Conversely, on NIR the performance is overall lower (13.1%) and".[^c35] The authors tie the remaining fit to how lexical each neural retriever is, a proposal taken up in [[lexicality-dependent-predictor-transfer]].[^c36] The failure is also concentrated on the queries where lexical and neural runs disagree most, discussed in [[semantically-defined-queries]]. This is a second domain for the same QPP concept, with a different retriever family, not a replacement for the image results above.

## Limits

- The neural text-retrieval result covers two collections and nDCG@10 only, and the neural models are zero-shot on Robust '04.[^c37] The paper's own ANOVA effects are small, and it does not test a predictor built for neural retrieval; see scaled-absolute-rank-error for how those effects were measured.
- The iQPP results rest on four image collections and two retrieval systems, and a predictor's rank moves across them; see [[predictor-generalization-across-scenarios]].
- Two generators and two retrievers. The results are for SDXL and GLIDE, and for CLIP (ViT-B/32) and BLIP-2 (ViT-L). Nothing here shows that the ranking of predictors survives a different model. The paper's cross-model experiments are where that would be tested. I did not read them.
- The prompts are MS COCO captions selected by k-means, plus DrawBench prompts.[^c16] Real users' prompts may differ from both. The paper notes that user-written prompts "can often be more descriptive", but that point is cited, not measured here.
- Retrieval performance is relative to a fixed image pool. The retrieved set is capped: "restrict the number of retrieved images to 2,000 per query".[^c17] Relevance labels come from a sentence-BERT similarity threshold followed by human review. A different pool would change which images count as hits.
- Each HBPP is an average over four images from two generators, so a single prompt's score rests on a small sample. The part I read reports no per-prompt reliability estimate. This is my inference.
- The best correlations are moderate, not decisive. The paper reports Pearson and Kendall values, not calibrated predictions of when a prompt will fail. The predictors are supervised on the benchmark's own annotators, so they do not transfer for free to other annotators or other scales.

## Related

- [[generation-retrieval-difficulty-divergence]] — the same prompt can be hard for generation and easy for retrieval, so a predictor for one does not stand in for the other.
- [[shared-history-prompt-difficulty-prediction]] — a difficulty predictor for RL training, built from training history rather than from the text.
- [[groupwise-query-performance-prediction]] — a post-retrieval QPP predictor for ad hoc retrieval that lets a batch of queries share context.
- [[multi-hop-retrieval-path-difficulty]] — a pre-retrieval predictor for multi-hop QA, scored against retriever average precision rather than human relevance judgements.
- [[coherence-based-performance-prediction]] — a post-retrieval predictor for text retrieval that reads the similarity among the top-ranked documents rather than scores or images.[^c28]
- [[predictor-generalization-across-scenarios]] — how a predictor's rank moves with the collection, the retrieval system and the correlation measure, in the image benchmark.
- [[saturated-performance-measure]] — why a target that most queries reach at its ceiling, such as P@10, can change which predictor looks best.

[^c1]: doi-10-48550-arxiv-2406-04746 — "we generate images with two diffusion models"
[^c2]: doi-10-48550-arxiv-2406-04746 — "high relevance (score 2)"
[^c3]: doi-10-48550-arxiv-2406-04746 — "The performance of a prompt is given by the average"
[^c4]: doi-10-48550-arxiv-2406-04746 — "the number of true positive images and n"
[^c5]: doi-10-48550-arxiv-2406-04746 — "the ratio between 1 and the rank of the first"
[^c6]: doi-10-48550-arxiv-2406-04746 — "attaching a custom regression head to the"
[^c7]: doi-10-48550-arxiv-2406-04746 — "a binary classification head for the image retrieval scenario"
[^c8]: doi-10-48550-arxiv-2406-04746 — "The correlation of an (image, image) pair is given by the cosine similarity"
[^c9]: doi-10-48550-arxiv-2406-04746 — "To evaluate performance predictors, we measure the Pearson and"
[^c10]: doi-10-48550-arxiv-2406-04746 — "For image generation, the fine-tuned CLIP shows the highest correlation"
[^c11]: doi-10-48550-arxiv-2406-04746 — "0.649 for GLIDE"
[^c12]: doi-10-48550-arxiv-2406-04746 — "which does not even see the generated/retrieved images"
[^c13]: doi-10-48550-arxiv-2406-04746 — "a worthy competitor for the post-retrieval predictors, being"
[^c14]: doi-10-48550-arxiv-2406-04746 — "are not able to capture the complexity of prompts/queries in text-to-image tasks"
[^c15]: doi-10-48550-arxiv-2406-04746 — "the ground-truth is automatically generated, which may introduce a significant bias in the evaluation"
[^c16]: doi-10-48550-arxiv-2406-04746 — "we combine the 200 prompts from DrawBench"
[^c17]: doi-10-48550-arxiv-2406-04746 — "restrict the number of retrieved images to 2,000 per query"
[^c18]: doi-10-48550-arxiv-2204-11489 — "of the queries with the actual ordering of average precision for the top 1000"
[^c19]: doi-10-48550-arxiv-2204-11489 — "retrieved by the Query Likelihood (QL) model"
[^c33]: doi-10-48550-arxiv-2302-09947 — "QPPs perform statistically significantly worse on neural IR systems"
[^c34]: doi-10-48550-arxiv-2302-09947 — "On TIR runs, almost all predictors perform particularly well (mean"
[^c35]: doi-10-48550-arxiv-2302-09947 — "Conversely, on NIR the performance is overall lower (13.1%) and"
[^c36]: doi-10-48550-arxiv-2302-09947 — "the performance that QPP methods achieve on NIR systems seems"
[^c37]: doi-10-48550-arxiv-2302-09947 — "Models are fine-tuned on the MS MARCO passage dataset"
[^c20]: doi-10-48550-arxiv-2302-10126 — "retrieval, where images have to be retrieved given an image query."
[^c21]: doi-10-48550-arxiv-2302-10126 — "the first benchmark for image query performance prediction in the query-by-example CBIR setting."
[^c22]: doi-10-48550-arxiv-2302-10126 — "the first three pre-retrieval predictors are unsupervised, while the last one is supervised on labeled"
[^c23]: doi-10-48550-arxiv-2302-10126 — "All post-retrieval predictors take into account the returned list of"
[^c24]: doi-10-48550-arxiv-2302-10126 — "post-retrieval predictors generally obtain higher"
[^c25]: doi-10-48550-arxiv-2302-10126 — "the image QPP task is far from being solved, since none of the"
[^c26]: doi-10-48550-arxiv-2302-10126 — "existing or proposed predictors can surpass a Kendall 𝜏 of 0.65,"
[^iqpp-measure]: doi-10-48550-arxiv-2302-10126 — "measures of retrieval effectiveness, namely the average precision"
[^c28]: doi-10-48550-arxiv-2310-11405 — "upon either the distribution of the retrieval scores, or the coherence"
