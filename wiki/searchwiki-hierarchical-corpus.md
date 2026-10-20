---
description: "An offline LLM pipeline compiles a corpus into a three-layer typed wiki (documents, topics, sources) so a retrieval agent picks which node to inspect next by granularity, not flat top-k chunks."
aliases: ["SearchWiki", "three-layer wiki compilation", "typed hierarchical wiki"]
sources: ["singh-2026"]
---
# SearchWiki hierarchical corpus compilation

> Before any query is asked, the corpus is rebuilt into a wiki with three
> granularities — and the retrieval agent's first decision becomes *which
> layer to open*, not which chunk scores highest.

## Definition / Mechanism

SearchWiki is an offline compilation pipeline that turns an unstructured
document or dialogue corpus into a three-layer typed wiki: document
overviews (per-document summaries with section subfolders), topics
(cross-document concept pages linking related documents and topics), and
source pages (page-level OCR/JSON records for fine-grained verification).[^c1]

A hierarchical indexer extracts each long document's table of contents and
mirrors it on disk, so the tree itself encodes granularity — a document
root summary links into top-level sections, each section spawns its own
summary and further subsections down to an exact source page range; short
documents without a usable table of contents collapse to a single summary
instead. A shared tool suite (`search_wiki`, `read_file`, `read_page`,
`grep_search`, `list_files`, `glob_file_search`, `update_scratchpad`) lets
an agent choose which layer to inspect next rather than retrieving flat
top-k chunks independently of one another.[^c2]

## Why it matters

On stall 2 (which axis first) this gives selection a concrete, coarse-to-fine
object: the agent's next-query decision is which *node* — document
overview, topic page, or exact source page — to open, descending only when
the coarser layer under-answers. "This layout supports progressive
disclosure: the agent can" start from summaries or topics and descend to a
specific page only when needed.[^c3]

## Limits

- The comparison is against flat top-k RAG baselines on ViDoRe v3,
  FinanceBench and three memory benchmarks, all inside singh-2026's own
  harness; no other structured-corpus method (e.g. a document-tree RAG
  built a different way) is run for comparison, so the gain is not isolated
  to the three-layer split specifically.
- Compilation is itself an LLM pass (a single call per document unit
  generates summaries and registers topics against a global registry); its
  own error rate — wrong section boundaries, duplicate or missed topics —
  is not reported, only downstream QA accuracy, so a silent compilation
  failure could look identical to a hard query in the results.
- Short documents without a usable table of contents lose the hierarchy
  entirely ("a direct single-summary route"), so the coarse-to-fine
  selection this note describes does not apply to them.

## Related

[[wikiresearcher-rl-navigation]] · [[value-of-information]] · [[adaptive-submodularity]]

[^c1]: singh-2026 — "knowledge into three layers - document overviews, crossdocument topic pages, and page-level source records; enabling progressive refinement of retrieval when initial lookup"
[^c2]: singh-2026 — "For long documents, our hierarchical indexer extracts a table"
[^c3]: singh-2026 — "This layout supports progressive disclosure: the agent can"
