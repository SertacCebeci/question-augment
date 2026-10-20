---
description: "Probes into a store reachable only by top-k similarity keep re-fetching the same items; choosing each next probe least similar to what was already returned raised unique coverage."
aliases: ["retrieval collisions", "collision rate", "furthest-query selection", "unique-chunk coverage", "coverage of a hidden store by probes"]
sources: ["openalex-org-w7204018931"]
---
# Retrieval collision in probing a hidden store

Some stores can be read only through a query. A query returns the few stored items nearest to it in embedding space, and nothing else. Anyone who wants most of the store then faces a coverage problem. Two probes that are close in meaning return overlapping items, so the second adds little. The thesis states the difficulty in these terms: "The difficulty is in finding queries that are diverse enough from each other such that an attacker can increase the coverage of the database leakage over time."[^c1] The failure has a name there: a retrieval collision, the case where "the same data chunks are repeatedly fetched."[^c2]

The mechanism proposed against collisions is a selection rule that uses what has already come back. A pool of candidate probes is kept, and an embedding store holds the retrieved items seen so far. At each step the next probe is the candidate "whose embedding exhibits the lowest cosine similarity to those in Ec"[^c3], that is, the one least like the returned set. The embedding store "stores the embeddings of all previously retrieved data throughout" the process.[^c4] The rule needs no model of what the store contains, which matters because the attacker "does not know the contents of the database they are trying to extract."[^c5] Its only input is the feedback of the probes themselves.

What was measured. With 100 queries and top-k set to 3, the thesis reports that selection "reduces retrieval collisions compared to random queries," with "273 and 256 unique chunks retrieved" for two of its databases.[^c6][^c7] Out of 300 chunks returned in total, that is the count of distinct items; the random-query figures for the same budget sit in a table that the slice read here does not include, so the size of the gain is not restated in this note.

## Limits

- The gain flattens as the store fills. On the smaller store the thesis says "the collision rate increases after a significant portion of the database is retrieved."[^c8] The read text gives no full saturation curve, only the figure that plots unique chunks against query count.
- The comparison is with random probes. The figure caption also names a "furthest" rule, so at least one alternative is tested. The work does not show that the cosine-minimising rule beats other diversity schemes; the claim is only that it beats random selection.
- The authors' own account of the effect is a hypothesis: "of the query pool itself plays a pivotal role" in the strategy's effectiveness.[^c9] The pool in the experiments was small, "only 10,000 randomly sampled text samples,"[^c10] and a larger or curated pool was not tested in the read text.
- The setting is an attack on embedding-based RAG pipelines with top-k retrieval. Whether the same selection helps when the store answers a person or a model, or when the probe is a question rather than a retrieval query, is not tested here.
- The adversarial-string half of the thesis (an optimised suffix that forces verbatim output, with a perplexity-constrained loss) is a method for extraction. It is not carried into this note; only the coverage concept is.

My inference, not the work's: an asker who probes an unknown source with questions whose answers keep landing on the same items faces the same collision. Choosing the next question by its distance from answers already in hand would be the question-side form of the rule. The work does not test that transfer.

## Related

- [[ball-coverage-acquisition]] — greedy coverage under a label-free geometric proxy; there the pool geometry is fixed up front, while here the coverage is built from feedback as probes return.
- [[set-level-diversity-floor]] — a diversity constraint held on a generated set of prompts; the same goal, enforced at selection over the whole set rather than one probe at a time against what has been returned.
- [[positive-first-most-ambiguous-selection]] — coverage counted as the fraction of clusters reached by retrieved positives, a count that also ignores redundancy among hits.
- [[questioning-diversity]] — pairwise distinctness measured on a finished question set, not on a sequence of probes.

[^c1]: openalex-org-w7204018931 — "The difficulty is in finding queries that are diverse"
[^c2]: openalex-org-w7204018931 — "cause retrieval collisions where the same data chunks are repeatedly fetched"
[^c3]: openalex-org-w7204018931 — "query q whose embedding exhibits the lowest cosine similarity to those in Ec"
[^c4]: openalex-org-w7204018931 — "stores the embeddings of all previously retrieved data throughout"
[^c5]: openalex-org-w7204018931 — "the attacker does not know the contents of the database they are trying to"
[^c6]: openalex-org-w7204018931 — "Our query selection strategy reduces retrieval collisions compared to random queries"
[^c7]: openalex-org-w7204018931 — "256 unique chunks retrieved for WK and HM, respectively"
[^c8]: openalex-org-w7204018931 — "the collision rate increases after a significant portion of the database is retrieved"
[^c9]: openalex-org-w7204018931 — "of the query pool itself plays a pivotal role"
[^c10]: openalex-org-w7204018931 — "the query pool comprises only 10,000 randomly sampled text samples"
