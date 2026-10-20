---
description: "An RL signal scoring each segment of a tool-use trajectory by how much it moved a learned success probability, so a model learns from one outcome reward when to invoke a tool."
aliases: ["CARL", "Competence-Aware Reinforcement Learning", "segment-level credit assignment"]
sources: ["kumar-2026", "arxiv-2512-19920"]
---
# Competence-aware credit assignment (CARL)

> Splits one binary outcome reward into a signed advantage per segment of a tool-use trajectory — invoke, assimilate, commit — so a model learns where its own answer already suffices and where a tool call is worth the cost, instead of being told when to reach for one.

## Definition / Mechanism

CARL (Competence-Aware Reinforcement Learning) trains a value critic $V_\phi(s)\in[0,1]$ at every structurally observable boundary of a tool-use rollout (a code-fence close, a `<context>` block close), estimating the probability that the trajectory from that point still reaches a correct answer. Treating each segment as an option in a Semi-Markov Decision Process, the terminal-reward-only, undiscounted Bellman equation reduces the per-segment advantage to $A(\text{seg}_k)=V_\phi(s_{k+1})-V_\phi(s_k)$ for intermediate segments and $A(\text{seg}_N)=R-V_\phi(s_N)$ for the final one; for one tool call this yields three signed advantages — query quality, extraction quality, answer commitment — from a single $R\in\{0,1\}$, and the per-segment advantages telescope back to the trajectory-level advantage $R-V_\phi(s_0)$, so no total credit is added or removed, only redistributed.[^c1]

The critic is warm-started (unsupervised, from the base model's own multi-rollout consistency across forced-tool and no-tool prompts) before PPO; without warm-up, early random critic gradients corrupt the shared [[backbone-of-a-formula|backbone]] and training trails the full method by about 9 EM on HotpotQA at 7B.[^c2]

The trained $V_\phi(s_0)$ separates questions the model can already answer from ones that need a tool with AUC 0.93 at 7B and 0.85 at 3B, and on tool-answerable ("Tier 2") questions the trained policy invokes tools 53% less often than the strongest trajectory-level RL baseline (Search-R1 PPO) while remaining about 10 EM points more accurate on those same questions — the value function that carries the credit signal is, incidentally, a calibrated estimate of the model's own competence boundary.[^c3]

Across five tool-use benchmarks (arithmetic, multi-hop QA, financial-table reasoning), moving from trajectory-level credit to token-level credit adds +4.0 average EM at 7B; moving from token-level to segment-level (CARL) adds a further +6.7, and the gain is largest on the most compositional multi-hop benchmark (+8.3 EM on Musique) and at smaller model scale (1.4x the 7B gain at 3B).[^c4]

## Why it matters

This is a training signal for the answerer's side of asking: instead of a prompt-based rule for when to call a tool (which cannot be learned or generalized), the model's own uncertainty about the current context — measured as a value function trained on outcome reward alone — becomes the trigger. It is a concrete instance of "recognize the edge of your own knowledge and ask only then," trained rather than specified.

## Transfer

| | Reinforcement learning (home field) | Here (tool-use asking) |
|---|---|---|
| Formalism | Options framework / Semi-Markov Decision Process, temporally-extended actions with a Bellman equation over options | Each invoke/assimilate/commit stretch of a rollout is treated as one option, terminating at a structural token boundary |
| What survives | The SMDP Bellman decomposition of a trajectory-level return into per-option advantages that telescope back to the whole | Directly: the per-segment advantage formula is applied unchanged to LLM tool-use rollouts |
| What does not | Options are typically hand-designed or discovered policies with their own learned termination conditions | The "option" boundary here is fixed by a structural token (a closing code fence), not learned — it works because tool-use rollouts expose observable boundaries pure reasoning trajectories lack |
[^c5.1][^c5.2][^c5]

## Limits

The reported gains are single-model-family (Qwen2.5, 3B/7B) results on five benchmarks against the paper's own baselines; no independent replication is cited. The method's boundary detection relies on tool-use trajectories having structurally observable segment transitions (code fences, context tags) — the paper itself notes this is what pure reasoning trajectories lack, so the mechanism does not transfer as-is to settings without such markers. `[?]` — this note is drawn from a single arXiv preprint (`kumar-2026`) not yet independently verified. A separate preprint (`arxiv-2512-19920`) finds that a PPO critic trained against the final outcome reflects the model's confidence in the final answer given the steps so far, and that at intermediate steps its value "essentially functions as a semantic classifier rather than an uncertainty verifier."[^c6] The per-segment values used here are intermediate values of that kind, so reading them as step-level competence inherits the question that preprint raises; this note does not settle it.[^c7]

## Related

[[value-of-information]] · [[expected-information-gain]] · [[adaptive-submodularity]]

[^c1]: kumar-2026 — "Given only a terminal reward R ∈ {0, 1}, how do we assign credit per segment? From the SMDP Bellman equation (Appendix A), under terminal-only reward and finite horizon (γ = 1), the persegment advantage reduces to"
[^c2]: kumar-2026 — "The cold-start ablation (no warm-up) trails our full method by ∼9 EM on HotpotQA at 7B (Appendix H)."
[^c3]: kumar-2026 — "A calibrated competence boundary. V (s0 ) classifies Tier 1 from Tier 2 questions with AUC 0.93 at 7B and 0.85 at 3B"
[^c4]: kumar-2026 — "Moving from trajectory-level credit (Search-R1 GRPO) to token-level credit (Search-R1 PPO) adds +4.0 average EM. Moving from token-level to segment-level (CARL) adds a further +6.7."
[^c5.1]: kumar-2026 — "CARL instantiates the Options framework (12): each segment is an option, termination fires at a structural delimiter, and the SMDP Bellman equation"
[^c5.2]: kumar-2026 — "tool-use trajectories have something pure reasoning trajectories lack: structurally observable boundaries (§3.1, Figure 1)."
[^c5]: kumar-2026
[^c6]: arxiv-2512-19920 — "essentially functions as a semantic classifier rather than an uncertainty verifier."
[^c7]: arxiv-2512-19920 — "rather than confidence in the correctness of the current step itself."
