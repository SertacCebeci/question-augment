---
description: "A store of triples with no source text can carry multi-hop answers when the question is answered hop by hop over retrieved neighbourhoods; answering in one shot scores clearly lower."
aliases: ["triplet-only question answering", "text-free knowledge graph QA", "KG-only multi-hop answering", "graph-as-sole-evidence QA"]
sources: ["arxiv-2512-00590"]
---
# Text-free triplet answering

Retrieval-augmented systems answer a multi-hop question by reading passages, and a knowledge graph in those systems is usually an index into the passages. The paper tests the other arrangement, in which the graph is the only evidence. The model must "answer factual questions in a textfree setting using only the constructed KG, without"[^t1] access to the source documents. The reading is hop by hop. The question is decomposed, and "each step" is grounded in the graph: the model names the entities it needs, links them to nodes, reads the neighbourhood of the selected nodes, answers the sub-question, and forms the next one from that answer. The loop runs for up to five sub-questions before a final answer.[^t2]

The reported scores are on the paper's own setup. On HotpotQA the triplets-only run reaches 64.5 exact match and 76.0 F1 with gpt-4.1, and on MuSiQue "46.8 EM and 59.8 F1 on MuSiQue."[^t3] The authors read this as showing that "complete and wellstructured symbolic representations of KGs can" serve "as a sufficient and reliable information source" for multi-hop reasoning.[^t4] The comparison class is systems that use text: the scores are "comparable to more resource-intensive systems such as AriGraph and HOLMES that rely on richer textual" context.[^t5]

The part that carries the result is the hop-wise reading, not the store alone. In the ablation, removing the iteration (single-step QA) drops MuSiQue from 55.9 to 43.4 F1 with gpt-4.1-mini. The paper's words: "confirming that multi-hop question decomposition" is needed "for effective reasoning over the constructed KG."[^t6] So a store with the right facts still fails to answer a chain unless the question is walked along it. The mechanism that transfers is the division of labour: the graph supplies the edges, and the question supplies the path through them.

Errors are not recoverable from text here, by design. The authors' QA check is a proxy for graph quality, since "noisy or invalid triplets directly impede correct answers."[^t7] A wrong triplet in the chain cannot be corrected by a passage that was never read. That is an inference from the setup; the paper does not test a text-backed variant of the same graph.

## Limits

- The baselines are the paper's comparison points. Their numbers were not re-run here, and the comparison is made across setups: text-using systems against a triplet-only one.
- The answer entity is present in the graph at two different rates. The abstract gives "the correct answer entity appears in 96% of generated triplets," and the conclusion gives "contains the correct answer entity in 97.5% of cases."[^t8] The two figures are not reconciled in the text read.
- Answer scoring uses the store's own aliases: "using the alias mappings stored in the KG" widens what counts as correct.[^t9] A store that holds more aliases earns more credit, so part of the score measures the store's aliasing rather than its facts.
- Only two multi-hop QA sets, MuSiQue and HotpotQA, and only OpenAI models plus Llama 3.3-70B.[^t10] Whether the result holds for questions whose answer lives only in prose, not in the store, was not tested.
- The ablation drops the iteration, not the graph. No run isolates how much of the score comes from the store versus the reasoning loop.

## Related

- [[external-graph-fact-update]] — the other place a triple store stands in for parametric knowledge; there the store is edited, here it is the only evidence.
- [[compressed-memory-versus-raw-retrieval]] — the same question of whether a compressed store can replace raw records; in that study raw records won.
- [[bridging-question-chaining]] — a multi-hop question grown one hop at a time; the hop-wise answering here is the answering side of the same chain.
- [[ontology-constrained-triplet-validation]] — the construction step that makes the store's facts well typed; the ablation links its removal to lower answer scores.

[^t1]: arxiv-2512-00590 — "using only the constructed KG, without"
[^t2]: arxiv-2512-00590 — "decomposes the question into subquestions, grounding each step in the retrieved KG context"
[^t3]: arxiv-2512-00590 — "46.8 EM and 59.8 F1 on MuSiQue"
[^t4]: arxiv-2512-00590 — "serve as a sufficient and reliable information source"
[^t5]: arxiv-2512-00590 — "to more resource-intensive systems such as AriGraph and HOLMES that rely on richer textual"
[^t6]: arxiv-2512-00590 — "confirming that multi-hop question decomposition"
[^t7]: arxiv-2512-00590 — "or invalid triplets directly impede correct answers,"
[^t8]: arxiv-2512-00590 — "contains the correct answer entity in 97.5% of cases"
[^t9]: arxiv-2512-00590 — "using the alias mappings stored in the KG"
[^t10]: arxiv-2512-00590 — "Our experiments are restricted to proprietary OpenAI models"
