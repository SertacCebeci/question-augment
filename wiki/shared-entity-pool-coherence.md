---
description: "Drawing every document type's people and places from one shared entity pool, with the relations stored first, makes cross-document questions answerable; independent random generation cannot."
aliases: ["coherent simulated universe", "global entity pool", "shared entity pool"]
sources: ["arxiv-2601-08847"]
---
# Shared entity pool coherence

Generating documents one at a time, each with its own random draws, yields a corpus with no internal relations. The paper calls this naive generation: "One of the significant shortcomings of synthetic generated data comes from naive generation".[^c1] Independently generated HR evaluations draw their names and managers at random, so the same person may be a manager in one document and a junior in another, and the department named in one file may not match the manager named in another.

This is not cosmetic. Aggregation questions need the relations to exist. Naive generation "will prevent the creation of challenging comprehension and aggregation questions", because "necessary relationships will either not be diverse or coherent enough, or may not even exist at all".[^c2]

The mechanism is ordering. The relations are created before any document is rendered, by drawing from shared pools: "then created by drawing from the global entity pools, which are saved in the ground truth database".[^c3] One pool serves several document types: "all the three document types above (in bold) draw from the same Global Entity" pool. The agent who closes a lease is therefore the agent who files a field report about it and the employee evaluated in the HR file.[^c4] The generator also enforces consistency inside the text: "It will also never happen that a Field Report talking about a particular Lease Contract" names a different sales agent from the one on the contract.[^c5] The result is coherent by design, "coherent according to the generation design".[^c6] The evaluation reports this in its corpora: "the same entities (people, properties, companies)" recur across leases, field reports and HR evaluations.[^c7]

For asking, the consequence is that a question such as how many leases one lessor holds has an answer only if the lessor's leases share an entity across documents. The taxonomy's aggregation tier, which the paper says requires the model to identify all relevant documents first, depends on that shared entity; this link is my inference from the design, not a claim the paper makes in those words.[^c8]

## Limits

The coherence is defined by the generator and is not checked against real enterprise data. The paper's own statement is that the approach "maintains entity consistency across documents" while the synthetic set may still lack real characteristics; see [[ground-truth-first-corpus-generation]] for the wider validity limits.[^c9]

In the passages read, the contrast between naive and coherent generation is argued, not measured. No table in what was read compares the two generators on the same models, so the size of the effect on scores is unknown.

The design covers three document types in one domain. The paper lists "Expanding beyond the current three document types" as future work.[^c10] Whether shared pools stay tractable with richer schemas, more entity types or longer relation chains is not tested; that is my inference.

## Related

- [[ground-truth-first-corpus-generation]] — the pool fills the database from which the documents are rendered.
- [[aggregation-extraction-gap]] — the difficulty these coherent relations are built to expose.
- [[dispersed-evidence-retrieval-collapse]] — the retrieval-side version of aggregation over evidence scattered through a corpus.

[^c1]: arxiv-2601-08847 — "One of the significant shortcomings of synthetic generated data comes from naive generation"
[^c2]: arxiv-2601-08847 — "will prevent the creation of challenging comprehension and aggregation questions"
[^c3]: arxiv-2601-08847 — "then created by drawing from the global entity pools, which are saved in the ground truth database"
[^c4]: arxiv-2601-08847 — "all the three document types above (in bold) draw from the same Global Entity"
[^c5]: arxiv-2601-08847 — "It will also never happen that a Field Report talking about a particular Lease Contract"
[^c6]: arxiv-2601-08847 — "are coherent according to the generation design"
[^c7]: arxiv-2601-08847 — "the same entities (people, properties, companies)"
[^c8]: arxiv-2601-08847 — "Aggregation questions are particularly challenging because they require the model to"
[^c9]: arxiv-2601-08847 — "maintains entity consistency across documents"
[^c10]: arxiv-2601-08847 — "Expanding beyond the current three document types"
