---
description: "Who produced a labelled example can predict its label with no content cue; on ChEMBL bioactivity, a model given only producer probabilities came close to a structure baseline."
aliases: ["intent leakage", "chemist style leakage", "source identity leakage", "author-identity shortcut"]
sources: ["arxiv-2512-20924"]
---
# Provenance cue leakage

A labelled example carries a record of who produced it, and that record can predict the label without any content cue. Where producers differ in what they make and which targets they pursue, producer identity is correlated with activity, and a model can learn the producer rather than the mechanism. The paper calls the chemistry case a "Clever Hans" failure mode and states the claim as models predicting bioactivity "without requiring a lab-independent understanding of chemistry".[^c1]

The concept has two steps. The first is recovery: a classifier can name the producer from the structure. The paper infers "style" from ChEMBL authorship, "treating each author identifier as a proxy for a lab- or PI-level group".[^c3] A fingerprint model over 1,815 prolific authors reaches 60% top-5 accuracy under scaffold-based splitting.[^c2] The second step is transfer: the producer probabilities alone, plus a protein identifier and no fingerprint, feed an activity model. Its validation AUROC is 0.652, against 0.656 for an ECFP plus protein model, and the paper reads the two as "very similar to one another across metrics and across random splits".[^c5] The paper's reading is that the activity model does not need chemistry: "The activity model does not need to infer detailed chemistry to perform well", and it "can instead learn the sociology of the dataset".[^c6][^c7]

The input is not structure-free in content. The producer vector keeps chemistry, since linear probes decode fingerprint bits from it with "median performance around 0.9 across the probed bits".[^c8] So "never sees molecular structure" describes what the activity model is given, not the information in it. The producer vector is a learned, compressed structural view that happens to align with who made the molecule, and the leak sits in that alignment. The paper's conclusion is that a large share of the signal usually credited to structure-activity learning "is also attainable by a model that never sees molecular structure at all".[^c16]

What the concept changes is the question asked of a benchmark score. A high score on a ChEMBL-derived split does not by itself show that a model learned structure-activity relations, because a producer-only path may produce the same number. The paper generalises the source beyond authors to "authors, labs, institutions, vendors, or campaigns", calling it an "underappreciated confounder in public medicinal chemistry datasets".[^c13] Its proposed check is to "include source-only or source+target baselines to bound the contribution" of the source.[^c12] My inference: a source-only score that matches the content model marks the benchmark as one a source alone can pass, and a gap between them is what the content model adds over the source.

## Limits

- One slice of data: the paper restricts to "prolific authors (more than 30 publications and more than 600" molecules, giving 1,815 authors.[^c9] Single-paper and small producers are absent, so nothing here reaches the long tail.
- The producer is a proxy. "We do not observe individual molecule designers",[^c10] and the authorship notion is called "imperfect" because papers list non-synthetic contributors too.[^c4]
- No producer-disjoint evaluation was run. The reported runs use scaffold-disjoint splits ("We enforce scaffold-disjoint splits at the compound level").[^c15] The paper "propose[s] author-disjoint splits"[^c11] but does not measure how far the score falls under them. How much of the leak survives such a split is open.
- No target-only row. Table 2 reports a dummy, molecular weight plus protein, author plus protein, ECFP plus protein, and the combined model. My reading is that no protein-identifier-alone row is present, so how much of the author model's AUROC is already carried by target identity is not separated. The paper's own point that adding author probabilities to ECFP "yields only modest additional gains" does not isolate that either.
- The mechanism is predictive, not causal. The paper shows near-equal predictive performance and borrows the Clever Hans analogy; it does not intervene on the producer. Whether the producer cue causes the label or only tracks each lab's target portfolio is not separated.
- One probe: a single LightGBM over ECFP and one curation protocol. Other learners, featurisations or splits could move the numbers, and the paper reports no spread beyond five scaffold splits.

## Related

- [[clever-hans-effect]] — the general reliance on a cue correlated with the label; this note fixes the cue to who produced the labelled data
- [[cross-generator-cross-corpus-split]] — the same disjointness idea for synthetic QA, applied to generator and corpus rather than to producer
- [[author-cue-review-bias]] — an author-identity cue that moves an LLM judge with correctness held fixed; here the cue moves the label itself

[^c1]: arxiv-2512-20924 — "without requiring a lab-independent understanding of chemistry"
[^c2]: arxiv-2512-20924 — "achieving 60% top-5 accuracy under"
[^c3]: arxiv-2512-20924 — "treating each author identifier as a proxy for a lab- or PI-level group"
[^c4]: arxiv-2512-20924 — "This authorship-derived notion is imperfect"
[^c5]: arxiv-2512-20924 — "they are very similar to one another across metrics and across random splits"
[^c6]: arxiv-2512-20924 — "The activity model does not need to infer detailed chemistry to perform well"
[^c7]: arxiv-2512-20924 — "it can instead learn the sociology of the dataset"
[^c8]: arxiv-2512-20924 — "median performance around 0.9 across the probed bits"
[^c9]: arxiv-2512-20924 — "we restrict to prolific authors (more than 30 publications and more than 600"
[^c10]: arxiv-2512-20924 — "we do not observe individual molecule designers"
[^c11]: arxiv-2512-20924 — "propose author-disjoint splits"
[^c12]: arxiv-2512-20924 — "include source-only or source+target baselines to bound the contribution"
[^c13]: arxiv-2512-20924 — "underappreciated confounder in public medicinal chemistry datasets"
[^c15]: arxiv-2512-20924 — "We enforce scaffold-disjoint splits at the compound level"
[^c16]: arxiv-2512-20924 — "is also attainable by a model that never sees molecular structure at all"
