---
description: "An LLM agent that searches documents with shell keyword and regex tools, and no standing vector index, reached 91% of a vector RAG's answer correctness across five document sets."
aliases: ["agentic keyword search", "keyword-search agent", "index-free agentic retrieval", "shell-tool retrieval", "grep-based agentic RAG"]
sources: ["arxiv-2602-23368"]
---
# Agentic keyword search retrieval

Document question answering can run without a vector index. The model is given a folder of files and a shell; it first reads the file metadata, then writes its own search commands. The paper's agent "can dynamically decide to do broad keyword searches or targeted regex patterns across one or more documents," using RipGrep-All for regex and multi-keyword matching and PDFGrep for page-range search.[^c1] Its loop writes a command, executes it, and either updates the answer when new context appears or keeps searching; error handling with "modified search patterns" is part of the same loop.[^c2]

Against a vector RAG baseline on the same questions, the agent kept most of the score. Across the five datasets in the main table, attainment averaged 94.52% for faithfulness, 88.05% for context recall and 91.48% for answer correctness.[^c3] The authors summarise this as "consistently achieving above 88% average attainment across all" three metrics, with no semantic search in the loop.[^c4] On FinanceBench, a separate set of long filings, the agent scored a mean correctness of 30.40% against 24.24% for the RAG baseline.[^c5]

The mechanism is the retrieval interface, not a better embedding. A lexical search returns exact spans the model can read whole, and the agent widens context or changes its pattern across rounds, so repeated search takes the place of a precomputed index. This reading is mine, not the paper's. The gap was widest on the most argumentative text: the lowest answer-correctness attainment was on PaulGrahamEssay (79.91%), and the authors tie it to the need for "contextual comprehension beyond keyword matching."[^c6][^c7]

## Limits

- The baseline is one fixed configuration: a Bedrock knowledge base with "fixed 300 token chunking strategy with 20% overlap," and a cap of five retrieved chunks.[^c8] A reranked or hybrid RAG was not tested, so "over 90%" is relative to this baseline.
- "Cost effective" is asserted, not measured; the slices read give no latency, token or cost figures for either side.[^c9]
- The FinanceBench comparison is a single subset. The authors' Run 4 dropped documents "the reference files were made unavailable publicly midexperimentation."[^c10]
- The Computer Use comparison covers "seven representative questions from the FinanceBench dataset," judged by hand.[^c11]
- The authors list "performance degradation with large documents" and limited multimedia handling among the limits, and say the approach "lacks long-term knowledge retention."[^c12]
- Scoring uses LLM-as-judge RAGAS metrics. No check on judge reliability appears in the slices read, and context recall is computed on segments the agent chose.
- The paper does not measure ranking. A separate study found that grep-style agents on one backbone reached only 0.280 Recall@10 on BEIR-type corpora, far below BM25 (see [[corpus-grounded-one-shot-query]]). The two results measure different things, so they do not settle whether lexical agents are weak retrievers or adequate answerers.

## Related

- [[corpus-grounded-one-shot-query]] — the same retrieval family on ranked-retrieval benchmarks, where grep-style agents trail a document-frequency-weighted BM25 query
- [[agentic-rag-autonomy-principles]] — this agent passes the autonomy tests by design: it chooses its own commands and conditions each on the last output
- [[compressed-memory-versus-raw-retrieval]] — another agentic-versus-fixed retrieval comparison, where raw retrieval won

[^c1]: arxiv-2602-23368 — "the agent can dynamically decide to do broad keyword searches or targeted regex patterns across one or more"
[^c2]: arxiv-2602-23368 — "error handling (for e.g. automatic retry)"
[^c3]: arxiv-2602-23368 — "an average attainment score of 94.52% across all datasets"
[^c4]: arxiv-2602-23368 — "consistently achieving above 88% average attainment across all"
[^c5]: arxiv-2602-23368 — "achieved a mean correctness score of 30.40%"
[^c6]: arxiv-2602-23368 — "The lowest attainment in this category was observed in the PaulGrahamEssay dataset (79.91%)"
[^c7]: arxiv-2602-23368 — "underscores the importance of continued research into improving contextual comprehension beyond keyword matching"
[^c8]: arxiv-2602-23368 — "fixed 300 token chunking strategy with 20% overlap"
[^c9]: arxiv-2602-23368 — "Our approach is simple to implement, cost effective"
[^c10]: arxiv-2602-23368 — "the reference files were made unavailable publicly midexperimentation"
[^c11]: arxiv-2602-23368 — "seven representative questions from the FinanceBench dataset"
[^c12]: arxiv-2602-23368 — "performance degradation with large documents, restricted"
