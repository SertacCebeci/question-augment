---
description: "Pairing a query that names a technical term with one that only describes it, on the same passage, splits a retriever's lexical dependence from its semantic matching; BM25 and BGE-M3 show big gaps."
aliases: ["TCQ/TAQ", "terminology concordant query", "terminology agnostic query", "lexical dependency gap"]
sources: ["arxiv-2601-03496"]
---
# Terminology-concordant versus terminology-agnostic queries

STELLA (aerospace retrieval, passages from NASA technical reports) writes two queries for each source passage. The terminology-concordant query (TCQ) includes the passage's domain terms verbatim and tests lexical matching. The terminology-agnostic query (TAQ) must not contain the term and instead states its description or definition, which tests whether the model matches meaning without the surface form.[^c1] The terms come from a dictionary built from the corpus. A TAQ for "propellant" would say "a chemical substance that is burned to propel a rocket".[^c2]

## How the pair is built

Both queries start from the same seed query. Over three density-raising steps, the TCQ adds terminology from the passage and so has high lexical overlap with it. The TAQ adds descriptions of the terms instead. These descriptions were written beforehand by an LLM from a window of five consecutive passages around the target.[^c3] An LLM self-critique pass checks hard constraints at each step, for example whether the query is answerable from the passage alone.[^c4] Each of 500 passages gets one TCQ and one TAQ, giving 1,000 pairs.[^c5] Because the passage is held fixed, the score difference TCQ minus TAQ (nDCG@10) is read as a "lexical dependency gap".

## What the gap showed

- BM25 does well on TCQ but drops sharply on TAQ, a gap of about 0.228.[^c6]
- The decoder-based Llama-Embed-Nemotron has a gap of about 0.1053, which the author reads as semantic understanding that survives the absence of the term.[^c7]
- BGE-M3 has a larger gap (0.272) than BM25, so the author says it behaves "more like a keyword matcher".[^c8]
- Intent matters. BM25 scores 0.886 on procedure queries under TCQ. The author attributes this to procedural documents repeating the same terms.[^c9]
- After translation, TCQ keeps its English terms and TAQ is translated in full. TCQ scores stay well above TAQ, and BGE-M3 falls from 0.655 on TCQ to 0.315 on TAQ, averaged over six languages.[^c10]

Many neural models score below BM25 overall, which the author takes as evidence that a hybrid of lexical and neural retrieval is needed in term-heavy domains.[^c11] That conclusion is the author's interpretation.

## Limits

- Everything is synthetic: LLM-written queries over one corpus (NASA reports) in one domain. Whether real aerospace users write TCQ-like or TAQ-like queries was not measured here.
- A TAQ has no term, but the description still comes from the passage's context, so TAQ may leak other lexical overlap. Overlap in the other words was not quantified in what I read.
- Reading the gap as "semantic understanding" is the author's inference. A smaller gap could also come from a model that is weak on TCQ. Gap and absolute score need to be read together.
- Seven embedding models and one BM25 baseline; no rerankers and no trained hybrid.
- My own inference: the design generalizes to asking, since a question that names the concept and one that only describes it can need different handling by whoever answers. This paper did not test that.

## Related

- [[embedding-retrieval-literal-token-anchoring]] — the same finding that embedders rank by literal tokens, shown there with disguised wording in math and agent trajectories
- [[lexical-reranker-sign-diagnostic]] — a cheap control for whether surface overlap drives rankings
- [[cross-retriever-reformulation-gain]] — query rewording gains depend on the retriever's lexical or semantic nature

[^c1]: arxiv-2601-03496 — "Terminology Concordant Query (TCQ): the terminology appearing in the passage is included verbatim in"
[^c2]: arxiv-2601-03496 — "a chemical substance that is burned to propel a rocket"
[^c3]: arxiv-2601-03496 — "using five consecutive passages from c − 2 to c + 2 as the expanded context passage"
[^c4]: arxiv-2601-03496 — "Is this query answerable solely from the given passage?"
[^c5]: arxiv-2601-03496 — "resulting in an evaluation set of 1,000 unique (query, passage) pairs"
[^c6]: arxiv-2601-03496 — "yielding a large lexical dependency gap of about 0.228 (TCQ−TAQ)"
[^c7]: arxiv-2601-03496 — "Llama-Embed-Nemotron minimizes this gap to around 0.1053"
[^c8]: arxiv-2601-03496 — "BGE-M3 exhibits an even larger gap (0.272) than BM25"
[^c9]: arxiv-2601-03496 — "achieves a very high score of 0.886 for Procedure / Operation under the TCQ"
[^c10]: arxiv-2601-03496 — "It achieves an average TCQ score of 0.655"
[^c11]: arxiv-2601-03496 — "lexical matching remains highly competitive in domains where discrimination over specialized terminology is crucial"
