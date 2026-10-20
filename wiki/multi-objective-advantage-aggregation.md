---
description: "A multi-objective RL scheme that discretizes and normalizes each pedagogical objective's reward before averaging advantages, so no objective dominates the update."
aliases: ["pedagogically aligned multi-objective RL", "reward discretization and advantage aggregation", "PEARL tutor optimization"]
sources: ["chang-2026"]
---
# Multi-objective advantage aggregation

> When a policy must satisfy several competing objectives at once, average
> the *normalized per-objective advantage*, not the raw reward — otherwise
> the objective with the widest or densest reward signal decides every
> update on its own.

## Definition / Mechanism

Chang et al. (2026) train PEARL, a [[staged-socratic-hint-policy|Socratic]] tutoring agent, with an RL scheme built for
multi-turn dialogue that must jointly satisfy eight pedagogical dimensions —
accuracy, leakage control, completeness, cognitive-load management,
Socratic guidance, metacognitive facilitation, adaptive teaching and
emotional support. Directly averaging these dimension-level terminal
rewards "can destabilize training and cause high-variance objectives to
dominate optimization."[^c1]

Their fix has three steps applied per rollout group. Each dimension's
aggregated reward is first discretized to the nearest of five bins {0.1,
0.3, 0.5, 0.7, 0.9}, preserving coarse ordering while damping noise. Within
each dimension a group-relative advantage is then computed by subtracting
the group mean and dividing by the group standard deviation — the same
normalization GRPO/GSPO use for a single reward, applied separately per
dimension. The final trajectory advantage averages (or weights) the
per-dimension advantages: "this design aggregates and discretizes rewards
within each dimension, then normalizes and aggregates advantages across
dimensions. It places pedagogical objectives on comparable scales, limiting
domination by high-variance dimensions and stabilizing sparse or
low-variance rewards."[^c2]

A turn-count penalty subtracts a decayed fraction of the bin margin from
trajectories longer than the group's shortest completed one, discouraging
unnecessarily long dialogues without discarding the discretized ordering,
and the policy is optimized with GSPO's sequence-level clipped objective,
chosen because it "operates at the sequence level rather than the token
level, thereby alleviating the instability of GRPO in MoE training."[^c3]

## Why it matters

In PEARL's own ablation (Qwen3-30B-A3B [[backbone-of-a-formula|backbone]]), adding advantage
aggregation and reward discretization on top of episodic RL alone raised
the average pedagogical score from 88.6 to 91.0 to 92.1, and the
turn-count penalty then cut dialogue length from 15.0 to 6.9 turns while
raising the average further to 92.9.[^c4]

This is a concrete demonstration that *how* several per-turn objectives are
combined into one training signal — not just what the objectives are —
changes what the resulting policy asks and how long it keeps asking before
committing to an answer.

## Transfer

| | |
|---|---|
| Home field | RL policy optimization (GRPO/GSPO-family group-relative advantage, LLM alignment) |
| Here | Multi-turn Socratic tutoring, one policy update per dialogue group under several pedagogical objectives at once |
| What survives | Group-relative normalization to control the scale of a single reward signal; sequence-level clipped-objective policy updates |
| What does not | Any convergence or Pareto-optimality guarantee across multiple non-commensurable objectives; the uniform per-dimension weighting is a stated default, not derived from a utility function over the dimensions |

## Limits

The ablation's tutoring scores are produced by PEARL's own reward model
rather than the independent external evaluator or blind teacher comparisons
used for the paper's headline results, so the component-by-component gains
cited above are self-scored, not externally validated. The method is
demonstrated on one backbone family (Qwen3-30B-A3B) and one domain (math
tutoring dialogue); nothing here shows the discretize-then-normalize
scheme survives objectives that trade off directly against one another
rather than merely differing in variance or density.

## Related

[[investigative-question-grpo-training]] · [[preference-optimization-for-questions]] · [[value-of-information]] · [[mutual-information]]

[^c1]: chang-2026 — "Directly averaging the corresponding dimensionlevel rewards into a single terminal reward can destabilize training and cause high-variance objectives to dominate optimization"
[^c2]: chang-2026 — "This design aggregates and discretizes rewards within each dimension, then normalizes and aggregates advantages across dimensions. It places pedagogical objectives on comparable scales, limiting domination by high-variance dimensions and stabilizing sparse or low-variance rewards."
[^c3]: chang-2026 — "We then optimize the policy πθ using GSPO (Zheng et al. 2025), which operates at the sequence level rather than the token level, thereby alleviating the instability of GRPO in MoE training."
[^c4]: chang-2026 — "Advantage aggregation and reward discretization further improve the score to 91.0 in T5 and 92.1 in T6, supporting more balanced and stable multi-objective optimization. Finally, the turn-count penalty reduces dialogue length from 15.0 rounds in T6 to 6.9 in T7 while increasing the average to 92.9."
