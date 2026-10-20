---
description: "Before retrieval, a question is unrolled into sub-questions and a reasoning chain whose low-confidence entities stay masked, so guessed content does not steer the search."
aliases: ["question unrolling", "unrolled question", "masked reasoning chain", "uncertainty mask in query formulation"]
sources: ["arxiv-2512-10422"]
---
# Uncertainty-masked question unrolling

A question is rewritten before it reaches a retriever. The rewrite has three parts: the original question Q, a set of sub-questions S, and a reasoning chain R of triples (head, relation, tail). The model fills an entity only where it is confident. "Each entity stands for either an uncertainty mask ⟨UNCERTAIN⟩ if the LLM lacks confidence; a question-related concept otherwise," and the last tail is a placeholder ⟨FILL⟩ for the answer.[^c1] The unrolled question U = Q‖S‖R is what gets embedded and searched.

The mechanism turns on what is left out of the query. An entity the model is unsure of, once written into the search text, pulls retrieval toward documents that match the guess. The authors state the trade directly: "generating such entities and augmenting the original question with these entities could rather lead to wrong retrievals or hallucinations in reasoning."[^c2] Masking keeps the search text to what the model holds with confidence and leaves the open slot as an explicit hole.

The hole is filled later, after retrieval. Given the unrolled question and the top-k documents, "the LLM fills in the uncertainty masks" from the evidence, and the answer is generated from the completed chain.[^c3] The paper states the consequence for the pipeline: "the LLM and the retriever can leverage only internal knowledge about" what the model is certain of, and the masked slots are where retrieved evidence is supposed to enter.[^c4]

What was measured. Removing both the masks and the completion stage lowered retrieval Recall@2 on the multi-hop sets: the authors report gains from the masks of "8.0% on MuSiQue, and 8.9% on 2WikiMultihopQA," with a smaller 1.4% on HotpotQA.[^c5] Decomposition into sub-questions and the masked chain were ablated separately: on MuSiQue, the full unrolling "raises it to 59.6%, achieving a 36% improvement" over no unrolling.[^c6] The authors' explanation is that "masking out low-confidence tokens prevents negative effects on subsequent inference steps."[^c7] That is their reading of their own numbers, not a separately tested mechanism.

A transfer to human asking, which is my inference and not the paper's: a question asked with its known parts and its open slots written apart gives a search two different jobs. The known parts are the query; the open slots are the targets the answer must supply. Writing the unknowns down before searching is what the masks do for the model.

## Limits

- The evidence is for one system: an LLM writes the unrolling, a fine-tuned dense encoder retrieves, and the QA sets are HotpotQA, 2WikiMultihopQA, MuSiQue and NaturalQuestions. Open-ended questions, questions without a fixed answer, and human askers are not tested.
- The mask ablation removes two things at once. The variant "does not generate uncertainty masks in question unrolling and does not perform reasoning chain completion."[^c8] The gain is therefore the combined effect of masking and completion, not of masking alone.
- The criterion for "lacks confidence" is not stated in the passages I read; it is said to be in the prompt appendix (H.1), which I did not read. Whether the model's confidence is calibrated is not checked here.
- The sub-question and masked-chain ablation (Table 16) reports single recall numbers. I found no variance or repeated runs in the passages read (my reading).
- The paper's second contribution, reranking by contrasting retriever layers, is a retrieval scoring method. It changes which documents are ranked, not how a question is formed or answered, so it is not written here.

## Related

- [[self-ask-decomposition]] — the sub-question half of unrolling; self-ask answers each sub-question in turn, while unrolling fixes the sub-questions as query text for one retrieval.
- [[query-anchored-expansion-integration]] — also about how generated text enters retrieval; there the expansion is interpolated with the query vector, here it is written into the question with its unknowns marked.
- [[prompted-versus-trained-query-augmentation]] — the rival family of LLM-written query expansion; unrolling differs in producing an explicit decomposition with holes rather than a pseudo-document.

[^c1]: arxiv-2512-10422 — "Each entity stands for either an uncertainty"
[^c2]: arxiv-2512-10422 — "generating such entities and augmenting the original question with these entities could rather lead"
[^c3]: arxiv-2512-10422 — "the LLM fills in the uncertainty masks"
[^c4]: arxiv-2512-10422 — "the LLM and the retriever can leverage only internal knowledge about"
[^c5]: arxiv-2512-10422 — "8.0% on MuSiQue, and 8.9% on 2WikiMultihopQA"
[^c6]: arxiv-2512-10422 — "MQ + SQ + RC raises it to 59.6%, achieving a 36% improvement"
[^c7]: arxiv-2512-10422 — "masking out low-confidence tokens prevents negative effects on subsequent inference steps"
[^c8]: arxiv-2512-10422 — "does not perform reasoning chain completion, on the retrieval and QA performances"
