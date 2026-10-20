---
description: "A template's bias is the spread, across social groups, of each group's accuracy as a percentage of the template's pooled baseline; 0% means every group matches the baseline."
aliases: ["percentage deviation from baseline bias score", "max-min group spread bias score", "baseline-relative group bias score"]
sources: ["doi-10-48550-arxiv-2308-12539"]
---
# Baseline-relative group deviation score

Template-based bias measures start from a reference point and ask how far each group falls from it. The assumption is stated directly: "the assumption is that performance" should be consistent across social groups, so that "if a model is unbiased, its score for each group should match" a common baseline.[^c1] In CALM the baseline is local to the template: "take the baseline score on a template to be the average accuracy on 350 prompts."[^c2] The 350 prompts are the template filled with fifty names for each of seven social groups.

Each group is then scored against that baseline. The group's correct count (out of its 50 prompts) is compared with the baseline, and "the difference from the baseline, taken as a percentage change" gives the group score.[^c3] My reading of the garbled formula in the text is (correct_g / 50 − baseline) / baseline × 100 (my inference from the extraction; the equation itself did not survive).

The template-level bias is then a spread, not a signed deviation: the paper takes "the average of the difference between the maximum and minimum bs across all social groups" for each template.[^c4] Gender uses three groups and race four. The model-level number averages the gender and race scores "across the three NLP tasks."[^c5] Because each template is reduced to a max-minus-min, the score says how far apart the most-favoured and least-favoured group sit, and not which group is ahead.

## What the construction does to the number

- Zero is reached only when every group's accuracy equals the template's baseline. Any two groups that differ by the same amount give the same score, whichever side of the baseline they lie on (my inference from the max-minus-min form).
- The deviation is relative to the baseline. A fixed accuracy gap on a template with low baseline accuracy is a larger percentage than the same gap on a high-accuracy template. This is a property of the formula, not a finding the paper tests.
- Averaging over templates reports the typical template spread. The paper notes that accuracy "for each template" varies significantly across groups, so the averaged figure can sit well below the worst template.[^c6]
- The score needs a ground truth for each prompt: "For each prompt in CALM, we have the ground truth answer." Tasks without one cannot enter this construction.[^c7]

## Limits

- Where a model fails a task, the construction breaks down. The authors report that "certain models exhibit significant underperformance in specific tasks, achieving near-zero" accuracy, and "we exclude such tasks from bias scores for those models."[^c8]
- The groups are operationalised by names, from US sources, for seven US-centred social groups. "The target word list we used for the CALM dataset creation is limited to seven social groups."[^c9]
- Gender and race name lists overlap, so the two scores are not independent: "some interdependence in gender and race bias scores."[^c10]
- Combining tasks is unsettled. The authors write that "future research is needed to better understand how to incorporate multiple" tasks to measure overall bias.[^c11]
- Uncertainty is reported as the spread across random prompt subsets (Table 3), not as an interval on each group's score. The authors' own description is that "the standard deviations are small."[^c12] Whether a single group score is precise enough to compare two models is not shown.

## Related

- [[template-set-sensitivity-of-bias-scores]] — how stable the template-level scores are when the template set changes; this note is the aggregation those scores go through.
- [[calibration-fairness-gap]] — the same move, a subgroup value minus a background value, applied to calibration error rather than accuracy.
- [[predicted-group-disaggregated-calibration-error]] — splitting an error measure by group so that disparities an aggregate hides become visible.
- [[subgroup-abstention-gap]] — group differences in abstention, a disparity measured without a template-local baseline.

[^c1]: doi-10-48550-arxiv-2308-12539 — "the assumption is that performance"
[^c2]: doi-10-48550-arxiv-2308-12539 — "take the baseline score on a template to be the average accuracy on 350 prompts."
[^c3]: doi-10-48550-arxiv-2308-12539 — "group is the difference from the baseline, taken as a percentage change as follows"
[^c4]: doi-10-48550-arxiv-2308-12539 — "average of the difference between the maximum and minimum bs across all social groups"
[^c5]: doi-10-48550-arxiv-2308-12539 — "score for the model as the average of gender and racial bias across the three NLP tasks"
[^c6]: doi-10-48550-arxiv-2308-12539 — "For each template, we found significant variation in accuracy across different social groups."
[^c7]: doi-10-48550-arxiv-2308-12539 — "For each prompt in CALM, we have the ground truth answer."
[^c8]: doi-10-48550-arxiv-2308-12539 — "we exclude such tasks from bias scores for those models"
[^c9]: doi-10-48550-arxiv-2308-12539 — "The target word list we used for the CALM dataset creation is limited to seven social groups"
[^c10]: doi-10-48550-arxiv-2308-12539 — "some interdependence in gender and race bias scores"
[^c11]: doi-10-48550-arxiv-2308-12539 — "Future research is needed to better understand how to incorporate multiple"
[^c12]: doi-10-48550-arxiv-2308-12539 — "The standard deviations are small."
