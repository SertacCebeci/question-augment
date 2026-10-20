---
description: "A metric scoring an agent's response over every task, including ones whose right response is a clarification, abstention or refusal, so executable-but-wrong SQL still fails."
aliases: ["Business Truth Rate", "BTR"]
sources: ["lee-2026-business"]
---
# Business Truth Rate

> A response is scored against the world it actually returns to the
> asker, not against whether the query ran: a correctly executing query
> that gives the wrong business number, or an answer where a
> clarification was owed, counts as a failure.

## Definition / Mechanism

Lee (2026) defines Business Truth Rate (BTR) as
part of a [[calibration|reliability]]-first framework built to score a benchmark where
roughly half the tasks have no correct SQL at all: "A reliability-first
evaluation framework: Business Truth Rate, False Success Rate, coverage
separated from answer accuracy, calibration, and cost per correct
answer, with every denominator pinned and a pre-registered paired
bootstrap that fixed the permitted claim verb before any test number
existed."[^c1]

Its denominator is every task, not every returned answer: "Business
Truth Rate is over all tasks, False Success Rate over answers only,
coverage and answer accuracy over answerable tasks."[^c2]

A task whose required behavior is CLARIFICATION_NEEDED, ABSTAIN or
REFUSE is scored business-true only if the agent produces that behavior
against a written contract; a task with executable ground truth is
scored by result equivalence against accepted SQL.

## Why it matters

BTR is built to expose a gap execution-match metrics cannot see: agents
that run valid SQL on every task still score low once wrong business
numbers count as failures. "The baselines in this paper execute valid
SQL and reach Business Truth Rates between 0.275 and 0.300, while
returning wrong business numbers on most of the answers they give."[^c3]

Read against coverage and answer accuracy, BTR separates *how much a
system commits* from *whether the commitment was right*: "QueryProof
answers 0.600 of tasks and is correct on 1.000 of the answerable
questions it chose to answer; the baselines answer 1.000 and are correct
on 0.350."[^c4]

A system can raise BTR either by answering more correctly or by
declining more of what it would get wrong — the metric does not by
itself say which move was taken, only the net outcome on the asker's
side.

## Limits

BTR presupposes a benchmark with a written behavior contract for every
non-executable task (WarehouseReliabilityBench here); it is not a general
formula, only defined relative to such a contract. The benchmark backing
every number above is synthetic, which the paper itself flags: warehouses
generated from a pinned seed "buy executable ground truth... It costs
external validity, which is reported as a limitation." Resampling by
template family rather than by task widens the measured BTR gap's
interval to include zero, so the metric's *direction* here is better
supported than its *magnitude*.

## Related

[[rule-gated-behavior-gate]] · [[abstention]] · [[clarification-benchmarks]]

[^c1]: lee-2026-business
[^c2]: lee-2026-business — "Business Truth Rate is over all tasks, False Success Rate over answers only, coverage and answer accuracy over answerable tasks."
[^c3]: lee-2026-business — "The baselines in this paper execute valid SQL and reach Business Truth Rates between 0.275 and 0.300, while returning wrong business numbers on most of the answers they give."
[^c4]: lee-2026-business — "QueryProof answers 0.600 of tasks and is correct on 1.000 of the answerable questions it chose to answer; the baselines answer 1.000 and are correct on 0.350."
