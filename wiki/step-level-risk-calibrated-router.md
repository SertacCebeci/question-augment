---
description: "A step-level router trained with a Brier-calibration loss plus a CVaR-constrained tail-risk objective decides, mid-trajectory, whether a weak agent should escalate to a stronger one."
aliases: ["R2V router", "R2V-Agent router", "risk-calibrated step-level router", "step-level SLM-LLM routing"]
sources: ["hemadri-2026"]
---
# Step-level risk-calibrated router

> Instead of routing a whole query to a cheap or expensive model before
> execution, a per-step router estimates the probability that the weak
> agent will fail the episode *from here* and escalates only when that
> calibrated risk crosses a cost-derived threshold.

## Definition / Mechanism

Hemadri, Mohammed, Maheshwary et al. (2026) target agentic
POMDPs, where difficulty is trajectory-dependent rather than fixed at the
prompt: "task difficulty shifts mid-trajectory after flaky tool calls,
truncated observations, or compounding local errors — making pre-execution
routing brittle."[^c1]

At each step $t$ a compact risk feature vector $f_t$ (verifier scores,
token [[entropy]], candidate consistency, horizon fraction) feeds a router
$r_\psi(f_t)$ trained with a Brier-[[calibration]] loss toward the conditional
probability that the deployed small model will fail the episode, plus a
Conditional-Value-at-Risk-constrained Lagrangian that penalizes routers
that are cheap on average but brittle on tail perturbation seeds. The
hard rule escalates when $r_\psi(f_t)$ exceeds a threshold and budget
remains. That threshold has a closed form derived from the cost-sensitive
routing loss $\ell_{route}$: "If $0 \le c_{LLM} - c_{SLM} \le \kappa$, the
clipped threshold equals $(c_{LLM}-c_{SLM})/\kappa$" — the Bayes-optimal
cut is set by the escalation-cost gap divided by the failure penalty, not
tuned by search.[^c2]

Across HumanEval+, TextWorld and TerminalBench with four small-model
backbones, "R2V improves the reliability-cost frontier: it achieves 94.3%
HumanEval+ success with 0.60% LLM escalation, recovers TextWorld from
64.6% SLM-only success to 98.2% at 41.7% escalation, and reaches 93.3%
TerminalBench success at 33.9% LLM calls, roughly half the heuristic-router
cost."[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Agent architectures (this paper) | R2V router / R2V-Agent router | exact — the paper's own two names for its central component |
| Agent architectures (this paper) | risk-calibrated step-level router | exact — the paper's descriptive term, used in the abstract |
| Agent architectures (this paper) | step-level SLM-LLM routing | close — names the routing *problem* the router solves, used interchangeably with the router itself in the paper's framing |

## Why it matters

On stall 2, this is a stop/escalate decision made from a score built for
another purpose — the same pattern as [[value-of-information]] cutting a
threshold on expected gain — but the score here is a *trained, calibrated*
failure-probability rather than a hand-read confidence or entropy signal,
and the cut point is derived from cost parameters rather than fit by grid
search. It sits next to [[bayesian-self-escalation]] (same role: decide
mid-trajectory whether to hand off to a stronger model) but answers it with
a differently-shaped object: a regression-calibrated, cost-derived
threshold trained offline on a fixed policy's residual failures, not a
belief updated online under a proven-optimal dynamic-programming rule.

## Transfer

| | |
|---|---|
| **In its home field** | Proper-scoring-rule calibration (Brier score minimized by the true conditional probability) and CVaR-constrained risk-sensitive reinforcement learning (penalize the tail of a cost distribution, not just its mean) |
| **Here** | Both losses trained jointly on an agent's step-level risk features to produce the escalation signal |
| **What survives** | The Bayes-optimal-threshold argument: once the router is Brier-calibrated, the cost-optimal hard cut is a closed-form function of the escalation/execution cost gap (see[^c2] above) |
| **What does not** | The oracle guarantees are conditional on the router actually being well calibrated at deployment; the paper supplies no proof that the CVaR-Lagrangian training converges to that calibrated optimum, only that it discourages tail-brittle solutions empirically |

## Limits

The routing labels $y_t$ mark contexts on trajectories where the SLM's
*episode* later failed, not ground-truth step-correctness — a step
preceding an eventual failure need not itself have been the wrong action,
so the calibration target is a proxy. The cost-optimal-threshold argument
(Corollary 6) assumes a known, fixed cost ratio $c_{LLM}/c_{SLM}$ and a
correctly Brier-calibrated router; deployment uses a plug-in estimate, and
the excess-cost bound the paper gives is only as tight as that calibration
error. `hemadri-2026` is a 2026 arXiv preprint, not yet peer-reviewed. [?]

## Related

[[bayesian-self-escalation]] · [[confidence-calibrated-cascade-judgment]] · [[learned-deferral]] · [[value-of-information]]

[^c1]: hemadri-2026 — "task difficulty shifts mid-trajectory after flaky tool calls, truncated observations, or compounding local errors - making pre-execution routing brittle."
[^c2]: hemadri-2026 — "If 0 ≤ cLLM − cSLM ≤ κ, the clipped threshold equals (cLLM − cSLM )/κ."
[^c3]: hemadri-2026 — "R2V improves the reliability-cost frontier: it achieves 94.3% HumanEval+ success with 0.60% LLM escalation, recovers TextWorld from 64.6% SLM-only success to 98.2% at 41.7% escalation, and reaches 93.3% TerminalBench success at 33.9% LLM calls, roughly half the heuristic-router cost."
