---
description: "Per-item relevance top-K can omit the connector items a joint answer needs; closing the selected set over a dependency graph with a Steiner tree restores them, at a precision cost."
aliases: ["Steiner-tree spanner", "connectivity-preserving subset", "join-closed schema filtering", "structure-closed top-K", "dependency-closed top-K"]
sources: ["arxiv-2512-16083"]
---
# Dependency-closed selection

Choosing what to put in front of a reader or a generator item by item, by relevance to the question, can leave out items that carry no surface link to the question but are needed to combine the chosen ones. In Text2SQL these are key columns: the paper says they are "indispensable for joins and aggregations, yet bear no surface-form relation to the query text", so "retaining them requires structural connectivity rather than purely semantic retrieval".[^c1]

The mechanism the paper builds on this observation runs in three steps. A graph is put over the items, with edges for the declared or predicted dependencies between them (foreign-key links, and links from each non-key column to its table's primary or foreign key). The items are then ranked by relevance to the query. Relevance gives a set of terminals, the top m items, and the task becomes finding a minimal connected subgraph that spans them. Edges between a terminal and a key in the same table cost 0, every other edge costs 1, which favours cheap joins. The subgraph is solved greedily: at each step the cheapest edge is added that reduces the number of connected components. The items this adds beyond the terminals are the connectors, and the selected set is the terminals plus the connectors.[^c2][^c3]

The authors motivate the closure by the fact that a strict top-K cut does not ensure connectivity, even though the top items often already include the needed keys.[^c4] Measured on Spider and BIRD, adding the Steiner expansion to the graph-reranked scores "notably boosts" low-k recall: at k=2, column recall rose from 0.7272 to 0.8100 on Spider, and from 0.4741 to 0.5790 on BIRD.[^c5] The same step cost precision at k=2 (a "modest precision trade-off"), because the connectors are extra candidates.[^c6] Removing both the dependency graph and the Steiner layer gave the steepest fall in k=2 recall (0.7137 on Spider, 0.4705 on BIRD), which the authors read as showing "the value of schema context" beyond the LLM ranker.[^c7]

What survives the move out of databases is the structural point, which is independent of SQL: a set picked by per-item relevance may fail to hold together, and a closure over a dependency structure among the items can recover what was left out. What does not survive is the specific graph. Foreign keys are formal and, in the paper, partly predicted; the analogue of a join between two pieces of a prose context is not given by the paper and is my inference, not tested here.

## Limits

- The closure is measured only as column recall and precision at small k on Spider and BIRD, in the part of the paper I read. The ablation does not report a downstream answer accuracy for the variant without the closure.
- The Steiner stage is described by the authors as "an optional add-on". The paper's main claims rest on the full pipeline, so the closure's own contribution is an ablation, not a separate result.
- The keys are often absent from the database, and the paper predicts them with an LLM (GPT-4.1-mini) where they are missing.[^c8] A wrong predicted edge is followed by the closure as if it were a real join, and no error rate for the predicted edges is reported in what I read.
- The solver is a greedy approximation, not an exact Steiner tree. The authors say it is "sufficient in practice", with no bound or comparison reported.
- The edge costs (0 within a table to a key, 1 otherwise) are a design choice. No sensitivity to them is shown.
- The closure adds items to the set, so it trades recall against precision. Where a generator is hurt by extra context, that cost is not measured in the part read.

## Related

- [[set-level-selection-over-relevance]] — the same complaint about per-item relevance ranking; there the missing property is coverage or non-redundancy scored by rubric, here it is connectivity computed from a dependency graph.
- [[question-rewriting-schema-scaling]] — the same Text-to-SQL setting with a different move: that note compresses the question's reading context before generation, this one selects a connected sub-schema of the context.

[^c1]: arxiv-2512-16083 — "retaining them requires structural connectivity rather"
[^c2]: arxiv-2512-16083 — "Because the Steiner tree is built over the FD graph, every join key"
[^c3]: arxiv-2512-16083 — "that reduces the number of connected components; this is sufficient in"
[^c4]: arxiv-2512-16083 — "not guaranteed under a strict top-𝐾 cut; this stage is an optional"
[^c5]: arxiv-2512-16083 — "recall rises from 0.7272 to 0.8100 on Spider"
[^c6]: arxiv-2512-16083 — "modest precision trade-off at k=2"
[^c7]: arxiv-2512-16083 — "the steepest drop at k=2 recall (0.7137 on Spider, 0.4705 on BIRD)"
[^c8]: arxiv-2512-16083 — "omit explicit primary or"
