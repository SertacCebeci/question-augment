---
description: "In an instructor pilot, automated rubric scoring was rated fair in its consistency but weakest on construct validity, the gap a follow-up verification stage was added to close."
aliases: ["fairness-validity tension", "procedural fairness versus construct validity", "consistency versus construct validity in automated scoring"]
sources: ["arxiv-2512-12592"]
---
# Fairness–construct validity tension

Automated scoring can be judged on two properties that do not automatically go together. Procedural fairness asks that the same criteria apply to all students, so that similar answers get similar scores. The paper defines fairness as the condition "that all students have an equal opportunity to demonstrate their learning".[^c1] Construct validity asks whether the score reflects what the student knows: validity "concerns whether an assessment accurately measures what a student knows".[^c2] A scorer can satisfy the first while failing the second, because consistency says nothing about what the scorer keys on.

The mechanism is the one the paper reports. Its instructors rated automated scoring as fair in its consistency, a finding it states as "instructors found the system to be fair in its consistency".[^c3] They rated the same scoring lowest on construct validity: "its construct validity received the lowest rating of" any metric in the survey, with 55.6% agreement against 88.9% for consistency.[^c3b] The authors explain the gap by a property of the scorer, not of the rubric: "they rated its construct validity lower, noting that it tended to reward surface-level features over deep comprehension".[^c4] A scorer that rewards surface features applies those features the same way to everyone, which is exactly why it looks fair while being weak on construct. The authors summarize the result as "a crucial tension between procedural fairness and construct validity".[^c5]

The rubric is not the source of the gap in this pilot. Rubric generation was rated highly on both fairness and content validity, and the authors locate the difficulty in scoring against the rubric.[^c6] Their proposed remedy is not a more consistent scorer but a second stage that gathers evidence beyond the text, which they describe as the point where "purely automated methods may achieve consistency at the cost" of depth.[^c7] That remedy is the subject of [[interactive-verification-reassessment]].

My reading, not the paper's claim: the tension is a general shape. When a measure is made uniform across cases, it can become uniform in the wrong feature. The paper shows the shape in perception ratings from one set of raters; it does not measure the two properties against an external criterion of student understanding on the same scoring instrument.

## Limits

The evidence is a survey of nine instructors on a single set of exemplar answers. The paper says so directly: the study "did not include actual student data or responses".[^c8] The construct-validity rating is a perception, not a measurement of validity against an independent measure of what the students know. The consistency rating is also perceived, not measured as inter-rater agreement. Whether the tension is a true trade-off, or only a gap in one scorer's design, is not settled by this work. A scorer with better features might raise construct validity without losing consistency, and the pilot did not test one.

The pilot's own design blurs the picture. Instructors reviewed and could correct every automated score before it was used, so the consistency they rated was partly their own.[^c9] That supervision is part of why the scoring looked fair, and it is not an assumption of a fully automated system.

## Related

- [[validity-reliability-tradeoff]] — the same shape in bias testing: a design that secures one property narrows another; here the pair is framed as fairness and construct validity.
- [[interactive-verification-reassessment]] — the second stage the pilot added to address the construct-validity gap, with its own limits.
- [[expert-evaluation-guidance]] — a parallel case in LLM judging, where a finer rubric alone did not raise agreement and added guidance on what a correct answer must contain did.

[^c1]: arxiv-2512-12592 — "that all students have an equal opportunity to demonstrate their learning"
[^c2]: arxiv-2512-12592 — "Validity concerns whether an assessment accurately measures what a student knows"
[^c3]: arxiv-2512-12592 — "found the system to be fair in its consistency"
[^c3b]: arxiv-2512-12592 — "its construct validity received the lowest rating of"
[^c4]: arxiv-2512-12592 — "they rated its construct validity lower, noting that it tended to reward surface-level features over deep comprehension"
[^c5]: arxiv-2512-12592 — "between procedural fairness and construct validity"
[^c6]: arxiv-2512-12592 — "Rubric generation (Stage 1a) was perceived as"
[^c7]: arxiv-2512-12592 — "purely automated methods may achieve consistency at the cost"
[^c8]: arxiv-2512-12592 — "did not include actual student data or responses"
[^c9]: arxiv-2512-12592 — "reviewed all system-generated outputs (rubric, scores, questions)"
