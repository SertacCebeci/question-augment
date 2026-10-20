---
description: "Scalar rewards can leave responses near their group mean unordered, so their group-relative advantage can take the wrong sign; a three-way judgment against a reference is offered as a remedy."
aliases: ["advantage flipping", "advantage inversion near the mean", "mean-band advantage sign error"]
sources: ["arxiv-2512-07710"]
---
# Advantage flip near the group mean

In group-relative training, a response's advantage is its reward measured against the other responses sampled for the same prompt. The sign of that advantage tells the update whether to reinforce a response or push it down. The Shopee report says that a scalar reward model can get this sign wrong for responses that sit close to the group mean. The mechanism is given in one clause: reward models trained with the Bradley–Terry loss "often exhibit nonlinear reward curves, making group samples near the mean reward value" incomparable.[^c1] The consequence is stated directly: "This can lead to advantage flipping, where the advantage direction is incorrectly" computed.[^c2] The introduction gives the same effect as "invert advantages near the mean value of group."[^c7]

**Mechanism, concretely.** Take a group of rollouts, each scored by one scalar reward, and subtract the group mean. Rollouts far above the mean and far below it are ordered correctly relative to it. The trouble is the band around the mean. There the scalar values are close, and if the reward model's scale is nonlinear, small true differences in quality are not reliably reflected in the scores. My reading of the paper's claim, which it does not spell out: a response that is in fact slightly better than a neighbour can receive a value just under the mean, and so a negative advantage, while the update still pushes the policy toward the neighbour. The sign of the update is then wrong for that pair, and the error is confined to the band, which is why it is easy to miss in an average reward.

**The remedy the paper chooses.** It changes the judgment rather than the update rule. The reward model is a generative one with chain-of-thought reasoning, which the authors say "also demonstrated higher accuracy than ORM baselines."[^c3] The label set is also changed: "we introduced a three-class comparison scheme," in which an output is "better," "similar," or "worse" "relative to reference answers,"[^c4][^c5] so that outputs at or below the reference level receive consistently ordered scores. The authors say this "fundamentally prevents advantage flipping by ensuring consistent gradient direction."[^c6]

**What transfers to asking and answering (my inference).** The part that survives outside training concerns the judge. A judge asked for a number must place two near-equal responses at distinct points on a scale. A judge asked whether a response is better, similar or worse than a reference can return "similar," which is an honest answer for a close pair. A scalar score cannot express a tie without inventing a gap. This is an argument from the paper's design, not a result the paper measures. A related argument, from a different ablation, is in [[pairwise-judge-over-scalar-reward]].

## Limits

- The paper states the flip and its remedy but does not report how often flips occur in its rollouts, nor how many advantage signs changed. That the flip is common in practice is not established by this text.
- The mechanism is one clause ("nonlinear reward curves", "incomparable") with no derivation and no plot of reward against quality in the part read. The band-around-the-mean reading above is mine.
- The remedy changes three things at once: a chain-of-thought generative judge, a three-class label, and a reference answer per prompt. The text does not separate their effects. The accuracy claim is against ORM baselines, not against a scalar model trained the same way with the same reference.
- The three-class scheme needs a reference answer for each prompt. Where no reference exists, the paper gives no route.
- A sign error near the mean is one defect of the group-relative advantage. A different one, that the magnitude depends only on how many group members were right or wrong, is treated in [[spurious-advantage-grpo]].

## Related

- [[group-relative-advantage]] — the baseline whose sign is at issue: each response is measured against its own group's mean
- [[zero-variance-group-waste]] — the other way a group teaches nothing, when all rollouts tie rather than sit near the mean
- [[pairwise-judge-over-scalar-reward]] — a separate argument that a judge should answer a comparison rather than give a score
- [[bradley-terry-preference-model]] — the pairwise model whose nonlinear reward scale the paper blames for the flip
- [[spurious-advantage-grpo]] — a different defect of the same advantage: its magnitude, not its sign

[^c1]: arxiv-2512-07710 — "making group samples near the mean reward value"
[^c2]: arxiv-2512-07710 — "This can lead to advantage flipping, where the advantage direction is incorrectly"
[^c3]: arxiv-2512-07710 — "which also demonstrated higher accuracy than ORM baselines"
[^c4]: arxiv-2512-07710 — "we introduced a three-class comparison scheme"
[^c5]: arxiv-2512-07710 — "relative to reference answers"
[^c6]: arxiv-2512-07710 — "This design fundamentally prevents advantage flipping by ensuring"
[^c7]: arxiv-2512-07710 — "invert advantages near the mean value of group"
