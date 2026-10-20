---
description: "Asking an expert to predict another's report, with each answer scored against that report, makes truthful answers an equilibrium; chained queries form a DAG ending at the target."
aliases: ["higher-order queries", "iterated-expectation queries", "DAG-elicitable query set", "expectation-of-expectation queries"]
sources: ["arxiv-2512-05271"]
---
# DAG-elicitable queries

A forecaster can be asked for more than a forecast of the target. The
query can ask for a forecast of another forecaster's forecast. The
mechanism that makes such answers worth giving is a payment: each answer is
scored by a proper rule against the thing it predicts. When the thing
predicted is itself another expert's elicited report, the scoring chains.
The paper's claim is that "incentivized to report truthfully, so is expert j"
once expert i is paid to report truthfully.[^c1]

The concrete step is small. A quadratic score elicits a mean: the expected
score is maximised by reporting the posterior expectation. The same score,
applied to a report Y_i instead of the target Y, elicits "E[Y_i | S_j]", the
expectation that expert j forms of expert i's expectation. "One could take this
scheme a step further and elicit a query such as" that, and the
incentive carries over.[^c2][^c3] A set of queries is DAG-elicitable when the
queries can be arranged in an acyclic graph in which each query is elicitable
with respect to its out-neighbours and the target Y is the unique sink.[^c4]

The paper treats the whole rule as a one-shot Bayesian game: each expert
receives a payment that depends on the reports of its out-neighbours, and "then
it is a unique Bayes-Nash equilibrium for experts to report answers to each query
truthfully."[^c5] The paper calls this a straightforward observation, not a
deep result. Its weight lies in what the queries let the principal compute.

What they let the principal compute is the point of the paper. In the
two-signal example with one common signal, every agent's forecast is the sum of
a private and a shared component, and the known lower bound says no function
of those forecasts beats the prior by a non-vanishing amount.[^c6] Asking one
expert to predict another's report returns the shared component exactly, so
"by asking one additional question, we can optimally aggregate all information."[^c7]
The mechanism changes what the forecasts can reveal, not what they say.

A second family, difference queries, asks each expert what it adds to the
estimate formed by the experts before it in a fixed order. Summed over the
order, the answers cover the target's variance exactly once. The paper's
statement is that "this approach allows us to fully re-construct Y with only n
queries."[^c8] An earlier family, intersection queries, reaches the same
optimal error with 2^n queries, which the paper states as "the query complexity
of this aggregation rule is 2n".[^c9] The difference family is therefore the
cheaper of the two in query count, while its order and agent complexity stay
at n.

The chain of scoring is the mechanism's cost. A query whose payment depends on
another query's answer asks the expert to reason about that answer, and the
depth and breadth of that reasoning are the complexity measures of
[[query-order-and-agent-complexity]]. The scoring target is an expert's
reported posterior rather than a realised outcome, so the construction sits
close to [[peer-prediction]], where a peer's report stands in for the truth.
That resemblance is mine; the paper does not place its mechanism in that
literature except as a related area.[^c10]

## Limits

- Truthfulness is an equilibrium statement under a common prior. The experts
  share the prior: it is "a prior distribution D that is known to all"
  the experts, though the principal is assumed to know nothing of it.[^c11]
  Where experts disagree about the prior, the equilibrium claim is not
  covered by this text.
- The model is the partial information model: independent signals, each seen
  by a subset of experts, and the target is their sum. The paper says "we leave
  extensions to correlated signal structures as an exciting avenue for future
  work."[^c12]
- No experiment is reported. The equilibrium is in a model of rational experts
  who can compute the posterior expectation of a peer's posterior. Whether
  people or LLMs answer such queries truthfully, or at all, is not tested.
- The payment for a query depends on another expert's report, and the text
  does not analyse what happens when one report is wrong and the error feeds
  down the chain. That is my observation about the construction, not a
  result of the paper.
- The worked example uses an exact additive signal structure. Real forecasts
  are not sums of private and shared components, and the example shows that a
  query can recover a shared signal, not that real experts' forecasts contain
  one that a query can recover.

## Related

- [[query-order-and-agent-complexity]] — the cost axes of a DAG-elicitable
  query set: how long the chain is and how many experts it draws on
- [[robust-forecast-aggregation]] — the worst-case setting these queries are
  used to improve on
- [[peer-prediction]] — scoring a report against a peer's report without
  access to the truth; the closest existing mechanism family

[^c1]: arxiv-2512-05271 — "incentivized to report truthfully, so is expert j"
[^c2]: arxiv-2512-05271 — "it is well-known that the quadratic score"
[^c3]: arxiv-2512-05271 — "one could take this scheme a step further and elicit a query such as"
[^c4]: arxiv-2512-05271 — "Following the elicitation literature, we define a query function as elicitable if there is a payment"
[^c5]: arxiv-2512-05271 — "Then it is a unique Bayes-Nash equilibrium for experts to"
[^c6]: arxiv-2512-05271 — "aggregation function of the forecasts"
[^c7]: arxiv-2512-05271 — "by asking one additional question, we can optimally aggregate all information"
[^c8]: arxiv-2512-05271 — "this approach allows us to fully re-construct Y with only n queries"
[^c9]: arxiv-2512-05271 — "It follows that the query complexity of this aggregation"
[^c10]: arxiv-2512-05271 — "The areas of peer prediction [Fal23] and elicitation complexity"
[^c11]: arxiv-2512-05271 — "a prior distribution D that is known to all"
[^c12]: arxiv-2512-05271 — "We leave extensions to correlated signal structures as an exciting avenue for future work."
