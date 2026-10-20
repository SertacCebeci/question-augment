---
description: "Embedding retrievers score a document differently by where the relevant span sits; most favor the start, one the end, and it is measurable only with document length held fixed."
aliases: ["position bias in dense retrieval", "primacy bias in embedding models", "length-controlled bucketing"]
sources: ["arxiv-2601-08363"]
---
# Embedding-retriever position bias

A dense retriever should judge a document by what it says, not by where the answer-bearing span lies. Zeng et al. (PosIR) test this on 10 embedding models. Their benchmark ties each query to a precise reference span, with 310 datasets over 10 languages and 31 domains.[^c1]

## The measurement design

Earlier analyses moved the relevant information around without controlling document length. A failure on late evidence then confounds two causes: a positional preference, or a capacity limit on long inputs.[^c2] PosIR groups queries by the length of their positive document, in 512-token buckets, and reads positional effects only inside a bucket. The authors claim this isolates position bias from length-induced degradation.[^c3] Positions are then binned as relative positions (20 bins) within the document.

## What was found

- **Primacy is the common shape.** Most models lose retrieval quality as the relevant information moves toward the end of the document.[^c4]
- **Recency exists too.** NV-Embed-v2 shows the opposite skew, toward the end of the document.[^c5]
- **Bias grows with length.** The abstract reports that position bias "even increases with document length", in multilingual and cross-lingual settings.[^c6] In the longest bucket (Q4), models degrade so uniformly that position stops being the main source of score variation. The authors attribute this to failure to encode long documents.[^c7]
- **Architecture does not predict it.** The authors saw no clear link between positional sensitivity and model size, vector dimension, causal versus bidirectional attention, or pooling (CLS, last, mean). They suggest training-data distributions may overshadow these choices.[^c8]
- **Short-text benchmarks miss it.** The Spearman correlation between model rankings on MMTEB and on PosIR is 0.62 (p = 0.05). It is 0.73 for documents up to 512 tokens and 0.39 (p = 0.2) for the longest bucket.[^c9] NV-Embed-v2 and KaLM-Embedding-12B do well on MMTEB and on short documents but degrade in Q3 and Q4. The authors tie this to their short-context training.[^c10]

## A candidate mechanism (exploratory)

The authors compute the gradient of the query-document cosine score with respect to each document token embedding. They do this for 3,131 English pairs whose reference span lies in the middle (relative position 0.4 to 0.6) of documents of 1024 tokens or more. Qwen3-Embedding-8B, a primacy model, shows an extreme saliency peak at the very beginning with sharp decay. NV-Embed-v2 has low sensitivity over the first 20% of tokens and a rise from the midpoint to a peak at the end.[^c11] The authors state the analysis is correlational and that token ablation or positional perturbation would be needed for causality.[^c12]

## Limits

- The mechanism is a hypothesis. The saliency curves are correlational, and the authors only conjecture that the final-position spike comes from last-token pooling.
- Ten models only. The "no architectural correlate" finding rests on that small set, and NV-Embed-v2 is a single recency case.
- Eight of the ten languages are translations. The authors report quality checks, but I did not read those checks.
- Whether the same bias holds for rerankers or for LLM readers is not tested here. The related reader-side result is a separate measurement.
- Retrieval quality was measured with nDCG@10 only. Whether fixing the bias improves downstream answering is not tested.

## Related

- [[reader-slot-zero-primacy]] — primacy among retrieved passages in a reader's prompt, a different locus (slot, not span within a document)
- [[mcq-answer-position-bias]] — position effects on answer options
- [[llm-judge-biases]] — position bias as one systematic bias among several in model judges
- [[interaction-vs-encoding-bias]] — separating where in the pipeline a bias arises

[^c1]: arxiv-2601-08363 — "comprises"
[^c2]: arxiv-2601-08363 — "Second, document length and information"
[^c3]: arxiv-2601-08363 — "This design strictly isolates position bias"
[^c4]: arxiv-2601-08363 — "primacy bias, where retrieval performance degrades as the relevant information"
[^c5]: arxiv-2601-08363 — "exhibits a recency bias skewed towards the end of the document, diverging"
[^c6]: arxiv-2601-08363 — "position bias is pervasive in embedding models and"
[^c7]: arxiv-2601-08363 — "leading to uniformly degraded performance where position bias"
[^c8]: arxiv-2601-08363 — "model size, vector dimension, attention mechanism (bidirectional / causal), or"
[^c9]: arxiv-2601-08363 — "the correlation drops to 0.39 (p = 0.2), indicating no"
[^c10]: arxiv-2601-08363 — "suffer substantial degradation in Q3 and Q4."
[^c11]: arxiv-2601-08363 — "saliency curve for Qwen3-Embedding-8B (Orange) is characterized by an extreme"
[^c12]: arxiv-2601-08363 — "emphasize that the above analyses are correlational."
