---
description: "Choosing evidence as a set can score properties no single item has, such as coverage, non-redundancy and consistency; per-item relevance ranking cannot see them."
aliases: ["document-set selection", "set-level relevance", "subset selection for generation", "set-level evidence selection"]
sources: ["doi-10-48550-arxiv-2608-03527"]
---
# Set-level selection over per-item relevance

A retriever usually scores each candidate against the query and keeps the top k. When the answerer then reads the kept items together, the set can fail a requirement that no single item fails. The paper's example is a patient asking how to treat depression: every retrieved document is relevant, yet "the resulting set remains suboptimal for several reasons" — it misses one treatment type, repeats psychotherapy content, and includes a non-authoritative source.[^c1] The authors locate the cause in the training signal: relevance labels "measure the relevance of single document", and so "it cannot ensure that the returned document set satisfies the" needs of the query.[^c2] Their claim is that "individually well-matched topk documents may not form a set that satisfies" the agent's needs.[^c3]

The alternative the paper proposes puts the requirements at the level of the set. Its set-level rubrics are "overall quality of a document set" along three dimensions: relevance, covering the aspects the query needs; conciseness, "whether the set contains little repetitive, redundant," or irrelevant content; and consistency, whether claims across documents are compatible.[^c4][^c5] None of these can be read off one document, and each needs the whole candidate set in view. The selected set is the object being judged; a training label is a chosen subset, not a ranking. In the label ablation, replacing the rubric-guided set labels with a conventional relevance ranking lowered the average score from 52.5 to 48.1, and the authors read this as evidence that "relevance ranking is insufficient for generationoriented document-set selection."[^c6][^c7]

The rubrics are used only to build training labels and to score rollouts. At inference the reranker "directly selects a high-quality subset from" the retrieved candidates, with no rubric in its input.[^c8] So the set requirement is meant to be carried by the trained selector, not checked at run time. What was measured is downstream: the trained reranker scored 60.1 on four deep-research benchmarks, "outperforming the second-best baseline," by 2.6 points, and about 2 points on five RAG benchmarks.[^c9]

## Limits

- The measured quantity is the score of an agent's final answer under LLM-judged rubrics, not the quality of the selected set. The authors say so: "Developing more objective metrics to directly evaluate the quality of selected document sets is a promising direction."[^c10]
- The set rubrics are written by GPT-5.1 from a reference answer that GPT-5.1 also wrote. The rubric weights and the aspects they name are therefore one model's view of the need. The authors say "The construction of rubric-based rewards relies on GPT-5.1," which they flag as costly at scale.[^c11]
- The ablations in the section I read remove RL, remove cold-start SFT, remove the rubrics from the teacher, or switch the label to a ranking. None removes the set-level rubrics alone, and none compares them with a plain diversity or redundancy criterion. So the gain is not shown to come from set structure rather than from extra supervision.
- The deep-research test sets are samples: "we sample a subset of queries" from each benchmark, because judging is expensive.[^c12]
- The evidence is one backbone (Qwen3-8B) and one search API for the deep-research side. Whether the effect holds for other sizes of set or other retrievers is not tested here.

## Related

- [[evidence-grade-calibrated-reranking]] — the per-item alternative: a learned grade bias is added to each document's relevance score, so the ranking stays additive over items.
- [[ig-redundancy-coverage-utility]] — a subset score with a redundancy penalty and a coverage bonus, the same shape of objective applied to follow-up questions rather than documents.
- [[questioning-diversity]] — a set-level diagnostic over a set of generated questions; it measures one of the set properties this paper writes into its rubrics.
- [[minimal-conflict-localization-under-noisy-oracle]] — the same point for consistency: a property of a whole set that pairwise checks cannot certify.
- [[reader-slot-zero-primacy]] — reports that MMR diversification did not help a frozen reader; that is a diversity heuristic, not a set selector learned from rubrics, so the two do not test the same thing.
- [[hierarchical-set-rubric-reward]] — how the set-level and document-level scores of a selected set are combined into one reward.
- [[determinantal-quality-diversity-selection]] — a fixed-size subset scored by a determinant, so that redundancy costs score without a rubric; a concrete set objective where this note's paper learns set labels from rubrics.

[^c1]: doi-10-48550-arxiv-2608-03527 — "the resulting set remains suboptimal for several reasons"
[^c2]: doi-10-48550-arxiv-2608-03527 — "ensure that the returned document set satisfies the"
[^c3]: doi-10-48550-arxiv-2608-03527 — "individually well-matched topk documents may not form a set that satisfies"
[^c4]: doi-10-48550-arxiv-2608-03527 — "overall quality of a document set"
[^c5]: doi-10-48550-arxiv-2608-03527 — "whether the set contains little repetitive, redundant,"
[^c6]: doi-10-48550-arxiv-2608-03527 — "relevance ranking is insufficient for generationoriented document-set selection"
[^c7]: doi-10-48550-arxiv-2608-03527 — "This variant further decreases the average score to 48.1"
[^c8]: doi-10-48550-arxiv-2608-03527 — "At inference time, RubricRanker directly selects a high-quality subset from"
[^c9]: doi-10-48550-arxiv-2608-03527 — "60.1, outperforming the second-best baseline,"
[^c10]: doi-10-48550-arxiv-2608-03527 — "Developing more objective metrics to directly evaluate the quality of selected document sets is a promising direction."
[^c11]: doi-10-48550-arxiv-2608-03527 — "The construction of rubric-based rewards relies on GPT-5.1,"
[^c12]: doi-10-48550-arxiv-2608-03527 — "we sample a subset"
