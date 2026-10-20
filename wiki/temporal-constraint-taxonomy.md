---
description: "A taxonomy of 26 pairwise temporal relations plus 3 ordinal operators, built by fusing Allen's interval algebra with point algebra, that enumerates how a fact's timestamp can constrain another fact's."
aliases: ["ChronoQG temporal taxonomy", "temporal-constraint taxonomy"]
sources: ["liu-2026-chronoqg"]
---
# Temporal-constraint taxonomy

> Which time relation can a question use to narrow the answer, when facts
> may be dated to a point or to an interval — enumerated once instead of
> being invented ad hoc per benchmark.

## Definition / Mechanism

"ChronoQG therefore introduces a comprehensive taxonomy of temporal
constraints by integrating Allen's interval algebra with point algebra."[^c1]

The taxonomy sorts every pairwise constraint by the temporal type of the
two facts it relates — interval–interval (Allen's 13 relations), point–
interval, interval–point, and point–point — plus a fifth, non-pairwise
family for ranking a candidate set:

"Pairwise constraints cannot express questions that require identifying the
earliest, latest, or 𝑘-th fact satisfying a temporal condition. To support
such cases, ChronoQG further introduces three ordinal operators:
start_rank, end_rank, and duration_rank."[^c2]

"Overall, the taxonomy contains 26 pairwise temporal relations and 3
ordinal operators."[^c3]

## Why it matters

A generator or a selector that only has *before / after / during* cannot
express that two memberships overlapped, or that one fact must be ranked
first among several — it can only ask questions whose temporal axis is
coarser than the graph actually supports. The taxonomy is the operator
space [[chronoqg]] samples from when it picks the next temporal filter to
apply to a candidate set.

## Transfer

| | |
|---|---|
| **In its home field** | Allen's interval algebra: 13 relations between two intervals, closed under composition, used for constraint-propagation reasoning about which combinations of relations are jointly satisfiable. |
| **Here** | A flat catalogue of relation *names*, partitioned by whether each side of a fact is point- or interval-valued, used to label which filter a sampling step may apply next. |
| **What survives** | The 13 interval–interval relation names and their pairwise-exhaustive, mutually-exclusive structure; the point-algebra's before/equal/after. |
| **What does not** | Allen's composition table and the constraint-propagation machinery for checking joint satisfiability of a set of relations — ChronoQG never checks whether an accepted combination of temporal filters is itself consistent beyond the direct candidate-narrowing test. |

## Limits

The taxonomy is exhaustive only for facts with well-defined point or
interval timestamps; relations "marked as Deleted are either semantically
ambiguous or associated with facts that mix point and interval timestamps"
are excluded from sampling rather than classified, so the taxonomy is
silent on mixed or ambiguous temporal facts.

## Related

[[chronoqg]] · [[tkgqg-constraint-count-degradation]] · [[constraint-as-information]]

[^c1]: liu-2026-chronoqg
[^c2]: liu-2026-chronoqg — "Pairwise constraints cannot express questions that require identifying the earliest, latest, or 𝑘-th fact satisfying a temporal condition. To support such cases, ChronoQG further introduces three ordinal operators: start_rank, end_rank, and duration_rank."
[^c3]: liu-2026-chronoqg — "Overall, the taxonomy contains 26 pairwise temporal relations and 3 ordinal operators."
