---
description: "Indexing each release of a multi-release system as its own corpus keeps near-identical text from different versions from mixing in retrieval; the query then picks the corpus."
aliases: ["per-release corpus", "release-specific retrieval", "version-partitioned index"]
sources: ["arxiv-2601-02345"]
---
# Release-partitioned corpus

A multi-release system is a set of versions in operation at the same time: "versions are referred to as multi-release systems."[^d1] Each version carries documentation that largely repeats its neighbours, since "While releases share substantial overlaps,"[^d2] the documents differ in the details that matter for a question. For retrieval this is a specific failure. Near-identical passages that give different values for different releases compete for the same query, and the one that wins may belong to the wrong version.

The paper's answer is a partition before retrieval. Its pipeline creates "a separate corpus for each release, instead of combining all" documents into one index.[^d4] The purpose is to keep the index from "mixing information from different releases,"[^d3] and the authors state the consequence as "differences between releases do not affect the LLM" at answer time.[^d5] The partition is only half the mechanism. A query has to be sent to the right corpus, and the paper's rewriting step does this: a user question becomes several standalone queries, because "some tied to releases, and others independent of" releases are needed to answer it.[^d12] The system then "selects the most relevant corpus for document retrieval" for the query.[^d6] The authors credit the release-specific behaviour to rewriting: query rewriting improves retrieval "by enabling release-specific retrieval across" the documents.[^d9]

The same paper argues against a hierarchical alternative, which first retrieves whole documents and then passages within them. That works "well when the documents are sufficiently distinct,"[^d8] but "However, this hierarchical method cannot effectively" separate overlapping release documents.[^d7] This is the authors' argument from the design; the text I read does not test the hierarchical method on their data.

The partition sits upstream of the retrieval units. Once a corpus is chosen, the text is cut into search and context chunks ([[decoupled-search-context-chunk-size]]), so the two choices can be varied independently.

## Limits

- The partition is not isolated. The ablated steps are "dual chunking, context reduction, and context selection," with query rewriting as the fourth, and corpus creation is not among them.[^d10] So the effect of the per-release split by itself is not measured in the text I read. The ablation finding that matters is about query reinterpretation: "queries across multiple system releases is critical for effective" question answering.[^d13]
- One industrial corpus carries the multi-release claim. The Ciena set has multi-release structure, and the public REQuestA set does not: "multi-release characteristics, which are absent in REQuestA."[^d11] The Ciena data "cannot be publicly released," so the multi-release result cannot be replicated from the paper's package.[^d16]
- Questions that span releases are only partly covered. The business need is for "a version-agnostic response that remains relevant across multiple" releases.[^d14] The text does not say how a question that fits no single corpus is answered beyond rewriting into several queries.
- Cost is not reported. Shared text is indexed once per release corpus, so the total index grows with the number of releases; the text gives no index size, storage cost, or update cost. (My inference from the design; the text notes that each release "requires updating version-specific documentation.")[^d15]
- The alternative is untested here. One shared index with release metadata attached would avoid duplicated corpora. The note on [[metadata-fused-embedding-retrieval]] reports metadata fusion in a single index, but nothing in this paper compares the two designs.

## Related

- [[decoupled-search-context-chunk-size]] — the other structural choice in the same pipeline; it cuts chunks inside whichever corpus the query selects.
- [[metadata-fused-embedding-retrieval]] — the single-index alternative: put release metadata into the embedding instead of splitting the corpus.

[^d1]: arxiv-2601-02345 — "versions are referred to as multi-release systems"
[^d2]: arxiv-2601-02345 — "While releases share substantial overlaps"
[^d3]: arxiv-2601-02345 — "from mixing information from different releases"
[^d4]: arxiv-2601-02345 — "separate corpus for each release, instead of combining all"
[^d5]: arxiv-2601-02345 — "differences between releases do not affect the LLM"
[^d6]: arxiv-2601-02345 — "selects the most relevant corpus for document retrieval"
[^d7]: arxiv-2601-02345 — "However, this hierarchical method cannot effectively"
[^d8]: arxiv-2601-02345 — "well when the documents are sufficiently distinct"
[^d9]: arxiv-2601-02345 — "retrieval accuracy by enabling release-specific retrieval across"
[^d10]: arxiv-2601-02345 — "dual chunking, context reduction, and context selection"
[^d11]: arxiv-2601-02345 — "multi-release characteristics, which are absent in REQuestA"
[^d12]: arxiv-2601-02345 — "some tied to releases, and others independent of"
[^d13]: arxiv-2601-02345 — "queries across multiple system releases is critical for effective"
[^d14]: arxiv-2601-02345 — "version-agnostic response that remains relevant across multiple"
[^d15]: arxiv-2601-02345 — "requires updating version-specific documentation"
[^d16]: arxiv-2601-02345 — "cannot be publicly released"
