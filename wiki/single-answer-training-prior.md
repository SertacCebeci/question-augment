---
description: "Training on one correct answer per query leaves most DETR decoder slots inactive, capping multi-answer recall; removing self-attention and dropping slots at random widens activation."
aliases: ["active decoder-query collapse", "single-moment prior", "index collapse", "coordination collapse"]
sources: ["doi-10-48550-arxiv-2603-02363"]
---
# Single-answer training prior

When every training query has exactly one correct answer, a model learns to expect one. Pujol-Perich et al. (2026) show this in DETR-style video moment retrieval, where K learnable decoder queries each propose one candidate moment with a confidence score. The number of "active" decoder queries (those whose confidence does not vanish) acts as a compute budget for how many answers can be returned: "when only 2 queries are activated in a 4-moment instance, the upper bound of retrieved moments is 50%."[^c1] They call a shortfall of this kind active decoder-query collapse.

**Measured symptom.** Models trained on caption-based data activate "around 4, regardless of the number of moments of the search queries (x-axis)."[^c2] The active count does not scale with the number of true answers, so multi-answer queries (see [[caption-to-search-query-shift]]) lose recall.

**Two structural causes the authors identify.**

1. *Coordination collapse.* Self-attention among decoder queries pushes them apart "to avoid redundancy", but it also lets them agree on which slot handles the single answer while the rest stay silent.[^c3] Removing it, with the losses unchanged, lets each query act independently. Redundant predictions are then filtered with non-maximal suppression at post-processing.
2. *Index collapse.* The same few indices (for example 1 to 4) repeatedly dominate confidence, reinforced throughout training, "where the same decoder query indices repeatedly dominate" while the others are never used.[^c4]

**Remedy.** A decoder-query dropout "randomly zeroes out k% of the" learnable queries on each training step.[^c5] It spreads supervision over more slots. Together the two changes increase the number of active queries. The authors report gains of up to 14.82% mAPm on search queries, and up to 21.83% on multi-moment ones.[^c6] They also say that alternative ways of activating more queries, such as other matching strategies, produce redundant predictions. I have not read those ablations closely.

**What transfers.** The general point is that a supervision regime with one gold answer teaches a system to stop at one, and that a fix can come from model structure instead of re-annotating data. The slot-activation mechanics are specific to set-prediction detectors. For text question answering this is my analogy and was not tested.

## Limits

- The evidence is on three VMR datasets with synthetic multi-moment labels, and mainly on CG-DETR and related DETR models.
- Collapse is diagnosed by counting active slots. Causation from the prior is argued by the removal and dropout interventions, not by training on multi-answer data as a control.
- Removing self-attention depends on non-maximal suppression, a fixed post-processing step. Its sensitivity to thresholds was not examined in what I read.
- The language gap is not addressed.

## Related

- [[caption-to-search-query-shift]] — the evaluation shift that exposes the prior
- [[under-specification-severity-asymmetry]] — another case where a vague input has more than one valid reading

[^c1]: doi-10-48550-arxiv-2603-02363 — "the upper bound of retrieved moments is 50%."
[^c2]: doi-10-48550-arxiv-2603-02363 — "around 4, regardless of the number of moments of the search queries (x-axis)."
[^c3]: doi-10-48550-arxiv-2603-02363 — "the role of SA is pushing decoder queries apart from each other to avoid redundancy."
[^c4]: doi-10-48550-arxiv-2603-02363 — "where the same decoder query indices repeatedly dominate"
[^c5]: doi-10-48550-arxiv-2603-02363 — "randomly zeroes out k% of the"
[^c6]: doi-10-48550-arxiv-2603-02363 — "improves performance on search queries by up to 14.82% mAPm , and"
