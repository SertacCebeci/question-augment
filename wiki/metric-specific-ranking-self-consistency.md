---
description: "An LLM reranker's agreement across sampled rankings, scored with metric-shaped overlap, predicts its ranking quality and is better calibrated than verbalized confidence; stability is not correctness."
aliases: ["reranker-internal QPP", "self-consistency query performance prediction", "RBO-based ranking consistency"]
sources: ["doi-10-48550-arxiv-2606-03535"]
---
# Metric-Specific Ranking Self-Consistency

A sequence-to-sequence LLM reranker emits an ordered list, not a single answer, so answer-level agreement from question answering does not transfer. The paper asks whether the reranker can estimate the quality of the ranking it has just produced ("reranker-internal QPP", query performance prediction).[^c1] Its training-free answer is to sample several rankings and measure how far they agree with the greedy ranking, with the agreement measure shaped like the metric being predicted.

## Mechanism

Consistency on a query is the average agreement between the greedy ranking (temperature 0) and each of N sampled rankings.[^c2] The agreement function is chosen per metric:

- Precision@k: the overlap of the two top-k sets divided by k.
- NDCG@k: a truncated, normalized Rank Biased Overlap (RBO), which weights agreement at shallow depths more (p = 0.9 in the paper).[^c3]
- MRR@k: the reciprocal rank, in the sampled list, of the item the greedy list put first.[^c4]

The premise is that "a model with a clear understanding of ranking should achieve both high self-consistency and strong ranking performance."[^c5]

## What was measured

On TREC Deep Learning 2019 to 2022 with four LLMs, self-consistency was compared with QPP-Gen, an LLM-based unsupervised QPP method that judges each retrieved passage separately. Self-consistency was better calibrated (lower ECE) in almost all cases, and its Spearman correlation with true performance was competitive, better on NDCG@10 but sometimes worse on Precision and MRR.[^c6] The authors explain QPP-Gen's miscalibration by false positives: it judges many irrelevant top passages relevant, and these accumulate when lower ranks matter, as in NDCG.[^c7]

Verbalized confidence from the same reranker, asked to append "Confidence: 0.85" after its list, was severely overconfident: for most samples it exceeded 0.8, and the problem was not mitigated by model size.[^c8] The paper's supervised remedies (Verb-Num, a scalar metric estimate, and Verb-List, an ordered list) reached the best results, Verb-Num often in correlation and Verb-List in ECE, at the cost of only a few extra output tokens.[^c9]

## Limits

- Stability is not correctness. When many relevant passages exist, the model may put different relevant subsets on top in each run, giving high quality but low consistency; the authors say "a model can repeatedly make the same relevance mistake while remaining highly consistent."[^c10]
- It needs several ranking runs, so it is costlier than QPP-Gen's per-passage pass or a verbalized estimate.[^c10]
- Robustness-style variants (perturbing the query and measuring stability) were left untested.[^c11]
- Only TREC DL passage ranking and four LLMs were tested; whether the consistency-to-quality link holds for other ranking tasks is not established here. That the metric-shaped design (rather than a generic overlap) is what helps was not ablated in the slices I read; that is my reading.

## Related

- [[decision-token-extraction-overconfidence]] — another case where a model's own stated or token-level confidence saturates near 1 regardless of correctness
- [[lexical-reranker-sign-diagnostic]] — a different diagnostic of reranker behavior
- [[noise-invariant-verbal-confidence-rules]] — verbalized confidence as a signal and its failure modes

[^c1]: doi-10-48550-arxiv-2606-03535 — "can an LLM reranker estimate the quality of the ranking it has just produced?"
[^c2]: doi-10-48550-arxiv-2606-03535 — "Consistency on a query is computed by the average consistency between the stable greedy ranking Ig and each of the N sampled rankings Is,j ."
[^c3]: doi-10-48550-arxiv-2606-03535 — "we employ"
[^c4]: doi-10-48550-arxiv-2606-03535 — "Mirroring MRR’s sensitivity to the position of the first relevant document"
[^c5]: doi-10-48550-arxiv-2606-03535 — "that a model with a clear understanding of ranking should achieve both high self-consistency and"
[^c6]: doi-10-48550-arxiv-2606-03535 — "Self-consistency is better calibrated than"
[^c7]: doi-10-48550-arxiv-2606-03535 — "incorrectly judges many highly ranked but"
[^c8]: doi-10-48550-arxiv-2606-03535 — "this phenomenon is not"
[^c9]: doi-10-48550-arxiv-2606-03535 — "Verb-Num often achieves the best Spearman correlation, while Verb-List attains the lowest ECE."
[^c10]: doi-10-48550-arxiv-2606-03535 — "A model can repeatedly make the same relevance"
[^c11]: doi-10-48550-arxiv-2606-03535 — "but this would be a separate consistency-based"
