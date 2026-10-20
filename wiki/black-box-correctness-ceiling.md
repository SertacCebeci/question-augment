---
description: "Three self-consistency variants, schema relevance, executability, and log-probability all rank text-to-SQL correctness within the same narrow 0.61-0.68 AUROC band."
aliases: ["black-box correctness ceiling", "self-consistency AUROC ceiling"]
sources: ["richardson-2026"]
---
# Black-box correctness ceiling (text-to-SQL)

> Every agreement-style signal for "is this generated SQL query correct" —
> however it is computed — lands in the same narrow band; the ceiling is on
> the *family* of signals, not on any one implementation.

## Definition / Mechanism

Richardson (2026) scores six signals for ranking correct
text-to-SQL queries above incorrect ones (AUROC) on hard multi-table BIRD and
Spider benchmarks: string, structural and execution self-consistency (three
ways of clustering repeated samples for the same question), a schema-relevance
score (embedding similarity between the question and the tables/columns
used), query executability, and the model's own sequence log-probability.
"the black-box statistical signals such as string, structural, and execution
self-consistency, a schema-relevance score, and query executability all fall
between about 0.61 and 0.68 auroc, with string self-consistency the strongest
at 0.675. White-box log-probability is similar (0.67)."[^c1]

The ceiling holds despite the signals measuring unrelated properties of the
output — repeated-sample agreement, embedding overlap with the schema, and
whether the query merely runs — which the paper reads as evidence the
band is a property of *statistics computed without inspecting the query's
logic*, not of any particular statistic. Log-probability, tested against the
strongest black-box baseline directly, shows no significant difference:
"−0.006 [−0.028, +0.017] (n.s.)" against string self-consistency.[^c2]

## Why it matters

On stall 2, self-consistency is the default signal an asking/answering
system reaches for to decide whether the current answer needs more probing.
This result says re-weighting or combining *within* that family (which
clustering method, whether to add schema relevance or executability) cannot
move a selection policy's discrimination past roughly 0.68 AUROC on this
task; the ceiling is crossed only by a signal that inspects the candidate's
logic (see [[cross-provider-judge-ensemble]]), not by refining agreement
statistics.

## Limits

Measured on one task family (SQL generation with an executable ground
truth) across two generators and two benchmarks; whether the same ceiling
holds for open-ended natural-language generation, where there is no
execution oracle to define "correct," is untested.[^c3]

## Related

[[abstention]] · [[cross-provider-judge-ensemble]] · [[verifier-cross-schema-transfer-gap]] · [[calibration]]

[^c1]: richardson-2026 — "the black-box statistical signals such as string, structural, and execution self-consistency, a schema-relevance score, and query executability all fall between about 0.61 and 0.68 auroc, with string self-consistency the strongest at 0.675. White-box log-probability is similar (0.67)."
[^c2]: richardson-2026 — "−0.006 [−0.028, +0.017] (n.s.)"
[^c3]: richardson-2026
