---
description: "Rolling out each training question with and without tools, on-policy, labels whether tools are needed; four outcome classes become targeted signals that cut redundant calls without losing accuracy."
aliases: ["AKBE", "agentic knowledge boundary enhancement", "with-tool and no-tool dual rollouts", "on-policy intrinsic knowledge boundary"]
sources: ["doi-10-48550-arxiv-2605-26952", "arxiv-2512-16883"]
---
# Dual-path knowledge-boundary probing

Agentic reinforcement learning (RL) on search-tool tasks has a drift: the authors report that training "induces increasing redundant tool calls and blurs the model's intrinsic knowledge boundary", so the model stops telling when tools are needed and when parametric knowledge suffices.[^c1] Reward shaping that penalises tool calls is too coarse: it "tend to incentivize indiscriminate tool-call suppression, leading to reward hacking".[^c2] AKBE (Chen et al., 2026) replaces the coarse penalty with a per-question label obtained by probing the current policy.

## Mechanism

For every training question the policy is rolled out twice in parallel: G_wt rollouts with tools and G_nt rollouts with tool access disabled. WT records whether any with-tool rollout is correct; NT whether any no-tool rollout is correct.[^c3] The knowledge boundary of the policy on that question is then defined per instance: KB = 1 if some no-tool rollout is correct (tools unnecessary), else KB = 0.[^c4] No-tool rollouts have no environment latency, so the probe is cheap.[^c5]

The (WT, NT) pair sorts the question into four classes, each with its own target trajectory:

- **Tool-dependent** (WT correct, NT wrong): target is the correct with-tool trajectory with the fewest tool calls, so necessary calls are kept but minimised.[^c6]
- **Efficiency** (both correct): target is a correct no-tool trajectory, teaching the model to skip calls on questions inside its boundary.[^c7]
- **Hallucination** (tools wrong, no-tool correct): target is a correct no-tool trajectory, steering away from tool results that derail correct internal reasoning.[^c8]
- **Both-wrong**: no reliable target exists; only the ordinary RL loss applies.[^c9]

The total loss is L_GRPO + λ·L_AKBE, where L_AKBE is cross-entropy on the selected targets, and L_GRPO can be swapped for other agentic RL losses.[^c10] Because the rollouts come from the current policy, the label is recomputed every step and follows the boundary as it moves.[^c11]

## What was measured

- On seven QA benchmarks with a Wikipedia search tool, AKBE gave +1.85 average accuracy and 18% fewer tool calls than standard agentic RL on Qwen3-4B, about 25% higher tool productivity.[^c12]
- Reward-shaping baselines cut calls but lost accuracy; the confidence-threshold baseline avoided collapse but cut few calls.[^c13]
- An offline variant (signals built from a frozen, fully trained policy) used even fewer calls but scored lower: the late-stage boundary is "overly optimistic for the weaker policy during early training", so it suppresses tools prematurely.[^c14]
- Ablation: removing the Tool-dependent class drops accuracy below GRPO, because the remaining classes only push toward no-tool answers; it acts as the guard against over-suppression. Removing Efficiency raises calls; removing Hallucination costs a little accuracy.[^c15]

A fractional version of the same label appears in AdaSearch (Lin et al., 2026). It samples a set of parametric-only answers, scores them by substring match, and labels a question solvable when the solve rate reaches a threshold: "Then, we define a threshold ρ and label instances" with a solve rate at or above it as solvable.[^c18] The labels come from a single pass "before training", not from rollouts that move with the policy.[^c19][^c20] The authors report that more samples per question give "a more reliable estimate of the solve rate", which improves both the decision score and EM.[^c17] They also note that the labels "inevitably contain sampling-based noise", with no formal analysis of its effect.[^c16] The contrast with the on-policy probe above is therefore the label's timing, not its content (my inference).

## Limits

- "Within the boundary" means at least one sampled no-tool rollout was correct; a lucky guess counts as knowledge. This is my inference from the definition; the paper offers no calibration check.
- Labels need verifiable gold answers and the cost of extra no-tool rollouts per question; only QA with a Wikipedia retriever was tested.
- Both-wrong questions, typically the hardest, receive no boundary signal.
- λ is fixed during training; the authors flag an adaptive λ as future work (read in the limitations section, not quoted).
- Results are mostly on small Qwen models; transfer to other tools (code, web) is untested.

## Related

- [[search-decision-boundary-misalignment]] — the same over-search/under-search failure, diagnosed by counterfactual answer-now probes and fixed with DPO, offline per step rather than by on-policy dual rollouts.
- [[knowledge-boundary-aware-reward]] — also estimates the boundary online from group rollouts, but shapes the reward for abstention rather than adding a supervised target.
- [[knowledge-boundary-aware-self-distillation]] — another use of a knowledge boundary as a training signal.
- [[boundary-sharpness]] — how sharply a model separates what it knows from what it does not, the quantity this training aims to restore.

[^c1]: doi-10-48550-arxiv-2605-26952 — "increasing redundant tool calls and blurs the"
[^c2]: doi-10-48550-arxiv-2605-26952 — "suppression, leading to reward hacking."
[^c3]: doi-10-48550-arxiv-2605-26952 — "and no-tool) in parallel:"
[^c4]: doi-10-48550-arxiv-2605-26952 — "We define the knowledge boundary as the perinstance determination of whether tools are required and the minimum tool calls necessary."
[^c5]: doi-10-48550-arxiv-2605-26952 — "compared to with-tool rollouts, making this probing step computationally efficient."
[^c6]: doi-10-48550-arxiv-2605-26952 — "We select the correct with-tool trajectory with the minimum number"
[^c7]: doi-10-48550-arxiv-2605-26952 — "teaching the model to bypass unnecessary tool invocations for"
[^c8]: doi-10-48550-arxiv-2605-26952 — "indicating that tool calls introduce"
[^c9]: doi-10-48550-arxiv-2605-26952 — "original RL objective for these instances."
[^c10]: doi-10-48550-arxiv-2605-26952 — "where LGRPO can be replaced by any classic agentic"
[^c11]: doi-10-48550-arxiv-2605-26952 — "knowledge boundary is dynamically re-evaluated at"
[^c12]: doi-10-48550-arxiv-2605-26952 — "calls by 18% over standard agentic RL, yielding 25% higher tool productivity"
[^c13]: doi-10-48550-arxiv-2605-26952 — "provides limited TC reduction."
[^c14]: doi-10-48550-arxiv-2605-26952 — "the weaker policy during early training."
[^c15]: doi-10-48550-arxiv-2605-26952 — "Tool-dependent signals serve as a crucial protective"
[^c16]: arxiv-2512-16883 — "rate, they inevitably contain sampling-based noise."
[^c17]: arxiv-2512-16883 — "more reliable estimate of the solve rate and empirically improves both F1dec and EM, as shown"
[^c18]: arxiv-2512-16883 — "Then, we define a threshold ρ and label instances"
[^c19]: arxiv-2512-16883 — "p using substring exact match (SubEM), which"
[^c20]: arxiv-2512-16883 — "Before training, we use the stage 1 policy"
