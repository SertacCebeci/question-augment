---
description: "A trajectory-level reward that scores task completion minus a per-turn penalty, optimized by simulated self-play against a hidden-goal user to train when an agent clarifies versus executes."
aliases: ["Multi-turn Reward", "MR", "CLARE", "self-evolution via collaborative simulation", "clarification-aware self-evolving agent"]
sources: ["zhu-2026-clarify"]
---
# Multi-turn Reward clarification training

> The decision to ask or act is folded into one number — task value minus a
> turn penalty — and a policy is trained on it by simulated interaction
> rather than by hand-written rules.

## Definition / Mechanism

Zhu, Li and Huo train CLARE, a multi-agent 3D tool-use system, to decide at
each turn between clarifying and executing by optimizing a **Multi-turn
Reward**:

$$MR(\tau) = V(\mathrm{Exec}(\mathcal{T}_{3D},\theta_{exec}), G^*) - \lambda \cdot K$$

where $V \in [0,1]$ is an automated verifier's task-completion score against
the user's hidden goal $G^*$, $K$ is the number of interaction turns, and
$\lambda$ (set to 0.1) penalizes verbosity. "We evaluate the quality of each
sampled trajectory 𝜏 using a composite Multi-turn Reward (MR), balancing
task fidelity against interaction efficiency."[^c1]

Training is self-play: for a context, the agent samples $N$ candidate
responses from its current policy and rolls each out to completion against
a **Simulated User** that holds the true goal but reveals it only when
explicitly asked. "U [the Simulated User] is not a static responder but a
stateful agent designed to mimic realistic human behavior... U operates
under an Information Asymmetry setting."[^c2]

Because only the terminal turn produces an executable output, the
trajectory's $MR$ is credited back to every earlier turn: "the final
trajectory reward $MR(\tau)$ is retroactively mapped to all step-level
instruction-output pairs within that specific trajectory... early,
proactive questions are correctly credited for enabling successful
downstream execution."[^c3]

Trajectories ranked by $MR$ are then used for Supervised Fine-Tuning (clone
the top trajectories) or Direct Preference Optimization (chosen/rejected
pairs by $MR$).

## Known as

| Field | Name there | Match |
|---|---|---|
| The paper's framework name | CLARE | exact — names the whole system this reward trains |
| The paper's objective name | Multi-turn Reward / MR | exact — the reward function itself |
| The paper's training-paradigm name | self-evolution via collaborative simulation | exact — names the self-play loop that optimizes MR |

## Why it matters

This is a trainable stand-in for the ask/act trade-off that
[[value-of-information]] states in closed form: "the decision of when to
clarify versus when to execute is itself learnable—excessive clarification
increases interaction cost, while premature execution risks failure."[^c4]
Trained on simulated rollouts, it raised single-step task success from a
24.40% best-baseline average to 60.40% (DPO variant) on the paper's own
3D-Clarify benchmark, and from single-digit success to 34–49% on multi-step
tasks where baselines collapse to 0%.[^c5]

## Transfer

| | |
|---|---|
| **In its home field** | Preference optimization / RL-style reward shaping for general LLM-agent training, where a terminal outcome reward is common but credit assignment across turns is the hard part. |
| **Here** | Applied to the single decision of asking a clarifying question versus executing, in one domain (3D tool orchestration) with an automated, checkable verifier. |
| **What survives** | The shape of the objective — completion value minus a turn penalty — as a trainable substitute for value-of-information when no closed-form utility is available, and the mechanism of crediting an early question with the terminal outcome it enabled. |
| **What does not** | Any optimality guarantee: MR is a hand-set trade-off ($\lambda = 0.1$) with no proof the learned policy approaches the VoI-optimal one; the verifier $V$ and simulated user's information-asymmetry schedule are specific to this benchmark and untested elsewhere. |

## Limits

This wiki's claim about *transfer* rests on one paper, one domain (3D
generation/reconstruction tool calls), one [[backbone-of-a-formula|backbone]] (Qwen3-8B, LoRA-tuned),
and a simulated user whose disclosure schedule is scripted rather than
drawn from real dialogues; $\lambda$ and the turn cap ($T_{max}=8$) are
fixed by the authors, not derived. `zhu-2026-clarify` is an unreviewed
arXiv preprint (2026); the reported percentages are this paper's own
benchmark, 3D-Clarify, which the same authors built and control.

## Related

[[value-of-information]] · [[preference-optimization-for-questions]] · [[expected-information-gain]] · [[clarification-benchmarks]]

[^c1]: zhu-2026-clarify — "We evaluate the quality of each sampled trajectory 𝜏 using a composite Multi-turn Reward (MR), balancing task fidelity against interaction efficiency."
[^c2]: zhu-2026-clarify
[^c3]: zhu-2026-clarify
[^c4]: zhu-2026-clarify — "the decision of when to clarify versus when to execute is itself learnable—excessive clarification increases interaction cost, while premature execution risks failure."
[^c5]: zhu-2026-clarify — "Averaged across all single-step underspecifications, Clare-SE-DPO achieves 60.40% SR (CR: 73.51%), more than doubling the strongest baseline (CEP: 24.40% SR) and demonstrating that clarification policies are learnable through simulated interaction."
