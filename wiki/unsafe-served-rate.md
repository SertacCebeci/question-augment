---
description: "The unsafe-served rate counts wrong cached answers over all queries, not over cache hits, so the safety cost of answer reuse stays visible when hit rates are low."
aliases: ["USR", "wrong-cached-answer rate", "unsafe-served-rate"]
sources: ["doi-10-48550-arxiv-2605-27494"]
---
# Unsafe-served rate

The unsafe-served rate (USR) is the number of queries that received a wrong cached answer, divided by all queries, whether they were served from the cache or not. Shah (2026) defines it as the measure that "directly measures the fraction of all queries that received a wrong cached answer."[^c1] A query counts as unsafe only when the answer came from the cache and disagrees with gold, so a correct cached answer and a regenerated answer both contribute nothing.

The denominator is the point of the metric. The paper's companion quantity is the conditional false-hit rate, FH, and it is defined as a ratio over the same numerator: "FH=USR/aHR is the conditional false-hit rate among served cached answers."[^c2] Here aHR is the answer-cache hit rate. Because FH divides by the hits, a system that rarely serves from the cache can show a modest FH while still putting wrong answers in front of users in absolute terms. The paper's reason for preferring it is that USR is "the only number a production operator can act on."[^c3] My inference from the two definitions is that FH answers "when the cache hits, how often is it wrong," and USR answers "how many of my users got a wrong cached answer." These are different operational questions, and only the second is what the paper calls the safety metric.

On this metric, the paper reports that GroundedCache "drives USR to 0.0% on every HotpotQA regime" against 15–35% for naive semantic caching, and reports a 34× reduction in wrong cached answers per query on the mtRAG document-drift regime.[^c4b] Those figures come from a fixed denominator of N = 200 queries per cell, which the paper uses to argue that USR confidence intervals are tight, unlike the conditional rate.

The metric also has a deliberate blind spot. The retrieval-cache path is excluded from the numerator, because such a hit still regenerates the answer, and the paper says it therefore "cannot return a stale answer" by construction.[^c5] USR therefore measures error in answer reuse only. A wrong retrieval set that still produces a wrong regenerated answer is not counted as cache error.

## Limits

- USR is scored against gold, and only where gold exists. The paper computes exact-match and token-F1 "against gold (when available)."[^c6] For queries with no gold answer, the metric is not defined, and the safety claim does not reach them.
- The disagreement flag is a conjunction, and the paper describes it as one: "A query is flagged as a disagreement when F1 < 0.5" and the normalized gold string also fails to appear in the answer.[^c7] By my reading of this definition, a wrong cached answer with token-F1 at or above 0.5 is not flagged, so USR can undercount wrong answers that share many tokens with gold. The paper does not test this.
- A reported 0.0% at N = 200 is an upper-bound claim, not a zero. The paper's own caveat for small counts applies to the conditional measure: the Wilson 95% upper bound "is non-trivial when k is small."[^c8] My own inference is that a 0/200 result still leaves an upper bound above zero, so the claim of complete elimination is a point estimate.
- The metric was measured on one generator (Qwen2.5-7B-Instruct) and two datasets. Its behaviour under a different generator, a judge-based support check, or a different match rule has not been reported here.

## Related

- [[evidence-validated-answer-reuse]] — the router whose wrong-answer rate this metric scores; the gates are judged by how far they lower USR and how much reuse they give up.

[^c1]: doi-10-48550-arxiv-2605-27494 — "directly measures the fraction of all queries that received a wrong cached answer"
[^c2]: doi-10-48550-arxiv-2605-27494 — "FH=USR/aHR is the conditional false-hit rate among served cached answers."
[^c3]: doi-10-48550-arxiv-2605-27494 — "the only number a production operator can act on"
[^c4]: doi-10-48550-arxiv-2605-27494 — "drives USR to 0.0% on every HotpotQA regime"
[^c4b]: doi-10-48550-arxiv-2605-27494 — "a 34× reduction in wrong cached answers per query"
[^c5]: doi-10-48550-arxiv-2605-27494 — "so by construction it cannot return a stale answer"
[^c6]: doi-10-48550-arxiv-2605-27494 — "against gold (when available)"
[^c7]: doi-10-48550-arxiv-2605-27494 — "A query is flagged as a disagreement when F1 < 0.5"
[^c8]: doi-10-48550-arxiv-2605-27494 — "is non-trivial when k is small"
