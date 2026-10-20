---
description: "A threshold rule routes a robot's joint posterior over target, anchor and frame to execute, clarify, reobserve, or abort, diagnosing which variable is ambiguous before asking."
aliases: ["posterior-to-decision policy", "RefGuard decision policy", "four-way decision interface"]
sources: ["wei-2026"]
---
# RefGuard decision policy

> A robot defers commitment on a referring instruction until a posterior over
> *which object, relative to which anchor, in which frame* is concentrated
> enough to act on safely — otherwise it asks, re-senses, or refuses.

## Definition / Mechanism

Wei et al. (2026) maintain a joint posterior over three coupled
latent variables — the target object, the anchor object a spatial relation
refers to, and the reference frame ("my left" vs. the robot's) — instead of
committing to a single most-likely value of each before planning. The
decision policy maps this posterior grounding state and feasibility evidence
to one of four decisions:

"The decision policy maps the posterior grounding state and feasibility
evidence to one of four decisions. RefGuard executes when the posterior
concentrates on a single feasible grounding interpretation and the [[planner-dynamic-stopping|planner]]
can produce a safe action. It clarifies when the top hypotheses disagree on
the target identity, anchor assignment, or reference-frame interpretation.
It reobserves when perceptual evidence is weak or stale, and aborts when no
compatible target, anchor, or satisfiable action constraint exists."[^c1]

Concretely: let $p_1,p_2$ be the largest and second-largest target-belief
masses, $\Delta_T = p_1-p_2$, $\bar H_T$ the normalised target [[entropy]], and
$\kappa = \tfrac12 p_1 + \tfrac12(1-\bar H_T)$ a posterior-concentration
score. The system ABORTs if no valid hypothesis remains, REOBSERVEs if
$p_1<0.50$ or $\kappa<0.40$, CLARIFYs if $\Delta_T<0.15$ or the target
entropy exceeds 1.50 nats or the competing anchor/frame hypotheses are not
action-equivalent, and otherwise EXECUTEs. Before asking, the system also
diagnoses *which* variable to ask about, from which of the top hypotheses
disagree:

"If the top rows disagree mainly on target identity, the case is labelled
TARGET-AMBIGUOUS, whereas competing anchor assignments yield
ANCHOR-AMBIGUOUS. When the rows share target and anchors but differ only in
reference frame, RefGuard returns FRAME-AMBIGUOUS."[^c2]

## Why it matters

On a real UF850 arm across identity-switch stress trials, this policy
produced zero wrong-object executions while VLA and LLM-based baselines that
commit early switched identity in 33–46% of the same trials ([[identity-switch]]).
It is a working instance of routing a *specific* axis of [[efe-planning-as-variational-inference|ambiguity]] — which
of target, anchor, or frame is unresolved — into a targeted clarifying
question rather than a generic "please clarify," and of treating reobserve
(gather more evidence passively) and abort (refuse) as decisions distinct
from asking.

## Limits

- The thresholds (0.50, 0.40, 0.15, 1.50 nats) are calibrated on 30
  development episodes disjoint from every evaluation set, then frozen —
  "Thresholds are selected on 30 development episodes, disjoint from every
  evaluation set, and then frozen for evaluation."[^c3]
- They are not derived from a general theory of ambiguity and are untested
  beyond this platform/task family.
- The rule needs enumerable, discrete hypotheses over target, anchor and
  frame, and an action-equivalence test between them; it does not extend
  directly to open-ended free-text referents with no discrete hypothesis
  table.
- $\kappa$ is used only for decision-making and is explicitly not a
  calibrated confidence metric (the paper's own caveat).

## Related

[[identity-switch]] · [[value-of-information]] · [[sprt]] · [[clarification-benchmarks]]

[^c1]: wei-2026 — "The decision policy maps the posterior grounding state and feasibility evidence to one of four decisions. RefGuard executes when the posterior concentrates on a single feasible grounding interpretation and the planner can produce a safe action. It clarifies when the top hypotheses disagree on the target identity, anchor assignment, or reference-frame interpretation. It reobserves when perceptual evidence is weak or stale, and aborts when no compatible target, anchor, or satisfiable action constraint exists."
[^c2]: wei-2026
[^c3]: wei-2026 — "Thresholds are selected on 30 development episodes, disjoint from every evaluation set, and then frozen for evaluation."
