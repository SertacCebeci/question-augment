---
description: "A rubric is rewarded when an independent, frozen proxy that sees only the rubric reaches the correct verdict; this closes the loop on the rubric step that outcome reward leaves unsupervised."
aliases: ["rubric transferability", "proxy-guided rubric verification", "Proxy-GRM"]
sources: ["arxiv-2603-16600"]
---
# Proxy-verified rubric transferability

A generative reward model writes a rubric, then a criterion-by-criterion evaluation, then a verdict. Training usually rewards only the verdict, so the rubric is never checked and "models may learn to produce rubrics that rationalize a pre-determined answer rather than guide principled" judgment.[^c1] The work defines rubric transferability: a rubric is good if an independent evaluator, given only the inputs and that rubric, also reaches the correct preference.[^c2]

## Mechanism

A separate proxy agent is trained only to consume rubrics, never to write them. It takes the query, image, both responses and an external rubric, and returns an evaluation and a verdict. This keeps its verdict from being confounded by its own rubric-writing tendencies.[^c3] During policy RL the proxy is frozen. The reward is accuracy (+1/-1) plus proxy correctness (+1/-1) plus 0.5 times a format term.[^c4]

At inference the proxy can be run as a check. Agreement raises confidence. Disagreement is only logged, because the proxy may be the one that is wrong.[^c5]

## What was measured

- On VL-RewardBench the best configuration reached 75.22% overall, against 73.8% for the previous best open model. It used about 50k training samples, against more than 200k for the baselines.[^c6]
- Rubrics transfer. Unified-Reward-SFT given rubrics from the trained model rose from 66.10% to 69.86% on VL-RewardBench.[^c7]
- An SFT-trained proxy beat an RL-trained proxy on all three benchmarks (75.22% vs 73.38%). The authors attribute this to outcome-RL models having inconsistent evaluation processes, and so giving noisy rubric signals. That explanation is theirs and was not isolated experimentally.[^c8]
- A weak proxy hurts. The 3B proxy fell below the no-proxy baseline on MM-RLHF-Reward Bench (76.48% vs 80.59%), which the authors read as near-random feedback early in RL.[^c9]
- Adding the proxy reward beats using it to modify the accuracy reward. All seven explicit-modification schemes were worse than plain addition. The authors hypothesize credit-assignment confusion.[^c10]

## Limits

- Everything is on pairwise preference for vision-language reward models with one 7B base. Nothing is shown for questioning or answering tasks.
- The proxy reward needs a ground-truth preference label, so it verifies rubrics only where labels exist.
- The SFT-over-RL and credit-assignment explanations are hypotheses, not tested mechanisms.
- Transfer was tested on three evaluators from related model families, not on unrelated judges.
- Part of the gain over baselines may come from distillation data and teacher choice rather than the proxy; the ablation without a proxy only partly separates these.

## Related

- [[pretraining-grounded-rubric-self-play]] — another route to rubric quality, by grounding in a document rather than verifying by a second agent
- [[rubric-complexity-normalized-reward]] — rubric-based RL reward that scores criteria but does not check rubric validity
- [[llm-judge-biases]] — biases that an unverified rubric can inherit

[^c1]: arxiv-2603-16600 — "models may learn to produce rubrics that rationalize a pre-determined answer rather than guide principled"
[^c2]: arxiv-2603-16600 — "We define rubric transferability as the property that the generated rubric R is sufficiently informative"
[^c3]: arxiv-2603-16600 — "the proxy agents are trained only to follow rubrics, not to generate them"
[^c4]: arxiv-2603-16600 — "The proxy agent is kept frozen throughout policy training"
[^c5]: arxiv-2603-16600 — "the policy model’s answer is"
[^c6]: arxiv-2603-16600 — "achieves the highest overall accuracy of 75.22% and macro accuracy of 73.93%"
[^c7]: arxiv-2603-16600 — "improves"
[^c8]: arxiv-2603-16600 — "Proxy-SFT outperforms Proxy-RL on"
[^c9]: arxiv-2603-16600 — "indicating that insufficiently capable proxy agents introduce harmful noise into the training signal"
[^c10]: arxiv-2603-16600 — "All explicit modification schemes perform worse than the implicit additive"
