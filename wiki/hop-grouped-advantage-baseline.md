---
description: "Normalising a question-proposer's reward within groups of questions of equal hop count, not within samples of one prompt, cuts rollouts to under a third and keeps a stable baseline."
aliases: ["HRPO", "hop-grouped relative policy optimization", "structure-grouped advantage"]
sources: ["arxiv-2601-07055"]
---
# Hop-grouped advantage baseline

A proposer that writes questions is rewarded by how a solver fares on them. That reward needs several solver attempts per question, so group-relative training (GRPO) of the proposer is costly. Dr. Zero's alternative is to build the baseline from other questions of the same structure.

## Mechanism

With GRPO, a proposer writes m candidate questions per seed prompt, and each gets n solver attempts. That costs m(n+1) rollouts: 4 proposer rollouts and 4x4 solver rollouts, 20 in all.[^c1]

HRPO writes one question per prompt and groups the generated questions across prompts by hop count h. Each advantage is the reward standardised within the h-hop group.[^c2] Hop count is only a grouping variable. Difficulty itself comes from the solver pass rate.[^c3] With five solver predictions this takes 6 rollouts in total.[^c4]

The authors report that a single global baseline (REINFORCE++) became unstable on diverse query structures. They say this gave high-variance gradients and frequent training failures, and that grouping by structure fixed it.[^c5]

The reward being normalised is a pass-rate reward. It is zero when the solver is never or always right. Otherwise it is (n-k)/(n-1), which is maximal when exactly one attempt is correct.[^c6]

In a comparison on the 3B backbone, HRPO reached an average of 0.326 against 0.320 for GRPO, using under a third of the solver rollouts.[^c7] HRPO was better on one-hop sets such as NQ. GRPO kept the lead on multi-hop sets such as HotpotQA.[^c8]

My reading, not a claim of the paper: the same device can be used for any proposer reward whose scale differs by question type. Normalising within type stops the proposer from drifting toward whichever type pays most.

## Limits

- The paper's own caveat is that multi-step tasks may still need more compute for an accurate baseline.[^c9]
- The comparison is one backbone (3B) and aggregate scores differ by 0.006. I did not see a variance estimate for this particular comparison.
- Hop count is the only grouping variable tried. Whether other structure variables work is untested.
- The hop count of each question must be known or estimated. I did not read how that estimate's errors affect training.
- Groups with few members would give noisy standardisation. Group sizes were not examined in what I read.

## Related

- [[zero-variance-group-waste]] — groups whose rewards are all equal give no signal
- [[uncertainty-peaked-challenge-reward]] — another solver-agreement reward for a proposer, normalised by domain
- [[strategy-conditioned-rollout-grouping]] — grouping rollouts by a structural attribute
- [[curriculum-collapse]] — proposer drift that grouping is meant to resist

[^c1]: arxiv-2601-07055 — "requires m + mn = m(n + 1) rollouts."
[^c2]: arxiv-2601-07055 — "HRPO calculates advantages"
[^c3]: arxiv-2601-07055 — "empirical question difficulty is determined by the solver pass rate"
[^c4]: arxiv-2601-07055 — "HRPO requires one proposer rollout and five solver rollouts (6 total)."
[^c5]: arxiv-2601-07055 — "we find that a global baseline becomes unstable when processing diverse query structures."
[^c6]: arxiv-2601-07055 — "the reward is maximized when exactly one solution is correct and decays linearly as the number of"
[^c7]: arxiv-2601-07055 — "The results show that HRPO achieves an average score of"
[^c8]: arxiv-2601-07055 — "one-hop datasets (e.g., NQ), while GRPO retains an advantage on multi-hop benchmarks (e.g., HotpotQA)."
[^c9]: arxiv-2601-07055 — "higher computational resources are still essential"
