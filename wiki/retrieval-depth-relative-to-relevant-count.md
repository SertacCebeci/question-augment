---
description: "Answer quality from retrieved context is best when the depth K is near the relevant count N_p: too few positives starve the answer, too many negatives confuse the model."
aliases: ["K/Np ratio", "retrieval depth ratio", "top-K to relevant-count ratio", "K over Np regime"]
sources: ["arxiv-2512-20854"]
---
# Retrieval depth relative to relevant count

A retrieval system returns the top K documents, and a generator answers from them. The question of how big K should be is usually asked in absolute terms. The paper asks it relative to the number of relevant documents in the base, N_p, and reports that the ratio K/N_p, not K alone, tracks how good the generated answer is. The authors write that "it is generally not known which choice of K will be optimal for a given retrieval."[^d1]

The measurement groups retrieved sets by K/N_p and, within each group, records the distribution of answer scores on a 1-to-5 scale. On ARXIV the pattern is that "the best scored responses occur at values of K which are comparable" to N_p.[^d2] The explanation the authors give is a two-sided one. Below the optimum, "there may not be enough positive texts to give a good response"; above it, "high K/Np there may be too many negative texts," and "within K, which can confuse the LLM and lead" to lower scores.[^d3][^d4]

The optimum moves with the dataset. On MSMARCO the paper reports "a higher “optimal” ratio of NKp than for ARXIV," and the authors speculate that "the reason for this is that" MSMARCO texts are simpler to read, so that extra negatives cost less.[^d5][^d6] The paper says the same shift is "demonstrated to a further extent" on HotpotQA sentences.[^d14] The paper's reading is that the optimal ratio depends on how hard the documents are for the generator, and not on any single fixed K.

The conclusion lists the regime as more important than the embedding: "than the choice of an embedding model when" choosing a retrieval measure, the document type and the ratio "appear to be more important."[^d7] The paper also says that the regime depends on "the choice of K (which may be varied at runtime depending on a query and the retrieved texts)," so K is something a system can set per query rather than a fixed design constant.[^d8]

For the asker and answerer this makes the depth a matter of the expected number of relevant documents. A depth that is right for a query with many relevant documents can be wrong for one with few. The relevant count is what the [[unknown-relevant-total-recall]] note is about: the regime the paper measures is defined by N_p, which a live system usually does not know.

## Limits

- The ratio is observational. The segments are bins of K/N_p over retrieved sets, and the paper keeps only bins with at least 300 samples: "only segments with minimum 300 samples, the ratio NKp is rounded to the first digit."[^d9] The bins are coarse, and the reported optimum is read from them.
- The score is an LLM judgment. The authors report that "The judgment by LLM correlates well with human" judgment, on 96 samples scored by the three authors.[^d10] That is a small human check, and the authors are also the raters.
- The explanation of why ARXIV is harder is the authors' own: "For ARXIV specifically, these scores may be exacerbated due to the difficulty of" the dataset.[^d11] It was not tested as a separate factor.
- The coverage is uneven. For HotpotQA paragraphs the authors say the "range of K/Np for HotpotQA-paragraphs is too" narrow to show the pattern clearly.[^d13]
- Costs were left out. The conclusion says that the useful range of K/N_p also depends on "computation expenses and time lag (growing with K)," which the paper does not measure.[^d12]
- Nothing here gives a rule for choosing K. The paper reports how answer quality varies with the ratio; it does not test a procedure that sets K from an estimate of N_p, and I did not find one in the text.

## Related

- [[unknown-relevant-total-recall]] — the ratio is defined by N_p, and the estimate Fe is one way a system could approach it without labels
- [[top-k-balance-measure]] — a measure that stays defined as K changes, which matters once K is varied per query
- [[retrieval-order-sensitivity]] — at high K/N_p the order of the negatives matters, which the paper uses to explain where nDCG leads

[^d1]: arxiv-2512-20854 — "it is generally not known which choice of K will be optimal for a given retrieval"
[^d2]: arxiv-2512-20854 — "the best scored responses occur at values of K which are comparable"
[^d3]: arxiv-2512-20854 — "enough positive texts to give a good response"
[^d4]: arxiv-2512-20854 — "within K, which can confuse the LLM and lead"
[^d5]: arxiv-2512-20854 — "but with a higher “optimal” ratio of NKp than for"
[^d6]: arxiv-2512-20854 — "We speculate the reason for this is that"
[^d7]: arxiv-2512-20854 — "than the choice of an embedding model when"
[^d8]: arxiv-2512-20854 — "the choice of K (which may be varied at runtime depending"
[^d9]: arxiv-2512-20854 — "only segments with minimum 300 samples, the ratio NKp is rounded to the first digit"
[^d10]: arxiv-2512-20854 — "The judgment by LLM correlates well with human"
[^d11]: arxiv-2512-20854 — "scores may be exacerbated due to the difficulty of"
[^d12]: arxiv-2512-20854 — "computation expenses and time lag (growing with K)"
[^d13]: arxiv-2512-20854 — "range of K/Np for HotpotQA-paragraphs is too"
[^d14]: arxiv-2512-20854 — "demonstrated to a further extent"
