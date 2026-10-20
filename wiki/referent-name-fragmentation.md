---
description: "A referent the literature names by acronym, full name or version splits across records; merging them barely moved top-1 hits but lifted the other hit rates in one ablation."
aliases: ["dataset naming ambiguity", "entity aliasing", "surface-form fragmentation", "dataset name ambiguity", "entity normalization", "alias-aware deduplication"]
sources: ["arxiv-2512-15363", "arxiv-2512-00590"]
---
# Referent name fragmentation

When one thing is named several ways, a search index can record it as several things. The paper's case is datasets, which are referenced inconsistently: "across the literature, e.g., by acronym, full name, or version,"[^r1] so a lookup keyed on one name reaches only the records that carry that name. The evidence filed under the other names stays out of reach. The authors state the consequence directly: the naming split "leads to fragmented results and low recall."[^r2]

The mechanism is one of identity rather than wording. The same object sits under several surface forms, and a pipeline that treats each form as a separate entity holds a partial picture of it in each. This is the reverse of the one-name, many-referents failure in [[ambiguous-name-branch-coverage]]: there a query spreads over several objects, here an object is split over several names.

KATS repairs the split with a dataset-resolution step in its offline graph build. Algorithmic methods first produce candidate duplicate pairs, "The algorithmic methods first generate high-probability" pairs.[^r3] The LLM does not cluster the ambiguous names open-endedly. It performs a "more reliable binary verification task" on each candidate pair.[^r4] Verified duplicates are merged, so the task links that were filed under different names are gathered in one node.

The measured effect is an ablation. Disabling the module has little effect on top-1 hit rates, but it "results in significant performance degradation of" the other hit-rate metrics.[^r5] The authors conclude that "resolving dataset naming ambiguities is a critical factor in realworld dataset search."[^r6] The ablation ran without the LLM reranker, "instead of using LLM reranking, we directly evaluate the search results from the KG."[^r7]

The split between the two kinds of metric is the informative part. Top-1 hits depend on the single best-ranked record, which fragmentation seldom removes. The other hit rates count how many relevant datasets are reachable at all, and that is where a split name costs. This reading of the two rows is mine; the paper reports the rows and the conclusion, not this explanation.

The same split appears as a construction step in a second pipeline, where it is called entity normalization. After extraction, each triplet's subject and object are matched against existing entries of the same entity type or a compatible parent type. The top-10 candidates, ranked by similarity of their stored aliases, go to an LLM, which decides whether the "extracted entity is synonymous with one of the existing entries."[^r10] On a match the mention takes the canonical label and its surface form is kept as an alias; otherwise a new entity is created.

The measurement here is a question-answering score, not a dataset search. Removing the ontology check and the normalization together lowers MuSiQue exact match from 42.6 to 27.0, so the two are measured only jointly.[^r11] Removing the alias store alone lowers it to 36.5, and the paper reads that as "alias expansion improves entity matching in question answering."[^r12] My reading, not the paper's: a split name costs a graph reader reachable evidence, in the way the dataset ablation found for the other hit rates.

## Limits

- One ablation on one benchmark, the CS-TDS-M suite in the Figure 7 caption. The paper reports hit rates. It does not report how often a merge was wrong, that is, how many distinct datasets sharing a name were fused. Nothing read here measures that rate.
- The resolution depends on the upstream LLM. The authors concede that "the quality of our KG is fundamentally dependent" on its fidelity, and that the system "still lacks a specialized module for automatically verifying the authenticity of all LLM outputs and correcting possible" errors.[^r8][^r9]
- The ablation removes the reranker, so the gap describes the graph's own ranking. Whether it survives a reranker was not shown.
- The mechanism was measured for dataset names in scientific text. Whether other kinds of entity with many surface forms (methods, models, metrics) fragment the same way was not tested here.
- The normalization result comes from a single MuSiQue table with one model, and its ablation removes normalization together with the ontology check. Normalization's own effect is not measured. The text read does not report how often the LLM merged two distinct entities by mistake.[^r11]

## Related

- [[ambiguous-name-branch-coverage]] — the inverse case: one name over several referents, where a complete answer must cover every branch.
- [[information-need-reification]] — the same task-to-data gap seen from the asker's side, closed there by an inspectable interpretation rather than a resolved index.
- [[ontology-constrained-triplet-validation]] — the type-and-schema check that the same pipeline runs alongside this normalization step; the two are ablated together.
- [[text-free-triplet-answering]] — the answering side of a graph built with this merging; the store is the only evidence there.

[^r1]: arxiv-2512-15363 — "across the literature, e.g., by acronym, full name, or version,"
[^r2]: arxiv-2512-15363 — "which leads to fragmented results and low recall"
[^r3]: arxiv-2512-15363 — "The algorithmic methods first generate high-probability"
[^r4]: arxiv-2512-15363 — "more reliable binary verification task"
[^r5]: arxiv-2512-15363 — "top-1 hit rates, but results in significant performance degradation of"
[^r6]: arxiv-2512-15363 — "resolving dataset naming ambiguities is a critical factor in realworld dataset search"
[^r7]: arxiv-2512-15363 — "instead of using LLM reranking, we directly evaluate the search results from the KG"
[^r8]: arxiv-2512-15363 — "the quality of our KG is fundamentally dependent"
[^r9]: arxiv-2512-15363 — "verifying the authenticity of all LLM outputs and correcting possible"
[^r10]: arxiv-2512-00590 — "extracted entity is synonymous with one of the existing entries."
[^r11]: arxiv-2512-00590
[^r12]: arxiv-2512-00590 — "confirming that alias expansion improves entity matching in question answering"
