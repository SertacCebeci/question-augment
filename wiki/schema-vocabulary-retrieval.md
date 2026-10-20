---
description: "Retrieving the valid schema vocabulary for a request and putting it in front of the generator, so the formulation chooses among real keys and values instead of recalling them."
aliases: ["Tag Retrieval Augmentation", "TRA", "schema-vocabulary retrieval augmentation", "tag knowledge-base retrieval"]
sources: ["arxiv-2512-04738", "arxiv-2511-18405"]
---
# Schema vocabulary retrieval before formulation

A request in ordinary language has to be turned into a query whose names are fixed by a schema: keys, values, relation labels. The asker may not know those names. The OsmT authors state the problem for OpenStreetMap, where "identifying the appropriate tag keys and values from natural language input is" often "non-trivial" for users without domain expertise.[^o1] Their example is a request for beekeeper workplaces. Models map "Beekeeper" to the key workplace, "which is not valid in the OSM schema"; the valid tag is craft=beekeeper.[^o2]

The mechanism is a retrieval step before generation. A knowledge base holds query–tag pairs. The request is embedded, the nearest stored entries are found by cosine similarity, and their tags are pooled into a candidate set. A language model then refines that set against the request, and the result is filtered against the list of valid tags, "ensuring syntactic correctness."[^o3] The generator receives the request together with the surviving tags, so the formulation is a choice among items that exist in the schema rather than a recall of them.

Two parts of the knowledge base matter for what the mechanism can do. The pairs come partly from the training queries, parsed into their tags. Tags that are rare or unseen in that data are covered by pseudo-queries: for each valid tag, a language model writes a description from a few examples, and "apply a pre-trained language model (PLM) to generate a" such entry is what gets stored.[^o4] So the index covers the whole valid set, and part of its text is generated rather than observed.

The effect is reported as an ablation on the paper's own model. Removing TRA gives "a significant decline in KVS and OQS scores," where KVS scores the key–value structures and OQS is the paper's overall query score.[^o5] Replacing the retrieved tags with ground-truth tags is an upper bound, "suggesting additional gains are achievable through improved tag retrieval."[^o6] On the retriever itself the paper finds a trade-off rather than a winner: "sBERT yields slightly higher" exact match at larger k, while the contrastively tuned variant gives steadier F1, and the latter is the one adopted.[^o7] On two other geographic query benchmarks, GeoQuery and NLmaps v2, the paper reports that "explicit linking strategies consistently" improve performance, using a schema-linking variant of the same idea.[^o8]

A variant with no retrieval step appears in a tabular-analysis agent. Talk2Data parses the uploaded table into a compact context, "we parse a lightweight schema and exemplars: column names and inferred types", with a few sample rows, numeric ranges and representative categorical values, and injects it into every prompt that decides or generates a turn.[^o10] The stated invariant is that "only facts derived from the uploaded data (schema, ranges, exemplars) are injected".[^o11] When the whole valid vocabulary fits in the prompt, the candidate set is the table itself and no filter against an external list is needed. That last step is my inference from the mechanism; the paper does not compare this against retrieval, and it names retrieval-augmented prompting as future work.[^o12]

## Limits

- The size of the TRA effect is in an ablation table that the read text does not reproduce, so the magnitude here rests on the word "significant" in the paper's prose. The text read gives no significance test.
- The result is for one schema and one benchmark family, OverpassNL. The GeoQuery and NLmaps results use a different variant ("a schema-linking variant of TRA"), so they do not show the same mechanism transfers unchanged.
- Part of the gain for the paper's model comes from pretraining on tag-related corpora. The authors contrast this with other LLMs, which get TRA "only at inference time"; the read text does not separate the two contributions for the same model.[^o9]
- The score is agreement with gold queries. Whether a user who gets the candidate tags asks or understands better is not measured; the paper measures the generated query, not the person.
- The filter needs an enumerable set of valid items to check against. OSM supplies one. Where the valid vocabulary cannot be listed, the filter has nothing to test against. This is my inference from the mechanism, not something the paper tests.
- Synthetic pseudo-queries are part of the index. Whether they pull retrieval toward the generator's own phrasing is not tested in the text read.

## Related

- [[schema-gated-relation-grounding]] — the same schema enters after the proposal, as a gate that scores a named relation; here it enters before generation, as candidates in the prompt.
- [[candidate-constrained-entity-identification]] — choosing from a short candidate list raises naming accuracy in a different setting (knowledge-base visual QA); the same move of offering candidates.
- [[stepwise-validated-logical-form]] — checks during the build come from an executor's feedback; the check here is a static filter against the valid set.

[^o1]: arxiv-2512-04738 — "identifying the appropriate tag keys and values from natural language input is"
[^o2]: arxiv-2512-04738 — "which is not valid in the OSM schema"
[^o3]: arxiv-2512-04738 — "ensuring syntactic correctness"
[^o4]: arxiv-2512-04738 — "apply a pre-trained language model (PLM) to generate a"
[^o5]: arxiv-2512-04738 — "a significant decline in KVS and OQS scores"
[^o6]: arxiv-2512-04738 — "suggesting additional gains are achievable through improved tag retrieval"
[^o7]: arxiv-2512-04738 — "sBERT yields slightly higher"
[^o8]: arxiv-2512-04738 — "explicit linking strategies consistently"
[^o9]: arxiv-2512-04738 — "apply TRA only at inference time"
[^o10]: arxiv-2511-18405 — "we parse a lightweight schema and exemplars: column names and inferred types"
[^o11]: arxiv-2511-18405 — "only facts derived from the uploaded data (schema, ranges, exemplars) are injected"
[^o12]: arxiv-2511-18405 — "Extending to schema repair and retrieval-augmented prompting is future work."
