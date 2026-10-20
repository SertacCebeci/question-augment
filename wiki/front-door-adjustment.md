---
description: "Front-door adjustment estimates a subgraph's effect via a generated in-distribution surrogate, so an unmeasured shift needn't be blocked; it raised GNN precision-importance correlation."
aliases: ["front-door criterion", "front-door deconfounding", "Deconfounded Subgraph Evaluation", "mediator-based adjustment"]
sources: ["doi-10-48550-arxiv-2201-08802"]
---
# Front-door adjustment

When a cause X and an outcome Y share a confounder that cannot be measured, the usual remedy, backdoor adjustment, is unavailable: it needs the confounder in hand. Pearl's front-door adjustment works without it, provided the effect of X on Y runs through a mediator M that carries all of that effect and whose link from X is not confounded with Y. The effect of X on Y is then recovered by chaining two estimable pieces, X to M and M to Y, and averaging over M.

The paper applies this to explanation evaluation. The cause is the explanatory subgraph Gs, the outcome is the model's prediction Y, and the confounder is the distribution shift D, which the authors call "hardly measurable".[^c1] With D unavailable the backdoor route is closed: "Hence, the causal effect of Gs on Y is not identifiable from SCM I."[^c2]

The mediator is a surrogate G*s. It "is the surrogate variable of Gs , which completes Gs to make them in the data".[^c3] Three properties are asked of it. It keeps the subgraph: it "originates from and contains Gs".[^c4] It is in-distribution: it "should follow the data distribution", so the predictor is queried on plausible graphs.[^c5] And it blocks the shift: "thus no link exists between D and G∗s", so the shift cannot reach the mediator.[^c6] The identifying assumption is the last one, together with the claim that the causal information of Gs on Y survives the completion: it "is well-preserved by G∗s".[^c7]

The estimator chains the two pieces. The conditional distribution from Gs to the surrogate is learned from data; the surrogate-to-prediction piece is obtained by "feeding the surrogate graph Gs∗ into the GNN predictor", conditioned on the subgraph.[^c8] The authors write the effect as a sum over surrogates, "we chain two identifiable partial effects of Gs on G∗s and G∗s on Y together".[^c9] The hard step is producing the surrogates at all: "it is non-trivial to instantiate Gs∗ and collect the (Gs , Gs∗ ) pairs", so they train a conditional variational graph auto-encoder (CVGAE) with an adversarial objective.[^c10]

The effect on evaluation is the point. Scored by the surrogate-based effect rather than by removal, the correlation between explanation precision and importance improves: "Substantially, ρdse greatly improves after the frontdoor adjustments via the surrogate variable."[^c11] The largest case is GNNExplainer on MNISTsup, where the correlation rises from negative to 0.17.[^c12] Among generators, the CVGAE "outperforms other generators consistently across all cases" against a random generator, a variational graph auto-encoder and an adversarially regularised one.[^c13]

What survives the transfer (my inference, not tested here): the identification argument is domain-free, since it uses only the structure of the causal graph. What does not transfer is the content of the assumptions. For a text or image model, a generated plausible completion of the input would have to carry the discriminative content and share no hidden cause with the shift. Whether a language model can produce such completions, and whether the no-link assumption holds there, is open.

## Limits

- The residual correlation is weak. The paper says "weak positive or negative correlations still exist, which indicates the limitation of the current CVGAE".[^c14]
- The method's quality is bounded by the generator; the authors defer "higher-quality generation" to future work.[^c15]
- The identifying assumptions (the surrogate contains Gs, carries its discriminative information, and has no link from D) are causal assumptions. The generator metrics are evidence that the generator is good, not evidence that the assumptions hold.
- Validation against ground truth exists only for the two synthetic datasets, and the validity measure presumes a ground-truth explanation "that contains all discriminative information of the full graph G".[^c16] On Graph-SST2 the reference is a user study with "70 volunteers" answering ten questions each.[^c17]
- The ethics statement concedes the point that matters outside the lab: modelling the distribution shift "could be a barrier to fulfill their evaluation faithfulness".[^c18]

## Related

- [[ood-confounded-removal-evaluation]] — the problem this adjustment answers: removal moves the input off distribution and confounds the score
- [[causal-model-of-explanation]] — explanation as giving causes; the front-door route estimates a causal effect of the subgraph rather than a correlation with the output

[^c1]: doi-10-48550-arxiv-2201-08802 — "as D is hardly measurable, we can not"
[^c2]: doi-10-48550-arxiv-2201-08802 — "Hence, the causal effect of Gs on Y is not identifiable from SCM I."
[^c3]: doi-10-48550-arxiv-2201-08802 — "G∗s is the surrogate variable of Gs , which completes Gs to make them in the data"
[^c4]: doi-10-48550-arxiv-2201-08802 — "First, it originates from and contains Gs"
[^c5]: doi-10-48550-arxiv-2201-08802 — "should follow the data distribution"
[^c6]: doi-10-48550-arxiv-2201-08802 — "thus no link exists between D and G∗s"
[^c7]: doi-10-48550-arxiv-2201-08802 — "is well-preserved by G∗s"
[^c8]: doi-10-48550-arxiv-2201-08802 — "feeding the surrogate graph Gs∗ into the GNN predictor"
[^c9]: doi-10-48550-arxiv-2201-08802 — "we chain two identifiable partial effects of Gs on G∗s and G∗s on Y together"
[^c10]: doi-10-48550-arxiv-2201-08802 — "it is non-trivial to instantiate Gs∗ and collect the (Gs , Gs∗ ) pairs"
[^c11]: doi-10-48550-arxiv-2201-08802 — "Substantially, ρdse greatly improves after the frontdoor adjustments via the surrogate variable."
[^c12]: doi-10-48550-arxiv-2201-08802 — "The most notable case is GNNExplainer in MNISTsup"
[^c13]: doi-10-48550-arxiv-2201-08802 — "outperforms other generators consistently across all cases"
[^c14]: doi-10-48550-arxiv-2201-08802 — "positive or negative correlations still exist, which indicates the limitation of the current CVGAE"
[^c15]: doi-10-48550-arxiv-2201-08802 — "We leave the exploration of higher-quality generation in future work."
[^c16]: doi-10-48550-arxiv-2201-08802 — "that contains all discriminative information of the full graph G"
[^c17]: doi-10-48550-arxiv-2201-08802 — "70 volunteers are engaged"
[^c18]: doi-10-48550-arxiv-2201-08802 — "could be a barrier to fulfill their evaluation faithfulness"
