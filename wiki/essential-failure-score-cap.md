---
description: "Capping a rubric's weighted score when a core criterion fails stops minor criteria offsetting a missed essential fact; pairwise concordance rose from 3.0 to 3.5."
aliases: ["hard rejection", "truncation mechanism", "core-failure score ceiling", "essential-criterion cap"]
sources: ["doi-10-48550-arxiv-2603-13691"]
---
# Essential-failure score cap

A weighted rubric sums credit over criteria, and a sum can compensate: a strong showing on minor criteria can add up to enough to hide a missed core one. This is the general flaw of scalar combination that [[compensatory-leakage]] names. QuarkMedBench deals with it inside the score itself. When a core criterion fails, the aggregate is capped, so no amount of other credit can lift the response past the cap.

## Mechanism

Each query's rubric is split into four dimensions: "four core dimensions: Necessary, Important, Highlight, and Pit".[^c1] The score is weighted. Satisfied Essential, Important and Highlight criteria add credit, and Pitfall criteria subtract. The Pitfall criteria are the negative criteria of [[question-specific-rubric]], the named failure modes a response can be penalized for. The default weighting is "Essential : Important : Highlight : Pitfall = 2:1:1:2".[^c2]

The weights were chosen by A/B testing against human-annotated pairwise samples. The authors report that "substantially amplifying the weights for Essential and Pitfall criteria markedly enhanced" scoring accuracy, "elevating the ratio from approximately 2:1 to 3:1".[^c3][^c4] Here the ratio is the count of correct pairwise rankings against reversed ones, and equal weights (1:1:1:1) sit at the 2:1 end of Table 3.

The cap is the second move. Essential and Pitfall are the criteria that "serve as pivotal dimensions for determining the fundamental adequacy of a response".[^c5] If scores on them fall below predefined thresholds, the model "should be precluded from accumulating supplementary points, regardless of its proficiency in other dimensions", and "the ultimate aggregate score is strictly capped".[^c6][^c7] The authors report that this "elevates the concordance ratio from 3.0 to 3.5".[^c8]

So there are two levers. Weighting changes how much a core error costs in the sum. The cap changes whether any surplus credit can offset it at all. The first makes a core error heavier; the second makes it decisive. The paper's ratio gains come from these two steps, reported in sequence.

Under the transfer, what survives is the ordering idea, that a failed core criterion should settle the outcome before minor criteria are counted. What does not survive as stated is the form. A cap keeps a graded score on one scale and only bounds its top; a multiplicative gate, as in the reward design [[compensatory-leakage]] describes, zeroes out the rest. The paper does not compare the two.

## Limits

- The ratios are reported as "approximately 2:1 to 3:1" and as "3.0 to 3.5". The parts read give no number of pairs, no interval and no variance, so the size of the gain is not known.
- The weights and the cap were tuned on the same human pairwise samples used to report the gains. The gains are therefore in-sample.
- The weighting does not rise monotonically with core emphasis. Table 3 lists the more core-heavy 3:1:1:3 configuration as "Slightly < 3:1", against "Over-enhanced Core" (my reading of the table).
- The cap's thresholds are "predefined", but their values are not in the parts read, and the paper does not say at which weight configuration the cap was tested.
- Concordance measures whether pairs are ranked in the human order. It does not show that absolute scores are calibrated.
- No arm compares the cap with a multiplicative gate, a lexicographic order, or the same weights without a cap, so the cap's contribution beyond the weights is not isolated.

## Related

- [[compensatory-leakage]] — the flaw of scalar combination this cap addresses: a lower-priority gain can overturn a decision an earlier criterion fixed.
- [[question-specific-rubric]] — the weighted positive and negative criteria whose structure the cap acts on.
- [[non-compensatory-repair-score]] — another non-compensatory aggregation, a harmonic mean over answering and repair rather than a cap on one rubric.

[^c1]: doi-10-48550-arxiv-2603-13691 — "four core dimensions: Necessary, Important, Highlight, and Pit"
[^c2]: doi-10-48550-arxiv-2603-13691 — "Essential : Important : Highlight : Pitfall = 2:1:1:2"
[^c3]: doi-10-48550-arxiv-2603-13691 — "substantially amplifying the weights for Essential and Pitfall criteria markedly enhanced"
[^c4]: doi-10-48550-arxiv-2603-13691 — "elevating the ratio from approximately 2:1 to 3:1"
[^c5]: doi-10-48550-arxiv-2603-13691 — "criteria serve as pivotal dimensions for determining"
[^c6]: doi-10-48550-arxiv-2603-13691 — "regardless of its proficiency in other dimensions"
[^c7]: doi-10-48550-arxiv-2603-13691 — "the ultimate aggregate score is strictly capped"
[^c8]: doi-10-48550-arxiv-2603-13691 — "elevates the concordance ratio from 3.0 to 3.5"
