---
description: "A calibration reward that adds the confidence term separately for correct and incorrect answers, so the worst correct answer always outscores the best wrong one, avoiding Brier-reward accuracy loss."
aliases: ["MSCR", "Margin-Separated Calibration Reward", "strict reward margin calibration"]
sources: ["arxiv-2601-07264"]
---
# Margin-separated calibration reward

When an RL agent must output a verbalized confidence q alongside its answer, the Brier-based reward of Damani et al. (RLCR) is R = 1[correct] - (q - 1[correct])^2. Its lowest reward for a correct answer (q = 0, giving 0) equals its highest reward for a wrong one (q = 0, giving 0). Xuan et al. (2026) say this overlap "may make learning sensitive to the training data distribution".[^c1]

## The reward

MSCR writes the reward as: correct answers get 1 + b1(1 - (1 - q)^2); wrong answers get -b2 q^2, with b1, b2 > 0. The consequence is a strict margin: "correct answers receive a base reward of at least 1 (even with q = 0), while incorrect answers receive at most 0".[^c2] This removes the "safe failure" loophole: a wrong answer stated with zero confidence can no longer tie a correct answer. Calibration still shapes the reward inside each branch. A format penalty is subtracted when the confidence tag is missing.[^c3]

A simpler repair was also tried: down-weight the Brier term by lambda = 1/3, which restores a positive margin but shrinks the calibration signal.

## What was measured

Agents are Search-R1-style, trained with GRPO on NQ plus HotpotQA with Qwen2.5-3B/7B and Qwen3-4B, then tested on in-distribution sets and SimpleQA-verified. Vanilla RLCR (lambda = 1) gave the lowest ECE but "significant accuracy degradation, indicating reward hacking behavior". MSCR "attains higher accuracy than the weighted Brier variant with lambda=1/3 while simultaneously improving calibration" across most settings.[^c4] The authors report ECE relative reductions up to 68% and AUROC relative gains up to 17% for the CAR framework, and generalization from the local Wikipedia retriever to noisy web search and to tool-integrated math.[^c5]

## Limits

The margin argument is a design rationale; the paper shows the accuracy-versus-ECE pattern empirically, not a proof that overlap causes the accuracy loss. "Across most settings" means not all. Values of b1, b2 are tuning knobs and their sensitivity is not the focus here. Tool-integrated math agents kept elevated ECE after training. Only verbalized numeric confidence was trained.

## Related

- [[log-score-verbalized-confidence-reward]] — a different proper-scoring reward for the same output.
- [[accuracy-calibration-gradient-conflict]] — another account of why joint accuracy and calibration objectives trade off.
- [[tool-type-confidence-dichotomy]] — the pilot finding that motivated training on search agents.
- [[calibration]] — the property being rewarded.

[^c1]: arxiv-2601-07264 — "training data distribution."
[^c2]: arxiv-2601-07264 — "correct answers receive a base reward of at least"
[^c3]: arxiv-2601-07264 — "we fall back to a minimal calibration reward"
[^c4]: arxiv-2601-07264 — "significant accuracy degradation, indicating reward hacking behavior"
[^c5]: arxiv-2601-07264 — "with ECE relative reductions of up to 68%"
