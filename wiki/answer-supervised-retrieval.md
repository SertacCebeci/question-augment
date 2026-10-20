---
description: "A retriever can be trained without relevance labels: the generator's next-token loss flows back through a straight-through top-k selection over compressed document vectors."
aliases: ["generator-supervised retrieval", "label-free retriever training", "straight-through top-k retrieval", "end-to-end retrieval through the generation loss"]
sources: ["arxiv-2511-18659"]
---
# Answer-supervised retrieval

A retriever is usually built to rank documents by how much they resemble the question. Answer-supervised retrieval changes what the ranking is judged by: the ranking is updated with the loss of the answer the generator writes from the top documents, so a document is preferred when it makes the reference answer more likely. The CLaRa paper motivates this by the failure of the usual split. "Retrievers select documents based on surface-level similarity"[^c1], and when selection is discrete the generator's signal does not reach the ranking, so nothing tells the retriever "why certain documents should be preferred over others."[^c2]

The mechanism, as the paper builds it. Each document is compressed once, offline, into a fixed set of memory-token vectors by a frozen compressor. A query is encoded into the same space by a separate query encoder, and each document receives a cosine score against it. The top-k documents are chosen with a straight-through (ST) estimator. The forward pass keeps the discrete choice; the backward pass uses a temperature softmax over the same scores, so the choice is hard at inference and gradients still flow during training. The authors describe this as preserving "retrieval behavior during inference while allowing smooth gradient feedback during training."[^c3] The selected vectors are concatenated with the query and fed to the generator, and one next-token loss updates both the query encoder and the generator.

The alternative the authors argue against is reinforcement-learning retrieval, in which the retriever is updated from rewards over repeated samples. They judge that "this RL-based approach suffers from training instability and low efficiency due to repeated sampling."[^c4] Their own method is described as needing no relevance labels: "our method is data free as it relies"[^c5] on the downstream next-token objective alone. The loss is described as "providing a weak supervision signal that naturally adapts retrieval to downstream"[^c6] generation.

What was measured. The headline claim is that "Experiments across multiple QA benchmarks show that CLaRa achieves state-of-the-art" [^c7] compression and reranking, "even at a text compression rate of 16."[^c8] The evaluation uses "four single-hop and multi-hop QA benchmarks with Mistral-7B and Phi-4B."[^c9] These are system-level numbers for the whole pipeline, and the parts of the paper read here do not isolate the retriever's share.

Why it should work, by the authors' account. The paper gives a gradient argument: the retriever is pushed to rank documents that support correct generation, and it receives representation-level feedback from the generator. The section is headed as a theoretical justification, and it opens by saying "We provide an explanation for why learning from NTP"[^c10] yields the training signal. It is an argument about the gradient path, not a bound on retrieval quality.

## Limits

- The signal is weak by the authors' own description (see the quote above). One answer's loss says little about which of many documents is the evidence, and the text read gives no measure of how often the top-k set contains the document that actually supports the answer.
- The document side does not move. Retrieval runs "over these frozen compressed vectors."[^c11] Only the query encoder adapts, so the ranking can change only through how queries are represented. This is a limit of the design, not a finding about what answer loss can do in general.
- "Data free" means no relevance labels, not no answers. The loss in the paper is over the reference output for each training question (my reading of the loss equation), so question–answer pairs are still needed.
- The straight-through estimator gives a biased gradient. The paper uses it because RL is unstable; the parts read do not analyse the bias, and do not compare the estimator with RL on the same tasks.
- The gradient argument is offered as an explanation. The parts read do not contain a proof that the learned ranking converges to answer utility, and I cannot say from them how the appendix's Algorithm 1 behaves beyond the stated formulas.
- All results are on QA benchmarks with two generator models. Whether the same training transfers to tasks without a short reference answer is not tested in the text read.

## Related

- [[question-elicited-salience-compression]] — the compressor that produces the frozen vectors this retriever ranks over; the same paper pretrains it on generated questions.
- [[generation-augmented-retrieval]] — expands the query with generated text scored against chunks; the retriever there is not trained on answer loss.
- [[prompted-versus-trained-query-augmentation]] — the split between prompted and trained query writers; the query encoder here is trained, but through the answer loss rather than a retrieval score.
- [[grounded-selective-pruning]] — filters retrieved knowledge by answer usefulness after retrieval, without changing the retriever.

[^c1]: arxiv-2511-18659 — "Retrievers select documents based on surface-level similarity"
[^c2]: arxiv-2511-18659 — "retriever why certain documents should be preferred over others"
[^c3]: arxiv-2511-18659 — "retrieval behavior during inference while allowing smooth gradient feedback during training"
[^c4]: arxiv-2511-18659 — "this RL-based approach suffers from training instability and low efficiency due to repeated sampling"
[^c5]: arxiv-2511-18659 — "our method is data free as it relies"
[^c6]: arxiv-2511-18659 — "providing a weak supervision signal that naturally adapts retrieval to downstream"
[^c7]: arxiv-2511-18659 — "Experiments across multiple QA benchmarks show that CLaRa achieves state-of-the-art"
[^c8]: arxiv-2511-18659 — "even at a text compression rate of 16"
[^c9]: arxiv-2511-18659 — "We evaluate CLaRa on four single-hop and multi-hop QA benchmarks with Mistral-7B and Phi-4B"
[^c10]: arxiv-2511-18659 — "We provide an explanation for why learning from NTP"
[^c11]: arxiv-2511-18659 — "By retrieving over these frozen compressed vectors"
