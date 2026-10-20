---
description: "Splitting one LLM-written hypothetical answer into one query per intent, then fusing the per-query rankings by rank, keeps a dominant intent from crowding out the others in retrieval."
aliases: ["HQG", "hypothetical query generation", "intent-specific hypothetical queries", "hypothetical fact pool"]
sources: ["arxiv-2511-16283"]
---
# Intent-decomposed hypothetical queries

Retrieval can be driven by text the LLM writes about the question instead of by the question itself. In the hypothetical-document family, the LLM writes a plausible answer and that passage is embedded in place of the question. For a question with several correct answers, one such passage has a known weakness. In the MuISQA paper's example about Alzheimer's drugs, a long synthetic passage "is typically dominated by one prevailing intent (e.g., adverse drug effects) while underrepresenting others" such as therapeutic efficacy or active compounds.[^c1] Embedding the whole passage as one vector "risks emphasizing certain intents and suppressing complementary information".[^c2]

The mechanism changes the unit that is embedded. The LLM first writes several hypothetical answer instances, each describing one candidate answer. Each instance is then broken into factual statements, one per intent, so the pool holds a statement for each pair of instance and intent. The paper's wording is that the procedure "explicitly decomposes it into a set of focused statements, each capturing a distinct sub-intent of the original question".[^c3] Each statement is embedded alone and returns its own ranked list of chunks.

The lists are merged by reciprocal rank fusion. A chunk's score is the sum, over all lists, of 1/(k + rank), so only positions count and raw similarities do not. The stated reason is that similarity scores fluctuate across documents and that dense models have a bias: "dense embedding models often exhibit bias toward" certain fragment types, with high-frequency domain terms scoring too high.[^c4] The smoothing constant is fixed at K=60 in all experiments.[^c5] Rank fusion of this kind also appears in [[entity-aware-rank-fusion]], where it merges entity order with dense order; the sense here is the same, the lists differ.

What survives the transfer from question decomposition. [[question-decomposition-retrieval]] splits the question into sub-queries and then reranks the merged pool against the original question. Here the object split is a hypothesis, not the question: the pieces are claims that a plausible answer would contain, and their job is to reach passages that a question-shaped query does not reach. The method's point is that the split happens before retrieval and that the fusion is by rank. Whether a reranker against the question is needed afterwards is not addressed in the text read.

What was measured. On the MuISQA benchmark the paper reports that the method "substantially enhances evidence diversity, retrieval coverage, and answer completeness compared with existing RAG baselines".[^c6] The table's Average IRR column, read in the row order of its methods, gives 61.2 for naive RAG, 63.5 for HyDE and 67.5 for this method, with Qwen2.5-72B as the generator (my reading of an unlabelled table layout).[^c7] The generator matters: with Qwen2.5-3B, 7B, 72B and Qwen3-235B the method's IRR is 62.6, 62.8, 67.5 and 66.4, and the paper's reading is that "smaller models often produce less informative and domain-aware hypotheses, yielding weaker queries and reduced retrieval and answer quality."[^c8]

The paper also reports that a wrong hypothesis can still help. In a MuSiQue case, an incorrect statement about a person's father raised the similarity of the target passage and led to successful retrieval, and the paper says imperfect hypothetical generation "can occasionally facilitate retrieval by guiding the search toward target passages".[^c9] So the retrieval gain does not need the hypothesis to be true; it needs the hypothesis to point at the right region of the corpus.

## Limits

- No ablation in the text read separates the two steps. The full text, as searched, has no run that removes the intent split or the fusion alone. The comparison is against naive RAG, query rewriting, HyDE and Core-SubQ. My inference: the gain cannot yet be attributed to the split rather than to the larger number of retrieval calls the method makes per question.
- The benchmark is the authors' own: 500 questions in five domains, each with 20 arXiv articles retrieved by keyword and no manual filtering.[^c10] Its gold answers were pre-annotated by an LLM and then corrected by humans, and the pre-annotation model, DeepSeek-V3, is also one of the generators tested.[^c11] Whether that shares blind spots with the method is not tested here.
- The general datasets (HotpotQA, 2WikiMQA, MuSiQue, NQ, TriviaQA) are multi-hop or single-answer sets. They test generalisation of the retrieval pipeline, but they do not contain multi-intent questions, so they do not test the mechanism that motivates the method.
- The paper's "vector entropy" measure of query diversity hardly moves across methods: the table values sit between 8.06 and 8.18 (my reading). The measured retrieval gain is therefore not accompanied by a query-side diversity gain as the paper's own metric registers it.
- The number of intent statements per question is not varied in the text read, and K=60 with top-10 passages is fixed. The paper reports that varying K has "only a minor effect on passage-level retrieval metrics," but the depth of the hypothesis pool is not studied.[^c12]

## Related

- [[question-decomposition-retrieval]] — sub-queries split from the question, merged and then reranked against it; here the hypothesis is what gets split
- [[generation-augmented-retrieval]] — averages the scores of several expansions rather than splitting one passage into intent statements; the single-passage weakness above applies to it
- [[entity-aware-rank-fusion]] — another rank-level RRF merge, of entity order with dense order
- [[multi-intent-evidence-coverage]] — the measure this method was scored with, and where its gain is read
- [[hypothesis-conditioned-query-rewriting]] — forms a working answer first and rewrites retrieval around it, which is the same starting point with a different split

[^c1]: arxiv-2511-16283 — "a long synthetic passage is typically dominated by one prevailing intent (e.g., adverse drug effects) while underrepresenting others"
[^c2]: arxiv-2511-16283 — "risks emphasizing certain intents and suppressing complementary information"
[^c3]: arxiv-2511-16283 — "explicitly decomposes it into a set of focused statements, each capturing a distinct sub-intent of the"
[^c4]: arxiv-2511-16283 — "dense embedding models often exhibit bias toward"
[^c5]: arxiv-2511-16283 — "the RRF smoothing constant is set to K=60"
[^c6]: arxiv-2511-16283 — "substantially enhances evidence diversity, retrieval coverage, and answer completeness compared with existing RAG baselines"
[^c7]: arxiv-2511-16283
[^c8]: arxiv-2511-16283 — "queries and reduced retrieval and answer quality"
[^c9]: arxiv-2511-16283 — "retrieval by guiding the search toward target passages"
[^c10]: arxiv-2511-16283 — "we retrieve 20 articles without manual filtering"
[^c11]: arxiv-2511-16283 — "We developed a custom annotation interface and adopted DeepSeek-V3 as the sole model for pre-annotation"
[^c12]: arxiv-2511-16283 — "varying K has only a minor effect on passage-level retrieval metrics"
