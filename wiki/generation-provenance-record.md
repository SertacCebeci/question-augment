---
description: "A generated question is stored with the graph path, evidence, configuration and review history that produced it, so its settings can be read back and the item audited later."
aliases: ["provenance record of a generated item", "derivation record", "generation lineage", "provenance completeness"]
sources: ["arxiv-2512-01045"]
---
# Generation provenance record

A generated question-answer item can travel as a bare pair of strings, or with the derivation that produced it. Med-CRAFT keeps the second form: each final sample "stores not only the generated textual content, but also the graph path, evidence segments, provenance chain, configuration parameters, quality scores, and review status."[^c1] The record is what lets a reader of one item ask where it came from: which source video and time segment its evidence was bound to, which traversal configuration set its hop count and visual dependency, and which review accepted it.

The idea is imported from data provenance in databases and workflows, where "derivation histories are essential" for accountability and debugging.[^c2] The transfer is partial. What survives is the chain from an output back to its inputs and settings. What does not obviously survive is the database assumption that re-running a job returns the same rows. A pipeline that calls a language model is re-run with fixed inputs, configurations, seeds and model versions,[^c7] and the paper reports "agreement rates" for graph artifacts, reasoning chains, QA pairs and provenance records.[^c8] Whether that agreement falls short of identity is my inference; the text read does not say.

What the record makes measurable is provenance completeness: the proportion of accepted items for which the system "can recover the source" video, segment, cues, graph path, configuration, model version and review history.[^c3] On the full configuration the paper reports, among other figures, "provenance completeness of 0.98".[^c4] Under normal execution the system "achieved lineage success of 0.99, provenance completeness of 0.98,"[^c5] and under an injected storage interruption the figures fall, "reducing lineage success to 0.90, provenance completeness to 0.90".[^c6]

Why this sits with question generation: once the hop count and the visual-dependency setting are stored with the item, a difficulty claim about a dataset can be checked item by item against the configuration that was requested, rather than taken from a run summary. This is my inference from the paper's configuration-profile design, not a result the paper reports. It is the construction-time counterpart of the answer-side audit in [[traceable-evidence-chain]].

## Limits

- Every number here is the authors' own measurement on their own system and runs. The text read contains no outside audit that a recovered record matches what actually happened.
- Completeness is recoverability, not correctness. A full record shows where a sample came from; it does not show that the evidence entails the answer. The same line that reports completeness reports evidence entailment separately, at 0.94 for the full system.[^c4]
- The text read has no run without the record to compare with, so it does not show that storing the configuration changes how items are selected, reviewed or used.
- The record is only as complete as the storage under it, and the fault runs show it degrading when storage fails.[^c6]
- The measured system is one pipeline on medical instructional video. Other domains and other generators are not tested.

## Related

- [[traceable-evidence-chain]] — audits an answer's claims against retrieved sources at answer time; this note is the construction-time derivation of a generated item.
- [[evidence-chain-question-generation]] — has the question-writer build an evidence chain before writing the question; a record would keep that chain after the question exists.
- [[hop-depth-difficulty-with-entropy-check]] — sets item difficulty by knowledge-graph path length; the record is where that setting would be kept with the item.
- [[provenance-gated-assertion]] — caps a claim's strength by how the claim was obtained; a different provenance object, the source of a claim rather than the derivation of an item.

[^c1]: arxiv-2512-01045 — "graph path, evidence segments, provenance chain, configuration"
[^c2]: arxiv-2512-01045 — "where derivation histories are essential"
[^c3]: arxiv-2512-01045 — "for which the system can recover the source"
[^c4]: arxiv-2512-01045 — "valid reasoning-chain rate of 0.92, evidence entailment of 0.94, configuration fidelity of 0.96, and provenance completeness of 0.98"
[^c5]: arxiv-2512-01045 — "achieved lineage success of 0.99, provenance completeness of 0.98"
[^c6]: arxiv-2512-01045 — "reducing lineage success to 0.90, provenance completeness to 0.90"
[^c7]: arxiv-2512-01045 — "rerunning selected construction jobs under identical inputs, configurations, software versions, model versions, and"
[^c8]: arxiv-2512-01045 — "We report agreement rates for intermediate graph"
