---
description: "Normalized weights cannot express confidence shared by a whole group; a separate mean-weight factor lets low group support shrink that group's update, while relative weights set the baseline."
aliases: ["absolute group reliability", "group-wide reliability factor", "mean-weight attenuation"]
sources: ["doi-10-48550-arxiv-2609-36900"]
---
# Absolute reliability sets the update strength

A group-relative advantage is built from weights that are normalized: each rollout's share is its weight over the group total. Normalization removes the level of the weights, and the level is exactly where a group-wide doubt would show. The paper states the gap: "relative weighting alone cannot express common low confidence: multiplying every weight by the same constant leaves normalized weights unchanged."[^b1] A group in which every rollout is doubtful looks, to a purely normalized scheme, the same as a group in which every rollout is trusted. The abstract makes the same point: "post-hoc or purely relative weighting cannot represent group-wide uncertainty."[^b2]

## Mechanism

The paper keeps two jobs apart. The relative shares decide which rollouts shape the baseline (the mechanism in [[reliability-inside-group-baseline]]). A separate factor, the group's mean weight, multiplies the normalized advantage. For a fixed admitted set and with the numerical stabilizer set to zero, multiplying all weights in a group by a constant c in (0, 1] multiplies that group's advantages by c.[^b3] So a group of doubtful rollouts receives a smaller update while its baseline is unchanged. The paper's division of labour is: "relative weights determine which rollouts inform the baseline."[^b4] The factor sets the update strength, and its rationale is that each group's update "remains coupled to the amount of supported reward evidence."[^b5]

The denominator of the policy loss is part of the mechanism. The paper keeps it equal to the original number of groups, and says so because it "makes abstention reduce, rather than renormalize, the reward update."[^b6] A denominator that counted only the admitted groups would cancel the attenuation.

Admission is a second, group-level gate. A group is admitted only when its total weight and its effective size are large enough; the effective size is defined so that it equals the group size for equal weights and falls to one when only one weight is nonzero.[^b7] Groups that fail the gate get zero reward advantage.

The magnitude bound on each advantage holds with or without an exact fit: the advantage stays within the rollout's own weight.[^b8]

## Transfer

What survives the transfer is the argument, not the formula. Any scheme that normalizes group weights before scaling the update has the same blind spot, and an absolute term is the only place a group-wide doubt can enter. What does not survive automatically is the meaning of the factor. The paper's mean weight is informative only because each per-rollout weight is calibrated against trusted data, so that a weight of one means "no detected discrepancy" and not just "a number." Without such calibration the mean is an unlabelled scale (my inference).

The stated rationale also carries a choice that the paper does not test. A group can be doubtful for a legitimate reason, for instance a hard prompt on which the two views disagree honestly. Shrinking that group's update slows learning there. The sections read do not measure this cost (my inference).

## Limits

- The experiments do not isolate this factor. The sections read compare the whole reliability path against a control, and do not report a run in which only the absolute factor is removed (my reading of the sections read).
- The "coupled to supported evidence" wording is the paper's design rationale, not a measured effect.
- The exact scaling by c holds for a stabilizer of zero. The paper's advantage formula adds a stabilizer to the denominator, which changes the scaling by a small amount (my reading of its formula).
- Each method in the experiments has one run, so the size of any effect of this factor has no seed-level uncertainty attached.[^b9]

## Related

- [[reliability-inside-group-baseline]] — the relative half of the same construction, which sets the baseline
- [[group-relative-advantage]] — the normalized advantage that this factor rescales
- [[zero-variance-group-waste]] — a group with no spread gives no learning signal; the same group can also be low in support
- [[paired-view-discrepancy-reliability]] — the per-rollout weights whose group mean is used here

[^b1]: doi-10-48550-arxiv-2609-36900 — "relative weighting alone cannot express common low confidence"
[^b2]: doi-10-48550-arxiv-2609-36900 — "purely relative weighting cannot represent group-wide uncertainty"
[^b3]: doi-10-48550-arxiv-2609-36900 — "multiplying all weights in a group by c"
[^b4]: doi-10-48550-arxiv-2609-36900 — "relative weights determine which rollouts inform the baseline"
[^b5]: doi-10-48550-arxiv-2609-36900 — "remains coupled to the amount of supported reward evidence"
[^b6]: doi-10-48550-arxiv-2609-36900 — "makes abstention reduce, rather than renormalize,"
[^b7]: doi-10-48550-arxiv-2609-36900 — "Geff = 1 occurs when only one weight is nonzero"
[^b8]: doi-10-48550-arxiv-2609-36900 — "The resulting advantage satisfies"
[^b9]: doi-10-48550-arxiv-2609-36900 — "Each method has one run"
