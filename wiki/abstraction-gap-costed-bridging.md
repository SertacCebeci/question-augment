---
description: "Query-evidence mismatch is the minimal set of typed bridging assumptions needed to entail the query; costing each bridge by family and repairing the failing one beats one similarity score."
aliases: ["RAG abstraction gap", "typed bridge calculus", "stage-localized reflective refinement"]
sources: ["doi-10-48550-arxiv-2606-09459"]
---
# Abstraction gap as costed bridging

A query and the document that answers it are often stated at different levels of abstraction: the query asks for an "executive", the text says "CEO". AbstRAG defines the mismatch as the abstraction gap, "the minimal set of typed assumptions required to" align query intent with the evidence the document has.[^c1] Retrieval then becomes a search for the cheapest set of assumptions that, with the segment and background knowledge, entails the query. Its cost is the gap, and it is infinite when no set suffices (this is the paper's formulation, in Section 3.3).

## Mechanism

**Four bridge families, ordered by risk.** Expression (same referent, surface variation), conceptual (paraphrase, concept-level shifts), intent-evidence (specific evidence to a more general queried class, such as "CTO of Anthropic" to "AI company representative") and event-type (indirect evidence through frames, nominalizations, artifacts). Each family has a weight, with expression cheapest and intent and event highest. The last two rest on typicality, so they are treated as revisable hypotheses that still cost something, admitted only inside a budget.

**Why one score is not enough.** Dense retrieval merges entity normalization, role binding under a shared temporal scope, and linking of consequences to events into a single number. The authors say it "folds these heterogeneous operations into" one similarity, so it cannot say which bridge made a segment relevant or where to repair a failure.[^c2] Their example is a query about LLM-company and chip-supplier collaborations in 2024. The answer sentence says "CTO of Anthropic visited the head of TSMC's 3 nm fabrication division this Tuesday". Finding it needs affiliation, office-to-type, and a date taken from the document header.

**Relevance** combines match quality, a query-independent utility prior (results and conclusions carry claims more than background), and a discount that decays exponentially with bridge cost. A segment that satisfies the query with fewer or safer bridges ranks higher.

**Indexing versus query side.** Conservative, query-independent normalizations (coreference, entity and time normalization, context lifting) run once at index time. Query-side expansion is limited to cost-bounded controlled disjunction.

**Reflective refinement.** When retrieval fails, a critic diagnoses the failure, localizes the responsible stage, and proposes a minimal patch to that operator. The patch is accepted only if sufficiency and compression do not regress. This edits the retrieval mechanism, unlike Self-RAG-style loops that edit the generated answer.

## What was measured

Across three within-document benchmarks and seven baselines, the paper reports nDCG@10 wins in 18 of 21 paired contrasts and generation accuracy gains of 1.9, 5.2 and 4.0 percent. Ablations attribute most of the retrieval gain to refinement. Turning it off costs 9.2 Suff@10 on FEVEROUS but only a small loss on SciFact, where "the loss shrinks to −1.6 Suff@10" because a ceiling of about 93 is already reached.[^c3] Refinement fires on 2% of SciFact cases and rises with how much abstraction the evidence needs.[^c4]

The two controls block different errors. On a small stress slice, removing the compression control raises the over-expansion false-positive rate from 0 to 73.7 percent, and "isolating" over-expansion as the error only that control catches.[^c5] Removing the sufficiency control costs 9.2 Suff@10 on FEVEROUS instead.

A cost-budget failure shows the price of bridges. FEVEROUS SUPPORTS loses 3.1 nDCG@10 because it "crosses two bridge types whose summed" cost exceeds the budget.[^c6] Raising the budget would restore it with noisier expansion.

## Limits

- Scope is single-document retrieval. The background resource is drawn from or paired with that one document, and the main runs fill the role and event bridges from a document-local abstraction map. A 30-case toy check covers a non-empty background resource.
- The 73.7 to 0 percent figure comes from a small refinement-stress slice. It is not a benchmark-wide rate.
- The cost weights and per-bridge distances are hand-set catalogs. The "multiplicative dominance" and conservativity properties are proved in the paper's appendix, which I did not read.
- Whether the same typing helps open-domain or multi-document retrieval is not tested here.
- That a person asking a question benefits from naming the bridge is my inference from the design, not something the paper measured.

## Related

- [[reasoning-gap-driven-retrieval]] — also turns unmet evidence items into targeted follow-up retrieval, but by reasoning type, not bridge type
- [[hypothesis-conditioned-query-rewriting]] — rewrites the query toward decision-useful evidence; here the repair is localized to a typed operator
- [[retrieval-utilization-gap]] — separates retrieval failures from use failures; this note splits the retrieval failure further
- [[prompted-versus-trained-query-augmentation]] — query expansion is the rival strategy; here expansion is cost-capped

[^c1]: doi-10-48550-arxiv-2606-09459 — "the minimal set of typed assumptions required to"
[^c2]: doi-10-48550-arxiv-2606-09459 — "Dense retrieval folds these heterogeneous operations into"
[^c3]: doi-10-48550-arxiv-2606-09459 — "the loss shrinks to −1.6 Suff@10"
[^c4]: doi-10-48550-arxiv-2606-09459 — "The refinement loop activates on 2% of SciFact,"
[^c5]: doi-10-48550-arxiv-2606-09459 — "the over-expansion falsepositive rate jumps from 0% to 73.7%, isolating"
[^c6]: doi-10-48550-arxiv-2606-09459 — "(−3.1) crosses two bridge types whose summed"
