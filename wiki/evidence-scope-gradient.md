---
description: "Retrieval accuracy over personal multimodal histories falls as the evidence a question needs spreads from one concept to a whole history: concept, then event, then aggregated questions."
aliases: ["context scope", "required evidence scope", "scope-graded personalization benchmark"]
sources: ["doi-10-48550-arxiv-2602-19001"]
---
# Evidence scope gradient

Life-Bench sorts personalization questions by how much of a personal history each one must draw on. Its ten tasks are "organized by required evidence scope: concept identification, event understanding, and aggregated reasoning."[^c1] Concept questions concern who is in the user's life and how they relate; event questions concern what happened at a specific time and place; aggregated questions compose evidence across events and time periods.

The scope is a design variable, and its effect on measured accuracy is the finding. Averaged over retrieval methods, accuracy is "average accuracy across retrieval methods ranges from 0.58-0.77 on Concept Identification tasks, but decreases to 0.30-0.57 on Event Understanding and 0.26–0.40 on Aggregated Reasoning."[^c2] The authors describe the mechanism as compounding: "more evidence to compose into a coherent answer."[^c3] Each wider scope adds records to search, modalities to align and evidence to combine, so a retriever that returns the right item for a concept question can still miss most of what an aggregated question needs.

Two parts of the gradient are not only retrieval. On event tasks, with the same backbone, "macro-averaged accuracy over the 4 Event tasks decreases from 0.74 with" oracle evidence to 0.57 with the strongest retrieval configuration, so retrieval accounts for a gap of about 0.17.[^c4] On the aggregated task of frequency and counting, the best retrieval reaches only 0.20, and "Even full-context, which bypasses retrieval, achieves only" 0.38.[^c6] So the gradient is not removed by better retrieval alone.

The scope also decides which retrieval method fits. "No single retrieval paradigm dominates: performance depends on the alignment between the demanded evidence scope and the method’s retrieval" and storage strategy.[^c5] Lexical matching wins where the evidence is a distinctive name or date; a concept-memory method wins on persona questions and collapses on event questions. A question's scope is therefore part of what determines which retrieval strategy will answer it.

## Limits

- One benchmark, ten tasks, one backbone family for the main gap. The gradient is shown on Life-Bench's own category design; the paper does not show that the same scope ordering holds on real archives. Its data are "synthetically generated, enabling public release without exposing real users’ data."[^c7]
- The benchmark does not test change over time. It "does not provide a continual-learning protocol for measuring how systems adapt to incrementally arriving records."[^c8] A scope gradient measured on a fixed, bounded history says nothing about histories that grow.
- The three categories bundle several things: how many records must be found, how many reasoning steps are needed, and how many modalities must be aligned. The paper's gradient cannot say which of these drives the drop. My inference, not the paper's: the scope label is a useful proxy for difficulty, not a measured property of each question.
- Accuracy is averaged over methods and tasks; the ranking of methods reverses across tasks, so a single average gradient hides which method fails where.

## Related

- [[evidence-forgetting-rate]] — the same retrieval-then-generation split; there, retrieval succeeded and generation failed, while here both stages bottleneck and the failure grows with scope.
- source-linked-knowledge-graph — the graph method the paper offers for the wide-scope tasks, where its largest margins appear.

[^c1]: doi-10-48550-arxiv-2602-19001 — "organized by required evidence scope: concept identification, event understanding, and aggregated"
[^c2]: doi-10-48550-arxiv-2602-19001 — "average accuracy across retrieval methods ranges from 0.58-0.77 on Concept Identification tasks, but decreases to 0.30-0.57 on Event Understanding and 0.26–0.40 on Aggregated Reasoning"
[^c3]: doi-10-48550-arxiv-2602-19001 — "more evidence to compose into a coherent answer"
[^c4]: doi-10-48550-arxiv-2602-19001 — "macro-averaged accuracy over the 4 Event tasks decreases from 0.74 with"
[^c5]: doi-10-48550-arxiv-2602-19001 — "No single retrieval paradigm dominates: performance depends on the alignment between the demanded evidence scope and the method’s retrieval"
[^c6]: doi-10-48550-arxiv-2602-19001 — "Even full-context, which bypasses retrieval, achieves only"
[^c7]: doi-10-48550-arxiv-2602-19001 — "is synthetically generated, enabling public release without exposing real users’ data"
[^c8]: doi-10-48550-arxiv-2602-19001 — "continual-learning protocol for measuring how systems adapt to incrementally arriving records"
