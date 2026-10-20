---
description: "On one course, students scored near ceiling on AI-permitted take-home modules and about 30 points lower on proctored exams, so module scores track the AI condition."
aliases: ["AI inflation effect", "AI-driven grade inflation", "AI-permissive score inflation", "take-home versus proctored score gap"]
sources: ["arxiv-2512-10758"]
---
# AI score inflation

A score on an assessment that permits generative AI is partly a property of the tool, not only of the learner. The paper's term is "the AI inflation effect"; in one place it is "the observed AI-driven grade inflation effect".[^c1] Its evidence is a single course, a graduate Python for data science course with N=41, that ran both formats. Students "achieved near-perfect scores on knowledge checks" where AI use was allowed, but "performance dropped significantly on the proctored exams".[^c2][^c3] The shift is in the upper tail: "90.2% of students scored 90% or higher" on the knowledge checks, while "only 4.9% achieved this on the exams".[^c4][^c5] The paper's reading is that the modular scores "be inflated by AI assistance and do not reflect true mastery".[^c6]

The same pattern appears in correlations with the proctored exam. The paper reports that modular assessments show a weaker link to exam performance, "suggesting greater susceptibility to AI-related score inflation", while the interconnected project ([[interconnected-problem-chaining]]) reaches "r=0.925" with the exam.[^c7][^c8]

The concept this changes is what a score carries. A take-home score normally reads as a measure of the learner's competence on the material. Under permitted AI it carries two things at once: the competence and the assistance the tool supplied. The proctored exam is the paper's reference because it removes the tool. Where the two diverge, the module score is no longer evidence about the competence the exam measures. My reading: this makes an item's validity relative to the AI condition it was given under. The same module under the other condition would give a different score. The paper does not run that comparison, so the claim is the inference, not the finding.

## Limits

- One course carries both formats. The paper says the Spring 2025 course "is the only course in which a proctored exam" was given.[^c9] The gap rests on one cohort of 41, and the other two offerings have no exam to compare against.
- Permission is not use. The take-home work is described as the place "where AI use was permitted".[^c10] The paper does not measure how many students used AI, so attributing the gap to AI is an inference from the design, not an observation of use.
- Format and tool are confounded. A take-home and a proctored exam differ in time, supervision and content. My reading: the design cannot separate the effect of the tool from these differences, because the same items were not given under both conditions.
- The reported coefficients do not agree across sections. The abstract gives "with modular assessments (r = 0.954, p < .001)" for the interconnected project,[^c11] while Figure 3 gives r=0.925 against the exam and r=0.671 for the modular work. I did not reconcile these; they are reported as they appear.
- The exam is taken as the reference for "true mastery". That is assumed, not tested, in the text read.

## Related

- [[interconnected-problem-chaining]] — the assessment structure the paper proposes as less exposed to this inflation.
- [[attempt-inflation]] — another headline number moved by a condition rather than by ability: there more attempts, here more assistance.
- [[short-form-check-blindness-to-open-ended-bias]] — the format of a check decides what it can show; the same question applies to a take-home versus a proctored exam.
- [[metacognitive-laziness]] — one way AI help can leave a learner's own monitoring undeveloped, which a take-home score would not reveal.

[^c1]: arxiv-2512-10758 — "The observed AI-driven grade inflation effect"
[^c2]: arxiv-2512-10758 — "students achieved near-perfect scores on knowledge checks"
[^c3]: arxiv-2512-10758 — "performance dropped significantly on the proctored exams"
[^c4]: arxiv-2512-10758 — "90.2% of students scored 90% or higher"
[^c5]: arxiv-2512-10758 — "only 4.9% achieved this on the exams"
[^c6]: arxiv-2512-10758 — "be inflated by AI assistance and do not reflect true mastery"
[^c7]: arxiv-2512-10758 — "suggesting greater susceptibility to AI-related score inflation"
[^c8]: arxiv-2512-10758 — "Interconnected project scores are strongly correlated with proctored exam scores (r=0.925)"
[^c9]: arxiv-2512-10758 — "is the only course in which a proctored exam"
[^c10]: arxiv-2512-10758 — "where AI use was permitted"
[^c11]: arxiv-2512-10758 — "with modular assessments (r = 0.954, p < .001)"
