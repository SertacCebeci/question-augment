---
description: "Scoring constraint compliance and semantic accuracy as separate axes lets a response fail one and pass the other; the paper's evidence that the axes are independent is weak."
aliases: ["constraint compliance versus semantic accuracy", "CC and SA dimensions", "orthogonal constraint and content scores", "constraint-content separation"]
sources: ["arxiv-2512-17920"]
---
# Constraint compliance dissociated from semantic accuracy

A response to an instruction can be scored on two things at once: whether it obeys the form of the instruction, and whether its content is right. The paper separates them on purpose. Its judges answer two questions: does the response "satisfy the word-count requirement," and "does the response correctly explain the concept."[^d1][^d2] The reason given is that prior work "conflates constraint violations with semantic errors," so that it is unclear whether a model fails because it cannot follow instructions or because it cannot keep the knowledge.[^d3]

The claim of the note is that the two can come apart. In the same runs, the semantic score rises with more context while the compliance score has the U-shape described in [[constraint-compliance-u-curve]]. The paper reports that "Semantic accuracy improves monotonically with more context,"[^d4] while compliance does not. On this reading a response can keep its content and miss its length, and a single accuracy number would hide which failed.

The paper goes further and calls the two axes independent: "Constraint compliance and semantic accuracy are statistically orthogonal."[^d5] The reported correlation is r = 0.193 with p = 0.084,[^d10] and the paper describes the average constraint change as "larger than semantic change magnitude across compression levels."[^d6] The axes were also judged with different reliability: compliance has a Fleiss' kappa of 0.90, and the paper says "CC is a highly reliable, objectively measurable dimension."[^d7] Semantic accuracy has kappa 0.25, and the paper reads this as "greater subjective interpretation among judges."[^d8]

## Limits

- Orthogonality is not shown by a non-significant correlation. With 72 conditions, r = 0.193 at p = 0.084 is not significant at the paper's own threshold, and that is not evidence that the two are independent. A small association could be present and go undetected. My inference: the paper's word "orthogonal" claims more than the test supports. The claim that compliance and accuracy are distinct may still hold, but this text does not establish it.
- The two axes are measured on different scales. Compliance is a count-based deviation, and accuracy is a 0 to 10 rubric. A ratio of magnitudes, such as the reported 2.9 times larger constraint change, depends on the units, and no common unit is given. My inference: the ratio says more about the scoring than about the models.
- The kappa gap is partly built in. A word count is close to mechanical, so high agreement on compliance is expected from the rubric's design, while semantic accuracy requires judgement. The 0.90 figure shows the count is easy to score; it does not show that compliance is the more important or more real dimension. The paper uses it that way, and I do not read it that way.
- Semantic accuracy is weakly measured. Its kappa of 0.25 is "fair" in the paper's own label, so the dissociation rests on one axis that the judges themselves disagree about. A null or a positive result on that axis could shift with a different jury.
- The paper drops its third axis. It collects functional completeness, but says "our primary analysis focuses on CC and SA due to their higher inter-rater reliability,"[^d9] so the separation is between two of three measured dimensions, chosen partly by reliability.
- The constraint is one word count. "Constraint compliance" here means length compliance on a fixed-length explanation. The paper's broader scope, "format requirements (JSON, structured output)" and similar, is listed as a generalization and not tested in the parts read.
- A dissociation can also come from the judges. Scores are averages across three LLM judges, and the text read does not show that a judge's count matched a program's count on the same responses.

## What survives the transfer

The design survives in outline: score the form of an answer and its content on separate scales, and check each axis's reliability before reading any pattern from it. The independence claim does not survive as stated. Whether the two axes move together in other tasks is a question this text does not answer.

## Related

- [[constraint-compliance-u-curve]] — the compliance curve that makes the two axes diverge in these runs
- [[constraint-salience-against-helpfulness-prior]] — the paper's account of why compliance and content can fail separately
- [[format-compliance-normalized-performance-and-format-variance]] — scoring accuracy only on format-compliant outputs confounds skill with format following, the same problem seen from the other side
- [[grounding-answer-dual-axis-audit]] — another two-axis audit, here answer correctness against evidence overlap
- [[orthogonal-violation-attribution]] — distractors built to violate one constraint at a time, a way to attribute failures to one axis

[^d1]: arxiv-2512-17920 — "satisfy the word-count requirement"
[^d2]: arxiv-2512-17920 — "Does the response correctly explain the concept"
[^d3]: arxiv-2512-17920 — "conflates constraint violations with semantic errors"
[^d4]: arxiv-2512-17920 — "Semantic accuracy improves monotonically with more context"
[^d5]: arxiv-2512-17920 — "Constraint compliance and semantic accuracy are statistically orthogonal"
[^d6]: arxiv-2512-17920 — "than semantic change magnitude across compression levels"
[^d7]: arxiv-2512-17920 — "CC is a highly reliable, objectively measurable dimension"
[^d8]: arxiv-2512-17920 — "greater subjective interpretation among judges"
[^d9]: arxiv-2512-17920 — "focuses on CC and SA due to their higher inter-rater reliability"
[^d10]: arxiv-2512-17920 — "orthogonal (r=0.193, p=0.084)"
