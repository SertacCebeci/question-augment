---
description: "A groupwise QPP predictor runs a transformer over a batch of queries' BERT encodings, so each query's predicted performance depends on the other queries in its batch."
aliases: ["groupwise QPP"]
sources: ["doi-10-48550-arxiv-2204-11489"]
---
# Groupwise query performance prediction

Pointwise predictors score one query at a time. The BERT-based QPP model of Chen, He and Sun keeps the pointwise encoder and changes what happens after it. Each query-document pair is first encoded by BERT, and each document is represented by its top-1 ranked passage.[^c1][^c2] The [CLS] vectors of a batch are then "reshaped into a sequence", and a four-layer transformer, "which enables the cross attention among the [CLS] vectors in each batch", outputs one predicted performance per pair.[^c3][^c4] The batch is the group: "we regard each batch as a single group of query-document pairs."[^c5]

The motivation is the target, not the architecture. The authors say that existing BERT-based QPP methods "only use the text from individual query-document pairs", while considering other queries "is necessary for QPP tasks, which aim to obtain relative performance among" queries.[^c6][^c7] So the predictor is meant to place queries relative to one another, not only to estimate each one in isolation.

The design is borrowed from re-ranking. Co-BERT "incorporates cross-document ranking context" into BERT re-rankers, and the authors are "Inspired by Co-BERT [8]" to add a groupwise predictor to QPP.[^c8][^c9] What the borrowing carries over is a transformer that lets each item's output depend on the other items in the set.

Context is set by position ids, not by a different network. Shuffling the pairs gives a random order: "pairs are shuffled before being fed into the model in both training and inference."[^c10] In query order, "n queries are grouped together in the batch", so attention runs across queries at the same rank.[^c11] In document order, "A batch consists of n documents" returned for one query.[^c12] The full model, R+Q+D, mixes all three.[^c13]

On Robust04, GOV2 and ClueWeb09-B, the authors report that the model outperforms "all the baselines on all three collections", with significance at 0.05 against the BERT baseline of the same size.[^c14][^c15] The most telling row is the random-order variant. Its pairs are shuffled, so the model is given no ranking position, yet its row is above the BERT-Base row in every one of the six columns. On Robust04 the Pearson values are 0.608 against 0.585 for BERT-Base, and on ClueWeb09-B the Kendall values are 0.353 against 0.321.[^c16][^c17] My inference: in this comparison the gain cannot come from ranking order, since none is given, so it is attributed to the groupwise attention. The baselines are not matched on training data, so this attribution is not isolated (see Limits).

Which context helps depends on the collection. Query-level context "marginally improves" results on Robust04 and GOV2, while document-level context alone "greatly harms the" model on Robust04 and ClueWeb09-B.[^c18][^c19] The authors offer a reading: the model "has only learned the sequence information inside each query" and not the relations between queries.[^c20] That is their explanation of the drop, not a test of it.

Group size matters too. With batch size 1 the model reduces to pointwise learning, and the authors say cross-attention among queries "improves upon the pointwise" method by a large margin.[^c21][^c22] "The groupwise method works best with a group size" of 8.[^c23] The extra cost is small: the authors report "less than 1% additional computational cost compared to its BERT counterpart."[^c24]

What transfers from re-ranking and what does not. The device, attention over a set of encoded items, transfers. The target does not. In re-ranking the items are documents of one query, each with a relevance label. In QPP the items are queries, each with its own average precision, and the paper scores the model by how well its predicted ordering matches the actual ordering of AP@1000, not by error.[^c25] So what the group model learns is a ranking of queries within a group. Whether its outputs are calibrated per query is not measured, and the predictor is linearly combined with a baseline score, "our proposed predictor is linearly combined with" the n(σX%) predictor.[^c26]

## Limits

- Three TREC collections, with "with 249, 150 and 200 keyword queries, respectively."[^c27] With so few queries, the paper uses 2-fold cross-validation with "randomly generate 30 splits for each dataset," and "fold is used for model training and hyper-parameter tuning."[^c28][^c29] The reported numbers are averages over splits, not one held-out run.
- The baselines are not matched on data. They are "configured the same as our model except that they do not have a groupwise predictor", but they use "documents for each query in training due to the small number of queries."[^c30] A gap between groupwise and BERT rows therefore mixes the head with the training setup.
- The supervision label was chosen on the baseline: "According to our pilot study on the" BERT-Base baseline, "we use P@k as the supervision signals on Robust04 and" GOV2, with AP@1000 on ClueWeb09-B.[^c31][^c32] The read text does not report the groupwise model under the other label, so the choice is tuned on one baseline.
- Training uses top-100 documents per query, and testing uses "tested on the last checkpoint with the top-25 documents."[^c33] The document count at test time differs from training, and the grouping of test queries into batches is not described in the read text. Since each query's score is a cross-attention over its batch, the grouping sets its context. My inference: a query's predicted score may depend on which queries it is batched with, and the paper does not measure that sensitivity.
- The "less than 1%" figure covers the groupwise head. For document retrieval with BERT MaxP, passage selection adds "an approx. 1 min extra computational overhead."[^c34]
- Efficiency is left open: "In further research, we plan to" work on it, and nothing here tests a faster variant.[^c35]
- Accuracy is measured under one retriever, query likelihood, "retrieved by the Query Likelihood (QL) model."[^c36] Other retrievers are not tested.

## Related

- [[query-performance-prediction]] — the broader concept; this note is one predictor design within it, here for ad hoc retrieval rather than text-to-image.
- [[metric-specific-ranking-self-consistency]] — also predicts the quality of a ranking from the ranking itself, but from a reranker's own sampled outputs rather than from other queries.

[^c1]: doi-10-48550-arxiv-2204-11489 — "encode each query-document pair with BERT"
[^c2]: doi-10-48550-arxiv-2204-11489 — "Each document used in the next steps is represented by its top-1 ranked"
[^c3]: doi-10-48550-arxiv-2204-11489 — "the [CLS] vectors in a batch are reshaped into a sequence"
[^c4]: doi-10-48550-arxiv-2204-11489 — "which enables the cross attention among the [CLS] vectors in each batch"
[^c5]: doi-10-48550-arxiv-2204-11489 — "we regard each batch as a single group of query-document pairs"
[^c6]: doi-10-48550-arxiv-2204-11489 — "only use the text from individual query-document"
[^c7]: doi-10-48550-arxiv-2204-11489 — "which aim to obtain relative performance among"
[^c8]: doi-10-48550-arxiv-2204-11489 — "Co-BERT [8] incorporates cross-document ranking context"
[^c9]: doi-10-48550-arxiv-2204-11489 — "Inspired by Co-BERT [8], to boost the performance of BERT-based"
[^c10]: doi-10-48550-arxiv-2204-11489 — "pairs are shuffled before being fed into the model in both training and inference"
[^c11]: doi-10-48550-arxiv-2204-11489 — "n queries are grouped together in the batch"
[^c12]: doi-10-48550-arxiv-2204-11489 — "A batch consists of n documents"
[^c13]: doi-10-48550-arxiv-2204-11489 — "groupwise model with all three types of orders mentioned above"
[^c14]: doi-10-48550-arxiv-2204-11489 — "all the baselines on all three collections"
[^c15]: doi-10-48550-arxiv-2204-11489 — "Statistical significance at 0.05 relative to BERT baselines"
[^c16]: doi-10-48550-arxiv-2204-11489 — "(Random order)-base 0.608* 0.449* 0.665* 0.479* 0.481* 0.353*"
[^c17]: doi-10-48550-arxiv-2204-11489 — "0.585 0.423 0.637 0.454 0.447 0.321"
[^c18]: doi-10-48550-arxiv-2204-11489 — "The query-level ranking context marginally"
[^c19]: doi-10-48550-arxiv-2204-11489 — "Using document-level ranking context alone greatly harms the"
[^c20]: doi-10-48550-arxiv-2204-11489 — "the model has only learned the sequence information inside each query"
[^c21]: doi-10-48550-arxiv-2204-11489 — "which is equivalent to the pointwise learning without"
[^c22]: doi-10-48550-arxiv-2204-11489 — "the cross-attention among queries is effective and improves upon the pointwise"
[^c23]: doi-10-48550-arxiv-2204-11489 — "The groupwise method works best with a group size"
[^c24]: doi-10-48550-arxiv-2204-11489 — "less than 1% additional computational cost compared to its BERT counterpart"
[^c25]: doi-10-48550-arxiv-2204-11489 — "of the queries with the actual ordering of average precision for the top 1000"
[^c26]: doi-10-48550-arxiv-2204-11489 — "our proposed predictor is linearly combined with"
[^c27]: doi-10-48550-arxiv-2204-11489 — "with 249, 150 and 200 keyword queries, respectively"
[^c28]: doi-10-48550-arxiv-2204-11489 — "randomly generate 30 splits for each dataset"
[^c29]: doi-10-48550-arxiv-2204-11489 — "fold is used for model training and hyper-parameter tuning"
[^c30]: doi-10-48550-arxiv-2204-11489 — "documents for each query in training due to the small number of queries"
[^c31]: doi-10-48550-arxiv-2204-11489 — "According to our pilot study on the"
[^c32]: doi-10-48550-arxiv-2204-11489 — "we use P@k as the supervision signals on Robust04 and"
[^c33]: doi-10-48550-arxiv-2204-11489 — "tested on the last checkpoint with the top-25 documents"
[^c34]: doi-10-48550-arxiv-2204-11489 — "an approx. 1 min extra computational overhead"
[^c35]: doi-10-48550-arxiv-2204-11489 — "In further research, we plan to"
[^c36]: doi-10-48550-arxiv-2204-11489 — "retrieved by the Query Likelihood (QL) model"
