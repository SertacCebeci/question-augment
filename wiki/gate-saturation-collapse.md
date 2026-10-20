---
description: "When abstention is a discrete RL action under an error-penalized reward, the reward gradient and KL anchor share one saturating gate factor and vanish together."
aliases: ["collapse law", "gate-saturation collapse", "abstention collapse"]
sources: ["che-2026"]
---
# Gate-saturation collapse

> A policy trained to answer, abstain, or lose points for being wrong does
> not converge to the rational [[abstention]] threshold — it can converge to
> silence, while its own training-reward curve reads as improvement.

## Mechanism

Che, Yuan, Zhao & Yu (2026) study a policy-gradient learner with
a KL anchor to its base model (standard RLHF) under an error-penalized
reward ($+1$ correct, $-\lambda$ wrong, $0$ abstain). When abstention is a
discrete action, the model answers with probability $\sigma(v)$ for a gate
logit $v$; every gradient of the expected reward with respect to the gate
carries the [[saturation]] factor $\sigma'(v)$. The same factor multiplies the
KL anchor's restoring force, because for a Bernoulli gate
$\frac{d}{dv}\mathrm{KL} = \sigma'(v)(v-v_0)$.

"Reward and anchor share the factor σ ′ (v): where the gate" saturates,
both vanish together — the anchor supplies no restoring force on exactly
the coordinate that is collapsing.[^c1]

## The law

Under three conditions — blanket answering loses expected score, prompts
share a bounded confidence readout, abstention is a discrete action — the
model drifts toward refusing everything. Bernoulli KL to a fixed base is
bounded at the all-abstain vertex, so total abstention strictly beats the
base policy below an explicit anchor-strength threshold, with no dynamics
required.

"its mean training reward rising to zero like 1/t in training time" — up to
log factors, at a rate stable in the anchor strength, so the training curve
reads as improvement while coverage collapses.[^c2]

## The estimator sets the exponent

Group-normalized advantage estimators (GRPO) steepen the decay above a
knee at answer rate $\approx 1/G$ ($G$ the group size) and, below it,
silently replace the designed penalty $\lambda$ with an effective penalty
of 1, moving the trained threshold from $t^{*}=\lambda/(1+\lambda)$ to
$1/2$.

"Group normalization thus silently swaps in a rule whose" Chow threshold
is $1/2$, manufacturing the hallucinations the penalty rule was meant to
prevent.[^c3]

## Known as

| Field | Name | Status |
|---|---|---|
| rl-alignment (this paper) | collapse law | exact |
| rl-alignment (this paper) | gate-saturation collapse | exact |
| rl-alignment (informal, abstract) | abstention collapse | close — used loosely for the observed drift, while "collapse law" names the proved finite-time rate specifically |

## Evidence

Exact enumeration and simulation confirm the estimator-indexed menu of
predictions. Live experiments reproduce the collapse on 1.5B and 7B models.

"the rule silences questions the models demonstrably still solve" within
ten optimizer steps, isolated by ablation to the same mechanism.[^c4]

## Transfer

| | Home field (RL alignment) | Here (answerer's commitment, stall 10) | Survives | Does not |
|---|---|---|---|---|
| Object | A policy-gradient learner's gate logit deciding answer vs. abstain under a KL-anchored objective | The trained decision of how much an answerer commits to, and when it declines | The shared-factor mechanism: any regularizer whose gradient vanishes with the action probability ([[entropy]] bonus, forward-KL anchor) fails to arrest a drift toward non-commitment | Guarantees are proved for Bernoulli/mixture gate parameterizations and bounded readouts, not shown here for arbitrary decoder architectures without a gate coordinate |

## Limits

The theorem is proved for gate-and-mixture policy classes with a bounded
confidence readout and a fixed base-model correctness distribution; the
"lifting" to full sequence-level KL with trainable content (Theorem 2,
abridged in the extract read here) adds further conditions (branch-separable
content, an explicit KL-gradient regularity bound) not checked in this note
against the appendix. The finite-time law assumes gradient flow, not the
discrete-step, momentum-based optimizers used in practice; the paper closes
that gap only with matched live-model experiments, not a proof for
stochastic-gradient variants.

## Related

- [[value-of-information]] — the decision-theoretic reason abstention has a rational threshold at all
- [[investigative-question-grpo-training]] — a GRPO-trained question policy in the same training family, without the abstention gate
- [[confidence-report-repair]] — the structural fix this paper proves removes the shared vanishing factor

[^c1]: che-2026
[^c2]: che-2026 — "its mean training reward rising to zero like 1/t in training time"
[^c3]: che-2026 — "Group normalization thus silently swaps in a rule whose"
[^c4]: che-2026 — "the rule silences questions the models demonstrably still solve"
