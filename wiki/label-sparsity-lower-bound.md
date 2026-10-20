---
description: "Scoring rankings against a sparsely labelled pair set counts unlabelled good pairs as misses, so metrics become lower bounds that rise as more appropriate pairs get judged."
aliases: ["label sparsity", "lower-bound bias", "partially annotated evaluation", "incomplete relevance labels"]
sources: ["arxiv-2601-01350"]
---
# Label sparsity lower bound

A ranking metric checks each item a system returns against a set of pairs labelled as correct. When that labelled set covers only some of the candidate pairs, a correct pair that nobody labelled is scored exactly like an incorrect one. In the FC-CONAN paper a recommendation "is counted as correct if —and only if— the ⟨HS; CN⟩ pair is annotated as appropriate in the partition under test."[^c1] Absence from the labels is therefore not evidence of absence: the authors write that "unlabeled pairs remain ambiguous—often reflecting oversight rather than a true absence of relation."[^c2]

The concrete case is CONAN, a counter-narrative corpus that does "annotate only a sparse subset of all possible HS–CN pairs."[^c3] In a pilot with one recommender, "only 2 of 10 suggested CNs were labeled as appropriate, manual review judged 8 to be valid."[^c4] The eight valid CNs were there to be found but were unlabelled, so a metric computed on CONAN reports the lower figure.

The controlled version fixes a candidate pool of 100 counter-narratives, has twelve systems rank it for each hate-speech message, and scores every ranking against four partitions of the exhaustively labelled pairs (Diamond, Gold, Silver, Bronze). Using CONAN as the sole gold standard "yields zero scores across all metrics."[^c5] As judged pairs are added, scores rise: "As progressively more appropriate pairs are included" from CONAN to Diamond, Gold, Silver and Bronze.[^c6] The authors report that "metric values scale roughly in proportion to the number of appropriate" pairs in each partition.[^c7]

The bias belongs to the label set, not to the system. The same ranking receives different marks under different partitions. In the paper's example the top-ranked counter-narrative "is never judged appropriate in any partition," while the second is judged appropriate in three of the four.[^c8]

The authors conclude that "this results in artificially lower scores for most evaluation metrics in recommendation systems."[^c9] The lower-bound reading is restricted: it is drawn for metrics that are "not negatively affected by a greater number of positives," such as MRR@10 and Hit Ratio@10, whose scores on partially annotated data "should be considered lower bounds."[^c10][^c11]

What survives a transfer to other ranked tasks is the direction of the bias: any metric that counts a pair as correct only when it is labelled is biased down wherever labels are incomplete. This is, by my reading and not the paper's, the same situation that pooled test collections meet when unjudged items are treated as non-relevant. What does not transfer cleanly is the direction for metrics that fall as positives grow; the paper does not settle it.

## Limits

- The lower-bound claim is inferred from monotone growth across partitions. The authors say the sparse metrics "fail to reflect true retrieval system performance,"[^c12] but no complete ground truth is available to check the gap against. The top partition is not a ceiling either: "Bronze boosts volume" and keeps the only non-valid pairs.[^c13]
- The direction is stated only for metrics that are not hurt by more positives, and only for MRR@10 and Hit Ratio@10 in the reported experiment.
- The scope is narrow: 45 hate-speech messages by 129 counter-narratives from the English part of CONAN, twelve systems, one candidate pool. The authors say this "remains far from a fully exhaustive re-annotation."[^c14]
- The labels used as truth are themselves uncertain. The authors warn that "high agreement does not automatically guarantee high-quality labels."[^c15] Pairs with one annotator are the weakest: "pairs annotated by a single annotator, 379 pairs (≈11.49%)" were invalid.[^c16] The lower-bound argument assumes the positives in the higher partitions are right.
- The pilot with one recommender (2 of 10 labelled versus 8 judged valid) is an anecdote, not a measured rate.
- The claim that the bias is a property of incomplete labelling rests on the authors' own design, in which they "re-annotated a representative subset" rather than the full set of pairs.[^c17]

## Related

- [[weighted-nugget-recall]] — also a fixed gold set that caps what a metric can credit; there the gap lies in how the reference was built, here in which pairs were labelled at all
- [[reference-answer-defect-audit]] — a reference that wrongly rejects a correct output produces the same false-negative direction by a different route
- [[structured-annotator-disagreement-on-harm]] — how annotators disagree decides which labels a partition can be trusted to contain

[^c1]: arxiv-2601-01350 — "annotated as appropriate in the partition under test"
[^c2]: arxiv-2601-01350 — "unlabeled pairs remain ambiguous—often reflecting oversight rather than a true absence of relation"
[^c3]: arxiv-2601-01350 — "annotate only a sparse subset of all possible HS–CN pairs"
[^c4]: arxiv-2601-01350 — "only 2 of 10 suggested CNs were labeled as appropriate, manual review judged 8 to be valid"
[^c5]: arxiv-2601-01350 — "yields zero scores across all metrics"
[^c6]: arxiv-2601-01350 — "As progressively more appropriate pairs are included"
[^c7]: arxiv-2601-01350 — "metric values scale roughly in proportion to the number of appropriate"
[^c8]: arxiv-2601-01350 — "is never judged appropriate in any partition"
[^c9]: arxiv-2601-01350 — "This results in artificially lower scores for most evaluation metrics in recommendation systems"
[^c10]: arxiv-2601-01350 — "negatively affected by a greater number of positives"
[^c11]: arxiv-2601-01350 — "should be considered lower bounds"
[^c12]: arxiv-2601-01350 — "fail to reflect true retrieval system performance"
[^c13]: arxiv-2601-01350 — "Bronze boosts volume"
[^c14]: arxiv-2601-01350 — "remains far from a fully exhaustive re-annotation"
[^c15]: arxiv-2601-01350 — "high agreement does not automatically guarantee high-quality labels"
[^c16]: arxiv-2601-01350 — "pairs annotated by a single annotator, 379 pairs (≈11.49%)"
[^c17]: arxiv-2601-01350 — "re-annotated a representative subset"
