---
description: "Each rubric criterion is reduced to within-group win, tie and loss outcomes, fitted to a Bradley-Terry latent utility, and only then fused, so raw score magnitudes never enter the reward."
aliases: ["RLVR2", "verifiable ranking reward", "within-group ordinal reward aggregation", "criterion-wise Bradley-Terry utility fusion"]
sources: ["doi-10-48550-arxiv-2609-23457", "doi-10-48550-arxiv-2610-00389"]
---
# Within-group ordinal utility aggregation

A rubric scores each rollout on several criteria, while policy optimization takes one scalar per rollout. The usual bridge maps every criterion onto a common range and takes a weighted average. That quietly assumes a unit of one criterion is worth a unit of another. The work's objection is that the assumption fails when criteria are semantically different: "a binary compliance rubric and a continuous coverage rubric do not express quality in the same units."[^c1]

The alternative keeps only the order a criterion induces among the rollouts of one query. For each pair of rollouts in a group and each criterion, the outcome is 1 if one rollout beats the other by more than a tie margin, 0 if it loses, and 0.5 if the two lie within the margin; the margin is zero for discrete criteria. "Only thresholded within-group ordering is retained, while the raw score gap is discarded."[^c2]

The pairwise outcomes of one criterion are fitted to a [[bradley-terry-preference-model]], which gives each rollout a latent utility for that criterion. A tie enters as a half-win target, pushing the predicted probability toward one half.[^c3] The criterion utilities are then summed with the rubric weights, and the result is normalized within the group, so the best rollout in a group sits at 1 and the worst at 0.[^c4] The mechanism therefore has three stages: ordinal outcomes per criterion, a utility per criterion estimated from those outcomes, and a weighted sum of utilities. The weight is left to say how much a criterion matters, since no cross-criterion scale calibration is needed.

## What was measured

The property the work tests is invariance to monotone rescaling of a single criterion. In a replay over retained groups of exactly eight unique responses,[^c5] the authors multiply one criterion's scores by 10, remap another's levels from (0, 0.2, 1) to (0, 1, 100), and square a third. They compare raw cardinal summation, group-wise z-score normalization, and the ordinal scheme on whether the sign and the ordering of the fused reward survive. The invariance claim is conditional: it holds "preserving the pairwise outcome matrix, including any tie decisions."[^c6] A transformation that moves a tie boundary, with a nonzero margin, is "outside the strict invariance claim."[^c7]

The main claim is empirical and belongs to the paper: across three model scales and 16 benchmarks the method is reported to outperform the rubric-based RLVR baselines it was compared with.[^c8] Those numbers were not checked here.

Why the invariance holds is my inference, not the paper's stated proof. A monotone rescaling of one criterion leaves that criterion's pairwise order untouched, and the Bradley-Terry fit uses only that order, so the fitted utilities stay the same unless a tie boundary moves.

## Limits

- The invariance is an identity over the outcome matrix, not over the reward. Only ties that stay put are protected; the tie margin is a criterion-specific parameter whose effect on training the work does not isolate in the parts read.
- The normalization in the final step is relative to the group. A rollout gets 1 when it is best among its siblings, whatever their absolute quality (my inference). A group of uniformly poor responses still spreads across the full range.
- The method removes scale calibration but not the choice of criterion weights. The work says the weight should "reflect criterion importance rather than scale correction," and does not say how to set it.
- The non-compensatory case is handled outside this scheme. The paper's gate sends "a failure of the global-quality condition" to "a hard gate," and a low-quality layer to a soft penalty.[^c9] That is a separate mechanism, and it is what the note on [[compensatory-leakage]] describes as the failure it has to address.
- I read the method, the invariance replay and the abstract. I did not read the cost analysis or the full benchmark tables.

## Related

- [[bradley-terry-preference-model]] — the model fitted here per criterion, to within-group rollout outcomes rather than to human pairs
- [[multi-objective-advantage-aggregation]] — the other route: discretize and z-score each objective, then average advantages; it fixes comparability after normalization, where this scheme never builds a cardinal scale
- [[compensatory-leakage]] — the flaw of linear sums that the gate in the same paper is meant to stop
- [[covariate-adjusted-comparison-reward]] — the same within-group comparison model, extended with non-objective attributes such as length and formatting
- [[rollout-rubric-win-matrix]] — a sibling that keeps the raw pairwise win fraction per rubric with no per-criterion utility fit, and fuses rubrics by distance to observed ideal profiles instead of a weighted sum[^c10]

[^c1]: doi-10-48550-arxiv-2609-23457 — "a binary compliance rubric and a continuous coverage rubric do not express quality in the same units"
[^c2]: doi-10-48550-arxiv-2609-23457 — "Only thresholded within-group ordering is retained, while the raw score gap is discarded."
[^c3]: doi-10-48550-arxiv-2609-23457 — "A tie outcome ok (i, j) = 0.5 is treated as a half-win target, encouraging the predicted probability"
[^c4]: doi-10-48550-arxiv-2609-23457 — "we fuse the criterion-specific utilities and normalize them within the rollout group"
[^c5]: doi-10-48550-arxiv-2609-23457 — "We retain groups with exactly G = 8 unique responses"
[^c6]: doi-10-48550-arxiv-2609-23457 — "preserving the pairwise outcome matrix, including any tie decisions."
[^c7]: doi-10-48550-arxiv-2609-23457 — "such transformations are outside the strict invariance claim."
[^c8]: doi-10-48550-arxiv-2609-23457 — "Across three model scales and 16 benchmarks, RLVR2 consistently outperforms a broad"
[^c9]: doi-10-48550-arxiv-2609-23457 — "A failure of the global-quality condition triggers a hard gate,"
[^c10]: doi-10-48550-arxiv-2610-00389 — "rubric-wise pairwise judgments retain a separate win-rate profile for each response"
