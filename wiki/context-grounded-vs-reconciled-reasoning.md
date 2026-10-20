---
description: "Reasoning models in RAG either ground their answer in retrieved passages or reconcile them with internal knowledge; reconciling on irrelevant context is the costly mode."
aliases: ["context-grounded reasoning", "knowledge-reconciled reasoning", "reasoning strategy in RAG", "two reasoning modes over retrieved context"]
sources: ["arxiv-2512-18329"]
---
# Context-grounded vs knowledge-reconciled reasoning

When a reasoning model answers from retrieved passages, its reasoning takes one of two recognisable shapes. In the first, the model "treats the retrieved context as reliable evidence and performs reasoning directly based on it, without substantially invoking its internal knowledge."[^c1] The authors call this Context-Grounded Reasoning. In the second, the model "critically examines the retrieved information, compares it against its own internal knowledge, and resolves inconsistencies or gaps through reasoning."[^c2] They call this Knowledge-Reconciled Reasoning.

The split is measured, not only named. Qwen3, run in a standard vanilla RAG setup, was the subject: "we used the Qwen3 model on the HotpotQA dataset using a standard Vanilla RAG setup for 500 queries."[^c3] GPT-4o-mini was used to label each reasoning trace, and the result was "58.8% of model responses followed the Context-Grounded strategy, while 39.0% aligned with Knowledge-Reconciled reasoning."[^c4] The labelling says which mode a trace resembles. It does not show that the model chose that mode for a reason.

What the text reports as deciding the mode is the retrieved context. The grounded mode dominates "when the retrieval module provides relevant and sufficient information, the model predominantly relies on this external context as the principal evidence for inference."[^c5] The reconciling mode appears instead when the context is weak: "Knowledge-Reconciled Reasoning usually occurs when the retrieved contexts are irrelevant."[^c6] Under those conditions "the model draws upon internal knowledge to resolve knowledge conflicts, but this may lead to redundant reasoning."[^c7]

The cost is the point of the distinction. The reconciling mode is the one that spends tokens, and noisy retrieval is what triggers it. The authors' own account of their token savings runs the same way: their framework "eliminates conflicts in the context retrieved by retriever and generates clear reasoning steps. This avoids the knowledge conflicts and repeated redundant thinking that may occur in reasoning models."[^c8] Read as a mechanism (my reading, not the authors' wording): the same passages become a source of conflict or of plain evidence depending on whether they were filtered before the model reasons over them, and conflict is where the tokens go.

The authors also argue that the grounded mode can be carried into a non-reasoning model. Their framework reranks retrieved evidence and builds a reasoning chain from it. The abstract's headline is that it can "significantly reduce the average 98% output tokens overhead and 58.6% inferencing time."[^c9] The ablation says what carries the gain. Removing the retriever causes "a drastic drop in performance" on MuSiQue,[^c15] and "the Reasoning Constructor alone cannot compensate for the absence of relevant context."[^c10] So the grounded mode is only as good as the evidence it is given; restructuring cannot supply evidence that retrieval did not surface.

For a question-answerer, the distinction names a choice that is otherwise invisible: whether the supplied passages are being used as the evidence or are being overridden by what the model already holds. Asking which of the two is happening in a given answer is a question about the answer's source, not only its correctness (my inference from the mode split).

## Limits

- The strategy split is reported for one model family and one dataset in the text read: Qwen3, HotpotQA, 500 queries. Whether the 58.8% / 39.0% split holds for other models or datasets is not shown here.
- The labels are GPT-4o-mini's judgements, not human ones, and about 2.2% were ambiguous and dropped.[^c11][^c17] No agreement check against humans appears in the parts read.
- The authors call the two modes "preliminary observations" and frame them as "two hypotheses."[^c12] They are a working taxonomy, not a tested mechanism.
- The link from reconciling to token cost is the authors' explanation, backed by token-count comparisons. The per-model token numbers are in a figure I could not read in text form, so the 98% headline is taken from the abstract only.
- Reasoning is not uniformly helpful. On MultiHopRAG in vanilla RAG, "reasoning models exhibit slightly lower performance compared to nonreasoning models," which the authors attribute to how that dataset was built: its retrieval paragraphs are already structured, so "additional reasoning instructions could introduce unnecessary verbosity or overthinking."[^c13][^c16]
- Only multi-hop QA is tested. Nothing here shows the two modes in open-ended or non-retrieval settings.
- The token figure counts "all generated tokens, including reasoning steps," so it measures output volume, not the correctness cost of skipping reasoning.[^c14]

## Related

- [[distractor-similarity-reasoning-inflation]] — the same cost under irrelevant context, measured as reasoning-token growth and accuracy loss; this note names the mode that produces it.
- [[parametric-knowledge-gates-retrieval-noise-damage]] — irrelevant retrieval hurts accuracy mainly where the model's own knowledge is weak; the same gate seen from accuracy rather than tokens.
- [[parametric-suppression]] — a mechanistic account of how a memorised answer can overwrite conflicting evidence late in the network, the internal side of the reconciling mode.
- [[per-problem-reasoning-pattern-selection]] — reasoning patterns chosen per problem; here the pattern is the way retrieved evidence is used.

[^c1]: arxiv-2512-18329 — "The model treats the retrieved context as reliable evidence and performs reasoning directly based on it, without substantially invoking its internal knowledge."
[^c2]: arxiv-2512-18329 — "The model critically examines the retrieved information, compares it against its own internal knowledge, and resolves inconsistencies or gaps through reasoning."
[^c3]: arxiv-2512-18329 — "we used the Qwen3 model on the HotpotQA dataset using a standard Vanilla RAG setup for 500 queries."
[^c4]: arxiv-2512-18329 — "58.8% of model responses followed the Context-Grounded strategy, while 39.0% aligned with Knowledge-Reconciled reasoning."
[^c5]: arxiv-2512-18329 — "when the retrieval module provides relevant and sufficient information, the model predominantly relies on this external context as the principal evidence for inference."
[^c6]: arxiv-2512-18329 — "Knowledge-Reconciled Reasoning usually occurs when the retrieved contexts are irrelevant."
[^c7]: arxiv-2512-18329 — "the model draws upon internal knowledge to resolve knowledge conflicts, but this may lead to redundant reasoning."
[^c8]: arxiv-2512-18329 — "This avoids the knowledge conflicts and repeated redundant thinking that may occur in reasoning models."
[^c9]: arxiv-2512-18329 — "significantly reduce the average 98% output tokens overhead and 58.6% inferencing time"
[^c10]: arxiv-2512-18329 — "the Reasoning Constructor alone cannot compensate for the absence of relevant context."
[^c11]: arxiv-2512-18329 — "we employed GPT-4o-mini to annotate all model outputs based on their reasoning contents."
[^c12]: arxiv-2512-18329 — "Based on preliminary observations, we propose two hypotheses regarding the reasoning strategy in the RAG framework"
[^c13]: arxiv-2512-18329 — "Within the Vanilla RAG setting, reasoning models exhibit slightly lower performance compared to nonreasoning models."
[^c14]: arxiv-2512-18329 — "output tokens cover all generated tokens, including reasoning steps."
[^c15]: arxiv-2512-18329 — "The Retriever has the most pronounced impact on MuSiQue, where its removal causes a drastic drop in performance."
[^c16]: arxiv-2512-18329 — "additional reasoning instructions could introduce unnecessary verbosity or overthinking"
[^c17]: arxiv-2512-18329 — "The remaining 2.2% were ambiguous and excluded from further analysis."
