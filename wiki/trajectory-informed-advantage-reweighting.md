---
description: "A GRPO abstention reward that scales with each group's empirical correctness rate rather than a fixed ternary value, applied as a decoupled post-hoc advantage adjustment."
aliases: ["TIAR", "Trajectory-Informed Advantage Reweighting", "decoupled advantage adjustment"]
sources: ["pan-2026-tiar"]
---
# Trajectory-informed advantage reweighting

> A training signal for "answer or abstain" that reads each query's
> difficulty from the GRPO group's own sampled trajectories, instead of
> assigning [[abstention]] a fixed reward.

## Definition / Mechanism

Pan et al. train GRPO on ternary rewards (correct $R_c=+1$, wrong
$R_w=-1$, abstain $R_a$) and observe that a fixed $R_a=0$ implicitly fixes
an abstention threshold at empirical correctness $\hat p = 0.5$ for every
query, regardless of the query's actual difficulty. They derive the
opportunity cost of abstaining, from the expected value of attempting
$V_{attempt}(\hat p) = \hat p R_c + (1-\hat p) R_w = 2\hat p - 1$, as
$R_a^* = (1-\hat p)|R_w| - \hat p R_c = 1 - 2\hat p$, where $\hat p =
n_c/(n_c+n_w)$ is the group's own empirical correctness rate among its
non-abstaining trajectories, defined "when $n_c+n_w>0$": $R_a^*=1$ when
no attempt in the group succeeds, $R_a^*=-1$ when every attempt succeeds,
and the ternary reward is recovered exactly as the special case
$\hat p=0.5$.[^c1]

Substituting $R_a^*$ directly into GRPO's group-normalized advantage
computation is shown to create a coupling problem: because every
advantage in a group shares the same group mean and standard deviation,
changing $R_a$ shifts the normalization statistics and so distorts the
advantages assigned to the correct and wrong trajectories in the same
group, weakening the learning signal on exactly the hard questions where
a correct answer is rare and valuable. TIAR (Trajectory-Informed
Advantage Reweighting) resolves this by leaving the standard GRPO
normalization untouched for correct/wrong trajectories and instead adding
a separate, decoupled adjustment $\lambda(1-2\hat p)$ to only the
abstaining trajectories' advantages after normalization, with $\lambda$ a
tunable scaling strength (the paper reports $\lambda=1.0$ as best by
ablation, and $\lambda=0.3$ as unstable).[^c2]

## Why it matters

On AbstentionBench (20 datasets, 6 scenarios, evaluated with Llama-3.1-8B
and Qwen3-8B), "TIAR achieves state-of-the-art abstention F1 scores
across five of six evaluation categories, outperforming the static
ternary baseline on 17 of 31 benchmark datasets while fully preserving
baseline accuracy."[^c3]

A coupled (non-decoupled) implementation of the same $R_a^*$ reward
instead degraded accuracy by 0.76 points versus the ternary baseline
despite a smaller abstention-F1 gain, isolating the decoupling itself —
not merely using $\hat p$ as a reward — as what the gain depends on.[^c4]

## Transfer

| | |
|---|---|
| **In its home field** | GRPO (Shao et al. 2024) group-normalizes a scalar reward across sampled completions per prompt to update a policy without a learned critic, developed for domains with one checkable reward per trajectory. |
| **Here** | The three outcomes of an abstention decision (correct, wrong, abstain) share one GRPO group, and the abstain reward is no longer a fixed scalar but a function of the other two outcomes' empirical mix in the same group. |
| **What survives** | The group-relative, critic-free update; GRPO's tolerance for a reward computed after sampling rather than fixed in advance. |
| **What does not** | GRPO's assumption that every trajectory in a group is normalized by one shared statistic without side effects — reusing that statistic for a reward that itself depends on the group's composition is what produces the coupling problem the paper reports. |

## Limits

- The dynamic reward is undefined when a group has no attempted
  (non-abstaining) trajectory; the algorithm applies the adjustment only
  conditionally on that case not arising.
- Reported gains are a single training run per model (fixed seed) on one
  training set (656 CRAG-derived examples) and two 8B base models; the
  paper states this is due to GRPO's computational cost, so no variance
  across seeds is on record.
- The correctness judge is itself an LLM (Llama-3.1-8B-Instruct via
  pattern matching and semantic analysis), validated by the AbstentionBench
  authors against human annotation at 82.3% agreement — the reward signal
  therefore inherits that judge's error rate.

## Related

[[certainty-weighted-grpo-reward]] · [[savor-calibration-abstention-reward]] · [[abstention]] · [[awa-rl]]

[^c1]: pan-2026-tiar — "Ra∗ = (1 − p̂) · |Rw | − p̂ · Rc = 1 − 2p̂."
[^c2]: pan-2026-tiar — "this introduces a coupling problem: because all advantages share the same group mean R̄ and standard deviation σ, modifying Ra changes the normalization statistics, which distorts Âc and Âw ."
[^c3]: pan-2026-tiar — "TIAR achieves state-of-the-art abstention F1 scores across five of six evaluation categories, outperforming the static ternary baseline on 17 of 31 benchmark datasets while fully preserving baseline accuracy."
[^c4]: pan-2026-tiar
