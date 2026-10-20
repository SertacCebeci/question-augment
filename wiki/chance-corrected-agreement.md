---
description: "Raw agreement between two graders can reach 100 percent while saying nothing about correctness; Cohen's kappa subtracts chance agreement and is undefined when every label is the same."
aliases: ["Cohen's kappa", "kappa", "chance-corrected inter-rater agreement", "grader agreement", "Scott's pi"]
sources: ["doi-10-48550-arxiv-2608-13867"]
---
# Chance-corrected agreement

Two graders that label the same items can agree closely while neither has shown that it can tell a defect from a success. The text's degenerate case: "Two graders that mark every submission PASS will agree on every item."[^c1] Their agreement is 100 percent and their usefulness is zero. The chapter's claim is that "Agreement is a calibration result, not a correctness verdict."[^c2]

Raw percent agreement "answers only one question: on what share of items did the labels match?"[^c3] The answer ignores how often each label appears by chance. The text's example: two raters each assign PASS to 90 of 100 items and disagree on 10. "Their observed agreement is therefore 90 percent." But if their labels were independent, given their marginal frequencies, they would agree on about 82 items (0.81 for PASS, 0.01 for FAIL). "That number appears strong until label prevalence is taken into account."[^c4]

Cohen (1960) corrected for this. Kappa is "the proportion of possible agreement beyond chance that the" raters achieved: observed agreement minus expected agreement, divided by one minus expected agreement.[^c5] In the example that gives kappa of about 0.44, which the text reads as moderate agreement beyond what the label frequencies predict. The mechanism is that a high raw rate can be produced by one dominant label, and kappa removes exactly that contribution.

The degenerate limit is where the correction breaks. With the always-PASS pair, observed and expected agreement are both 100 percent, so "Kappa is therefore undefined, not perfect."[^c6] A kappa of zero or undefined is a signal that the labels carry no variation from which agreement can be estimated, which is a different finding from agreement.

The text's own gate for an LLM-as-judge pair uses kappa rather than raw agreement "because percent agreement can overstate grader quality" when one label dominates.[^c7] The agreement floor, kappa threshold and minimum trial count were fixed before the judges ran. That gate "has been exercised only against replay fixtures," so it is shown as a design decision rather than a field result.[^c8]

Kappa does not repair an ambiguous rubric. "None of these measures can make an ambiguous rubric reliable. They make that ambiguity harder to hide behind a high raw agreement rate."[^c9] Fleiss (1971) "extended chance-corrected agreement to multiple raters and to designs in which different raters evaluate different items."[^c10] Scott's pi pools the category distribution to estimate chance.[^c9]

## Limits

- Kappa measures agreement, the consistency of labels. It does not measure whether the labels match what the system needs. That is the point of the chapter's claim that a grader must be checked against the judgment the system actually needs.[^c2]
- Kappa is sensitive to the class balance of the sample. The text's example uses a 90/10 split; a different prevalence in operation changes both the observed and the expected agreement.
- The text itself flags that its gate is tested only on replay fixtures.
- My inference: a kappa value near 0.44 is not, by itself, a threshold for deployment; the text gives a worked calculation, not a cut-off that should transfer to other rubrics.

## Related

- [[llm-judge-validation-gap]] — the same question for LLM judges, where agreement with a human label is not validity
- [[validity-reliability-tradeoff]] — the reliability side of the trade that kappa measures
- [[run-to-run-spread]] — the variance that agreement between repeated labels also inherits

[^c1]: doi-10-48550-arxiv-2608-13867 — "Two graders that mark every submission PASS will agree on every item."
[^c2]: doi-10-48550-arxiv-2608-13867 — "Agreement is a calibration result, not a correctness verdict."
[^c3]: doi-10-48550-arxiv-2608-13867 — "Raw percent agreement answers only one question: on what share of items did the labels match?"
[^c4]: doi-10-48550-arxiv-2608-13867 — "That number appears strong until label prevalence is taken into account."
[^c5]: doi-10-48550-arxiv-2608-13867 — "defined kappa as the proportion of possible agreement beyond chance that the"
[^c6]: doi-10-48550-arxiv-2608-13867 — "Kappa is therefore undefined, not perfect."
[^c7]: doi-10-48550-arxiv-2608-13867 — "percent agreement can overstate grader quality"
[^c8]: doi-10-48550-arxiv-2608-13867 — "The gate has been exercised only against replay fixtures,"
[^c9]: doi-10-48550-arxiv-2608-13867 — "None of these measures can make an ambiguous rubric reliable."
[^c10]: doi-10-48550-arxiv-2608-13867 — "extended chance-corrected agreement to multiple raters and to designs in which different raters evaluate different items."
