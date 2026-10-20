---
description: "A budgeted trigger that grows a belief's dimensions once the entropy gap to target cannot close within remaining questions at the best available information rate."
aliases: ["EXPAND criterion", "entropy gap criterion", "dynamic state expansion"]
sources: ["echarghaoui-2026"]
---
# Entropy-gap expansion

> When the best question left in the bank cannot close the distance to a
> target confidence within the rounds still available, stop asking within
> the current model of $W$ and grow the model instead: propose a new
> dimension, give it a prior, and fold it into the product-space belief.

## Definition / Mechanism

In [[balar|BALAR]], the trigger fires per round: "When the existing
question bank is exhausted or the best available MI is insufficient to
close the [[entropy]] gap within the remaining budget, BALAR triggers an
EXPAND step."[^c1]

The condition compares the current entropy gap to a target against the
best remaining one-step information rate times the rounds left; the paper
reads the resulting inequality as: "the current [[possible-worlds|state space]] $\Theta$ is
insufficiently resolved relative to the remaining interaction horizon, and
expanding $\Theta$ with new candidate dimensions is warranted" — i.e. even
optimal greedy asking on the existing dimensions cannot reach the target
entropy before the budget runs out.[^c2]

Once triggered, the procedure generates a new dimension by an LLM call
conditioned on the conversation so far, elicits its prior, folds it into
the belief under an independence assumption, and rebuilds likelihood
tables: "Recomputes likelihood tables for all existing questions over the
new dimension" before generating new questions that target the added
dimension and the existing ones with highest marginal entropy.[^c3]

The paper frames the trade-off it produces as its own analogy, not a
proof: "The Expand mechanism allows BALAR to refine its state
representation, analogous to gradient descent on the manifold of possible
intents."[^c4]

## Why it matters

This is a budget-aware, algorithmic answer to "should the axis set of $W$
grow now" — as opposed to [[reverse-bayesianism]]'s axiomatic bookkeeping
rule for *how* to redistribute belief once it does. Reverse Bayesianism
says nothing about *when* to expand; this criterion is a threshold rule for
exactly that decision, keyed to a fixed question horizon.

## Transfer

| | |
|---|---|
| **Home field** | Information theory / sequential experiment design: a target entropy and a per-round information-rate bound give a minimum round count to reach it. |
| **Here** | The axis set of the questioner's own world model $\Theta$, not just its distribution — the "rounds needed" bound is used to decide whether to hold the model fixed or grow it. |
| **What survives** | The round-count reasoning: dividing the entropy gap by the best available one-step information rate lower-bounds how many further questions are needed under the current model. |
| **What does not** | Any guarantee that expansion *closes* the gap — the new dimension is LLM-proposed, not derived from the entropy math, so nothing bounds how much information the new dimension actually carries; expanding can also raise entropy before any question reduces it again. |

## Limits

- The trigger threshold $\lambda$ is a free hyperparameter (paper reports a
  default of 1) with no procedure given for setting it from the task; a
  smaller $\lambda$ delays expansion, a larger one triggers it earlier, and
  the paper's own ablation (ARBench cell) is the only [[calibration]] evidence.
- The round-bound derivation assumes the *current* dimensions' answers stay
  conditionally independent given $\theta$ even after expansion, the same
  assumption [[balar|BALAR]]'s selection guarantee needs and that expansion
  itself puts under strain by adding a correlated new axis.
- Single arXiv preprint (2026-05), not independently replicated here.

## Related

[[balar]] · [[reverse-bayesianism]] · [[mutual-information]] · [[possible-worlds]]

[^c1]: echarghaoui-2026 — "When the existing question bank is exhausted or the best available MI is insufficient to close the entropy gap within the remaining budget, BALAR triggers an EXPAND step."
[^c2]: echarghaoui-2026 — "the current state space Θ is insufficiently resolved relative to the remaining interaction horizon, and expanding Θ with new candidate dimensions is warranted"
[^c3]: echarghaoui-2026 — "Recomputes likelihood tables for all existing questions over the new dimension"
[^c4]: echarghaoui-2026 — "The Expand mechanism allows BALAR to refine its state representation, analogous to gradient descent on the manifold of possible intents."
