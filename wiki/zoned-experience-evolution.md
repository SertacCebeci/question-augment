---
description: "A gradient-free agent improves by evolving a library of reward-zoned, credit-assigned text experiences instead of its weights, retrieved as tools to guide when and how it asks."
aliases: ["PRIME", "Proactive Reasoning via Iterative Memory Evolution"]
sources: ["arxiv-2604-07645"]
---
# Zoned experience evolution

> Optimize the library, not the weights: a frozen agent's behavior changes because what it retrieves changes, not because a gradient touched it.

## Definition / Mechanism

Wang & Jiang (2026) replace policy-parameter optimization with library optimization: "we optimize the memory library M rather than the policy parameters θ," updating it each round as $M_{i+1}\sim\mu(\cdot|M_i,\{\tau_i\mid X_i,\pi\})$ from newly collected trajectories. Each memory is a structured tuple $m=(m_{core}, m_{stage}, m_{cond}, m_{zone})$ — situation/action/outcome/lesson, an interaction phase (exploration / verification / completion), applicability conditions, and a zone — rather than a raw trajectory or a flat playbook line.[^s1]

Turning a trajectory into a memory starts with **credit assignment**: "identifies which turns contributed most to the final outcome. Given turn-level credits, we select the top-K turns as key turns that capture the most informative moments of the interaction." Two credit strategies are used by environment shape: Reward-to-Go weights early pivotal turns for sequentially dependent tasks, Equalized weights every turn uniformly for tasks with parallel information gathering (e.g. eliciting several independent preferences before acting).

The distilled memory is then filed by trajectory reward into one of three semantic zones: "the Golden Zone contains successful strategies to replicate, the Warning Zone captures failure patterns to avoid (e.g., “jumped to generating full itinerary without clarifying questions” leading to repeated backtracking), and the Preference Zone records user behavior patterns that enable personalization." At inference the retrieved set is presented to the frozen policy zone-labeled — golden as positive guidance, warning as a pitfall list, preference as personalization — rather than as undifferentiated context.

The library itself evolves by four meta-level operators applied probabilistically across rounds, not by simply appending: "Mutation: Refines experience clarity based on empirical feedback. Generalization: Abstracts environment-specific details from high-performing experiences. Crossover: Combines complementary insights from multiple experiences. Pruning: Removes stale or underperforming experiences from the library." Generalization is reported concretely turning "In IntentionGym travel tasks, ask about trip [details]" into a cross-environment rule; pruning uses usage and success thresholds to retire memories.

Across eight multi-turn user-centric benchmarks (frozen Qwen3 backbones, no weight updates), the retrieved library changes task completion materially: "Qwen3-8B + PRIME achieves 193% improvement on FunctionGym and 50% on TauGym over the raw base model." Against GRPO-trained agents on the same benchmarks, the method is competitive rather than dominant, at a fraction of the cost: "PRIME requires 5–6 times fewer GPU-hours per environment compared to GRPO." A library built from one model's rollouts also transfers, with reduced gain, to a smaller frozen model at inference time with no retraining of either model.

## Why it matters

This targets stall 2 (a policy that should ask but was never told to, and cannot be retrained) with a mechanism distinct from a flat lesson log: whether an agent asks a clarifying question, and which one, is steered by which zone dominates retrieval for the current stage — golden strategies that include "ask before acting" compete against warning entries that punished exactly that omission, and the zone assignment is derived from the trajectory's own reward, not hand-labeled.

## Limits

Reward-to-go vs. equalized credit assignment is chosen by environment, not learned or justified beyond "best for" claims from the paper's own environment set. GRPO still produces larger absolute gains than PRIME on the same tasks — this is a cost/interpretability trade, not a strict improvement. The user simulator (Qwen3-32B) stands in for a real user across every benchmark, so what "the user's" response teaches the credit-assignment and distillation steps is itself a simulated signal. `[?]` — single preprint, work in progress, not independently replicated.

## Related

[[convolve-context-evolution]] · [[experience-repository]] · [[competence-aware-credit-assignment]] · [[clarification-request]]

[^s1]: arxiv-2604-07645
