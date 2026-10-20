---
description: "A training-free evolutionary method that rewrites an LLM agent's channel-selection prompt from rollout results, gated to guarantee monotonic improvement without touching model weights."
aliases: ["Communication Policy Evolution", "CPE"]
sources: ["ma-2026-communication"]
---
# Communication Policy Evolution (CPE)

> A prompt-only evolutionary loop that improves *when an agent should ask by text vs. by structured UI*, accepting a candidate policy only after it beats both the training batch and a held-out validation set.

## Definition / Mechanism

CPE optimizes the communication policy $\pi_{comm} = (\text{system\_prompt}, \text{examples}, \text{appendixes})$ by iterative refinement against rollout results, without modifying model weights. Each round: (1) evaluate $\pi$ on a training batch $B_r$; (2) an LLM optimizer analyzes hybrid-only signals (scores, trajectories, task specs, current policy, patch history) and proposes a JSON patch $\Delta\pi$; (3) the patch is applied as a text override to produce a candidate $\pi'$; (4) a two-stage gate — $\pi'$ must beat $\pi$ on $B_r$ (train accept), then beat the current best $\pi^*$ on a held-out set $D_{val}$ (val accept) — decides whether $\pi^*$ updates. "Val-accepted candidates update π∗, guaranteeing monotonic improvement."[^c1]

CPE is applied selectively, only where the naive hybrid policy already underperforms a single-channel baseline: "We apply CPE only to settings where naive hybrid interaction underperforms at least one single-channel baseline, indicating ineffective channel selection." In those settings the optimized policy achieves the best task completion of any tested configuration: "The optimized policies achieve best task completion across all evaluated configurations, using only prompt-level refinement without modifying model weights."[^c2]

## Why it matters

It gives the channel-selection meta-decision ([[communication-policy]]) a concrete, cheap optimization procedure: no fine-tuning, only a train/val-gated prompt edit loop, applicable whenever a hand-written or naive hybrid policy is measurably worse than committing to one channel.

## Transfer

| | Home field (ML optimization) | Here |
|---|---|---|
| Formalism | mutate-and-select search with a held-out validation gate (evolutionary strategies / early-stopping practice) | an LLM proposes textual patches to a prompt; a two-stage accept gate replaces gradient update |
| Survives | the train/val split guaranteeing the *accepted* trajectory of candidates is monotonically non-decreasing on measured data | yes — the same two-gate structure is used verbatim |
| Does not survive | a formal convergence guarantee over the true objective (population-level optimality, regret bounds) | CPE guarantees monotonicity only on the specific batches it was gated against, not on unseen distributions; the "guarantee" is empirical-batch, not statistical |

## Limits

The monotonic-improvement claim is scoped to the batches $B_r$ and $D_{val}$ actually used; it is not a generalization guarantee. CPE was tested only where hybrid access was already shown to underperform a single channel, so its behavior when hybrid is already best is unreported. [?] — verifier to confirm ma-2026-communication.

## Related

[[communication-policy]] · [[value-of-information]] · [[optimal-decision-tree]]

[^c1]: ma-2026-communication
[^c2]: ma-2026-communication — "We apply CPE only to settings where naive hybrid interaction underperforms at least one single-channel baseline, indicating ineffective channel selection."
