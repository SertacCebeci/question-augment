---
description: "A top-K retrieval score that weighs retrieved positives against retrieved negatives without the total relevant count; it tracked LLM answer quality about as well as F on several datasets."
aliases: ["T measure", "top-K selection measure", "positives-minus-negatives retrieval score", "Np-free retrieval measure"]
sources: ["arxiv-2512-20854"]
---
# Top-K balance measure

A retrieval score is usually a count of what the retriever got right, scaled by something the evaluator must know. The top-K balance measure T takes only what the top K contains. With n_p retrieved positives and n_n = K − n_p retrieved negatives, the paper defines T = (1 − α)·n_p − α·n_n/K, with α in [0, 1].[^t1] The paper says that "where nn =K-np is the number of negative (irrelevant) documents within K."[^t2]

The parameter α sets a trade-off inside the top K: "for T it gives a tradeoff between importance of positives and negatives within K."[^t3] A small α rewards retrieving positives; a large α penalises each negative more heavily, in proportion to its share of K. The point of the design is that T contains no total N_p. The authors say the motivation is "simple removal of unknown Np,"[^t4] which is the step that makes a measure usable where the denominator of recall is missing. The unknown total is described in [[unknown-relevant-total-recall]].

The authors also tested a simpler form without the division by K, which they call T_u. It is equivalent to T up to a change of α, but it "has worse correlations with the response quality score on ARXIV," and the paper's reason for keeping the normalisation is that K can change: the normalisation "should be helpful" when K is "changing ... depending on amount of retrieved texts or their vicinity to the query."[^t5][^t6] Dividing by K therefore matters when the same measure is compared across different cut-offs.

Against F, the reported result is that T "does not lose much in terms of correlations" with the response score, "even though it is formulated without Np."[^t7] The comparison depends on the dataset. The paper reports that T "correlates better with the response score than F on most segments" for ARXIV and HotpotQA-sentences, and is worse on MSMARCO, and that "the difference depends more on the data than on the embeddings."[^t8] Against nDCG, the conclusion is that "the T measure is better" except in the high-ratio regime where nDCG leads on ARXIV.[^t9]

## Limits

- The value of α is chosen by the authors, and the reported correlations are the best value found: "the correlations are given by the maximal values as α is varied within a subset of the data."[^t10] A correlation read at its best α is optimistic for any new collection, and the paper does not report a held-out choice.
- T is not better across the board. For MSMARCO and Natural Questions, the text says "F appears to outperform both T and nDCG for all values of K/Np tested."[^t11] T also "is overtaken by nDCG and F as K/Np increases" on HotpotQA-sentences.[^t12]
- Every correlation is with an answer written and scored by one model, GPT-4o-mini, so the paper does not check T against human judgments of retrieval quality.
- The authors note the measures need relevance labels for the top K, and that latency was left out: "We left out a consideration of the additional latency incurred when evaluating the results of a retrieval in realtime."[^t13]
- The reason T and F diverge on MSMARCO versus ARXIV is not established. The paper reports that the difference depends on the data, and offers no mechanism beyond that.
- The measure counts positives and negatives. It does not register the order of the top K, which the paper's own nDCG results suggest can matter at high K/N_p. That point is my inference from the paper's discussion, not a test of T.

## Related

- [[unknown-relevant-total-recall]] — the missing denominator that T is designed to avoid
- [[retrieval-order-sensitivity]] — nDCG's advantage on ARXIV is read by the authors as an order effect, which a count-based measure like T does not see
- [[recall-only-partial-credit]] — a recall-only score misses over-selection; T's negative term is a count-based answer to the same gap
- [[saturated-performance-measure]] — measure choice can change which system looks best, so a new measure has to be checked against the outcome it predicts

[^t1]: arxiv-2512-20854 — "T = (1 − α)np − α"
[^t2]: arxiv-2512-20854 — "where nn =K-np is the number of negative (irrelevant) documents within K"
[^t3]: arxiv-2512-20854 — "for T it gives a tradeoff between importance of positives and negatives within K"
[^t4]: arxiv-2512-20854 — "it is defined by Equation 3, is simple removal of"
[^t5]: arxiv-2512-20854 — "has worse correlations with the response quality score on ARXIV"
[^t6]: arxiv-2512-20854 — "depending on amount of retrieved texts or their"
[^t7]: arxiv-2512-20854 — "the T measure does not lose"
[^t8]: arxiv-2512-20854 — "more on the data than on the embeddings"
[^t9]: arxiv-2512-20854 — "Except the above, the T measure is better"
[^t10]: arxiv-2512-20854 — "the correlations are given by the maximal values as"
[^t11]: arxiv-2512-20854 — "to outperform both T and nDCG for all values of"
[^t12]: arxiv-2512-20854 — "is overtaken by nDCG and F as K/Np increases"
[^t13]: arxiv-2512-20854 — "We left out a consideration of the additional latency incurred when evaluating the results of a"
