---
description: "The fraction of an agent's clarification interactions whose next navigation step is correct — separates asking in the right place from asking more often."
aliases: ["ISE", "Information-Seeking Effectiveness"]
sources: ["gao-2026"]
---
# Information-Seeking Effectiveness (ISE)

> Asking more is not the same as asking better; ISE is the metric that
> tells the two apart.

## Definition / Mechanism

Gao, Kang, Wang & Woo (2026) define ISE as a local diagnostic,
not a final-task metric: "the fraction of help interactions after which the
agent's next navigation action lands on the correct path... ISE tests
whether each identified help interaction was locally useful: if help was
requested and the next action was correct, the interaction was productive
at the one-step level."[^c1]

Under [[action-rating|ACTION-RATING]]'s controlled answer channel (answer
quality held fixed so that variation in ISE cannot be explained by better
or worse answers), self-gating separates volume from quality: "At τ=10,
the agent issues 6× more clarifications (2.4 vs. 0.4/record), yet ISE rises
from 50% to 74%... Virtually all additional volume is opportunistic, and
both modes attain ≈75% ISE."[^c2]

The dissociation runs the other way too at a looser threshold: "At τ=1,
volume increases further (5.9 QA/record) but ISE drops to 62%: the
additional questions are less likely to land on the correct path."[^c3]
More questions and better-placed questions are shown to be independent
outcomes of where the threshold is set — pushing the threshold too low
adds volume without adding usefulness.

## Why it matters

A count of clarification turns says nothing about whether they were asked
at the right decision points. ISE gives a per-interaction correctness
check that can rise while volume falls, or fall while volume rises,
making the two report different things. For any agent that logs a
navigation or task step after each question, ISE is a computable proxy for
"was this specific question worth asking" without requiring a downstream
utility function.

## Limits

- Computed under a controlled answer channel that fixes answer quality;
  "Because the controlled answer channel fixes answer quality, ISE
  variation across conditions reflects differences in where the agent
  sought help, not what it received." Under uncontrolled, model-generated
  answers, ISE is not shown to isolate location from answer quality in the
  same way.[^c4]
- Measured on one domain family (HTS classification) where "correct next
  navigation step" has a ground-truth taxonomy path; the metric needs a
  verifiable next-step target and does not obviously transfer to open-ended
  tasks without one.
- A one-step correctness probe: it does not measure whether the eventual
  final answer was correct, only whether the step immediately following the
  question was on the right path.

## Related

[[action-rating]] · [[value-of-information]] · [[entropy-threshold-clarification-trigger]]

[^c1]: gao-2026
[^c2]: gao-2026
[^c3]: gao-2026 — "At τ =1, volume increases further (5.9 QA/record) but ISE drops to 62%: the additional questions are less likely to land on the correct path."
[^c4]: gao-2026 — "Because the controlled answer channel fixes answer quality, ISE variation across conditions reflects differences in where the agent sought help, not what it received."
