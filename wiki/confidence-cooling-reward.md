---
description: "Multiplying a self-reward by a sigmoid of mean token NLL damps gradients from low-reward and overconfident samples, leaving moderately uncertain high-reward ones the strongest signal."
aliases: ["confidence-aware cooling", "cooling weight", "NLL cooling of rewards"]
sources: ["arxiv-2512-22545"]
---
# Confidence-cooling reward

A policy trained on its own reward has no outside check on which of its samples carry information. Two kinds carry little. Samples the reward scores near zero are trivial. Samples the policy already produces with high confidence teach it little that it does not already do. Cooling is a multiplicative damping that targets both at once.

The adjusted reward in the paper takes the self-reward, raised to a power γ, and multiplies it by a sigmoid of a sharpened difference: the sample's average token negative log-likelihood under the current policy, minus a baseline c.[^c1] Read from that formula (my reading of Eq. 8), a sample with near-zero reward gets a near-zero adjusted reward, and a sample whose tokens the policy finds very probable falls below the baseline, so its sigmoid is close to zero. The paper states the purpose: cooling "downweights gradients from two types of" uninformative sample, the trivial and the overconfident.[^c2]

The sample that keeps its gradient is the one that is good by the reward but not yet certain. The paper puts it directly: such samples "obtain the strongest gradient signal."[^c3] The point is that a high-scoring answer the policy already finds obvious is not what the update should push hardest on.

The adjusted reward replaces the raw self-reward in the policy update, where it enters the GRPO loss. So cooling acts inside a critic-free, group-relative update, as a reweighting of each sample's reward, not as an extra loss term.[^c4]

The effect is measured by ablation. Removing cooling "leads to consistent drops (3B: 74.6→72.8; 7B: 81.4→79.6)," and the authors read this as cooling stabilizing training.[^c5] The abstract describes the same mechanism as one that "further stabilizes training and suppresses trivial or overly confident generations."[^c6]

## Limits

- One ablation, one recipe. The sections read compare the full method with and without cooling on Qwen2.5-VL at 3B and 7B. The gap is about 1.8 points on each scale. No spread across runs is reported in those sections (my reading).
- The hyperparameters are named but not swept. The paper gives example values and says that "c are hyperparameters controlling reward scaling, cooling" sharpness and the NLL baseline.[^c7] Whether the gain holds for other baselines is not tested in the sections read.
- Confidence is not correctness. The overconfident case is defined only by low per-token NLL under the same policy. A sample the policy is sure of and gets wrong is cooled exactly as a sure and correct one would be, so the device cannot tell confident errors from confident truths (my inference from Eq. 8).
- The comparison is against no cooling, not against other ways of down-weighting likely samples, so the ablation shows that some damping helps here, not that this form of damping is the right one.
- The gain depends on the underlying self-reward being informative. The paper's own intro flags cross-domain instability of single proxies; cooling does not address that, and the weighting of the signals is a separate device (see [[reliability-weighted-signal-fusion]]).

## Related

- [[reliability-weighted-signal-fusion]] — the other reward-side device in the same method; it weights signals inside a reward, while cooling reweights samples after the reward is formed
- [[answer-reasoning-consistency-reward]] — a reward on the trace-answer link; cooling would act on any scalar reward of this kind, since it needs only a reward and a token likelihood
- [[calibration]] — the NLL here is a confidence signal, and nothing in the paper checks that it is calibrated

[^c1]: arxiv-2512-22545 — "is the average token negative log-likelihood"
[^c2]: arxiv-2512-22545 — "This design downweights gradients from two types of"
[^c3]: arxiv-2512-22545 — "samples obtain the strongest gradient signal"
[^c4]: arxiv-2512-22545 — "Policy update: compute Radj (ŷ) via Eq. (8) and"
[^c5]: arxiv-2512-22545 — "leads to consistent drops (3B: 74.6→72.8; 7B: 81.4→79.6)"
[^c6]: arxiv-2512-22545 — "further stabilizes training and suppresses trivial or overly confident generations"
[^c7]: arxiv-2512-22545 — "c are hyperparameters controlling reward scaling, cooling"
