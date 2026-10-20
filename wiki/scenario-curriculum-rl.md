---
description: "A five-phase reinforcement-learning curriculum, gated on measured mastery, that introduces retry-only episodes, then switch-required, then abstain-required."
aliases: ["scenario-structured curriculum", "curriculum-controlled reinforcement learning"]
sources: ["chen-2026-retry"]
---
# Scenario-structured curriculum RL

> An RL training schedule that introduces harder [[recovery-postulate|recovery]] scenarios only once the policy has mastered the easier ones, so a tool-use agent learns retry, then switch, then abstain, in that order.

## Definition / Mechanism

Phase 1 trains retry-only episodes (100% S1, at most 2 injections); Phases 2–3 introduce switch-required episodes (20%→40% S2); Phase 4 adds abstain-required episodes (10% S3); Phase 5 trains the full mix (30/45/25 S1/S2/S3). Advancement between phases is gated on measured mastery rather than a fixed schedule — e.g. Phase 4 requires S3 transfer above 50%, average turns under 15, and no regression on S1/S2.[^c1]

The policy is optimized with DAPO under a KL constraint against the reference policy; without the KL term, training collapses within 25–30 iterations as the repetition rate exceeds 80%.[^c2]

Reward is partial-credit, not binary: on an incomplete episode it is 0.3 times the fraction of required actions matched, times a repetition penalty; without this dense term, 38% of training tasks would have zero reward variance. Critically, the reward has no positive term for correct [[abstention]] — S3 episodes cannot pass the underlying task evaluator — so any tendency to escalate after paths are exhausted comes from the recovery constraints in context and from exposure to S3 during training, not from a reward signal for abstaining correctly.[^c3]

## Why it matters

Over the curriculum, the rollout abstain rate rises from 23.7% (before S3 is introduced) to 33.3% (once it is), with average turns stabilizing at 10.7 — the authors read this only as a training diagnostic, not as confirmation that abstention was learned as a reward-driven skill.[^c4]

## Limits

The reward function has no term for correct abstention, so the rising abstain rate cannot be read as evidence that abstention was independently reward-learned rather than induced by exposure and context; the mastery-gate thresholds and phase mixes are tuned for one training run (Qwen3-4B on Combined Retail) and are not shown to transfer to a different task domain or model scale.[^c5]

## Related

[[bayesian-tool-memory]] · [[bench2robust]] · [[tool-use-robustness-gap]]

[^c1]: chen-2026-retry — "Phase 1 trains R ETRY (100% S1, max 2 injections); Phases 2–3 introduce S WITCH (20%→40% S2); Phase 4 adds A BSTAIN (10% S3); Phase 5 trains the full repertoire (30/45/25). Auto-advancement requires mastery (e.g., Phase 4 demands S3 transfer > 50%, avg turns < 15, and no S1/S2 regression)."
[^c2]: chen-2026-retry — "We use DAPO [Yu et al., 2025] with a KL constraint (coefficient 0.02) to prevent policy collapse—without KL, training collapses within 25–30 iterations as repetition rate exceeds 80%."
[^c3]: chen-2026-retry — "The partial-credit term provides dense signal: without it, 38% of training tasks have zero reward variance. Importantly, the reward contains no positive term for correct abstention: S3 episodes cannot pass the benchmark task evaluator."
[^c4]: chen-2026-retry — "In the 4B training run, the curriculum-phase abstain rate increases from 23.7% (early phases, before S3 exposure) to 33.3% (late phases with S3 present), with average turns stabilizing at 10.7."
[^c5]: chen-2026-retry — "Accordingly, we treat S3 as a controlled training condition rather than evidence that abstention is independently reward-learned (Appendix L)."
