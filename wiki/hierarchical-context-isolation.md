---
description: "A host/manager/worker agent hierarchy bounds the planner's context to step-response summaries, isolating decomposition and tool execution to scale wide information-seeking without saturation."
aliases: ["InfoSeeker", "near-decomposable agent hierarchy"]
sources: ["arxiv-2604-02971"]
---
# Hierarchical context isolation

> Give the planner only the sequence of step and result, never the
> subtasks, tool calls or intermediate traces that produced the result,
> and both the depth of reasoning and the width of parallel search can
> grow without the planner's own context ever saturating.

## Definition / Mechanism

Lee, Huang, He et al. (2026) structure an
information-seeking agent as three layers with a strict abstraction
boundary between each: a Host that plans high-level steps, a set of
domain-specific Managers that decompose a step into parallel subtasks
and validate the results, and Workers that execute one subtask each
through tool calls. "The host never accesses subtasks, tool calls, or
intermediate execution details. Its reasoning is strictly based on the
sequence of step–response pairs, which bounds host-level context growth
and enables long-horizon planning."[^c1]

At each iteration the Host emits a step $q_t$ and picks a Manager to
solve it; that Manager decomposes $q_t$ into $P_t$ subtasks, dispatches
them to Workers, reflects on the returned results (accepting or asking
for a revision), and aggregates them into one summary $y_t$ that is
appended to the Host's context. The aggregation is explicitly a
MapReduce pattern: "a sequential Map phase performs adaptive
decomposition into weakly coupled subtasks. Workers then execute these
subtasks concurrently under a concurrency budget $W_w$. Finally, a
sequential Reduce phase aggregates and compresses intermediate outputs
into a coherent step-level summary returned upstream."
[^c2]

Because subtasks are weakly coupled, worker execution time collapses from a sum
over subtasks to a max over them, so widening the worker pool buys
wall-clock speed without growing what any single agent — Host, Manager
or Worker — has to hold in context at once.

On two web-information-seeking benchmarks this yields both accuracy and
speed gains: "the system achieves a Success Rate of 8.38% (Avg@4) and
9.50% (Pass@4), representing a 64% improvement over the strongest
baseline."
[^c3]

Scaling the worker pool on a 20-query sample "reduces
[latency] from 911 seconds with a single worker to just 162 seconds with
17 workers, yielding a ≈5.7× speed-up. This result validates that
hierarchical context isolation and MapReduce-style aggregation
effectively mitigate the latency and context saturation issues
prevalent in sequential baselines"[^c4]

## Why it matters

Most agent architectures that decide what to search or ask next
accumulate everything — subtasks, tool traces, intermediate failures —
into one growing context that the same model must both plan from and
reason over; wide, data-intensive tasks saturate that context long
before the task is done. Hierarchical context isolation is a structural
answer that does not depend on a bigger context window: what propagates
upward across a layer boundary is a compressed step-response pair, not
the trace that produced it. That makes the two axes a selection policy
usually trades against each other — how deep to reason, how wide to
search — separately scalable, and it lets new domains (a new Manager
and Worker type) be added without touching the Host's planning logic.

## Limits

- Both benchmarks (WideSearch-en, BrowseComp-zh) are read by the same
  team; no independent replication is reported here.
- The Host still selects among Managers and the Manager still decides
  when to accept versus revise a batch of subtask results, but the
  extract read gives no scoring or ranking rule for either choice — the
  mechanism isolates context, it does not establish how a step or a
  revision is judged better than another.
- The reported gains use a heterogeneous model strategy — a stronger
  model (gpt-5.1) for Host and Managers, a cheaper model (gpt-5-mini) for
  Workers — so part of the measured effect may be this allocation rather
  than the hierarchy itself; the extract does not isolate the two.
- Concurrency budgets, the Manager's accept/revise thresholds, and
  scheduling overhead are named but not quantified in what was read.

## Related

[[state-gated-strategy-routing]] · [[decomposer-planner-centric-rl]] · [[context-pollution-naive-tool-addition]] · [[proact-architecture]] · [[role-differentiated-parallel-elicitation]]

[^c1]: arxiv-2604-02971 — "The host never accesses subtasks, tool calls, or intermediate execution details. Its reasoning is strictly based on the sequence of step–response pairs, which bounds host-level context growth and enables long-horizon planning."
[^c2]: arxiv-2604-02971 — "Information aggregation in InfoSeeker follows a MapReduce-inspired pattern Dean and Ghemawat [2008]. At the Host and Manager levels, a sequential Map phase performs adaptive decomposition into weakly coupled subtasks. Workers then execute these subtasks concurrently under a concurrency budget Ww . Finally, a sequential Reduce phase aggregates and compresses intermediate outputs into a coherent step-level summary returned upstream."
[^c3]: arxiv-2604-02971 — "the system achieves a Success Rate of 8.38% (Avg@4) and 9.50% (Pass@4), representing a 64% improvement over the strongest baseline (OpenAI o3-high Multi-Agent at 5.10% Avg@4)"
[^c4]: arxiv-2604-02971 — "end-to-end latency is reduced from 911 seconds with a single worker to just 162 seconds with 17 workers, yielding a ≈ 5.7× speed-up. This result validates that hierarchical context isolation and MapReduce-style aggregation effectively mitigate the latency and context saturation issues prevalent in sequential baselines"
