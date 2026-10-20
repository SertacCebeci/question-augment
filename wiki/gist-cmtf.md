---
description: "A goal-state inference layer that scores candidate symbolic goals and exposes clarification as a causal action, instead of a tool call, whenever the top goal's confidence or margin is too low."
aliases: ["GIST-CMTF", "goal-state inference layer", "goal-aware causal filtering"]
sources: ["babu-2026-gist"]
---
# GIST-CMTF

> Before letting a causal tool-filtering pipeline commit to a goal, score
> how confident and how separated the top candidate goal is, and route to
> a clarification action rather than a tool call when it is not.

## Definition / Mechanism

Babu & Shukla (2026) extend Causal Minimal Tool
Filtering (CMTF) — a prior method that exposes only the next causally
necessary tool given a known symbolic goal state — with an upstream layer
that first infers the goal itself. A module H maps the request, current
state and tool-contract context to a ranked set of candidate symbolic
goals with confidence scores; let p⋆ be the top score and p(2) the
second. In the paper's own simplest instantiation, [[efe-planning-as-variational-inference|ambiguity]] is a
disjunction of two threshold tests: "ambiguity can be decided using a
confidence threshold τ and a margin threshold δ" — the top candidate is
rejected if its confidence is below τ or its lead over the runner-up is
below δ.[^c1]

When that test fires, the system does not fall back to an ad hoc
clarifying turn: "We model clarification as a causal action rather than
an external fallback. A clarification action has its own preconditions
and effects," represented in the same precondition/effect vocabulary as
every other tool, so a clarification like "ambiguous goal →
goal specified" is one causal step among others rather than an
exception path.[^c2]

If the test does not fire, the accepted top goal is handed to CMTF
unchanged, which exposes the next minimal causal tool frontier toward
that goal.

## Why it matters

Across seven model backends, six filtering methods and 120 controlled
tasks (5,040 runs), GIST-CMTF reaches 97.0% task success, against 80.1%
for always taking the top-confidence goal without clarification
("top-goal CMTF") and 82.9% for choosing the goal whose description is
textually closest to the request ("semantic-goal CMTF"); the oracle that
is handed the true goal reaches 99.5%.[^c3]

## Limits

The ambiguity test's own worked form (confidence + margin thresholds) is
offered as "the simplest implementation," with τ and δ set for the
evaluation rather than learned or tied to a task-independent value of
information; the paper states the detector may otherwise be a learned
classifier, so the thresholded rule is one instance, not the method's
necessary form. All 120 tasks are constructed by the authors over a
deterministic mocked tool environment (calendar, email, files, contacts,
authorization) with hand-labeled candidate and intended goals; no
external benchmark or human user is involved, so the reported rates are
this benchmark's, not a general property of tool-using agents.

## Related

[[missing-input-clarification-gate]] · [[wrong-goal-execution]] ·
[[entropy-threshold-clarification-trigger]] · [[value-of-information]]

[^c1]: babu-2026-gist — "In the simplest implementation, ambiguity can be decided using a confidence threshold τ and a margin threshold δ"
[^c2]: babu-2026-gist — "We model clarification as a causal action rather than an external fallback. A clarification action has its own preconditions and effects"
[^c3]: babu-2026-gist
