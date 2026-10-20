---
description: "An RL policy and objective (MaxInfoRL) that adds information gain about hidden dynamics to task reward, weighted by an increasing function of epistemic coupling, so the agent probes rather than waits."
aliases: ["Dynamics Information-Seeking", "DIS", "MaxInfoRL objective"]
sources: ["banerjee-2026"]
---
# Dynamics Information-Seeking

## Definition / Mechanism

Banerjee & Goan (2026) distinguish their policy from
classical active perception, which targets state uncertainty alone: "This
involves executing exploratory actions specifically designed to isolate and
identify the underlying parameters of shifted dynamics θ. ... we select
actions that maximize [[expected-information-gain|expected information gain]], which highlights that the
policy πDIS is not maximizing reward, but rather the reduction of
uncertainty regarding the dynamics parameters (θ)".[^c1]

Run alone, this pure information-seeking policy would never stop probing to
complete the task, so the paper folds its information-gain term into a
composite objective rather than deploying it directly: "We propose the
MaxInfoRL objective, a unified control law which explicitly trades off task
performance, information gain, and risk."[^c2]

The trade-off is not fixed: the weight on information gain is itself a
function of the coupling metric [[compound-uncertainty-coefficient]] (κ).
"α = α(κ) is a monotonically increasing function of epistemic coupling...
it approaches zero in the Low Deficit regime (κ < τlow, restoring pure task
optimization) and dominates in the High Deficit regime (κ > τhigh), making
information gain the primary objective."[^c3]

## Why it matters

This is a concrete answer to "when and why should an agent actively query
rather than wait for information to arrive": query when the coupling metric
says the axes cannot be disentangled passively, and scale how much to query
by how coupled they currently are, rather than using a fixed
exploration budget or a constant intrinsic-motivation bonus. It reframes
axis selection (stall 2) as a continuously reweighted objective rather than
a one-shot ranking of candidate questions.

## Transfer

| | |
|---|---|
| Home field | Safe reinforcement learning / optimal experiment design |
| Here | A model of when an asking agent should shift from accepting incoming information to actively soliciting it, and how strongly, as a function of a measured coupling between uncertainty sources |
| Survives | Information gain as an added reward term scaled by a state-dependent coefficient; the qualitative claim that the right amount of active querying is not constant but should track how unresolved the coupling currently is |
| Does not survive | This is continuous control action selection, not discrete question selection — there is no candidate question set, no Λ-style stopping rule, and the risk term $R_{risk}$ has no stated analogue for a dialogue or QA setting |

## Limits

The objective is proposed and motivated but the paper's contribution here is
architectural framing plus the earlier proof-of-concept (Sec. 1.2) that
motivates it, not a demonstrated closed-loop trained agent under this exact
objective in the same 120-configuration sweep reported for the empirical
super-additivity result; readers should not read [[epistemic-trap]]'s
measured 77%-vs-46% gap as already produced by an agent using this
objective.

## Related

- [[epistemic-trap]]
- [[compound-uncertainty-coefficient]]
- [[expected-information-gain]]
- [[value-of-information]]

[^c1]: banerjee-2026
[^c2]: banerjee-2026
[^c3]: banerjee-2026
