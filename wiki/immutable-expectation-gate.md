---
description: "An agentic loop stops on a task not because the acting agent says it is done, but because a read-only, machine-parsed expectation is checked by a separate review agent."
aliases: ["self-assessed module", "SAM do-until loop", "expectation gate"]
sources: ["arxiv-2604-13180"]
---
# Immutable expectation gate

> A stopping rule enforced by keeping the criterion out of the hands of
> the agent that is trying to satisfy it.

## Definition / Mechanism

Liu & Gonski (2026) build SciFi's stopping mechanism
on a unit called a Self-Assessed Module (SAM): a plain-Markdown task
description with three parts — context, to-do, and a mandatory
**expectation**, the explicit end point the work must reach. The
expectation is not read by the executing agent as free text to interpret
loosely; it is deterministically parsed out of the task description by
fixed code, so it "cannot be fabricated by the agent during execution."
[^c1]

The same file is then frozen: "the agent is never allowed to modify
the task description, especially the expectation." The executor cannot
loosen, satisfy-by-editing, or quietly renegotiate its own stopping
criterion.
[^c2]

Satisfying the criterion and *declaring* it satisfied are two different
acts, assigned to two different agents. A work agent iterates
tool-use-and-execute until it claims completion; only then does a
separate review agent check the frozen expectation against what was
actually produced.
[^c3]

A claim of completion is not itself the stop signal — verification
against the read-only criterion is. This repeats recursively: a SAM
may decompose into sub-SAMs, and the parent is done only when all of
its sub-SAMs are completed and its own expectation is verified to be
met.
[^c4]

The loop is a three-stage pre-scan → work → review cycle ("do-until"):
any review failure, whether a false positive from the work agent or a
time cutoff, restarts the cycle with the review agent's failure notes
carried forward as memory, rather than silently extending the same
attempt.

This criterion-level stop is backstopped, not replaced, by a
resource-level one: the loop runs inside hard budget limits.
[^c5]

Per-model spend is metered independently — a model that exhausts its
budget is disabled and swapped for another of the same capability
rank.
[^c6]

The expectation gate answers *what counts as done*; the budget gate
answers *how long a stalled attempt is allowed to keep trying*.

## Why it matters

Most self-reported stopping ("I'm done") is unfalsifiable by
construction — the same process that did the work also judges it. This
gate separates the two: the criterion is fixed and unreadable-as-editable
by the executor, and the judgment is made by a second, independently
invoked process. That separation, not the specific SAM markup, is the
transferable part for any task-agnostic asker/answerer that must decide
when to stop iterating rather than merely when to claim it is finished.

## Limits

Single arXiv preprint (`arxiv-2604-13180`), not independently verified
by this wiki [?]. The mechanism presupposes a task whose expectation can
be stated in checkable natural language up front — the paper's own
framing restricts it to "closed-loop scientific tasks" with clear
objectives and verifiable stopping criteria; on genuinely open-ended,
creative tasks capability is still uncertain.
[^c7]

The paper also reports that an *over-specified* expectation can
backfire: excessive up-front instruction may instead constrain the
search and increase cost — so tightening the gate is not free, and the
right level of detail is itself task-dependent and evaluated only
qualitatively across a handful of internal HEP tasks, not benchmarked
against an alternative stopping design.
[^c8]

## Related

- [[rule-gated-behavior-gate]] — the same move (never let the acting model
  judge its own situation) applied to answer/clarify/abstain decisions
  rather than task completion.
- [[stopping-rules]] — the broader family of criteria this adds a new,
  systems-engineering member to.
- [[correctable-set]] — another gate that separates "can this be
  satisfied at all" from the agent's own claim of success.
- [[compound-ai-systems]] — the architectural frame (a system of
  distinct components, not one model) this gate is built inside.

[^c1]: arxiv-2604-13180 — "The SAM format is deterministically parsed, so that the expectation is always explicitly extracted from the task description and cannot be fabricated by the agent during execution."
[^c2]: arxiv-2604-13180 — "During execution, the SAM itself is treated as read-only, and the agent is never allowed to modify the task description, especially the expectation, thus preserving the robustness of the closed-loop process."
[^c3]: arxiv-2604-13180 — "After the work agent claims that the task or sub-task is complete, an independent review agent is invoked to check the expectation and verify that the current SAM has indeed been satisfied."
[^c4]: arxiv-2604-13180 — "A SAM is considered complete only when all of its sub-SAMs are completed and its own expectation is verified to be met."
[^c5]: arxiv-2604-13180 — "(bounded in practice by hard limits for budget control)"
[^c6]: arxiv-2604-13180
[^c7]: arxiv-2604-13180 — "its capability for genuinely creative exploration is still uncertain."
[^c8]: arxiv-2604-13180 — "excessive up-front instruction may instead constrain the search and increase cost."
