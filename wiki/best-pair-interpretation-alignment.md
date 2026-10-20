---
description: "Scoring a model's set of readings of an ambiguous question by the best generated-gold pair on schema and constraint features, since exact query match is near zero though readings are valid."
aliases: ["interpretation alignment", "ambiguity-aware matching", "best-aligned pair scoring"]
sources: ["doi-10-48550-arxiv-2609-36082"]
---
# Best-pair interpretation alignment

When a question admits several valid formal readings, comparing one generated query to one gold query punishes legitimate variation. GeoOutageBench (a benchmark of ambiguous geospatiotemporal questions mapped to SPARQL) instead scores a set of generated readings against a set of gold readings.

## Mechanism

Each question has at most three valid reference SPARQL interpretations (72 across 48 evaluation questions). For every generated-gold pair, the evaluator extracts class, property, spatial-constraint and temporal-constraint feature sets, computes F1 on each, and keeps the maximum average score over all pairs for that question.[^c1] The score therefore asks whether a generated reading keeps the ontology grounding and the spatiotemporal constraints of some gold reading. It does not ask whether the syntax matches.[^c2]

The reason is measured. Three frontier LLMs all produced syntactically valid queries, yet exact query-text match was near zero, because valid readings differ in variable names, projections, join order, filters, or which reading of the ambiguity was chosen.[^c3] Alignment separated the models (0.805, 0.749 and 0.745) where exact match could not.[^c4]

The set size is a second diagnostic. The generated interpretation counts differed (51, 60 and 61 against 72 references). The authors read fewer readings as lower downstream execution cost and more readings as wider coverage of alternatives.[^c5] An appendix also defines ambiguity-aware matching that compares the full interpretation sets, not only the first reading.[^c6]

## Why it matters

A system that is asked an ambiguous question and answers by committing to one reading, or by listing several, can only be judged fairly if the metric accepts any valid reading. Best-pair matching makes "same meaning, different surface" count as correct. It also leaves set size as a separate, visible tradeoff between coverage and cost.

## Limits

Taking the maximum over pairs credits a model that gets one reading right even if its other readings are wrong. The note does not establish that the max rewards calibrated enumeration. The reference sets hold at most three readings, so recall of additional valid readings is unmeasured. Gold readings are authored by the benchmark's builders, so completeness is assumed. My reading that the max-pair rule is lenient to spurious extra readings is an inference, not a result of the paper. Only three models and one domain (power outage, storm events) were tested. The paper does not test whether asking a clarifying question would beat enumerating readings.

## Related

- [[interpretation-space]] — the same idea of a set of readings, scored there by answer coverage rather than best-pair match
- [[text-to-sql-ambiguity-taxonomy]] — defines ambiguity as two or more non-equivalent valid queries, the condition this metric assumes
- [[ambiguity-taxonomy]] — kinds of ambiguity that produce the multiple readings

[^c1]: doi-10-48550-arxiv-2609-36082 — "class, property, spatial-constraint, and temporal-constraint feature"
[^c2]: doi-10-48550-arxiv-2609-36082 — "than whether its syntax exactly matches a gold counterpart."
[^c3]: doi-10-48550-arxiv-2609-36082 — "Exact query-text match is near zero,"
[^c4]: doi-10-48550-arxiv-2609-36082 — "Claude Opus 4.7 obtains the highest alignment"
[^c5]: doi-10-48550-arxiv-2609-36082 — "Gemini 3.1 Pro generated the fewest"
[^c6]: doi-10-48550-arxiv-2609-36082 — "set, while ambiguity-aware matching compares the full interpretation sets:"
