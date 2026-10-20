---
description: "A chunk is scored by how probable it makes the reference answer under the generator, teacher-forced, so sufficiency for answering is measured directly, not by query similarity."
aliases: ["in-context answer sufficiency", "forward alignment score", "answer-centric chunk scoring", "answer log-likelihood chunk score"]
sources: ["arxiv-2511-16326"]
---
# Answer-sufficiency chunk score

A retrieved chunk can be scored by what it does for the answer rather than by how much it resembles the question. The score used in the ARK paper is the generator's own likelihood. The chunk is placed in the prompt together with the question, and the model is asked how probable the reference answer is, token by token. The authors call this the forward alignment, and say it "quantifies the sufficiency of the chunk t to generate the correct answer."[^c1] The answer tokens serve as targets under teacher forcing, so the model is never asked to generate them freely. The score is the mean token log-likelihood, "without them being part of the conditioning context."[^c2] It is computed "in a single forward pass."[^c3]

The second instrument runs the other way. The backward alignment pairs the chunk with the answer and scores the probability of reconstructing the question. It measures "the relevance of a chunk in linking the answer back" to the query.[^c4] Together the two make a two-sided check. A chunk that makes the answer likely given the question, and the question likely given the answer, is one that lies on the path between them. The paper states the aim as "selected chunks are strongly correlated with the" reasoning path from question to answer.[^c5]

The positives are then chosen by a unified score, S = λf·Sf + λb·Sb + λv·Sv. The third term is the cosine similarity under the original retriever, kept as a regulariser: its purpose is "to regularize the finetuning process and mitigate catastrophic forgetting."[^c6] The weights are fixed by the authors, who say "we believe adjustment is unnecessary."[^c7] The top-M chunks by this score become the positive set for each query.

What changes is the unit of judgment. A query-similarity retriever asks whether a chunk is about the question. The sufficiency score asks whether, given that chunk, the generator would write the reference answer. The paper's motivation is that the two can come apart. Standard retrievers, "optimized for query-document similarity, frequently fail to align with the downstream goal of generating a precise answer."[^c8] The reported effect is an average gain: the abstract says the fine-tuned retriever is "improving 14.5% over the base model" on the ten evaluated datasets.[^c9] The ablation attributes most of this to the forward term: "Forward alignment proves most critical, as it directly" measures sufficiency for the correct answer.[^c10]

## Limits

- The score is a likelihood under one generator. A chunk is sufficient for that model with that reference answer; the text read does not show how a different generator would rank the same chunks. The property measured is a chunk-with-model property, which is my inference from the formula, not a claim the paper makes.
- It needs a reference answer for every training question. The training set is small: the paper says it samples "200 cases each from the" Finance and Legal domains.[^c11] The text read does not show how the score behaves on questions whose answers are long or open-ended, where the likelihood of one reference is a noisy target.
- The score is per chunk. Where an answer needs several chunks together, each chunk can look insufficient alone. The paper's gains are largest on the multi-hop sets, where "retrieval must synthesize dispersed evidence."[^c12] A per-chunk likelihood does not model that joint need, and the parts read do not test it.
- The weights λf, λb, λv are not tuned. The text read gives no sensitivity analysis, so how much the ranking depends on those choices is not known.
- The paper reports gains over the base retriever. I found no comparison in the parts read against a sufficiency judgment that is not a likelihood, such as a learned verdict or a human label, so the likelihood is not shown to be the best instrument of sufficiency, only a working one.

## Related

- [[answer-supervised-retrieval]] — trains the ranking itself from answer loss through a straight-through top-k; here the answer likelihood only chooses positives, and the retriever is trained by a contrastive loss on query-chunk cosine.
- [[information-gain-reward]] — the same teacher-forced log-likelihood instrument, used as a reward for clarifying exchanges rather than as a score for chunks.
- [[sufficiency-criterion-strictness]] — whether a context counts as sufficient depends on the criterion chosen; the likelihood score is one criterion among others.
- [[structured-gap-sufficiency-judge]] — a learned binary sufficiency verdict with a typed gap; the score here is continuous and read off the generator's own probabilities.
- [[augmented-query-hard-negative-curriculum]] — the later stages of the same paper, which contrast these selected positives against hard negatives mined by augmented queries.

[^c1]: arxiv-2511-16326 — "quantifies the sufficiency of the chunk t to generate the correct answer"
[^c2]: arxiv-2511-16326 — "without them being part of the conditioning context"
[^c3]: arxiv-2511-16326 — "This score is computed in a single forward pass"
[^c4]: arxiv-2511-16326 — "the relevance of a chunk in linking the answer back"
[^c5]: arxiv-2511-16326 — "selected chunks are strongly correlated with the"
[^c6]: arxiv-2511-16326 — "To regularize the finetuning process and mitigate catastrophic forgetting"
[^c7]: arxiv-2511-16326 — "we believe adjustment is unnecessary"
[^c8]: arxiv-2511-16326 — "frequently fail to align with the downstream goal of generating a precise answer"
[^c9]: arxiv-2511-16326 — "improving 14.5% over the base model without substantial architectural modifications"
[^c10]: arxiv-2511-16326 — "Forward alignment proves most critical, as it directly"
[^c11]: arxiv-2511-16326 — "sample 200 cases each from the"
[^c12]: arxiv-2511-16326 — "where retrieval must synthesize dispersed evidence"
