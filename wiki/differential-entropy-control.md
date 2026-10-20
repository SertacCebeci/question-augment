---
description: "An entropy bonus on correct trajectories and a penalty on incorrect ones, in one reward; the paper argues this lifts correctness and correct-set diversity together, where a global term trades them."
aliases: ["differential smoothing", "DS-GRPO", "differential entropy regularisation", "differential reward modification", "conditional entropy control"]
sources: ["arxiv-2511-19942"]
---
# Differential entropy control

A global entropy term applies one sign to every trajectory. An entropy bonus raises the spread of the policy and, in the paper's words, "Intuitively, entropy bonus improves diversity but at the cost of correctness."[^d1] An entropy penalty does the reverse: it "improves correctness but at the cost of diversity."[^d2] Each is a single dial with a fixed trade, so the choice of sign is forced on the whole output distribution.

The differential form splits the term by correctness. The paper's reasoning starts from what diversity should mean: "we only care about diversity over correct (high reward) trajectories."[^d3] The bonus is therefore applied only where the correct solutions are, and the penalty only where the incorrect ones are. The paper calls this differential smoothing: it "applies an entropy bonus exclusively to positive samples and an entropy penalty exclusively to negative samples."[^d4]

The argument has two parts. First, the reward change on correct trajectories is what targets correct-set diversity: the paper "formally proves that the reward modification for correct trajectories directly optimizes for diversity."[^d5] Second, the penalty on incorrect trajectories can be added without touching that diversity: "an entropy penalty on negative trajectories does not impact the policy" over correct responses.[^d6] Under the paper's theorem, a differential reward reaches correctness and correct-set diversity at least as high as the global bonus, under the same proximity constraint to the base model. The theorem's wording is "there exist parameters" for the differential reward, given parameters for the global one.[^d7] The stated assumption is "Assume the model have correct estimation for the reward of all trajectories."[^d8]

In training, the paper implements this as a change to the advantage in GRPO. For a correct completion it subtracts a log-probability term; for an incorrect one it adds one.[^d9] In practice the base model in the log term is replaced by the behaviour policy from the previous update, "due to its superior stability," while the paper says that "Notably, our analysis remains valid even if" the base model is substituted.[^d10]

On the reported results, the paper states that "We consistently observe that DS-GRPO improves both Pass@1 and Pass@K relative to the vanilla" baseline.[^d11] The largest figure is "on the Mistral-8B model, DS-GRPO outperforms the baseline by up to 6.7%."[^d12] The global terms do better on some tasks than others: the bonus "improves performance on Countdown but hurts performance (and underperforms standard GRPO)" on MATH500, and the penalty is the reverse.[^d13][^d14] The paper reads this as the task dependence that [[solution-multiplicity]] is meant to explain, and the differential form is offered as the way out of choosing a sign.

## Limits

- Theorem 3.4 is an existence claim. It says some differential parameters match or beat the global bonus on correctness and on the normalised variance over correct trajectories. It does not say the practical hyperparameters, which are free non-negative weights, will find them, or that they are optimal.
- The diversity measure is a normalised variance of the policy's probabilities over the correct set. A small variance is said to mean "the probability distribution is more uniform," which is a proxy; the Pass@K gains are measured separately.[^d15]
- The theory is in the paper's abstraction, with a binary reward and an assumed correct reward estimate. Real verifiers make mistakes, and the reward here has no partial credit; whether the result extends to graded rewards is not shown (my inference).
- The implementation is not the theory. It replaces the base model with the behaviour policy, a choice the paper justifies by stability, not by the proof. The text says the analysis "remains valid" under that substitution; the stability claim is empirical.
- The paper's own description of its scope is inconsistent. The abstract says it ran "models from" a size range, and the text gives "1B to 7B parameters"; the introduction says the models run "from 1.5B-8B."[^d16] I did not resolve which set was used.
- The evaluation covers Countdown and mathematical reasoning, with the best reported gain on AIME24. The comparison set is a few diversity heuristics; no other domain is tested in the parts I read, and the paper's claim that the method is "universally superior" is a claim from its theory and these tasks, not from broader evidence.[^d17]
- The sign rule for global terms is the paper's own finding on four tasks; [[solution-multiplicity]] carries the same limit.

## Related

- [[selection-reinforcement-bias]] — the bias on the correct set that the bonus on correct trajectories is built to counter
- [[solution-multiplicity]] — the task property that decides which global sign helps, and which the paper's differential form is meant to make unnecessary
- [[rlvr-entropy-collapse]] — the same entropy fall, approached by a covariance account and a per-token rule
- [[entropy-covariance-token-selection]] — a token-level selection rule in the same literature, where the differential form works at the level of trajectories and their correctness
- [[entropy]] — the quantity whose sign the terms set; here the term is applied to the log-probability of whole trajectories

[^d1]: arxiv-2511-19942 — "Intuitively, entropy bonus improves diversity but at the cost of correctness."
[^d2]: arxiv-2511-19942 — "entropy penalty does the reverse and improves correctness but at the cost of"
[^d3]: arxiv-2511-19942 — "we only care about diversity over correct (high reward) trajectories"
[^d4]: arxiv-2511-19942 — "which applies an entropy bonus exclusively to positive samples and an entropy penalty"
[^d5]: arxiv-2511-19942 — "formally proves that the reward modification for correct trajectories directly optimizes for"
[^d6]: arxiv-2511-19942 — "an entropy penalty on negative trajectories does not impact the policy"
[^d7]: arxiv-2511-19942 — "there exist parameters"
[^d8]: arxiv-2511-19942 — "Assume the model have correct estimation for the reward of all trajectories"
[^d9]: arxiv-2511-19942 — "exclusively to negative samples"
[^d10]: arxiv-2511-19942 — "due to its superior stability"
[^d11]: arxiv-2511-19942 — "We consistently observe that DS-GRPO improves both Pass@1 and Pass@K relative to the vanilla"
[^d12]: arxiv-2511-19942 — "on the Mistral-8B model, DS-GRPO outperforms the baseline by up to 6.7%"
[^d13]: arxiv-2511-19942 — "entropy bonus improves performance on Countdown but hurts performance (and underperforms standard GRPO)"
[^d14]: arxiv-2511-19942 — "entropy penalty in fact improves performance on MATH500, while underperforming on Countdown"
[^d15]: arxiv-2511-19942 — "A small normalized variance indicates that the probability distribution is more uniform"
[^d16]: arxiv-2511-19942 — "1B to 7B parameters"
[^d17]: arxiv-2511-19942 — "differential smoothing is universally superior"
