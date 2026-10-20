---
description: "An answer is committed only when the field-of-view coverage of the task-relevant region passes a threshold; a query is called unanswerable once its relevant region is fully explored."
aliases: ["geometric examination", "FoV coverage gate", "post-inference geometric examination", "coverage-verified answer commitment"]
sources: ["arxiv-2512-02458"]
---
# Geometric coverage answer gate

> An embodied agent accepts or refuses its own answer by a measure that
> does not come from the model: how much of the region the question
> depends on has actually been seen, not how confident the model feels.

## Definition / Mechanism

The agent keeps a 2D occupancy map and a cumulative coverage map C of the
cells its saved observations have looked at. Coverage is computed by
"ray casting from the agent’s pose to identify visible cells."[^c1]

The answer is produced in two phases. First, reasoning modules work on the
memory: a global step prunes the 3D scene graph "to isolate task-relevant
sub-graphs", a local step retrieves the keyframes those sub-graphs point to,
and a question-answering step writes the answer.[^c2] Second, a geometric
examination checks that answer against the coverage map. For each
task-relevant room the paper uses the "coverage rate η to represent the
explored proportion of this room".[^c3] If that rate for all task-relevant
rooms "exceeds a predefined threshold, the inference is deemed grounded and
accepted."[^c4]

The branch matters for asking and answering alike. If relevant space is
still unexplored, the answer is declined and exploration continues. If an
answer exists and the relevant space is covered, the agent commits to it.
If no answer exists, the examination looks at the irrelevant rooms, and only
when no unexplored area remains is the query labelled
"unexplored areas remain, the query is formally labeled as unanswerable."[^c5]
So refusal is licensed by exhaustion of the search region, not by the model
failing to find something. The paper states the aim directly: the mechanism
"prevents premature task termination, detects inexecutable tasks, and
mitigates redundant revisiting of explored space."[^c6]

The reason given for an external measure is that model-based confidence is
unreliable here. The paper says prior approaches "rely on model-based
confidence heuristics and often suffer from calibration issues", and that
the gate uses "model-agnostic geometric information (i.e., FoV coverage) to
provide an unbiased, external verification."[^c7] The two failure modes it
targets are "premature termination, where the agent hallucinates an
answer/success before fully exploring", and endless back-and-forth in
explored space.[^c8]

Reported effect: removing the FoV mechanisms from both reasoning and
exploration "leads to a sharp decline in both accuracy" and efficiency; the
paper gives "SSPL drops by ∼ 11% in EMN with GPT5" as one instance.[^c9]

## Transfer

The part that plausibly survives outside navigation is the decision shape:
commit, explore, or refuse, each keyed to a count of how much of the set
that could hold the support for an answer has been examined. For a question
answered from documents or tables, the "region" would be the set of
sources that could contain the fact, and the coverage would be the share of
that set actually read. This is my inference; the paper does not test it,
and nothing in the text I read covers non-spatial domains.

## Limits

- The relevant set is not verified externally. The gate is external to the
  answer, but "task-relevant" comes from the scene graph that the MLLM's
  own pruning step builds.[^c2] A wrong relevance judgement leaves the gate
  passing on the wrong rooms. My inference: the gate is only as external as
  the relevance step.
- Coverage measures space seen, not objects recognised. A covered cell can
  hold an object the MLLM missed. The text does not test this gap.
- The threshold is called "predefined", but the value and any sweep over it
  do not appear in the slices I read.
- The ablation removes FoV mechanisms from reasoning and exploration
  together ("in reasoning and exploration (3DSPMR w/o Geo).")[^c10] so the
  effect of the answer gate alone is not isolated from the Geo-Sem exploration
  module.
- Memory gating is a separate mechanism. Its reported benefit is a smaller
  image store, not accuracy: the paper says the FoV-driven gate "filters
  redundant observations while retaining essential visual information."[^c11]
- The benchmark is small on the infeasible side: "scenario includes 10 tasks,
  4 of which are infeasible."[^c12] Infeasibility is the claim the gate is
  most needed for, and it rests on a benchmark of this size.

## Related

- [[coverage-driven-retrieval-control]] — the same shape, coverage deciding
  when to stop, in legal element retrieval; there the coverage is over a
  fixed schema of required elements, here over the space the agent has seen.
- [[planner-dynamic-stopping]] — the sufficiency judgement made by the
  model itself; the gate replaces that judgement with a geometric count.
- [[calibration]] — the model-confidence signal the paper argues against as
  a basis for committing.
- [[abstention]] — the "unanswerable" label is an abstention whose licence
  here is exhaustion of the search region, not the model's uncertainty.

[^c1]: arxiv-2512-02458 — "ray casting from the agent’s pose to identify visible cells."
[^c2]: arxiv-2512-02458 — "prunes the 3D scene graph G to isolate task-relevant sub-graphs;"
[^c3]: arxiv-2512-02458 — "coverage rate η to represent the explored proportion of this room:"
[^c4]: arxiv-2512-02458 — "exceeds a predefined threshold, the inference is deemed grounded and accepted."
[^c5]: arxiv-2512-02458 — "unexplored areas remain, the query is formally labeled as unanswerable."
[^c6]: arxiv-2512-02458 — "this mechanism effectively prevents premature task termination, detects inexecutable tasks, and mitigates redundant revisiting of explored space."
[^c7]: arxiv-2512-02458 — "model-agnostic geometric information (i.e., FoV coverage) to provide an unbiased, external verification."
[^c8]: arxiv-2512-02458 — "geometric awareness, MLLMs exhibit two failure modes: (1) premature termination, where the agent hallucinates an answer/success before fully exploring;"
[^c9]: arxiv-2512-02458 — "removing the FoV-based mechanisms leads to a sharp decline in both accuracy"
[^c10]: arxiv-2512-02458 — "in reasoning and exploration (3DSPMR w/o Geo)."
[^c11]: arxiv-2512-02458 — "driven gating mechanism, which filters redundant observations while retaining essential visual information."
[^c12]: arxiv-2512-02458 — "scenario includes 10 tasks, 4 of which are infeasible"
