---
description: "Structured runtime context — Beta-posterior recoverability estimates, fallback maps, and heuristic constraints — that raises a tool-use agent's failure recovery without retraining."
aliases: ["Bayesian Tool Memory", "BTM"]
sources: ["chen-2026-retry"]
---
# Bayesian Tool Memory

> When a tool call fails, an agent must choose to retry the same path, switch to an alternative, or abstain — Bayesian Tool Memory (BTM) hands that choice its [[recovery-postulate|recovery]] context, as prompt text, without retraining the policy.

## Definition / Mechanism

BTM is structured runtime context supplied to a tool-use agent after a tool failure. It combines three parts: Beta-posterior recoverability statistics per (tool, error) pair and per (source, target) switch transition, estimated from training-split rollouts; domain-specific fallback maps naming which tool can substitute for which; and heuristic constraints — retry before abandoning a path, verify before an irreversible action, escalate only after available paths are exhausted.[^c1]

On held-out Retail tasks (402 tasks unseen during BTM's own statistics or any RL training), giving BTM to an untrained 4B base model raises its pass rate under injected tool failures by +16.8pp when no alternative tool exists and +11.7pp when one does — a gain from context alone, with no retraining.[^c2]

## Known as

| Field | Name there | Relation |
|---|---|---|
| tool-use agents (this paper) | BTM | exact — the paper's own abbreviation for the same object |

## Why it matters

Combined with a curriculum-trained RL policy, BTM reaches 40.8–45.5% task completion under injection while preserving clean-episode performance, and the RL policy keeps most of its recovery gain even when BTM is withheld at inference — the two are reported as complementary, not substitutes.[^c3]

## Transfer

| | |
|---|---|
| home field | Bayesian statistics — Beta-Binomial conjugate estimation of a success probability |
| here | a per-(tool, error) and per-(source, target) recoverability probability, computed from rollouts and handed to the agent as text |
| what survives | the posterior mean as a compact, updatable summary statistic |
| what does not | the [[calibration]] itself: swapping true posterior values for shuffled ones changes performance by only seed-level variation, so estimation correctness is not what drives BTM's gain — the fallback maps and constraints are |

[^c4]

## Limits

Switch beliefs specifically rest on only 6–20 observed transitions per (source, target) pair, with acknowledged selection bias, and the ablation isolating structure from calibration is reported for the Retail domain alone — whether the fallback-map/constraint component would still dominate in a domain where these are sparser or simply wrong is untested.[^c5]

## Related

[[bench2robust]] · [[tool-use-robustness-gap]] · [[scenario-curriculum-rl]] · [[bounded-rationality]]

[^c1]: chen-2026-retry — "BTM combines (1) Beta-posterior recoverability statistics estimated from training-split rollouts, (2) domain-specific fallback maps with granularity annotations, and (3) heuristic constraints such as retrying before abandoning a path, verifying information before irreversible actions, and escalating only after available recovery paths have been considered."
[^c2]: chen-2026-retry — "BTM improves the 4B base model by +16.8pp without alternatives and +11.7pp with alternatives on held-out Retail tasks; most of the gain comes from fallback maps and recovery constraints."
[^c3]: chen-2026-retry — "Combining the two reaches 40.8–45.5% under injection while preserving failure-free performance."
[^c4]: chen-2026-retry
[^c5]: chen-2026-retry — "Switch beliefs P̂ (switch | j → k) are defined analogously for (source, target) pairs; these are observed recovery rates after j → k transitions (not causal switch-success probabilities) and carry higher uncertainty (n = 6–20) due to sparser data and selection bias."
