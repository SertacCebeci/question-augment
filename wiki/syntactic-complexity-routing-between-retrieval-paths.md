---
description: "A cheap parse-based complexity score routes each question to dense retrieval, graph retrieval, or a score-weighted fusion, because graph retrieval hurts simple questions and costs far more."
aliases: ["EA-GraphRAG", "adaptive GraphRAG routing", "query-complexity routing of retrieval paradigm"]
sources: ["arxiv-2602-03578", "arxiv-2512-09487", "doi-10-48550-arxiv-2606-21553"]
---
# Syntactic complexity routing between retrieval paths

Heavier retrieval machinery is not uniformly better: the right path depends on the question. Graph-augmented retrieval helps multi-hop reasoning, but the paper cites evidence that it "underperforms vanilla RAG on single-hop question-answering, achieving 13.4% lower accuracy on Natural Questions".[^c1] The proposed explanation is that graph retrieval "introduces noise and ambiguities into the retrieved contexts."[^c2] EA-GraphRAG therefore decides per question which path to run, from the question's surface structure alone.

## Mechanism

1. A featurizer parses the query (constituency and dependency trees, entity counts, tree-shape features) and builds a feature vector.[^c3]
2. A small scorer maps it to a continuous complexity score s(q) in (0, 1). It is trained on queries where the two systems disagree: label 1 if graph retrieval is right and dense is wrong, 0 for the reverse. Samples where both agree are dropped.[^c4]
3. Two thresholds tuned on a validation set split the score range: low goes to dense retrieval, high to graph retrieval, and the band between goes to fusion. In the band, reciprocal rank fusion weights the graph side by s(q) and the dense side by 1 - s(q).[^c5]
4. The thresholds maximize a composite of validation accuracy and expected latency, so they set the accuracy-cost trade-off.[^c6]

Measured per-query retrieval time: dense 0.08 s, graph 3.23 s, the router without fusion 1.14 s, the full system 2.19 s. The extra cost of the full system comes mainly from fusion on borderline queries.[^c7] The authors report better accuracy at lower latency than semantic-model routers, because the adapter avoids running a heavy semantic model on every query.[^c8]

The idea for asking and answering: how hard a question is can be read before answering, from its structure, and that reading selects how much evidence machinery to spend. The disagreement-only training label (my inference) means the scorer learns "needs graph" rather than "is hard in general".

A different design moves the choice inside the generation policy. RouteRAG's policy emits a retrieval mode, passage, graph or hybrid, as an action token at each turn, and is trained by reinforcement learning, so the mode follows the reasoning so far rather than a score computed before answering (my reading of the action space).[^c9] The paper reports that adaptive mode choice "yields stronger robustness and generalization than" any single fixed mode, an ablation over the three modes.[^c10] The router is therefore learned from answer reward, not from disagreement labels, and it pays for graph retrieval only through the cost term in [[correctness-gated-retrieval-cost-reward]].

## Limits

- The score is syntactic; a short single-hop-looking question that needs a relation chain will be misrouted. The paper's own datasets (two single-hop, two multi-hop QA benchmarks) are not a test of that.
- The label depends on the particular dense and graph retrievers; the scorer may not transfer to other pairs (my inference, untested).
- Thresholds are tuned per validation set; sensitivity across domains was not established here.
- Cost numbers are retrieval time only, not generation.
- A surface rule can send almost every query to one path. A rule-based router of this kind, which sends queries with named entities, dates or numbers to BM25, was beaten by fixed hybrid retrieval in a text multi-hop QA ablation: "the routing heuristic overroutes to BM25 by firing on named entities".[^c11] The per-path scores of such a router are also hard to read, because it gives the easier queries to one path; the authors take the apparent edge of BM25 to be "the entity heuristic tends to route structurally" simpler queries there, which is their reading and was not separately measured (my reading).[^c12] Whether a learned syntactic score avoids this was not tested in that work.

## Related

- [[ambiguity-versus-incapability-routing]] — another router that picks a response type from an uncertainty signal
- [[cost-aware-module-selection-for-help-queries]] — selecting a module by expected cost
- [[hop-depth-difficulty-with-entropy-check]] — difficulty by hop depth, a different readout of question complexity
- [[correctness-gated-retrieval-cost-reward]] — the in-policy alternative: the mode is picked turn by turn under an RL reward that charges retrieval time

[^c1]: arxiv-2602-03578 — "on single-hop question-answering, achieving 13.4% lower accuracy"
[^c2]: arxiv-2602-03578 — "it also introduces noise and ambiguities into the retrieved contexts."
[^c3]: arxiv-2602-03578 — "We extract features from constituency parse trees using Stanza"
[^c4]: arxiv-2602-03578 — "Samples where both methods agree are excluded from training."
[^c5]: arxiv-2602-03578 — "we use complexity-aware RRF where weights are"
[^c6]: arxiv-2602-03578 — "Thresholds are selected to maximize a composite objective of validation accuracy and expected latency."
[^c7]: arxiv-2602-03578 — "The overhead of the"
[^c8]: arxiv-2602-03578 — "avoiding the need to run an additional"
[^c9]: arxiv-2512-09487 — "allows the model to adaptively choose among passage, graph, and hybrid retrieval"
[^c10]: arxiv-2512-09487 — "yields stronger robustness and generalization than"
[^c11]: doi-10-48550-arxiv-2606-21553 — "the routing heuristic overroutes to BM25 by firing on named entities"
[^c12]: doi-10-48550-arxiv-2606-21553 — "the entity heuristic tends to route structurally"
