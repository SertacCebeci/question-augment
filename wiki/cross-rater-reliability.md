---
description: "Cross-rater reliability compares whether one group's labels reproduce another's aggregate pattern, correcting for chance; LLM labels can diverge item by item yet mirror human tendencies."
aliases: ["xRR", "cross-rater reliability", "cross-kappa", "normalized cross-kappa", "normalized κx"]
sources: ["arxiv-2512-09662"]
---
# Cross-rater reliability

Chance-corrected agreement between two graders asks whether they label the same items alike. Cross-rater reliability (xRR) asks whether one group of annotators can reproduce the labelling pattern of another. The conventional measures "assume a single objective ground truth and penalise all disagreement equally," which fits poorly with subjective labels, where a split among annotators can be real diversity rather than error.[^c1] xRR keeps the chance correction but changes the unit being compared. Its core statistic is a cross-kappa, "designed to measure annotation agreement between replications in a chance-corrected manner," and a normalized form that compares two replications with each other.[^c2]

The normalized cross-kappa does not look at agreement inside a group. It "does not evaluate pairwise agreement within a group, but instead compares two independent replications of an annotation experiment."[^c3] It "quantifies how similarly the two groups behave on average across items, correcting for chance and for differences in the marginal label distributions."[^c4] Because it works on group-level patterns, a group can be unreliable item by item and still have an aggregate that matches another group's.

The hate-speech study shows this case. Its LLM annotators agreed among themselves only at a "slight to fair" level, and their labels diverged from the human labels at the item level.[^c5] Yet the normalized κx between the human group and the LLM group was 0.35 to 0.41, which the paper reads as "a fair to moderate degree of similarity between the human and LLMs annotations."[^c6] The authors' gloss is that "although the LLMs disagree among themselves on individual items, the overall pattern of their aggregated annotations moderately mirrors the general tendencies observed in the human judgements."[^c7] The same paper does not turn this into replacement: "LLMs still fail to capture the full spectrum of human annotation patterns."[^c8]

The chance correction still matters here. It uses the marginal label distributions, so a group that labels most items one way does not score well by default. That part is inherited from Cohen's kappa, as in [[chance-corrected-agreement]] (my inference on the transfer).

What a high value licenses is narrower than the metric's authors suggest. They read a high normalized κx as assurance that the crowd "are functioning as an extension of the trusted annotators."[^c9] The paper's own conclusion is more cautious: "These results suggest that LLMs should not yet be treated as full substitutes for human annotators in socially grounded tasks."[^c10] A high value says two groups behave alike on average across items. It does not say either group is correct on any item.

## Limits

- Three annotators per post. The authors "restricted our analysis to instances with exactly three human annotators."[^c11] With three raters the per-item distribution takes few values, and the stability of the normalized κx at other group sizes was not tested (my inference).
- Binary labels only. "The task under study is binary hate speech detection, where each post is classified as either hate or non-hate."[^c12] Whether group-level mirroring holds for graded or multi-class labels is not shown here.
- Point values without intervals. The normalized κx values are reported as 0.35 to 0.41 with no interval, so a gap of that size between datasets or models is not established by this paper (my inference).
- Replication is not correctness. Two groups can mirror each other and share the same error on the same posts; this measure cannot detect a shared error.

## Related

- [[chance-corrected-agreement]] — the pairwise kappa that xRR generalises from two raters to two groups
- [[annotator-disagreement-calibration]] — also treats annotator spread as the object to match, rather than one ground truth
- [[llm-judge-validation-gap]] — the question of how far LLM labels can be trusted, to which a group-level mirror is one partial answer
- [[ordinal-judge-fidelity]] — the ranking form of the same idea: a labeller can get the order right while the levels are off

[^c1]: arxiv-2512-09662 — "assume a single objective ground truth and penalise all disagreement equally"
[^c2]: arxiv-2512-09662 — "designed to measure annotation agreement between replications in a chance-corrected manner"
[^c3]: arxiv-2512-09662 — "does not evaluate pairwise agreement within a group, but instead compares two independent replications of an annotation experiment"
[^c4]: arxiv-2512-09662 — "It quantifies how similarly the two groups behave on average across items, correcting for chance and for differences in the marginal label distributions."
[^c5]: arxiv-2512-09662 — "the LLMs exhibits slight to fair agreement"
[^c6]: arxiv-2512-09662 — "the normalized κx values reveal a fair to moderate degree of similarity between the human and LLMs annotations"
[^c7]: arxiv-2512-09662 — "although the LLMs disagree among themselves on individual items, the overall pattern of their aggregated annotations moderately mirrors the general tendencies observed in the human judgements"
[^c8]: arxiv-2512-09662 — "LLMs still fail to capture the full spectrum of human annotation patterns"
[^c9]: arxiv-2512-09662 — "are functioning as an extension of the trusted annotators"
[^c10]: arxiv-2512-09662 — "These results suggest that LLMs should not yet be treated as full substitutes for human annotators in socially grounded tasks"
[^c11]: arxiv-2512-09662 — "we restricted our analysis to instances with exactly three human annotators"
[^c12]: arxiv-2512-09662 — "The task under study is binary hate speech detection, where each post is classified as either hate or non-hate"
