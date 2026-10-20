---
description: "An answer's faithfulness can be scored without a reference: the minimal KL divergence between the topic shifts the question asks for and the shifts the answer makes, mapped to [0,1]."
aliases: ["semantic faithfulness", "SF score", "FS score", "question-answer topic-transition divergence"]
sources: ["arxiv-2512-05156"]
---
# Semantic faithfulness score

A question-context-answer triplet is written as distributions over a shared set of topics. The context has a topic distribution p(c). The question and the answer each arrive at a new topic distribution by a transition from that context. The paper writes the answer case as "pa = pTc A", where A is a row-stochastic matrix, and introduces a second matrix Q for the question, "consistent with the marginal distributions".[^c1] Both matrices are estimated from the triplet itself. The idea is that a faithful answer moves topics in the way the question points at: it should transform the topics of the context in a way that is semantically similar to how the question queries those same topics.[^c2]

The score is the minimum of a conditional [[kl-divergence]] between the two matrices, D(A‖Q), weighted by the context distribution and taken over all pairs of matrices that satisfy the marginal constraints. The score is defined "in terms of the minimal value of this KL divergence (4), obtained by" joint optimisation over A and Q.[^c3] With D_min that minimum, the score is FS = 1/(1 + D_min). It lies in (0, 1]. "Values of one are attained when the two probability distributions A and Q" coincide, which the paper reads as the answer producing the topical shifts the question implies. A small score marks an answer whose topical focus diverges from the question's.[^c4]

The minimisation is convex when the constraint sets are convex, so the minimum is unique. The paper computes it by alternating minimisation, "the AM method of Csiszar and Tusnády is known as the Blahut-Arimoto (BA) algorithm".[^c5] The topic space itself comes from a sentence-embedding model: "This is achieved using a pre-trained sentence embedding model", with the context and the answer treated as noisy observations of the LLM's internal state.[^c6] The method needs only the question, the context and the answer. "The black-box setting of our formulation implies that we do not have access to additional information" such as log-probabilities.[^c7] It is reference-free: the paper says "the SF metric FS is reference-free: it quantifies" alignment without a gold answer.[^c8] The paper also proposes sampling K paraphrases of the question and keeping the answer with the highest score, a use that the reference-free property makes possible.[^c9]

## What the transfer keeps and drops

The divergence and its minimum under marginal constraints come from information theory, and the paper's claim that the minimum is "a welldefined and unique quantity" rests on the Csiszár–Tusnády result.[^c10] That part survives the transfer. What does not survive is the reading of A and Q as causal topic flows. The matrices are fitted to whatever topic space the embedding produces, so the score inherits that space's granularity and noise. The paper gives no independent check that the fitted flows mean what the reading says. That is my inference from the method, not a result of the paper.

## What was measured

The experiments use 10 question-context-answer triplets, drawn from one risk-factor section of a single 10-K filing.[^c11] The two question groups have nearly the same mean score: "Both groups exhibit similar mean Semantic Faithfulness".[^c12] The abstract still names question structure as "the key driver of faithfulness variation".[^c13] Taken together, these two statements are in tension, and the within-group spread is the only support for the stronger reading. In a qualitative example, an LLM judge "rated two answers identically (9/10 across all criteria)", yet "The FS metric correctly assigned a lower score to the hallucinating answer".[^c14]

## Limits

- Ten triplets from one document, written by one author. The paper states that "Validation on larger and more diverse datasets remains an important direction for" future work.[^c15]
- The one hallucination example is a single case judged by eye. The slices I read contain no labelled hallucination benchmark and no human judgement of faithfulness against which FS is checked.
- FS measures alignment between topic transitions. It does not check whether a claim in the answer is true in the context. The paper describes it as preserving "query-relevant information in the answer".[^c16]
- The values depend on the embedding model; the paper's computations use "lightweight sentence transformers for embedding (e.g., Qwen3-Embedding-0.6B)".[^c17]
- The reading of a low score as "lack of faithfulness" is the paper's interpretation. The text does not establish the direction of the relation with human judgements.

## Related

- [[semantic-entropy-production]] — the same paper's second score, computed from the same transition matrices, but measuring irreversibility rather than alignment
- [[kl-divergence]] — the divergence that is minimised here; FS is a transform of its minimum under marginal constraints
- [[semantic-entropy]] — answer-only uncertainty; the paper argues that answer entropy alone is the wrong quantity
- [[supported-faithfulness-score]] — claim-level faithfulness against evidence, scored with a decomposer; not a topic-level divergence
- [[reference-less-source-alignment]] — another reference-free route, which aligns source and output triplets and counts missing and extra facts
- [[faithfulness-divergence]] — a different "faithfulness": confidence distributions against the truth, not topic transitions
- [[alpha-gameability-of-faithfulness-metrics]] — a caution for any faithfulness score that can be satisfied without a real dependence on the thing it claims to measure

[^c1]: arxiv-2512-05156 — "We can write such relation as pa = pTc A"
[^c2]: arxiv-2512-05156 — "should transform the topics from"
[^c3]: arxiv-2512-05156 — "defined in terms of the minimal value of this KL divergence (4), obtained by"
[^c4]: arxiv-2512-05156 — "Values of one are attained when the two probability distributions A and Q"
[^c5]: arxiv-2512-05156 — "the AM method of Csiszar and Tusnády is known as the Blahut-Arimoto (BA)"
[^c6]: arxiv-2512-05156 — "This is achieved using a pre-trained sentence embedding model"
[^c7]: arxiv-2512-05156 — "The black-box setting of our formulation implies that we do not have access to additional information"
[^c8]: arxiv-2512-05156 — "the SF metric FS is reference-free: it quantifies"
[^c9]: arxiv-2512-05156 — "we assume a more general setting where all questions Qk are constructed as semantically"
[^c10]: arxiv-2512-05156 — "is a welldefined and unique quantity"
[^c11]: arxiv-2512-05156 — "We validated the framework on 10 question-context-answer triplets"
[^c12]: arxiv-2512-05156 — "Both groups exhibit similar mean Semantic Faithfulness"
[^c13]: arxiv-2512-05156 — "with question structure, and not just entropy magnitude, emerging as the"
[^c14]: arxiv-2512-05156 — "The FS metric correctly assigned a lower score to the hallucinating answer"
[^c15]: arxiv-2512-05156 — "Validation on larger and more diverse datasets remains an important direction for"
[^c16]: arxiv-2512-05156 — "FS quantifies the preservation of"
[^c17]: arxiv-2512-05156 — "lightweight sentence transformers for embedding (e.g., Qwen3-Embedding-0.6B)"
