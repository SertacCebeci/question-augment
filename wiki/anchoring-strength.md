---
description: "A scalar score, effective support minus mismatch minus an anchor-budget penalty, decides whether in-context cues override a pretrained prior; too little or too much bait loses."
aliases: ["semantic anchoring", "anchoring strength", "Max-S selection", "Unified Contextual Control Theory"]
sources: ["arxiv-2512-05765"]
---
# Anchoring strength

When a pretrained model is given cues (labelled examples, a redefinition, a stated intent), those cues compete with the model's prior for which latent rule it runs. Chang's UCCT scores that competition with one scalar, S = ρd − dr − γ log k.[^c1] The first term, effective support ρd, is the density of the bait: how strongly the current cues recruit the target concept.[^c2] The second, mismatch dr, is the instability of the representation under perturbation. The third, γ log k, is a penalty on the k anchors admitted into context: "The cost of the bait."[^c3]

The decision is a comparison of two scores, not a threshold. The model runs the target rule when its score exceeds the prior's, so the gap ∆S = S(PT) − S(Pprior) carries the behaviour, and the boundary is ∆S = 0, described as "a comparison between two scores, not a fitted parameter."[^c4] Because the budget term grows without bound while support saturates, S is not monotone in the number of anchors. The paper reads this as three regimes: with too few anchors the prior wins; in an intermediate band the target wins; past an optimal budget, the cost of the extra context pulls the target back under the prior, which the paper calls over-baiting.[^c5] In its in-context examples, two demonstrations that redefine the minus sign as plus are reported to "flip every tested frontier" model from its usual answer on a subtraction item.[^c6]

The anchors do not install a concept. The paper's reading is that they recruit a neighbourhood of latent patterns whose extent follows the spread of the anchor cohort.[^c16] In its cross-modal test, anchors "in CLIP bind 96.4% of held-out non-cat animals but only" 9.1% of vehicles, so the cohort recruits an animal-like region rather than the word "cat."[^c7][^c8]

The terms are meant to be read from observable quantities. The budget k counts admitted anchors, mismatch comes from output sensitivity under perturbation, and support from self-consistency across sampled reasoning paths.[^c9] The paper's summary is that anchoring "succeeds when bait matches pattern density": familiar concepts bind with few examples, rare ones resist.[^c11]

A reading for asking, which is mine and not the paper's: if a question's cues are the bait, then both how many constraints it carries and how familiar their target is bear on whether the answerer locks onto the intended rule. Past the budget, adding constraints may cost more than it adds. The paper does not test questions; it tests in-context rules and images.

## Limits

The formula is defined in this paper, but its measurement procedure is deferred: "full measurement formulas are given" in the companion UCCT paper.[^c12] What is shown here is the shape of the curve in a few in-context cases, not a fitted S across tasks.

The paper states the test that would discriminate its account, a controlled suite where the rule is fixed and familiarity varies, and predicts that "higher support or lower mismatch should reduce" the anchors needed.[^c13] That prediction is stated, not reported here. The paper also names what would refute it: "anchoring is stable would refute us."[^c14]

The "phase transition" is the paper's interpretation of the curve. The sharp flips are shown for a few frontier models on small arithmetic-like and rule-choice tasks; nothing here establishes that the same score governs open-ended questions, or that the three terms are separable in practice.

## Related

- [[demonstration-label-consistency]] — the share of demonstrations that carry the query's label, which is the composition of the anchor cohort that the score counts
- [[parametric-suppression]] — a prior that overwrites context in knowledge conflicts, located by layer; a mechanistic picture of the prior winning
- [[process-outcome-consistency-verification]] — the paper's other control level: whether the trace warrants the answer, rather than whether the cues bind it

[^c1]: arxiv-2512-05765 — "S = ρd − dr − γ log k"
[^c2]: arxiv-2512-05765 — "The density of the bait."
[^c3]: arxiv-2512-05765 — "The cost of the bait."
[^c4]: arxiv-2512-05765 — "a comparison between two scores, not a fitted parameter."
[^c5]: arxiv-2512-05765 — "Three regimes follow from the Max-S comparison."
[^c6]: arxiv-2512-05765 — "flip every tested frontier"
[^c7]: arxiv-2512-05765 — "9.1% of vehicles (Chang et al., 2025): the anchors recruit an"
[^c8]: arxiv-2512-05765 — "in CLIP bind 96.4% of held-out non-cat animals but only"
[^c9]: arxiv-2512-05765 — "mismatch dr comes from output sensitivity under perturbation"
[^c11]: arxiv-2512-05765 — "Table 1. Anchoring succeeds when bait matches pattern density."
[^c12]: arxiv-2512-05765 — "full measurement formulas are given"
[^c13]: arxiv-2512-05765 — "higher support or lower mismatch should reduce"
[^c14]: arxiv-2512-05765 — "anchoring is stable would refute us."
[^c16]: arxiv-2512-05765 — "Recruitment is neighborhood-level, not concept-level."
