---
description: "A patient record is filtered by the corpus chunks retrieved for it, and the filtered facts rewrite the next query in a loop; on EHR-based medical QA this beat one-shot expansion."
aliases: ["RGAR", "recurrence generation-augmented retrieval", "factual-conceptual recurrence"]
sources: ["doi-10-48550-arxiv-2502-13361"]
---
# Recurrent factual-conceptual retrieval

Medical questions draw on two kinds of knowledge that a retriever usually handles as one: conceptual knowledge in a medical corpus, and factual knowledge in the patient's own record. The RGAR system retrieves both and lets each refine the other, built on "both relevant factual and conceptual knowledge from dual sources".[^c1]

The loop has three steps. A general-purpose LLM writes several queries from a basic query (the question plus the record), and those queries "are then used to retrieve conceptual knowledge" from the corpus.[^c2] An LLM then reads the whole record with the question and the retrieved chunks, and keeps the facts it judges relevant, "to filter relevant factual knowledge efficiently and effectively using conceptual knowledge".[^c3] The basic query is then rebuilt from the question plus this extract, and the cycle repeats. "This establishes a recurrence interaction between" the two kinds of knowledge,[^c4] and "RGAR defaults to 2 rounds of recurrence".[^c5]

The mechanism rests on a view of records as noisy query material. The authors argue that "retrieval from EHRs can be seen as query filtering" that removes irrelevant content so the corpus is searched with the pertinent facts.[^c6] They also note that "lengthy EHR content containing substantial irrelevant information into dense retrievers can degrade" retrieval.[^c7] What separates this from a one-pass filter is the recurrence: the conceptual results decide which record facts count as relevant, and those facts decide the next search.

What was measured. With Llama-3.2-3B-Instruct, option-free retrieval, and 32 chunks from a 125.8k-chunk textbook corpus, the average accuracy over MedQA-USMLE, MedMCQA and EHRNoteQA was 61.04 for RGAR, 57.96 for one-shot GAR, 55.05 for vanilla RAG and 49.13 with no retrieval. "RGAR achieves the highest average performance across the three datasets".[^c8] On EHRNoteQA, the record-heavy set, RGAR scored 73.28 against 65.48 for GAR, but i-MedRAG scored 74.22, and the authors place RGAR "slightly below that of iMedRAG" there.[^c9]

Two ablations locate the gain. Keeping the factual extraction but removing its interaction with the conceptual results leaves "the system shows only moderate improvements when extracting factual knowledge from EHR without conceptual knowledge".[^c10] On rounds, "significantly improves performance by enabling interaction between factual and conceptual knowledge" even at one round, and with 8 chunks "the default two-round setup achieves a performance of 75.78%", about one point above a single round.[^c11][^c12] More rounds gave no clear benefit. The authors' account is that later rounds generate multi-hop facts, the retriever then fetches multi-hop concepts, "which may cause LLMs to over-infer".[^c13]

My inference, not tested in the paper: a loop whose next query is built from its previous output can carry one drifted step forward, the failure described for multi-round retrieval in [[knowledge-overshadowing]]. The paper's rounds result is consistent with that reading but does not isolate it.

## Limits

- The primary model is one 3B instruct model, "Our primary experiments utilize Llama3.2-3B-Instruct".[^c14] The model sweep (Table 3) is on MedQA-USMLE alone. The component and rounds ablations (Figure 3) are on EHRNoteQA alone, per the caption "Accuracy with Different Numbers of Retrieved Chunks on EHRNoteQA Dataset".[^c15]
- The gains are uneven. On MedMCQA, RGAR scored 51.02 against 50.01 with no retrieval, and the authors point to arithmetic questions, "MedMCQA incorporates arithmetic reasoning questions (roughly 7% of the total)".[^c16]
- The claim that gains grow with record length rests on the paper's own comparison: "the improvements achieved by our RGAR over GAR exhibit a positive correlation" with context length.[^c17] The evidence is three datasets plus four length bins on one of them.
- Retrieval was not scored directly. The authors say that "we evaluate retrieval effectiveness through QA performance", because no ground-truth chunks exist.[^c18] The recurrence is therefore credited through answer accuracy. The text does not check whether the extracted facts are faithful to the record; that gap is my reading.
- Long records: the method assumes the whole record fits the context window. "in extreme cases where EHR content exceeds" the limit, the authors suggest chunk-free approaches.[^c19]
- Cost: the authors say "our system operates with fixed time complexity", while corpus retrieval "its time complexity scales proportionally with the size of the" corpus.[^c20][^c21] The extra LLM calls per round are not given as a number in the text read.
- The comparison with GPT-3.5 uses a figure from another paper's setting: RGAR with Llama-3.1-8B is reported as "surpassing the 66.22% reported by MedRAG" for GPT-3.5, which was not rerun here.[^c22]
- The method is zero-shot, and "its effectiveness is partially contingent on" the model's instruction following, which the authors say they cannot fully mitigate.[^c23]

## Related

- [[generation-augmented-retrieval]] — the one-shot expansion that the loop's first round reduces to; the recurrence adds the record as a second source.
- [[knowledge-overshadowing]] — a failure of multi-round retrieval in which the next query drops a condition; the same drift could affect this loop (my inference).
- [[query-rewrite-filter-coupling]] — a rewrite's effect depends on the filter that follows it; the record extraction here is such a filter.
- [[multi-query-expansion-precision-penalty]] — a multi-query result that went the other way on a biomedical benchmark.

[^c1]: doi-10-48550-arxiv-2502-13361 — "both relevant factual and conceptual knowledge from dual sources"
[^c2]: doi-10-48550-arxiv-2502-13361 — "are then used to retrieve conceptual knowledge"
[^c3]: doi-10-48550-arxiv-2502-13361 — "to filter relevant factual knowledge efficiently and effectively using conceptual knowledge"
[^c4]: doi-10-48550-arxiv-2502-13361 — "This establishes a recurrence interaction between"
[^c5]: doi-10-48550-arxiv-2502-13361 — "RGAR defaults to 2 rounds of recurrence"
[^c6]: doi-10-48550-arxiv-2502-13361 — "retrieval from EHRs can be seen as query filtering"
[^c7]: doi-10-48550-arxiv-2502-13361 — "lengthy EHR content containing substantial irrelevant information into dense retrievers can degrade"
[^c8]: doi-10-48550-arxiv-2502-13361 — "RGAR achieves the highest average performance across the three datasets"
[^c9]: doi-10-48550-arxiv-2502-13361 — "slightly below that of iMedRAG"
[^c10]: doi-10-48550-arxiv-2502-13361 — "the system shows only moderate improvements when extracting factual knowledge from EHR without conceptual knowledge"
[^c11]: doi-10-48550-arxiv-2502-13361 — "significantly improves performance by enabling interaction between factual and conceptual knowledge"
[^c12]: doi-10-48550-arxiv-2502-13361 — "the default two-round setup achieves a performance of 75.78%"
[^c13]: doi-10-48550-arxiv-2502-13361 — "which may cause LLMs to over-infer"
[^c14]: doi-10-48550-arxiv-2502-13361 — "Our primary experiments utilize Llama3.2-3B-Instruct"
[^c15]: doi-10-48550-arxiv-2502-13361 — "Accuracy with Different Numbers of Retrieved Chunks on EHRNoteQA Dataset"
[^c16]: doi-10-48550-arxiv-2502-13361 — "MedMCQA incorporates arithmetic reasoning questions (roughly 7% of the total)"
[^c17]: doi-10-48550-arxiv-2502-13361 — "the improvements achieved by our RGAR over GAR exhibit a positive correlation"
[^c18]: doi-10-48550-arxiv-2502-13361 — "we evaluate retrieval effectiveness through QA performance"
[^c19]: doi-10-48550-arxiv-2502-13361 — "in extreme cases where EHR content exceeds"
[^c20]: doi-10-48550-arxiv-2502-13361 — "its time complexity scales proportionally with the size of the"
[^c21]: doi-10-48550-arxiv-2502-13361 — "our system operates with fixed time complexity"
[^c22]: doi-10-48550-arxiv-2502-13361 — "surpassing the 66.22% reported by MedRAG"
[^c23]: doi-10-48550-arxiv-2502-13361 — "its effectiveness is partially contingent on"
