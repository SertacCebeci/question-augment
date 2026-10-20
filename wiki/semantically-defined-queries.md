---
description: "Queries where lexical and neural retrievers do oppositely well are where performance predictors fail most, and where a predictor is most needed to choose between the two retriever families."
aliases: ["TIR-NIR divergent queries", "queries where lexical and neural runs disagree", "semantically hard topics"]
sources: ["doi-10-48550-arxiv-2302-09947"]
---
# Semantically defined queries

The paper calls a query "semantically defined" when the two retriever families behave oppositely on it. Operationally these are "those queries where NIR behave, on average, oppositely w.r.t. the TIR, either failing or succeeding at retrieving documents."[^q1] The selection is by disagreement alone. The authors rank the Robust '04 topics by the absolute difference in nDCG@10 between the lexical and the neural systems, averaged within each family, and keep the top quartile, "in the top quartile for the absolute difference in performance (nDCG), averaged."[^q2] That gives 62 topics. Of these, "35 topics are better handled by TIR models, while 27 obtain better nDCG" with neural rankers.[^q3]

The subset is where the predictors break. On the full Robust '04 set the run type has a small effect. On the 62 topics the interaction between predictor and run type "grows from 0.30% to 0.91%", and the run-type effect rises "0.11% to 0.67%", about six times larger.[^q4] The authors' summary: "on the selected topics, arguably those where a QPP is the most useful to help select the right model, using NIR systems has a negative impact (6 times bigger) on the performance of QPPs."[^q5] Restricted to these topics, the pattern "we get similar patterns as those observed for" Deep Learning '19, where the lexical-neural gap is widest.[^q6] The one group that behaves differently is the BERT-based predictors, which do better on neural runs but "are the worst approaches in terms of predictive capabilities for both".[^q7]

The consequence the authors draw is practical. If a predictor cannot tell how a neural retriever will do where it differs from a lexical one, "then a QPP cannot be safely used to carry out model selection."[^q8] The point of a predictor is to choose between systems, and this subset is where the choice is hardest. The same concept is different from the cross-task divergence in [[generation-retrieval-difficulty-divergence]]: there the same prompt is hard for generation and easy for retrieval, while here the same query is hard for one retriever family and easy for another.

## Limits

- The subset is chosen on the outcome it then explains. Taking the top quartile of the very difference between families makes a larger predictor effect on that subset partly true by construction. The paper's own numbers would look like this even if the predictors were no worse on those queries. This is my inference, and the paper does not guard against it.
- The subset is one collection, Robust '04, where the neural models are zero-shot. The paper does not repeat the subset analysis on Deep Learning '19, where the whole collection already shows the pattern.
- "Semantically defined" is the authors' label for retriever disagreement. The selection does not show that these queries are semantically harder in any linguistic sense. The paper cites an earlier study on what makes a query semantically hard, and does not test whether this selection matches it.
- The absolute effects stay small: the interaction reaches 0.91%. The claim is that the effect is several times larger on the subset, not that predictors collapse there.
- The predictor family is the paper's nineteen methods, so the result is not checked against predictors trained for neural retrieval.

## Related

- [[query-performance-prediction]] — the predictors whose failure is measured on this subset.
- [[lexicality-dependent-predictor-transfer]] — why predictors built on lexical signals fit neural runs unevenly, the account that the subset result is consistent with.
- scaled-absolute-rank-error — the per-query measure that the paper uses for these subset analyses.
- [[generation-retrieval-difficulty-divergence]] — another divergence in difficulty, across tasks rather than across retriever families.

[^q1]: doi-10-48550-arxiv-2302-09947 — "those queries where NIR behave, on average, oppositely w.r.t. the TIR, either"
[^q2]: doi-10-48550-arxiv-2302-09947 — "in the top quartile for the absolute difference in performance (nDCG), averaged"
[^q3]: doi-10-48550-arxiv-2302-09947 — "35 topics are better handled by TIR models, while 27 obtain better nDCG"
[^q4]: doi-10-48550-arxiv-2302-09947 — "grows from 0.30% to 0.91%"
[^q5]: doi-10-48550-arxiv-2302-09947 — "has a negative impact (6 times bigger) on the performance of QPPs"
[^q6]: doi-10-48550-arxiv-2302-09947 — "we get similar patterns as those observed for"
[^q7]: doi-10-48550-arxiv-2302-09947 — "but are the worst approaches in terms of predictive capabilities for both"
[^q8]: doi-10-48550-arxiv-2302-09947 — "then a QPP cannot be safely used to carry out model"
