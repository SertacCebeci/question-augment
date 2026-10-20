---
description: "Distance between a model's answer distributions under two subgroups' phrasings, such as Jensen-Shannon or total variation, flags group-level disparity without ground-truth labels."
aliases: ["cross-group consistency", "cross-group response divergence", "group-conditioned answer divergence", "prompt fairness divergence"]
sources: ["arxiv-2511-19956"]
---
# Cross-group response divergence

Let P(Ŷ|g) be the distribution of the model's answers over all phrasings that subgroup g produces for a task, and P(Ŷ|g') the same for another group. The cross-group response divergence is the distance between the two: D(g, g') = d(P(Ŷ|g), P(Ŷ|g')). The distance d is left open; the paper states that "d(·, ·) can be instantiated as Jensen–Shannon divergence (JSD) or Total Variation (TV) distance."[^c1] Earlier, for the labelled setting, the same role is given to symmetric KL or TV.[^c2]

The quantity compares two marginals, not two answers. It does not ask whether one wording gets the same answer as another; it asks whether the answers a group's wordings produce are distributed like those of a different group. A value near zero means that, for this task, the model's output distribution does not depend on which group wrote the prompt. A large value means the same task gets systematically different treatment by group. The paper puts it as: "A large value of Dg,g′ indicates that the model produces systematically different responses for the same underlying task"[^c3]

Its purpose in the paper is to be usable without answers. When the task has no gold label, the group comparison is the only available fairness handle, and the paper says the metric measures "the sensitivity of model outputs to group identity, prompt phrasing," without requiring ground-truth labels.[^c4] To compute it, the answers are embedded, clustered, and each group's answers become a probability vector over the clusters: "we estimate a probability distribution pg over the discovered semantic clusters"[^c5] The divergence is then taken between these vectors. JSD and symmetric KL are built from the same KL building block (JSD is the average of two KL divergences to the mixture), so the choice between them changes the scale and the handling of zero cells, not the idea.

On the unlabelled BOLD prompts, the paper reports pre-mitigation cross-group divergences that "reach 0.28 and typically fall in the 0.14–0.22 range," and after neutralization and multi-generation a largest gap reduced "to 0.22 and many distances falling to 0.17 or below."[^c6] For the labelled Adult task, the Figure 3 text gives a maximum of "as high as 0.16" before mitigation.[^c7] On the BOLD matrices the paper says that after mitigation "the magnitude of these cross-group gaps decreases across most pairs."[^c8]

## Limits

- The abstract's 0.28 and the Figure 3 text's 0.16 are not the same quantity. The Figure 3 caption gives symmetric KL on Adult; the abstract does not say which metric or dataset its 0.28 refers to. A reader should not compare the two numbers as if they measured one thing.
- The partition is chosen by the method. Clustering uses "kmeans (k = 4, ninit = 50)"[^c9] over embeddings from one model, and the divergence is a function of that partition. The paper averages over five k-means initializations,[^c10] which addresses the seed but not the choice of k or of the embedding model.
- A zero divergence does not show that the answers are right. On unlabelled tasks, two groups can receive the same wrong answer and the metric reports no disparity. This is my inference from the definition, since the paper gives no accuracy for the BOLD setting.
- The BOLD prompts are not stylistic rewrites: the paper says they "explicitly encode demographic information."[^c11] What the divergence picks up there is partly the presence of a demographic term in the text, which the neutralization removes by design. It is not the same measurement as the rephrased-style one on Adult.
- Each group has five rephrasings per base prompt, from one paraphrasing model, and the results are for one answer model. The sizes of the divergences depend on these choices and are not shown to transfer.
- The text does not report confidence intervals for the divergence values, so a reduction from 0.22 to 0.17 cannot be read as established in size.

## Related

- [[subgroup-sensitivity]] — the within-group term: the answer spread inside one group's phrasing family. The paper defines it separately from the divergence.
- [[demographic-conditioned-mirage]] — demographic descriptors shaping output instead of evidence; the same cue family, seen from the output side.
- [[identity-neutral-query-rewriting]] — removing identity cues before generation, the kind of intervention whose effect this divergence is used to measure.
- [[kl-divergence]] — the building block of the symmetric KL instance and of JSD.
- [[paraphrase-group-hallucination-dispersion]] — spread across paraphrase groups on a single item; this note compares groups of prompts across the whole task.

[^c1]: arxiv-2511-19956 — "where d(·, ·) can be instantiated as Jensen–Shannon divergence (JSD) or Total Variation (TV) distance"
[^c2]: arxiv-2511-19956 — "instantiated as symmetric KL or Total Variation (TV) distance"
[^c3]: arxiv-2511-19956 — "systematically different responses for the same underlying task"
[^c4]: arxiv-2511-19956 — "without requiring ground-truth labels by measuring the sensitivity of model outputs to group identity, prompt phrasing,"
[^c5]: arxiv-2511-19956 — "over the discovered semantic clusters"
[^c6]: arxiv-2511-19956 — "divergence values reach 0.28 and typically fall in the 0.14–0.22"
[^c7]: arxiv-2511-19956 — "where divergence values reach as high as 0.16"
[^c8]: arxiv-2511-19956 — "the magnitude of these cross-group gaps decreases across most"
[^c9]: arxiv-2511-19956 — "All embeddings are jointly clustered via kmeans (k = 4, ninit = 50)"
[^c10]: arxiv-2511-19956 — "average results across five random initializations of k-means"
[^c11]: arxiv-2511-19956 — "explicitly encode demographic information"
