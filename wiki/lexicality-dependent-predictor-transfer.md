---
description: "Lexical query performance predictors track a neural retriever better the more lexical that retriever is; sparser SPLADE variants give higher correlations, on three models only."
aliases: ["QPP lexicality transfer", "predictor fit tracks retriever lexicality", "lexical signal dependence of QPP on neural retrievers"]
sources: ["doi-10-48550-arxiv-2302-09947"]
---
# Lexicality-dependent predictor transfer

Most query performance predictors were built for bag-of-words retrieval. They read term statistics of the query and the collection, or the score distribution of a lexical run. Applied to neural first-stage retrievers, they work unevenly, and the paper's proposed explanation is that the fit follows how lexical each neural retriever is. In its words, "the performance that QPP methods achieve on NIR systems seems to correlate with the importance these systems give to lexical signals."[^l1] Among the neural models on Robust '04, the dense bi-encoders are where the predictors do worst: "dense approaches are those where QPP perform the worst."[^l2] The late-interaction and sparse models get the highest post-retrieval correlations, which fits a reading in which the more a model leans on term matching, the more the predictor's lexical inputs still apply.

The test is a dose-response on sparsity. The authors apply the predictors to three versions of SPLADE++ that differ in the regularization that controls sparsity, and they take sparser models to be more lexical, "as a first approximation". The reasoning: "Increasing the sparsity of representations leads to models that cannot rely as much on expansion."[^l3] The result is that "in the majority of the cases, QPPs perform the best for" the sparsest version.[^l4] The one exception is NQC, which "completely reverses" the order.[^l5] The authors conclude that predictor performance "tends to correlate with the degree of lexicality of the NIR approaches."[^l6]

The mechanism is my inference, not the paper's claim. A predictor that reads lexical overlap or the spread of top scores is reading features that a lexical ranker produces by construction. A dense retriever can score documents on a different basis, so the same feature is a weaker proxy for its success. The paper does not measure that.

## Limits

- The lexicality claim rests on three checkpoints of one model family, with sparsity as the proxy for lexicality. The paper calls this "a first approximation", and it does not test dense models with lexical-leaning training, so the direction of causation is open.
- The analysis is for post-retrieval predictors only, because the pre-retrieval ones are weak: "we focus this analysis on post-retrieval methods only."[^l7] Pre-retrieval predictors see only the query, so this note says nothing about them.
- The switches across sparsity levels are not always clean: "There are a few switches, often associated with very close correlation".[^l8] The ordering is a tendency across predictors, not a law.
- Neural models were fine-tuned on MS MARCO and then evaluated zero-shot on Robust '04.[^l9] The lexicality effect is therefore tangled with training domain. The paper contrasts the two collections, but it does not separate the two causes.
- The measure is Pearson correlation on 249 and 43 topics, averaged over the predictors, with nDCG@10 as the target. It is a fit statistic, not a calibrated prediction of when a retriever will fail.

## Related

- [[query-performance-prediction]] — the predictors whose transfer to neural retrieval this note concerns.
- [[semantically-defined-queries]] — the query subset where the lexical and neural runs disagree most, and where the fit is worst.
- [[terminology-concordant-versus-agnostic-queries]] — probes a retriever's lexical dependence with paired queries, not through predictor fit.
- [[embedding-retrieval-literal-token-anchoring]] — embedding retrievers that rank by literal tokens when wording diverges, a related lexical dependence.

[^l1]: doi-10-48550-arxiv-2302-09947 — "the performance that QPP methods achieve on NIR systems seems"
[^l2]: doi-10-48550-arxiv-2302-09947 — "dense approaches are those where QPP perform the worst"
[^l3]: doi-10-48550-arxiv-2302-09947 — "Increasing the sparsity of representations leads to models that cannot rely"
[^l4]: doi-10-48550-arxiv-2302-09947 — "in the majority of the cases, QPPs perform the best for"
[^l5]: doi-10-48550-arxiv-2302-09947 — "Only one predictor, NQC, completely reverses"
[^l6]: doi-10-48550-arxiv-2302-09947 — "tends to correlate with the degree of lexicality of the NIR approaches"
[^l7]: doi-10-48550-arxiv-2302-09947 — "we focus this analysis on post-retrieval methods only"
[^l8]: doi-10-48550-arxiv-2302-09947 — "There are a few switches, often associated with very close correlation"
[^l9]: doi-10-48550-arxiv-2302-09947 — "Models are fine-tuned on the MS MARCO passage dataset"
