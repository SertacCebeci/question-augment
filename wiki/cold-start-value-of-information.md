---
description: "A pessimistic, ambiguity-set value-of-information rule for querying before the answerer's response distribution is known; at or below the standard estimate when the nominal model lies in the set."
aliases: ["pessimistic value of information"]
sources: ["zhu-2026"]
---
# Cold-start value of information

> When you do not yet know how the answerer responds, price a question by
> its worst case over the response models you cannot yet rule out — not by
> the one you hope is true.

## Definition / Mechanism

Zhu (2026) extends net [[value-of-information|value of information]] to a sequential
comparison: let $J_A(s)$ and $J_D(s)$ be the expected cost of accepting or
deferring the current output (each charging a retention penalty for
drift), and $J_{stop}(s)=\min\{J_A(s), J_D(s)\}$.[^c1]

The net one-step expected value of a query action $a$ is the drop in
$J_{stop}$ it is expected to buy under the response model $p(z\mid s,a)$,
minus its weighted cost:
$\mathrm{nEVI}(a\mid s_t) = J_{stop}(s_t) - \mathbb E_{z\sim p(z\mid s_t,a)}\,J_{stop}(T(s_t,a,z)) - \lambda_C\, c(a)$
(the paper's Eq. 3).[^c2]

A greedy controller queries the admissible action of maximum value,
"queries only when the maximum is positive," and is conditional on the
[[correctable-set|reachability gate]] — because "a response model that is
optimistic about what a click achieves can manufacture positive value for
an unreachable case."[^c3]

At deployment onset $p(z\mid s,a)$ is unknown, so Zhu (2026)
replaces the point estimate with an [[efe-planning-as-variational-inference|ambiguity]] set $\mathcal P_a$: "an
ambiguity set of response distributions consistent with prior evidence for
action a: for instance, all distributions within a divergence ball of a
simulated-user model, or all mixtures of an expert-agreement model and a
no-response model with bounded weight."[^c4]

The pessimistic net value (Eq. 5) takes the supremum of expected
post-query cost over $p \in \mathcal P_a$ instead of an expectation under
one assumed model, and must be positive for a query during the cold-start
phase; the paper calls this "conservative by construction: it suppresses
queries whose value depends on an optimistic reading of how clinicians
respond, at the cost of some missed opportunities."[^c5]

The exit from the cold-start phase has two conditions, both fixed before
deployment: the set shrinks toward the empirical response distribution
"once a minimum number of observed responses per channel and per stratum
is reached, with the minimum fixed in advance and the shrinkage schedule
reported"; and "strata that never reach the minimum remain permanently
pessimistic" — an under-observed source stratum never leaves the
worst-case regime.[^c6]

## Why it matters

Zhu (2026) claims no novelty for net value of information —
"we claim no novelty for it" — and places the paper's contribution in the
gated coupling of Eq. 4, "the coupling of channel-level value estimation
to a release decision that is gated by a reachability test," which is the
object of [[correctable-set]], not of this note.[^c7]

What this note adds is independent of that novelty question: the paper
"treat[s] the response model as an explicit staged object rather than an
assumption" and supplies a pre-declared rule for the interval before that
object is trustworthy.[^c8]

This wiki's reading of the stall-2 and stall-4 maps — not the paper's — is
that the existing rows price a question only once a response model is
assumed; the cold-start rule is a default for the state every asker
meeting a new source passes through first.

## Transfer

| | |
|---|---|
| In its home field | Distributionally robust optimisation: a minimax/worst-case value over an ambiguity set of possible models |
| Here | Valuing a query to a not-yet-modelled answerer, at the moment an asking system first meets that source |
| What survives | The ordering guarantee (pessimistic value $\leq$ standard value, given the nominal model lies in the set) and the shrink-on-evidence pattern: stay conservative until a pre-declared evidence minimum is met, then narrow the set toward what was observed |
| What does not | The specific ambiguity-set constructions offered are illustrative for one clinical setting; the paper gives no general rule for sizing the divergence ball or the mixture weight |

## Limits

- The ordering "pessimistic $\leq$ standard" presupposes the nominal
  model $p(z\mid s,a)$ is a member of $\mathcal P_a$: a supremum over a
  set that excludes the assumed model is not bounded by the expectation
  under it. A divergence ball centred on the nominal model satisfies this
  by construction; an arbitrary bounded mixture need not. The paper states
  the inequality without this condition.
- Single-author arXiv Perspective (2026), not peer-reviewed; the rule is
  proposed for one clinical setting and has no reported user or
  deployment. `method` here means a specified rule, not a practice in use.
- Proposed, not tested: the paper's own minimal pilot has not been run —
  "We therefore specify the smallest study that could refute its base
  layer, before any clinician is recruited and without new data
  collection," comparing the gated controller against "voxel-[[entropy]]
  querying, random querying, a fixed-click heuristic, and passive
  correction, holding total simulated effort equal."[^c9]
- A badly chosen ambiguity set can make the mechanism vacuous, with no
  diagnostic beyond a sensitivity check: "Sensitivity of the resulting
  policy to Pa should be reported alongside its performance, since a
  policy whose behavior is invariant to the ambiguity set is not actually
  using response information."[^c10]
- The retention penalty inside $J_A, J_D$ prices drift against a protected
  reference set of model parameters; an asker with no internal parameters
  to protect needs a different accounting for what $J_{stop}$ charges.

## Related

[[value-of-information]] · [[correctable-set]] · [[expected-utility]] · [[bounded-rationality]] · [[question-budgets]]

[^c1]: zhu-2026 — "Let JA (s) and JD (s) denote the expected costs of accepting and deferring, each including PR (s), and let Jstop (s) = min{JA (s), JD (s)}."
[^c2]: zhu-2026 — "The net one-step expected value of information is"
[^c3]: zhu-2026 — "queries only when the maximum is positive"
[^c4]: zhu-2026 — "an ambiguity set of response distributions consistent with prior evidence for action a: for instance, all distributions within a divergence ball of a simulated-user model, or all mixtures of an expert-agreement model and a no-response model with bounded weight."
[^c5]: zhu-2026 — "conservative by construction: it suppresses queries whose value depends on an optimistic reading of how clinicians respond, at the cost of some missed opportunities."
[^c6]: zhu-2026 — "once a minimum number of observed responses per channel and per stratum is reached, with the minimum fixed in advance and the shrinkage schedule reported"
[^c7]: zhu-2026 — "we claim no novelty for it"
[^c8]: zhu-2026 — "as an explicit staged object rather than an assumption"
[^c9]: zhu-2026 — "We therefore specify the smallest study that could refute its base layer, before any clinician is recruited and without new data collection"
[^c10]: zhu-2026 — "Sensitivity of the resulting policy to Pa should be reported alongside its performance, since a policy whose behavior is invariant to the ambiguity set is not actually using response information."
