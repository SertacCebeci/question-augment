---
description: "Measured as the change in probed-answer quality between adjacent iterations, most agentic RAG iterations change nothing, and the few decisive ones mostly come early in the trajectory."
aliases: ["partial utility", "decisive iteration", "iteration-level utility", "per-iteration answer utility"]
sources: ["doi-10-48550-arxiv-2609-16453"]
---
# Decisive iteration sparsity

An agentic RAG loop can add retrieval steps that change its answer, help it, hurt it, or do nothing. Partial utility measures which: it is the change in partial answer quality from one probing point to the next, so that positive, negative and near-zero values mean improvement, degradation and negligible change.[^c1] It is only defined where the probe of [[in-trajectory-answer-probing]] is available, so it is a measurement of the trajectory after the fact.

On two RL-trained pipelines the distribution of partial utility is strongly peaked at zero. The paper describes it as "around zero, indicating that most iterations do not substantially" change the probed answer, and states that "the majority of iterations contribute zero utility" while only a smaller share cause a clear change.[^c2] The same distribution has two tails, so the paper reads the result as showing that "retrieval reasoning iterations can be either beneficial or harmful."[^c3]

The name of the note comes from the paper's word for the few non-zero steps. Partial utility is "sparsely distributed across iterations", and the decisive ones are the iterations that move the answer.[^c4] The paper also says these decisive iterations "often occur early" in the trajectory.[^c5] Trajectories are grouped by net utility, and the grouping shows the shape: positive-utility trajectories "generally improve rapidly in the early iterations and" then plateau.[^c6] Negative-utility trajectories "drop sharply in early iterations", and the later steps "usually fail to recover the lost quality".[^c7][^c8] The paper reads this as "a mismatch between" the model's stopping behaviour and its intermediate answer quality, which is the motivation for predicting partial utility.[^c9]

Partial answer quality is easier to predict than partial utility. The abstract's claim is that "partial answer quality is more predictable than partial utility", so the change is the harder target even though the level is easier.[^c10]

## Limits

The sparsity figure pools the trajectories of three datasets. It is drawn "on the merged development sets of the three datasets," and the paper does not show a per-dataset split in the parts read.[^c11] Only the basic loop was measured. The paper chose this setting "without the additional complexity introduced by modules such as self-reflection, document refinement or path selection," so the sparsity is not shown for loops with those modules.[^c12]

A zero utility does not say why nothing changed. The retriever may have returned nothing new, or the model may have read it and ignored it; the probe does not separate these (my inference). Utility is also a difference of two F1 scores, each from one greedy answer. A zero can hide a change in wording that F1 scores the same, and a non-zero can come from answer variance that the paper does not estimate (my inference).

Partial utility is a realized change after an iteration. It is not an expected value of a query made before it is run, which is the sense of [[value-of-information]]; the two share a marginal-gain shape but not the timing (my reading).

## Related

- [[in-trajectory-answer-probing]] — the probe whose differences between adjacent steps this note calls partial utility.
- [[value-of-information]] — the expected worth of a query before it is run; partial utility is the realized change after an iteration (my reading).
- [[stop-continue-criteria-in-retrieval-loops]] — the stop decision that a utility signal would inform, and the family the paper's early stopping belongs to.

[^c1]: doi-10-48550-arxiv-2609-16453 — "in partial answer quality relative to the preceding probing point"
[^c2]: doi-10-48550-arxiv-2609-16453 — "around zero, indicating that most iterations do not substantially"
[^c3]: doi-10-48550-arxiv-2609-16453 — "retrieval reasoning iterations can be either beneficial or harmful"
[^c4]: doi-10-48550-arxiv-2609-16453 — "partial utility is sparsely distributed across iterations"
[^c5]: doi-10-48550-arxiv-2609-16453 — "and often occur early"
[^c6]: doi-10-48550-arxiv-2609-16453 — "Positive-utility trajectories generally improve rapidly in the early iterations and"
[^c7]: doi-10-48550-arxiv-2609-16453 — "For negative-utility trajectories, partial answer quality often drops sharply in early iterations"
[^c8]: doi-10-48550-arxiv-2609-16453 — "later iterations usually fail to recover the lost quality"
[^c9]: doi-10-48550-arxiv-2609-16453 — "This suggests a mismatch between"
[^c10]: doi-10-48550-arxiv-2609-16453 — "partial answer quality is more predictable than partial utility"
[^c11]: doi-10-48550-arxiv-2609-16453 — "on the merged development sets of the three datasets"
[^c12]: doi-10-48550-arxiv-2609-16453 — "without the additional complexity introduced by modules such as self-reflection, document refinement or path selection"
