---
description: "Restricting a retriever's candidate pool to the gold document, then to the gold pages, gives a diagnostic ceiling that splits page-recall loss into cross-document and within-document parts."
aliases: ["oracle-restricted retrieval", "oracle candidate pool", "Oracle-Document and Oracle-Page conditions", "oracle page retrieval"]
sources: ["doi-10-71781-36173"]
---
# Oracle candidate restriction

A retrieval failure can have two causes that look identical in an end-to-end score: the retriever ranks chunks from the wrong filing above the right ones, or it ranks the right filing but the wrong pages above the answer-bearing page. The thesis separates them by running the same retriever, with the same embedding model and similarity function, over three nested candidate sets. Standard retrieval searches the full corpus. Oracle-Document keeps only chunks from the gold filing. Oracle-Page keeps only chunks from the gold pages of the gold filing. The sets satisfy strict containment, so with a fixed retriever the only thing that changes across conditions is the pool the search runs over.[^c1]

The point of the construction is the bound it gives. Because each oracle set is a subset guaranteed to contain the gold evidence, removing distractors can only help a monotone metric, and the thesis states this as an inequality on page recall and on answer accuracy, under a fixed generator.[^c2] The difference between standard retrieval and Oracle-Page is then split in two. The first term, the cross-document gap, is the page-recall gain from fixing the document. The second, the generation gap, is the accuracy gain from giving the generator the gold pages instead of the gold filing. A large first term points at document discovery; a large second term points at within-document localization.[^c3]

On FinanceBench at k = 5 with BGE-M3, the decomposition gives a clear reading. Standard retrieval reaches document recall 0.94 but page recall 0.35.[^c4] Restricting to the gold filing raises page recall to 0.60, so cross-document interference accounts for 0.25 points of lost page recall. The remaining 0.40 is within the correct filing. Moving from Oracle-Document to Oracle-Page raises numeric match from 0.44 to 0.70.[^c5] The thesis reads this as imprecise page localization, rather than generation capacity, being the main obstacle to correct numeric answers.[^c6]

## Limits

- The oracle conditions are diagnostic reference points under one retriever, not ceilings. The thesis says so directly: "bounds rather than mathematical guarantees for every possible model." A learned reranker or domain-tuned retriever can exceed the Oracle-Document score by using signals the fixed oracle retriever does not use.[^c7]
- Oracle-Page is 1.00 page recall by construction, since the gold pages are supplied from annotation. What it measures is the within-page chunk quality and ranking, not whether a page can be found.[^c8]
- The monotonicity claim holds only for robust metrics, those that depend on whether gold evidence is present. Surface metrics such as ROUGE-L or BLEU may not be monotone under removal of distractors, so the bound does not transfer to them.[^c9]
- The decomposition was run on one benchmark, FinanceBench, with 150 questions and one embedding model at k = 5.[^c10] The thesis does not show that the split between document-level and page-level loss holds on other corpora or at other k.
- The thesis's own term for the gap is the diagnostic decomposition, and it is not a proof that either term is a fixed property of the task. Under a different retriever the two terms can move.

## Related

- [[retrieval-utilization-gap]] — separates evidence that never surfaced from evidence that surfaced and was misused; this note splits the never-surfaced part further into document and page levels.
- [[candidate-set-narrowing-recall]] — narrowing a set helps only while the right option survives the cut; the oracle conditions are narrowing with recall fixed at one by construction.
- [[two-stage-reranking]] — a reranker reorders a first-stage candidate set; the oracle bound above applies to a fixed first stage and does not cap a reranked pipeline.

[^c1]: doi-10-71781-36173 — "yielding empirical upper bounds on what retrieval improvements alone could achieve."
[^c2]: doi-10-71781-36173 — "from the fact that the generator Gθ is fixed across conditions, so improvements in retrieved"
[^c3]: doi-10-71781-36173 — "If ∆page is large, improvements should focus on crossdocument retrieval. If ∆gen is large, improvements should focus on finer-grained evidence"
[^c4]: doi-10-71781-36173 — "Standard retrieval achieves high document recall (DocRec@5 = 0.94) but low page recall (PageRec@5 = 0.35)."
[^c5]: doi-10-71781-36173 — "raises numeric match from 0.44 to 0.70, a gain of 0.26 points that reflects the quality of"
[^c6]: doi-10-71781-36173 — "imprecise page localization, not generation capacity, is the primary obstacle to correct"
[^c7]: doi-10-71781-36173 — "a learned reranker or a domain-tuned retriever can exceed an oracle-document score by using ranking signals that"
[^c8]: doi-10-71781-36173 — "The gold evidence is guaranteed to appear in the candidate pool, the only remaining source"
[^c9]: doi-10-71781-36173 — "or embedding-based scores may not be monotonic, as they can be influenced by irrelevant"
[^c10]: doi-10-71781-36173 — "evaluated on the full 150 FinanceBench questions at k = 5."
