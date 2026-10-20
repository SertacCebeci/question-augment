---
description: "A similarity evaluator separates output classes only as far as each class's outputs agree: CLIP's ROC-AUC on ASCII generations sat near 0.55, and 0.83 after filtering."
aliases: ["within-class consistency ceiling", "embedding class separability", "same-class retrieval ROC-AUC"]
sources: ["arxiv-2512-04125"]
---
# Consistency-bounded evaluator separation

A similarity evaluator can be asked whether it tells output classes apart. The procedure in this work: embed each generated image and its reference with CLIP, score each pair by cosine similarity, and compare same-class pairs with different-class pairs. The summary statistic is ROC-AUC, which "quantifies how well a model separates positive from negative pairs".[^c1] Chance is 0.5, and 1.0 is perfect discrimination.[^c2]

The result is that this separation is capped by how consistent each class's outputs are. On unfiltered generations CLIP "showed weak class separation", with an AUC near 0.55.[^c3] After the inconsistent generations were filtered out, ROC-AUC "rose to 0.83, demonstrating that CLIP can discriminate effectively when ASCII generations are semantically consistent."[^c4] The abstract puts the same pattern per class: most ASCII categories are not separated at all, "yielding chance-level performance even for low-variance classes".[^c15]

The mechanism is a matter of overlap. Figure 2 plots the two distributions, with "Green indicates positive (intra-class) pairs, red indicates negative (inter-class) pairs."[^c6] Spread within a class widens its same-class distribution until it meets the cross-class one. Filtering narrows the spread but does not remove the overlap: "separation is not complete, with substantial overlap remaining."[^c7] The reading here is mine: a class is separable when its members sit close together relative to their distance from other classes, so an evaluator's score can only be as clean as the outputs it scores.

The work gives two attributions for the same numbers, and it does not settle between them. One is that "the bottleneck lies in the quality of LLM-generated ASCII rather than in the evaluator."[^c8] The other, in the abstract, is that the bottleneck lies "in representation rather than generational variance".[^c5] Its results section then says "the primary limitation lies in CLIP" representational capacity "along with variance in model generations",[^c9] and its limitations section names "a dual bottleneck".[^c10] The evidence on the evaluator side is weak: fine-tuning CLIP with triplet loss "yielded only modest gains".[^c14] So the data show that separation depends on both the evaluator and the output distribution, and not which one dominates.

## Limits

- Two selections give the 0.83. Section 5.2 attaches it to filtering on standard deviation and mean similarity. Section 5.2.1 attaches it to restricting to classes with high mean similarity, where "AUC increased to 0.83", and says that "indicating that CLIP can represent ASCII structure only for a subset of well-formed" categories.[^c13] The lowest-variance subsets, by contrast, "approached near chance performance".[^c12] The text does not reconcile these.
- The filter uses the same mean-similarity statistic the separation is read from. A filter on that statistic partly selects for the outcome (my inference, not tested here).
- Filtering is not an evaluation method. The paper says that "Filtering demonstrates an upper bound of performance but is not" a sustainable strategy.[^c11]
- One evaluator, one fine-tuning recipe. Other embedding models were not compared, so whether the ceiling belongs to CLIP or to any similarity score is open.
- Only ASCII art was measured. Extending the ceiling to other symbolic or rendered-image classes is my extrapolation.
- Per-class numbers for the chance-level categories are not in the text read; the claim rests on the abstract's summary.

## Related

- [[evaluator-architecture-for-answer-quality]] — which evaluator tracks the references; here the question is whether any similarity evaluator can separate classes when the outputs spread.
- [[feedback-quality-bottleneck]] — another capped pipeline, where the limit depends on which stage is being measured.
- [[llm-judge-score-instability]] — judges disagreeing with themselves; here the outputs disagree within a class.

[^c1]: arxiv-2512-04125 — "quantifies how well a model separates positive from negative pairs"
[^c2]: arxiv-2512-04125 — "indicating random performance and 1.0 indicating perfect discrimination"
[^c3]: arxiv-2512-04125 — "On unfiltered generations, CLIP showed weak class separation"
[^c4]: arxiv-2512-04125 — "ROC-AUC rose to 0.83, demonstrating that CLIP can discriminate effectively"
[^c5]: arxiv-2512-04125 — "revealing that the bottleneck lies in representation rather"
[^c6]: arxiv-2512-04125 — "Green indicates positive (intra-class) pairs, red indicates"
[^c7]: arxiv-2512-04125 — "separation is not complete, with substantial overlap remaining."
[^c8]: arxiv-2512-04125 — "quality of LLM-generated ASCII rather than in the evaluator."
[^c9]: arxiv-2512-04125 — "the primary limitation lies in CLIP"
[^c10]: arxiv-2512-04125 — "This highlights a dual bottleneck"
[^c11]: arxiv-2512-04125 — "Filtering demonstrates an upper bound of performance but is not"
[^c12]: arxiv-2512-04125 — "even the lowest-variance subsets approached near chance performance"
[^c13]: arxiv-2512-04125 — "indicating that CLIP can represent ASCII structure only for a subset of well-formed"
[^c14]: arxiv-2512-04125 — "fine-tuning with triplet loss yielded only modest gains"
[^c15]: arxiv-2512-04125 — "to separate most ASCII categories, yielding chance-level performance even for"
