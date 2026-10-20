---
description: "Recall needs the total count of relevant documents, which a changing knowledge base does not reveal; evaluation then uses fixed labels, an estimate of that count, or a measure that omits it."
aliases: ["unknown recall denominator", "unknown total relevant count", "recall without the relevant total", "Np-free evaluation"]
sources: ["arxiv-2512-20854"]
---
# Unknown relevant total

Recall is the share of all relevant documents that a retriever returned. Its denominator is the total number of relevant documents in the knowledge base, and an evaluator often does not have that number. The paper states the situation as "documents relevant to a query is typically unknown, and recall cannot be computed."[^u1] In a changing knowledge base the total "is not known in advance for an arbitrary query," so recall is unknown as well.[^u2]

The F measure combines precision and recall, so it inherits the problem. The paper writes F with the number of retrieved positives, the cut-off K and the total N_p, and its denominator is "αK + (1 − α)Np".[^u3] The paper also says that F "requires knowing Np, which can be achieved by labeling" part of the base.[^u18] Without N_p, F cannot be computed for a query at all.

The paper lists the routes that get around the missing denominator.[^u4] The first is a fixed benchmark: a labelled subset of the base that is kept as it is, and so "is fixed and must be recreated" when the base changes.[^u17] The second is to estimate the total for each query, by pooling, by extrapolating the count to a larger K, or by capture–recapture. The third is to use a measure that never contains the total: "Using an evaluation measure that does not include the total number of relevant documents."[^u5] The paper tests nDCG as a member of this third group, and its own measure T, written up in [[top-k-balance-measure]].

The estimating route has a cheap variant. Fe is F with the total replaced by the number of positives found in the top 2K: "positives in the top 2K rather than the total number."[^u6] The authors favour it because a more careful estimate may fail at low totals: an estimate "by a capture-recapture method may be too crude."[^u7] Its footing is that the top 2K holds enough positives to stand in for the total, which is more likely when N_p is small relative to K.

The surprising result is that at high K/N_p the estimate does better than the true total: "an estimated Np serves better than the real Np."[^u8] The authors suspect the cause lies in the documents. The relevant ones in the top 2K "are more important and should" count more than the rest, and that is why the estimate can outdo the count.[^u9] This is their suspicion. The paper does not test it.

What the paper measures is agreement with a downstream outcome, not with recall itself. Each candidate measure is correlated with an LLM-scored answer built from the same top K, so a measure is judged by whether it "correlates with an LLM-scored quality of a response."[^u10] For someone building or auditing a retrieval system, the practical reading is that a recall-type score needs labels for the whole base, and the alternatives trade that cost for a different kind of error.

## Limits

- The regime is narrow. The abstract reports experiments on datasets "with a relatively low number of relevant documents (2–15)."[^u11] The authors add that their experiments "focus on retrieval scenarios with relatively moderate ranges of Np, which may limit the applicability of our findings to broader retrieval regimes."[^u12]
- Every measure needs relevance judgments for the retrieved set. The paper says so directly: "The measures (even not involving a knowledge of Np) require identifying relevancy of the top-K documents with respect to a query."[^u13] Its own labels come from an LLM, "method of obtaining labels is by using an LLM."[^u14] The same model, GPT-4o-mini, both writes the responses and scores them.[^u15]
- The advantage of Fe at high K/N_p was seen mainly on ARXIV and MSMARCO. The authors say that "The comparisons on other datasets are more limited, and shown" in the appendix.[^u16]
- The cause of Fe's advantage is a suspicion offered by the authors. Nothing in the text tests it, and the claim that the estimate beats the true total should be read as one measured pattern on a few datasets.
- A correlation with an LLM-scored response is evidence about usefulness for generation. It is not a check that the measure equals recall.

## Related

- [[label-sparsity-lower-bound]] — incomplete labels also undercount correct items; there the labelled set is of pairs in recommendation, while here the denominator of recall itself is missing.
- [[weighted-nugget-recall]] — a fixed gold set caps what a metric can credit, the fixed-benchmark route in another task.
- [[recall-only-partial-credit]] — a recall-only score cannot see extra wrong picks, which a count-based balance of positives and negatives is meant to catch.
- [[saturated-performance-measure]] — the choice of ground-truth measure can change which predictor looks best, so the choice of a Np-free measure is not neutral either.
- [[top-k-balance-measure]] — the Np-free measure T that the paper proposes in place of recall.
- [[retrieval-depth-relative-to-relevant-count]] — the regime in which F and Fe are compared is set by K/N_p, which needs N_p.

[^u1]: arxiv-2512-20854 — "documents relevant to a query is typically unknown, and recall cannot be computed"
[^u2]: arxiv-2512-20854 — "is not known in advance for an arbitrary query"
[^u3]: arxiv-2512-20854 — "αK + (1 − α)Np"
[^u4]: arxiv-2512-20854 — "There are several ways to circumvent the lack of"
[^u5]: arxiv-2512-20854 — "Using an evaluation measure that does not include the total number of relevant documents"
[^u6]: arxiv-2512-20854 — "positives in the top 2K rather than the total number"
[^u7]: arxiv-2512-20854 — "by a capture-recapture method may be too crude"
[^u8]: arxiv-2512-20854 — "an estimated Np serves better than the real Np"
[^u9]: arxiv-2512-20854 — "are more important and should"
[^u10]: arxiv-2512-20854 — "it correlates with an LLM-scored quality of a response"
[^u11]: arxiv-2512-20854 — "number of relevant documents (2–15)"
[^u12]: arxiv-2512-20854 — "relatively moderate ranges of Np , which may limit"
[^u13]: arxiv-2512-20854 — "The measures (even not involving a knowledge of Np ) require identifying"
[^u14]: arxiv-2512-20854 — "method of obtaining labels is by using an LLM"
[^u15]: arxiv-2512-20854 — "GPT-4o-mini for both generating and scoring the"
[^u16]: arxiv-2512-20854 — "The comparisons on other datasets are more limited, and shown"
[^u17]: arxiv-2512-20854 — "The subset is fixed and must be recreated"
[^u18]: arxiv-2512-20854 — "which can be achieved by labeling"
