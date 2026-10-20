---
description: "Active Testing picks which unlabeled test items to annotate under a budget, reweights them to stay unbiased, and can stop early, cutting labels sharply while estimating performance within 1%."
aliases: ["active evaluation", "label-efficient test set selection", "active test set construction"]
sources: ["arxiv-2603-21840"]
---
# Active Testing

Active Testing asks a different question from active learning: not "which labels improve the model" but "which test items, once labeled, best estimate the model's performance". Given a labeling budget, it chooses the subset of an unlabeled test pool whose annotation yields the closest estimate to full-test-set performance.[^c1] The point is that a test set needs low-error labels, so each label is expensive, and many items are redundant for estimation.

## Mechanism

1. Score unlabeled items using only inputs (embeddings, a surrogate classifier, dropout uncertainty, embedding-space coverage, or attention-head disagreement), annotate the top-scoring one, and repeat until the budget is spent.
2. Correct the selection bias. Items chosen by a score are not a draw from the population, so the plain average is biased.[^c2] The paper uses the inverse-probability-weighted (Horvitz-Thompson) estimator, which divides each item's metric by N times its selection probability and stays unbiased. Estimators such as PURE and LURE are reported to overestimate accuracy and to leave the [0, 1] range, so they were not used for accuracy.[^c3]
3. Optionally stop adaptively. Fixed-budget methods exhaust the whole budget whatever the need.[^c4] The proposed rule tracks the gap between the unweighted random-sampling estimate and the weighted unbiased estimate. When the gap falls below a threshold tau the active set is deemed representative and annotation stops. A proposition shows the gap goes to zero as the budget approaches full annotation.[^c5]

## What was measured

Across 18 datasets, 4 embedding strategies and 4 task types, annotation reductions of up to 95% were reported with the estimate within 1% of the full test set, with no strategy universally best.[^c6] On IMDB the stopping rule with the attention-disagreement strategy halted after 50 samples,[^c7] and on QNLI cost dropped from $500 to $10 at B = 500 at an assumed $0.02 per label.[^c8] Overall the strategies performed comparably, with small differences, and the proposed Agreement strategy was best mainly at small budgets.[^c9]

Two extensions are shown: a cost prior over languages, which spends budget on cheap languages to evaluate an expensive one, and favoring minority-class items so annotators find rare, high-impact cases.

## Limits

- The stopping rule's stability is judged against a random-sampling estimate on the same subset, not against the unavailable full-test-set metric; it is a heuristic convergence check, and the guarantee stated is asymptotic as the budget approaches the full set (a finite-sample bound is only in an appendix I did not read).
- The multilingual result assumes cross-lingual transferability of model accuracy.[^c10]
- Stratified sampling needs class priors that an unlabeled pool lacks, so it is only a reference.[^c11]
- Headline figures come from a single embedder and predictor shown in the main text, averaged over 10 seeds; thresholds (tau = 0.01) and the $0.02 label cost are the authors' choices. My inference: savings depend on the pool being redundant and the model being already competent.

## Related

- [[mutual-information]] — one of the compared uncertainty scores is a mutual-information (dropout-based) quantity
- [[optimal-question-asking]] — choosing which item to query under a budget is the same selection problem, here for evaluation rather than inference

[^c1]: arxiv-2603-21840 — "Active Testing focuses on estimating test performance with minimal annotation, requiring different"
[^c2]: arxiv-2603-21840 — "Active Testing introduces a bias into"
[^c3]: arxiv-2603-21840 — "since they tend to overestimate"
[^c4]: arxiv-2603-21840 — "Therefore, the annotation process exhausts the whole"
[^c5]: arxiv-2603-21840 — "automatically terminates the annotation process as soon as we estimate that a sufficient"
[^c6]: arxiv-2603-21840 — "no single approach emerging as universally superior"
[^c7]: arxiv-2603-21840 — "stops the annotation process after 50 samples"
[^c8]: arxiv-2603-21840 — "from $500 to $10 at B = 500"
[^c9]: arxiv-2603-21840 — "Overall, all strategies perform comparably, with relatively small differences"
[^c10]: arxiv-2603-21840 — "This experiment assumes cross-lingual transferability"
[^c11]: arxiv-2603-21840 — "as it requires prior knowledge"
