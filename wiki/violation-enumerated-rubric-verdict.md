---
description: "A rubric item counts as met only when the grader lists no violated failure guideline for it; in training ablations this nested check beat a binary met-or-unmet verdict on the same item."
aliases: ["violation-list grading", "nested guideline checking", "violation-based rubric scoring"]
sources: ["arxiv-2512-23707"]
---
# Violation-enumerated rubric verdict

A grader asked whether an answer meets a requirement can be made to answer in three shapes: a yes or no, a number, or a list of the ways the answer fails some named standard. The research-plan paper uses the third shape, and the difference lies in what the grader must write before it decides. For each goal-specific rubric item, "the grader must explicitly identify which, if any, general guidelines" are violated by the part of the plan that addresses the item.[^c2] The item is marked satisfied "if and only if the grader returns" an empty list of violations.[^c1] The score for a plan is the fraction of its items with an empty list.

The standard is a fixed set of seven general guidelines, such as "Handles all criteria", "No overlooked flaws" and "Well justified rationale". The paper says it derives them from failure modes of model-written research ideas in earlier work: "We derive these guidelines from" common failure modes such as vague proposals or overlooked flaws.[^c3] So the grader is not asked for an overall impression of an item. It is asked to name, for that item, a failure from a list that is already known to matter, and an item with no named failure passes.

The mechanism is a two-level test. The first level asks whether the rubric requirement is addressed at all. The second asks whether the addressing survives each guideline. The paper's ablation removes only the second level and keeps the binary first level: "without our proposed nested checking of the general guidelines, only grading whether the instance-specific rubric items were" addressed or not "leads to much worse scores".[^c5] The authors also state the reason they kept the structure: "we found that this violation-based grading yields more grounded scores than direct binary or numeric rating".[^c4] Because each verdict is a list, the scores can be broken down by guideline, which "allows us to decompose performance along these axes".[^c6]

Two further choices in the grader prompt bear on the same mechanism. The authors note that locally hostable models "are often too lenient when grading rubrics directly", so they "explicitly instruct the grader to first list weaknesses before proceeding with item-wise grading".[^c7][^c12] The stated effect is stricter grading and better agreement with a larger judge. The same leniency shows up in people: human annotators "were generally lenient, marking rubric items as satisfied if" the plan addressed them even imperfectly.[^c8]

## Limits

The evidence for the nested check is a single ablation, on training runs scored by Claude-4-Sonnet on a validation set.[^c9] The binary arm's number is in the paper's Table 2, not in the prose, and I did not read it into this note. The comparison is against one alternative verdict form only; the paper does not test a numeric verdict with the same guidelines.

The enumeration is only as good as the guideline list. The seven guidelines were chosen from prior failure-mode work, and nothing in the paper shows that a different list would give the same ordering. A grader that lists violations can also miss the item it was asked about: the paper reports that for one guideline, "the cost and effort efficiency of the plans worsens according to the held-out grader" while the self-grader scored it as improving.[^c11] The structure does not guarantee that the list is right.

Agreement is modest at the level of single judgments. The jury's majority vote reached a Cohen's κ "score of 0.297 with the human consensus", and the paper concedes that "automated grading may be noisy" per sample, with useful signal only in aggregate.[^c10] A violation list makes the reasons visible; it does not make each reason correct.

## Related

- [[expert-report-derived-atomic-rubrics]] — atomic yes/no checklists over report content; there the items are the content, here the items are fixed and the verdict per item is an enumerated failure list.
- [[pretraining-grounded-rubric-self-play]] — the rubric is kept from the generator as privileged information; this note is about how the grader turns that rubric into a verdict.
- [[pessimistic-min-judge-aggregation]] — another way to make a rubric verdict strict: take the minimum over judges, rather than enumerate failures inside one judge.

[^c1]: arxiv-2512-23707 — "We consider a rubric item satisfied if and only if the grader returns"
[^c2]: arxiv-2512-23707 — "the grader must explicitly identify which, if any, general guidelines"
[^c3]: arxiv-2512-23707 — "We derive these guidelines from"
[^c4]: arxiv-2512-23707 — "we found that this violation-based grading yields more grounded scores than direct binary or numeric rating"
[^c5]: arxiv-2512-23707 — "without our proposed nested checking of the general guidelines, only grading whether the instance-specific rubric items were"
[^c6]: arxiv-2512-23707 — "allows us to decompose performance along these axes"
[^c7]: arxiv-2512-23707 — "often too lenient when grading rubrics directly"
[^c8]: arxiv-2512-23707 — "annotators were generally lenient, marking rubric items as satisfied if"
[^c9]: arxiv-2512-23707 — "We report Claude-4-Sonnet rubric grading scores on the"
[^c10]: arxiv-2512-23707 — "automated grading may be noisy"
[^c11]: arxiv-2512-23707 — "the cost and effort efficiency of the plans worsens according to the held-out grader"
[^c12]: arxiv-2512-23707 — "we explicitly instruct the grader to first list weaknesses before proceeding with item-wise grading"
