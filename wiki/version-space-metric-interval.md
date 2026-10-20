---
description: "The min and max of a metric over surrogates consistent with queried scores form an interval that narrows as queries prune the version space; it is an operational width, not a coverage guarantee."
aliases: ["certificate interval", "version-space uncertainty interval", "extremal-surrogate bounds", "bound width"]
sources: ["arxiv-2601-03087"]
---
# Version-space metric interval

Take a hypothesis class H and the set S of inputs already sent to a black-box model, each with the score it returned. The λ-approximate version space H_λ(S) is the set of hypotheses whose outputs stay within λ of those scores on S. In the paper's words, this set "contains all surrogate models that approximate the black-box scores on queried examples within tolerance λ."[^c1]

A quantity of interest µ(h), here the group AUC gap ΔAUC, is then bracketed by its extremes over that set. One solves for a hypothesis that maximises µ and one that minimises µ over H_λ(S); the two values give an interval [µ_min, µ_max] that must contain the gap for every surrogate still compatible with the queries.[^c2] The paper solves both problems as constrained empirical risk minimisation, using a sigmoid pairwise ranking surrogate because "As ROC-AUC is nondifferentiable, we optimise a sigmoid pairwise" ranking loss.[^c3]

Two properties follow from the construction. First, the width has a direct reading: it "upper-bounds how much the" estimated gap could change under any hypothesis still compatible with the observed queries.[^c4] Second, the interval is a function of the queried set, so it narrows as queries accumulate: the version space "becomes increasingly constrained, and the range of possible fairness" values shrinks with it.[^c5] An audit can therefore stop when half the width is below a tolerance and report the midpoint: "if (µtmax − µtmin )/2 ≤ ϵ then" return the midpoint.[^c6]

The width also tracks error in the paper's runs. "Bound width strongly correlates with actual error for" both selection rules on the Civil Comments case, with correlation 0.85 for the Bayesian variant and 0.74 for the disagreement variant (Figure 5).[^c7]

## Limits

- The interval is not a coverage guarantee. The authors say its width is "a useful operational proxy for uncertainty" and that it "should not be interpreted as a formal coverage" guarantee.[^c8]
- Measured coverage is high on one case and lower on the other. The ground-truth metric lay inside the interval in over 95% of queries on Civil Comments, "for BAFA-BO and 95.4% for disagreement." On Bias-in-Bios, "coverage is lower due to surrogate" and target mismatch, with the average violation still below the authors' tolerance.[^c9]
- The version space is taken over a small BERT family, not the black box's own parameters. The paper reports that swapping in DistilBERT changes the area under the error curve by less than 5% over three seeds, which is a small check, not a proof that the family is adequate.[^c10]
- The tolerance λ and the stopping ε are choices the auditor makes; the paper's guarantee-free stopping rule inherits them. My inference: a too-small λ can make the version space empty, a too-large one makes the interval loose, and neither failure is detected by the interval itself.
- The method needs labels and group attributes on the audit pool. The width is a bound on the metric over the pool, not over the deployment distribution.

## Related

- [[version-space]] — the consistency set itself, defined over a declared hypothesis language; this note takes the extremes of a metric over that set.
- [[rashomon-committee-querying]] — also an ε-version-space method, but it queries where a Gibbs-weighted committee disagrees, not where a metric's bound is widest.
- [[bound-disagreement-query-selection]] — the query rule that reads the two extremal hypotheses of this interval.
- active-fairness-auditing — the auditing setting in which the interval is used to stop and to select.

[^c1]: arxiv-2601-03087 — "This set contains all surrogate models that approximate the black-box scores on queried examples within tolerance λ."
[^c2]: arxiv-2601-03087 — "two feasible hypotheses by extremising the"
[^c3]: arxiv-2601-03087 — "As ROC-AUC is nondifferentiable, we optimise a sigmoid pairwise"
[^c4]: arxiv-2601-03087 — "The resulting width has a direct operational meaning as it upper-bounds how much the"
[^c5]: arxiv-2601-03087 — "becomes increasingly constrained, and the range of possible fairness"
[^c6]: arxiv-2601-03087 — "if (µtmax − µtmin )/2 ≤ ϵ then"
[^c7]: arxiv-2601-03087 — "Bound width strongly correlates with actual error for"
[^c8]: arxiv-2601-03087 — "it should not be interpreted as a formal coverage"
[^c9]: arxiv-2601-03087 — "coverage is lower due to surrogate"
[^c10]: arxiv-2601-03087 — "replacing the surrogate with DistilBERT increases AUEC by less than 5%"
