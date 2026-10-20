---
description: "Abstaining mid-generation the instant a per-token value estimate drops below the fallback reward provably dominates no-abstention and every fixed-position baseline."
aliases: ["dynamic abstention", "value-thresholding", "dynamic mid-generation abstention"]
sources: ["arxiv-2604-18419"]
---
# Dynamic value-thresholding

> Abstain the moment continuing is worth less than quitting — not before, at
> the input, and not at some fixed later checkpoint.

## Definition / Mechanism

Cast [[abstention]] as an explicit action $\perp$ inside a KL-regularized RL
formulation of LLM generation: the vocabulary is augmented with $\perp$,
carrying a fixed fallback reward $r_\perp$ (the utility of deferring to a
human or a stronger model), while a finished answer scores $1$ if correct
and $0$ otherwise. For binary reward and zero KL weight, the state's value
function reduces to the model's own probability of eventually answering
correctly. The optimal policy over this augmented action space abstains
exactly when the expected value of continuing drops below $r_\perp$ — the
rule the paper calls **dynamic value-thresholding**: a two-layer MLP probe
on the model's hidden state is trained by binary cross-entropy to estimate
$V_t$ at *every* token position, and generation halts the instant the
estimate crosses $r_\perp$.[^c1]

## Why it matters

Because the abstention-augmented policy $a(\pi)$ only ever replaces a
low-value continuation with $r_\perp$, its value dominates both the base
policy and $r_\perp$ at every state, so it never scores worse than either
extreme — no-abstention or immediate abstention — and strictly better than
either whenever some reachable state's value falls below $r_\perp$.[^c2]

Because the rule keeps the option to wait, it dominates the family of
fixed-position rules (input-only screening, or a single checkpoint at a
fixed step $k$) that must commit to $\perp$ or not at one predetermined
position — the dynamic rule can defer past a temporary dip and still catch
an unrecoverable one.[^c3]

When the base policy is itself optimal and there
is no KL anchor, dynamic value-thresholding is the optimal policy among
*all* abstention-augmented policies, not merely better than the baselines
tested.[^c4]

The size of the gain is bounded: under an $L$-Lipschitz value
function the improvement over no-abstention grows at most linearly in the
abstention rate, scaled by $L$ (or by $r_\perp$ for immediate abstention).[^c5]

Measured on chain-of-thought math benchmarks, the predicted ordering
holds and widens on harder problems and higher abstention rates.[^c6]

## Limits

The dominance and optimality proofs assume an *oracle* value function;
Section 5's probe is only an estimator, and the guarantees do not transfer
automatically to its error. Optimality (not just dominance) additionally
requires $\beta=0$ (no KL anchor) and an already-optimal base policy — a
condition the paper notes real LLMs are trained to violate, since $\beta>0$
is used in practice to prevent mode collapse. The setting further assumes a
sparse, binary (or bounded) terminal reward with a deterministically
verifiable correctness signal, restricting direct applicability to
reasoning domains like math, code and symbolic logic rather than open-ended
generation.

## Related

- [[abstention]]
- [[gate-saturation-collapse]]
- [[two-stage-abstention-paradigm]]
- [[conformal-abstention-floor]]
- [[chain-entropy-abstention-gate]]

[^c1]: arxiv-2604-18419 — "We abstain when the value function falls below r⊥ ."
[^c2]: arxiv-2604-18419
[^c3]: arxiv-2604-18419 — "Given any base LLM, dynamic value-thresholding dominates input processing based on value-thresholding. Further, it dominates fixed-position abstention at position k > 1 when low-value states cannot recover before k."
[^c4]: arxiv-2604-18419 — "Given a base LLM that dominates all non-abstaining LLMs, and assuming zero KL regularization, dynamic value-thresholding dominates all abstention-enabled policies."
[^c5]: arxiv-2604-18419 — "Given any base LLM, and assuming zero KL regularization and Lipschitz continuity, dynamic abstention improves over no abstention at a rate that is upper-bounded linearly in the abstention rate."
[^c6]: arxiv-2604-18419 — "on Phi-3 at α = 0.9, dynamic abstention achieves 0.64 selective accuracy, compared to 0.34 for the best input-processing baseline and 0.33 for the best fixed-position baseline — roughly double the performance of either family."
