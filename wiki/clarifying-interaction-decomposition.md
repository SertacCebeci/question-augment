---
description: "A task-agnostic decomposition of resolving ambiguity through clarification into three subtasks — when to ask, what to ask, how to use the answer — each with its own evaluation."
aliases: ["three-subtask framework for clarification", "when/what/how-to-use decomposition"]
sources: ["zhang-2023"]
---
# Clarifying-interaction decomposition

> Splitting "should this system ask a clarifying question" into three
> separately-evaluable problems, so that a system's failure on one does not
> get blamed on the others.

## Definition / Mechanism

Zhang & Choi (2023) formally define resolving [[efe-planning-as-variational-inference|ambiguity]] with
clarifying questions as three sequential subtasks: "We begin this work by
formally defining three sub-tasks for resolving ambiguity with clarifying
questions: (1) determining when to ask for clarification, (2) identifying
what clarifying question to ask, and (3) reacting to clarification with the
proper response."[^c1]

Each subtask gets its own metric, deliberately decoupled from the other two:
Task 1 (when) is scored as uncertainty estimation — a scalar $u(x)$ per
input, evaluated by AUROC at separating inputs whose performance improves
with clarification from ones that do not, and by end-task performance under
a fixed interaction budget $b\%$; Task 2 (what) is scored on whether the
generated question exposes the ambiguity and elicits a disambiguating
response, using an oracle-generated clarifying QA pair as ground truth
rather than a system's own generation, so that Tasks 1 and 3 can be
evaluated without inheriting Task 2's errors; Task 3 (how to use the answer)
is scored by comparing the output produced after clarification, $\hat y$,
against the gold output $y^*$. The paper evaluates Tasks 1 and 3 directly
and substitutes an oracle for Task 2, because "our other two subtasks are
more novel and less well studied in LLMs."[^c2]

## Why it matters

The decomposition is the reason a single end-to-end "does the system ask
good clarifying questions" score is hard to interpret: a system can fail
because it asks when it should not (Task 1), asks the wrong thing (Task 2),
or asks well but fails to use the answer (Task 3), and these three failure
modes need different fixes. Framing "when to ask" as **uncertainty
estimation** rather than classification is itself a claim about stall 2:
selection is not a yes/no gate but a scored, budget-constrained ranking
problem, the same framing [[expected-information-gain]] and
[[value-of-information]] use from decision theory.

## Limits

- The three subtasks are evaluated with an oracle standing in for Task 2;
  no end-to-end system in this paper is scored on all three at once, so the
  decomposition's practical value — does fixing them separately actually
  compose into a better end-to-end asker — is not tested here.
- Restricted to single-turn clarification (one question, one answer) across
  QA, MT and NLI; it says nothing about multi-turn or sequential-axis
  selection (stall 2's "which axis **first**").
- "When to ask" is operationalised as a fixed interaction budget $b\%$ of
  examples, not as a per-example decision rule with an explicit cost of
  asking.

## Related

[[intent-sim]] · [[expected-information-gain]] · [[value-of-information]] · [[clarification-only-aleatoric-uncertainty]] · [[semantic-entropy]]

[^c1]: zhang-2023 — "We begin this work by formally defining three sub-tasks for resolving ambiguity with clarifying questions: (1) determining when to ask for clarification, (2) identifying what clarifying question to ask, and (3) reacting to clarification with the proper response."
[^c2]: zhang-2023 — "our other two subtasks are more novel and less well studied in LLMs"
