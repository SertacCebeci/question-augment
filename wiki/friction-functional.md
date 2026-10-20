---
description: "A weighted scalar F = F+ − F− scores a response's epistemic contribution — information gain against miscalibration, contradiction, hazard and value-conflict."
aliases: ["net friction functional", "unproductive friction", "productive friction"]
sources: ["arxiv-2604-25136"]
---
# Friction functional

> Five numbers instead of one: four ways a response can hurt, one way it can
> help, and their difference is what the response is worth epistemically.

## Definition / Mechanism

Pustejovsky & Krishnaswamy (2026) approximate a latent,
unobservable epistemic-risk functional with a tractable scalar built from
five observable component scores over a dialogue history $h$ and a candidate
response $y$. Four components are pooled into an **unproductive friction**
term:

> "F − (h, y) =
> w1 Unc(h, y) + w2 Contr(h, y) +
> w3 Haz(h, y) + w4 ValConf(h, y)"[^c1]

— miscalibration (Unc), contradiction with established context (Contr),
latent safety/normative hazard (Haz), and value conflict (ValConf): the four
failure modes that "systematically degrade belief quality over time." A
fifth component is pooled separately as **productive friction**:

> "F + (h, y) = w5 InfoGain(h, y)"[^c2]

— the expected information gain of interventions such as clarification and
verification, which deliberately spend short-term interaction cost to cut
long-term epistemic uncertainty. The net **friction functional** is the
difference:

> "F (h, y) = F + (h, y) − F − (h, y)"[^c3]

A positive $F$ means the response's productive friction outweighs its
unproductive friction — net epistemic benefit; a negative $F$ means the
opposite. This single scalar is what feeds [[frictive-intervention|frictive
policy]] training as a reward-shaping term, a preference signal, a
group-ranking criterion, or — in [[risk-conditioned-trust-region]] — a
risk estimate that expands or shrinks a policy's trust region.

The five components are chosen against three explicit design criteria: each
must correspond to a known epistemic pathology, each must be computable from
signals actually available at training or inference time —

> "Each component must be operationalizable from observable signals
> available at training or inference time, without access to the latent belief state or true risk functional."[^c4]

— and each must be monotone (higher score, more danger or more benefit).

## Why it matters

Training signals for asking-versus-acting are usually a single scalar
(a reward bonus for asking, a binary label) that cannot distinguish *why* a
response is risky from *why* it is informative. Decomposing the score into
named, separately-weighted components lets a designer see which pathology
(miscalibration vs. hazard vs. stale context) is driving a low score, and
lets [[risk-conditioned-trust-region|a downstream method]] treat "risk" as
something with structure rather than a single unexplained number.

## Limits

The five components are a "minimal basis," not a closed theory: the paper
states additional components may be added as new failure modes are
identified, and the weights $w_1 \ldots w_5$ are left as free parameters
with no fitting procedure given in this text. Each component (Unc, Contr,
Haz, ValConf, InfoGain) is itself only named here, not operationalized —
their concrete estimators are outside this extract's scope, so the
functional's practical behavior is unverified without them.

## Related

- [[frictive-intervention]] — the taxonomy whose classes the five
  components are built to mirror.
- [[threshold-optimality-of-clarification]] — the dominance condition that
  motivates weighting productive friction against its cost.
- [[risk-conditioned-trust-region]] — a method that uses this functional's
  value as a context-dependent risk estimate.
- [[information-gain-reward]] — a different operationalization of the same
  expected-information-gain idea that composes $F^+$ here.

[^c1]: arxiv-2604-25136 — "F − (h, y) = w1 Unc(h, y) + w2 Contr(h, y) + w3 Haz(h, y) + w4 ValConf(h, y)"
[^c2]: arxiv-2604-25136 — "F + (h, y) = w5 InfoGain(h, y)"
[^c3]: arxiv-2604-25136 — "F (h, y) = F + (h, y) − F − (h, y)"
[^c4]: arxiv-2604-25136 — "each component must be operationalizable from observable signals available at training or inference time, without access to the latent belief state or true risk functional."
