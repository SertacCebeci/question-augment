---
description: "A token-level KL penalty adds one term per sampled token but one per decision, so in policy-gradient training it constrains the sampling stage far more than the decision stage."
aliases: ["gradient attribution property", "balanced versus unbalanced gradient attribution", "length-weighted KL asymmetry"]
sources: ["arxiv-2601-01580"]
---
# Length-weighted KL attribution

In GRPO-style and PPO-style RLHF, the penalty that keeps the trained policy near a reference model is usually applied per token and added to the reward. The work takes this placement as its object: "we consider the token-level KL" penalty added to the reward, in the usual way.[^c1] The question is how a single reward signal, passed through such a penalty, reaches the two stages of a reasoning policy (see [[two-stage-decision-sampling]]).

The work proves a contrast. For a simple surrogate reward, the group-relative advantage is one scalar per trajectory, and it multiplies the gradient of both stages in the same way. The sufficient statistic that carries future value "is scale-invariant: it enters both Q-values as an" identical factor, so the reward is attributed to each stage on equal footing; the argument is that "There is no action-specific immediate reward that could create magnitude asymmetry".[^c2] This is called balanced attribution.

Adding the token-level KL penalty breaks the symmetry by counting, not by reward. A sampling action contributes one log-ratio term per token of its trace, while a decision action contributes one term. The decision's immediate reward is "scalar", a single number per decision.[^c3] With traces of hundreds of tokens, the sampling penalty is a sum of order L_k and the decision penalty is of order one, so the ratio of their magnitudes is about L_k: "systematic gradient magnitude asymmetry".[^c4] The work notes that this does not depend on how the importance ratio is clipped: "it arises from the token-level" summation, so "The unbalanced gradient phenomenon therefore persists" under clipped objectives.[^c5] The stated consequence is that the penalty "heavily constrains πsample while leaving πd underoptimized".[^c6]

The same accounting is applied to SFT, which the work treats as close to a KL divergence between the model and the data distribution: "SFT operates similarly to a KL-divergence".[^c7] On this reading the SFT objective regularises the sampling stage without giving the decision stage a reward-shaped signal. This is the work's mechanism for why RL-trained models learn to reject wrong answers and SFT-trained ones do not. It is a claim about where gradient mass lands, not a measured change in any internal module.

## Limits

- The main-text argument is a proof sketch with a binary STOP/RESAMPLE decision. The work says "See Appendix A.2 for complete proof"; I did not read that appendix, so the general statement is only as checked as the sketch.[^c8]
- The analysis deliberately simplifies the algorithm. "Our theoretical analysis abstracts away clipping and trustregion constraints to preserve tractability."[^c9] The clipped-ratio argument is a remark, not a full derivation.
- The asymmetry depends on long traces. The work's premise is that "reasoning traces have Lk ≫ 1 (hundreds of tokens".[^c10] For short traces the ratio L_k is small and the argument weakens; the work does not quantify where that happens.
- The surrogate is analysed "for tractability; practice uses clipped variants for stability."[^c11] Real GRPO runs may behave differently.
- The reward is binary correctness. "We analyze binary correctness rewards" and other reward structures "may differ and warrant separate investigation".[^c12]
- The experiments compare RL with SFT overall; they do not isolate the KL term, for instance by removing it or moving it into the advantage. A KL-only ablation was in an appendix table I did not read, so I cannot say what it shows. Ablations in other work sometimes report that a KL penalty hurts, which may confound this account (see [[per-problem-reasoning-pattern-selection]]).
- Other explanations of the RL/SFT gap, such as on-policy sampling of the training data, are not compared against this one in the slices I read (my inference).

## Related

- [[two-stage-decision-sampling]] — the decomposition whose two stages this asymmetry concerns
- [[kl-divergence]] — the divergence itself; this note is about where its token-level sum enters a training objective
- [[post-rl-sft-calibration-restoration]] — another account of how RL and SFT differ, in terms of confidence calibration rather than gradient attribution
- [[per-problem-reasoning-pattern-selection]] — its ablation reports a KL penalty hurting, a possible confound for any claim about KL placement

[^c1]: arxiv-2601-01580 — "we consider the token-level KL"
[^c2]: arxiv-2601-01580 — "There is no action-specific immediate reward that could create magnitude asymmetry"
[^c3]: arxiv-2601-01580 — "The immediate reward for decisions is scalar"
[^c4]: arxiv-2601-01580 — "systematic gradient magnitude asymmetry"
[^c5]: arxiv-2601-01580 — "The unbalanced gradient phenomenon therefore persists"
[^c6]: arxiv-2601-01580 — "heavily constrains πsample while leaving πd underoptimized"
[^c7]: arxiv-2601-01580 — "SFT operates similarly to a KL-divergence"
[^c8]: arxiv-2601-01580 — "See Appendix A.2 for complete proof"
[^c9]: arxiv-2601-01580 — "Our theoretical analysis abstracts away clipping and trustregion constraints to preserve tractability"
[^c10]: arxiv-2601-01580 — "reasoning traces have Lk ≫ 1 (hundreds of tokens"
[^c11]: arxiv-2601-01580 — "We analyze simple surrogate rewards for tractability"
[^c12]: arxiv-2601-01580 — "We analyze binary correctness rewards"
