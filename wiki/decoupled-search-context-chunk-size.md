---
description: "Retrieval favors small chunks and answer generation favors large ones; indexing small search chunks that each map to a larger context chunk serves both from one document."
aliases: ["dual chunking", "decoupled search and context chunks", "S-chunks and C-chunks"]
sources: ["arxiv-2601-02345"]
---
# Decoupled search and context chunk sizes

Retrieval-augmented generation has to cut each document into chunks, and a single chunk size has to do two jobs. The first job is search, which favors small pieces: "For search, smaller chunks tend to increase retrieval accuracy."[^c3] The second job is answering, which wants more text in view. Small chunks give precision but leave the answering model with little context,[^c1] while "whereas large chunks supply more context but tend to lower" retrieval accuracy.[^c2] The authors name this as a known sensitivity of RAG to chunk size, and they answer it by not choosing one size.

The mechanism, as Algorithm 1 of the paper defines it, runs in two passes over the same pages. Each page is divided into k equal search chunks, and only those are embedded and stored in the vector index. Each page also yields one context chunk, which is the page itself plus a padding of characters taken from the page before and the page after, so the answering model sees more than the matched fragment.[^c4] The two sets are linked by a fixed map: "is a one-to-one correspondence between context chunks and" search chunks, so a retrieved search chunk resolves to "the corresponding (and larger)" context chunk that is passed to generation.[^c4][^c5] Because only search chunks are embedded, "chunks do not require vectorization in our approach."[^c6] The retriever is therefore tuned for small units while the generator receives larger ones, and the two sizes are set separately.

The reported settings were k = 2 search chunks per page ("We set k = 2 to split each") and a padding of 500 characters, chosen to "provide sufficient preceding and succeeding context."[^c7][^c8] The baseline the paper compares against uses the same chunks for both jobs: "same chunks for both search and answer generation, we treat" each page as one chunk, splitting only pages longer than 3,000 characters.[^c12]

## Limits

- The gain is not isolated. The headline comparison pits the full pipeline against a baseline that lacks query rewriting and context reduction as well as dual chunking; the baseline "does not have a context-reduction step."[^c13] The abstract's 16.5% and 12% improvements therefore bundle several components. The text does report a dual-chunking ablation in which each added step is tested on a base with none: "every non-base ablation outperforms the base in at least" one metric,[^c10] and the authors conclude each step "contributes positively to the overall approach."[^c11] I read that finding, not the per-metric table for dual chunking alone.
- The two parameters are fixed, not swept. The text I read gives no sensitivity analysis for k or the padding size, so whether two search chunks per page suits other document layouts is open.
- The construction is page-based: the algorithm builds context chunks from neighbouring pages. How it would handle text without page boundaries is not addressed. (My inference from the algorithm.)
- All results use one open model, Llama 3-70B, for both the answering and the judging role.[^c15] The chunk-size effect was not compared across models here.
- Hallucination is credited jointly: "reduction further reduce hallucinations by improving retrieval" is attributed to dual chunking and context reduction together, so their separate contributions to hallucination are not measured.[^c14]

## Related

- [[release-partitioned-corpus]] — the other structural choice in the same pipeline: which corpus a search runs against, decided before the chunks are cut.
- [[query-relative-token-overflow]] — a pre-LLM probe whose note suggests it could resize chunks; that is a suggestion there, not a test of dual chunking.

[^c1]: arxiv-2601-02345 — "precision but provide limited context for answer generation"
[^c2]: arxiv-2601-02345 — "whereas large chunks supply more context but tend to lower"
[^c3]: arxiv-2601-02345 — "For search, smaller chunks tend to increase retrieval accuracy"
[^c4]: arxiv-2601-02345 — "is a one-to-one correspondence between context chunks and"
[^c5]: arxiv-2601-02345 — "the corresponding (and larger)"
[^c6]: arxiv-2601-02345 — "chunks do not require vectorization in our approach"
[^c7]: arxiv-2601-02345 — "We set k = 2 to split each"
[^c8]: arxiv-2601-02345 — "provide sufficient preceding and succeeding context"
[^c9]: arxiv-2601-02345 — "QAMR outperforms a baseline RAG-based chatbot without dual-chunking"
[^c10]: arxiv-2601-02345 — "every non-base ablation outperforms the base in at least"
[^c11]: arxiv-2601-02345 — "contributes positively to the overall approach"
[^c12]: arxiv-2601-02345 — "same chunks for both search and answer generation, we treat"
[^c13]: arxiv-2601-02345 — "does not have a context-reduction step"
[^c14]: arxiv-2601-02345 — "reduction further reduce hallucinations by improving retrieval"
[^c15]: arxiv-2601-02345 — "for both LLM-Core and LLM-Eval"
