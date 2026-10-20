---
description: "Two answerers with equal average scores can return disjoint top answers, so a tie in MRR says nothing about which answers were found; an oracle over both bounds their complementarity."
aliases: ["top-k answer overlap", "answer-set overlap", "Jaccard overlap of top-k answers", "oracle combination upper bound", "score parity hides answer divergence"]
sources: ["arxiv-2511-22565"]
---
# Answer-set complementarity

Two answerers can reach the same aggregate score by different routes. A mean reciprocal rank (MRR) averages the rank given to the correct answer over queries, so two methods with the same MRR may place different entities at the top. The question "are they the same answerer?" then has to be asked of the answer sets, not of the averages. Complex query answering over knowledge graphs gives a clean case. The neural methods and the training-free query relaxation baseline, RELAX, reach comparable MRR on several benchmarks, and the paper asks whether they "are arriving at the same answers, or do they achieve similar performance through fundamentally different predictions?"

The measure is the overlap of the two top-k sets. For a query, the authors take the entities each method ranks in its top k and compute the Jaccard similarity of the two sets, which is 1 when the sets coincide. "A value of 0 means that the sets are disjoint."[^c1] The result is that score parity does not come from shared answers: "similar MRR, they do so by ranking different entities highly."[^c2] The overlap depends on query shape. On FB15k237+H and NELL995+H, "for simple query types such as 1p, RELAX and neural models exhibit moderate to high overlap, approaching" high values at large k; "overlap declines substantially" as structures grow more complex (2i, 3p, pi). "For ICEWS18+H, the overlap is much lower."[^c3][^c4][^c5] The authors' conclusion is terse: "Their top-ranked outputs diverge significantly for complex" queries.[^c6]

A second measure asks what the divergence is worth. The oracle combination takes, for each query, whichever method's scores give the higher MRR for that query: "scores from each method that yields the higher MRR for the given query."[^c7] Across the datasets and query types, "the oracle combination consistently achieves higher MRR," and the relative gains reach "with relative gains in the metric reaching 30–50% for several query types."[^c8][^c9] The gains are largest on path queries: "the largest improvements occur for path queries (2p, 3p)"[^c13] The authors read this as relaxation recovering structural connections that the neural models only partly capture.[^c14]

The concept carries two consequences for how answers are compared. First, an aggregate tie is not an identity of answers: a benchmark that reports only MRR cannot say whether the two answerers are substitutes or complements. Second, a per-query selection between two answerers gives a bound on what their combination could add, and that bound can be large where the aggregate scores are equal. The paper states that the oracle is a bound and not a method: "Our combination experiments used an oracle to estimate the theoretical upper bound of complementarity."[^c10]

## Limits

- The oracle reads the true answer to choose, per query, the better of two score lists. It is an upper bound on complementarity, not a combiner. The authors say so: designing realistic fusion "remains an open avenue."[^c11] My inference, not the paper's: with per-query selection over any two methods whose errors vary across queries, the oracle gain will be positive; the number says that the errors differ, and says less about how much a usable rule could recover.
- The paper names the obstacle to a realistic rank-level combination: "devising principled combination methods, as RELAX computes counts, which have a different interpretation."[^c12] A rule that works on counts may not transfer to normalised neural scores, and the text does not test one.
- The overlap is of predicted top-k sets. It is not a measure of which answers are correct, and the paper does not report a correct-answer overlap in the sections read. Whether the two methods agree on the answers that matter is therefore not established.
- Three neural methods, three datasets, one relaxation scheme. The overlap is reported as a figure over k, and the text reads it qualitatively. No confidence interval for the Jaccard values appears in the parts read.
- The combination gains are significance-tested with paired t-tests and Holm–Bonferroni correction.[^c15] That addresses the chance of a spurious gain across methods, not the gap between an oracle and a deployable rule.

## Related

- [[query-relaxation-path-counting]] — the symbolic answerer whose top-k sets are compared here with the neural ones.
- [[complementary-retrieval-signals]] — the same lesson in retrieval: lexical and semantic search miss different evidence, and using both helps. Different component, same logic of complementarity.
- [[complementary-reasoning]] — a different sense of "complementary": parametric and contextual facts used in one chain, not two answerers over one question.

[^c1]: arxiv-2511-22565 — "whereas a value of 0 means that the sets are disjoint."
[^c2]: arxiv-2511-22565 — "similar MRR, they do so by ranking different entities highly."
[^c3]: arxiv-2511-22565 — "for simple query types such as 1p, RELAX and neural models exhibit moderate to high overlap, approaching"
[^c4]: arxiv-2511-22565 — "overlap declines substantially"
[^c5]: arxiv-2511-22565 — "For ICEWS18+H, the overlap is much lower"
[^c6]: arxiv-2511-22565 — "Their top-ranked outputs diverge significantly for complex"
[^c7]: arxiv-2511-22565 — "scores from each method that yields the higher MRR for the given query."
[^c8]: arxiv-2511-22565 — "Across datasets and query types, the oracle combination consistently achieves higher MRR,"
[^c9]: arxiv-2511-22565 — "with relative gains in the metric reaching 30–50% for several query types"
[^c10]: arxiv-2511-22565 — "Our combination experiments used an oracle to estimate the theoretical upper bound of complementarity."
[^c11]: arxiv-2511-22565 — "remains an open avenue."
[^c12]: arxiv-2511-22565 — "devising principled combination methods, as RELAX computes counts, which have a different interpretation"
[^c13]: arxiv-2511-22565 — "the largest improvements occur for path queries (2p, 3p)"
[^c14]: arxiv-2511-22565 — "query relaxation effectively recovers structural connections that neural models"
[^c15]: arxiv-2511-22565 — "Statistical significance is assessed using paired t-tests with Holm–Bonferroni correction for"
