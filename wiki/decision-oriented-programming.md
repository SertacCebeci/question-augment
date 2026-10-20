---
description: "A coding agent reifies each design decision it would otherwise make silently as a persistent, editable object, elicited from the programmer as a binary question and traced to a test."
aliases: ["DOP", "Aporia", "decision bank"]
sources: ["arxiv-2604-05203"]
---
# Decision-oriented programming

> Move the decision an agent would silently make into a persistent object
> the programmer answers with yes or no, and connect it to a test.

## Definition / Mechanism

Kasibatla et al. (2026) name the failure mode first: an
agent that turns a high-level goal directly into code makes many small
design decisions on the programmer's behalf, invisibly. Decision-oriented
programming (DOP) is a paradigm with three design goals — decisions are
explicit and structured, co-authored interactively, and traceable to code:
"(1) decisions are explicit and structured, serving as the shared medium
between the programmer and the agent; (2) decisions are co-authored
interactively, with the agent proactively eliciting them from the
programmer; and (3) each decision is traceable to code."[^c1]

**Aporia** instantiates DOP as a VS Code extension orchestrating three
[[clarification-request|Claude Code]] instances over the Agent Client
Protocol — a questioner, a planner and an implementer: "Aporia orchestrates
three specialized agents—a questioner, a planner, and an
implementer—each an instance of Claude Code controlled using the Agent
Client Protocol."[^c2]

Given a programmer's high-level goal, the questioner generates **binary
(yes/no) design questions** grounded in the current code, each carrying
Aporia's rationale for either answer: "In response, Aporia generates
yes/no questions meant to elicit design decisions relevant to the
goal."[^c3]

The questions surface inline as Question Bubbles; each answer is
stored, along with an optional free-text comment, as a persistent,
editable entry in a **Decision Bank** — a structured record the
programmer can also add to directly. The planner formalizes each accepted
decision into a property-grouped test suite (one suite per decision, not
per component), giving the decision an executable, checkable meaning; the
implementer then changes the codebase against the goal, the Decision Bank
and the tests. The binary format is a deliberate trade against
open-ended questions: answering "yes" or "no" to a surfaced question
exploits *recognition* of an already-held intent, cheaper than
*recalling and verbalizing* one from scratch.

## Why it matters

A within-subjects study (N=14) against Claude Code as a plan-oriented
baseline measured both the volume and the accuracy of elicited decisions.
Aporia participants made far more decisions, and elicitation did not
merely substitute for decisions they would have made anyway — it raised
the total: "participants using Aporia made 13.5 times more elicited
decisions (95% CI [10.9, 16.7], 𝑝 < 0.001) than those using Claude
Code. … Aporia users also made 2.99 times more decisions overall (95% CI
[2.69, 3.32], 𝑝 < 0.001)."[^c4]

A separate correctness analysis compared each participant's description
of their own implementation against the code they actually submitted:
"Mismatches like these were 79% less likely with Aporia (𝑅𝑅 = 0.21, 95%
CI [0.08, 0.55], 𝑝 < 0.001). On average, 4.7% of described policies were
mismatches with Aporia vs. 12.1% with Claude Code."[^c5]

Proactive, binary elicitation is the isolable mechanism behind both
effects: it is what a
plan-oriented baseline (prompt, generate, review) does not do
systematically, even though the same underlying agent (Claude Code) can
ask clarifying questions when it chooses to.

## Transfer

| | |
|---|---|
| **Home field** | Design rationale notation — Questions, Options, Criteria (QOC) |
| **Here** | Eliciting a coding agent's implicit design decisions from the programmer |
| **What survives** | Reifying a decision as an explicit, persistent, revisable object separate from the artifact it constrains |
| **What does not** | QOC's Options and Criteria structure collapses into a single binary question with rationale; Aporia does not track competing options or evaluation criteria, only accept/reject |

## Limits

- Single study, N=14, one baseline (Claude Code), one language/domain
  (Python web apps); generalization to other agents or task types is
  untested.
- The binary question format is a chosen trade-off, not validated against
  an open-ended alternative: several participants found some questions
  "too detailed" or "too obvious," and the paper reports no question
  quality or relevance metric, only decision counts and the correctness
  grid.
- Counting "non-elicited" decisions for the Claude Code baseline involved
  some subjectivity, a caveat the authors themselves flag.
- A design probe, not a production system: no measure of how question
  volume or Decision Bank size scales with task size, or of programmer
  fatigue over longer sessions.

## Related

[[decision-centric-design]] · [[structural-disagreement-clarification]] · [[clarification-request]]

[^c1]: arxiv-2604-05203 — "(1) decisions are explicit and structured, serving as the shared medium between the programmer and the agent; (2) decisions are co-authored interactively, with the agent proactively eliciting them from the programmer; and (3) each decision is traceable to code."
[^c2]: arxiv-2604-05203 — "Aporia orchestrates three specialized agents—a questioner, a planner, and an implementer—each an instance of Claude Code controlled using the Agent Client Protocol"
[^c3]: arxiv-2604-05203 — "In response, Aporia generates yes/no questions meant to elicit design decisions relevant to the goal"
[^c4]: arxiv-2604-05203 — "on average, participants using Aporia made 13.5 times more elicited decisions (95% CI [10.9, 16.7], 𝑝 < 0.001) than those using Claude Code. More interestingly, Aporia users also made 2.99 times more decisions overall (95% CI [2.69, 3.32], 𝑝 < 0.001) than Claude Code users."
[^c5]: arxiv-2604-05203 — "Mismatches like these were 79% less likely with Aporia (𝑅𝑅 = 0.21, 95% CI [0.08, 0.55], 𝑝 < 0.001). On average, 4.7% of described policies were mismatches with Aporia vs. 12.1% with Claude Code."
