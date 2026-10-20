---
description: "Splits a retriever's biases into those that live in the query-document comparison, fixable by rewording the query, and those baked into document encodings, which no rewording reaches."
aliases: ["query-document interaction bias", "document encoding bias"]
sources: ["arxiv-2604-06097"]
---
# Interaction bias vs. encoding bias

> Some of what a retriever gets wrong lives in how the question is put;
> some of it lives in the document, and no way of putting the question
> reaches it.

## Definition / Mechanism

Goyal, Mukherjee, Saxena, Phukan, Chandrasekharan & Sundaram (2026)
test five query-rewriting techniques against four dense-retriever biases
and split the results into two kinds. **Query-document interaction
biases** — "such as literal matching—arise from how queries and documents
are compared and can be mitigated through query transformation."[^c1]
**Document encoding biases** — "particularly position bias—appear
embedded in document representations and persist regardless of query
formulation, likely requiring retriever-level modifications." The
split is read off the data, not asserted: literal-matching bias falls by
an average 39% under every tested technique, while brevity bias — the
worst offender at baseline — leaves the best method (simple rewriting) a
residual |t| of 6.62 against a baseline of 15.57, "suggesting that
brevity bias may be more deeply encoded in document representations,
requiring retriever-level interventions rather than query modifications
alone." Position bias sits in between: it is nearly eliminated by one
query-side technique (Query2Doc, 5.28 → 2.81) yet worsened by another
(HyDE), so the same feature can be interaction-typed under one
reformulation and encoding-typed under another — the taxonomy classifies
a *bias-under-a-technique*, not the bias alone, until enough techniques
have been tried to see which residual will not move.

## Why it matters

This bounds what rewording a question — any question, not only a
retrieval query — can be expected to fix. If what a wording elicits
depends partly on how the content is internally represented by whoever
or whatever answers it, no reformulation on the asking side removes that
part; only a change on the answering side does. The framework gives this
a falsifiable test — try several distinct rewordings and see whether a
residual sensitivity to the confound survives all of them — rather than
leaving "some biases resist rewording" as an intuition.

## Limits

Two categories from four biases and five techniques is a small basis for
a general taxonomy; the paper itself treats the split as an
"implication for researchers," not a settled classification. A bias
scored as interaction-type here (literal matching) could still turn out
encoding-type under a technique not tested (step-back prompting,
multi-query fusion, chain-of-thought retrieval — named as future work).
The taxonomy is defined only for dense bi-encoder and late-interaction
retrievers; sparse and generative retrieval are out of scope.

## Related

- [[masking-vs-mitigating-bias-reduction]]
- [[retrieval-order-sensitivity]]
- [[format-restriction-effect]]
- [[presupposition-hallucination-gap]]

[^c1]: arxiv-2604-06097 — "Query-document interaction biases—such as literal matching—arise from how queries and documents are compared and can be mitigated through query transformation."
