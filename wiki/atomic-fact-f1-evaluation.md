---
description: "Decomposes the reference and the answer into atomic facts and takes precision, recall and F1 over matched facts, so over-claiming lowers the score as well as omission."
aliases: ["Atomic-ROUGE", "atomic-fact precision and recall", "atomic-unit F1"]
sources: ["arxiv-2512-05371"]
---
# Atomic-fact F1 evaluation

A factual answer can be scored by splitting both it and a reference into minimal, self-contained claims, then matching the claims. ChipMind's Atomic-ROUGE works in two parts. "First, human experts decompose the reference answer y into" a set of atomic facts, and "a powerful LLM similarly decomposes the generated answer" into its own set.[^a1][^a2] An LLM semantic judge then marks which generated facts are semantically equivalent to some reference fact. Precision, recall and F1 are computed over those matched sets.

The paper's stated motivation is the failure of two older families of score. "Traditional n-gram overlap metrics (e.g., ROUGE) struggle with semantic variations", and the embedding-based metrics such as BERTScore "still fail to reliably evaluate factual correctness".[^a3] The decomposition changes the unit that gets scored. The unit is a fact, not a token or a sentence, so a partly wrong sentence earns credit for the facts it gets right and no credit for the one it gets wrong. My reading is that this is why the paper prefers it for fact-intensive answers. The paper does not test that reading directly.

The two sides of the match do different jobs. The paper's mapping is that "precision, recall, and F1-score quantify factual correctness, completeness, and balanced semantic fidelity, respectively".[^a4] A generated fact with no reference match lowers precision, which is the only place over-claiming shows up. A reference fact with no generated match lowers recall. This matters because a recall-only score cannot register over-selection at all; the wiki's note on [[recall-only-partial-credit]] makes that point for multi-answer items, and the precision term here answers it for free-text answers.

The validation is against people. Three senior chip engineers "independently rated ChipMind outputs on 10-point scales" for semantic fidelity and answer completeness, and the ratings were averaged. Atomic-ROUGE reached a Pearson correlation of 0.83 with those averaged ratings, against 0.71 for BERTScore.[^a5][^a6][^a8] A correlation of this size says the score orders answers roughly as the raters did. It does not say the score is a calibrated rate of correct facts.

## Limits

The judge is an LLM, and the metric inherits its variance. Both the decomposition and the matching are done by the model. The paper says Atomic-ROUGE evaluation "leveraged GPT-4.1";[^a7] the parts read do not report run-to-run variance or a second judge.

The reference atoms come from human experts on the paper's own benchmark, SpecEval-QA. The validation uses one set of answers and three raters. "Minimal, self-contained" is the unit, and the parts read do not define it operationally, so two annotators may split the same reference differently and the score will move with the split.

Equal weighting of precision and recall into F1 is the default shown. The paper does not justify it against other weightings, and an answer that should be long, or short, may need a different balance.

The metric scores agreement with the reference atoms. It cannot detect a reference that is itself incomplete or wrong, and the parts read do not test that case.

## Related

- [[weighted-nugget-recall]] — the recall-side cousin: a judge-weighted fraction of a fixed gold nugget set, with no precision term.
- [[recall-only-partial-credit]] — why a recall-only score cannot see over-selection, the gap the precision side here closes.
- [[atomic-entailment-repair-loop]] — the same decomposition into atomic units, used to repair an output rather than to score it.

[^a1]: arxiv-2512-05371 — "first, human experts decompose the reference answer y into"
[^a2]: arxiv-2512-05371 — "a powerful LLM similarly decomposes the generated answer"
[^a3]: arxiv-2512-05371 — "still fail to reliably evaluate factual correctness"
[^a4]: arxiv-2512-05371 — "precision, recall, and F1-score quantify factual correctness, completeness, and balanced semantic fidelity, respectively"
[^a5]: arxiv-2512-05371 — "senior chip engineers independently rated ChipMind outputs on 10-point scales"
[^a6]: arxiv-2512-05371 — "Atomic-ROUGE achieved a Pearson correlation of 0.83 with human ratings"
[^a7]: arxiv-2512-05371 — "Atomic-ROUGE evaluation, leveraged GPT-4.1"
[^a8]: arxiv-2512-05371 — "(r = 0.71)"
