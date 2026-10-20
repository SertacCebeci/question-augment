---
description: "Sorting a question by the operations its answer needs (lookup, decomposition, filter-and-aggregate) picks the retrieval pipeline; removing that planning step cost BookRAG the most in ablation."
aliases: ["query category classification", "operation-typed query classes", "single-hop multi-hop global aggregation", "query classification for operator planning"]
sources: ["arxiv-2512-03413"]
---
# Demand-typed query classification

A question can be sorted by what its answer requires the system to do, not by how hard it is. BookRAG, a retrieval method over a structured document index, uses three such classes. A Single-hop query has "a single piece of information retrieved via a Scent-based Retrieval operation" as its need.[^c1] A Multi-hop query needs evidence from several places and is handled "by decomposing into sub-problems".[^c2] A Global Aggregation query "often necessitates analyzing content under multiple filtering conditions", so it needs a filter applied across the document and then a calculation over what passes.[^c3]

The sort matters because it selects the pipeline. The agent first classifies the question, and "based on this classification and a predefined set of operators designed for the BookIndex", it "generates a specific operators plan that effectively guides the retrieval and generation strategies."[^c4] The operators come in four types: Formulator (LLM steps that decompose the query or extract its entities), Selector (filters and subtree selection over the index), Reasoner, and Synthesizer. The authors' claim is that "each category requires a different solution strategy."[^c5] The classes are therefore a way of choosing which operators to compose, so the same question can be answered by a short pipeline or a long one.

What was measured is the cost of not sorting. In the ablation, the variant without planning, "defaulting to a static, standard workflow for all queries",[^c6] was the one whose removal gave "the most significant performance loss" of the modules tested. The authors read this as showing that "a static workflow is insufficient for handling diverse types of queries."[^c7] The experiments are on three long, multimodal document sets, described as "three widely adopted benchmarks".[^c8]

## Limits

- The three classes are the authors' partition, chosen for their benchmarks. The paper says the design is "extensible", allowing "for the resolution of a broader range of query types by integrating" more operators,[^c9] but it does not test whether other partitions of questions do better.
- The "w/o Planning" ablation removes classification and operator choice together. Its loss shows that a static workflow is worse than this planned one; it does not isolate whether the classifier's labels were correct. In the slices I read, no classifier accuracy is reported. That is my inference from the ablation design.
- The labels come from an LLM prompt. How often the label is wrong, and what a wrong label costs, is not shown in the text I read.
- The classes describe the operations a question needs on a document. They say nothing about questions that need no document, or about open-ended answers.

## Related

- [[complexity-tiered-strategy-routing]] — also sorts each query and picks a strategy, but along a difficulty scale that sets how much reasoning to spend; here the sort is by which operations the answer requires, and the output is a pipeline rather than a depth.
- [[syntactic-complexity-routing-between-retrieval-paths]] — routes a question to dense or graph retrieval by a parse-based complexity score, a cheaper proxy for the same retrieval-path choice.
- [[information-scent-patch-navigation]] — the foraging frame behind the Selector operators, which the Single-hop and Global classes call on.
- [[searchwiki-hierarchical-corpus]] — another retrieval agent that chooses which node of a structured corpus to inspect, by granularity.

[^c1]: arxiv-2512-03413 — "a Single-hop query typically requires a single piece of information retrieved via a Scent-based Retrieval operation"
[^c2]: arxiv-2512-03413 — "by decomposing into sub-problems"
[^c3]: arxiv-2512-03413 — "a Global Aggregation query often necessitates analyzing content"
[^c4]: arxiv-2512-03413 — "generates a specific operators plan that effectively guides the"
[^c5]: arxiv-2512-03413 — "each category requires a different solution strategy"
[^c6]: arxiv-2512-03413 — "defaulting to a static, standard workflow for all queries"
[^c7]: arxiv-2512-03413 — "static workflow is insufficient for handling diverse types of queries"
[^c8]: arxiv-2512-03413 — "three widely adopted benchmarks"
[^c9]: arxiv-2512-03413 — "for the resolution of a broader range of query types by integrating"
