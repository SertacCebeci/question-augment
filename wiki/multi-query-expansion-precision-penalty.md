---
description: "In a controlled biomedical RAG benchmark, LLM multi-query expansion lowered contextual precision by 0.138 versus plain dense retrieval and gave no recall gain, when queries were already specific."
aliases: ["multi-query precision paradox", "naive query diversification noise", "RAG-Fusion style expansion cost"]
sources: ["openalex-org-w7160456902", "doi-10-48550-arxiv-2502-13361"]
---
# Multi-query expansion precision penalty

Multi-query expansion has an LLM write alternative phrasings of a question, retrieves for each, merges the results and ranks passages by how many variants retrieved them. In a controlled comparison on 250 BioASQ questions, only the retrieval strategy varied. Embeddings, store, generator, prompt and k=10 were fixed. The expansion used three paraphrases and cross-variant frequency ranking.[^c1]

The outcome ran against its design intent. Contextual precision was 0.671, the lowest of all strategies and 18 points under the best one, outside the confidence intervals of every other strategy.[^c2] Recall did not rise either: 0.839 versus 0.887 for plain dense search.[^c3] Faithfulness was indistinguishable from dense (both 0.897), so the cost landed on what context reached the model, not on how the model used it.[^c4]

The authors' explanation is a hypothesis, not a tested mechanism. The paraphrases pull thematically adjacent passages that are irrelevant to the specific question, and frequency ranking cannot tell relevant passages from generically popular ones, because there is no reranking step.[^c5] A second hypothesis is that the queries were already specific, so there was little ambiguity to resolve and the extra sweeps added mostly noise.[^c6]

My reading (inference, not measured here): expansion helps only to the degree the original query under-specifies its target. When it does not, merging more candidates raises the noise share of a fixed-size context. The paper also notes the cost side, since expansion triples the LLM calls per query.[^c7]

A medical RAG paper reports the reverse for a multi-query scheme. It does not count how many variants retrieved a passage; it averages the similarity of three generated queries, and it reports that removing the multi-query step hurt retrieval as the number of chunks grew.[^c8] The two results differ in fusion rule, corpus and task, so neither tests the other's setting, and the second is a single-benchmark ablation.

## Limits

- One corpus (40,181 passages), one generator, one embedding model, one hyperparameter setting (three variants, one fusion rule); no grid search was run.
- Generator and judge were the same model, so the metrics may favour that model's style.
- The mechanism (adjacent-passage noise, no ambiguity to resolve) is untested; no ablation of the ranking rule or a reranker after expansion was run.
- The authors say the result may reverse for larger corpora or shorter, more ambiguous queries; that was not tested.
- Precision is judged by an LLM, with no human validation.

## Related

- [[query-length-dependent-expansion-prompting]] — expansion's value depends on the query's form, consistent with the ambiguity condition here
- [[prompted-versus-trained-query-augmentation]] — prompted LLM rewriting versus trained rewriting
- [[cross-retriever-reformulation-gain]] — when reformulation helps depends on the retriever
- [[generation-augmented-retrieval]] — score-averaged generated queries, the medical-RAG result that points the other way

[^c1]: openalex-org-w7160456902 — "Passages are ranked by the number of query variants that retrieved them (cross-variant frequency), with document ID as a deterministic tie-breaker"
[^c2]: openalex-org-w7160456902 — "Multi-Query Expansion is the clear outlier, scoring 0.671 [0.630, 0.709]"
[^c3]: openalex-org-w7160456902 — "In practice, recall actually decreases modestly (0.839 vs. 0.887 for Dense), and precision deteriorates sharply."
[^c4]: openalex-org-w7160456902 — "Multi-Query is statistically indistinguishable from Dense (both 0.897)"
[^c5]: openalex-org-w7160456902 — "which then enter the merged context without a reranking step to filter them"
[^c6]: openalex-org-w7160456902 — "there is limited ambiguity to resolve"
[^c7]: openalex-org-w7160456902 — "it triples the number of LLM API calls per query"
[^c8]: doi-10-48550-arxiv-2502-13361 — "Removing the multi-query generation step from CKR causes performance to degrade as N increases"
