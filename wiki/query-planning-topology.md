---
description: "Query planning in research agents takes three shapes: parallel sub-queries issued in one pass, sequential ones that adapt to evidence, and tree search over branching decompositions."
aliases: ["query planning structure", "parallel versus sequential query planning", "sub-query planning topology", "planning shape of decomposition"]
sources: ["arxiv-2512-02038"]
---
# Query planning topology

Query planning turns a hard question into work that can be executed. "Query Planning refers to the process of transforming a complex and logically intricate question into"[^q1] a set of sub-queries, each answerable on its own, so that the acquisition of evidence can proceed step by step. The survey's useful move is to sort planners by their shape, that is, by when a sub-query is written relative to the evidence that comes back. Three shapes are distinguished.

In parallel planning the question is decomposed "into independent sub-queries that may be resolved in parallel."[^q2] The sub-queries are produced in one go, before any retrieval has happened. Its advantage is cost: "generation enables parallel processing of sub-queries."[^q3] Its weakness is structural: "they typically operate in a one-shot fashion,"[^q4] so the planner cannot use an intermediate result to change a later query. It also assumes that the sub-queries are independent: they "often ignore data and logical dependencies across sub-queries,"[^q5] and where a later sub-query needs an earlier answer the result can be "ill-posed or unanswerable sub-queries."[^q6]

In sequential planning, "each round of decomposition builds upon the outputs of"[^q7] the rounds before it. The next query is written after the last evidence arrived, which lets a planner handle a chain in which each step depends on the one before: the multi-turn form "allows the sequential planning to perform logically dependent query decompositions that are often intractable for pre-processing planning."[^q8] The price is turns: "excessive reasoning turns or overly long reasoning chains can incur substantial"[^q9] computational cost, and a longer chain can add noise, "potentially causing instability during reinforcement learning training."[^q10]

In tree-based planning each sub-query becomes a node "within a structured search space, typically represented as a tree or a directed acyclic graph (DAG)."[^q11] A search procedure then expands, scores and prunes the nodes. The survey notes that a DAG lets the planner "aggregate intermediate answers along multiple branches,"[^q12] which a single chain cannot do. On my reading the shape subsumes the other two: sibling sub-queries can be issued together, and a branch can be extended step by step.

What survives the move from the survey's examples to a general question is one axis: whether a sub-question may depend on the answer to another. Parallel planning assumes that dependence away, sequential planning builds it into the order of its rounds, and tree planning is described as able to "capture both hierarchical and non-linear dependencies"[^q16] across sub-tasks. Planners are also tuned to the outcome rather than to the decomposition. The survey observes that heuristic or task-agnostic query planning "often suffers from misalignment with end-to-end objectives in downstream applications,"[^q14] and that one reinforcement-learned planner was trained so that "the planner is reinforced only when documents retrieved"[^q13] by its sub-queries let the reader answer correctly.

## Limits

The passage read is a survey of published systems, not a measurement. It names representative works for each shape but, in the part read, gives no controlled comparison of the three shapes on the same questions. The efficiency and accuracy trade-offs stated above are the authors' reading of the cited work, and they are not established here. The cost of tree planning is not discussed in the part read.

The three-way split is a classification, and the survey's own examples blur it: its tree examples include planners that "restructure sequential reasoning traces into a"[^q15] DAG, so a system can sit on a boundary. The shape describes the planner's control flow, not its quality. A parallel planner with a good decomposition can outscore a sequential one with a poor stopping rule; this is my inference, not something the text tests.

## Related

- [[dependency-aware-subquestion-scheduling]] — a ready-set controller over an explicit sub-question dependency graph, one concrete way to run dependent sub-queries without a fixed linear order.
- [[confidence-gated-query-decomposition-tree]] — a tree-shaped decomposition with a per-node rule that answers, splits or extracts, a concrete instance of the tree shape.

[^q1]: arxiv-2512-02038 — "Query Planning refers to the process of transforming a complex and logically intricate question into"
[^q2]: arxiv-2512-02038 — "parallel planning, which decomposes the input into independent sub-queries that may be resolved in parallel"
[^q3]: arxiv-2512-02038 — "generation enables parallel processing of sub-queries"
[^q4]: arxiv-2512-02038 — "they typically operate in a one-shot fashion"
[^q5]: arxiv-2512-02038 — "often ignore data and logical dependencies across sub-queries"
[^q6]: arxiv-2512-02038 — "This can result in ill-posed or unanswerable sub-queries"
[^q7]: arxiv-2512-02038 — "each round of decomposition builds upon the outputs of"
[^q8]: arxiv-2512-02038 — "allows the sequential planning to perform logically dependent query decompositions that are often intractable for pre-processing planning"
[^q9]: arxiv-2512-02038 — "excessive reasoning turns or overly long reasoning chains can incur substantial"
[^q10]: arxiv-2512-02038 — "potentially causing instability during reinforcement learning training"
[^q11]: arxiv-2512-02038 — "typically represented as a tree or a directed acyclic graph (DAG) [51]"
[^q12]: arxiv-2512-02038 — "This design enables the planning to aggregate intermediate answers along multiple branches"
[^q13]: arxiv-2512-02038 — "Crucially, the planner is reinforced only when documents retrieved"
[^q14]: arxiv-2512-02038 — "suffers from misalignment with end-to-end objectives in downstream applications"
[^q15]: arxiv-2512-02038 — "restructure sequential reasoning traces into a"
[^q16]: arxiv-2512-02038 — "capture both hierarchical and non-linear dependencies"
