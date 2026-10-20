---
description: "Query type, a taxonomy of question kinds, accounts for part of the query-to-query spread in QPP accuracy for dense retrievers, an effect the paper finds absent for BM25."
aliases: ["query-type effects on QPP", "between-query variance in QPP", "sARE linear mixed model"]
sources: ["doi-10-48550-arxiv-2310-11405"]
---
# Query type variance in query performance prediction

Most QPP evaluation reduces a predictor's accuracy to one correlation with effectiveness. An alternative scores each query separately. Faggioli et al. proposed a scaled Absolute Rank Error, "approach based on the scaled Absolute Rank Error (sARE)": for each query, the gap between the rank a predictor gives it and the rank the evaluation metric gives it.[^c1] This replaces a point estimate with a distribution, one error value per query and predictor, "a point estimate prediction approach, as provided by the correlation".[^c2]

The paper then splits that variance by source. Each query has an error for every predictor, so predictor identity is a within-query factor. Each query also belongs to exactly one type, so the type is "query type as a between-query factor".[^c3] A linear mixed effects model carries both: level 1 holds the predictor, and level 2 lets query type shift the intercept and the predictor slope. The share a factor explains is read off as a pseudo-R², the drop in residual or random-effect variance when the factor is added to a nested model (my summary of Section 6).

The types are the six categories of Bolotova et al.'s non-factoid question taxonomy: Evidence-based, Factoid, Experience, Instruction, Reason and Not a Question. The authors "merge the two TREC DL query sets" and assign each query one type.[^c4]

The result depends on the retriever. For BM25 no query-type term enters the fitted models, and "of query type is observed for BM25".[^c5] For the dense retrievers, "the effect of query type is exclusive to dense retrieval".[^c6] The paper reports that the predictor explains 12.4 to 14.6% of the residual variance for TCT-ColBERT and 7.5% to 16.5% for ANCE, "respectively) is explained by differences in predictors".[^c7] The abstract's headline is that query types "are up to 35% responsible for the unstable performance of QPP predictors".[^c8]

The interaction is the practical point. Query types "work well for some predictors but much worse for others".[^c9] For TCT-ColBERT under MAP, the paper finds an interaction with two types, Experience and Reason, which "were found as harder questions" in the original categorisation.[^c10] The conclusion states the claim generally: "the type of query is responsible for a large amount of variance in query performance".[^c11]

## Limits

- Small cells. The analysis pools roughly one hundred TREC DL queries across six types. The per-type counts are not in the part of the paper I read, so the type-level estimates are fragile (my inference).
- Shares, not causes. The percentages are shares of explained variance in one fitted model per retriever and metric, chosen by deviance and significance. "Responsible for" is the paper's phrase for a variance share; it does not say why a type is hard for a predictor.
- The taxonomy is applied as given. Its categories come from a non-factoid study by another group, and the result holds only as far as that labelling is reliable.
- Two dense retrievers and one corpus. The "exclusive to dense retrieval" contrast is among three retrievers. The BM25 sanity check is reported only as "the results were similar" for dense coherence predictors.[^c12]
- The model says the types differ, not which predictor to use for them. The paper's own suggestion is untested: "it would be useful to examine the development of further predictors" for harder types.[^c13]

## Related

- [[query-performance-prediction]] — the task whose per-query accuracy is decomposed here.
- [[coherence-based-performance-prediction]] — the predictors whose per-query errors are analysed in this note.
- [[generation-retrieval-difficulty-divergence]] — another case where difficulty depends on the kind of input, not only on the predictor (my comparison; the two works measure different things).

[^c1]: doi-10-48550-arxiv-2310-11405 — "approach based on the scaled Absolute Rank Error (sARE)"
[^c2]: doi-10-48550-arxiv-2310-11405 — "a point estimate prediction approach, as provided by the correlation"
[^c3]: doi-10-48550-arxiv-2310-11405 — "query type as a between-query factor"
[^c4]: doi-10-48550-arxiv-2310-11405 — "We merge the two TREC DL query sets"
[^c5]: doi-10-48550-arxiv-2310-11405 — "of query type is observed for BM25"
[^c6]: doi-10-48550-arxiv-2310-11405 — "the effect of query type is exclusive to dense retrieval"
[^c7]: doi-10-48550-arxiv-2310-11405 — "respectively) is explained by differences in predictors"
[^c8]: doi-10-48550-arxiv-2310-11405 — "are up to 35% responsible for the unstable performance of QPP predictors"
[^c9]: doi-10-48550-arxiv-2310-11405 — "well for some predictors but much worse for others"
[^c10]: doi-10-48550-arxiv-2310-11405 — "Experience and Reason were found as harder questions"
[^c11]: doi-10-48550-arxiv-2310-11405 — "the type of query is responsible for a large amount of variance in query performance"
[^c12]: doi-10-48550-arxiv-2310-11405 — "the results were similar"
[^c13]: doi-10-48550-arxiv-2310-11405 — "it would be useful to examine the development of further predictors"
