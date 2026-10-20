---
description: "Matching labelers to samples by sorting both, most ambiguous sample to most accurate labeler and filling capacity in order, minimises the worst single label's noise."
aliases: ["optimal labeler assignment", "min-max labeler assignment", "bottleneck assignment of samples to labelers"]
sources: ["arxiv-2512-12870"]
---
# Worst-case noise labeler assignment

Once a set of samples has been chosen for labeling, each one still has to go to a labeler. The OLAS paper (arXiv:2512.12870) treats this as its own optimization. There are M labelers, each with an accuracy a_i and a capacity c_i, the number of samples that labeler can annotate in one cycle; and there are query points, each with an entropy e_j. Each point is labeled once, by one labeler.[^a1]

The objective is the largest noise any single label carries, not the total or the average. The model is set up "to minimize the maximum generated noise among all" labels.[^a2] The paper contrasts this with rival rules that choose a labeler to maximise expected quality or minimise expected risk for one instance, and calls its own choice "a worst-case rather than average-case criterion".[^a3]

The result is a sorting rule. With points sorted by entropy, most ambiguous first, and labelers sorted by accuracy, most accurate first, the optimum fills the most accurate labeler's capacity with the most uncertain points, then the next labeler, and so on. In the paper's words, a more uncertain query point "should be assigned to the labeler with the highest accuracy", and this "will guarantee the lowest maximum noise generated among all possible assignments".[^a4][^a5] The mechanism, in plain terms (my reading): the bottleneck is the largest noise on any label, and that is set by whichever high-entropy point lands on a weak labeler. Moving the most ambiguous points to the most accurate labelers lowers that bottleneck first.

The rule does not depend on the shape of the noise. "The solution to the optimal assignment is independent of the structure of the noise model".[^a6] What carries over to another setting is the ordering, not the numbers. The only property the rule needs is the one stated in [[uncertainty-dependent-label-noise]]: noise decreasing in accuracy and increasing in entropy. The proof is in the paper's Appendix A, which this note did not read; the claim here rests on the theorem's statement in the body.

How it performs. On a crowdsourced music-genre dataset, the paper reports that the methods using optimal assignment "clearly and consistently outperform every method that does not use optimal labeler".[^a9] Its entropy-sampling baseline with random assignment reaches 0.671 (ES+RLA, in the paper's notation as I read it),[^a10] and entropy sampling with the optimal assignment reaches 0.690.[^a8] The paper's own reading of that gap is the more important finding: "entropy based sample selection paired with optimal labeler assignment alone captures nearly all of the benefit".[^a7] On that dataset, the joint optimization of which sample and which labeler added little beyond the assignment rule.

## Limits

- The objective is a choice. Minimising the largest noise is not the same as minimising the total; the parts of the paper this note read do not show a head-to-head comparison with a sum objective.
- One label per sample is assumed. The paper says extending to several labels per sample "leads to a qualitatively different modeling regime",[^a11] so the sorting rule covers single labels only.
- The ordering needs labeler accuracies that are ranked correctly. The paper argues that the policy "primarily depends on" relative differences, not exact values, and so tolerates estimation noise.[^a12] That is the paper's claim; this note did not test it, and a wrong ranking of two close labelers is the case it would break (my inference).
- Capacities are fixed inputs and no sample can receive two labels. Where redundancy is affordable, the rule answers a different question than aggregation does.
- The advantage over random assignment is shown on simulated labelers and one crowdsourced dataset; on that dataset the margin of the joint method over the assignment-only method is small.

## Related

- [[uncertainty-dependent-label-noise]] — the noise function this rule minimises; the rule needs only its monotonicity
- [[noise-seeking-uncertainty-sampling]] — the choice of which points to query, which comes before the question of who labels them
- [[class-stratified-scheduled-noise-uncertainty-sampling]] — another way of choosing a query set under a budget, along a different axis: class balance rather than labeler quality

[^a1]: arxiv-2512-12870 — "We also assume that each query point should be labeled only one time using one labeler"
[^a2]: arxiv-2512-12870 — "minimize the maximum generated noise among all"
[^a3]: arxiv-2512-12870 — "a worst-case rather than average-case criterion"
[^a4]: arxiv-2512-12870 — "should be assigned to the labeler with the highest accuracy"
[^a5]: arxiv-2512-12870 — "will guarantee the lowest maximum noise generated among all possible assignments"
[^a6]: arxiv-2512-12870 — "the solution to the optimal assignment is independent of the structure of the noise model"
[^a7]: arxiv-2512-12870 — "alone captures nearly all of the benefit"
[^a8]: arxiv-2512-12870 — "close to the strongest method in the comparison, ES+OLA, at 0.690"
[^a9]: arxiv-2512-12870 — "clearly and consistently outperform every method that does not use optimal labeler"
[^a10]: arxiv-2512-12870 — "ES+RLA reaches 0.671"
[^a11]: arxiv-2512-12870 — "leads to a qualitatively different modeling regime"
[^a12]: arxiv-2512-12870 — "relative differences in labeler reliability rather than exact values"
