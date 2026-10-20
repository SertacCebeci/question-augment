---
description: "The probability costly external support would materially improve an AI agent's output; the optimal support-seeking policy under a missed-support-error bound is a threshold on it."
aliases: ["value of support", "SDS-Opt", "strategic decision support optimization"]
sources: ["kiyani-2026"]
---
# Value of support

> A framework for deciding whether an AI agent should act alone or pay for
> costly external support (a human, a tool, a stronger model): separate the
> *value* of support from its cost, and optimise the rate of support calls
> subject to a bound on the error of missing support that was needed.

## Definition / Mechanism

Kiyani et al. (2026) let $X$ be the agent's input, $Y_0$ the
output it produces unsupported, and $Y_1$ the output it would produce with
support. A binary indicator $g(X,Y_0,Y_1)$ marks whether support was
materially beneficial on that instance. The **value of support** is
"val(x, y0 ) := P(g(X, Y0 , Y1 ) = 1 | X = x, Y0 = y0 )" — the probability
that calling support would produce a substantially better outcome, given
what the agent has produced so far. The **missed-support error** of a
strategy $a$ is "P a(X, Y0 ) = 0 | g(X, Y0 , Y1 ) = 1", i.e. "the
probability that the agent acts alone, conditioned on support being
beneficial." The strategic decision support optimisation (SDS-Opt)
minimises how often support is called subject to keeping this error at or
below a declared $\varepsilon$.[^c1]

Theorem 3.1 characterises the optimum: "There exists an optimal solution to
(SDS-Opt) of the form a⋆ (x, y0 ) = 1{val(x, y0 ) > τ ⋆ }, with possible
randomization on the boundary." The optimal population-level policy is
therefore a single threshold on the value-of-support quantity, not on
confidence, [[entropy]], or any other proxy computed from the agent's own
output alone.[^c2]

## Why it matters

The result gives the wiki a second, formalism-distinct answer to "ask for
help or act alone": rather than a Bayesian posterior over eventual success
([[bayesian-self-escalation]]), the optimal cut is over a directly-defined
benefit probability, and the constraint is stated as a missed-benefit error
rate rather than a cost-weighted expected value. It licenses treating any
support-seeking rule — clarifying question, tool call, human escalation —
as a threshold on one comparable quantity once $g$ is fixed for the task.

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | constrained statistical decision theory (Neyman–Pearson-style optimal rule under a one-sided error bound) | when an AI agent should call for external support instead of acting alone |
| What survives | the shape of the result: the optimal randomised rule under a one-sided error constraint is a threshold on a single scalar statistic | unchanged in form — Theorem 3.1 is proved directly for val(x, y0 ) |
| What does not | in Neyman–Pearson the statistic is a [[likelihood-ratio|likelihood ratio]] with a known sampling distribution | val(x, y0 ) is a benefit probability defined per task via $g$, with no closed form for $\tau^\star$ and no distributional assumption offered at this population level |

## Limits

Theorem 3.1 is a population-level optimality result: it assumes the joint
distribution of $X, Y_0, Y_1$ (and hence val) is known. It says nothing
about how to estimate val or set $\tau^\star$ from data — that is a
different object (the online algorithm, [[strategic-oversight-support-seeking]]).
The indicator $g$ is itself a per-task modelling choice (a verifiable-answer
match in some of the paper's four example domains, a quality-metric cut in
another), so "value of support" is not one fixed quantity across tasks.
`kiyani-2026` is a 2026 arXiv preprint, not yet peer-reviewed. [?]

## Related

[[bayesian-self-escalation]] · [[value-of-information]] · [[strategic-oversight-support-seeking]] · [[sprt]]

[^c1]: kiyani-2026 — "val(x, y0 ) := P(g(X, Y0 , Y1 ) = 1 | X = x, Y0 = y0 )"
[^c2]: kiyani-2026 — "There exists an optimal solution to (SDS-Opt) of the form a⋆ (x, y0 ) = 1{val(x, y0 ) > τ ⋆ }, with possible randomization on the boundary"
