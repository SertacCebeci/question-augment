---
description: "Ranking the same LLM outputs with different evaluator cohorts can reorder the top model: physicians split by seniority and setting, matched AI agents agree, yet global rank concordance stays high."
aliases: ["cohort-dependent model ranking", "evaluator-panel-dependent ranking", "top-rank divergence across evaluator groups"]
sources: ["doi-10-1038-s41746-026-02942-6"]
---
# Evaluator-cohort ranking shift

A ranking of answers is a property of the answers together with the people who ranked them. In a multicenter study of LLM-written interpretations of real clinical cases, more than 400 physicians ranked five model outputs per case on six dimensions. The order they produced was not stable across cohorts: "the identity of the top-ranked model was not stable across seniority strata, suggesting that evaluative emphasis shifts with clinical experience rather than reflecting random dispersion."[^e1] Practice setting moved it as well, with "directional inversions observed for several models" between high-altitude and plain-region physicians.[^e2] The authors' summary is that "clinical seniority shapes multidimensional evaluation priorities and that physician-centered judgment exhibits structured heterogeneity rather than consensus uniformity."[^e3]

The shift is not noise around one answer. Seniority changed which output sat at the top, and the change followed the evaluators' priorities: junior physicians "tended to favor" one model across dimensions, while senior physicians split their first-place votes across others on coherence, accuracy and clinical usefulness.[^e4] The rubric did not remove it. A structured rubric "was provided to physicians," and the AI-agent evaluators were "configured to follow the identical ranking framework and score conversion rules."[^e5] Ordinal ranks were converted to 100, 75, 50, 25 and 0 so that cohorts could be compared, which fixes the scale but not the choice of who ranks.[^e18]

The paper also shows that agreement at one level can hide disagreement at another. Kendall's W, "where 0 indicates no agreement and 1 indicates perfect," unanimous agreement, was 0.798 between physicians and AI agents across all models and dimensions, and the authors read it as broad agreement.[^e17] Yet at the top of the list the two groups diverged: "AI agents consistently assigned the highest rankings to OpenAI o1 across all six dimensions, whereas physicians favored DeepSeek-R1 and GPT-4o."[^e7] A single concordance coefficient can be high while the answer a reader would pick first differs by evaluator group. My inference: whenever the question is "which answer is best", a global W is the wrong summary, and the top-rank split is the quantity to report.

The AI-agent cohort shows the opposite pattern on stability. Configured as one model with identical prompts, the agents were nearly invariant across simulated seniority: "76.7% of ranking pairs were identical across seniority levels, compared with 3.3% among physicians."[^e8] The authors refuse to read this as a virtue: "This consistency, however, should not be equated with validity."[^e9] Their reading is that the agents "do not reproduce the structured heterogeneity of physician judgment."[^e10] The cohort that looks most reliable is the one that has lost the variation that the human cohort carries.

So the same answers can have different best-ranked members depending on who is asked. Which evaluator population is the right one is not settled by the ranking itself. The paper says so directly: the comparison "did not establish which group provided the most clinically valid assessments."[^e11]

## Limits

- Seven cases, each judged only by physicians of the matching specialty. "the effects of case content and evaluator specialty are confounded and cannot be disentangled without cross-specialty evaluation of the same case."[^e12] The top-rank split may belong to the case set as much as to the cohort.
- All cases and evaluations were in Chinese, and the AI agents were all powered by one underlying LLM architecture.[^e13][^e19]
- The scores are ordinal: the method "captures relative preference but does not measure absolute quality differences between closely ranked" models.[^e14] A split at the top of a near-tied list may be small in quality terms.
- The paper does not separate model architecture, training data and prompt design as causes of the agents' stability; these "were not directly assessed."[^e15] The reason agent rankings do not split is therefore open.
- Preference is not validity. The authors state that closer alignment with a physician subgroup "should not be interpreted as evidence of alignment with superior evaluation quality."[^e16] This note describes how rankings move with the cohort, not which cohort to trust.

## Related

- [[llm-judge-validation-gap]] — human validation of LLM judges is rare; this note adds that a high rank-level agreement can coexist with a split at the top
- [[rater-effects-latent-score-model]] — treats each rater's strictness as a latent parameter so a score can be inferred; a cohort-level shift is a change in who ranks, which a per-rater correction does not remove (my inference)
- [[simulated-respondent-variance-deficit]] — simulated survey respondents spread less than humans; the AI-agent evaluators here show the same loss of spread, now in rankings
- [[reducible-context-gap-disagreement]] — on HealthBench, rater identity explains little of physician disagreement, which sits against the seniority effect found here; the two differ in task and in the measure used

[^e1]: doi-10-1038-s41746-026-02942-6 — "the identity of the top-ranked model was not stable across seniority strata"
[^e2]: doi-10-1038-s41746-026-02942-6 — "directional inversions observed for several models"
[^e3]: doi-10-1038-s41746-026-02942-6 — "clinical seniority shapes multidimensional evaluation priorities and that physiciancentered judgment exhibits structured heterogeneity rather than consensus uniformity"
[^e4]: doi-10-1038-s41746-026-02942-6 — "junior physicians tended to favor"
[^e5]: doi-10-1038-s41746-026-02942-6 — "configured to follow the identical ranking framework and score conversion rules"
[^e6]: doi-10-1038-s41746-026-02942-6 — "where 0 indicates no agreement and 1 indicates perfect,"
[^e7]: doi-10-1038-s41746-026-02942-6 — "AI agents consistently assigned the highest rankings to OpenAI o1 across all six dimensions"
[^e8]: doi-10-1038-s41746-026-02942-6 — "76.7% of ranking pairs were identical across seniority levels"
[^e9]: doi-10-1038-s41746-026-02942-6 — "This consistency, however, should not be equated with validity."
[^e10]: doi-10-1038-s41746-026-02942-6 — "do not reproduce the structured heterogeneity of physician judgment"
[^e11]: doi-10-1038-s41746-026-02942-6 — "the study compared evaluation patterns across physician seniority groups but did not establish which"
[^e12]: doi-10-1038-s41746-026-02942-6 — "the effects of case content and evaluator specialty are confounded and cannot be disentangled without"
[^e13]: doi-10-1038-s41746-026-02942-6 — "all cases and evaluations were conducted in Chinese"
[^e14]: doi-10-1038-s41746-026-02942-6 — "relative preference but does not measure absolute quality differences between closely ranked"
[^e15]: doi-10-1038-s41746-026-02942-6 — "although the relative contributions of model architecture, training data,"
[^e16]: doi-10-1038-s41746-026-02942-6 — "Closer alignment between AI-agent evaluators and any physician subgroup should not be interpreted as"
[^e17]: doi-10-1038-s41746-026-02942-6 — "The global rank concordance analysis (W = 0.798"
[^e18]: doi-10-1038-s41746-026-02942-6 — "These ordinal rankings were then converted into standardized scores of 100 (rank"
[^e19]: doi-10-1038-s41746-026-02942-6 — "all AI agents were powered by a single underlying LLM architecture"
