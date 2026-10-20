---
description: "A query reformulation's retrieval gain is conditioned on the retrieval paradigm it is issued to: BM25 gains shrink under learned-sparse retrieval and often vanish under dense retrieval."
aliases: ["retrieval-paradigm-conditional reformulation gain", "cross-retriever reformulation transfer"]
sources: ["arxiv-2604-27421"]
---
# Cross-retriever reformulation gain

> The same rewritten query is not the same rewrite to every retriever: a query expansion that helps BM25 can be neutral to a learned-sparse retriever and harmful to a dense one.

## Definition / Mechanism

Bigdeli et al. (2026) hold the reformulation
method, the generating LLM and the decoding configuration fixed and
vary only the downstream retriever — BM25 (lexical), SPLADE (learned
sparse) and BGE (dense) — across TREC DL and six BEIR datasets. The
same ten LLM-based reformulation methods (instruction-driven,
pseudo-document, question-answer and corpus-grounded) are scored
under all three paradigms, isolating the interaction between the
reformulation and the retriever's representation from the choice of
reformulation itself. The headline result: "reformulation gains are
strongly conditioned on the retrieval paradigm, that improvements
observed under lexical retrieval do not consistently transfer to
neural retrievers, and that larger LLMs do not uniformly yield better
downstream performance."[^c1]

Under SPLADE, "gains are smaller and less consistent. Several
document-level methods that substantially improve BM25 exhibit only
marginal improvements under SPLADE, and in some cases introduce
slight degradations in nDCG@10" — attributed to redundancy, since
SPLADE already performs neural term expansion during encoding, so an
LLM's explicit lexical enrichment duplicates work the retriever does
itself.[^c2]

Under BGE, "the divergence is more pronounced. While a subset of
document-level methods maintains modest improvements on DL 2019 and
DL 2020, others fail to outperform the original query" — because
dense retrieval reads a query as a point in a continuous embedding
space, and a lexical expansion that adds matchable terms for BM25 can
move that point in a direction uncorrelated with, or opposed to,
relevant documents' embeddings.[^c3]

The pattern is stated as a rule of thumb in the paper's own table
caption: "LLM-based reformulation yields the largest gains with BM25,
offers moderate improvements with BGE (especially on hard queries),
but provides limited benefit with SPLADE++, where the original query
often remains the strongest."[^c4]

Corpus-grounded methods (conditioning the expansion on initially
retrieved evidence, e.g. LameR, CSQE) transfer better to SPLADE and
BGE than unconstrained pseudo-document generation, because
conditioning constrains the added text to distributionally relevant
terms rather than open-ended topical broadening.

## Why it matters

Almost all prior evaluation of LLM-based query reformulation pairs a
method with a lexical retriever alone, and reports that pairing's gain
as the method's gain. This note names the confound: a reformulation's
effect is not a property of the rewrite text by itself, but of the
rewrite *as read by a specific retriever*. A practitioner choosing or
designing a reformulation strategy for a dense-retrieval pipeline
cannot infer its value from a BM25 benchmark; the same wording change
that elicits better matches from a term-overlap retriever can elicit
worse matches from an embedding-space one. This generalizes the
formulation question this category asks — how a question's wording
changes what it elicits — to a second variable most reformulation
work leaves fixed: what elicits also depends on what is reading the
question.

## Limits

The three retrievers (BM25, SPLADE, BGE) are one exemplar each of
their paradigm; the finding is that paradigm predicts transfer
failure in this study, not a proof that every learned-sparse or dense
retriever behaves identically to SPLADE or BGE. The reformulations
themselves are unchanged across retrievers — no method here adapts its
rewrite to the target retriever's representation — so the note
establishes that gains do not transfer as-is, not that they could not
transfer if reformulation were retriever-aware. `[?]` — unverified:
the paper does not report statistical significance tests on the
BEIR-average cross-paradigm differences it summarizes qualitatively.

## Related

- [[reformulation-pattern-library]] — chooses *which* transformation to
  generate but, like the methods surveyed here, does not condition
  that choice on the target retriever's paradigm.
- [[compcqr]] — trades one committed rewrite for combinatorial
  redundancy fused by RRF; whether that redundancy also survives the
  BM25-to-dense transfer failure documented here is untested.
- [[reformulation-method-ranking-instability]] — the companion finding
  from the same study: a reformulation method's *relative* standing
  against other methods is also conditional, on the generating LLM's
  backbone and scale rather than the retriever.
- [[format-restriction-effect]] — a different surface-form change
  (restricting output form) whose effect also depends on what reads
  the output, the parallel case on the generation side of asking.

[^c1]: arxiv-2604-27421 — "reformulation gains are strongly conditioned on the retrieval paradigm, that improvements observed under lexical retrieval do not consistently transfer to neural retrievers, and that larger LLMs do not uniformly yield better downstream performance."
[^c2]: arxiv-2604-27421 — "gains are smaller and less consistent. Several document-level methods that substantially improve BM25 exhibit only marginal improvements under SPLADE, and in some cases introduce slight degradations in nDCG@10"
[^c3]: arxiv-2604-27421 — "the divergence is more pronounced. While a subset of document-level methods maintains modest improvements on DL 2019 and DL 2020, others fail to outperform the original query"
[^c4]: arxiv-2604-27421 — "LLM-based reformulation yields the largest gains with BM25, offers moderate improvements with BGE (especially on hard queries), but provides limited benefit with SPLADE++, where the original query often remains the strongest."
