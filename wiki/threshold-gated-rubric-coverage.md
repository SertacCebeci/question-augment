---
description: "Scoring an open answer by how many pre-written criteria it meets, with zero credit below a cut k set from physician answers, so scattered hits do not add up to coverage."
aliases: ["CACS", "clinician-anchored coverage score", "thresholded rubric coverage", "rubric coverage threshold", "conjunctive coverage score"]
sources: ["doi-10-48550-arxiv-2603-02097"]
---
# Threshold-gated rubric coverage

An open-ended answer can be scored against a fixed list of case-specific criteria, each judged present or absent. The usual score is a mean: the share of criteria met, averaged over cases. A threshold-gated score changes the arithmetic. A response earns nothing until it has met at least k of the N criteria, and only above k does each further criterion add credit. In the benchmark studied here N is 30 and k is 10. The per-case credit is the number of criteria met, minus k, plus one, floored at zero; the benchmark score is the average of that credit over cases, scaled by the number of possible credit levels. The rule is stated as: "zero credit below k and graded credit above k."[^t1]

The point of the gate is that partial correctness does not accumulate into coverage. Mean accuracy "rewards every isolated rubric hit, even below the clinical coverage" threshold, so a response that collects scattered hits scores as well as one that covers a coherent set of requirements.[^t2] The paper's own numbers show the size of the difference. Across eleven frontier models, "Rubric Accuracy ranges from 39.6% to" 52.1%, while the gated score ranges from 17.8% to 32.9%.[^t3] The gap follows from which criteria get met. Generic criteria (communication, disclaimers, safety compliance) recur across the corpus and "are satisfied 60.2%" of the time, while case-specific clinical content is satisfied less often: "criteria are satisfied only 38.8%".[^t4] A gate converts that asymmetry into a loss for the answer that leans on generic hits: "failure mode: a response cannot compensate for" missing case-specific substance by piling up cheap criteria.[^t5]

The threshold is set from people, not from the grader. The authors "randomly sample 285 cases" and had physicians write responses to them; a separate physician group then graded those responses against the same case-specific criteria.[^t6] The cut is the rounded mean of those physician rubric-hit scores: "We set k to their rounded empirical mean, yielding k = 10".[^t7] The reference responses met "10.19/30 criteria per case" on average, which rounds to 10.[^t8] The method is the contrasting-groups logic of standard-setting, which "follows contrasting-groups and borderlinegroup standard-setting" in the measurement literature the authors cite.[^t9] So the cut is not chosen in advance; it is read off where a reference group falls.

What survives the transfer is the gate and the calibration procedure, not the constant. The number 10 of 30 belongs to this rubric and this physician pool. Any other checklist would need its own reference group to set its own cut.

## Limits

- The authors say k is "a physician-explicit coverage anchor, not a universal clinical safety threshold."[^t10] One k is used across all three difficulty levels, so the difficulty analysis tests robustness at a single operating point, not a threshold per stratum. The paper reports sensitivity to nearby thresholds in an appendix table; I did not read that table, so I cannot say how sharp the ranking is near k = 10.
- The score is a benchmark measure: "CACS is a benchmark coverage metric for thresholded rubric coverage, not" a deployment rule.[^t11]
- Scoring at scale "relies on automated rubric graders," and the primary grader is an external model, so the gate inherits the grader's reliability on each criterion.[^t12]
- The evaluation covers "singleturn, text-only responses to curated cases rather" than interactive or longitudinal care, and it is localized to Chinese clinical practice.[^t13]
- The paper does not compare the gate against a weighted or precision-type score on physician judgment in the part I read. My inference, not the paper's: a count gate treats every criterion alike once the cut is passed, so whether weighting criteria would change the ordering of models is untested here.

## Related

- [[recall-only-partial-credit]] — set-overlap credit also rewards hits and charges nothing for extras, but it has no gate, so a score can rise with each additional option
- [[dependency-aware-checklist-scoring]] — gates credit on prerequisites rather than on a count of met criteria; both expose what a flat checklist total hides
- [[compensatory-leakage]] — a related failure of combining criteria into one score; a count gate blocks additive compensation, though the paper does not frame it in those terms
- [[expert-report-derived-atomic-rubrics]] — how the atomic, content-bearing criteria a gate counts can be drawn from expert-written reports

[^t1]: doi-10-48550-arxiv-2603-02097 — "zero credit below k and graded credit above k."
[^t2]: doi-10-48550-arxiv-2603-02097 — "Mean accuracy rewards every isolated rubric hit, even below the clinical coverage"
[^t3]: doi-10-48550-arxiv-2603-02097 — "Rubric Accuracy ranges from 39.6% to"
[^t4]: doi-10-48550-arxiv-2603-02097 — "that recur across the corpus) are satisfied 60.2%"
[^t5]: doi-10-48550-arxiv-2603-02097 — "failure mode: a response cannot compensate for"
[^t6]: doi-10-48550-arxiv-2603-02097 — "We randomly sample 285 cases"
[^t7]: doi-10-48550-arxiv-2603-02097 — "We set k to their rounded empirical mean, yielding k = 10"
[^t8]: doi-10-48550-arxiv-2603-02097 — "corresponding to 33.96% mean rubric-hit rate or 10.19/30 criteria per case"
[^t9]: doi-10-48550-arxiv-2603-02097 — "follows contrasting-groups and borderlinegroup standard-setting"
[^t10]: doi-10-48550-arxiv-2603-02097 — "is a physician-explicit coverage anchor, not a universal clinical safety threshold."
[^t11]: doi-10-48550-arxiv-2603-02097 — "CACS is a benchmark coverage metric for thresholded rubric coverage, not"
[^t12]: doi-10-48550-arxiv-2603-02097 — "Its scalable scoring relies on automated rubric graders"
[^t13]: doi-10-48550-arxiv-2603-02097 — "It evaluates singleturn, text-only responses to curated cases rather"
