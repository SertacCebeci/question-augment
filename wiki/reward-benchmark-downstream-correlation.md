---
description: "Reward benchmark validity measured as rank agreement between its accuracy ranking of reward models and the ranking of the policies those models produce under best-of-N and PPO."
aliases: ["proxy gap", "benchmark-downstream rank correlation", "reward benchmark validity"]
sources: ["doi-10-48550-arxiv-2604-07343", "arxiv-2512-23067"]
---
# Reward benchmark downstream correlation

A reward benchmark ranks reward models by how often each one prefers the chosen answer in a pair. Its claim to be useful rests on something it does not measure directly: whether that ranking predicts which reward model, used to steer a policy, yields better outputs. The authors name the gap between the two "the proxy gap", which is the discrepancy between a reward model's classification accuracy and the actual quality of the policy it produces.[^d1]

The test is a rank comparison, not a single accuracy. Each reward model is used in two downstream settings with a small fixed policy, Qwen2.5-0.5B-Instruct, which the authors chose deliberately so that differences come from the reward signal and not from the policy.[^d2] In Best-of-N, the policy generates 16 candidates per prompt and the reward model picks the highest-scoring one. In PPO, the reward model fine-tunes the policy. The outputs of either run are scored by an LLM judge (Qwen2.5-32B) against the user's rubric, and that score serves as the downstream ground truth.[^d3][^d4] The benchmark's ranking of reward models is then compared with the downstream ranking using Spearman's rho, plus NDCG, Rank Biased Overlap and weighted Kendall's tau. Spearman weighs the whole list; the other three weight the order of the top models more heavily.[^d5]

On this test the paper reports that its benchmark outperforms the personalized baselines, PersonalRewardBench variants built from Chatbot Arena and PRISM, across correlation metrics.[^d6][^d7] The reported Spearman values are 0.2571 for Best-of-N and 0.3714 for PPO, and the NDCG for Best-of-N is 0.9180.[^d8][^d12] The authors read this as evidence that "accuracy on Personalized RewardBench is a faithful predictor of how a reward model will steer a policy".[^d13] My reading: the absolute Spearman values are modest, and the correlation is shown only against other personalized benchmarks.

A parallel result sits in another note: verifier accuracy on process-outcome items tracks policy performance with a strong linear fit across five verifiers, [[process-outcome-consistency-verification]]. The same question, whether a static accuracy predicts a trained policy, is asked there with more verifiers and a different domain.

A second paper asks the same question under reward-guided decoding (RGD), where a personal reward steers generation from a single base policy at inference time, without per-user fine-tuning.[^d15] It defines policy accuracy on the scoring function used at generation time, as a per-user share of preference pairs that this scorer ranks correctly.[^d14] On a simple style-preference dataset, upstream reward-model accuracy correlates only weakly with downstream policy accuracy; the authors summarise the finding as a lack of correlation.[^d16] The link weakens as model scale grows.[^d17] Method rankings can also reorder between the two evaluations, so a reward method that ranks first upstream need not rank first downstream.[^d18] Their practical finding sits beside this one: simple in-context learning with retrieved demonstrations outperforms the reward-guided methods at 3B parameters and above.[^d19]

## Limits

- The number of reward models in the downstream rankings is not stated in the text I read. Without it the rho values cannot be weighed against sampling error here. The authors cite 95% Wilson intervals in an appendix I did not read, and that appendix is where the robustness claim lives.[^d9]
- The policy is a 0.5B model. Its outputs under PPO, and the ranking it induces, may not transfer to a larger policy. The authors chose the small model to isolate the reward signal; they do not test the transfer.
- The ground truth is itself a judge. The judge's agreement with human ratings is high, "97.5% directional agreement" on the benchmark pairs, but that agreement is measured on the benchmark pairs, not on the downstream outputs.[^d10]
- The comparison set in the read tables is personalized baselines only. A claim about reward benchmarks in general would need general benchmarks in the same comparison, and none appears in the slices I read.
- The paper says that baseline signals "degrade further during PPO training" while its own metrics increase, and calls the benchmark "a stable and actionable training objective."[^d11] That is an interpretation of a few numbers, and "actionable" is not tested here.
- The value of a rank correlation depends on how many models are compared. With few models, a single swap changes Spearman and NDCG a lot; this is my reading, not a measured effect in the paper.
- The second paper's policy accuracy scores responses that already exist. The authors say it measures how well the scoring function ranks static responses, not whether the policy generates aligned output, so a scorer that ranks well can still steer generation poorly.[^d20] My reading: the generation test on user-authored completions is a separate measurement, and the two should not be merged.
- The second paper reads its negative correlations with generation quality as a sign of reward hacking. The text I read does not isolate that cause.[^d21] The mechanism it invokes is the one in [[reward-overoptimization]].
- The second paper's limitations section is empty in the extracted text, and its correlations come from one style dataset and a few model scales. How far they generalise is not shown there. My reading.

## Related

- [[personal-rubric-reward-gap]] — the benchmark whose accuracy ranking is tested here against downstream outcomes.
- [[process-outcome-consistency-verification]] — verifier benchmark accuracy against policy performance in a different domain.
- [[real-query-distribution-transfer-failure]] — a benchmark validated as a stand-in by rank correlation with a production target; the same validity check, a different target.
- [[rubric-option-position-bias]] — judge position bias changes the top-1 candidate, so it enters best-of-N selection and rubric-based reward alike.
- [[reward-model-bias-linear-tractability]] — reward-model length bias affects which candidate Best-of-N selects, a reason a benchmark's accuracy may not match its downstream effect.
- [[reward-overoptimization]] — the reward-hacking account the second paper uses to read negative correlations with generation quality.

[^d1]: doi-10-48550-arxiv-2604-07343 — "the actual quality of the policy it produces"
[^d2]: doi-10-48550-arxiv-2604-07343 — "we deliberately employ a lightweight policy model"
[^d3]: doi-10-48550-arxiv-2604-07343 — "the policy generates N = 16 candidate responses per prompt"
[^d4]: doi-10-48550-arxiv-2604-07343 — "This evaluation score serves as the ground truth proxy for response quality"
[^d5]: doi-10-48550-arxiv-2604-07343 — "the correct ordering of high-performing models while discounting discrepancies among"
[^d6]: doi-10-48550-arxiv-2604-07343 — "Personalized RewardBench significantly outperforms existing"
[^d7]: doi-10-48550-arxiv-2604-07343 — "a personalized evaluation set derived from Chatbot Arena"
[^d8]: doi-10-48550-arxiv-2604-07343 — "in both BoN (0.2571) and PPO (0.3714) settings"
[^d9]: doi-10-48550-arxiv-2604-07343 — "95% Wilson confidence intervals confirming that these rankings are"
[^d10]: doi-10-48550-arxiv-2604-07343 — "97.5% directional agreement, rising to 99.7% when ties are excluded"
[^d11]: doi-10-48550-arxiv-2604-07343 — "While baseline signals degrade further during PPO training"
[^d12]: doi-10-48550-arxiv-2604-07343 — "it achieves an NDCG of 0.9180"
[^d13]: doi-10-48550-arxiv-2604-07343 — "accuracy on Personalized RewardBench is a faithful predictor of how a reward model will steer a policy"
[^d14]: arxiv-2512-23067 — "the scoring function used at generation time"
[^d15]: arxiv-2512-23067 — "maintaining a single base policy"
[^d16]: arxiv-2512-23067 — "RM accuracy is uncorrelated with policy accuracy (𝜏 = 0.08-0.31)"
[^d17]: arxiv-2512-23067 — "degrading as scale increases"
[^d18]: arxiv-2512-23067 — "method rankings can completely invert between"
[^d19]: arxiv-2512-23067 — "dominating all reward-guided methods"
[^d20]: arxiv-2512-23067 — "Policy accuracy measures how well the scoring function ranks static"
[^d21]: arxiv-2512-23067 — "the negative correlations suggesting reward hacking"
