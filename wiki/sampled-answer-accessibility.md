---
description: "A question's accessibility is how often its correct answer appears among stochastic samples from the base model; RL repair rates rise with it, and a zero count is not proof of absence."
aliases: ["pre-RL accessibility", "answer accessibility", "sample-frequency accessibility", "accessibility at k"]
sources: ["doi-10-48550-arxiv-2605-07153"]
---
# Sampled answer accessibility

Draw a fixed number of independent answers from a model to one closed-book question, under the decoding it will be trained or tested with, and count how many are judged correct. In this paper the sample is 128 draws, and the count is what the authors call pre-RL accessibility: "we measure pre-RL accessibility as the fraction of the correct" answer among those draws.[^a1] The measure is about the output distribution. It asks how readily a fact comes out of the model as text. It does not ask whether the model stores the fact.

The count matters because greedy decoding returns one answer and hides how close a failed answer was. Among questions the base model gets wrong under greedy decoding, the chance that RL later fixes one rises with the count. Partially accessible answers (9 to 16 correct samples out of 128) are repaired at about 52%,[^a2] and highly accessible ones at about 84%.[^a3] Where the correct answer never appears in the 128 samples, RL still lifts the fact to greedy output in 6 to 13% of cases.[^a4] Repair here means that "the post-RL model successfully answers via greedy decoding" on held-out test questions.[^a5]

Pass@k gives the same picture from the other side. Pass@k counts a question as solved "if the correct answer appears within the first k independent samples."[^a6] After RL, post-RL accuracy at k = 1 or 2 matches what the base model needs k = 16 or 32 to reach.[^a7] As k grows toward 256 the two curves nearly meet, and "the pre-RL model can usually reach the facts that RL unlocks."[^a8] The paper's reading is that RL "primarily redistributes probability mass over existing knowledge rather than acquiring new facts," moving correct answers "from the low-probability tail into reliable greedy generations."[^a9][^a10]

So accessibility sorts questions into three positions. A high count means the answer is already near the top of the distribution, and RL moves it to greedy decoding with little trouble. A low but nonzero count means the answer sits in the tail, and RL raises it into greedy range. A zero count is the hard case. The paper reads it as a fact that is "encoded but deeply suppressed, not absent."[^a12] It also says that zero observed hits "should not be taken as proof that the corresponding fact" is absent from the model.[^a11]

The count is a Monte Carlo estimate of a per-question probability. A count of 1 or 2 out of 128 is hard to tell from noise, and the paper leaves that bin out of its training comparison for this reason: "to distinguish from random sampling noise."[^a16] A zero count has the same problem at the other end: it does not separate probability zero from a probability near 1/128.

## Limits

- The count is a proxy by the authors' own statement: "This metric is not intended to prove whether a fact is stored".[^a13] It is "a practical proxy for how readily a fact can be elicited from the" output distribution.[^a14]
- The count depends on the sampling setup. The samples are "drawn using the same hyperparameters as the RL rollout phase."[^a15] A different temperature or decoder would give different counts, and so would a different verifier. The paper uses an LLM judge instead of exact match because exact match yields "reward sparsity and yielding only marginal gains."[^a17] Whether the count shifts under exact match is my inference, not something the paper tests on the count itself.
- Scope is zero-shot, one-hop, closed-book, non-chain-of-thought factual QA. The larger-model checks, up to 72B and a mixture-of-experts model, are on NQ only: "on the NQ dataset. As presented".[^a18]
- The claim that RL adds no new facts rests on a finite budget. The convergence at k = 256 is an observation on the test set, not a bound on what the model stores. That the zero-count facts are recoverable in "6 to 13%" of cases is also one dataset's number. (My inference.)
- The note does not establish that the count predicts difficulty or answer quality for tasks that are not factual recall, such as reasoning or open-ended generation. The paper does not test this.

## Related

- [[edge-of-competence-selection]] — the pass@k reading of the same kind of curve; its zero-coverage claim meets a counterexample in factual RL.
- [[rare-correct-rollout-reinforcement]] — what training does with questions whose count is near zero.
- [[candidate-selection-gap]] — the same caution about pass@K gaps: a large K can hit a correct answer by chance.
- [[parametric-suppression]] — another case of a correct answer present in the model but not at the output; there it is found in intermediate layers, here by sampling frequency.

[^a1]: doi-10-48550-arxiv-2605-07153 — "we measure pre-RL accessibility as the fraction of the correct"
[^a2]: doi-10-48550-arxiv-2605-07153 — "correct samples) are repaired at ∼52%"
[^a3]: doi-10-48550-arxiv-2605-07153 — "highly accessible answers (≥65/128) at ∼84%"
[^a4]: doi-10-48550-arxiv-2605-07153 — "RL successfully elevates the fact to the greedy decoding output at a"
[^a5]: doi-10-48550-arxiv-2605-07153 — "the post-RL model successfully answers via greedy decoding"
[^a6]: doi-10-48550-arxiv-2605-07153 — "if the correct answer appears within the first k independent samples."
[^a7]: doi-10-48550-arxiv-2605-07153 — "model requires k = 16 or k = 32 to achieve, indicating that RL turns a large sampling budget into"
[^a8]: doi-10-48550-arxiv-2605-07153 — "k = 256, the pre-RL model can usually reach the facts that RL unlocks."
[^a9]: doi-10-48550-arxiv-2605-07153 — "RL primarily redistributes probability mass over existing knowledge rather than"
[^a10]: doi-10-48550-arxiv-2605-07153 — "moving correct answers from the low-probability tail into"
[^a11]: doi-10-48550-arxiv-2605-07153 — "should not be taken as proof that the corresponding fact"
[^a12]: doi-10-48550-arxiv-2605-07153 — "suggesting that some of these facts are encoded but deeply suppressed, not absent"
[^a13]: doi-10-48550-arxiv-2605-07153 — "This metric is not intended to prove whether a fact is stored"
[^a14]: doi-10-48550-arxiv-2605-07153 — "to provide a practical proxy for how readily a fact can be elicited from the"
[^a15]: doi-10-48550-arxiv-2605-07153 — "hyperparameters as the RL rollout phase."
[^a16]: doi-10-48550-arxiv-2605-07153 — "to distinguish from random sampling noise"
[^a17]: doi-10-48550-arxiv-2605-07153 — "causing reward sparsity and yielding only marginal gains"
[^a18]: doi-10-48550-arxiv-2605-07153 — "on the NQ dataset. As presented"
