---
description: "Rewarding correct answers and honest model-uncertainty flags alike, penalizing only hallucination, to train attribution over difficulty-rewritten math problems."
aliases: ["RL-UA", "uncertainty-aware RL", "three-tier attribution reward"]
sources: ["arxiv-2604-17293"]
---
# Attribution-aware RL reward

> Reward honest failure the same as success, and only hallucination the
> same as failure — the model learns to tell "I can't" from "you didn't
> say" instead of learning to refuse more.

## Definition / Mechanism

Ren et al. (2026) train [[uncertainty-source-attribution|attribution]]
with GRPO under a three-way sparse reward, one grade below binary
correct/incorrect: "We use GRPO training with a sparse reward: +1 for
correct answers or correct uncertainty classification; 0 for honest
abstention (incorrect answer but flagged as model uncertainty); and -1
for hallucinations. This setup encourages the model to answer when
confident and correctly attribute the source of uncertainty otherwise."
[^c1]

The training questions are synthesized from one math dataset by rewriting
along two axes, so the model sees both failure modes under a controlled,
verifiable ground truth: "The dataset comprises three instance types:
Original Problems to preserve reasoning capability; Extremely Difficult
Variants (rewritten to exceed model capabilities) to simulate model
uncertainty; and Insufficient Variants (rewritten with missing
conditions) to simulate data uncertainty." All rewrites pass an
LLM-based verification and filtering pass before training.

## Why it matters

Despite training on math alone, the gain transfers to knowledge-intensive
tasks the model was never trained on, and it targets exactly the metric
that plain RL does not move: on Qwen3-4B-Instruct-2507, model-uncertainty
recognition on reasoning tasks rises from 23.3% (backbone) and 13.3% (a
standard RL baseline trained only on answerable data) to 53.5% under
RL-UA, while accuracy holds at 72–73% across all three; on Qwen3-8B in
thinking mode, MU-F1 on knowledge-intensive tasks rises from 35.6% to
54.1% and AVG-F1 from 48.2% to 62.7%, again without a drop in ACC. A
standard RL baseline — reward on answerable data only — actually degrades
[[uncertainty-source-attribution|attribution]] (Qwen3-4B's reasoning MU-F1
falls from 23.3% to 13.3%), showing the three-tier reward, not RL itself,
does the work.[^c3]

## Limits

Demonstrated on two backbones (Qwen3-4B-Instruct-2507 and Qwen3-8B
thinking) and one training domain (mathematics); whether the reward
transfers when the *training* data itself spans knowledge-intensive
tasks, or to larger or closed-source models, is **unverified**. The
reward still requires a way to construct paired difficulty/insufficiency
rewrites with verifiable labels — a resource the source built by hand for
math and did not show generalizing automatically to other domains.

## Related

- [[uncertainty-source-attribution]]
- [[abstention]]
- [[chain-entropy-abstention-gate]]

[^c1]: arxiv-2604-17293 — "We use GRPO training with a sparse reward: +1 for correct answers or correct uncertainty classification; 0 for honest abstention (incorrect answer but flagged as model uncertainty); and -1 for hallucinations. This setup encourages the model to answer when confident and correctly attribute the source of uncertainty otherwise."
[^c3]: arxiv-2604-17293 — "On Qwen3-4B-Instruct-2507, RL-UA substantially outperforms both the backbone model and a standard RL baseline, especially on model uncertainty recognition (MU-F1), while maintaining or slightly improving answer accuracy."
