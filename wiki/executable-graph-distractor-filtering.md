---
description: "Having a model emit an executable computational graph with explicit distractor nodes gave distractor robustness at 359 tokens, 89% fewer than reasoning models, with a capacity threshold."
aliases: ["DAGGER", "distractor-aware graph generation", "executable computational graph reasoning"]
sources: ["arxiv-2601-06853"]
---
# Executable graph generation as distractor filter

Instead of free-form chain-of-thought, the model writes the problem as a graph of value nodes and dependencies that is then executed, and marks distractor nodes explicitly. Committing to specific nodes and edges means irrelevant quantities must be either wired in or labeled out, rather than being silently absorbed by prose.[^c1]

**Measured effect.** Gemma-3 12B fine-tuned with SFT then GRPO reached 69.4% weighted accuracy at 359 tokens per problem; its drop under distractors was 12.0-14.4 points, against 14.2-17.5 for Qwen 3-8B and up to 40.7 for standard CoT models.[^c2] Qwen 3-8B stayed higher in absolute accuracy (71.4%) but used about 3,128 tokens, so the graph approach used 89% fewer.[^c3]

**Robustness not trained directly.** Training data had on average 0.21 natural distractor nodes against 2.7 in evaluation, which the authors take as evidence that the structure itself provides an inductive bias for filtering.[^c4] Distractor-node annotations in the graph added little on clean data but +2.9 (4B) and +5.0 (12B) points under distractors.[^c5]

**Capacity threshold.** Without training, the graph format gave 33.3% at 4B but 61.7% at 12B, which exceeded all CoT baselines, so the format needs enough model capacity.[^c6]

## Limits

One language (Bangla), one model family for the graph approach (Gemma-3), and the training distribution of distractors was not controlled beyond the count, so "structure causes robustness" is the authors' interpretation, not an isolated effect. Failed graph executions count as errors, so an execution-rate cost is folded into accuracy. Reasoning models were not given the same graph format, so format and training are not fully separated. For asking, the idea that forcing an explicit relevant/irrelevant commitment helps is my inference.

## Related

- [[anchored-distractor-taxonomy-math-problems]] — the distractor classes this evaluation uses.
- [[entity-agnostic-reasoning-skeleton]] — another structured intermediate form for reasoning.
- [[distractor-strength-reward-signal]] — distractors as a training signal rather than a test.

[^c1]: arxiv-2601-06853 — "the computational graph requires the model to commit to specific nodes and dependencies"
[^c2]: arxiv-2601-06853 — "The 12B GRPO model drops only"
[^c3]: arxiv-2601-06853 — "uses 89% fewer tokens than"
[^c4]: arxiv-2601-06853 — "suggesting that the graph structure itself provides an inductive bias for distractor"
[^c5]: arxiv-2601-06853 — "Annotations provide minimal impact on clean data but yield +2.9 (4B) and +5.0"
[^c6]: arxiv-2601-06853 — "Without any training, †DAGGER achieves 33.3%"
