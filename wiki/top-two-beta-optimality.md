---
description: "Top-two best-arm sampling reserves a fixed fraction beta for the leader, so it is only beta-optimal; the right beta depends on the unknown instance and can change sample complexity sharply."
aliases: ["top-two sampling", "top-two methods", "beta-optimal sampling", "T3C", "top-two Thompson sampling"]
sources: ["doi-10-48550-arxiv-2301-03785"]
---
# Top-two sampling and beta-optimality

Fixed-confidence best-arm identification asks which of K arms has the largest mean and stops once the evidence reaches a set level of confidence. Top-two sampling is a family of rules for choosing which arm to sample next. Each round it picks a leader and a challenger from the current estimates, and "the sampling strategy randomizes between these two arms."[^c1] The rule is cheap because it never has to compute a full allocation over all K arms, only over the leader and one challenger.

The price is a free parameter. The rule gives a share β in (0, 1) of the sampling to the leader and divides the rest among the other arms. The paper states what this buys: "if a β fraction of the sampling resources are reserved for the top arm" then the remaining fraction can be allocated well among the other arms.[^c2] The guarantee is therefore conditional on β. The sample complexity is inversely proportional to a transportation cost Γβ(ν) that is at least the instance's true complexity Γ(ν), with equality only at a value β⋆ that "depends on the bandit instance and is unknown a priori."[^c3] The authors call these rules β-optimal. Their abstract names the cost: the efficient approaches "have provable gaps to the optimal performance."[^c4]

The gap is shown empirically, not only bounded. The paper's Figure 1 plots sample complexity against β and shows "the sensitivity of the sample complexity to β," with "a substantial gap (e.g., an order of magnitude)" between the best β-optimal guarantee and the optimal one.[^c5] The value β = 0.5 has been the default: it "has been prescribed as a reasonable choice for the top-two algorithms," and the authors report it "can be noticeably different from the optimal choice in some instances."[^c6] For the instances in that figure the optimal β is about 0.27 for each of three existing approaches.[^c7]

The mechanism is a trade-off inside one number. Samples given to the leader confirm the current answer; samples given to challengers test it. A fixed split encodes a prior about how much confirmation is enough, and the paper's measurements say that when the prior is wrong the cost falls on sample count, not on the identified arm. Transferred to questioning, the same structure suggests that a fixed ratio between re-checking the current answer and probing alternatives is an instance-dependent choice rather than a constant. That transfer is my inference; the paper is about bandits only.

Top-two sampling was first introduced for the Bayesian setting.[^c8] The non-Bayesian versions the paper compares, such as "top-two sequential probability ratio test (TT-SPRT)", are the ones that "achieve optimal performance only when an instance-dependent parameter β is known a priori."[^c9]

## Limits

- The ~0.27 optimum and the "order of magnitude" gap are the paper's own numbers on its chosen instances. They are not universal constants, and I read the introduction and the cited figure statements, not the full experimental section.
- The scope is fixed-confidence, non-Bayesian, and parametric. The paper notes that "the existing relevant literature focuses on the family of exponential distributions," and its generalization targets other families. Nothing here covers non-parametric bandits.
- The β-optimality statements are asymptotic in the paper's analysis. The note does not establish finite-sample behaviour for any β.
- The paper says the gap appears "in some bandit instances." Where a fixed β happens to be close to the optimum, the gap is small; the note does not claim it is always large.
- Whether a β-free rule is always preferable in practice is not settled here. The paper's claim is about sample complexity in its settings, and it gives up nothing in computation that I could find in what I read.

## Related

- optimal-allocation-tracking — the same allocation problem, solved by tracking the optimal proportions rather than by fixing β
- [[thompson-sampling]] — the Bayesian setting in which top-two sampling was first introduced
- [[pac-best-arm-sample-complexity-lower-bound]] — the complexity measure that the transport cost is compared against
- [[neyman-allocation]] — a fixed-budget allocation rule by formula, a different target from fixed-confidence sampling

[^c1]: doi-10-48550-arxiv-2301-03785 — "the sampling strategy randomizes between these two arms"
[^c2]: doi-10-48550-arxiv-2301-03785 — "if a β fraction of the sampling resources are reserved for the top arm"
[^c3]: doi-10-48550-arxiv-2301-03785 — "which depends on the bandit instance and is unknown a priori"
[^c4]: doi-10-48550-arxiv-2301-03785 — "provable gaps to the optimal performance (e.g., the β-optimal approaches in top-two methods)"
[^c5]: doi-10-48550-arxiv-2301-03785 — "a substantial gap (e.g., an order of magnitude)"
[^c6]: doi-10-48550-arxiv-2301-03785 — "been prescribed as a reasonable choice for the top-two algorithms"
[^c7]: doi-10-48550-arxiv-2301-03785 — "In all these cases, the optimal value of"
[^c8]: doi-10-48550-arxiv-2301-03785 — "Top-two sampling was first introduced in [10] for"
[^c9]: doi-10-48550-arxiv-2301-03785 — "achieve optimal performance only when an instance-dependent parameter β is known a priori"
