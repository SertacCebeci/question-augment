---
description: "Splitting k parallel samples evenly across reasoning modes beats drawing k from a collapsed mixture whenever the modes succeed on different inputs, provided the modes can be controlled."
aliases: ["mode-conditioning", "ModC", "mode-conditioned test-time scaling", "balanced mode allocation", "mode coverage in parallel sampling"]
sources: ["arxiv-2512-01127"]
---
# Mode-balanced sampling

Parallel sampling spends a budget of k independent attempts on one input and keeps a verified answer. Its yield depends on the per-attempt success probability on that input. Fine-tuning and reinforcement learning can push a model onto a few strategies, so a strategy that would solve the input may be sampled almost never. The work names this "diversity collapse, where models concentrate on a few modes and repeated samples produce the same mistakes."[^c1] It says that finetuning and RL are "well-documented to induce diversity collapse, where generations concentrate on only a few dominant modes."[^c2]

The idea is to stop drawing from the collapsed distribution and to divide the budget among the modes instead. "Even when an LLM is balanced across two modes with complementary strengths" the work argues that allocating k/2 samples to each mode does better than k draws from the mixture.[^c3] The argument is a short derivation. Let each mode m have success probability p_m on an input. Splitting the budget evenly gives a Pass@k of one minus the product of the two per-mode failure terms, each raised to the power k/2. A model that does not know which mode is better uses the first mode with a random weight w whose mean is one half. Its single-sample success is then a mixture, and by Jensen's inequality its expected Pass@k cannot exceed the value at w = 1/2. Whenever the two success probabilities differ, the balanced split is strictly higher. In the paper's words, "allocating compute evenly across modes is strictly better than sampling from the model" and its own uncertain mixture.[^c4] The gain sits on inputs where one mode is weaker: "The advantage becomes especially pronounced on inputs where the" dominant mode fails and a lower-probability mode succeeds.[^c5]

The derivation says nothing about how to make a model sample from a chosen mode, and prompting is unreliable here. The paper therefore trains for control in two ways. Separate specialist models are each trained on one partition of the data, and "This design ensures strong specialization and reduces" correlated errors across the budget.[^c6] Alternatively one model is trained with mode-specific prefix tokens, and "At inference, balanced compute allocation is enforced by" sampling evenly across the prefixes.[^c7]

The evidence is on two tasks. On Countdown, a search problem with depth-first and breadth-first modes, standard training on mixed data "tends to bias toward one" algorithm for many individual problems, and under balanced ModC "the fraction of BFS per problem is concentrated around 0.5."[^c8] On an adversarial test set, filtered so that "filter for problems where either oracle BFS or oracle DFS (but not both) achieves less than 5% success", the paper reports the gap "boosts up to" 20% at Pass@1024.[^c9] On real distillation data, from two teachers, the paper reports that ModC with Qwen2.5-7B "achieves the same Pass@1024 as standard" training with a quarter of the samples, about a 4x efficiency gain.[^c10] A control matters for reading this: with 50-50 data for the two modes and no allocation, the paper saw no gain on Countdown.[^c11]

## Limits

- Every experiment uses two modes. The conclusion lists "extending ModC to a larger number of modes" as future work.[^c12] The bound is also stated for two modes only.
- The derivation needs the per-input success probabilities of the modes, and the main text assumes the modes are known: "we assume that the relevant modes are known a priori."[^c13] It shows that balanced allocation beats a mixture at weight one half. It does not show that balanced allocation is optimal; the conclusion names "adaptive allocation policies" as open work.[^c14]
- The largest gains come from an adversarial set built so that each problem is solvable by only one of the two modes. The natural-set gain is smaller: "the scaling behavior dramatically improves by up to 8% for Pass@1024."[^c15] My reading: the headline numbers measure a regime chosen to reward coverage.
- Specialists and prefixes do not rank the same everywhere. On Countdown, "ModC with separate models outperforms ModC with prefixes", and the paper reads this as knowledge transfer across modes being "less crucial" there. On real data the prefix version is the scalable one, and that trade-off is not settled by the sections read.
- A random partition of the training data also sometimes helps, "but does not outperform" the mode partition.[^c16] So part of the effect may be the extra structure in the data rather than the modes as such; the paper's control suggests the mode split does more, but on two tasks only.
- The 4x figure is for one model size on one dataset in the sections read; the wider range of models in the abstract is not checked here.
- Whether a "mode" is a strategy or merely a label is an assumption. On the distillation data the modes are teacher identities. My inference: the derivation applies to any two groups whose success probabilities differ on an input, so it does not by itself say the groups are reasoning strategies.

## Related

- [[test-time-scaling]] — the general lever of spending more samples at inference; this note fixes how a sample budget is divided among modes.
- [[per-problem-reasoning-pattern-selection]] — also finds that the best reasoning pattern varies per problem, but picks one pattern per problem with a verifier; here the budget is split across modes without choosing per input.
- [[set-level-diversity-floor]] — the same worry that a generated set collapses onto few members, enforced at selection inside a search rather than in training.
- [[curriculum-collapse]] — the question-side form of mode collapse, handled there with a coverage reward.

[^c1]: arxiv-2512-01127 — "where models concentrate on a few modes and"
[^c2]: arxiv-2512-01127 — "are well-documented to induce diversity collapse, where generations concentrate on only a"
[^c3]: arxiv-2512-01127 — "Even when an LLM is balanced across two modes with complementary strengths"
[^c4]: arxiv-2512-01127 — "allocating compute evenly across modes is strictly better than sampling from the model"
[^c5]: arxiv-2512-01127 — "The advantage becomes especially pronounced on inputs where the"
[^c6]: arxiv-2512-01127 — "This design ensures strong specialization and reduces"
[^c7]: arxiv-2512-01127 — "At inference, balanced compute allocation is enforced by"
[^c8]: arxiv-2512-01127 — "the fraction of BFS per problem is concentrated around 0.5"
[^c9]: arxiv-2512-01127 — "filter for problems where either oracle BFS or oracle DFS (but not both) achieves less than 5% success"
[^c10]: arxiv-2512-01127 — "the model achieves the same Pass@1024 as standard"
[^c11]: arxiv-2512-01127 — "not see any gains compared to standard training"
[^c12]: arxiv-2512-01127 — "extending ModC to a larger number of modes"
[^c13]: arxiv-2512-01127 — "we assume that the relevant modes are known a priori"
[^c14]: arxiv-2512-01127 — "integrating ModC with adaptive allocation policies"
[^c15]: arxiv-2512-01127 — "the scaling behavior dramatically improves by up to 8% for Pass@1024"
[^c16]: arxiv-2512-01127 — "ModC with random paritioning sometimes shows gains but does not outperform"
