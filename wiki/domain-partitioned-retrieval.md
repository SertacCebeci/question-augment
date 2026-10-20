---
description: "Split a heterogeneous corpus into one retrieval index per domain and route each query to the matching index, so structurally different documents are not ranked in one pool."
aliases: ["domain-partitioned RAG", "per-domain retrieval modules", "partitioned vector collections"]
sources: ["arxiv-2602-23371", "doi-10-48550-arxiv-2603-08329"]
---
# Domain-partitioned retrieval

Instead of one index over the whole corpus, the corpus is cut along its document types and each cut gets its own vector collection. The reason given is structural: "we adopt a domain-partitioned retrieval strategy in which the legal corpus is" divided into separate pipelines, here case law, statutes and the Constitution, and the Indian Penal Code.[^c1] Each kind of document has its own shape. Judgments are chunked after isolating sections such as "Facts", "Issues" and "Held";[^c2] statutes are "segmented by article headers through regular expressions";[^c14] penal records are serialized into offense-and-punishment segments.[^c15] The authors' claim is that a single pool fails for this reason: "Treating these materials as a single undifferentiated corpus often" leads to drift.[^c3]

## Mechanism

The partition only helps if something decides which index a question goes to. Here an orchestrator does it: it "performs query classification to determine whether the input pertains to statutes, the IPC, case law, or multi-domain reasoning."[^c4] Retrieval then runs against one collection or in a hybrid mode, "depending on the detected query" type.[^c5] When several collections are searched at once, "a hybrid retriever fuses similarity scores across collections through weighted combination," and the weights are set per domain, "enabling domain-specific balancing between constitutional and statutory queries."[^c6]

Two stages follow. First the answerer decides where a question's evidence lives, before any retrieval; then it retrieves inside that source. The routing key is the domain label of the question, not its surface difficulty. The mechanism transfers beyond law only if the corpus really has parts with different internal structure and the classifier can tell them apart. Whether that holds elsewhere is my inference, not something the paper tests.

The paper's second routing target is a graph store for questions that similarity cannot reach: the knowledge graph exists for "relational and multi-hop queries that cannot be addressed by embedding similarity alone."[^c7] So the full design is two decisions: which partition, and whether to traverse relations.

## What was measured

The one system-level contrast removes the graph and keeps the partition: the comparison arm is the "RAG-Only Pipeline: Knowledge Graph removed."[^c8] The reported effect is on the graph, not on the partition: "The KG-augmented system consistently outperforms the non-KG variant across all metrics."[^c9] The partitioned modules are evaluated separately, with precision, recall and F1 at k, and the paper reads the Constitution module as precise but low in recall: it "maintains high precision but lower" recall, which the authors tie to its "tightly scoped statutory focus."[^c16]

## Limits

- No run isolates the partition. There is no single-index arm, so the claim that partitioning reduces drift is asserted from the design rationale, not measured.
- Routing accuracy is never reported. Whether the classifier sent each question to the right module, and how often it sent to several, is not scored in the parts I read.
- The method section calls the workflow "a planned agentic workflow";[^c11] §3.5 describes it as operating. Which parts ran in the reported evaluation is not stated in what I read.
- The benchmark is built from the index. The 40 questions were written "while ensuring that every question was answerable from the system" — so the benchmark measures what the partitioned index can answer, and a gap in the corpus cannot show up in it.
- Scoring is by an "independent judge model" on four dimensions, and "the overall score is computed as the mean of these dimensions."[^c12] The judge is not named in the parts I read, and no human agreement is reported there.
- Module-level retrieval numbers are low in places: the table row for Past Cases recall reads "0.150 0.245" at k = 5 and k = 10,[^c13] so, read as Recall@5, the case-law module returned about a seventh of the relevant passages (my inference from the table layout, which the text extraction makes hard to read).
- One jurisdiction, one corpus, one embedding model (all-MiniLM-L6-v2, top-k of 5 by default). Nothing here says the split survives a different corpus or embedder.

## Related

- [[syntactic-complexity-routing-between-retrieval-paths]] — routes between dense and graph retrieval by a parse-based complexity score; this note routes by the domain the query falls in, a different key.
- [[release-partitioned-corpus]] — the same kind of split by document version rather than by domain.
- [[cross-domain-evidence-integration]] — once evidence sits in several domains, an answer has to combine them; a partition makes that integration step necessary.
- [[per-source-exhaustive-coverage]] — the same kind of cut at the level of single documents, with one retrieval loop per document and no router; that paper compares against a pooled top-K baseline, so it does not isolate the cut either.

[^c1]: arxiv-2602-23371 — "we adopt a domain-partitioned retrieval strategy in which the legal corpus is"
[^c2]: arxiv-2602-23371 — "Case law documents which include around 2,900"
[^c3]: arxiv-2602-23371 — "Treating these materials as a single undifferentiated corpus often"
[^c4]: arxiv-2602-23371 — "which performs query classification to determine whether the input pertains to statutes, the IPC,"
[^c5]: arxiv-2602-23371 — "depending on the detected query"
[^c6]: arxiv-2602-23371 — "enabling domain-specific balancing between constitutional and statutory queries"
[^c7]: arxiv-2602-23371 — "enabling relational and multi-hop queries that cannot be addressed by embedding similarity alone"
[^c8]: arxiv-2602-23371 — "RAG-Only Pipeline: Knowledge Graph removed."
[^c9]: arxiv-2602-23371 — "The KG-augmented system consistently outperforms the non-KG variant across all metrics"
[^c10]: arxiv-2602-23371 — "maintains high precision but lower"
[^c16]: arxiv-2602-23371 — "reflecting its tightly scoped statutory focus"
[^c11]: arxiv-2602-23371 — "a planned agentic workflow"
[^c12]: arxiv-2602-23371 — "The overall score is computed as the mean of these dimensions"
[^c13]: arxiv-2602-23371 — "0.150 0.245"
[^c14]: arxiv-2602-23371 — "segmented by article headers through regular expressions"
[^c15]: arxiv-2602-23371 — "IPC data from the FIR dataset (3,481 records) is serialized"
[^c16]: arxiv-2602-23371 — "reflecting its tightly scoped statutory focus"
