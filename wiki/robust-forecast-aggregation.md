---
description: "Robust forecast aggregation scores a rule by its worst-case error against the best use of pooled information; aggregating reported forecasts cannot beat a random expert, but extra queries can."
aliases: ["robust aggregation", "worst-case forecast aggregation", "robust aggregation of expert forecasts"]
sources: ["arxiv-2512-05271"]
---
# Robust forecast aggregation

A principal has several experts, each holding part of the information about a
quantity Y, and must turn their forecasts into one estimate. Robust
aggregation asks for a rule whose error is bounded without knowing how the
information is split among the experts. The error is taken in the worst case
over the information structure. The reference point is the best estimate the
pooled information allows, the posterior expectation of Y given every
signal.[^c1]

The standard result in this setting is pessimistic. Under projective
substitutes, the experts' posterior expectations cannot be aggregated to do
better than a fixed baseline: "no aggregation of the experts' individual
forecasts can outperform simply following a random expert."[^c2] The
introduction states the strength of that baseline: "aggregating forecasts from
n agents is only a constant factor better than randomly picking" one of them.[^c3]
The random-expert rule draws an expert uniformly and reports its
expectation; it is the reference against which any aggregation is measured.[^c4]
The error metric is the squared-error gap to the best estimate, normalised by
the gap between the prior and the best estimate, so that the prior has error 1
and the best estimate has error 0.[^c5]

The paper's change is to what the principal asks, not to how it combines the
answers. Asking a forecast of a forecast, and scoring it, lets the principal
recover shared information that the forecasts alone hide, as the
[[dag-elicitable-queries]] note describes. In the partial information model,
where each subset of experts observes its own independent signal and Y is
their sum, the paper gives the following tradeoffs.

- With at most d queries, the best achievable worst-case error is 1 − d/n.
  The paper's words: "each additional query reduces the best achievable error by 1/n."[^c6]
  The gain is linear and carries no early jump: "there are no early exponential
  improvements in adding one or two" more queries.[^c7]
- Restricting instead the agent and order complexity of the queries, and
  asking for linear aggregation rules, the error can be made to vanish when
  the bounds allow. The paper's summary: "as long as agents are able to reason about"
  ω(√n) other agents and conduct ω(√n)-order reasoning, "high-quality
  aggregation is possible in the worst case."[^c8] The cost measures are in
  [[query-order-and-agent-complexity]].

Earlier work framed the problem for two experts with a binary state. The
introduction of the paper cites it as the place the robust problem was first
posed, and it treats probabilistic forecasts over events.[^c9] The paper's
own setting is real-valued quantities, which is why its bounds are not the
binary ones.[^c10] The one earlier use of a peer-prediction mechanism for robust
aggregation, the paper says, is "in the simple setting of two experts and a
binary outcome."[^c11] That mechanism is [[peer-prediction]], and the
paper's query framework is a wider route to the same goal.

## Limits

- The results hold in the partial information model with independent signals.
  "We leave extensions to correlated signal structures as an exciting avenue
  for future work."[^c12]
- The 1 − d/n bound is a worst-case statement over the information structure.
  It says nothing about the error on a typical structure, and no average-case
  measure is reported.
- The tight characterisation holds only for linear rules: "we are only able to
  characterize tight upper bounds when" the restriction is to linear rules.[^c13]
  For the regime d = ω(√n), the paper states that "while we are unable to
  derive tight lower bounds on error for" that regime, so the vanishing error is
  an upper bound, not a matched optimum.[^c14]
- The gain depends on the principal being able to ask the richer queries and
  get truthful answers. The incentive guarantee is an equilibrium result under a
  common prior, covered in [[dag-elicitable-queries]]; a principal who cannot
  elicit those answers is back at the random-expert baseline.
- The paper's worked case is an exact additive model. Whether real expert
  pools have the structure that makes the vanishing error reachable is not
  tested here.
- The "error" here is the paper's normalised squared error. A different loss,
  such as log loss on probabilities, changes the benchmark, and the text does
  not say how the bounds transfer. That is my observation.

## Related

- [[dag-elicitable-queries]] — the query mechanism that changes the error
  bounds in this setting
- [[query-order-and-agent-complexity]] — the costs of the queries that reach
  the lower error bounds
- [[peer-prediction]] — the mechanism family the paper cites as the one earlier
  use of truthful peer scoring for robust aggregation, in the two-expert binary
  case

[^c1]: arxiv-2512-05271 — "the error expresses the worst-case difference in information expressed by A versus"
[^c2]: arxiv-2512-05271 — "can outperform simply following a random"
[^c3]: arxiv-2512-05271 — "aggregating forecasts from n agents is only a constant factor better than randomly picking"
[^c4]: arxiv-2512-05271 — "P is a randomized aggregation rule which outputs a uniformly random expert"
[^c5]: arxiv-2512-05271 — "the error expresses the worst-case difference in information expressed by A versus"
[^c6]: arxiv-2512-05271 — "each additional query reduces the best achievable error by 1/n"
[^c7]: arxiv-2512-05271 — "there are no early exponential improvements in adding one or two"
[^c8]: arxiv-2512-05271 — "reasoning when answering queries, high-quality aggregation is possible in the worst case"
[^c9]: arxiv-2512-05271 — "first introduced the problem of robust forecast aggregation"
[^c10]: arxiv-2512-05271 — "while we study aggregation of forecasts over real-valued"
[^c11]: arxiv-2512-05271 — "which applies peer prediction to robust aggregation, but in the simple"
[^c12]: arxiv-2512-05271 — "We leave extensions to correlated signal structures as an exciting avenue for future work."
[^c13]: arxiv-2512-05271 — "we are only able to characterize tight upper bounds when"
[^c14]: arxiv-2512-05271 — "While we are unable to derive tight lower bounds on error for"
