---
description: "Pseudo-relevance feedback helps few queries and hurts more, hidden by averages; in a user audit, withholding expansion from harmed queries was worth about twice applying it to helped ones."
aliases: ["PRF query drift asymmetry", "selective PRF audit", "audit-then-automate sPRF"]
sources: ["doi-10-48550-arxiv-2607-12098", "arxiv-2511-17255"]
---
# Query-expansion harm asymmetry

Expanding a query with terms taken from its own top-ranked documents (pseudo-relevance feedback, PRF) raises average retrieval scores, but the average conceals a per-query split. Non-relevant expansion terms pull the ranking away from the user's intent, which is called query drift. Aggregate offline metrics such as nDCG average over queries, so they hide which queries were degraded and by how much.[^c1]

## What the audit measured

Liang, McDonald and Ounis ran a participatory audit. For 43 TREC Deep Learning 2019 queries, a ColBERT baseline ranking and a ColBERT-PRF ranking were merged by Team Draft Interleaving. The merged set was shown in a 3x3 Latin-square grid, with the originating system hidden. Users clicked a card, then chose a passage, and these choices were read as preferences between the two systems.[^c2]

Result: only 20.9% of queries benefited from PRF, 25.6% suffered a degraded user experience, and 53.5% showed no clear preference.[^c3] So expansion hurt more queries than it helped, a split invisible to aggregate evaluation.

A second study, with different participants, compared policies. Reverting harmed queries to the baseline gave a 68.5% relative gain in user engagement. Applying PRF only to queries that had benefited gave 37.0%, so avoiding harm was worth nearly twice as much.[^c4] Applying PRF only where the audit signalled benefit beat universal PRF by +10.5 adjusted selections per query (p = 0.032, d = 1.9) over 20 selective queries. A difference-in-differences check used the neutral queries as control, because their interleaved ranking was held constant across both studies.[^c5]

## Why existing selection inherits the opacity

Selective PRF normally decides per query with query performance prediction (QPP) built from the same ranking statistics. The authors argue such methods lack robustness across tasks and are validated against offline metrics that may not match user satisfaction, so the selector "inherits, rather than resolves" the opacity.[^c6]

## Automating the label

Their proposal for automation is a conjecture they only sketch, since the text reports an initial result without detail. It is to show an LLM reranker the same interleaved pool users saw and read which system's documents it ranks higher, instead of asking it to classify whether PRF helps. The ranking then serves as the explanation, because it points to specific documents.[^c7]

## Limits

- It is a 3-page workshop paper. The audit covers 43 queries, one collection and one PRF method (ColBERT-PRF).
- The 108 users are split into two studies of 54. Engagement (selections) is the outcome, which is not the same as relevance or satisfaction.
- The 20-query selective comparison is small, and the 11 hurt plus 9 benefit queries were selected by the first study's own labels.
- The Stage 2 LLM replication is claimed ("initial") but its agreement figures are not in the text I read, so I treat it as unverified.
- Whether the harm asymmetry carries over to other expansion methods, such as LLM-generated query rewriting, is my open question; it was not tested.

## Related

- [[llm-filtered-pseudo-relevance-feedback]] — another PRF fix that targets non-relevant feedback documents.
- [[plan-before-search-anchoring]] — names a different cross-hop form of query drift.
- [[knowledge-overshadowing]] — a query drifting because one condition dominates.
- [[embedding-space-relevance-feedback]] — the same drift in dense-vector feedback: a VLM image-search paper finds plain PRF gives no gain and reads a later-round decline as possibly drift, untested.[^c8]
- [[rationale-level-relevance-judging]] — judging relevance with inspectable evidence.

[^c1]: doi-10-48550-arxiv-2607-12098 — "conceal the specific queries that are degraded by query expansion"
[^c2]: doi-10-48550-arxiv-2607-12098 — "We present this combined document set in a"
[^c3]: doi-10-48550-arxiv-2607-12098 — "First, only 20.9% of queries benefit from PRF, while 25.6% suffer"
[^c4]: doi-10-48550-arxiv-2607-12098 — "nearly twice the 37.0% gain"
[^c5]: doi-10-48550-arxiv-2607-12098 — "analysis with Neutral queries as a control"
[^c6]: doi-10-48550-arxiv-2607-12098 — "providing no transparent justification for when or why expansion"
[^c7]: doi-10-48550-arxiv-2607-12098 — "rather than asking an LLM to classify whether PRF helps or harms a query (an"
[^c8]: arxiv-2511-17255 — "drift phenomenon discussed in the relevance feedback literature"
