---
description: "Prompt ensemble voting: the answers of several separately worded, well-scoring prompts are combined by a weighted vote, so no single wording or generation path decides the label."
aliases: ["ensemble voting over prompts", "weighted prompt voting", "prompt ensembling", "ensemble learning based prompt optimization voting"]
sources: ["arxiv-2511-16122"]
---
# Prompt ensemble voting

A single prompt is one draw from a very large space of wordings, and its answer carries whatever that wording happens to favour. Prompt ensemble voting keeps a pool of prompts that each score well on the task, asks every member the same question, and returns the label with the largest weighted share of the votes. The ELPO paper writes the rule as a weighted argmax: "Formally, given M ensemble members, the final prediction" is the label y that maximises the sum, over members j, of w_j times an indicator that member j predicts y.[^c12]

The reason given for pooling is that each prompt carries its own bias. "Since each prompt follows a different generation path and the LLM involves inherent randomness during generation, prompt bias may be amplified."[^c3] Voting is the device for averaging that bias out. The paper asks for a pool that is varied on purpose: an ensemble voting strategy "aggregates multiple well-performing yet structurally diverse candidate prompts."[^c2] So the two conditions are that each member is good on a development set and that the members differ in how they were written.

The votes are not equal. "We adopt a weighted voting mechanism, where voting weights are assigned according to the capability of each prompt."[^c4] The weights are fitted, not set by hand: a macro-F1 objective on the labelled data, a penalty "a regularization coefficient designed to ensure balanced weight allocation"[^c5], and a floor on each weight, since "wmin > 0 is a pre-given constant as a weight threshold."[^c14] The pool itself is not fixed either. "During each iteration, the ensemble pool is automatically updated based on the latest evaluation results"[^c11], so membership changes as the search runs.

## What was measured

The ablation in the paper has three rows: no vote, an average vote over the selected prompts, and the weighted vote. "using an average strategy to vote on the selected prompts can slightly improve accuracy"[^c6], and "applying a weighted voting strategy can further enhance model performance."[^c7] The same section also varies the generators that produce the pool. "increasing the diversity of generators leads to a significant improvement in F1 score on these datasets"[^c8], and with that expansion in place "the ensemble framework strategy can further enhance model performance."[^c15] So in the paper's own account, the vote is a refinement on top of a more varied pool, not the main source of the gain.

The transferable point is about the answer, not the optimiser. A label that several differently phrased prompts agree on depends less on any one phrasing, and a weight that reflects each prompt's measured reliability keeps weak phrasings from counting as much as strong ones. What does not transfer from this text is the claim that a particular optimiser builds the pool; the vote needs only some set of prompts that each have a score.

## Limits

- **The vote needs a label set.** The rule is an argmax over a set Y. The datasets are true/false, multiple-choice and integer-answer tasks: "GSM8K includes questions that require integer answers"[^c13]. For free-form answers, this text gives no aggregation rule; comparing strings or asking a judge would be a further step that is not tested here (my inference).
- **Diversity is asserted, not measured.** "Structurally diverse" is the paper's term and is not a variable in its ablations. The generator ablation shows that more generators help, which is not the same as showing that more structurally different prompts help.
- **Correlated members would add little.** If the members are wordings of one template, their votes agree and the ensemble reduces to one prompt. This is my inference from the stated motivation, not something the paper tests. The related note on prompt invariance reports tight clustering of performance across structurally different prompts, which points the same way.
- **The weights are fitted on the data they are judged by.** The penalty is the paper's guard against overfitting. The slices read give no held-out test of the weights, so the weighted gain may be partly an in-sample effect (my inference).
- **The ablation gains have no spread in the text read.** The gains in the voting table are reported without seeds or intervals in the parts read, and the table's column labels are not in the extracted text. The ordering "average, then weighted" is the paper's own description.
- **The pool inherits the search's weakness.** The paper concedes that "the search strategy does not always guarantee that the best prompts will be selected from the candidates."[^c10] It also says the search is "not sufficiently robust."[^c9] A vote over a poor pool is still a vote over a poor pool.
- **Cost at answer time.** Every answer needs one call per member. The paper's cost comparison is about the optimisation, and the answer-time cost of M members is not reported in the parts read (my inference).

## Related

- [[evolutionary-prompt-search]] — produces a population of wordings and keeps the single best on a dev score; a voting pool keeps several, and weights them instead of choosing one.
- [[bayesian-prompt-optimization]] — uses a surrogate to choose which prompt to try next; in the ELPO paper the surrogate screens candidates before evaluation, which is a separate step from the vote.
- [[prompt-variant-augmentation]] — gives robustness to wording during training by showing several renderings; the vote gives a similar robustness at answer time, across prompts rather than in the weights.
- [[model-prompt-matching-bias]] — combines multiple prompts and different readers as a response to a prompt that fits one reader poorly.
- [[cot-prompt-invariance]] — the invariance result that bears on whether votes over different prompts disagree at all.

[^c2]: arxiv-2511-16122 — "aggregates multiple well-performing yet structurally diverse candidate prompts"
[^c3]: arxiv-2511-16122 — "Since each prompt follows a different generation path and the LLM involves inherent randomness during generation, prompt bias may be amplified"
[^c4]: arxiv-2511-16122 — "We adopt a weighted voting mechanism, where voting weights are assigned according to the capability of each prompt"
[^c5]: arxiv-2511-16122 — "a regularization coefficient designed to ensure balanced weight allocation"
[^c6]: arxiv-2511-16122 — "using an average strategy to vote on the selected prompts can slightly improve accuracy"
[^c7]: arxiv-2511-16122 — "applying a weighted voting strategy can further enhance model performance"
[^c8]: arxiv-2511-16122 — "increasing the diversity of generators leads to a significant improvement in F1 score on these datasets"
[^c9]: arxiv-2511-16122 — "Secondly, our search strategy is not sufficiently robust."
[^c10]: arxiv-2511-16122 — "the search strategy does not always guarantee that the best prompts will be selected from the candidates."
[^c11]: arxiv-2511-16122 — "During each iteration, the ensemble pool is automatically updated based on the latest evaluation results"
[^c12]: arxiv-2511-16122 — "Formally, given M ensemble members, the final prediction"
[^c13]: arxiv-2511-16122 — "GSM8K includes questions that require integer answers"
[^c14]: arxiv-2511-16122 — "wmin > 0 is a pre-given constant as a weight threshold"
[^c15]: arxiv-2511-16122 — "the ensemble framework strategy can further enhance model performance"
