---
description: "Pooled weighted rubric pass rates can hide a priority inversion: split by criterion weight, trivial items pass at 80–90% while critical ones pass at 32.4–41.7%."
aliases: ["priority inversion in rubric scoring", "weight-class pass rate", "critical-criterion pass rate"]
sources: ["doi-10-48550-arxiv-2607-02175"]
---
# Weight-stratified rubric pass rate

A rubric is a set of criteria about an ideal answer. Each criterion is "an atomic, MECE assertion about the ideal response"[^c1], carries a weight from 1 to 5, and is marked met or not met by an expert. The usual headline is the weighted share met: "The rubric pass rate is the sum of weights of criteria with expert_rating=true divided by the sum of all weights."[^c2] A single weighted share is an average over criteria, and an average can conceal which criteria carry the failures.

The mechanism is the split. Keep the same expert labels, group them by weight class, and report a pass rate per class. In the pilot the classes diverge sharply: "low-stakes weight-1 criteria passed at 80–90%"[^c3], while "critical weight-5 criteria pass at only 32.4% (Gemini and GPT) to 41.7% (Claude)."[^c4] The authors name the pattern in their opening: "The central finding is an inversion of clinical priority: the highest-weighted (weight-5, critical) criteria passed at only 32.4–41.7%."[^c5] The weighted headline does not show this on its own; the class split does.

The same split along a second axis gives the same shape. By category, "Instruction following (87.5%) and style (100%) are essentially solved for all three models."[^c6] Reasoning is "the largest category (123 criteria) and the weakest"[^c7], at 28.5% for Gemini[^c8] and 42.3% for Claude.[^c9] The authors summarise the contrast as a dissociation: "clinical reasoning and safety are not" solved, though the formatting is.[^c10] A fluent answer can clear every format criterion and still fail the one criterion that carries the clinical decision.

For asking and answering, the point is what the split can see. A holistic or pairwise rating would likely call all three responses fluent and plausible, and the authors state the consequence directly: "The inversion in Table 3 is invisible to holistic scoring and visible to atomic scoring."[^c11] Two things make the visibility: each decisive inference is its own criterion, and the weight is kept as a label instead of being folded into one total. A critical miss then counts five times a trivial one, and the miss stays attributable to a specific inference.

## Limits

- The sample is small: "tasks and 184 criteria we cannot conduct statistical inference about model rankings."[^c12] The per-class rates are descriptive, from five clinician-written scenarios and three models.
- Weight-5 criteria are most of the rubric: "35/108 = 32.4%" is the Gemini row for that class, and 108 of the 184 criteria carry weight 5.[^c13] By my arithmetic from Table 3, weight 5 carries 540 of the 768 total weight, about 70%. So the headline rate is mostly a critical-criterion rate, and part of the inversion is a property of how many criteria the clinicians labelled critical. (my inference)
- The pooled figure is not the reported mean. Table 2 averages task-level rates. Pooling Claude's Table 3 counts gives 328 of 768 weight, about 0.43, against a reported mean of 0.47. (my arithmetic; I found no reconciliation of the two in the text read)
- Weights are clinical judgement. The rubrics pass peer review for "weight calibration," but no inter-rater statistic on the weights is reported, so a class split is only as good as the weight labels it groups by. (my inference)
- Each criterion has one expert label.[^c14] A class pass rate therefore inherits any single-rater error in the weight and in the met/not-met call.
- The rubrics "cite predominantly UK/US guidance,"[^c15] so the inversion is shown for these scenarios and these health-system norms, not for clinical practice in general.

## Related

- [[expert-report-derived-atomic-rubrics]] — atomic binary rubrics scored as an unweighted share passed; this note adds clinician weights and the split by them
- [[evaluation-choices-encode-error-priorities]] — the weight is a normative choice, and disaggregating the metrics keeps that choice visible
- [[weighted-nugget-recall]] — partial-credit coverage weighted by a judge rather than by a clinician
- [[judge-coverage-overestimation]] — judges credit surface completeness, the kind of omission the class split exposes

[^c1]: doi-10-48550-arxiv-2607-02175 — "Each rubric criterion is an atomic, MECE assertion about the ideal response"
[^c2]: doi-10-48550-arxiv-2607-02175 — "The rubric pass rate is the sum of weights of criteria with expert_rating=true divided"
[^c3]: doi-10-48550-arxiv-2607-02175 — "low-stakes weight-1 criteria passed at 80–90%"
[^c4]: doi-10-48550-arxiv-2607-02175 — "critical weight-5 criteria pass at only 32.4% (Gemini and GPT) to 41.7% (Claude)"
[^c5]: doi-10-48550-arxiv-2607-02175 — "The central finding is an inversion of clinical priority: the highest-weighted (weight-5, critical) criteria"
[^c6]: doi-10-48550-arxiv-2607-02175 — "Instruction following (87.5%) and style (100%) are essentially solved for all three models."
[^c7]: doi-10-48550-arxiv-2607-02175 — "the largest category (123 criteria) and the weakest"
[^c8]: doi-10-48550-arxiv-2607-02175 — "35/123 = 28.5%"
[^c9]: doi-10-48550-arxiv-2607-02175 — "52/123 = 42.3%"
[^c10]: doi-10-48550-arxiv-2607-02175 — "clinical reasoning and safety are not"
[^c11]: doi-10-48550-arxiv-2607-02175 — "The inversion in Table 3 is invisible to holistic scoring and visible to atomic scoring."
[^c12]: doi-10-48550-arxiv-2607-02175 — "tasks and 184 criteria we cannot conduct statistical inference about model rankings"
[^c13]: doi-10-48550-arxiv-2607-02175 — "35/108 = 32.4%"
[^c14]: doi-10-48550-arxiv-2607-02175 — "each criterion has one expert label"
[^c15]: doi-10-48550-arxiv-2607-02175 — "rubrics and scenarios cite predominantly UK/US guidance"
