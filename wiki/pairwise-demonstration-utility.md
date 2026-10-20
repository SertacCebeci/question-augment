---
description: "A candidate example is scored by how much it lowers the task loss beyond the query alone, not by similarity; a selector trained on that gain learns which examples help."
aliases: ["counterfactual example gain", "loss-reduction reward for context selection", "task-aligned utility of a candidate", "helpfulness score for retrieved context"]
sources: ["arxiv-2512-00489"]
---
# Pairwise demonstration utility

Take a model and a query. Compute the task loss on the query alone, then the loss on the query with one candidate example attached. The candidate's utility is the drop between the two. A positive value means the example made the prediction better; a negative value means it made it worse. The score is defined per pair, so the same candidate can help one query and hurt another. The authors of Task-Aligned Context Selection (TACS) use exactly this quantity as their reward: "positive rewards indicate that the retrieved image improves task accuracy."[^c1]

The point of the measure is the gap it closes. Similarity-based retrieval ranks candidates by how close they sit to the query in an embedding space. The paper's objection is that this "implicitly assum[es] that perceptual similarity equates to usefulness."[^c2] The utility score does not ask how close the candidate is. It asks what happens to the prediction when the candidate is present. The authors state the ideal directly: a good selection should give "a lower task loss than using the query alone."[^c3]

The score becomes a learning signal through a policy. A selector network produces a softmax over the candidate pool, samples one candidate, and receives the utility as reward. The reward is standardized within each batch, "to reduce gradient variance and stabilize updates."[^c4] The task network is detached from this path: "Gradients are detached from the Task model so that policy updates depend solely on reward signals."[^c5] A second, differentiable path (straight-through Gumbel-Softmax on the task loss) runs alongside it, and the two share the selector's parameters. The policy path is the one that uses the pair score. The differentiable path does not evaluate whether the candidate helped; the paper says so: "it does not explicitly evaluate whether adding a retrieved image actually improves the downstream prediction."[^c6]

What the learned selector ends up optimizing is, in the authors' words, "the expected gain in downstream task performance if a retrieved candidate is paired with the query."[^c7] This is a different target from similarity. It is also, in my reading, a different target from label agreement or from a fixed heuristic, since the value is whatever the current task model does with the candidate (my inference).

## What the work measured

The evaluation covers 18 datasets: fine-grained natural-image classification, medical classification and medical segmentation. The headline result is that "TACS consistently outperforms similarity-based retrieval, particularly in challenging or data-limited settings."[^c8] In the ablation on the retrieval source, a fixed similar-image retriever "improves performance somewhat, but significantly less than task-aligned context selection."[^c9]

The controls show that the gain is not from extra tokens. An empty context image, or a duplicate of the query, "has the same effect as not providing a context image at all, a loss of approximately 2% performance."[^c10] The selected examples also differ from neighbours. The authors' attention analysis reports that the selector is "often choosing complementary rather than visually similar images."[^c11] This last claim rests on reading attention maps and is an interpretation, not a measured mechanism.

## Limits

- The score needs labels. The training loss is the task's cross-entropy, which the paper describes as the "downstream performance signals (e.g. cross-entropy loss)."[^c12] A utility computed per pair therefore needs a labelled target for each query. The text gives no label-free variant, so whether the measure survives without labels is not tested (my inference from the equation).
- The reward is a loss difference, while the headline claims are about accuracy. The paper speaks of examples chosen over those that "merely appear similar,"[^c14] but the reward is cross-entropy. Whether a lower loss always means a better decision is not checked in the parts I read (my inference).
- The score is for one candidate added to one query. Pairs are not combined: "Current limitations include the reliance on a fixed candidate pool and the use of a single retrieved example per query."[^c13] Nothing here says how the pair scores add up when several examples are attached, or how they behave with a larger pool.
- The tasks are discriminative vision: classifiers and segmenters, with ViT-type backbones. The claim does not extend to generation or language, and the paper does not test it there.
- The main comparison arm is one similarity retriever with frozen embeddings. The ablation I read does not compare the pair score against random candidates from the same pool, the arm that [[similarity-selected-exemplars]] treats as the real test of whether similarity does any work.
- The paper does not report whether the gain is stable across seeds in the parts I read, and the qualitative "helpful" reading is the authors' own.

## Related

- [[similarity-selected-exemplars]] — the baseline this score is set against; there, random and kNN selection are the arms, and similarity does not reliably win
- [[counterfactual-retrieval-information-gain]] — the same gain-over-a-baseline idea, applied to the documents of a search step as RL credit rather than to a candidate example
- [[situational-relevance]] — relevance defined by what helps the task, not by closeness to the query, in a personalization setting
- [[demonstration-label-consistency]] — another property of chosen demonstrations that similarity does not control

[^c1]: arxiv-2512-00489 — "positive rewards indicate that the retrieved image improves task accuracy"
[^c2]: arxiv-2512-00489 — "implicitly assuming that perceptual similarity equates to usefulness"
[^c3]: arxiv-2512-00489 — "indicating that the retrieved context yields a lower task loss than using the query alone"
[^c4]: arxiv-2512-00489 — "the standardized reward within each batch to reduce gradient variance and stabilize updates"
[^c5]: arxiv-2512-00489 — "Gradients are detached from the Task model so that policy updates depend solely on reward signals"
[^c6]: arxiv-2512-00489 — "it does not explicitly evaluate whether adding a retrieved image actually improves the downstream prediction"
[^c7]: arxiv-2512-00489 — "the expected gain in downstream task performance if a retrieved candidate is paired with the query"
[^c8]: arxiv-2512-00489 — "TACS consistently outperforms similarity-based retrieval, particularly in challenging or data-limited settings"
[^c9]: arxiv-2512-00489 — "Fixed similar image retrieval improves performance somewhat, but significantly less than task-aligned context selection"
[^c10]: arxiv-2512-00489 — "has the same effect as not providing a context image at all, a loss of approximately 2% performance"
[^c11]: arxiv-2512-00489 — "often choosing complementary rather than visually similar images"
[^c12]: arxiv-2512-00489 — "align its choices directly with downstream performance signals (e.g. cross-entropy loss)"
[^c13]: arxiv-2512-00489 — "Current limitations include the reliance on a fixed candidate pool and the use of a single retrieved example per query"
[^c14]: arxiv-2512-00489 — "rather than those that merely appear similar"
