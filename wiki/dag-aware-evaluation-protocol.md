---
description: "Ordering an evaluator's checks by a prerequisite dependency DAG and skipping a check once its prerequisite has failed, so feedback names root causes instead of their downstream symptoms."
aliases: ["DAG-aware evaluation protocol", "DAG-based evaluation protocol"]
sources: ["wang-2026-asuka"]
---
# DAG-aware evaluation protocol

> Before turning a set of failed checks into feedback, order them by what
> depends on what, and stop reporting a symptom once its cause is already
> named — the receiver is told less, and told the part it can act on.

## Definition / Mechanism

Each evaluation criterion in [[asuka-bench|Asuka-Bench]] is annotated with a task type,
a difficulty weight, and prerequisite dependencies (e.g., a functionality
check that a feature's price updates correctly depends on the presence
check that the feature's elements exist at all); these dependencies induce
a directed acyclic graph (DAG) over the criteria attached to one task.
"[T]he UI Agent executes tasks following the topological order of the
DAG. A task is executed if and only if all of its prerequisite
dependencies have passed; if any prerequisite has failed or was not
executed, the task is skipped without evaluation." Skipped tasks produce
no feedback.[^c1]

The stated rationale: "This dependency-driven protocol avoids wasteful
evaluation of tasks whose foundations are unmet, and focuses the Code
Agent's attention on the root causes of failure rather than their
downstream symptoms."[^c2]

## Why it matters

Compared against a Flat protocol that evaluates every criterion
independently regardless of dependency status, the DAG protocol "cuts
evaluation token consumption by 23–26% ... and yields uniformly higher
fix rates because feedback is concentrated on root-cause failures (e.g.,
GLM-5 R2 task fix rate: 61.8% vs. 45.9%; MiniMax R2: 57.7% vs. 39.9%;
Seed-2.0-Pro R2: 35.7% vs. 30.9%)." The paper concludes DAG is "the
preferred protocol: more focused, slightly stricter, and substantially
cheaper."[^c3]

A softened variant (a parent criterion is non-blocking once at least 50%
of its own sub-criteria pass, threshold T=0.5) is adopted as the default
because strict blocking (T=1.0) under-credits work that later turns out
correct: relative to evaluating every task regardless of dependencies,
strict blocking loses a mean 6.0 pp of weighted Task Pass Rate, which the
soft variant shrinks to a mean 0.6 pp (worst case 1.6 pp).[^c4]

## Transfer

| | |
|---|---|
| In its home field | scoring an AI-generated software artifact against a fixed, pre-declared dependency DAG of test criteria for one benchmark task |
| Here | ordering which unmet constraints on $W$ get surfaced to an asker/answerer after a check, when some constraints logically presuppose others |
| What survives | the general principle — skip and withhold feedback on a downstream check once its prerequisite has already failed, so the receiver acts on the cause, not a cascade of its symptoms |
| What does not | the DAG itself was authored by hand per benchmark task (§3.2 of the source) and the domain is deterministic pass/fail UI testing; nothing in the paper shows a dependency structure can be discovered automatically for an open-ended question/answer setting, or that the same fix-rate/cost gain holds outside browser-grounded code evaluation |

## Limits

- The efficiency and fix-rate gains are measured on one benchmark's
  dependency graphs, authored by the benchmark's own construction
  pipeline, not on an independently validated notion of "root cause";
  a mis-specified DAG would misattribute blame in the same direction it
  currently corrects it.
- The comparison to the Flat baseline reuses Flat's numbers from an
  earlier version of the work rather than a fresh re-run under identical
  conditions to the reported DAG numbers, on the authors' own stated
  argument that a re-run was unnecessary because Flat's score is
  upper-bounded by evaluating every task; this note accepts that argument
  but a reader should note the two figures were not run in the same pass.
- Demonstrated only where dependency is a hard precondition (a UI element
  must exist before its behaviour can be tested); it says nothing about
  softer, probabilistic dependence between constraints.

## Related

[[asuka-bench]] · [[clarification-benchmarks]] · [[questioning-and-solving]]

[^c1]: wang-2026-asuka — "the UI Agent executes tasks following the topological order of the DAG. A task is executed if and only if all of its prerequisite dependencies have passed; if any prerequisite has failed or was not executed, the task is skipped without evaluation."
[^c2]: wang-2026-asuka
[^c3]: wang-2026-asuka — "cuts evaluation token consumption by 23–26% (GLM-5: 17.9M vs. 23.4M tokens; Qwen3.5-Plus: 18.4M vs. 25.0M) and yields uniformly higher fix rates because feedback is concentrated on root-cause failures (e.g., GLM-5 R2 task fix rate: 61.8% vs. 45.9%; MiniMax R2 : 57.7% vs. 39.9%; Seed-2.0-Pro R2 : 35.7% vs. 30.9%)."
[^c4]: wang-2026-asuka
