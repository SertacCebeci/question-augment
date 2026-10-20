---
description: "Widens the KL trust region between a policy and its base model with estimated epistemic risk, so the policy deviates from a dangerous prior instead of staying anchored to it."
aliases: ["FTR", "Friction-Conditioned Trust Region", "Friction-Conditioned Trust Regions", "risk-conditioned policy plasticity"]
sources: ["arxiv-2604-25136"]
---
# Risk-conditioned trust region

> Standard trust regions shrink when you're unsure of the world; this one
> shrinks when you trust the model you started from, and opens up the moment
> you don't.

## Definition / Mechanism

Pustejovsky & Krishnaswamy (2026) make the trust-region
radius of KL-regularized policy optimization (TRPO/PPO-style) a function of
estimated epistemic risk instead of a fixed constant:

> "KL(πθ (· | h) ∥ π0 (· | h)) ≤ ϵ(h),
> where ϵ(h) = ϵ0 + κ Risk(h)"[^c1]

$\pi_0$ is the trusted base policy, $\pi_\theta$ the policy being trained,
and $\text{Risk}(h)$ an estimate of the base policy's own epistemic danger
in context $h$ — not environment uncertainty, which is what a classical
trust region shrinks under. The inversion is deliberate:

> "When Risk(h) is high, the base policy is
> precisely the source of potential harm: remaining
> close to π0 would entrench unsafe, misleading, or
> normatively problematic behavior."[^c2]

So when the base model is judged reliable ($\text{Risk}(h)$ low), $\epsilon(h)
\approx \epsilon_0$ and updates stay tightly anchored, preserving
instruction-following and stylistic stability in routine contexts. When the
base model is judged dangerous, $\epsilon(h)$ grows and larger deviations —
clarifying, refusing, redirecting instead of the base model's default move —
become admissible:

> "This differs fundamentally from classical
> robust control, where trust regions shrink under
> uncertainty about dynamics; here, trust regions expand under lack of trust in the prior policy itself."[^c3]

The method is a constraint on the *feasible set* of policy updates, not a
reward term: it can be layered under a reward- or preference-based
objective built on the same risk estimate, because —

> "FTR is orthogonal to
> the other FPO methods. While FAR, FPP, and GRFR shape what
> the policy is optimized to prefer, FTR shapes where
> in policy space the optimizer is allowed to move."[^c4]

## Why it matters

Most mechanisms that change *when* an agent asks operate on the reward or
the output distribution for a single decision. This one operates one level
up, on how much the training update itself is allowed to move the policy
away from a known-good prior, conditioned on a per-context danger estimate.
It gives "ask more here" and "stay exactly as you were here" a shared
control variable — the trust-region radius — instead of two separate
mechanisms that can drift out of sync.

## Limits

$\text{Risk}(h)$ is presumed available from "an auxiliary risk head" with no
architecture, training procedure, or validation given in this extract — the
method's soundness rests entirely on that estimator's own accuracy, which
is unverified here. No experiments, ablations, or comparisons against a
fixed-radius trust region are reported in the sections read; the claim that
FTR dominates or even outperforms standard TRPO/PPO in practice is
unverified.

## Related

- [[friction-functional]] — the natural source of the $\text{Risk}(h)$
  estimate this method's radius scales with.
- [[threshold-optimality-of-clarification]] — the dominance condition this
  method is designed to approximate without evaluating it directly.
- [[frictive-intervention]] — the action classes (clarify, refuse, redirect,
  …) that a widened trust region makes reachable from the base policy.
- [[dynamic-value-thresholding]] — another risk-triggered departure from a
  default policy, gated by a value estimate rather than a KL radius.

[^c1]: arxiv-2604-25136 — "KL(πθ (· | h) ∥ π0 (· | h)) ≤ ϵ(h), where ϵ(h) = ϵ0 + κ Risk(h)"
[^c2]: arxiv-2604-25136 — "When Risk(h) is high, the base policy is precisely the source of potential harm: remaining close to π0 would entrench unsafe, misleading, or normatively problematic behavior."
[^c3]: arxiv-2604-25136 — "This differs fundamentally from classical robust control, where trust regions shrink under uncertainty about dynamics; here, trust regions expand under lack of trust in the prior policy itself."
[^c4]: arxiv-2604-25136 — "FTR is orthogonal to the other FPO methods. While FAR, FPP, and GRFR shape what the policy is optimized to prefer, FTR shapes where in policy space the optimizer is allowed to move."
