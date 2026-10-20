---
description: "Under RL with a correctness reward, the likely correct solutions are reinforced most and gain most, so the correct set sharpens and loses diversity; the paper states this as two propositions."
aliases: ["selection and reinforcement bias", "diversity collapse from correct-trajectory reinforcement", "base-probability reinforcement bias"]
sources: ["arxiv-2511-19942"]
---
# Selection and reinforcement bias

Vanilla RL fine-tuning, in the paper's abstraction, maximises expected reward minus a KL penalty to the base model. The paper's account of why this narrows outputs is that it "disproportionately reinforces correct trajectories that are already high-probability under the base LLM."[^r1] The narrowing is named diversity collapse, and it comes from two biases that act on the correct set.

The first is selection. Among correct trajectories, those with higher base probability are more likely to gain probability. The paper's Proposition 3.1 says it as a monotone statement: "among correct trajectories, those with higher base probabilities are more likely to be reinforced," so that a higher base probability gives a higher chance that the trained policy exceeds the base on that trajectory.[^r2]

The second is reinforcement. The size of the gain also scales with base probability. Proposition 3.2 gives the scaling: if the reward update has access to the complete set of correct trajectories, the gain for a correct trajectory is proportional to its base probability.[^r3] The paper's sentence on the mechanism is "Reinforcement bias then arises because these same trajectories receive" disproportionately larger updates.[^r4]

Together they push mass toward the solutions the base model already favours, within the correct set. The paper's derivation rests on a closed form for the KL-regularised optimum: "Since Lemma B.1 implies that" the optimal policy is proportional to the exponential of reward over the temperature, so the base probability enters as the prior the reward reweights.[^r5] The reweighting is the same for every correct answer; what differs is each answer's starting weight.

The bias is one-sided. The paper states that "the analysis of reinforcement and selection biases pertains specifically to correct trajectories."[^r6] On the incorrect side, "incorrect trajectories exhibit an inverse dynamic," and the distribution over them is flattened rather than sharpened.[^r7] So the collapse the theory describes is a collapse of the correct set, not of the whole output distribution. That is why the paper's later remedy acts only on correct trajectories.

## Limits

- The propositions are proved in the paper's abstraction: a token-level process with a binary reward, a verifier that labels a sampled set of trajectories, and a KL-regularised objective. The paper says "A verifier then identifies the subset of successful trajectories," so the correct set is the set the verifier finds in the samples, not all correct trajectories.[^r8] Proposition 3.2 assumes the reward covers the complete set of correct trajectories, which a finite sample does not supply.
- The proofs sit in the paper's Appendix B, which I did not read. What is stated here is the proposition text and its use in the argument; the derivation is not checked (my reading).
- The propositions describe the shape of the trained distribution, not the Pass@K curve. The link to Pass@K is the paper's claim that RL-tuned models "can even underperform the original base model" on Pass@K, which it takes from earlier work rather than from its own proof.[^r9]
- Base probability is a proxy for what the bias favours. Nothing here says that base probability tracks answer quality, so a correct but low-probability solution is the one the mechanism loses. Whether that loss matters depends on the task, which is [[solution-multiplicity]]'s question (my inference).
- The mechanism is a bias of the objective, so it is not specific to one training algorithm; but the paper does not test a different objective in the parts I read, so whether other RL variants show the same ordering is open.
- It is one mechanism for the collapse. [[rlvr-entropy-collapse]] attributes the same fall in entropy to a covariance between a token's log-probability and its advantage, a first-order account at the token level. The two accounts were not compared in the parts I read, and they may be two views of one effect (my inference).

## Related

- [[rlvr-entropy-collapse]] — a covariance account of the same downward drift in entropy, at the token level
- [[consensus-reward-tilting]] — another KL-regularised reward whose optimum tilts a reference distribution toward its mode; there the reward is agreement, here it is correctness
- [[solution-multiplicity]] — the task property that decides whether countering this narrowing with an entropy term is worth what it costs in correctness

[^r1]: arxiv-2511-19942 — "disproportionately reinforces correct trajectories that are already high-probability under the base LLM"
[^r2]: arxiv-2511-19942 — "among correct trajectories, those with higher base probabilities"
[^r3]: arxiv-2511-19942 — "if the reward update mechanism has access to the complete set of correct trajectories"
[^r4]: arxiv-2511-19942 — "Reinforcement bias then arises because these same trajectories receive"
[^r5]: arxiv-2511-19942 — "Since Lemma B.1 implies that"
[^r6]: arxiv-2511-19942 — "Crucially, the analysis of reinforcement and selection biases pertains specifically to correct trajectories."
[^r7]: arxiv-2511-19942 — "incorrect trajectories exhibit an inverse dynamic"
[^r8]: arxiv-2511-19942 — "A verifier then identifies the subset of successful trajectories"
[^r9]: arxiv-2511-19942 — "underperform the original base model"
