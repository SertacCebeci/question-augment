---
description: "Training an answerer to ignore spurious prompt cues works when the cue is made non-predictive of reward: balanced correct/wrong cue pairing plus a bias penalty with no bonus for agreement."
aliases: ["Epistemic Independence Training", "EIT", "balanced conflict strategy", "making bias non-predictive"]
sources: ["arxiv-2602-01528"]
---
# Non-predictive cue training

A model leans on a cue (a claimed consensus, an authority appeal) because, in training, the cue correlated with reward. The claim of this work is that the dependence is removed at the objective, not at the surface: the cue must carry no information about which answer is rewarded.[^c1] If a cue predicts correctness even weakly, an optimal policy may rationally exploit it; if it gives no directional advantage, the only viable strategy is task-relevant reasoning.[^c2]

## Mechanism

**Operational target.** Epistemic independence is defined as invariance of the output to the injected cue, P(Y | X, B) = P(Y | X) for all B. The authors scope this to prompt-level influence cues only.[^c3]

**Balanced conflict data.** Each cue supports the correct answer in 50% of training samples and an incorrect answer in 50%. Under that distribution any policy conditioning on the cue cannot beat one relying on intrinsic reasoning.[^c4]

**Asymmetric reward.** The reward is the sum of a structure term (a format parse check), an accuracy term, and an independence term. When the cue contradicts truth, the independence term gives a bonus for the right answer and a penalty for following the cue. When the cue is right, there is no bonus for being correct and a penalty only for a wrong answer. The missing bonus matters: rewarding agreement there would teach "always follow bias".[^c5] Optimisation is GRPO, on Qwen3-1.7B/4B with MMLU-Pro questions and only a bandwagon cue ("90% of people choose X").[^c6]

**Why the balance matters.** Training on wrong-cue samples only raised wrong-cue accuracy (63.6% to 84.2%) but lowered accuracy when the cue happened to be right (90.4% to 71.2%). That policy learned to oppose the cue, a shortcut that backfires, rather than to ignore it.[^c7] Debiasing prompts cut Qwen3-4B clean accuracy from 66.2% to 40.9%, which the authors read as rejecting helpful and harmful signals alike.[^c8]

**Ablation.** Dropping the independence reward lowered wrong-cue robustness from 80.0% to 65.8%; accuracy-only training was indistinguishable from baseline.[^c9]

**Reported effects.** On Qwen3-4B, adversarial-cue accuracy rose from 70.1% to 83.3%, and a model trained on bandwagon cues alone improved on unseen authority and distraction cues.[^c10]

## Limits

- The guarantee covers only the injected cue; the authors state it does not preclude reliance on other shortcuts present in the data.[^c3]
- Evidence is multiple-choice questions with synthetic cues; nothing here tests open-ended answering or real social pressure across turns.
- The reading that the model "treats bias as noise" is the authors' interpretation of accuracy numbers, not a probed mechanism.
- Small models (up to 8B) and one main training bias type; my inference is that other cue families with correlated truth rates could need their own balancing.
- The balanced 50/50 design requires knowing the correct answer to construct cues, which limits it to verifiable-answer data.

## Related

- [[sycophantic-capitulation]] — the failure being trained against: answers that move with pushback rather than evidence
- [[rlhf-sycophancy-amplification]] — the reward-side origin of cue attraction that this work targets
- [[reasoning-shortcut]] — cue-following as a shortcut; here the shortcut is removed by decorrelating it from reward
- [[option-matching-shortcut]] — another surface regularity a policy exploits when it predicts reward

[^c1]: arxiv-2602-01528 — "to learn independence, bias cues must be made non-predictive of reward"
[^c2]: arxiv-2602-01528 — "If a bias signal predicts correctness—even weakly—an optimal policy may rationally exploit it."
[^c3]: arxiv-2602-01528 — "it does not preclude reliance on other shortcuts that may be present in the data."
[^c4]: arxiv-2602-01528 — "any policy conditioning on the cue cannot achieve higher expected return than one relying on intrinsic reasoning."
[^c5]: arxiv-2602-01528 — "Crucially, there is no bonus for being correct when bias is also correct."
[^c6]: arxiv-2602-01528 — "We train EIT on Qwen3-1.7B and Qwen3-4B using MMLU-Pro"
[^c7]: arxiv-2602-01528 — "the model learns a shortcut that backfires when bias happens to support the correct answer."
[^c8]: arxiv-2602-01528 — "suggesting that debiasing prompts cause models to reject both helpful and harmful signals indiscriminately."
[^c9]: arxiv-2602-01528 — "Removing it drops wrongbias robustness from 80.0% to 65.8%"
[^c10]: arxiv-2602-01528 — "improves adversarialbias accuracy by +13.2% (70.1%→83.3%)"
