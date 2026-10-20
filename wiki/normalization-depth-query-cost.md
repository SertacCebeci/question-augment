---
description: "Splitting a synthesized schema into more tables deepens the joins a query needs; in one study deeper joins tracked more SQL errors, so the cost is generative rather than relational."
aliases: ["balanced normalization", "over-normalization", "3NF fragmentation cost", "join depth cost"]
sources: ["doi-10-48550-arxiv-2512-00329"]
---
# Normalization depth as query cost

Normalizing a relational schema removes repeated values, but it also spreads one fact over several relations, and a query that needs the fact must join them back. In the setting studied here, an LLM is prompted for a Third Normal Form schema from Wikipedia infobox timelines. The stated rationale is that "3NF reduces redundancy across temporal snapshots by factoring" repeated information out.[^n1]

The paper's point is that splitting has a cost that is not relational. Over-normalization "is not wrong relationally", and it is "costly generatively: every additional join is another chance for the query model to err."[^n2] The mechanism, in the paper's terms, is that a query model writing SQL has to choose a join path, and each join is one more step where it can pick the wrong relation or key. My reading is that the schema is fixed per domain, so an extra fragment is paid on every question that touches it, not once.

The measurements are structural. Gemini 2.5 Flash produced the most compact schemas, at 5.5 tables per domain, "tables/domain against 7.7 for Llama-3.1-8B", with the shallowest joins, 1.089 average depth.[^n3] The paper reads excessive fragmentation and high join depth as the places where errors concentrate: the Economy domain had 18 tables under Llama-3.1-8B against 2 under Flash, and Government Agencies had join depth of 2.03 to 3.65. Both "track increased SQL" errors.[^n4]

The same join is also what the temporal task needs. The paper's account of the temporal regime is that balanced normalization helps "because it is precisely what makes snapshot joins expressible."[^n7] A uniform snapshot key lets tables that change over time be joined by equality, so a question about before and after needs at least one join across snapshots. My inference, not the paper's measurement, is that the trade-off has two sides: too few tables and a snapshot comparison cannot be written at all, too many and each join is another place to fail.

The direction of this finds a counterpart in static text-to-SQL. Kohita (2025), studying given schemas rather than synthesized ones, reports that normalized schemas "introduce challenges such as base-table selection and join-prediction errors."[^n5] The paper states that its own result is the converse, a more nuanced trade-off in which balance helps.[^n6] The two findings are about different settings, so they do not settle one another.

## Limits

The evidence is correlational. The paper says that "normalization depth, naming style, temporal anchoring, and generator identity co-vary across the schemas we compare."[^n8] Join depth is therefore one of several properties that move together with accuracy, and the error link is not isolated. The test the paper proposes, though it did not run it, is "merging or splitting relations while preserving the same" functional dependencies, which would vary normalization with the information held fixed.[^n9]

No threshold is given. The study has three generators over ten domains, and "balanced" is never defined by a number of tables or a join depth. A reader cannot tell from this work where fragmentation starts to cost accuracy.

The fragmentation metrics are intrinsic. Completeness, losslessness, referential consistency and disjointness show that the database is well formed, but "They are silent on semantic fidelity," so a schema that scores well can still map a fact to the wrong role.[^n12] The 3NF property itself is prompted and checked by hand: "We do not formally prove 3NF compliance."[^n11]

The Gemini 2.5 Pro case study is a single question. Those schemas were not run through the query grid, so "this is evidence about query complexity not a measured accuracy gap."[^n10]

## Related

- [[schema-vocabulary-retrieval]] — the generator chooses among a schema's real keys; a more fragmented schema is a larger vocabulary to choose from.
- [[schema-gated-relation-grounding]] — a gate on relation names against the schema; the join cost here is what remains once the names are right.
- [[omega-squared-factor-share]] — the variance-share reading that puts the schema ahead of the query model in this grid.

[^n1]: doi-10-48550-arxiv-2512-00329 — "3NF reduces redundancy across temporal snapshots by factoring"
[^n2]: doi-10-48550-arxiv-2512-00329 — "costly generatively: every additional join is another"
[^n3]: doi-10-48550-arxiv-2512-00329 — "tables/domain against 7.7 for Llama-3.1-8B"
[^n4]: doi-10-48550-arxiv-2512-00329 — "both track increased SQL"
[^n5]: doi-10-48550-arxiv-2512-00329 — "schemas introduce challenges such as base-table selection and join-prediction errors"
[^n6]: doi-10-48550-arxiv-2512-00329 — "balanced normalization helps, because it is precisely"
[^n7]: doi-10-48550-arxiv-2512-00329 — "what makes snapshot joins expressible"
[^n8]: doi-10-48550-arxiv-2512-00329 — "co-vary across the schemas we compare"
[^n9]: doi-10-48550-arxiv-2512-00329 — "merging or splitting relations while preserving the same"
[^n10]: doi-10-48550-arxiv-2512-00329 — "so this is evidence about query complexity, not a measured accuracy gap"
[^n11]: doi-10-48550-arxiv-2512-00329 — "We do not formally prove 3NF compliance"
[^n12]: doi-10-48550-arxiv-2512-00329 — "They are silent on semantic fidelity"
