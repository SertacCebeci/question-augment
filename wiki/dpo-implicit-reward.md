---
description: "DPO writes the reward as beta times the log ratio of policy to reference, so the partition function cancels and preference learning needs no separate reward model."
aliases: ["implicit reward", "DPO reparameterization", "reward as log policy ratio", "implicit KL regularization"]
sources: ["arxiv-2601-06108"]
---
# DPO implicit reward

Standard RLHF maximizes a reward while penalizing a KL divergence from a reference policy, with a weight β.[^c1] That objective has a closed-form optimum: the reference policy reweighted by the exponential of reward over β, normalized by a partition function Z(x) that sums over responses to the prompt.[^c2] The work calls this "the foundation of direct preference optimization methods."[^c3]

Inverting that closed form expresses the reward through the policy. The reward equals β times the log ratio of the optimal policy to the reference, plus β log Z(x). The second term depends only on the prompt, so it is the same for both responses being compared and cancels in the preference probability. The work says so directly: "The partition function Z(x) cancels in the preference probability, enabling reward-free optimization."[^c4] Substituting this into the Bradley-Terry model gives the DPO loss, a log-sigmoid of β times the difference between the policy-to-reference log ratios of the preferred and dispreferred responses. The reward model is no longer trained; the policy carries the reward implicitly.

Call the quantity r_θ(y) = β log(π_θ(y|x)/π_ref(y|x)) the implicit reward. The work defines it as "where rθ (y) = β log(πθ (y|x)/πref (y|x)) is the implicit reward."[^c5] Its regularization is different from PPO's. In PPO the KL term sits inside the reward during training. In DPO "the KL constraint is implicit:" it is satisfied at the optimum rather than enforced along the way.[^c6] The work's consequence is that "This distinction explains why DPO can overfit more easily than PPO," because the regularization does not "constrain intermediate iterates."[^c7]

The reference policy also carries weight. The implicit reward "is undefined for y where πref (y|x) = 0," and it is "poorly calibrated where πref (y|x) is small."[^c8]

## Limits

- The reparameterization holds only if the policy takes the optimal form. The work notes that its derivation "assumes the policy takes the" optimal form, and that this implicit regularization has different properties from the explicit one.[^c9]
- The DPO loss inherits the Bradley-Terry assumptions on the preference data; the reparameterization says nothing about whether those hold (see [[bradley-terry-preference-model]]).
- The work gives no experiment on the reparameterization. The overfitting claim is a reading of the optimum-only regularization, not a measured effect in this work.
- The reference sensitivity is stated qualitatively; no bound on the miscalibration is given.
- The work mentions alternative f-divergences as other regularizers but does not derive how the implicit reward changes under them.

## Related

- [[bradley-terry-preference-model]] — the preference model that the reparameterization is substituted into
- [[coverage-separation-offline-online]] — the offline DPO loss is defined on the implicit reward, and its convergence depends on coverage
- [[reward-overoptimization]] — DPO's implicit reward is reported to show the same overoptimization pattern as an explicit reward model
- [[length-weighted-kl-attribution]] — the PPO-side placement of a token-level KL, where the penalty is explicit rather than implicit
- [[kl-divergence]] — the divergence that the objective penalizes, in both its explicit and implicit forms

[^c1]: arxiv-2601-06108 — "max Ex∼D,y∼π(·|x) [r(x, y) − βKL(π(·|x)∥πref (·|x))]"
[^c2]: arxiv-2601-06108 — "where Z(x) = y πref (y|x) exp(r(x, y)/β) is the partition function."
[^c3]: arxiv-2601-06108 — "the foundation of direct preference"
[^c4]: arxiv-2601-06108 — "The partition function Z(x) cancels in the preference probability, enabling reward-free optimization."
[^c5]: arxiv-2601-06108 — "where rθ (y) = β log(πθ (y|x)/πref (y|x)) is the implicit reward."
[^c6]: arxiv-2601-06108 — "In DPO, the KL constraint is implicit:"
[^c7]: arxiv-2601-06108 — "This distinction explains why DPO can overfit more"
[^c8]: arxiv-2601-06108 — "This reward is undefined for y where πref (y|x) = 0,"
[^c9]: arxiv-2601-06108 — "assumes the policy takes the"
