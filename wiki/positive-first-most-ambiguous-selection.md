---
description: "Under rare-positive imbalance, scoring boundary-near samples but ranking likely positives first yields batches that are both informative and mostly relevant; pure uncertainty or pure confidence fails."
aliases: ["PF-MA", "positive-first uncertainty sampling", "asymmetric-utility active learning"]
sources: ["arxiv-2603-24480"]
---
# Positive-first most ambiguous selection

A query-selection rule for interactive retrieval of a rare category. A user supplies a tiny seed (one positive, five negatives), a light linear classifier is retrained each round, and the system picks a small batch (10 items) for binary feedback. The authors' claim is that conventional active learning asks "which samples should be labeled to train the best overall model?", while here utility is asymmetric: querying a predicted-positive "provides substantially higher expected utility than querying a predicted-negative one".[^c1]

## Two failing baselines

Pure uncertainty sampling ("Most Ambiguous", score 1 − |0.5 − f(x)|) is informative but, with positives at 1 in 1000 or rarer, the boundary is crowded with negatives: "near-boundary points are mostly negatives".[^c2] Pure confidence ("Most Positive", score f(x)) fills the batch with positives, but they are "often redundant and belong to the already explored subspaces, offering limited information to the classifier".[^c3] Representativeness methods (CoreSet, discriminative AL) did worst: coverage below 0.1 and under 4% of the class found, because they oversample majority regions.[^c4]

## The rule

PF-MA scores a sample by its ambiguity if the classifier output is at least 0.5, and by its raw output if below 0.5. Because the positive half-space always outscores the negative one, the order is: positives near the boundary, then less ambiguous positives, and only then negatives if the budget is not yet filled.[^c5] So the batch is asymmetric: the user sees relevant items from round one (they may stop early), while boundary positives still refine the classifier.

## Measuring the goal: class coverage

Fraction of positives found is blind to redundancy. The paper proposes class coverage: cluster the class offline (K-means, K = 32, labels used only for evaluation) and count the fraction of clusters holding at least one retrieved positive.[^c6] Pairwise-distance diversity measures are rejected because compact classes can hold distinct modes and spread-out classes can be sampled from few modes.

## What was measured

On CIFAR100-LT, ImageNet-LT and PlantNet300K with CLIP and DINOv2 features, PF-MA gave the highest coverage at iteration 25 in nearly all settings, with the advantage growing over iterations. Simple step- or distance-based diversity add-ons were unstable.[^c7] The ranking held across K in {16, 32, 64}, where other methods' rankings shifted.[^c8]

## Limits

- Labels came from ground truth as a proxy for the user; no real users, noise or fatigue were tested.
- Coverage depends on offline clusters of the labelled class, so "visual modes" are whatever K-means finds; this is the authors' proxy for user value.
- Evaluated only with a linear SVM, batch 10, a one-positive seed, and image embeddings; the rule needs a calibrated-ish score near 0.5 as the boundary. Transfer to text questions is my inference, not tested.
- Gains over MA/MP are modest on some cells (differences in the second decimal in the table), and no significance tests were seen in the slices I read.

## Related

- [[expected-information-gain]] — the information-maximising ideal that uncertainty sampling approximates; PF-MA deliberately trades some of it for user-side utility.
- [[generalized-binary-search]] — chooses the most evenly splitting query; the symmetric-utility case PF-MA departs from.

[^c1]: arxiv-2603-24480 — "querying a predicted-positive sample provides substantially higher expected utility than querying a predicted-negative one"
[^c2]: arxiv-2603-24480 — "near-boundary points are mostly negatives"
[^c3]: arxiv-2603-24480 — "these samples are often redundant and belong to the already explored subspaces, offering limited information to the classifier"
[^c4]: arxiv-2603-24480 — "CoreSet and DAL achieve coverage below 0.1 and discover fewer than 4% of the class"
[^c5]: arxiv-2603-24480 — "It first selects positives near the decision boundary, then less ambiguous positives, and only includes negatives if the iteration budget is not yet filled."
[^c6]: arxiv-2603-24480 — "coverage is the fraction of clusters with at least one positive"
[^c7]: arxiv-2603-24480 — "PF-MA outperforms both MA and MP baselines, with the advantage becoming more pronounced over iterations."
[^c8]: arxiv-2603-24480 — "our method PF-MA consistently outperforms other baselines across all K values and iterations"
