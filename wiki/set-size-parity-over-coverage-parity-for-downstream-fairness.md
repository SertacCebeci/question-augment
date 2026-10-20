---
description: "Equal coverage across groups can leave a decision aid helping some groups far more; equal prediction-set size tracks equal downstream accuracy gain, and label-clustered CP shrinks the gap."
aliases: ["substantive fairness in conformal prediction", "procedural versus substantive fairness"]
sources: ["arxiv-2602-16794"]
---
# Set-size parity over coverage parity for downstream fairness

A conformal prediction (CP) set can be fair as a procedure and unfair as an aid. The work separates procedural fairness (properties of the sets themselves: equal coverage, equal set size across groups) from substantive fairness (whether CP-assisted decisions improve accuracy by similar amounts across groups, relative to a control with no set).[^c1] A method may reach 90% coverage for every group yet give compact sets to one group and large, less actionable ones to another, so the aid helps unevenly.[^c2]

## What was measured

An LLM-in-the-loop evaluator stands in for human decision makers: it answers a task with and without the prediction set, and substantive unfairness is summarized by maxROR over groups. The authors report that equalized set size correlates strongly with improved substantive fairness, whereas the standard goal of equalized coverage often has negative effects.[^c3] The two procedural metrics are in diametric opposition: methods optimize one at the expense of the other.[^c4] Mondrian and Group-Clustered CP, which enforce coverage parity through group-dependent calibration, were never optimal on maxROR and produced the most unfair outcomes on FACET and RAVDESS.[^c5]

## Why label clustering narrows the size gap

Theorem 4.1 bounds the expected set-size disparity between groups for label-clustered CP by three drivers: intra-cluster label heterogeneity, cross-cluster spread, and intra-label cross-group disparity.[^c6] One cluster (marginal CP) forces heterogeneous labels together; one cluster per label makes thresholds unstable for rare labels; a middle K controls both. Sharing thresholds across groups pools calibration data and avoids the artificial group differences Mondrian CP introduces.[^c7]

Utility matters too: Backward CP reached the lowest maxROR on some datasets, but its sets were larger and the accuracy gain smaller; Label-Clustered CP offered a balance between efficiency and substantive fairness.[^c8]

My inference, not the paper's claim: a fairness target defined on an intermediate artifact (coverage) can be uncorrelated with, or opposed to, the outcome it is meant to protect, so the proxy should be validated against the outcome.

## Limits

- Human behavior is approximated by an LLM; the paper validates qualitative agreement with prior human studies, not equivalence.
- Correlations are across a handful of datasets and CP methods, plotted per dataset; they are not causal estimates.
- Fairness is defined by accuracy gain across protected groups only; other downstream harms are untested.
- The bound is an upper bound; it shows drivers, not tight gaps.
- The relevance to asking and answering is by analogy: it concerns uncertainty sets shown to a decision maker, not questions.

## Related

None of the existing notes treats this concept directly; closest are the conformal notes below.

- [[credal-then-conformalize-interval-decomposition]] — another decomposition of conformal set width into interpretable parts
- [[dp-stability-full-data-conformal-coverage]] — conformal coverage guarantees, the procedural property here shown insufficient

[^c1]: arxiv-2602-16794 — "substantive fairness asks whether these sets provide comparable downstream benefits to different groups"
[^c2]: arxiv-2602-16794 — "Such a method is procedurally fair with respect to coverage, but"
[^c3]: arxiv-2602-16794 — "we find that Equalized Set Size correlates strongly with improved"
[^c4]: arxiv-2602-16794 — "are in diametric opposition; CP methods optimize one at"
[^c5]: arxiv-2602-16794 — "Mondrian and Group-Clustered CP are never"
[^c6]: arxiv-2602-16794 — "Theorem 4.1 highlights three drivers of set size disparity:"
[^c7]: arxiv-2602-16794 — "pools calibration data"
[^c8]: arxiv-2602-16794 — "Label-Clustered CP offers a"
