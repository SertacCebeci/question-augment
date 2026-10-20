---
description: "Extracted triplets are checked against an external ontology's entity types and domain-range rules and flagged, not dropped, when they fail; removing the check lowered multi-hop QA scores."
aliases: ["ontology-aware triplet refinement", "schema-constrained open information extraction", "Wikidata-aligned extraction", "domain-range validation"]
sources: ["arxiv-2512-00590"]
---
# Ontology-constrained triplet validation

Open extraction from text lets a model choose its own relation names, so the same fact can come out under several predicates and the output cannot be checked against anything. Closed extraction fixes the vocabulary in advance but needs annotated corpora for every new domain. The paper keeps the open extraction and adds a check against an external ontology. Each candidate triplet carries entity types for its subject and object, and the check asks whether the relation is defined for those types. The rule is stated directly: "A triplet is verified if (i) its subject and object types, together with the relation, are defined"[^o1] in the ontology, and the relation's domain and range constraints must also hold.

The check is a flag, not a filter. "Triplets that fail these checks are flagged as ontology-misaligned," and they are "but retained, as they remain linked to the main" graph through the later name-refinement step.[^o1] The paper gives the reason: "Preserving them enables computation of an ontology alignment score and provides interpretable cues for identifying or revising schema-inconsistent facts."[^o1] In the reported run, "only 3.5% of extracted triplets are flagged as" misaligned.[^o2]

The mechanism is measured by ablation. On MuSiQue, with gpt-4.1-mini, removing the ontology stage lowers both exact match and F1 (Table 6). The paper's reading is that the result shows "the importance of type and schema constraints for consistent" graph construction.[^o3] Removing the ontology and the entity normalization together lowers exact match from 42.6 to 27.0.[^o2] The table caption says that removing "ontology or entity normalization" "yields the largest drop, highlighting their importance for" reasoning over the graph.[^o4] That claim does not match the table's own rows: removing qualifiers gives the lowest single score, 23.9 exact match (see [[triplet-qualifiers]]).

What survives the transfer from Wikidata is the form of the check: a type signature and a domain-range rule, applied to every candidate. What does not survive is any claim about truth. A triplet can satisfy every signature and still be false. The paper's authors say the pipeline "can operate without an ontology or integrate domain-specific ontologies," so the check is not tied to Wikidata in the method, though only Wikidata was tested.[^o5]

The authors set this against prior work that uses the Wikidata ontology only for evaluation or entity linking. They "integrate a large-scale ontology from Wikidata directly into the" extraction stage, which is the difference the note turns on.[^o6]

## Limits

- A schema-valid triplet is not a verified one. The paper reports no precision against gold triplets. It says MINE-style evaluation "cannot measure classical precision or recall,"[^o7] and it treats multi-hop QA as "a functional proxy for two key properties of an" extracted graph.[^o8]
- Only Wikidata was used: "we focus only on Wikidata" in the current work.[^o9] Whether a smaller or domain ontology has enough types and relations to flag errors was not tested.
- The ablation is one table on one dataset with one model. The rate of ontology-misaligned triplets is reported for one run. Neither is repeated across datasets or extraction models here.
- Every stage uses LLM prompting: "Every stage of the pipeline currently uses LLMs with instructions and in-context" examples.[^o10] The check is therefore only as good as the typing the model supplies. My inference, not measured: a relation missing from the ontology would be flagged even when it is correct, and the paper does not say how often that happens.

## Related

- [[referent-name-fragmentation]] — the entity-merging step that the same ablation removes together with this check; the two are not separated in the paper.
- [[pico-typed-knowledge-graph-schema]] — another typed schema for a knowledge graph's extraction, built for clinical questions; there the typing buys alignment at a cost in coverage.
- [[triplet-qualifiers]] — the other extraction component ablated in the same table; qualifiers keep context that the type-and-relation check does not see.

[^o1]: arxiv-2512-00590 — "A triplet is verified if (i) its subject and object types, together with the relation, are defined"
[^o2]: arxiv-2512-00590
[^o3]: arxiv-2512-00590 — "demonstrating the importance of type and schema constraints for consistent"
[^o4]: arxiv-2512-00590 — "yields the largest drop, highlighting their importance for"
[^o5]: arxiv-2512-00590 — "ontology or integrate domain-specific ontologies,"
[^o6]: arxiv-2512-00590 — "large-scale ontology from Wikidata directly into the"
[^o7]: arxiv-2512-00590 — "Therefore, it cannot measure classical precision or recall"
[^o8]: arxiv-2512-00590 — "QA a functional proxy for two key properties of an"
[^o9]: arxiv-2512-00590 — "we focus only on Wikidata"
[^o10]: arxiv-2512-00590 — "Every stage of the pipeline currently uses LLMs with instructions and in-context"
