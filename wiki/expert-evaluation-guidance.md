---
description: "Adding task-specific expert guidance to a fixed rubric raised LLM judges' agreement with each other and with humans, where a finer rubric alone did not, by naming what a correct report must contain."
aliases: ["expert evaluation guidance", "task-specific expert guidance", "domain-expert judging guidance", "expert reference points for LLM judges"]
sources: ["arxiv-2512-17776"]
---
# Expert evaluation guidance

A rubric says which criteria to check; it does not say what a correct answer to this particular task contains. A judge that grades a long expert report against generic criteria has to supply the domain content itself, and the paper's account is that non-expert judges, "including LLM judges", "may fail to detect subtle domain-specific errors or omissions".[^g1] Expert evaluation guidance is a second input, written per task: the required content elements and expert expectations, each stated as a concrete statement that can be checked directly against the report.[^g2] The judge reads it together with the fixed rubric, and the guidance "provides domain-grounded context and reference points" for the judgment.[^g3]

The guidance is built in two steps. A domain expert first reformulates the task into a report-style prompt, then derives the substantive content an adequate report should cover. A second expert from the same field cross-reviews it for omissions, redundancies and ambiguities.[^g4] The fixed part is separate and generic: the paper's rubric has "101 scorable rubric items in total", applied identically across tasks and organised into coverage ("whether required components are present") and quality ("the targeted components are executed to a high standard").[^g5]

The reason for the layer is a measured problem with the rubric alone. The paper's ablation runs four stages on the same judges: Vanilla, +Dimensions, +Granular Rubrics and +Expert Guidance. Vanilla reliability between the five LLM judges is moderate, and "reliability drops substantially under +Dimensions".[^g6] Breaking the criteria into granular items did not recover it, and Pearson’s r and Spearman’s ρ dropped at that stage.[^g7] Expert guidance is the stage that worked: it "attains the highest reliability" across metrics and the highest correlation with human judgments.[^g8] The authors read this as guidance that "clarifies what to look for under each criterion, enabling more consistent judgments across different LLM judges".[^g9]

So the granular rubric is not the fix for judge disagreement on its own. What the guidance adds is the task's own content, so that each fine-grained item has something concrete to be matched against.

## Limits

- The human comparison is small: "the 45 reports" with "two independent ratings from domain experts" each, 90 ratings in total.[^g10] The figures are averages over five judge models.
- The paper does not separate the gain from expert authorship from the gain from having task-specific content at all. The sections read contain no control where the guidance is written by a non-expert. My inference: the two effects are confounded in this design.
- The cost of writing guidance for each task, and whether it scales beyond the 50 tasks used, is not reported in the sections read.
- The authors state that the framework relies on judges that "may inherently exhibit biases relative to human experts"[^g11], and that the benchmark is "intended to complement, not replace, human oversight".[^g12]
- Where no expert has written the answer's content, the guidance has to be drafted some other way. The paper does not test an automatic drafting route. My inference: a guidance drafted by a model would carry the same blind spots the layer is meant to cover.

## Related

- [[expert-report-derived-atomic-rubrics]] — derives the rubric itself from an expert article; here the rubric is fixed and the task content lives in a separate guidance layer.
- [[llm-judge-validation-gap]] — judges in NLG papers are rarely checked against humans; this paper reports such a check and the agreement it found.
- [[llm-judge-biases]] — the judge failure modes that guidance is meant to offset on expert content.
- [[citation-back-tracking]] — the claim-level side of the same benchmark, which checks cited and uncited claims rather than the whole report.

[^g1]: arxiv-2512-17776 — "may fail to detect subtle domain-specific errors or omissions"
[^g2]: arxiv-2512-17776 — "enumerates the required content elements and expert expectations for each task as concrete, verifiable statements"
[^g3]: arxiv-2512-17776 — "provides domain-grounded context and reference points to"
[^g4]: arxiv-2512-17776 — "cross-reviewed by another"
[^g5]: arxiv-2512-17776 — "This process yields 101 scorable rubric items in total"
[^g6]: arxiv-2512-17776 — "reliability drops substantially under +Dimensions"
[^g7]: arxiv-2512-17776 — "Pearson’s r and Spearman’s ρ drop"
[^g8]: arxiv-2512-17776 — "+Expert Guidance attains the highest reliability"
[^g9]: arxiv-2512-17776 — "what to look for under each criterion, enabling more consistent judgments across different LLM judges"
[^g10]: arxiv-2512-17776 — "the 45 reports, we collected two independent ratings from domain experts"
[^g11]: arxiv-2512-17776 — "which may inherently exhibit biases relative to human experts"
[^g12]: arxiv-2512-17776 — "not replace, human oversight in the evaluation and use of"
