---
description: "Scoring an answer by the cosine similarity of its embedding to the retrieved evidence fails as a grounding signal for short answers: length and specificity mismatch dominates the score."
aliases: ["evidence-consistency signal", "answer-evidence cosine", "embedding grounding score", "answer-evidence similarity"]
sources: ["doi-10-48550-arxiv-2606-29090"]
---
# Answer-evidence embedding similarity

A natural way to ask whether an answer is grounded in the evidence it was produced from is to embed both and compare the vectors. AB-RAG builds this in as its second confidence signal: the cosine similarity between the embedding of the answer and the embedding of the evidence, mapped to [0, 1].[^c1] The intent is that a high value means the answer is semantically close to the evidence, which the paper takes to indicate grounding.[^c2]

On short-answer question answering the signal does not work. On the closed model its AUROC against answer correctness sits at 0.353 and 0.374, which the paper reads as no better than chance and on these datasets slightly worse.[^c3] The explanation the paper gives is a mismatch of form rather than a failure of grounding. The answers "are very short, often a single name or a few words, while the passages are long," and embedding a two-word answer and a hundred-word passage into one space produces a score that is dominated by the difference in length and specificity, not by whether the answer is supported.[^c4][^c5]

Alternative formulations were tried. "Several alternative formulations were tried, and Table X shows" that none of them rescued the signal.[^c6] The paper did not drop the signal: "reached a useful level, it is kept in the estimator at a near-zero" weight of 0.05.[^c7] It keeps the door open for longer answers, where a similarity between answer and evidence might carry more information, and the paper says so.[^c8]

What survives the transfer from this setting is the structural point. A symmetric embedding similarity between a short string and a long context measures how alike their surface and topic are, and a short answer is almost never alike a passage in length, so the score is confounded before it reaches the question of support. What does not survive is any claim that answer-evidence similarity is useless as such: the paper's failure is measured on one kind of answer, and the text leaves longer answers untested (my reading).

## Limits

The AUROC figures are the closed-model ones quoted above; the per-backbone table for this signal was not read in full here. The alternative-formulation test (Table X) is reported for one backbone and one dataset, so "none of them rescued the signal" holds only there.

The length-and-specificity account is the paper's explanation for the failure. The text reads as an argument from the setting, not as a controlled manipulation that holds the answer's length fixed while varying support, so the mechanism is plausible rather than isolated (my reading).

Nothing here measures grounding by a different means. The note says that this similarity fails, not that every grounding check does; a check that reads the evidence against the answer as a claim is a different object and is not tested in this work.

## Related

- [[abstention]] — the selective-prediction setting in which a confidence score is used as a gate; this is one candidate score that does not separate correct answers.
- [[stop-continue-criteria-in-retrieval-loops]] — the loop in which AB-RAG wants its three signals to decide whether to retrieve more; the grounding term is one of the inputs.
- [[answer-evidence-gap]] — a different failure of answer-support: there the final answer stays right while the visible reasoning stops supporting it; here a similarity score cannot tell whether support is present at all.

[^c1]: doi-10-48550-arxiv-2606-29090 — "evidence. It is the cosine similarity between the embedding"
[^c2]: doi-10-48550-arxiv-2606-29090 — "A high value means the answer is semantically close to the evidence, which is intended to indicate grounding."
[^c3]: doi-10-48550-arxiv-2606-29090 — "closed model, at 0.353 and 0.374, which means it is no better"
[^c4]: doi-10-48550-arxiv-2606-29090 — "these datasets are very short, often a single name or a few"
[^c5]: doi-10-48550-arxiv-2606-29090 — "specificity that the cosine similarity is dominated by that"
[^c6]: doi-10-48550-arxiv-2606-29090 — "Several alternative formulations were tried, and Table X shows"
[^c7]: doi-10-48550-arxiv-2606-29090 — "reached a useful level, it is kept in the estimator at a near-zero"
[^c8]: doi-10-48550-arxiv-2606-29090 — "leaves the door open for tasks"
