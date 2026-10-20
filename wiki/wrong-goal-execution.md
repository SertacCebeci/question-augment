---
description: "A tool-using agent's failure mode in which it completes a causally valid tool sequence toward an inferred goal that differs from the user's true intended goal, distinct from choosing the wrong tool."
aliases: ["wrong-goal execution"]
sources: ["babu-2026-gist"]
---
# Wrong-goal execution

> The tool path can be internally correct and the outcome still wrong,
> because the agent never checked it was solving the right problem.

## Definition / Mechanism

Babu & Shukla (2026) define wrong-goal execution as the
case where an agent reaches an inferred goal ĝ that does not match the
user's intended goal g_true, by way of a tool sequence that is itself
causally valid for ĝ: "We define wrong-goal execution as the failure mode
in which the agent executes a causally valid tool sequence for an
inferred goal ĝ that does not match the intended goal g_true."[^c1]

The paper distinguishes this from wrong-tool selection, where the goal is
known and correct but the wrong tool is chosen for it: "In wrong-tool
selection, the agent chooses an incorrect tool relative to a known goal.
In wrong-goal execution, the agent may choose tools that are causally
valid relative to an inferred goal, but the inferred goal itself is not
the user's intended objective."[^c2]

## Why it matters

Measured on the paper's 120-task tool-use benchmark, methods that commit
to a goal without checking whether it is sufficiently specified show a
substantial rate of this failure: "Top-goal CMTF has a wrong-goal
execution rate of 19.4%, and semantic-goal CMTF has a wrong-goal
execution rate of 16.7%. [[gist-cmtf|GIST-CMTF]] reduces this rate to 2.5%,
corresponding to an 87.1% relative reduction versus top-goal."[^c3]

This makes wrong-goal execution a failure that neither tool-selection
accuracy nor task-completion rate alone will surface: a run can select
every tool correctly relative to the goal it committed to and still miss
the request, so the metric requires a separately annotated intended goal
per task, not just a gold tool trace.

## Limits

The rate is measured only on the paper's own constructed benchmark
(explicit, ambiguous, missing-variable and clarification-required
requests across five workflow domains) with a deterministic mocked
environment; whether the 19.4%/16.7% baseline rates generalize to other
tool libraries, request distributions, or live (non-mocked) tool
execution is not established. The definition itself presupposes an
annotated ground-truth intended goal for every request, which the paper
supplies by construction and a deployed system would not have.

## Related

[[gist-cmtf]] · [[missing-input-clarification-gate]] ·
[[clarification-request]]

[^c1]: babu-2026-gist — "We define wrong-goal execution as the failure mode in which the agent executes a causally valid tool sequence for an inferred goal ĝ that does not match the intended goal g true"
[^c2]: babu-2026-gist
[^c3]: babu-2026-gist
