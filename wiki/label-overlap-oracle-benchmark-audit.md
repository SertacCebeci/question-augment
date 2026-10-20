---
description: "A model-free oracle ranking by a shared category label (charge), BM25 breaking ties, can recover nearly all of a benchmark's trained-model gain when relevance is defined through that label."
aliases: ["charge-controlled evaluation", "charge-overlap oracle", "label-as-anchor versus label-leak audit"]
sources: ["doi-10-48550-arxiv-2606-12993"]
---
# Label-overlap oracle as a benchmark audit

When a retrieval benchmark grades a document relevant because it shares a category with the query, a high score can measure category matching rather than the skill the benchmark is named for. The audit tests this with a ranker that has no model at all: sort candidates by whether they share the query's gold primary label, and break ties inside each group with BM25. In Chinese legal case retrieval the label is the charge. The paper reads the result as the share of the BM25-to-best-system gap that this oracle closes.[^c1]

## Mechanism

Two readings of a strong NDCG@10 look identical on one leaderboard. Under "charge-as-anchor", using charge identity is a legitimate signal. Under "charge-as-label-leak", relevance grades collapse to same-versus-different charge by pool construction, so the score rewards charge classification more than legal reasoning.[^c2] The oracle separates them by construction. Gold charge is the primary sort key, and BM25 only orders documents within a same-charge partition, never across charges.[^c3]

Measured result: on LeCaRDv2 the oracle closes 99.2% of the BM25-to-best-trained gap, with no detectable difference from the best system. On LeCaRDv1 it closes 84.3%. On CAIL2022 it falls below the strongest trained reranker.[^c4] The paper traces the LeCaRDv2 result to the benchmark's rubric. Top relevance is defined by a match in the crime's key constitutive elements, which largely encode the charge. The charge-to-relevance macro-AUC falls across benchmarks (0.871, 0.759, 0.728), and that gradient is not implied by any single rubric.[^c4]

Holding charge fixed isolates what is left. KELLER's +0.103 NDCG@10 advantage over BM25 shrinks to a +0.026 within-charge residual. Its cluster-bootstrap interval excludes zero, and it is about a quarter of the advantage.[^c5] So the headline score is mostly, not entirely, charge by construction.

The same label can also be used earlier in the pipeline. A zero-training channel that restricts BM25 to the predicted charge raised first-stage R@100 on LeCaRDv2 by 0.025, while wrong-charge controls hurt. The authors present this as evidence of the confound, not as a better retriever.[^c6]

Transferable idea (my gloss): when a benchmark's relevance definition contains a cheap categorical attribute, rank by that attribute alone and report how much of the model gain remains, within each category.

## Limits

- The claim is about the benchmark, not about any system. The paper says it does not claim that any system relies on charge.[^c1]
- The oracle is a diagnostic baseline, not an upper bound or a retriever. A learned within-charge ranker could in principle beat it.[^c3]
- The effect is uneven. It is near-total on one benchmark and weaker on the other two. The CAIL2022 verdict rests on only n=40 queries and depends on the anchor system chosen.
- A cascade using predicted rather than gold charge reproduces 76.6% of the LeCaRDv2 gap and does not transfer to the other benchmarks.
- The first-stage positive control is exploratory, was selected post hoc among six variants, and has unverified dense-rank provenance.
- Only Chinese legal case retrieval was tested. Whether the pattern holds in other domains with categorical relevance definitions is not shown.

## Related

- [[graded-relevance-binarization-threshold]] — another way a benchmark's relevance grading changes what a score means
- [[reasoning-shortcut]] — the shortcut family this label confound belongs to
- [[option-matching-shortcut]] — a similar case of a surface cue standing in for the target skill

[^c1]: doi-10-48550-arxiv-2606-12993 — "not a uniform explanation of NDCG@10, and not"
[^c2]: doi-10-48550-arxiv-2606-12993 — "The two are"
[^c3]: doi-10-48550-arxiv-2606-12993 — "BM25 affects ordering only within each samecharge partition, never across charges."
[^c4]: doi-10-48550-arxiv-2606-12993 — "The same charge-only rule recovers just 84.3% of the gap on LeCaRDv1"
[^c5]: doi-10-48550-arxiv-2606-12993 — "About a quarter"
[^c6]: doi-10-48550-arxiv-2606-12993 — "showing that R@100 can be increased"
