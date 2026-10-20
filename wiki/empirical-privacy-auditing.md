---
description: "Privacy auditing estimates a mechanism's epsilon from outside: plant a canary in the data, guess its presence from the output, and convert the guess's TPR and FPR into a lower bound."
aliases: ["ContextLeak", "empirical privacy auditing", "empirical epsilon lower bound", "canary-based privacy audit"]
sources: ["arxiv-2512-16059"]
---
# Empirical privacy auditing

A differentially private mechanism comes with a theoretical budget ε. The paper's premise is that this bound is often loose in practice.[^c1] An empirical audit measures leakage from the outside instead. The auditor builds two neighbouring datasets that differ in one record, runs the mechanism many times, and tries to say from each output which dataset produced it. In private in-context learning the record is a planted canary, inserted by a hidden coin: the canary goes in "with a probability of 0.5" on each run, and the auditor does not know which way the coin fell.[^c2]

The auditor's score is its accuracy a, the share of runs in which its guess about the canary is right. Chance is the zero-leakage reference: "a 50% auditing accuracy (random guess) corresponds with no privacy leakage."[^c3] The same guesses also give a true-positive rate (canary runs flagged) and a false-positive rate (canary-free runs flagged).[^c4] The paper turns these rates into an empirical lower bound on ε, citing Nasr et al.: "an empirical ε lower bound (Nasr et al., 2021; 2023) is calculated as."[^c5] The extracted formula is garbled in the text I read. My reading is the standard form, the larger of log(TPR/FPR) and log((1−FPR)/(1−TPR)). The number is a floor on what the mechanism leaks through this attack, not a measurement of its full loss.

What makes the audit worst-case is what the auditor is allowed to try. Its goal is "to concurrently design a user query that maximally elicits the canary's disclosure," alongside a canary that the model can identify.[^c6] The estimate is therefore a maximum over attacks the auditor found, not an average over random exemplars. The reason given is that average-case audits can miss outliers: an exemplar that is rare "could still trigger privacy" violations.[^c7]

The reported result is that, across models and DP mechanisms, "the empirically recovered privacy loss increases monotonically with the" theoretical budget.[^c8] The gaps are large: "the large gaps we observe between theoretical and empirical guarantees highlight" how pessimistic the formal bounds are when run through a real pipeline.[^c9]

## Limits

- The bound is one-sided. A high audit score shows leakage at least that large. A low score shows only that this attack failed. Nothing here certifies that a mechanism leaks less than its stated ε. (my inference)
- The number depends on the attack. Auditing accuracy "is a function of the user query template," so a weaker template yields a smaller ε and a looser claim.[^c10] Prompt optimisation helped only a little: "GEPA slightly improves auditing accuracy."[^c11]
- The auditor is assumed to know the task. It has "information about the sensitive database and the structure of what each sensitive data point looks like."[^c12] How much a real adversary knows, and whether it can match the canary to the data, is not measured.
- The signal is not uniform across models. For smaller models the paper reports "we observe no meaningful improvement in auditing performance as ε increases."[^c13]
- The tested mechanisms are the paper's own choices. Report-Noisy-Max is "proposed for the classification task," and an embedding-space aggregation covers open-ended generation.[^c14] Other private ICL methods are not audited in this text.
- Monotonicity is shown over the budgets tested. Nothing here shows the relation is linear or that the bound is tight at any single ε.

## Related

- [[presence-probe-query-design]] — the query template that turns a planted canary into a presence signal the audit can score.
- [[llm-red-teaming]] — also a search for inputs that expose a model's weakness; the audit's target is a presence signal rather than a failure.
- [[exploitable-information-leakage]] — a different leakage measure, scored by a blind opponent's reconstruction of content rather than by a presence test.
- [[dp-stability-full-data-conformal-coverage]] — a formal DP guarantee of the kind an empirical audit checks against.
- [[personal-representation-leakage]] — the same exposure in personalised LLMs, where membership inference is one listed vulnerability.

[^c1]: arxiv-2512-16059 — "are often loose in practice"
[^c2]: arxiv-2512-16059 — "dataset with a probability of 0.5"
[^c3]: arxiv-2512-16059 — "a 50% auditing accuracy (random guess) corresponds with no privacy leakage"
[^c4]: arxiv-2512-16059 — "binary predictions of canary presence or absence induce a True"
[^c5]: arxiv-2512-16059 — "an empirical ε lower bound (Nasr et al., 2021; 2023) is calculated as"
[^c6]: arxiv-2512-16059 — "maximally elicits"
[^c7]: arxiv-2512-16059 — "a rare or outlier exemplar could still trigger privacy"
[^c8]: arxiv-2512-16059 — "the empirically recovered privacy loss increases monotonically with the"
[^c9]: arxiv-2512-16059 — "the large gaps we observe between theoretical and empirical guarantees highlight"
[^c10]: arxiv-2512-16059 — "is a function of the user query template"
[^c11]: arxiv-2512-16059 — "GEPA slightly improves auditing accuracy"
[^c12]: arxiv-2512-16059 — "the sensitive database and the structure of what each sensitive data point looks like"
[^c13]: arxiv-2512-16059 — "we observe no meaningful improvement in auditing performance as ε increases"
[^c14]: arxiv-2512-16059 — "the Report-Noisy-Max (RNM) strategy, proposed for the classification task"
