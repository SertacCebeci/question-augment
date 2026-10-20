---
description: "Formalizes ambiguity as ≥2 non-equivalent valid SQL readings of a question and unanswerability as zero, then splits eleven problematic subcategories, three new to knowledge-augmented systems."
aliases: ["ABISS taxonomy", "unified taxonomy for knowledge-augmented text-to-SQL systems", "knowledge-augmented ambiguity taxonomy"]
sources: ["sullutrone-2026"]
---
# Text-to-SQL ambiguity taxonomy

> Which axis is unresolved is defined by counting how many non-equivalent SQL
> readings a question still admits — the query-mapping function makes $|W|$
> countable for one task instead of asserted.

## Definition / Mechanism

Sullutrone et al. (2026) define a deterministic mapping
function $f(q, D, K)$ from a natural-language question $q$, database $D$ and
external-knowledge set $K$ to the subset of all non-equivalent valid SQL
queries on $D$ that correctly answer $q$: "The function 𝑓 (𝑞, 𝐷, 𝐾) returns
the set of queries in S that correctly answer 𝑞 on D, given the
disambiguating information in K." A question is ambiguous when
$|f(q,D,K)| \geq 2$ and unanswerable when $f(q,D,K) = \emptyset$.[^c1]

On this base, eight top-level categories split into eleven problematic
subcategories: three [[efe-planning-as-variational-inference|ambiguity]] classes native to the text (structural —
scope and attachment; semantic-mapping — lexical overlap and entity
ambiguity; lexical vagueness), three unanswerability classes from the
schema or domain (missing schema elements, missing external knowledge,
improper question), and two categories the paper adds for
knowledge-augmented systems — Missing User Knowledge (the question is
answerable only once the user supplies a user-specific fact, e.g. "my
department") and Conflicting Knowledge (the knowledge base itself holds two
non-equivalent facts for the same term). "In total, the taxonomy yields
eleven problematic subcategories. Together with two answerable subcategories
… this produces the thirteen subcategories used in the generation pipeline
… and benchmark evaluation."[^c2]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Text-to-SQL benchmarking (this paper) | ABISS taxonomy / unified taxonomy for knowledge-augmented text-to-SQL systems | exact |
| Not this concept | **ambiguity taxonomy** ([[ambiguity-taxonomy]], Berry et al./CLAMBER) | close, not exact — that taxonomy classifies linguistic and missing-element ambiguity generically; this one is text-to-SQL-specific, formalized by query-set cardinality, and adds knowledge-augmentation categories (Missing User Knowledge, Conflicting Knowledge) absent there |

## Why it matters

For stall 2, a system cannot choose which axis to ask about before it can
name the axis at all. This taxonomy gives text-to-SQL a countable,
falsifiable criterion for "which axis is open" — the size of the surviving
query set — rather than a category label assigned by inspection; the two
new categories exist because prior taxonomies did not account for
user-specific or knowledge-base-internal sources of the same underdetermination (see Limits).

## Transfer

| | |
|---|---|
| In its home field | Query equivalence — whether two SQL queries produce the same result on every database state — is a formal-semantics notion from database theory, used here to decide when two candidate readings of a question are the *same* answer versus different ones. |
| Here | The cardinality $\lvert f(q,D,K)\rvert$ stands in for $\lvert W\rvert$ restricted to one task: counting surviving readings makes ambiguity a number instead of a judgment call. |
| What survives | The counting criterion itself — more than one non-equivalent reading means the axis is still open — generalizes to any task with a checkable notion of "same answer." |
| What does not | The equivalence check is SQL-specific (results agree on every database state); a task without an executable, checkable output (open-ended NL generation) has no analogous procedure for deciding when two candidate readings collapse to one. |

## Limits

This note's claim that the taxonomy names axes rests on the paper's own
category-conformance validation (a council of LLMs majority-voting that a
generated question "genuinely exhibits" its assigned category) rather than
on human-annotated ground truth for every item; the taxonomy's coverage
claim (that it closes the gaps prior schemes left) is the authors' own
comparison against related taxonomies, not an independent audit.[^c3]

## Related

[[ambiguity-taxonomy]] · [[clarification-benchmarks]] · [[possible-worlds]] · [[black-box-correctness-ceiling]]

[^c1]: sullutrone-2026 — "The function 𝑓 (𝑞, 𝐷, 𝐾) returns the set of queries in S that correctly answer 𝑞 on D, given the disambiguating information in K."
[^c2]: sullutrone-2026 — "In total, the taxonomy yields eleven problematic subcategories. Together with two answerable subcategories (with and without external evidence), this produces the thirteen subcategories used in the generation pipeline (Section 4) and benchmark evaluation (Section 5)."
[^c3]: sullutrone-2026
