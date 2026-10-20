---
description: "Removing parts of an input to test an explanation pushes it out of distribution; the shift confounds the subgraph-prediction link, so removal-based explanation scores mislead."
aliases: ["feature removal evaluation", "removal-based explanation evaluation", "removal-based evaluator", "OOD effect in explanation evaluation"]
sources: ["doi-10-48550-arxiv-2201-08802"]
---
# Out-of-distribution confounded removal evaluation

To test whether a part of an input explains a model's output, a common check removes the rest, feeds the remaining part to the same model, and scores the part by how much of the prediction it still supports. For explanatory subgraphs of graph neural networks (GNNs) this is the feature removal principle: the subgraph is fed to the predictor alone, and its importance is read off the subgraph-prediction correlation.[^c1] The check looks like a measurement. The claim of this work is that the removal step changes what is being measured.

Removal moves the input off the data distribution. Dropping edges or nodes can break the regularities that every training graph obeys: "hence, simply removing some bonds (edges) or atoms (nodes) creates invalid molecular subgraphs" that never occur in the training set.[^c2] The model is then queried on inputs it has never seen, and its output on them need not reflect what the kept part contains.

The paper's causal reading turns this into a confound. The distribution shift D is an unobserved variable upstream of both the subgraph and the prediction, so the path Gs ← D → Y is open: "distribution shift D opens the spurious path Gs ← D → Y".[^c3] A subgraph-prediction correlation measured on removal then mixes what the subgraph says with what the shift does. In the abstract's words, "OOD effect acts as the confounder, which brings spurious associations between the" subgraph importance and the model prediction.[^c4]

A concrete case from the paper's Figure 1a: a trained predictor classified a full graph as "House". The ground-truth explanation subgraph gave that class a probability "surprisingly low (0.21)".[^c5] For a subgraph "with less discriminative information" the probability was 0.70.[^c11] The paper concludes that "Clearly, the removal-based evaluator assigns the OOD subgraphs" importance scores that are unreliable.[^c6]

Across the benchmarks the pattern is broader. Without in-filling, on two synthetic motif datasets the ground-truth subgraphs reached only "ground-truth subgraphs only reaches 43.8% and 40.8%" of the importance of the full graph.[^c7] Comparing explainers, the paper reports that the precision of a subgraph against the ground truth "is negatively correlated with the importance" in most cases.[^c8] The proposed mechanism is that "discarding a part of a graph could violate some underlying properties of graphs and mislead the" target GNN, a mechanism the paper ties to adversarial attack work on graphs.[^c9] Explainers built for high prediction accuracy are hit hardest: they are "easily distracted by the OOD effect and thus miss the important subgraphs".[^c10]

What survives the move to other domains (my inference, not tested in the paper): the structural point. A score computed on an input whose ablation leaves the distribution the model was trained on cannot by itself be read as the contribution of the kept part, whatever the domain. What does not transfer is the specific constraint, valency rules or degree distributions, and nothing here shows that a language model given a truncated or masked context is confounded in the same way.

## Limits

- The evidence is two synthetic motif datasets with known ground truth, plus a sentiment-graph dataset with no ground truth. Negative correlation in most cases is not negative correlation in all cases.
- The confound is a causal assumption. D is never measured, and the structural causal model is taken as given. The data show a correlation pattern consistent with the OOD story; they do not isolate D as its cause.
- Precision against the ground-truth subgraph is the yardstick for "faithful" here. If the ground-truth explanation is itself a poor account of the model, the yardstick is wrong too.
- The main text analyses insertion-based evaluation; deletion is deferred to an appendix.[^c12]
- The note records that removal scores disagreed with ground truth on these datasets. It does not show that removal is worse than every alternative in practice, and it proposes no fix; the fix is a separate note.

## Related

- [[front-door-adjustment]] — the identification route that estimates a subgraph's effect despite the unmeasured shift this note describes
- [[causal-model-of-explanation]] — explanation as giving causes; the removal confound is a failure to separate a subgraph's causal role from a shift that moves both it and the output
- [[alpha-gameability-of-faithfulness-metrics]] — a parallel worry: an intervention-based faithfulness score can look satisfied without a real dependence between explanation and intervention effect (my inference from that note's description)
- [[counterfactual-explanation]] — also varies the input to test an explanation, but to nearby valid cases; removal leaves the distribution, which is the failure mode here (my inference)

[^c1]: doi-10-48550-arxiv-2201-08802 — "the current evaluation frameworks use the feature removal"
[^c2]: doi-10-48550-arxiv-2201-08802 — "hence, simply removing some bonds (edges) or atoms (nodes) creates invalid molecular subgraphs"
[^c3]: doi-10-48550-arxiv-2201-08802 — "distribution shift D opens the spurious path"
[^c4]: doi-10-48550-arxiv-2201-08802 — "OOD effect acts as the confounder, which brings spurious associations between the"
[^c5]: doi-10-48550-arxiv-2201-08802 — "surprisingly low (0.21)"
[^c6]: doi-10-48550-arxiv-2201-08802 — "Clearly, the removal-based evaluator assigns the OOD subgraphs"
[^c7]: doi-10-48550-arxiv-2201-08802 — "ground-truth subgraphs only reaches 43.8% and 40.8%"
[^c8]: doi-10-48550-arxiv-2201-08802 — "is negatively correlated with the importance"
[^c9]: doi-10-48550-arxiv-2201-08802 — "discarding a part of a graph could violate some underlying properties of graphs and mislead the"
[^c10]: doi-10-48550-arxiv-2201-08802 — "easily distracted by the OOD effect and thus miss the important subgraphs"
[^c11]: doi-10-48550-arxiv-2201-08802 — "with less discriminative information"
[^c12]: doi-10-48550-arxiv-2201-08802 — "We focus on insertion-based evaluation here while we discuss deletion-based evaluation in Appendix C."
