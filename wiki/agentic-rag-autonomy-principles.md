---
description: "Three tests (autonomous strategy, iterative execution, interleaved tool use) check whether the model, not a fixed pipeline, drives retrieval; the authors' table passes only their own method."
aliases: ["agentic RAG criteria", "truly agentic RAG", "RAG autonomy dimensions", "Naive Agentic RAG"]
sources: ["doi-10-48550-arxiv-2602-03442"]
---
# Agentic RAG autonomy principles

> A retrieval method counts as agentic here when the model, not an external
> rule, decides the strategy, adapts the number of rounds, and conditions each
> tool call on what the previous calls returned.

## Definition / Mechanism

The paper's distinction is about who controls the retrieval workflow. Its
introduction says that "neither approach is truly agentic, as the model is not
allowed to adapt the workflow based on the specific task, choose different
interaction strategies, or decide when sufficient evidence has been gathered to
provide an answer."[^c1] Two families are named as failing this: single-shot
retrieval that concatenates passages into the input, and predefined workflows
that the model follows step by step.[^c2]

The authors turn this into three binary tests, stated in their appendix:[^c3]

1. **Autonomous Strategy.** The model dynamically chooses high-level moves
   (whether, when and how to retrieve, decompose, verify, re-plan) "without
   being constrained to a single pre-specified workflow," rather than having
   those moves "decided by external rules/classifiers/evaluators."
2. **Iterative Execution.** The method runs multiple rounds and "can adapt the
   number of rounds based on intermediate results," rather than being strictly
   one-shot.
3. **Interleaved Tool Use.** Each tool call is "conditioned on observations
   from previous tool outputs instead of a fixed toolchain that is always
   executed in the same order," in a ReAct-like action, observation, reasoning
   loop.

The point of the criteria is that they separate two things that are often
bundled: having an agent loop, and having the agent decide the loop. A method
can run many retrieval rounds and still fail the first test if an external
classifier chooses each round's action. Under this reading, the mechanism that
matters is where the decision to stop, retrieve again, or switch
interface sits. The paper's own evidence for this is that a naive agentic
variant with a single embedding tool "consistently outperforms Naive RAG and
previous baselines," which the authors take as showing the value of the
autonomy itself rather than of any particular tool.[^c4]

## Limits

- The criteria are the authors' own, and the verdict is theirs too. Their
  table marks A-RAG as the only method that "fully satisfies all three," and
  they grade other methods as partial or boundary cases ("∆") on the same
  scale. A judge with other criteria could reach a different ranking.[^c5]
- Each test is a yes/no property of a method's design, but the paper's
  evidence for the autonomy effect is comparative accuracy. That shows an
  association between the design and better scores, not that autonomy in a
  given dimension causes the gain. The paper's ablation varies tools, not the
  degree of autonomy.
- The principles say nothing about cost. A method that decides freely may
  spend more rounds; the paper's test-time scaling results show accuracy rising
  with step budget, but the criteria do not say when extra rounds are worth it.
- The evidence comes from open-domain multi-hop QA with two backbone families.
  Whether the same three tests sort methods the same way on other tasks is not
  shown.
- The paper claims the agent "spontaneously generalizes to diverse workflows"
  under the hierarchical toolset, but it does not catalogue those workflows
  against the three tests, so the link from the criteria to observed behaviour
  is asserted rather than measured.[^c6]

## Related

- [[hierarchical-retrieval-interfaces]] — the tool design the paper pairs with
  these criteria; its ablation is the paper's test of tool granularity, not of
  autonomy.
- [[retrieval-utilization-gap]] — separates retrieval failure from use failure,
  a distinction the autonomy tests do not draw.

[^c1]: doi-10-48550-arxiv-2602-03442 — "neither approach is truly agentic, as the model is not allowed to adapt the workflow based on the specific task"
[^c2]: doi-10-48550-arxiv-2602-03442 — "designing an algorithm (with or without graph structures) that retrieves"
[^c3]: doi-10-48550-arxiv-2602-03442 — "We identify three key principles to determine whether a RAG method is truly agentic"
[^c4]: doi-10-48550-arxiv-2602-03442 — "consistently outperforms Naive RAG and previous baselines"
[^c5]: doi-10-48550-arxiv-2602-03442 — "A-RAG is the only method that fully satisfies all three"
[^c6]: doi-10-48550-arxiv-2602-03442 — "the agent spontaneously generalizes to diverse workflows tailored to various"
