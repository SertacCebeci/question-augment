---
description: "Generation-augmented retrieval writes candidate answers, contexts and titles per question, scores chunks against each and averages the scores; in medical QA it gained about 3 points over RAG."
aliases: ["GAR", "generation-augmented query expansion"]
sources: ["doi-10-48550-arxiv-2502-13361", "arxiv-2511-16283"]
---
# Generation-augmented retrieval

Generation-augmented retrieval (GAR) expands the query before the search, and the expansion is text written about the question rather than a rephrasing of it. The approach is described as "by generating relevant context for query expansion".[^c1] The original version fine-tunes a BERT model "to produce three types of content that enhance retrieval": potential answers, contexts and titles.[^c2]

What makes it an ensemble rather than a single rewrite is the scoring step. Each generated text is embedded and compared with the candidate chunks, the similarities are normalised over those candidates, and the results are combined into one score per chunk. The paper's wording is "normalizing and averaging the similarities of these expanded queries".[^c3] Read against its equation, this is a softmax over candidate chunks for each expansion, summed across the three, which is my reading of the formula.

The train-free variant replaces the fine-tuned generator with a prompted LLM. The paper frames this as the common practice, "to prompt LLMs to serve as train-free query generators", and implements GAR "train-free in accordance with" its own retrieval setup.[^c4] The point of averaging is stability. In a t-SNE view of one sample question, "the specific chunks retrieved do not overlap significantly" across the three generated queries, and the authors conclude there is "the need to average the retrieval similarities of these three queries to achieve more stable retrieval results".[^c5][^c6]

What was measured. On three medical QA sets with Llama-3.2-3B-Instruct, the authors report that "GAR outperforms vanilla RAG by approximately 3% on average, with a maximum improvement of 4.37% across datasets".[^c7] The average accuracy was 57.96 for GAR and 55.05 for RAG. The gain is not uniform: on MedMCQA, GAR scored 50.42 against 50.54 for RAG, so the average gain comes from the other two sets.[^c8] In an ablation on EHRNoteQA, "removing the multi-query generation step from CKR causes performance to degrade as N increases", which the authors read as evidence that several queries are needed for stable retrieval at larger depths.[^c9] Using the dataset's own answer options instead of generated ones changes little: "original options shows slightly higher average Accuracy, the difference is minimal".[^c10]

## Limits

- The GAR used here is the paper's own train-free implementation, not the fine-tuned original. The text read compares prompted expansion against vanilla RAG and does not run the fine-tuned version.
- The case for averaging rests on one sample question's t-SNE plot. The text read does not ablate the averaging rule against other fusion rules, such as rank fusion or counting how many variants retrieve a chunk. Whether averaging beats those is untested here.
- The setting is narrow: option-free retrieval, one corpus of textbook chunks, one dense retriever (MedCPT), and 32 chunks by default.
- The "about 3 points" is an average over three datasets, and it is not a gain on every one of them (see the MedMCQA result above).
- Averaging over generated texts assumes the generator's three texts are about the same topic. The paper's t-SNE shows they cover overlapping regions, not that they are correct; my reading is that correctness of the generated text is not measured here.
- Three expansions averaged are not the same as one passage split by intent. On multi-intent questions, a single long hypothetical passage is reported to lean toward one intent and under-represent the rest.[^c11] Averaging three GAR texts does not split a passage into intent-specific statements; whether it covers intents better than one passage is not tested in the text read. The split-then-fuse alternative is [[intent-decomposed-hypothetical-queries]].

## Related

- [[intent-decomposed-hypothetical-queries]] — splits one hypothetical answer into intent statements and fuses their rankings; the same starting point, with the split done before retrieval
- [[recurrent-factual-conceptual-retrieval]] — the loop whose first round is GAR; the recurrence adds the patient record as a second source and feeds extracted facts back into the query.
- [[multi-query-expansion-precision-penalty]] — a multi-query result that went the other way on a biomedical benchmark, with frequency fusion instead of score averaging.
- [[prompted-versus-trained-query-augmentation]] — the split between prompted and trained expansion; GAR was originally trained, and the paper uses it prompted.
- [[query-anchored-expansion-integration]] — how a saved expansion enters the query representation; score-level averaging is one such integration choice.

[^c1]: doi-10-48550-arxiv-2502-13361 — "by generating relevant context for query expansion"
[^c2]: doi-10-48550-arxiv-2502-13361 — "to produce three types of content that enhance retrieval"
[^c3]: doi-10-48550-arxiv-2502-13361 — "normalizing and averaging the similarities of these expanded queries"
[^c4]: doi-10-48550-arxiv-2502-13361 — "to prompt LLMs to serve as train-free query generators"
[^c5]: doi-10-48550-arxiv-2502-13361 — "the specific chunks retrieved do not overlap significantly"
[^c6]: doi-10-48550-arxiv-2502-13361 — "the need to average the retrieval similarities of these three queries to achieve more stable retrieval results"
[^c7]: doi-10-48550-arxiv-2502-13361 — "GAR outperforms vanilla RAG by approximately 3% on average"
[^c8]: doi-10-48550-arxiv-2502-13361
[^c9]: doi-10-48550-arxiv-2502-13361 — "Removing the multi-query generation step from CKR causes performance to degrade as N increases"
[^c10]: doi-10-48550-arxiv-2502-13361 — "original options shows slightly higher average Accuracy, the difference is minimal"
[^c11]: arxiv-2511-16283 — "a long synthetic passage is typically dominated by one prevailing intent (e.g., adverse drug effects) while underrepresenting others"
