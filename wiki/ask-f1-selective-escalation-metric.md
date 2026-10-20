---
description: "The harmonic mean of question precision and blocker recall scores whether an agent asks about the right things — not merely whether it asks — and punishes question-spam by construction."
aliases: ["Ask-F1", "ASK-F1", "selective escalation metric", "Judgment Matrix"]
sources: ["arxiv-2604-09408"]
---
# Ask-F1: a harmonic-mean metric for selective escalation

> An agent that asks about every uncertainty wastes human resources; an
> agent that never asks produces confidently wrong outputs — one number
> that cannot be gamed from either side.

## Definition / Mechanism

Trinh et al. (2026) score an agent not on whether it
asks, but on whether its questions target the information gaps ("blockers")
a task actually has. "A SK -F1 captures this tension through precision and
recall over question-asking behavior." Given a task's registered
blockers $B$ and the agent's questions $Q$: precision is the share of $Q$
judged relevant to some blocker, recall is the share of $B$ addressed by a
relevant question, and Ask-F1 is their harmonic mean. Relevance is decided
by a fixed, replicable judge, not the agent itself or a free-form human
simulator: a frozen LLM "compares the agent's question against the
registered trigger questions and blocker descriptions and returns the
corresponding resolution if the question targets a specific blocker, else
the fixed string 'irrelevant question'."[^c2]

The harmonic mean is the load-bearing design choice, not an arbitrary
aggregation: "it architecturally penalizes gaming through question spam,
since an agent that achieves high recall by asking fifty questions per task
will be penalized by near-zero precision." The two-axis decomposition
also separates failure modes that a single pass-rate number conflates:
"high precision with low recall indicates an agent that under-asks and
confidently assume[s]; low precision with high recall indicates one that
spams users with questions. No current model scores consistently high in
both." Plotting agents on precision × recall × success (the "Judgment
Matrix") separates a good agent from three failure types occupying the same
task-success number: the lucky guesser (succeeds without asking, fragile),
the over-asker (noisy, slower than manual work), and confident
hallucination (never asks, forms wrong beliefs, delivers plausible but
incorrect output) — the quadrant task-completion metrics alone cannot see.

## Why it matters

Every existing agent benchmark supplies complete specifications and scores
only task completion, so an agent that silently guesses a missing
requirement and gets lucky scores identically to one that would have asked.
Ask-F1 is the first metric that makes the *choice* to ask — not just the
outcome of asking — the thing under measurement, and does so without a cost
model or a hand-tuned asking budget: the harmonic mean alone rules out
gaming by volume.

## Limits

- Precision and recall are defined only relative to a fixed blocker
  registry authored per task; the metric cannot detect a well-targeted
  question about a real gap the registry omitted.
- Relevance judgment is delegated to a frozen open-source LLM acting as a
  semantic judge; its own error rate against human judgment is reported
  only in an appendix this note does not draw from — unverified here.
- The metric presumes progressive discovery (blockers surface through
  exploration, not upfront); on a benchmark without that design, Ask-F1
  would not separate front-loaded question-spam from targeted escalation
  the same way.

## Related

- [[abstention]] — the answerer's-side analogue: a reject option instead of
  a forced answer, here scored on the asker's side instead.
- [[detection-to-abstention-gap]] — the same paper's failure analysis finds
  a model (Claude) that detects it is stuck without escalating, the
  agentic-tool-use form of this gap.
- [[question-budgets]] — the cost asymmetry Ask-F1's harmonic mean encodes
  structurally instead of as an external budget.
- [[act-silent-stop-decomposition]] — another benchmark's disjoint-rate
  decomposition of the same act-or-ask choice, for mobile GUI agents.
- [[shaped-ask-f1-reward]] — the RL reward this metric's sparse,
  harmonic-mean structure is decomposed into for training.

[^c2]: arxiv-2604-09408
