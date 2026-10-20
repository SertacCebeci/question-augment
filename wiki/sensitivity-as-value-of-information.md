---
description: "**This wiki's inference, not a claim in [[sadeghi-2026|Sadeghi et al. (2026)]].** Wherever"
aliases: []
sources: ["sadeghi-2026"]
---
# Sensitivity analysis as a value-of-information proxy

> **This wiki's inference, not a claim in Sadeghi et al. (2026).** Wherever
> the object an agent is asking about is itself an input to an optimization
> problem, [[value-of-information]]'s usual blocker — no written utility —
> is already gone: the objective function *is* the utility, and local
> sensitivity analysis is a cheap, standing estimator of how much a
> parameter's uncertainty could still matter to the decision.

## The claim

[[value-of-information]]'s own limits say it "needs a utility function and a[^s1]
decision set — absent during exploration", and [[expected-information-gain]]
notes that VoI's exactness is blocked by the same missing ingredient: EIG
scores information, not decision relevance, precisely because no utility is
on paper. [[sensitivity-weighted-question-score]] shows one setting where
that ingredient was never missing — a natural-language optimization
problem is, by the time it reaches a solver, already a decision problem
with an explicit objective $z(\theta)$ — and shows a cheap procedure that
uses it: perturb $\theta_i$ by a handful of multipliers, re-solve, and read
the swing in $z$, the shadow price and the binding-constraint change as a
proxy for how much resolving $\theta_i$ could change the decision. Read
together, the two notes support a narrower version of Howard's bound: **in
any asking problem where the downstream use of the answer is itself the
solution of a mathematical program, an off-the-shelf, already-computable
quantity (post-optimal sensitivity) stands in for the otherwise-intractable
value-of-information computation**, in the same way [[semantic-entropy]]
stands in for EIG's nested expectation when the downstream use is free text.

## Why it matters

This narrows one of the wiki's own recorded disagreements — Selection's
"Information vs value": *"VoI wins in principle and loses in practice: it
needs a utility function, and exploration has none yet."* The claim here is
that "exploration has none yet" is a claim about *unstructured* exploration;
wherever the asker's downstream artifact already has a written objective
(scheduling, routing, allocation — anything that ends in a solve), the
practical obstacle Sadeghi et al. (2026) route around does not arise, and a
question-selection procedure can price decision-relevance without eliciting
anything further from anyone.

## Limits

- Sadeghi et al. (2026) never frame their score as an estimator of
  Howard's $\mathrm{VoI}(q)$, and they report no comparison against it or
  against an exact regret computation; the identification above is this
  wiki's reading of what the mechanism does, not a result the paper states
  or tests.
- The equivalence is only structural. Howard's $\mathrm{VoI}$ is an
  expectation over the *posterior* decision change; the sensitivity score
  is a *local*, finite-multiplier perturbation of the *current* point
  estimate, computed once before any answer, and carries no probabilistic
  guarantee of tracking the true expected regret.
- Restricted to problems already expressed as an explicit mathematical
  program with a scalar objective. A decision problem that has not yet
  been formalized this way (most of the wiki's other stall-2 settings) gets
  nothing from this note.
- Inherits [[sensitivity-weighted-question-score]]'s own limits: the
  benchmark-construction circularity, the reliance on a strong translator
  model, and the lack of formal validity for shadow prices outside
  non-degenerate LPs.

## Related

[[sensitivity-weighted-question-score]] · [[value-of-information]] · [[expected-information-gain]] · [[expected-utility]] · [[semantic-entropy]]

[^s1]: sadeghi-2026
