---
description: "A tabular-QA pipeline runs a separate detector per SQL clause (intent, scope, condition), each gating its own single-round clarification only when its check fails."
aliases: ["MAIC-TQA clarification pipeline", "stage-gated underspecification clarification"]
sources: ["arxiv-2604-10159"]
---
# SQL-clause-gated clarification

> Which clause of the query is still open decides which agent asks, when it
> asks, and what it asks about — the pipeline stage *is* the question type.

## Definition / Mechanism

the ODUTQA-MDC paper (2026)'s MAIC-TQA runs a fixed
sequence of stages, each aligned to one SQL clause, and each with its own
detector that gates its own clarification request: "we categorize
underspecifications by their correspondence with SQL structures: table-scope
underspecification (impacting the FROM clause...), query-intent
underspecification (impacting the SELECT clause...), query-condition
underspecification (affecting the WHERE clause...)."[^c1]

At the SELECT/intent stage, a BERT classifier's output either passes or
triggers a fixed template question; the reply is concatenated to the query
and reclassified once, never more: "the clarification loop is restricted to
a single iteration." At the FROM/scope stage, a Scope Validator Agent
checks required slots against a domain schema and, on a missing or invalid
slot, emits a typed triplet naming exactly what is missing before asking —
"if the 'District' slot is absent, the output triplet would be ('',
'District', 'Missing')." At the WHERE/condition stage the SQL Generation
and Validation Agent only asks after executing a first SQL query: an empty
or partial result triggers a validation function that names the missing
condition, generates a condition-underspecification label, and requests one
more clarification before a single regeneration attempt: "the agent calls a
predefined SQL validation function to identify missing conditions, generates
a condition underspecification label, and requests clarification from the
user."[^c4]

Each detector-clarify pair is independently ablatable, and the three do not
matter equally. Removing the intent (SELECT) mechanism costs the least;
removing the scope (FROM) mechanism costs execution-completion rate (ECR)
the most (−16.92 / −15.31 points across two backbones); removing the
condition (WHERE) mechanism costs execution accuracy (EA) the most (−28.59 /
−27.29 points): "removing the scope clarification mechanism most severely
affects the ECR metric... removing the condition clarification mechanism has
the most pronounced impact on the EA metric."[^c5]

## Why it matters

For *what* an agent asks and *when*, this gives a concrete alternative to a
single generic "ask a clarifying question" call: one detector per output
slot the final query depends on (which table, which columns, which filter
values), each firing only on its own failure signature (a classifier
disagreement, a missing/invalid schema slot, an empty execution result), so
the question a user sees always names one concrete, checkable gap rather
than a vague restatement. The ablation turns "which kind of asking matters
most" into a measured, clause-by-clause answer instead of an aggregate
clarification-vs-no-clarification number.

## Limits

The staging is fixed and sequential (SELECT before FROM before WHERE); a
query underspecified on more than one clause at once is resolved one clause
at a time, in that order, never jointly. Each clarification loop is capped
at one round by design, so a slot still unresolved after one reply is not
retried. The clarification text itself is compared only in two modes —
fixed templates and one LLM (Qwen2.5-72B) rewriting canonical facts under a
built-in entity-preservation constraint — so the ablation's cost estimates
are tied to this domain (property/land/finance tables) and to a paraphrase
generator whose factual content is guaranteed correct by construction, not
to open-ended user answers that could themselves be wrong or off-topic.

## Related

[[text-to-sql-ambiguity-taxonomy]] · [[ambiguity-driven-execution-probing]] · [[tiered-demand-detection-gate]] · [[clarification-request]]

[^c1]: arxiv-2604-10159 — "table-scope underspecification (impacting the FROM clause; see Figure 1-Q3), query-intent underspecification (affecting the SELECT clause; see Figure 1-Q2), query-condition underspecification (affecting the WHERE clause; see Figure 1-Q4), and mixed underspecification."
[^c4]: arxiv-2604-10159 — "the agent calls a predefined SQL validation function to identify missing conditions, generates a condition underspecification label, and requests clarification from the user."
[^c5]: arxiv-2604-10159 — "removing the scope clarification mechanism most severely affects the ECR metric, leading to a significant drop of 16.92% for Qwen3 32B and 15.31% for Qwen3 30B A3B. Meanwhile, removing the condition clarification mechanism has the most pronounced impact on the EA metric, causing it to fall by 28.59% and 27.29% for the two models."
