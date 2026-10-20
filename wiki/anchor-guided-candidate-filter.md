---
description: "Adaptive expansion pulls in off-target passages; a second gate keeps only candidates whose typed intent anchor matches the sub-query, so recall and precision are set apart."
aliases: ["CSA-guided filter", "intent-anchor filter", "semantic anchor filtering", "typed anchor gate"]
sources: ["arxiv-2512-05371"]
---
# Anchor-guided candidate filter

A retriever that expands its evidence set until new items stop adding information buys completeness with noise.[^c3] A second gate, separate from the expansion, can prune by intent rather than by similarity. In ChipMind the LLM is first asked what the current sub-query needs, and it writes that need as a target anchor: a typed pair of a type and an entity.[^c1] Each retrieved candidate carries its own anchor, and a candidate is kept only if its anchor matches the target. The text states the rule as "retaining only nodes whose anchors exactly match".[^c2] The formula writes the same step as a compatibility test, Compat, and the text read does not define that test beyond the word "exactly" (my reading of the formula).

The paper gives the reason for the split in its own words. The adaptive stage "ensures evidence completeness, it can also introduce functionally irrelevant information", so the second stage removes what the first one brings in.[^c3] The effect is shown as a curve over the retrieval size K. Without the filter, performance is "degrading as K increases without it, due to noise from irrelevant documents". With it, ChipMind "maintains robust performance even at K = 50".[^c4][^c5] What the curve shows is that the filter lets a larger K be used without harm. It does not show that K = 50 is the right size, and the text read does not compare the gate with a plain similarity cutoff at the same K.

Put plainly, the mechanism separates two questions that one similarity score would answer together. The first is whether the search reached the evidence at all. The expansion answers it, and it is judged by how much each new batch still changes the model's belief, as in [[stop-continue-criteria-in-retrieval-loops]]. The second is whether this item is the kind of thing the sub-query asks for. Typed anchors answer that one. A passage can be topically close and still be the wrong kind of evidence; the wiki's note on [[relevance-completeness-divergence]] records a related gap, where topical relevance explains little of rated completeness, though in a different setting.

What survives the transfer is the structure: a recall-oriented expansion followed by a typed gate with a hard match rule. This does not depend on circuits. What does not survive is the gate's footing. The anchors are circuit entities and types, and the parts of the text read do not show how such anchors would be defined for other documents. Without a typed vocabulary for a domain, the gate has nothing to match, and the design falls back to the similarity filter the paper argues against (my inference).

## Limits

The evidence is one system on one benchmark, SpecEval-QA, built by the same authors. The filter's effect is reported as a figure over K and in prose; the parts read give no numeric table for filter on against filter off.

An exact-match gate is hard. An anchor assigned the wrong type removes relevant evidence, and nothing records the removal. The paper does not report how often anchors disagree with a reference, and the risk here is my inference, not a measured failure. How anchors are normalised before matching is not described in the parts read, so "exactly match" may hide a fuzzy step.

The claim is measured against the same system without the filter, not against other precision methods. Whether the gate helps where topical relevance is already adequate is not tested.

## Related

- [[fixed-capacity-evidence-replacement]] — under a fixed evidence budget a controller swaps items rather than appending; here the gate shrinks the candidate pool before any budget applies, a different lever on the same noise.
- [[schema-gated-relation-grounding]] — a similar accept-or-reject gate, applied to relation names before a query runs rather than to retrieved items.
- [[relevance-completeness-divergence]] — topical relevance is not a proxy for completeness, the gap a typed gate is meant to close.
- [[stop-continue-criteria-in-retrieval-loops]] — the stop decision that governs the expansion this gate follows.

[^c1]: arxiv-2512-05371 — "by generating a target anchor"
[^c2]: arxiv-2512-05371 — "retaining only nodes whose anchors exactly match"
[^c3]: arxiv-2512-05371 — "ensures evidence completeness, it can also introduce functionally irrelevant information"
[^c4]: arxiv-2512-05371 — "degrading as K increases without it, due to noise from irrelevant documents"
[^c5]: arxiv-2512-05371 — "robust performance even at K = 50"
