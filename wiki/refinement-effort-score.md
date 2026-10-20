---
description: "Graded by the effort still needed to repair a program for deployment, with each grade tied to the scope of the fix rather than similarity to a reference; judges miss that scope."
aliases: ["refinement effort", "repair-effort score", "tweak-versus-refactor scale", "deployability grade"]
sources: ["arxiv-2512-20159"]
---
# Refinement-effort score

A code answer can be graded by how much work it still needs before it is deployable. The AXIOM paper defines the score as "measuring the hypothetical effort needed to repair programs for deployment", so a higher grade means a program that needs less repair.[^c1]

The scale is anchored on function first. Grades of 3 and up go to a functionally correct program, one that can be "immediately deployed, though it may still require quality improvements."[^c2] Below that line, grades are separated by the scope of the fix. The paper's wording is that its scores are defined "By clearly defining each possible score based on the scope of required fixes", with examples such as "a localized tweak or a structural refactor".[^c3] For a functionally faulty program, the annotator decides "whether the functional changes in the diff is a structural refactor" (low grade) or a localized tweak (a higher grade).[^c4]

The point of the construction is that the grade names a kind of work. A reference-similarity metric asks how close a program is to a model answer. The paper's criticism of such rule-based metrics is that they "merely measure superficial similarity and require reference programs."[^c5] Binary pass or fail labels fail differently: they "reduce rich code behavior to a single bit of information, obscuring subtle errors."[^c6] A repair-effort grade keeps both the functional gate and the quality gradient, and it asks the grader a question it can answer by looking at the change that would be needed.

Judges, however, do not answer that question well. On the tweak-versus-refactor distinction, the paper reports that "no tested metric can reliably perform this task, with extremely low MCC" and that the values are "below 10.0, which is barely better than random guessing."[^c7] The failure has a direction: "They exhibit a pronounced tendency to overestimate the scope of changes,"[^c8] so localized corrections are read as architectural rewrites. The same paper finds that judges rank programs reasonably well while their absolute agreement with the ground truth is lower: "with ground-truth scores is considerably lower, with simpler metrics yielding higher agreement."[^c11] See [[ordinal-judge-fidelity]] for the ordering argument this extends.

Synthetic items graded on this scale are made by applying capped perturbations to a verified program, described in [[score-ceiling-perturbation]].

## Limits

- The refinement-effort test is conditional. The paper "only retain[s] programs whose functionality and code quality are correctly evaluated by the metric",[^c9] so the failure on scope is measured only where the judge had already got the other two questions right.
- The final grade is a human calibration, not a formula. The annotator is asked to "calibrate the target score to align with" the report, and the report includes static analysis, execution output and an LLM's code-quality note.[^c10] The scale says what a grade means; it does not by itself make a grader reliable, and the sections I read do not report how far two annotators agree on a tweak versus a refactor. (my inference)
- Coverage is code only (C++, Java, Python), with unit tests as the first gate. Whether a repair-effort scale carries over to prose answers, where "deployable" has no test suite, is my inference; the paper does not test it.
- The grade is about code quality as the annotator sees it. A grade of 2 versus 3 for a structural change depends on the annotator's reading of the diff, and the scale does not remove that dependence. (my inference)

## Related

- [[ordinal-judge-fidelity]] — a judge can keep the rank order of candidates while missing the absolute level; the paper finds the same split on code
- [[llm-judge-biases]] — the defect-first skew that makes a judge over-report faults and overstate the scope of a repair
- [[score-ceiling-perturbation]] — how the graded items on this scale are built
- [[refinement-quality-peak]] — iterative refinement can peak and fall; a repair-effort grade asks how far a finished artifact still is from deployable, a different axis

[^c1]: arxiv-2512-20159 — "measuring the hypothetical effort needed to repair programs for deployment"
[^c2]: arxiv-2512-20159 — "correct program to be immediately deployed, though it may still require quality improvements."
[^c3]: arxiv-2512-20159 — "By clearly defining each possible score based on the scope of required fixes"
[^c4]: arxiv-2512-20159 — "the annotator verifies whether the functional changes in the diff is a structural refactor"
[^c5]: arxiv-2512-20159 — "they merely measure superficial similarity and require reference programs."
[^c6]: arxiv-2512-20159 — "rich code behavior to a single bit of information, obscuring subtle errors."
[^c7]: arxiv-2512-20159 — "below 10.0, which is barely better than random guessing."
[^c8]: arxiv-2512-20159 — "They exhibit a pronounced tendency to overestimate the scope of changes"
[^c9]: arxiv-2512-20159 — "we only retain programs whose functionality and code quality are correctly evaluated by the metric"
[^c10]: arxiv-2512-20159 — "calibrate the target score to align with"
[^c11]: arxiv-2512-20159 — "with ground-truth scores is considerably lower, with simpler metrics yielding higher agreement"
