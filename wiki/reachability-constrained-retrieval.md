---
description: "Retrieval first keeps only the nodes reachable from an anchor in a graph, then ranks them by similarity; the restriction makes structural consistency hold by construction, not by ranking."
aliases: ["Path-Constrained Retrieval", "PCR", "anchor-reachable retrieval", "graph-reachable candidate restriction"]
sources: ["arxiv-2511-18313"]
---
# Reachability-constrained retrieval

Similarity search ranks every item in a store by how close it lies to the query. Reachability-constrained retrieval changes the set before the ranking. It first finds the nodes that can be reached from an anchor node along a graph's directed edges, and then ranks only those by similarity to the query. The formulation is explicit: "PCR restricts the candidate set to nodes reachable from the anchor before performing semantic search."[^c1] The reachable set is found by breadth-first search from the anchor, optionally cut at a maximum depth. The first step of the algorithm is "Compute the set of nodes reachable from anchor a using" breadth-first search, and the last is a top-k ranking over the restricted set.[^c2] Reachability is a directed path: the relation is "the existence of a directed path from anchor a to node v".[^c3]

The mechanism is a gate, not a preference. A node's membership in the reachable set is a precondition for retrieval, so no amount of semantic closeness admits a node the anchor cannot reach: "any node that is not reachable from the anchor cannot be retrieved, regardless of semantic similarity."[^c4] This is the difference from a [[structural-neighborhood-expansion|structure-aware ranker]] that widens a pool and then re-scores it. Here the structure only removes candidates; the similarity ranker never sees them. The paper compares this against vector search, BM25 and a weighted hybrid, and those three baselines carry no structural filter: "We compare PCR against three baseline methods."[^c5]

The gate is also the metric. Structural consistency is defined as the "Fraction of retrieved nodes that are reachable from the anchor."[^c6] The reported result follows: "PCR achieves 100% structural consistency, compared to 24% (Vector), 24% (BM25), and 32% (Hybrid) in baseline methods."[^c7] My reading is that this 100% is a consequence of the gate and not a finding about retrieval. What the experiment can measure is what the gate costs, and the paper reports that cost in relevance: "The slight reduction in overall relevance (70% vs 72-80% in baselines) is a reasonable trade-off for achieving perfect structural consistency."[^c8] The word "slight" is the paper's own judgement.

Where the gate bites depends on the graph. In a densely connected graph the reachable set may be most of the graph, and the constraint removes little. The paper's own caveat is that "In domains with disconnected graph components, PCR may retrieve fewer results than baselines, potentially reducing recall."[^c9] A fallback to global search exists for the case of no reachable nodes, but it is discouraged: "However, this should be used sparingly as it defeats the structural constraint purpose."[^c10]

The depth limit is a second knob. Capping the maximum path length d_max narrows the reachable set further. On the technology domain the depth ablation shows relevance at 1.00 for every depth from 2 to unlimited, and 0.90 at depth 1; the average distance penalty falls from 0.16 (unlimited) to 0.10 (depth 1). The paper's summary is that "Depth limits of 2-3 hops provide a good balance, with slightly lower distance penalties."[^c11]

## Limits

- **The headline number is not a test.** Because the gate defines the metric, 100% structural consistency shows the gate works, not that retrieval is better. The metric that could fail is relevance, and there the margin is small: the paper reports 70% overall against 72-80% for the baselines.[^c8]
- **The distance penalty is partly built in.** A constraint that forbids far nodes will lower the average distance of what is retrieved. The paper argues the lower penalty "is important for multi-hop reasoning, where maintaining coherent reasoning chains requires information from nearby nodes in the graph."[^c12] No reasoning outcome is measured. The paper itself lists "integration with reasoning frameworks for end-to-end evaluation" as future work.[^c20]
- **Anchor and graph dependence.** "Poor anchor choices can lead to limited or no reachable relevant nodes."[^c13] "Sparse or poorly connected graphs may limit retrieval effectiveness."[^c14] If the relevant nodes are not reachable from the anchor, the gate removes them and no ranker can recover them. This is my reading of the mechanism, and the paper's caveats point the same way.
- **Thin evidence.** "Our evaluation uses synthetic data with 30 nodes per domain."[^c15] The benchmark has "120 queries (20 per domain for tech, 2 per domain for others)."[^c16] Per-domain numbers rest on two queries in five of six domains. With k = 10 over 30 nodes, Relevance@10 returns a third of the domain, so the metric is coarse at this scale. This is my inference.
- **The advantage over vector search is not significant at the usual level.** The abstract says the method is "significantly outperforming vector search (p=0.09)",[^c21] but the paper's own wording is "The comparison with Vector search shows marginal significance."[^c17] The hybrid comparison (p=0.017) is the one that clears 0.05.
- **No graph-aware baseline.** The paper says that graph methods such as GraphRAG "do not explicitly constrain retrieval based on graph reachability,"[^c18] but it does not run any of them. Whether a reachability gate beats a graph-aware retriever is untested.
- **Cost at small scale only.** Reachability adds "approximately 2-5ms per query"[^c19] on a 30-node-per-domain benchmark. Behaviour on large graphs is not measured.
- **Scope.** This note concerns which evidence an answerer is handed. It says nothing about how a question is formulated or selected. That is my inference from the paper's setting, which is retrieval for an LLM agent's reasoning.

## Related

- [[structural-neighborhood-expansion]] — the opposite move on a similar graph: there seeds widen the pool to admit near-misses under a fixed budget, here the anchor's reachable set narrows the pool to a gate.
- [[candidate-set-restriction-conformal-prediction]] — another hard restriction of candidates; there validity holds only while the true answer stays inside the restricted set. My reading is that the same dependence holds here: the gate is safe only when the relevant nodes lie inside the reachable set.
- [[semantic-proximity-bias]] — similarity-first retrieval is the ranker this gate is placed in front of; the gate supplies a structural rule that a similarity ranker cannot apply by itself.

[^c1]: arxiv-2511-18313 — "PCR restricts the candidate set to nodes reachable from the anchor before performing semantic"
[^c2]: arxiv-2511-18313 — "Compute the set of nodes reachable from anchor a using"
[^c3]: arxiv-2511-18313 — "path(a, v) denotes the existence of a directed path from anchor a to node v"
[^c4]: arxiv-2511-18313 — "any node that is not reachable from the anchor cannot be retrieved, regardless of semantic similarity"
[^c5]: arxiv-2511-18313 — "We compare PCR against three baseline methods"
[^c6]: arxiv-2511-18313 — "Fraction of retrieved nodes that are reachable from the anchor"
[^c7]: arxiv-2511-18313 — "PCR achieves 100% structural consistency, compared to 24% (Vector), 24% (BM25), and 32% (Hybrid) in baseline methods"
[^c8]: arxiv-2511-18313 — "The slight reduction in overall relevance (70% vs 72-80% in baselines) is a reasonable trade-off for achieving perfect structural consistency"
[^c9]: arxiv-2511-18313 — "In domains with disconnected graph components, PCR may retrieve fewer results than baselines, potentially reducing recall"
[^c10]: arxiv-2511-18313 — "this should be used sparingly as it defeats the structural constraint purpose"
[^c11]: arxiv-2511-18313 — "Depth limits of 2-3 hops provide a good balance, with slightly lower distance penalties"
[^c12]: arxiv-2511-18313 — "This is important for multi-hop reasoning, where maintaining coherent reasoning chains requires information from nearby nodes in the graph"
[^c13]: arxiv-2511-18313 — "Poor anchor choices can lead to limited or no reachable relevant nodes"
[^c14]: arxiv-2511-18313 — "Sparse or poorly connected graphs may limit retrieval effectiveness"
[^c15]: arxiv-2511-18313 — "Our evaluation uses synthetic data with 30 nodes per domain"
[^c16]: arxiv-2511-18313 — "The benchmark includes 120 queries (20 per domain for tech, 2 per domain for others)"
[^c17]: arxiv-2511-18313 — "The comparison with Vector search shows marginal significance"
[^c18]: arxiv-2511-18313 — "these approaches do not explicitly constrain retrieval based on graph reachability"
[^c19]: arxiv-2511-18313 — "approximately 2-5ms per query"
[^c20]: arxiv-2511-18313 — "integration with reasoning frameworks for end-to-end evaluation"
[^c21]: arxiv-2511-18313 — "significantly outperforming vector search (p=0.09)"
