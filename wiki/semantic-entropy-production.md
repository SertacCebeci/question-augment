---
description: "Entropy production in answer generation, read as a KL cost of the context-to-answer transition; its lower bound (SEP) is argued to track answer quality better than answer entropy alone."
aliases: ["SEP", "semantic entropy production", "entropy production of LLM answer generation", "dissipated entropy of text generation"]
sources: ["arxiv-2512-05156"]
---
# Semantic entropy production

The second score in Halperin's paper reuses the transition matrices of the [[semantic-faithfulness-score]] and reads the context-to-answer step as a non-equilibrium process. In stochastic thermodynamics, "total entropy production for a stochastic system is given by the KL" divergence between the probabilities of a forward path and of its time-reversed path.[^p1] In the one-step setting the total splits into the change in the entropy of the system, H(A) − H(C) in topic terms, and a dissipated term: the paper's dissipated term "represents dissipated heat from subsystem X" to the rest of the model and the environment.[^p2]

The paper uses the first term as a better measure of answer entropy than the entropy of the answer by itself. "The present work suggests that it is entropy production, rather than" the marginal entropy of the answer, that quantifies uncertainty about an answer.[^p3] The reason given is that the system entropy change "appears a more meaningful way to quantify entropy of the LLM answer by computing its difference with" the entropy of the context.[^p4] This is the reverse of [[semantic-entropy]], which scores the answer's dispersion alone.

The total cannot be computed directly, because the reverse transition matrix is never observed. The paper takes a bound instead: "we can find a lower bound on entropy production in our process by minimizing the expression" over all reverse matrices that satisfy the marginal constraints.[^p5] The result is the SEP score. It is solved as a dual problem, and the paper reports that both optimisations converge for every triplet.

## Relation to the faithfulness score

When the correction term in the bound is negligible, SEP reduces to a function of FS: "When the correction term (the sum) is negligible, this yields the" approximation SEP ≈ 1/FS − 1.[^p6] The paper then tests this on 100 synthetic triplets and finds the relation weaker: "However, the relationship is weaker than the naive approximation".[^p7] Its recommendation follows: "We therefore recommend computing both metrics independently".[^p8] So SEP is related to FS but not a function of it.

On the 10 real triplets, "Group A exhibits higher SEP" than Group B, matching its larger entropy change.[^p9] The correlation between FS and SEP is reported as r = −0.612 with p = 0.060, which is weak evidence.[^p10] For nine of the ten triplets the dissipated term is negative: "in all triplets except A0, we observe SEP" below the entropy change.[^p11] The paper reads this as the LLM drawing on its internal knowledge: "The physical interpretation is that to generate answers with higher entropy than" the context.[^p12] That reading is the paper's, and nothing in the slices I read tests it.

## What the transfer keeps and drops

The decomposition of a total into a system term and a dissipated term is an identity for any stochastic process with a known reverse dynamics. That part survives the transfer to a discrete topic chain. The physics does not survive in the same form. The "Maxwell demon" is the hidden layers, which the paper calls "unobserved sub-systems of information engines", a label borrowed from thermodynamics.[^p13] Heat, temperature and the bath play no measured role in the computation; the quantity is a KL divergence between matrices. What is left is a lower bound on an unobserved quantity, with the physical interpretation attached afterwards.

## Limits

- Ten triplets from one filing, and one author. The paper states that "Validation on larger and more diverse datasets remains an important direction for" future work.[^p14]
- The SEP–FS relation is moderate overall, and the within-group pattern is inconsistent: Group B "shows no significant within-group correlation".[^p15]
- SEP is a lower bound. The exact entropy production needs the unobserved reverse matrix, so the reported SEP values can understate it, and the sign of the dissipated term is not settled by the bound.
- The paper's case for SEP over semantic entropy is an argument plus a group comparison. Its hallucination example is scored by FS, not SEP: "The FS metric correctly assigned a lower score to the hallucinating answer".[^p16] The slices I read contain no run that compares SEP and semantic entropy on the same labelled answers.
- The topic space comes from a sentence-embedding model, and the entropies are only as fine as that space.[^p17] Changing the embedding changes both the entropy change and the bound.

## Related

- [[semantic-faithfulness-score]] — the alignment score from the same transition matrices; SEP is a separate measure of irreversibility, not its inverse
- [[semantic-entropy]] — dispersion of an answer's meanings alone; SEP is argued to replace it by the change relative to the context
- [[entropy]] — the entropy change H(A) − H(C) is a difference of two Shannon entropies
- [[kl-divergence]] — the total entropy production is a KL divergence between a path and its reverse
- [[question-scoped-evidence-proxy]] — another reference-free evaluation that depends on how the question scopes the evidence

[^p1]: arxiv-2512-05156 — "total entropy production for a stochastic system is given by the KL"
[^p2]: arxiv-2512-05156 — "S m represents dissipated heat from subsystem X"
[^p3]: arxiv-2512-05156 — "the present work suggests that it is entropy production, rather than"
[^p4]: arxiv-2512-05156 — "appears a more meaningful way to quantify entropy of the LLM answer by computing its difference with"
[^p5]: arxiv-2512-05156 — "we can find a lower bound on entropy production in our process by minimizing the expression"
[^p6]: arxiv-2512-05156 — "When the correction term (the sum) is negligible, this yields the"
[^p7]: arxiv-2512-05156 — "However, the relationship is weaker than the naive approximation"
[^p8]: arxiv-2512-05156 — "We therefore recommend computing both metrics independently"
[^p9]: arxiv-2512-05156 — "Group A exhibits higher SEP"
[^p10]: arxiv-2512-05156 — "The correlation between FS and SEP is r"
[^p11]: arxiv-2512-05156 — "in all triplets except A0, we observe SEP"
[^p12]: arxiv-2512-05156 — "The physical interpretation is that to generate answers with higher entropy than"
[^p13]: arxiv-2512-05156 — "such unobserved sub-systems of information engines are often referred to"
[^p14]: arxiv-2512-05156 — "Validation on larger and more diverse datasets remains an important direction for"
[^p15]: arxiv-2512-05156 — "shows no significant within-group correlation"
[^p16]: arxiv-2512-05156 — "The FS metric correctly assigned a lower score to the hallucinating answer"
[^p17]: arxiv-2512-05156 — "lightweight sentence transformers for embedding (e.g., Qwen3-Embedding-0.6B)"
