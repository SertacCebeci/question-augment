---
description: "Lexical and semantic search miss different evidence; a multi-hop agent that can call both, and is rewarded for using both, loses recall and answer quality when either one is removed."
aliases: ["hybrid retrieval signals", "lexical-semantic complementarity", "multi-signal retrieval tools", "keyword and semantic search together"]
sources: ["doi-10-48550-arxiv-2607-10463"]
---
# Complementary retrieval signals

A retriever ranks text by a score, and the kind of score fixes what it can reach. A lexical scorer such as BM25 rewards exact or near-exact word overlap with the query. A semantic scorer rewards closeness in a learned vector space. The two miss different evidence. The GRASP paper makes this the central difficulty of agentic retrieval: the agent must decide "whether to use lexical matching or semantic similarity" at each step, not once for a whole pipeline.[^c1]

The gap shows up first in single-step retrieval. Across three multi-hop benchmarks, lexical retrieval alone was the weakest option. "Lexical retrieval alone performs substantially worse than semantic or hybrid" retrieval.[^c2] On answer quality the same ordering holds: "hybrid retrieval consistently outperforms lexical and semantic retrieval" among single-step methods.[^c3] The paper's hybrid merges the candidates from both scorers and reranks them, so a single pass already gains from having two signals. The paper's question is different: whether an agent that issues several searches can exploit the two signals across steps.

The agent it trains has three evidence actions: a semantic search, a keyword search, and a read action that returns the parent paragraph of a sentence it found. Its trajectories show a division of labour. The agent often begins broad, "with semantic search" to locate a topic or entity.[^c4] When the lexical result gives a bridge entity, the next search is a keyword query around that entity, and a read action checks the candidate in context before the next hop. The authors describe the pattern as semantic exploration first, lexical refinement second, and verification third. They tie it to human reading: "these patterns resemble human information foraging," with readers who skim for the gist and then scan for specific cues.[^c5]

The reward is where the complementarity is enforced. The complementary-search term is set only "when both semantic and" keyword search retrieve gold evidence, so a policy that leans on one tool earns nothing from that term.[^c6] The term exists to discourage "repeated calls to a single search tool."[^c7] Its weight is small, 0.15 of the total, against the answer term, but it is the only part of the reward that refers to the tool mix.

The ablation tests whether the two signals each carry weight. Removing either search tool lowers both exact match and F1: "dropping either τk or τs reduces both EM and F1."[^c8] The drop is not symmetric. "Removing semantic search leads to a substantially" larger degradation than removing keyword search.[^c9] Under the paper's reading, the keyword tool serves entity-specific evidence and the semantic tool serves the broader search that finds the first hop, so losing the second hurts more.

What transfers is the division of roles, not the exact weights. A question whose evidence is a named entity or an exact phrase is the case where a lexical score can reach what a dense one ranks low; a question about a relation between concepts is the case where the reverse holds. Which of these a given question is, the paper does not test on human askers; that step is my inference from the two roles.

## Limits

- Only one pair of signals was tested: "We use BM25 (Robertson and Zaragoza, 2009) as" the lexical retriever, with a 0.6B dense model as the semantic one.[^c10] The complementarity claim is about these two scorers, not about lexical and semantic search in general.
- The complementary-search term needs gold supporting-fact annotations, since the grounded-reading and complementary terms "both require ground-truth supporting facts for" scoring.[^c11] The mechanism as trained is therefore limited to datasets that carry such labels.
- The single-step hybrid includes a reranker over the merged pool, and the paper's hybrid row does not separate the gain from fusion from the gain from reranking. The reranker is named as "rerank the candidate pool" in its setup.[^c12]
- The result is for one 3B backbone: "our experiments are limited to a single 3B-parameter backbone," and the paper says the dependence on model scale is unclear.[^c13]
- The foraging comparison is an analogy the authors draw. No human readers were tested, and the trajectories were read by the authors, not measured against a foraging model.

## Related

- [[agentic-keyword-search-retrieval]] — a lexical-only agent over a document folder kept most of a vector RAG's answer correctness. Here the keyword tool is the smaller of the two contributions, so the two results do not conflict; they measure different settings.
- [[unsupported-rationale-query-refinement]] — fuses BM25 and a dense retriever in one shot and attributes the gain to complementary evidence without isolating it. The ablation here removes one signal at a time across steps.
- [[recurrent-factual-conceptual-retrieval]] — splits evidence by source, a patient record versus a corpus, rather than by the scoring rule; a second axis on the same division.
- [[query-adaptive-evidence-granularity]] — the grain of evidence, the other axis this agent varies inside its loop.
- [[coarse-to-fine-evidence-zoom]] — the read action is the same two-pass shape: locate a span, then look at its parent in full.

[^c1]: doi-10-48550-arxiv-2607-10463 — "whether to use lexical matching or semantic similarity"
[^c2]: doi-10-48550-arxiv-2607-10463 — "Lexical retrieval alone performs substantially worse than semantic or hybrid"
[^c3]: doi-10-48550-arxiv-2607-10463 — "hybrid retrieval consistently outperforms lexical and semantic retrieval"
[^c4]: doi-10-48550-arxiv-2607-10463 — "The agent often begins with semantic search"
[^c5]: doi-10-48550-arxiv-2607-10463 — "these patterns resemble human information foraging"
[^c6]: doi-10-48550-arxiv-2607-10463 — "We set the reward only when both semantic and"
[^c7]: doi-10-48550-arxiv-2607-10463 — "on repeated calls to a single search tool"
[^c8]: doi-10-48550-arxiv-2607-10463 — "dropping either τk or τs reduces both EM and F1"
[^c9]: doi-10-48550-arxiv-2607-10463 — "removing semantic search leads to a substantially"
[^c10]: doi-10-48550-arxiv-2607-10463 — "We use BM25 (Robertson and Zaragoza, 2009) as"
[^c11]: doi-10-48550-arxiv-2607-10463 — "both require ground-truth supporting facts for"
[^c12]: doi-10-48550-arxiv-2607-10463 — "rerank the candidate pool"
[^c13]: doi-10-48550-arxiv-2607-10463 — "our experiments are limited to a single 3B-parameter backbone"
