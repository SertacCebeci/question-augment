---
description: "A failure group is worth describing to a user when it both covers much of the model's errors and is often wrong; coverage and error ratio are separate measures, and each alone misleads."
aliases: ["coverage and error ratio", "worth-to-teach failure pattern", "error-ratio cutoff", "error coverage of a failure group"]
sources: ["arxiv-2512-21422"]
---
# Failure-group coverage and error ratio

A failure group is a set of evaluation instances that share a describable property, such as a human-annotated meta-label. Two numbers place it against a model's error record. **Coverage** is the group's share of all the model's errors: the wrong instances in the group divided by all wrong instances. **Error ratio** is the group's wrong-to-correct count: the wrong instances in the group divided by the correct ones. Coverage asks how much of the model's failing the group accounts for; error ratio asks how often the model fails inside the group.[^c1]

The two are kept apart because each alone misleads. Coverage alone rewards broad groups. A description such as "complex problem solving" can cover many errors and also many correct answers, and high coverage "may signal that the pattern is defined too broadly" to be actionable.[^c2] Error ratio alone rewards small groups. A low ratio makes a pattern less worth teaching, because a model that usually answers such instances correctly poses little risk to a user.[^c3] The paper adds that a low ratio is not always dismissable: in high-stakes domains even a modest risk may warrant attention, and rare failure modes of otherwise accurate models sit at low ratios.[^c4]

The paper's working threshold is an error ratio of 0.5 or higher, "suitable to teach users." Here 0.5 means the model is wrong "at least once in every three attempts" for that instance type.[^c5] A group that meets the threshold, with enough coverage to matter, is called worth-to-teach. Its own method for automatic discovery applies the same balance: it merges neighbouring erroneous regions "to balance coverage and error ratio," choosing merges that raise a combined error score.[^c6]

The numbers are specific to the model. On MMLU math, every meta-label group had an error ratio above 0.5 for GPT-3.5-turbo and together they covered all of its errors.[^c7] On MathCAMPS, one group accounted for 11.2% of GPT-4o's errors, while five groups accounted for 37.6% for GPT-3.5-turbo.[^c8] The same dataset and threshold therefore yield different numbers of patterns for different models. The paper reads this as a reason that "model choice matters, even with the same dataset" when a study is designed around teaching.[^c9]

What transfers is the split itself: an error region is worth naming only if it is both large and dense in errors, and those are two different quantities that a single accuracy figure hides. What does not transfer is the cutoff. The paper says that what counts as "high enough" "depends on the application," and it recommends either setting thresholds with stakeholders or reporting the teaching effect across a range of thresholds.[^c10]

## Limits

- The 0.5 cutoff is a choice the paper makes for its two datasets and five models, not a derived value. The authors say the thresholds should be examined against teaching outcomes, which they did not do.[^c11]
- Both measures are computed over one evaluation set D. A group's coverage depends on how many other errors the set contains, so the same pattern can move between thresholds when the set changes. The paper does not test this.
- The groups in the measurement are human meta-labels, so the measures say nothing about whether an unlabeled group that a method generates is worth teaching.
- Two datasets, one kind of task each, and one run per configuration. Whether high coverage with a high ratio predicts a user's gain is a separate question, taken up in [[error-anticipation-accuracy]].

## Related

- [[error-anticipation-accuracy]] — the teaching metric that the worth-to-teach groups feed; whether users learn to anticipate the failures these groups describe.
- [[failure-pattern-description-recall]] — how well automatic methods recover the groups these two measures select.
- [[over-reliance-discrimination-failure]] — a measured case where users could not tell wrong answers from right at all; a group-level measure like this one would not reveal that, since it is about the answerer's per-answer discrimination.
- [[abstention]] — a high-error-ratio region is a natural place to abstain; the paper's teaching is a user-side version of the same cut.

[^c1]: arxiv-2512-21422 — "Coverage measures the proportion of a model’s"
[^c2]: arxiv-2512-21422 — "may signal that the pattern is defined too broadly"
[^c3]: arxiv-2512-21422 — "the associated pattern becomes less compelling to"
[^c4]: arxiv-2512-21422 — "Low error ratios may also be needed to identify the rare"
[^c5]: arxiv-2512-21422 — "every three attempts for that instance type."
[^c6]: arxiv-2512-21422 — "To balance coverage and error ratio, we merge erroneous nodes iteratively"
[^c7]: arxiv-2512-21422 — "all meta-label groups have an error ratio"
[^c8]: arxiv-2512-21422 — "MathCAMPS, accounting for 11.2% of total error,"
[^c9]: arxiv-2512-21422 — "model choice matters, even with the same dataset"
[^c10]: arxiv-2512-21422 — "depends on the application."
[^c11]: arxiv-2512-21422 — "examine how different error-ratio and coverage thresholds affect teaching outcomes"
