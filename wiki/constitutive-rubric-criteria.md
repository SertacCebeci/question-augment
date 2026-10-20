---
description: "A rubric criterion is constitutive when a judge can grade it from rubric and response alone; presupposing criteria hand the hard judgment to the judge and agree less across judges."
aliases: ["constitutive versus presupposing criteria", "presupposing rubric", "self-contained rubric criterion"]
sources: ["doi-10-48550-arxiv-2606-03968", "doi-10-48550-arxiv-2605-03871"]
---
# Constitutive rubric criteria

A rubric criterion can carry its own grading knowledge, or it can name a property and leave the grader to supply what the property means. The QUBRIC authors call the first kind constitutive: "a judge can evaluate them using only the rubric text and the response, without" external knowledge.[^c1] Their example is a criterion that the response "explains that water expands when freezing due to" hydrogen bonding. Here the judge only checks for the presence of a stated content. The contrasting form, "the response provides a scientifically accurate explanation of why water expands when freezing", is presupposing: it "delegates the hard judgment (what counts as scientifically accurate) entirely to the judge."[^c2]

The authors say the distinction is a spectrum, and that "we design rubrics to be as constitutive as possible" because of what the embedding does to the judge.[^c3] They measured it. Four judges from three model families were compared against Claude Sonnet 4 as the reference. Against the reference, "constitutive rubrics achieve avg. κ=0.72", while "presupposing rubrics drop to κ=0.61".[^c4][^c5] Cohen's κ is reported rather than raw agreement because the two rubric types have different base rates; "rubrics are predominantly all-fail" for the presupposing type, which inflates raw agreement.[^c6] The authors report that "gradient holds across all four judges, including" the Claude family, where Sonnet 4.6 is compared with Sonnet 4.[^c7]

The mechanism the authors give is that grading knowledge written into the criterion reduces the work the judge must do, so the judges have less room to disagree on the hard part. The constitutive form also depends on the query. The authors say a co-designed query lets the rubric generator write constitutive criteria "that test reasoning about the" scenario, because the query contains the information the scenario needs.[^c8] A criterion of the first kind is therefore a property of the pair, the rubric and the question it was written for, and not of the rubric text alone.

A training-side result points the same way, though it was not measured as a judge-agreement study. EvoLM trains a rubric generator only to widen a small judge's score gap between preferred and dispreferred responses, and the criteria it learns change form. Early rubrics use labels; trained rubrics pack in "specific, verifiable expectations." In math, "the rubric concentrates 80% of the weight on a single criterion that embeds" the expected answer.[^c10] The authors describe the effect as moving evaluation "from holistic semantic judgment, which small judges perform unreliably, to pattern matching over concrete criteria."[^c11] The reading here is that a criterion carrying its own grading knowledge is what a judge can apply; the trained generator produces such criteria because the margin objective rewards them.

## Limits

- The agreement figures are against one reference judge, Claude Sonnet 4. That judge's own agreement with human annotators is "agreement with human annotation (86% accuracy," on 100 stratified samples, with κ=0.70.[^c9] The κ values therefore measure agreement with that judge, not with people.
- The constitutive and presupposing labels are the authors' classification. The text I read does not show how individual rubrics were labelled or how the labels were checked.
- The κ result is about consistency between judges. It is not a result about the policy's reward: the RL gains are reported for whole pipelines (query rewrite, contrastive rubrics, filtering), not for the criterion form alone.
- A presupposing criterion can be correct. The claim is about how consistently judges grade the two forms, not about which forms are true or good.
- The measurement is on rubrics for instruction following and related tasks, from one pipeline. No test with human graders grading the same criteria is reported in the parts I read.
- The EvoLM result is qualitative, over 100 evaluation prompts in four domains, and it does not measure judge agreement. A criterion that embeds the expected answer is checkable only if the answer is known in advance; that brings it close to the presupposing form this note warns about, and the paper does not test that tension (my inference).

## Related

- ungrounded-query-narrowing — constitutive criteria need a query that contains its scenario; a narrowed query without grounding pushes the rubric toward refusal checks.
- [[rubric-formation-gap]] — the bottleneck there is deciding what to check; the constitutive form fixes the content of the check inside the criterion itself (my inference from the two descriptions).
- [[atomic-criteria-questions-for-prompt-alignment]] — also splits a requirement into yes/no criteria; the constitutive question is whether each criterion carries the content its grader needs.

[^c1]: doi-10-48550-arxiv-2606-03968 — "a judge can evaluate them using only the rubric text and the response, without"
[^c2]: doi-10-48550-arxiv-2606-03968 — "delegates the hard judgment (what counts as scientifically accurate) entirely to the judge."
[^c3]: doi-10-48550-arxiv-2606-03968 — "we design rubrics to be as constitutive as possible"
[^c4]: doi-10-48550-arxiv-2606-03968 — "constitutive rubrics achieve avg. κ=0.72"
[^c5]: doi-10-48550-arxiv-2606-03968 — "presupposing rubrics drop to κ=0.61"
[^c6]: doi-10-48550-arxiv-2606-03968 — "rubrics are predominantly all-fail, inflating raw"
[^c7]: doi-10-48550-arxiv-2606-03968 — "gradient holds across all four judges, including"
[^c8]: doi-10-48550-arxiv-2606-03968 — "constitutive criteria that test reasoning about the"
[^c9]: doi-10-48550-arxiv-2606-03968 — "agreement with human annotation (86% accuracy,"
[^c10]: doi-10-48550-arxiv-2605-03871 — "the rubric concentrates 80% of the weight on a single criterion that embeds"
[^c11]: doi-10-48550-arxiv-2605-03871 — "judgment, which small judges perform unreliably, to pattern matching over concrete criteria"
