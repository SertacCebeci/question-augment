---
description: "Ranks candidate interventions — query, human-confirmed suggestion, or autonomous fill — by a utility-gain-cost-risk score, after a safety filter excludes over-authority candidates."
aliases: ["Trust-Calibrated Supervisory Controller", "TSC", "trust-calibrated supervisory control"]
sources: ["zhang-2026-impact"]
---
# Trust-calibrated supervisory controller

> Ranking which field to touch and who should touch it — human query, human
> confirmation, or autonomous fill — as one scored choice over a
> safety-filtered candidate set, not two separate decisions.

## Definition / Mechanism

Zhang et al. (2026) build an annotation agent that
incrementally resolves a partially specified structured event (a
Human-Object-Interaction record) field by field. At each step, every open
or revisable field generates a candidate intervention $\xi$ — "a target
field or field bundle, an interaction surface, and an authority level."
Candidate-conditioned estimates of propagation gain, interaction cost, and
overwrite risk are recalibrated from interaction history and combined with
immediate utility into one score: "Candidates are then ranked by
$S(\xi;c_h) = \lambda_1 U(\xi;c_h)+\lambda_2 \bar P(\xi;c_h)-\lambda_3
\bar C(\xi;c_h)-\lambda_4 \bar R(\xi;c_h)$."[^c1]

The score is not applied to the whole candidate set: "We enumerate all
candidates in $Q(c_h)$ and remove any that violate a lock constraint or
exceed the current authority policy, yielding the executable set
$Q_{safe}(c_h)$," and only then is the intervention chosen as the
arg-max of $S$ over $Q_{safe}(c_h)$ — a hard, pre-scoring exclusion of
anything that would revise an already human-confirmed field or act above
the controller's current authority grant.[^c2]

## Why it matters

The wiki's other selection criteria on this stall ([[mutual-information]],
[[expected-information-gain]], [[value-of-information]]) rank *which axis*
to constrain next but are silent on *who resolves it* — a question stall 4
asks separately. TSC answers both with one scored pass: the same candidate
carries both a field target (the stall-2 question) and an authority level
— query, suggest, or auto-complete (the stall-4 question) — and one linear
score orders all of them jointly, subject to a safety filter that runs
before the score, not after.

In a user study (9 participants, procedural HOI annotation), the fielded
system reduced manual actions "from 13.33 to 11.53 actions per event"
(a 13.5% reduction), raised the Complete Event Match Rate "from 42.22% to
46.67%," and recorded "95 accepted automated operations with zero
confirmed-field violations across all logged interactions."[^c3]

An ablation isolates what the controller itself buys, separately from the
completion model it ranks: "Without TSC, the uncalibrated system attempts
over 700 autonomous semantic applications in the one-shot phase, of which
approximately 50 are incorrect... With TSC, these high-risk interventions
are intercepted and downgraded from autonomous execution to
human-confirmation prompts, confining autonomy to high-confidence regimes
without sacrificing coverage." TSC does not change offline predictive
accuracy — it changes only which authority level a given prediction is
allowed to act under.[^c4]

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | Mixed-initiative supervisory control (human-robot / human-AI annotation): hard safety pre-filter, then linear multi-criteria scalarization over remaining candidates | Ranking candidate axis-and-source pairs — which field, and at what authority (query/suggest/auto) — for a structured elicitation agent |
| What survives | The two-stage shape: exclude anything unsafe or over-authority *before* scoring, then rank survivors by one weighted linear combination of gain, cost and risk | Unchanged in form; the argmax-over-safe-set structure does not depend on the HOI domain |
| What does not | The specific $\lambda$ weights and the vision/statistics-derived estimators for $P$, $C$, $R$ | Calibrated to structured HOI event annotation from interaction history; the paper gives no evidence the same weights or estimator design transfer to a different axis space, and does not compare the linear score against a non-linear alternative |

## Limits

- One domain, one user study (procedural HOI event annotation, 9
  participants): the headline reduction and match-rate figures are this
  system's measured outcome, not a general result about trust-calibrated
  ranking.
- The safety guarantee (zero confirmed-field violations) is produced by
  the lock-constrained feasible set that removes unsafe candidates before
  scoring, not by the linear score itself; the paper does not test what
  happens if the safety filter is removed and only the score is trusted.
- The $\lambda$ weights are described as tuned/calibrated but the paper's
  extract available here does not give their values or a sensitivity
  analysis, so "linear scalarization is sufficient" is not itself an
  established claim, only the operating point reported.
- `zhang-2026-impact` is a 2026 arXiv preprint (confirmed to exist and
  match this title via a search of the arXiv listing) but is not yet peer
  reviewed and carries `status: queued` (unverified by the wiki's source
  pipeline) at the time of this note. [?]

## Related

[[mutual-information]] · [[value-of-information]] · [[learned-deferral]] · [[bayesian-self-escalation]]

[^c1]: zhang-2026-impact — "Candidates are then ranked by S(ξ ; ch ) = λ1U(ξ ; ch )+λ2 P̄(ξ ; ch )−λ3C̄(ξ ; ch )−λ4 R̄(ξ ; ch ),"
[^c2]: zhang-2026-impact — "We enumerate all candidates in Q(ch ) and remove any that violate a lock constraint or exceed the current authority policy, yielding the executable set Qsafe (ch )."
[^c3]: zhang-2026-impact — "Full Assist reduces user operations from 13.33 to 11.53 actions per event, confirming that the system shifts annotators from repetitive low-level editing toward high-level decision making"
[^c4]: zhang-2026-impact
