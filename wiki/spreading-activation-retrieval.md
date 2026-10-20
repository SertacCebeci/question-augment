---
description: "Spreading activation retrieves multi-hop evidence by propagating weight from query-matched entities through a document-entity graph, reaching bridge documents the query never names."
aliases: ["spreading activation search", "activation spreading", "SA retrieval"]
sources: ["arxiv-2512-15922"]
---
# Spreading activation retrieval

Spreading activation (SA) is a search over an associative network. Starting nodes get activation 1, and each node passes activation to its neighbours in proportion to the weight of the link between them, so relevance reaches nodes that are linked to the query's matches without sharing its words. In the retrieval setting studied here the network is a knowledge graph built over a document corpus: chunks of text are nodes linked to the entities they mention, and entities are linked to one another by typed relations.[^c1] The query first picks seed entities by embedding similarity. Each link is weighted by the cosine similarity between the query and the link's embedding, and the weights are rescaled linearly with c = 0.4 so that activation does not saturate the graph.[^c2] Algorithm 1 then runs a breadth-first queue over the subgraph, adding each node's activation times link weight to its neighbours, and keeps the entities that end above a threshold of 0.5.[^c3] As the pseudocode is written, a visited set means each node is expanded once, so the spread is one bounded pass rather than a run to convergence; that is my reading of the algorithm, not a claim the paper makes. Documents are then fetched through the activated entities and pruned by a second similarity threshold.[^c4]

The mechanism's point is the bridge. A document whose entities are absent from the question can still be reached by a chain of links from the seeds. The paper's motivating example needs five entities along a path between two named places, and it argues that SA collects them where Personalized PageRank and closeness centrality do not.[^c5] That is one worked example, not a measurement.

The constraints are part of the mechanism, not tuning noise. The paper cites earlier work showing that unconstrained spreading "converges to a fixed state and retrieval results become" nearly independent of the query.[^c6] Hop limits, fan-out, thresholds and decay are what keep the output query-dependent.

What survives the transfer from cognitive psychology is the propagation with decay and a threshold. The original psychological use, which the paper traces to verification experiments, claimed that "longer network traversals correlate with slower verification times".[^c7] The retrieval paper does not test that claim and does not use it.

On the measured side, the paper reports SA as a standalone retriever on two multi-hop QA sets, MuSiQue and 2WikiMultiHopQA, with 100 sampled questions each. "In experiments with the phi4 model, SA-RAG alone" matched or beat the iterative baselines it was compared with, and was comparable to HippoRAG 2.[^c8] With gemma3 the order reverses: "With gemma3, however, HippoRAG 2 outperformed SA-RAG on both".[^c9] The larger effect is as a plug-in to iterative retrieval: "SA-RAG with CoT retrieval yields the strongest performance, substantially outperforming all baseline RAG approaches".[^c10]

## Limits

- Scale. The evaluation uses 100 questions per benchmark, and the authors say "More extensive validation is needed to empirically demonstrate the scalability of" the system.[^c11]
- Dependence on the reasoner. The gemma3 result shows the retrieved context can be adequate while the gain disappears; the authors suggest "the absence of similar improvements was not due to missing" context and point to the model's reasoning instead.[^c12] Whether the gain transfers to other readers is not tested.
- Precision. The paper notes that SA "exhibits a tendency to" give high relevance to entities that are not part of the answer path, which raises the risk of false positives.[^c13]
- Weights. Link weights come from an off-the-shelf embedding model, "adapted them only through simple linear scaling for our" task, and the authors list fine-tuning the embedder as future work.[^c14]
- Tuning. The constants (c, the thresholds, k and n) were chosen "by experimenting on multiple small samples of approximately 10 questions" and then fixed for the reported runs.[^c15]
- Reported size of the gain. The abstract says the CoT combination "yields up to a 39% absolute improvement in answer",[^c16] while the contributions call the range "absolute improvements in answer accuracy ranging" and then give "from 25% to 39% relative to naive RAG".[^c17] The same number is read two ways in the text, so the size of the gain should be taken as the paper's claim, not a settled figure.
- Baselines are training-free and the models are small and open-weight. Nothing here compares SA against a fine-tuned retriever.

## Related

- [[evidence-guided-query-reformulation]] — another route to bridge evidence: revising the multi-hop query from passages already read, where SA instead changes which passages are reached from the graph
- [[retrieval-reasoning-procedure]] — the retrieve-reason loop that SA is combined with as a plug-in module
- [[stop-continue-criteria-in-retrieval-loops]] — the iterative loop's stopping rule, which governs how many SA-expanded retrievals a chain-of-thought run makes

[^c1]: arxiv-2512-15922 — "We construct a knowledge graph containing three types of nodes: entities, entity descriptions, and documents (which"
[^c2]: arxiv-2512-15922 — "This adjustment helps prevent overactivation, which could otherwise result in nearly every node"
[^c3]: arxiv-2512-15922 — "exceeds the threshold τa are marked as activated"
[^c4]: arxiv-2512-15922 — "consisting of document nodes that have outgoing describes links connecting them to the activated entity nodes"
[^c5]: arxiv-2512-15922 — "in our example only SA collects all of the golden entities"
[^c6]: arxiv-2512-15922 — "outgoing links with no limits on hops, fan-out, or thresholds, converges to a fixed state and retrieval results become"
[^c7]: arxiv-2512-15922 — "showing that longer network traversals correlate with slower verification times"
[^c8]: arxiv-2512-15922 — "in experiments with the phi4 model, SA-RAG alone"
[^c9]: arxiv-2512-15922 — "With gemma3, however, HippoRAG 2 outperformed SA-RAG on both"
[^c10]: arxiv-2512-15922 — "SA-RAG with CoT retrieval yields the strongest performance, substantially outperforming all baseline RAG approaches"
[^c11]: arxiv-2512-15922 — "More extensive validation is needed to empirically demonstrate the scalability of"
[^c12]: arxiv-2512-15922 — "suggests that the absence of similar improvements was not due to missing"
[^c13]: arxiv-2512-15922 — "assign high relevance scores to non-golden entities, raising the risk of false positives"
[^c14]: arxiv-2512-15922 — "adapted them only through simple linear scaling for our"
[^c15]: arxiv-2512-15922 — "By experimenting on multiple small samples of approximately 10 questions"
[^c16]: arxiv-2512-15922 — "it yields up to a 39% absolute improvement in answer"
[^c17]: arxiv-2512-15922 — "our method yields absolute improvements in answer accuracy ranging"
