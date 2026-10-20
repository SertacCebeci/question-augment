---
description: "An LLM writes the questions each context could answer, once and offline; a new query is then ranked by its similarity to those stored questions, so no LLM runs at query time."
aliases: ["HyQE", "hypothetical query embeddings", "query-to-hypothetical-query ranking"]
sources: ["doi-10-48550-arxiv-2410-15262"]
---
# Hypothetical query context ranking

Context ranking reorders retrieved contexts by their relevance to a user query. The usual score is the cosine similarity between the query embedding and the context embedding. This work matches at a different place. An LLM is shown a context and asked for the queries it could answer, and the user query is compared with those written queries as well as with the context itself.[^c1] The score adds the two signals with a weight: the direct query–context similarity, plus λ times the highest similarity between the query and any hypothetical query stored for that context.[^c2]

The point of the design is where the LLM is called. "Since the hypothetical queries H(c) are independent of the input q, once H(c) and the corresponding embeddings are obtained, they can be stored and reused for future queries that involve the same context c."[^c3] At query time the work reduces to one query embedding and a short nearest-neighbour search over a context's stored questions. The paper's complexity argument is that generating M questions for each of the |C| contexts is a one-time cost, which "is amortized as the number of input queries increases, making our approach more scalable."[^c4] The contrast is with query-side expansion: "HyDE (Gao et al., 2023a) requires generating a group of hypothetical documents for each query".[^c5]

Why questions rather than hypothetical contexts? The stated reason is causal. Cosine similarity alone "can produce a spurious p(c|q) since c and q being similar does not necessarily imply that c provides answers to q".[^c6] A generated context carries the LLM's prior knowledge into the hypothesis, which the paper treats as an intervention that can create spurious links. A generated question is meant to stay inside the context's scope, because a context "has limited information and can only provide answers to a certain range of queries".[^c7] The paper's conclusion is that cosine similarity "should be applied only when comparing queries with queries".[^c8]

The formula comes from a variational argument. The paper treats context and query as random variables, and "reformulate[s] the ranking problem as a probability inference problem".[^c9] It maximizes an ELBO and approximates the likelihood term by a max over the stored questions, which yields the scoring rule above. A Jensen-bound alternative that averages over the questions instead of taking the max "cannot outperform using Eq.2".[^c10]

What was measured: nDCG@10 on five benchmarks (COVID, NEWS, Touche2020, DL19, DL20). The paper re-ranks the top K = 30 contexts from an initial list of 100, using five embedding models as the baselines.[^c11] Generators were Mistral-7b-instruct, GPT-3.5-turbo and GPT-4o.[^c12] "Our methods outperform the associated baseline embedding models most of the time."[^c13] The paper also reports that the method combines with HyDE retrieval: "HyQE is not only compatible with HyDE but also can further improve the ranking quality beyond that in Table 1."[^c14] On λ, "NDCG@10 decreases as λ increases for most embedding models, suggesting choosing small λ for these models."[^c15]

## Limits

- The amortization is argued from complexity, not from measured latency or cost. The part of the paper read reports no wall-clock timings. Its own limitation section says that "this amortization is built on the premise that the generated queries are stored for future retrieval. And such storage will raise the memory complexity of this framework."[^c16]
- Coverage matters. The score takes a max over the stored questions, so a query worded differently from every stored question gets no benefit from the λ term. Halving the stored questions lowered results: "most of the NDCG@10 scores are slightly lower than those without downsampling".[^c17] Whether a much larger or differently phrased query stream loses this benefit was not tested (my inference from the max).
- The causal account is a derivation with a qualitative check. The paper's support is an ICA projection for four COVID queries, which shows that "the queries are not necessarily adjacent to the contexts that provide answers to them".[^c18] No experiment isolates the causal term from the generation quality.
- Baselines are embedding models only. Document-expansion methods are discussed in related work, but the experiments do not compare against them.[^c11]
- The prompt was tuned by dataset type: "We use the same prompt for all the datasets except for the touche2020 dataset".[^c19] Generalization to a new domain depends on writing a new prompt, and that step is not described as automatic.
- The results are nDCG on five benchmarks with a fixed re-ranking depth. A live corpus that changes over time, where stored questions go stale, was not tested.

## Related

- [[contrastive-hypothesis-retrieval]] — also builds a generated hypothesis for retrieval, but on the query side and per query, the opposite placement from here.
- [[correctness-gated-key-evolution]] — also moves query-side work into the index by storing it on the document side. ERM keeps expansions that proved useful; HyQE generates questions per context from the start and gates nothing.
- [[prompted-versus-trained-query-augmentation]] — rewriting the query with an LLM before retrieval, which needs a model call per query; HyQE calls the LLM on the context instead, so the call is not repeated per query.
- [[pre-generated-qa-bank]] — the same offline question-writing applied to answers: the stored answer is returned directly when a query's question embedding clears a threshold, rather than only used to rank contexts.

[^c1]: doi-10-48550-arxiv-2410-15262 — "generate hypothetical queries based on the existing contexts. It then measures the relevance between the context and a user-given query based on the similarity between the hypothetical queries and the user-given query."
[^c2]: doi-10-48550-arxiv-2410-15262 — "where we introduce a hyperparameter λ to balance the two similarities"
[^c3]: doi-10-48550-arxiv-2410-15262 — "the hypothetical queries H(c) are independent of the input q, once H(c) and the corresponding embeddings are obtained, they can be stored and reused for future queries that involve the same context c"
[^c4]: doi-10-48550-arxiv-2410-15262 — "This complexity is amortized as the number of input queries increases, making our approach more scalable."
[^c5]: doi-10-48550-arxiv-2410-15262 — "HyDE (Gao et al., 2023a) requires generating a group of hypothetical documents for each query"
[^c6]: doi-10-48550-arxiv-2410-15262 — "can produce a spurious p(c|q) since c and q being similar does not necessarily imply that c provides answers to q"
[^c7]: doi-10-48550-arxiv-2410-15262 — "a context has limited information and can only provide answers to a certain range of queries"
[^c8]: doi-10-48550-arxiv-2410-15262 — "cosine similarity should be applied only when comparing queries with queries"
[^c9]: doi-10-48550-arxiv-2410-15262 — "reformulate the ranking problem as a probability inference problem"
[^c10]: doi-10-48550-arxiv-2410-15262 — "cannot outperform using Eq.2"
[^c11]: doi-10-48550-arxiv-2410-15262 — "We use five embedding models as the baselines for ranking"
[^c12]: doi-10-48550-arxiv-2410-15262 — "We use three different LLMs to generate the hypothetical queries"
[^c13]: doi-10-48550-arxiv-2410-15262 — "Our methods outperform the associated baseline embedding models most of the time."
[^c14]: doi-10-48550-arxiv-2410-15262 — "HyQE is not only compatible with HyDE but also can further improve the ranking quality beyond that in Table 1."
[^c15]: doi-10-48550-arxiv-2410-15262 — "NDCG@10 decreases as λ increases for most embedding models, suggesting choosing small λ for these models."
[^c16]: doi-10-48550-arxiv-2410-15262 — "this amortization is built on the premise that the generated queries are stored for future retrieval. And such storage will raise the memory complexity of this framework."
[^c17]: doi-10-48550-arxiv-2410-15262 — "most of the NDCG@10 scores are slightly lower than those without downsampling"
[^c18]: doi-10-48550-arxiv-2410-15262 — "the queries are not necessarily adjacent to the contexts that provide answers to them"
[^c19]: doi-10-48550-arxiv-2410-15262 — "We use the same prompt for all the datasets except for the touche2020 dataset"
