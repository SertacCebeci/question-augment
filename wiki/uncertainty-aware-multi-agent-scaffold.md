---
description: "A coding-agent scaffold that separates underspecification detection from execution, closing most of the resolve-rate gap to fully-specified tasks with difficulty-calibrated query rates."
aliases: ["UA-Multi", "uncertainty-aware multi-agent scaffold", "Intent Agent"]
sources: ["edwards-2026"]
---
# Uncertainty-aware multi-agent scaffold

> A coding-agent architecture that gives one agent the sole job of noticing
> missing information and halting the other, rather than asking each agent
> to interrupt its own execution to check.

## Definition / Mechanism

Edwards & Schuster (2026) evaluate LLM coding agents on an
underspecified variant of SWE-bench Verified, where a GPT-4o summarizer has
stripped detail from real GitHub issues and a GPT-5.1 user simulator holds
the withheld context. Their best configuration, UA-Multi, is two agents
sharing one [[backbone-of-a-formula|backbone]] LLM: a Main Agent with standard tools (read, edit,
execute) and an Intent Agent that at every turn reads the state history and
outputs one binary decision — is context missing — with no other tool.
Whenever it says yes, the Main Agent's next action is constrained to a user
query; otherwise the Main Agent proceeds on its own. "We design a
multi-agent scaffold consisting of two agents. The Main Agent is equipped
with standard tools to navigate repositories, edit files, and execute code.
The Intent Agent monitors the state history at each turn to determine if
the user's intent or repository context contains missing information."[^c1]

## Findings

Across Claude Sonnet 4.5 and Kimi K2.6, UA-Multi reaches a 69.40% task
resolve rate, against 54.8–61.6% for a single agent doing both jobs
(UA-Single) and the fully-specified upper bound (Full) at 70.4–72.8%: "It
achieves a 69.40% resolve rate, yielding a significant improvement over
UA-Single (p < 0.001) and closing the gap with the Interactive Baseline (p
= 0.621) and Full (p = 0.458) configurations."[^c2]

The query rate tracks task difficulty rather than firing at a constant
rate: "UA-Multi exhibits a 9.28% higher ask rate for medium ('15 min – 1
hour') tasks than easy ('<15 min') tasks, compared to only a 2.43%
increase for UA-Single."[^c3]

Restraint is calibrated, not indiscriminate: on the 156 (of 500) tasks
where UA-Multi asked nothing, it still resolved 76.92% of them, matching
the Hidden (no-interaction) baseline's 77.56% — "For the 156 tasks where
UA-MULTI refrained from asking, it still achieved a 76.92% resolve rate,
closely matching the Hidden baseline (77.56%)." A baseline that is
hard-prompted to always ask once ("Interactive Baseline") instead reaches
only 47.2–66.6% overall, partly from instruction-following failures where
the forced turn itself breaks task completion — asking is not free even
when cheap to trigger.[^c4]

## Why it matters

This is a second, independently-arrived-at answer to the question
[[multi-agent-clarification]] answers for task-oriented dialogue: when
several agents share one context, who gets to interrupt for a question.
MAC splits authority by **domain scope** (a supervisor and five domain
experts, each seeing different slots); UA-Multi splits it by **role**
(one agent only ever detects, the other only ever acts) with both agents
sharing the same backbone model and the same view of the state. The
measured effect is the same shape — decoupling beats folding the check
into the acting agent's own loop — but by a different mechanism, on a
different task family (code-editing trajectories up to 100 tool-call
iterations, not slot-filling dialogue turns).

## Limits

- One benchmark family (SWE-bench Verified, underspecified via GPT-4o
  summarization) and one user simulator (GPT-5.1) — a proxy the authors
  themselves flag as possibly "unnaturally cooperative" relative to real
  developers.
- [[calibration|Calibration]] is backbone-dependent: Kimi K2.6's UA-Multi asks far more
  (8.71 queries/task vs. 3.06 for Claude Sonnet 4.5) and does not close the
  gap to Full as tightly (p < 0.05 remaining), so "well-calibrated" is a
  property of this scaffold with a strong enough backbone, not of the
  architecture alone.
- The comparison to MAC above is this wiki's own reading of two papers
  that do not cite each other; no source measures the two split axes
  (scope vs. role) against each other directly.
- Frontier, proprietary-scale models only; the paper reports (citing prior
  work) that smaller open-weight models lack the calibration this result
  needs.

## Related

[[multi-agent-clarification]] · [[clarification-action-generation]] · [[uncertainty-decomposition]] · [[value-of-information]]

[^c1]: edwards-2026
[^c2]: edwards-2026
[^c3]: edwards-2026
[^c4]: edwards-2026
