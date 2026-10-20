---
description: "A fixed rubric detects only errors its criteria name in advance; injected clinical hallucinations most often left medical rubric scores tied, so a high score does not show absence of error."
aliases: ["rubric blind spot", "rubric-blind errors", "tied rubric scores", "rubric coverage limit"]
sources: ["doi-10-48550-arxiv-2609-12718"]
---
# Rubric blind spot

A rubric is a fixed list of criteria, each checked against a response, and the score is the count of criteria met. The blind spot is what such a score cannot register. The test that exposes it is a matched pair: take one response, change one clinically relevant fact, and see whether the score moves. Across three medical benchmarks the paper found that the commonest outcome was no movement at all. In its words, "tied scores are the most common outcome, indicating that many introduced hallucinations produce no change in the rubric score."[^r1]

## Mechanism

The rubric can only score what it names. The paper states the limit directly: a rubric "can only detect errors that the rubric specifies in advance."[^r2] A criterion helps when it points at the fact that the error changes: "Rubrics are more likely to discriminate when they contain criteria that specify the fact altered by the error."[^r3] Within one rubric the effect is concrete. Removing the fact-checking criteria from a RubricHub rubric raised the share of ties "from 3.6% to 39%" on hard hallucinations, and cut the paired AUROC from 0.792 to 0.662.[^r4]

Some error types resist enumeration. For dosage and threshold errors, "a rubric-author would need to predict every drug or threshold that should be mentioned and its correct value, which quickly becomes infeasible."[^r5] Additive errors are worse: they "introduce claims that a fixed rubric cannot ever enumerate."[^r6] Even an explicit criterion can fail where checking needs outside evidence. Among 31 HealthBench questions with a criterion against citing false papers, the grader "did not penalise the fabricated citation in any case."[^r7]

The gap is also a matter of density. HealthBench averages 11.45 criteria per question and HealthBench Professional 2.16, and the paper concludes that "sufficient rubric density is important to robustly discriminate correct and error-injected responses."[^r8] A high score on a sparse rubric therefore says even less than the same score on a dense one.

The consequence for interpretation is stated plainly: "A rubric score shows that a response meets the criteria being assessed, but does not show that clinically important errors are absent."[^r9]

## Limits

- The errors are injected, not natural. The paper says it studies "controlled injected errors rather than naturally occurring hallucinations."[^r10] Natural errors may fall elsewhere on the enumeration axis.
- Clinical significance is a reviewer judgement. Reviewers judged "80.3% of responses as diagnosis- or management-changing", but pairwise agreement was 69.2%, rising to 84% only after four error types were dropped.[^r11] The paper adopts that criterion from earlier work; it is a convention, not a measured harm.
- One grader model per benchmark. The paper says "Our medical benchmark experiments use a single grader model per benchmark", so grader sensitivity is not fully characterised.[^r12]
- The grader-capability result is narrower than the headline. More specific rubrics narrowed the gap between grader models, but the most specific rubric and grader pairings do not consistently separate the hardest hallucinations from correct responses.[^r13]
- The study covers medical rubrics only. Whether the same blind spot governs rubrics for answers to ordinary questions is untested here. My inference: any fixed criterion list has the same enumeration limit, but the size of the effect is not measured outside medicine.

## Related

- [[rubric-formation-gap]] — the same bottleneck seen from the criteria side: which checks get written, not how they are applied.
- [[constitutive-rubric-criteria]] — a criterion form a judge can grade from rubric and response alone; the fact-specific criteria here are one way a criterion does concrete work.
- [[threshold-gated-rubric-coverage]] — a coverage score over a fixed clinician rubric; it inherits the same limit of naming criteria in advance.
- [[controlled-error-injection]] — the matched-pair construction used to make these blind spots visible.
- [[claim-decomposed-retrieval-check]] — the complementary check the paper proposes for errors no criterion names.

[^r1]: doi-10-48550-arxiv-2609-12718 — "indicating that many introduced hallucinations produce no change in the rubric score"
[^r2]: doi-10-48550-arxiv-2609-12718 — "it can only detect errors that the rubric specifies in advance"
[^r3]: doi-10-48550-arxiv-2609-12718 — "Rubrics are more likely to discriminate when they contain criteria that specify the fact altered by the error"
[^r4]: doi-10-48550-arxiv-2609-12718 — "driven by an increase in tied scores from 3.6% to 39%"
[^r5]: doi-10-48550-arxiv-2609-12718 — "a rubric-author would need to predict every drug or threshold that should be mentioned and its correct value, which quickly becomes infeasible"
[^r6]: doi-10-48550-arxiv-2609-12718 — "introduce claims that a fixed rubric cannot ever enumerate"
[^r7]: doi-10-48550-arxiv-2609-12718 — "the grader did not penalise the fabricated citation in any case"
[^r8]: doi-10-48550-arxiv-2609-12718 — "sufficient rubric density is important to robustly discriminate correct and error-injected responses"
[^r9]: doi-10-48550-arxiv-2609-12718 — "but does not show that clinically important errors are absent"
[^r10]: doi-10-48550-arxiv-2609-12718 — "we study controlled injected errors rather than naturally occurring hallucinations"
[^r11]: doi-10-48550-arxiv-2609-12718 — "Reviewers judged 80.3% of responses as diagnosis- or management-changing"
[^r12]: doi-10-48550-arxiv-2609-12718 — "Our medical benchmark experiments use a single grader model per benchmark"
[^r13]: doi-10-48550-arxiv-2609-12718 — "do not consistently distinguish difficult hallucinations from correct responses"
