---
description: "A controller tracks solved/pending sub-questions and failed queries, computes the ready set whose dependencies are met, and per-question chooses retrieve, rewrite or pure-inference answer."
aliases: ["Supervisor execution state", "ready-set scheduling", "process-aware orchestration", "static query graph", "topological sub-query execution"]
sources: ["arxiv-2604-17405", "arxiv-2511-22955"]
---
# Dependency-aware sub-question scheduling

> Once a plan is a graph rather than a list, "which question next" is not
> one decision but a per-step choice among the questions whose prerequisites
> are already met — and, for each of those, whether to ask the world at all.

## Definition / Mechanism

the STRIDE authors (2026) motivate this against a fixed
sequential pipeline, arguing that a concrete plan's sub-questions are not
uniformly ordered: "existing approaches treat multi-hop reasoning as a
rigid, sequential pipeline, ignoring the rich dependency structures inherent
in complex questions. In reality, sub-questions can exhibit diverse
relationships: some are strictly sequential … others are independent and
parallelizable … and yet others form fork-join patterns."[^c1]

Their Supervisor tracks this as explicit state rather than position in a
list: "the Supervisor maintains an execution state denoted by
$\Omega=(S,P,F)$, where $S\subseteq C_q$ is the set of solved sub-questions
with their answers, $P\subseteq C_q$ is the set of pending sub-questions
(with $S\cap P=\emptyset$), and $F$ is a partial map that, for each pending
sub-question $c_i\in P$, records the set of retrieval queries that yielded
no useful results. At each step, it identifies the set of ready
sub-questions $P_{ready}\subseteq P$ whose dependencies (i.e., required
answers in $S$) are satisfied."[^c2]

For every ready sub-question the controller then chooses one of three
actions, not "retrieve" by default: "(1) If $c_i$ is fact-seeking and
$F(c_i)=\emptyset$, issue retrieve with a concise, entity-grounded query
$z_i$; (2) If $F(c_i)\neq\emptyset$, generate a rewrite via paraphrasing or
semantic reformulation, ensuring $z_i\notin F(c_i)$; (3) If $c_i$ requires
only reasoning over known answers (e.g., intersection, comparison), trigger
answer — bypassing retrieval and delegating to the reasoning module."[^c3]
A failed retrieval does not repeat the same query; it accumulates into $F$
and forces the next attempt on that sub-question to differ from every prior
miss, and a sub-question with everything it needs already in $S$ is answered
by inference instead of another retrieval call at all.

Because readiness, not list position, gates execution, independent
sub-questions run together and dependent ones wait: "the Supervisor enables
parallel execution of independent sub-questions (e.g., $c_1$ and $c_2$ in a
set-intersection question), while deferring dependent steps (e.g., $c_3$)
until their prerequisites are resolved."[^c4]

## Why it matters

This is a scheduling answer to "which question next" that sits below the
plan produced by [[entity-agnostic-reasoning-skeleton]]: the plan fixes
*what* sub-questions exist and their dependency edges, the Supervisor decides
*when* and *how* each one is pursued, re-evaluating the ready set every
iteration against newly solved facts rather than committing to an order in
advance. Replacing it with fixed-order sequential execution degrades every
dataset, most on MuSiQue, whose questions have the deepest dependency chains
in the paper's ablation set: "w/o Supervisor replaces our process-aware
supervisor with a conventional sequential execution pipeline, where
sub-questions are answered in fixed order and each retrieval depends solely
on the previous answer. The resulting performance degradation, particularly
on MuSiQue (-0.105 EM), highlights the importance of dynamic scheduling and
dependency-aware control in handling complex reasoning graphs with parallel
or conditional branches."[^c5]

## A graph fixed before execution

Comp-LLM (Sridharan, Roy, Raghunathan and Roy, 2025) applies the same
readiness rule to a graph that is built before any sub-query runs. A
decomposer emits the sub-queries and their pairwise dependencies, the
edges become a query graph, and an executor walks that graph in
topological order. The authors' motivation is the static case: multi-hop
question answering is a task "where the full execution plan is known ahead
of time but cannot be exploited for parallelism."[^c6] In their design the
dependency edges are the only state the scheduler needs: "the Query
Executor consists of a runtime scheduler that determines an execution plan
by identifying the nodes within the dependency graph that can execute in
parallel, thereby minimizing overall latency."[^c7]

This is the same ready-set idea as the Supervisor above, with one change
of timing. The STRIDE supervisor recomputes readiness after every retrieved
answer, so it can react to new evidence; the Comp-LLM scheduler computes
readiness from edges fixed in advance, so it cannot. The reported effect
is a latency gain, not an accuracy one: "Finally, Comp-LLM also achieves
1.1x-1.7x improvement in latency over the sequential processing of
sub-queries."[^c8] (Conjecture of this note: the ready set of a fixed DAG
is cheap to recompute, so the static form is the natural one when the
plan is known; whether it is also the better one on a question whose
answers change the plan is not shown by this work.)

## Limits

The ablation removes dynamic scheduling and query reformulation together (a
"conventional sequential execution pipeline" also drops the rewrite-on-miss
behavior), so the −0.105 EM MuSiQue figure is the effect of the whole
control layer, not dependency-aware parallel scheduling isolated from
retry-on-failure. The action rule for "fact-seeking vs. inference-only" is
itself decided by an instruction-following LLM call each iteration, and the
extract gives no separate accuracy figure for how often that action choice
is correct. All numbers are again the same three English multi-hop
benchmarks used throughout the paper.

The static-graph result has its own limits. The 1.1x-1.7x figure compares
parallel with sequential execution of the same graph inside Comp-LLM; it
does not compare a fixed graph with a dynamic supervisor, so which schedule
answers a given question faster or better is not established here. The
graph's edges come from a decomposer fine-tuned on dependency labels that
were produced by GPT-4o for the benchmark sets,[^c10] and the parts of the
paper read for this note do not report how often those edges are wrong; a
wrong edge would fix the schedule before any answer exists to correct it
(conjecture). The authors name the scope limit themselves: "this work only
applies to reasoning tasks that are static in nature."[^c9] Their
interactive example, games in which user input changes the next decision,
is the case where the supervisor's re-evaluation is needed and the static
graph is not.

## Related

[[entity-agnostic-reasoning-skeleton]] · [[decomposer-planner-centric-rl]] · [[self-ask-decomposition]] · [[expected-information-gain]] · [[value-of-information]]

[^c1]: arxiv-2604-17405
[^c2]: arxiv-2604-17405
[^c3]: arxiv-2604-17405
[^c4]: arxiv-2604-17405
[^c5]: arxiv-2604-17405 — "w/o Supervisor replaces our process-aware supervisor with a conventional sequential execution pipeline, where sub-questions are answered in fixed order and each retrieval depends solely on the previous answer. The resulting performance degradation, particularly on MuSiQue (-0.105 EM), highlights the importance of dynamic scheduling and dependency-aware control in handling complex reasoning graphs with parallel or conditional branches."
[^c6]: arxiv-2511-22955 — "the full execution plan is known ahead of time but cannot be exploited for parallelism."
[^c7]: arxiv-2511-22955 — "the Query Executor consists of a runtime scheduler that determines an execution plan by identifying the nodes within the dependency graph that can execute in parallel, thereby minimizing overall latency."
[^c8]: arxiv-2511-22955 — "Finally, Comp-LLM also achieves 1.1x-1.7x improvement in latency over the sequential processing of sub-queries."
[^c9]: arxiv-2511-22955 — "this work only applies to reasoning tasks that are static in nature."
[^c10]: arxiv-2511-22955 — "employ GPT-4o to only identify the dependencies between the sub-queries."
