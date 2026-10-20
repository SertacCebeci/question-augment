---
description: "A functional dependency restricted to a constant pattern, so the same attributes determine different targets in different contexts; a violation is the inconsistency a repair removes."
aliases: ["CFD", "conditional inclusion dependency", "CIND"]
sources: ["fan-2008"]
---
# Conditional functional dependency

> A classical functional dependency is one global rule or none. A CFD is a
> tableau of them, each bound to a pattern of constants — so "zip determines
> street" can hold for UK customers and fail everywhere else, and a
> violation of the local rule is still a global inconsistency.

## Definition / Mechanism

A functional dependency (fd) $X \to Y$ is required to hold on every tuple of
a relation. Fan, Geerts & Jia (2008) pair an fd with a
*pattern tableau*: a set of constants that restricts which tuples the fd
must hold on, and can also fix the value $Y$ takes. `customer([cc = 44, zip]
→ [street])` asserts that for UK customers zip determines street; it is not
an ordinary fd, because it is anchored to constants and is not required to
hold on the whole table.[^c1]

`customer([cc = 01, ac = 908, phn] → [street, city = 'mh', zip])` goes
further: for two US customers who share an area code and phone number, it
forces `street` and `zip` to agree *and* pins `city` to the constant `mh`.
Because the same source attributes (`cc`, `zip`) can be given different
targets under different patterns, a cfd set distinguishes local, context-
bound errors that a single global fd is powerless to state — either too
strong (false somewhere) or silent everywhere it is not. A **conditional
inclusion dependency (cind)** extends an inclusion dependency the same way:
`CD(album, price, genre = 'a-book') ⊆ book(title, price, format = 'audio')`
holds only for the audio-book pattern, not for every CD tuple.

A database is **inconsistent** with respect to a cfd/cind set exactly when
some tuple(s) violate one of its pattern-bound rules; detecting inconsistency
is checking these violations, not full fd satisfaction. **Repairing** is
finding another database instance that satisfies the constraint set and
minimally differs from the original — the distance is over edits to values,
not over sentences dropped from a theory.[^c2]

This is implemented, not only proposed: the Semandaq prototype specifies
cfds, detects violations with SQL-based queries, and computes a candidate
repair the user can inspect and further edit by hand.[^c3]

## Why it matters

Making the fd's scope part of the constraint, rather than assuming it holds
everywhere, is what lets a formalism built for schema design double as an
error detector for data: the same declarative language that used to police
which schemas are well-formed now says which *rows* are wrong, and where the
repair has to look. Because the rule is declarative, both detection and
repair can be automated instead of coded ad hoc per data source.

## Limits

This tutorial only sketches the formalism; the complexity of finding a cfd
violation and of computing a minimal repair, and the completeness proofs,
live in the cited TODS and ICDE papers, not in this extract [?]. A cfd set
is still hand-specified: a wrong or missing pattern silently mis-detects or
under-detects errors, and the tutorial itself lists the interaction between
error correction and object identification, repair at master-data scale
with precision/recall guarantees, incremental repair, and xml data as open.
The general repair definition (minimal edit distance to a consistent
instance) is attributed here to prior work (Arenas, Bertossi & Chomicki
1999), not established by this source.

## Related

[[agm-belief-revision]] — a different field's version of "change minimally
to restore consistency", over sentences dropped from a belief set rather
than values edited in a database. [[truth-maintenance-system]],
[[np-completeness]] — satisfiability of a constraint set is the
harder-general case a cfd violation check is a tractable special case of.
[[batched-oracle-entity-resolution]] — the same tutorial's other half, using
constraints to derive matching keys for object identification.

[^c1]: fan-2008 — "It is not a traditional fd since it is defined with constants and is not required to hold on the entire data set."
[^c2]: fan-2008 — "repairing is to find another database that is consistent and minimally differs from the original database"
[^c3]: fan-2008 — "Semandaq supports (a) specifications of cfds, (b) automatic detections of cfd violations, based on efficient sql-based techniques [8, 4], and (c) repairing, i.e., given a set of cfds and a dirty database, it finds a candidate repair that minimally differs from the original data and satisfies the cfds [6]."
