---
description: "A rollout's reward is its distance to the group's worst weighted profile over its distances to both ideals, so a gain on one rubric does not automatically cancel a loss on another."
aliases: ["relative-closeness reward", "ideal-solution ranking reward", "positive and negative ideal profiles", "TOPSIS-style reward"]
sources: ["doi-10-48550-arxiv-2610-00389"]
---
# Ideal-solution distance reward

Once the rubric columns are weighted, each rollout is a point in a space with one axis per rubric. The method takes, for each rubric, the largest and the smallest value that any rollout reaches. Together these form two vectors, "the positive and negative ideal profiles," which are "the observed extrema" of the weighted profiles.[^c1] Each rollout i has two Euclidean distances, D⁺ to the positive ideal and D⁻ to the negative ideal, and its quality reward is D⁻ divided by the sum D⁺ + D⁻, a value in [0, 1].[^c2] "If both distances vanish, we assign riqual = 1/2."[^c3]

The columns are scaled before the distances are taken. Each rubric column is "normalized by its Euclidean norm" and then multiplied by its weight, so the weights enter the geometry rather than a later average.[^c4] The weights themselves come from [[dispersion-redundancy-criterion-weights]], and the columns come from the [[rollout-rubric-win-matrix]].

The motivation is the failure of a linear average. The paper says that "a linearly weighted average of rubrics may cause scores across different dimensions to cancel each other out, assigning the same" reward to responses of different quality.[^c5] A distance to two ideals does not sum the coordinates, so a response that is strong on one rubric and weak on another lands at a distance from both ideals rather than at a middling average. The construction follows "ideal-solution ranking" from Hwang and Yoon (2012), a multi-criteria decision method, which the paper adopts rather than derives.[^c6] The paper's summary is that "distances to the ideals distinguish these multidimensional profiles."[^c7]

What was measured: among the variants the paper tests, the best reported result is "with empirical ideals and Euclidean distance, which is MatrixReward."[^c8] Holding the empirical ideals fixed, a Mahalanobis distance in place of Euclidean "narrows the reward distribution," with a standard deviation of "0.20 versus 0.26 across 800 groups."[^c9] That comparison changes only the metric. The paper reports that the Euclidean version gives the strongest benchmark results, but the part of the text read does not isolate how the narrower spread bears on training.

## Limits

- The ideals are the group's own extrema. The best rollout in each column defines the positive ideal and the worst defines the negative one, so the reward is relative to the group. A group of uniformly weak responses still spreads across the full [0, 1] range (my inference; the same property is noted for a related group-normalized scheme in [[within-group-ordinal-utility-aggregation]]).
- Because the ideals are observed rather than theoretical, one unusual rollout moves the ideal that every other rollout is measured against (my inference). The paper's comparison of empirical and theoretical ideals is in a part of the paper I did not read in full.
- A zero column contributes nothing: the paper normalizes "or zero for a zero column" (my reading of the algorithm), and a rubric no rollout separates therefore drops out of the distances.
- The quality reward is only one part of the training reward. "A fixed format-validity reward is added to the quality reward," so a format violation is handled outside the distance.[^c10]
- The distance is Euclidean in weighted rubric space; no argument is given here for why that metric suits every rubric set, and the one alternative tested is Mahalanobis on the same ideals.
- The evidence is one policy model (Qwen3-8B) and four open-ended benchmarks. The comparisons read here do not include a case where the rubric weights are deliberately wrong, so the claim that distances beat linear averages under such errors is untested in this work (my inference).

## Related

- [[rollout-rubric-win-matrix]] — supplies the rows whose weighted profiles are measured against the ideals
- [[dispersion-redundancy-criterion-weights]] — supplies the weights w_k that scale each axis
- [[within-group-ordinal-utility-aggregation]] — another way to avoid a cardinal weighted sum across criteria: per-criterion Bradley-Terry utilities, then a weighted sum
- [[group-relative-advantage]] — the usual group-normalized advantage, which a scalar reward like this one is passed through

[^c1]: doi-10-48550-arxiv-2610-00389 — "The positive and negative ideal profiles are the observed"
[^c2]: doi-10-48550-arxiv-2610-00389 — "A response closer to the positive ideal and farther from the negative ideal receives larger"
[^c3]: doi-10-48550-arxiv-2610-00389 — "If both distances vanish, we assign riqual = 1/2."
[^c4]: doi-10-48550-arxiv-2610-00389 — "normalize each rubric column by its Euclidean norm"
[^c5]: doi-10-48550-arxiv-2610-00389 — "rubrics may cause scores across different dimensions to cancel each other out, assigning the same"
[^c6]: doi-10-48550-arxiv-2610-00389 — "Following ideal-solution ranking"
[^c7]: doi-10-48550-arxiv-2610-00389 — "whereas distances to the ideals distinguish these multidimensional profiles."
[^c8]: doi-10-48550-arxiv-2610-00389 — "with empirical ideals and Euclidean distance, which is MatrixReward."
[^c9]: doi-10-48550-arxiv-2610-00389 — "standard deviation 0.20 versus 0.26 across 800 groups"
[^c10]: doi-10-48550-arxiv-2610-00389 — "A fixed format-validity reward is added to the quality reward"
