---
description: "Reasoning models default to one high-level pattern, yet the best pattern differs per problem; training on the verifier-chosen best pattern, with the cue masked, beats any fixed pattern."
aliases: ["reasoning pattern selection", "pattern sub-optimality", "group pattern selection optimization", "GPSO"]
sources: ["arxiv-2601-07238"]
---
# Per-problem reasoning pattern selection

Large reasoning models produce a small repertoire of high-level strategies. In the analysis of Wang et al. (2026), most trajectories fall into three: direct solution, reflection and verification, and exploration of multiple solutions.[^c1] Models default to one of them (usually reflection and verification), but accuracy depends on which pattern is used, and the best pattern varies by problem.[^c2] The authors' headline claim is that a model's default pattern is often not the best one for a given problem.[^c3]

## Mechanism

The oracle gap: when each of three patterns is forced through in-context prompts and the best-scoring pattern per question is taken, accuracy rises well above any single pattern (their Figure 1, on DeepSeek-R1-0528 and Qwen3-8B). The headroom is therefore in choosing, not in reasoning harder.

GPSO (Group Pattern Selection Optimization) turns this headroom into a training signal, extending GRPO in three steps:

1. Multi-pattern rollout. For each prompt, a pattern suffix (direct, reflect, explore, adaptive) is appended and several responses are sampled per pattern.
2. Optimal pattern selection. Each pattern's empirical accuracy under the verifier is computed; the best is chosen, and ties go to the shortest valid reasoning trace.[^c4] Only that pattern's group is used for the policy update.
3. Suffix masking. The pattern tokens get attention mask 0, so they scaffold exploration but cannot shape the representation of other tokens, and the policy must learn the problem-to-pattern mapping internally rather than read it off the prompt.

Reported effect: no fixed pattern wins everywhere (for example explore is best on AIME for one model while reflection is best on MATH500 and GPQA), whereas GPSO-trained models beat the best fixed pattern on every benchmark with default decoding.[^c5] Ablation: removing multi-pattern rollout hurts most (average drop of 5.3 points on one model), removing selection costs a moderate amount, and removing masking slows convergence slightly.[^c6]

Reading for question and answer quality (my inference): the quality of an answer depends on the strategy framing chosen before answering, not only on effort; and the right framing is item-specific, so a single fixed instruction ("always verify") is a bet on the average problem.

## Limits

- Evidence is on verifiable math and science benchmarks, training on DAPO-Math-17K; no open-ended or conversational question types were tested.
- The oracle "Best" per question uses the correct answer, so it is an upper bound, not an achievable selector. GPSO gains are modest (about 2 to 3 points on average).
- Whether the trained model actually picks different patterns per problem, rather than improving generally, is argued from fixed-pattern comparisons, not shown by a direct per-item analysis in the slices I read.
- The pattern inventory is hand-designed (three plus adaptive); the 98 percent coverage is of trajectories, not of all useful strategies.
- The ablation reports a KL penalty hurting, a confound with the pattern claims.

## Related

- [[intent-based-strategy-selection]] — selects a strategy per situation by detected intent, a rule-based analogue of choosing a move per case
- [[entity-agnostic-reasoning-skeleton]] — another way of fixing a reasoning strategy before answering

[^c1]: arxiv-2601-07238 — "98%) of reasoning trajectories can be classified into"
[^c2]: arxiv-2601-07238 — "varies significantly across different reasoning patterns"
[^c3]: arxiv-2601-07238 — "The reasoning patterns chosen by LRMs are not optimal."
[^c4]: arxiv-2601-07238 — "we select the one producing the shortest valid reasoning trace"
[^c5]: arxiv-2601-07238 — "reasoning mode consistently dominates across benchmarks"
[^c6]: arxiv-2601-07238 — "Without rollout, the model struggles to explore diverse"
