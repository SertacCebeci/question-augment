---
description: "Structural entropy scores a graph by the cost of describing its vertices through nested groupings; minimised over trees of height K, it can score sampled LLM answers as uncertainty."
aliases: ["structural information", "K-dimensional structural entropy", "encoding-tree entropy", "hierarchical structural entropy"]
sources: ["arxiv-2511-16275"]
---
# Structural entropy

Structural entropy is an information measure on the vertices of a graph, read through a tree of nested groupings rather than through the vertices alone. The tool was built for finding structure in graph data: the paper's own framing is that the principle "is widely used to discover the natural hierarchical structure of graph data".[^c1] With no hierarchy, the measure reduces to a degree-based entropy: "the one-dimensional structural entropy of graph G equals to the Shannon entropy of the stationary distribution induced by vertex degrees".[^c2] For a directed graph the degrees are replaced by the stationary distribution π of a random walk on the normalised transition matrix, and "there exists a unique stationary distribution" for an irreducible row-stochastic matrix.[^c3]

The hierarchy enters as an encoding tree. The root holds every vertex, each internal node splits its parent's set into successors, and each leaf holds one vertex. Each non-root node contributes a term built from the weight of edges entering its subset from outside and from the subset's volume relative to its parent. The tree's structural entropy is the sum of these terms. The K-dimensional version restricts the search to trees of height at most K: "we define SeSE as the total entropy of the optimal K-dimensional encoding tree".[^c4] Read this way, the number is the entropy left after the best grouping the height budget allows. The paper's gloss on the quantity is that it "quantifies the inherent uncertainty of the semantic space after optimal compression".[^c5]

## Applied to sampled answers

The paper turns this into a black-box uncertainty score. Sample N answers to one prompt; for each ordered pair, an NLI model gives "the probabilities of entailment, neutrality, and contradiction from the premise to the hypothesis"; those probabilities become directed edge weights; the weights are row-normalised into a transition matrix; its stationary distribution is computed; and a tree is built by repeatedly merging or combining sibling groups, which the paper says is done by "we traverse all sibling node pairs in T and greedily apply" the operators.[^c6][^c7] The score is the entropy of the tree found. The intuition the paper offers is that "Semantic spaces with clear regularities exhibit lower entropy, corresponding to lower uncertainty, while disordered spaces resist compression and yield higher entropy."[^c8]

## Relation to semantic entropy

The formal result is that this family contains [[semantic-entropy]] as a special case. The paper states it as "there exists a semantic graph such that the one-dimensional structural entropy of this graph is equal to semantic entropy".[^c9] The construction starts from the assumption behind SE, that the semantic space "can be perfectly partitioned into disjoint semantic equivalence classes", and builds a quotient graph whose "stationary distribution matches" the cluster probabilities.[^c10][^c11] On that graph, one-layer structural entropy and SE coincide. With K greater than one, the same object "can capture the hierarchical structure of the semantic space through a multi-level encoding tree".[^c12]

What survives the transfer from graph data to answer sets is the compression reading: an answer set that splits into nested, regular groups costs fewer bits than one that resists grouping. What does not survive automatically is the claim that real answer sets have the hierarchy the tree exploits. The paper supports that with illustrations and benchmark gains, not with a separate test of the hierarchy itself.

## Limits

- **Existence, not estimator identity.** The SE result is an existence statement about a constructed graph. It does not say that the NLI graph built from sampled answers reduces to SE under the same conditions. That the practical estimator generalises SE is the paper's framing, and I have not checked it beyond the statement quoted above.
- **Empirical result is a benchmark gain.** The paper reports that "SeSE outperforms baseline methods" over "its superior performance over baselines across 24" model-dataset pairs.[^c13][^c14] The reference label is correctness as judged by a model: "we use the GPT-5-mini model accessed through the OpenAI API to evaluate accuracy".[^c15] The AUROC therefore inherits the judge's error, and the excerpts I read do not show a judge-agreement check.
- **Tree height is a free setting.** The paper shows "performance sensitivity to the encoding tree height K".[^c16] Whether K is set in advance or chosen on the evaluation data is not something I could confirm from the parts I read.
- **The search is greedy.** The algorithm merges and combines by local moves. The excerpts I read give no optimality guarantee for the tree it returns, so the score is the entropy of a locally good tree, not provably the minimum. This is my inference from the algorithm's form.
- **Total uncertainty, not correctness probability.** The score is not a calibrated probability of being right; the text says so: "the latter pertaining to the orthogonal topic of model calibration".[^c17]
- **Cost is sampling plus pairwise entailment.** The pairwise NLI step is the same class of cost as the graph baselines the paper compares against: "Graph-based methods (KLE and SGD) utilize lightweight NLI models to compute entailment scores between responses".[^c18]
- **Untested settings.** The authors leave multi-agent and multimodal settings open: "Future work may explore extending SeSE to multiagent systems and multi-modal LLMs."[^c19]

## Related

- [[semantic-entropy]] — the one-layer special case: a single partition of the answers, with entropy over the cluster probabilities
- [[entropy]] — the Shannon term that the one-dimensional case reduces to
- [[abstention]] — the score is a candidate signal for the abstain-or-answer decision

[^c1]: arxiv-2511-16275 — "widely used to discover the natural hierarchical structure of graph data"
[^c2]: arxiv-2511-16275 — "equals to the Shannon entropy of the stationary distribution induced by vertex degrees"
[^c3]: arxiv-2511-16275 — "there exists a unique stationary distribution"
[^c4]: arxiv-2511-16275 — "we define SeSE as the total entropy of the optimal K-dimensional encoding tree"
[^c5]: arxiv-2511-16275 — "The structural entropy of the resulting encoding tree quantifies the inherent uncertainty of the semantic space after optimal compression"
[^c6]: arxiv-2511-16275 — "the probabilities of entailment, neutrality, and contradiction from the premise to the hypothesis"
[^c7]: arxiv-2511-16275 — "we traverse all sibling node pairs in T and greedily apply"
[^c8]: arxiv-2511-16275 — "Semantic spaces with clear regularities exhibit lower entropy, corresponding to lower uncertainty, while disordered spaces resist compression and yield higher entropy."
[^c9]: arxiv-2511-16275 — "there exists a semantic graph such that the one-dimensional structural entropy of this graph is equal to semantic entropy"
[^c10]: arxiv-2511-16275 — "can be perfectly partitioned into disjoint semantic equivalence classes"
[^c11]: arxiv-2511-16275 — "Construct a semantic quotient graph whose stationary distribution matches"
[^c12]: arxiv-2511-16275 — "can capture the hierarchical structure of the semantic space through a multi-level encoding tree"
[^c13]: arxiv-2511-16275 — "SeSE outperforms baseline methods"
[^c14]: arxiv-2511-16275 — "its superior performance over baselines across 24"
[^c15]: arxiv-2511-16275 — "we use the GPT-5-mini model accessed through the OpenAI API to evaluate accuracy"
[^c16]: arxiv-2511-16275 — "performance sensitivity to the encoding tree height K"
[^c17]: arxiv-2511-16275 — "the latter pertaining to the orthogonal topic of model calibration"
[^c18]: arxiv-2511-16275 — "Graph-based methods (KLE and SGD) utilize lightweight NLI models to compute entailment scores between responses"
[^c19]: arxiv-2511-16275 — "Future work may explore extending SeSE to multiagent systems and multi-modal LLMs."
