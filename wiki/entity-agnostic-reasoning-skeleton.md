---
description: "A planner first emits an abstract, entity-free reasoning strategy over entity types, then grounds it into concrete sub-questions, cutting cascading errors from premature lexical commitment."
aliases: ["General Strategy", "Meta-Planner two-stage plan", "reasoning-first decomposition"]
sources: ["arxiv-2604-17405"]
---
# Entity-agnostic reasoning skeleton

> Decide *how to reason* — the shape of the sub-question graph, in entity
> types — before deciding *what to retrieve*, so a homonymous or ambiguous
> name never gets the chance to steer the plan.

## Definition / Mechanism

the STRIDE authors (2026) observe that iterative RAG
systems usually decompose a question straight into entity-bound sub-queries,
and that this is where multi-hop errors cascade from: "they often perform
entity-centric decomposition too early, before establishing a task-aligned
reasoning structure. This can cause cascading errors when entity names are
ambiguous."[^c1]

Their fix is a two-stage plan produced by a single Meta-Planner call, in
which structure is committed before names are: "Rather than decomposing the
question directly into entity-bound sub-queries, it first constructs a
General Strategy, which is an abstract representation of the reasoning flow
that is independent of specific entity names. Only after this high-level
logic is established does it instantiate a Concrete Plan of executable,
entity-grounded sub-questions."[^c2]

Formally the General Strategy $S_q=\{s_1,\dots,s_m\}$ is written over entity
*types*, and the Concrete Plan $C_q=\{c_1,\dots,c_n\}$ is derived from it only
afterward: "$S_q$ … is the General Strategy — an abstract sequence of
reasoning steps expressed over entity types (e.g., person, location, work),
independent of specific names. And $C_q$ … is the Concrete Plan — a minimal,
ordered set of executable sub-questions grounded in the entities and
relations from $q$, derived by instantiating $S_q$."[^c3]

The type-level path is what does the disambiguating. On "Who wrote the book
that the movie *Lincoln* was based on?", grounding immediately risks the
surface entity Abraham Lincoln; the type-level path avoids it: "if the system
first abstracts the reasoning path as [movie → source book → author], it can
correctly disambiguate 'Lincoln' as a film entity and avoid being misled by
homonymous references."[^c4]

## Why it matters

This answers stall 1 of question selection — which axis to ask next — one
level of abstraction higher than most decomposers: the first commitment a
STRIDE system makes is to a *shape* of dependency graph over untyped roles,
and only the second commitment binds names to it. That ordering is a
controlled within-system comparison (same model, same downstream Supervisor
and execution layer, only the abstraction stage removed), which isolates the
type-before-token step itself as the source of the gain rather than some
other property of STRIDE.

Forcing the planner straight to a concrete plan (the `w/o Meta-Planner`
ablation) degrades every dataset tested, up to 0.197 EM on 2WikiMultihopQA:
"forcing the planner to directly output a concrete plan without high-level
intent modeling … leads to significant performance drops across all
datasets … demonstrating that abstract planning provides crucial scaffolding
for robust multi-hop decomposition."[^c5]

## Limits

The "Lincoln" case is the paper's own illustration, not a measured
disambiguation-error rate — the ablation's EM/F1 deltas are downstream
answer-quality numbers, not a direct count of avoided lexical-ambiguity
errors, so how much of the gain is disambiguation versus better step
ordering in general is *unverified*. All numbers come from three English
multi-hop benchmarks (2WikiMultihopQA, HotpotQA, MuSiQue); whether the
General Strategy stage helps on questions without an ambiguous entity at all
is not separately measured.

## Related

[[self-ask-decomposition]] · [[decomposer-planner-centric-rl]] · [[dependency-aware-subquestion-scheduling]] · [[value-of-information]] · [[expected-information-gain]]

[^c1]: arxiv-2604-17405 — "they often perform entity-centric decomposition too early, before establishing a task-aligned reasoning structure. This can cause cascading errors when entity names are ambiguous."
[^c2]: arxiv-2604-17405 — "Rather than decomposing the question directly into entity-bound sub-queries, it first constructs a General Strategy, which is an abstract representation of the reasoning flow that is independent of specific entity names. Only after this high-level logic is established does it instantiate a Concrete Plan of executable, entity-grounded sub-questions."
[^c3]: arxiv-2604-17405
[^c4]: arxiv-2604-17405 — "if the system first abstracts the reasoning path as [movie → source book → author], it can correctly disambiguate “Lincoln” as a film entity and avoid being misled by homonymous references."
[^c5]: arxiv-2604-17405 — "w/o Meta-Planner disables the abstract reasoning strategy by removing all General Strategy-related prompts, forcing the planner to directly output a concrete plan without high-level intent modeling. This leads to significant performance drops across all datasets (e.g., −0.197 EM on 2WikiMultihopQA with Qwen3-8B), demonstrating that abstract planning provides crucial scaffolding for robust multi-hop decomposition."
