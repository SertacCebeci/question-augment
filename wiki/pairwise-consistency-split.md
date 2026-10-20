---
description: "A tree split scored by how many observed pairwise comparisons its cut puts winner and loser on opposite sides; comparisons straddling a split are dropped from its children."
aliases: ["consistency score split", "winner-loser split criterion", "straddler exclusion"]
sources: ["arxiv-2512-14263"]
---
# Pairwise consistency split

A regression tree is usually grown on labelled items: each split is chosen so that the labels in the two children become more alike. Pairwise comparisons supply no item label, only an ordered pair of items, so that criterion has nothing to act on. The consistency score replaces it with a criterion read off the comparisons themselves. For a candidate cut on one feature, each comparison gets the value +1 when the winner falls on the right and the loser on the left, −1 for the reverse, and 0 when both items fall on the same side. The sample score is the mean of these values over the comparisons in the node.[^c1] Its population form is the absolute gap between the probability of +1 and the probability of −1, so it "equals 1 for a split that perfectly separates winners from losers and 0 for a split completely uncorrelated with preferences."[^c2]

The tree is grown greedily: at each node the candidate split with the highest sample score is taken.[^c3] Numeric candidates are midpoints between consecutive distinct values of a feature, the thresholds "are taken as midpoints" in the paper's notation.[^c4] Categorical candidates are binary partitions of the categories present at the node, enumerated only for features with at most three categories there, which keeps the candidate set small.

Straddlers are the mechanism that sets tree size. After a split, a comparison whose two items fall into different children is called a straddler: "Pairs for which one item lies in AL and the other in AR are called straddlers."[^c5] Descendant nodes are fitted only on comparisons whose two items lie inside the same child. Straddlers are not discarded, though: they are "retained for final leaf parameter fitting," where their separated items receive distinct rankings.[^c6] The paper says the exclusion "reduces the dataset size internally," and that this is "the growth of the DT thereby favoring smaller and more interpretable trees."[^c7] The conclusion puts the same point as a claim: excluding straddlers "yields shallow trees without needing growth-controlling" hyperparameters.[^c8]

Two justifications are given for dropping them. Descendant nodes should solve a problem conditional on items inside their own region, and a straddler carries information only about the parent ordering when the parent split gap dominates the residual spread on each side. The paper states the second as a lossless condition. Outside it, "exclusion becomes a controlled approximation": it trades some descendant-level signal for the smaller tree.[^c9]

Once the structure is fixed, each leaf receives a value with an independent zero-mean normal prior. The likelihood is the same pairwise likelihood used for Gaussian-process preference models, with the GP prior swapped for the leaf prior. The posterior is then approximated by a Gaussian at its mode, by a Laplace approximation, since "the posterior is approximated by a Gaussian centered at the mode."[^c10] The result is a tree whose leaves carry a joint Gaussian, which is what allows a pairwise acquisition rule such as [[qeubo]] to be evaluated on pairs of leaves. Two prior scales appear in the fit, but they "are not identifiable separately"[^c11]: the fit "depends only on the ratio"[^c12] of noise to prior scale. A sum-to-zero constraint then removes the constant-shift direction, which the paper says "the model is made identifiable by adding."[^c13]

On eight benchmark functions used as simulated decision-makers, the tree model is described as "a competitive alternative to GP-based approaches," strongest on rugged functions, and it "performs slightly worse on Rosenbrock and Hartmann, both non-rugged functions."[^c14] The paper also reports that the running time is faster than GP-based models, by a factor the appendix puts at 10 to 400.[^c15]

The paper's motivation is interpretability, not query efficiency alone. Earlier pairwise methods gave only local explanations: they "determine when one item is preferred over another but global interpretability is not possible."[^c16] The authors claim that, to their knowledge, no globally interpretable tree that learns directly from comparisons and supports active learning existed before.[^c17] That is their novelty claim, not something this note has checked against the literature.

## Limits

- The concentration result behind the score is not a guarantee of choosing the right split. The paper says it "is therefore best read as a heuristic motivation for the consistency score."[^c18]
- Straddler exclusion is exact only under the paper's condition. Elsewhere it is an approximation whose cost is not measured in the sections read.
- The tree is conditioned on the greedily chosen structure. The paper notes that "A full Bayesian treatment would account for two sources of uncertainty," and that only uncertainty in leaf values enters the acquisition step.[^c19]
- Within one leaf the acquisition rule "collapses," so the paper uses a separate sampling rule there, and only in its discrete item-set experiments.[^c20]
- Indifference statements are not modelled: "the inability to model indifference statements" is listed as a limitation by the authors.[^c21] Their second limitation is "with non-rugged functions as the number of dimensions increases" beyond seven.[^c22]
- The benchmark comparison uses simulated, noiseless decision-makers ("noiseless utility function using eight 2D to 6D benchmark functions").[^c23] The one real-data PBO case is a sushi ranking; the second case, patient messages, is said by the authors to be "not a PBO problem in the strict sense."[^c24]
- My reading, not the paper's claim: the extracted sample score in its equation has no absolute value, while the population score does. If the sample score is used unsigned, a split that puts winners on the left would score negative. The text I read does not settle which convention the search uses.
- The greedy search is not an exact tree optimiser. An exact minimum-cost tree is a different objective; see [[optimal-decision-tree]].

## Related

- [[qeubo]] — the acquisition rule the paper evaluates on leaf posteriors; its guarantees are stated for GP posteriors, so the leaf version inherits the rule, not the proof (my inference).
- [[rashomon-committee-querying]] — enumerates a set of near-optimal sparse trees to make a committee; this paper keeps one deterministic tree and puts the uncertainty into its leaves.
- [[optimal-decision-tree]] — exact minimum-expected-cost trees for test sequencing; the consistency split is greedy and scores a different quantity.

[^c1]: arxiv-2512-14263 — "has the winner on the right and the loser on the left of the split"
[^c2]: arxiv-2512-14263 — "perfectly separates winners from losers and 0 for a split completely uncorrelated with preferences"
[^c3]: arxiv-2512-14263 — "The tree is constructed greedily by selecting"
[^c4]: arxiv-2512-14263 — "are taken as midpoints"
[^c5]: arxiv-2512-14263 — "Pairs for which one item lies in AL and the other in AR are called straddlers"
[^c6]: arxiv-2512-14263 — "retained for final leaf parameter fitting"
[^c7]: arxiv-2512-14263 — "the growth of the DT thereby favoring smaller and more interpretable trees"
[^c8]: arxiv-2512-14263 — "without needing growth-controlling"
[^c9]: arxiv-2512-14263 — "exclusion becomes a controlled approximation"
[^c10]: arxiv-2512-14263 — "the posterior is approximated by a Gaussian centered at the mode"
[^c11]: arxiv-2512-14263 — "are not identifiable separately"
[^c12]: arxiv-2512-14263 — "depends only on the ratio"
[^c13]: arxiv-2512-14263 — "the model is made identifiable by adding a sum-to-zero"
[^c14]: arxiv-2512-14263 — "performs slightly worse on Rosenbrock and Hartmann, both non-rugged functions"
[^c15]: arxiv-2512-14263 — "that the running time is faster than GP-based models"
[^c16]: arxiv-2512-14263 — "determine when one item is preferred over another but global interpretability is not possible"
[^c17]: arxiv-2512-14263 — "DT that can be used for active learning and learns directly on PC data does not yet exist"
[^c18]: arxiv-2512-14263 — "and this is therefore best read as a heuristic motivation for the consistency score"
[^c19]: arxiv-2512-14263 — "A full Bayesian treatment would account for two sources of uncertainty"
[^c20]: arxiv-2512-14263 — "within a single leaf, qEUBO collapses"
[^c21]: arxiv-2512-14263 — "the inability to model indifference statements"
[^c22]: arxiv-2512-14263 — "with non-rugged functions as the number of dimensions increases"
[^c23]: arxiv-2512-14263 — "noiseless utility function using eight 2D to 6D benchmark functions"
[^c24]: arxiv-2512-14263 — "PMR is not a PBO problem in the strict sense"
