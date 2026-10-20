---
description: "Two costs of a higher-order query: order, the longest chain of nested beliefs it requires, and agent count, how many experts' beliefs it depends on; both burden the expert, not the principal."
aliases: ["order complexity", "agent complexity", "elicitation order", "query order"]
sources: ["arxiv-2512-05271"]
---
# Query order and agent complexity

A query asked of an expert can be cheap or expensive to answer even when it
is one question. The paper separates two costs of a DAG-elicitable query set,
the one in [[dag-elicitable-queries]], besides the number of queries. Both
are properties of the chain of reasoning the query requires, not of the
number of questions.[^c1]

Order is the longer of the two chains. A query is "order 1 if it is scored
against Y", order 2 if it is scored against order-1 queries and Y, and so on.
The order of a query is the length of the longest path from it to Y in the
graph that elicits the set. The order complexity of a set is the smallest,
over graphs that elicit it, of the largest order among its queries.[^c2] The
paper reads it as "the maximum number of iterated beliefs involved."[^c3]

Agent complexity counts breadth rather than depth. For a query, take every
query reachable from it in the graph and collect the experts who answered
them; the size of that set is the query's agent complexity. The agent
complexity of a set is again the smallest, over graphs, of the largest
such size.[^c4] A query can depend on many experts at order 2: it is the
expectation of a sum over all other experts' posterior expectations.[^c5]

The two axes are independent. The paper's examples show this. A query set
with one query per expert, each scored against Y, has query size n, order 1,
and agent complexity 1.[^c6] A query that asks expert n to predict the sum of
all others' expectations has order 2 and agent complexity n. An
iterated-expectation chain, in which expert i's expectation of expert j's
expectation of expert i's ... is asked, "depicts an example with high order
complexity" (order 2m) "but low agent complexity (2)."[^c7] Length and
breadth are different burdens, and a designer who limits one does not limit
the other.

The paper states the reason these matter for the expert. "Complexity implies
a larger cognitive burden on experts in answering their queries."[^c8] On
agent complexity, the same burden takes a specific form: a query of large
agent complexity "requires agents to form precise beliefs about the beliefs and
behavior of many other agents."[^c9] The burden falls on the answerer. The
principal's cost is the query count, which the paper measures separately.[^c10]

The complexity measures are then used to state bounds. With query count
restricted to d, the best linear aggregation error the paper proves is
1 − d/n, and the paper notes that this inherits to the agent and order
complexity, both bounded by d.[^c11] When the query count is free but the
agent and order complexity are restricted to d, the error is smaller than
1 − d/n in the regime the paper calls d = o(√n) (the extracted text gives the
rate as 1 minus a Θ term in d and n; my reading of the exponents is not
certain). In the regime d = ω(√n), "as long as agents are able to reason about"
that many others and conduct that much nested reasoning, "high-quality aggregation
is possible in the worst case."[^c12]

## Limits

- Both measures are defined as minima over DAGs that elicit the same query
  set. A given set of queries may have a cheap graph and an expensive one; the
  definition charges the cheap one. A rule that is cheap in the paper's sense
  is not necessarily cheap to ask, because the graph is the principal's
  design and the expert sees only the local question. That gap is my
  inference from the definition.
- The burden is asserted, not measured. The paper says "intuitively" that the
  query count burdens the principal, and that order and agent complexity burden
  the expert.[^c13] No experiment compares answer quality across orders or agent
  counts. Whether an LLM or a person answers an order-3 query worse than an
  order-1 query is not in this text.
- The counts are for the partial information model, where each expert sees a
  subset of independent signals. Other information structures may give other
  counts.
- The paper does not give a lower bound for order complexity d = ω(√n) that
  matches its upper bound: "we are unable to derive tight lower bounds on
  error for" that regime.[^c14]

## Related

- [[dag-elicitable-queries]] — the query sets these measures are defined on
- [[robust-forecast-aggregation]] — the setting in which the bounds are stated
  and the error they bound

[^c1]: arxiv-2512-05271
[^c2]: arxiv-2512-05271 — "A query is order 1 if it is scored against Y"
[^c3]: arxiv-2512-05271 — "the maximum number of iterated beliefs involved"
[^c4]: arxiv-2512-05271 — "The agent complexity of Q is the maximum over"
[^c5]: arxiv-2512-05271 — "we ask expert n to predict the sum of"
[^c6]: arxiv-2512-05271 — "Q has query size n, elicitation order 1, and agent complexity 1"
[^c7]: arxiv-2512-05271 — "Figure 1c depicts an example with high order complexity"
[^c8]: arxiv-2512-05271 — "complexity implies a larger cognitive burden on experts in answering their queries"
[^c9]: arxiv-2512-05271 — "it requires agents to form precise beliefs about the beliefs and behavior of many other agents"
[^c10]: arxiv-2512-05271 — "Intuitively, while higher query complexity places more of a burden on the principal"
[^c11]: arxiv-2512-05271 — "an immediate corollary of Theorem 3 is that approximators of limited agent and order complexity"
[^c12]: arxiv-2512-05271 — "reasoning when answering queries, high-quality aggregation is possible in the worst case"
[^c13]: arxiv-2512-05271 — "higher order or agent complexity places a higher cognitive"
[^c14]: arxiv-2512-05271 — "While we are unable to derive tight lower bounds on error for"
