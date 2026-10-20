---
description: "Graded test items can be built by applying rules that each cap a program's score, so the final grade is the minimum of the starting grade and the caps, which sets the grade balance by design."
aliases: ["rule-guided perturbation", "perturbation with score ceilings", "capped perturbation synthesis", "controlled-grade benchmark synthesis"]
sources: ["arxiv-2512-20159"]
---
# Score-ceiling perturbation

Many synthetic evaluation sets are made by asking a model to write answers of varying quality, and whatever grade comes out is what the model happened to produce. A different route fixes the grade first and edits a good answer until it matches. AXIOM starts from a verified high-quality program and applies a sequence of rules. Each rule is a natural-language instruction for one kind of change, paired with a ceiling: the highest grade the program may keep after that change.[^c1]

Ceilings compose by minimum. After a sequence of rules, the score "equals to min" of the original score and every ceiling in the sequence.[^c2] So the generator controls the target grade by choosing which ceilings to draw. The paper samples a number of steps and a ceiling for each, and makes one of the ceilings equal to the target. Each step is run through an LLM that first decides whether the rule is feasible; if it refuses, the attempt is dropped.[^c3]

Only the final functional status is checked, not each intermediate step. Programs with a target of 3 or 4 must pass the unit tests, and programs with a target of 1 or 2 must fail at least one, and anything else is discarded.[^c4] The paper calls this outcome-based check efficient, since intermediate edits need no verification. Context disruption adds a second kind of item: a program is paired with an unrelated requirement, and "their 0-point score is absolute," so no human calibration is needed for that grade.[^c5]

The motivation is balance. Prompting an LLM for programs directly is said to produce "uncontrolled error types and unbalanced score distributions."[^c6] Each rule is meant to map to one score: "Each rule defines a specific transformation mapping to a specific score."[^c7] The authors report that the resulting benchmark, with "1962 programs in C++, Java, and Python," provides "a balanced score distribution owing to the controllable nature" of the construction.[^c8]

The ceiling is a target, not the final grade. Each candidate is then calibrated by a human, who is asked to "calibrate the target score to align with" a report of the diff, the rules, static analysis, execution output and an LLM's quality note.[^c9] The grades themselves are those of [[refinement-effort-score]]. The paper's 45 rules are hand-written, not learned.[^c10]

## Limits

- Balance is claimed for the target grades. The sections I read do not show how far human calibration moved the grades, so the final distribution's balance is not confirmed here. (my inference)
- The authors state a design goal, not a measured result, for transfer: rules "should be generalizable across programming languages and domains."[^c11] The rules were written by hand for code.
- A ceiling says what flaw is intended. Unit tests confirm the functional half; the code-quality half depends on the rule being carried out faithfully and on the annotator. A model's edit can introduce a different flaw than the one named. (my inference)
- The authors acknowledge that the benchmark "may not fully represent the complexity of real-world projects" with private, repository-level dependencies.[^c12]
- The method needs a test oracle for the functional gate. Prose answers have no unit tests, so the min-of-ceilings control does not transfer as it stands; any transfer to prose is my inference.

## Related

- [[refinement-effort-score]] — the grade scale these items are calibrated onto
- [[reference-answer-defect-audit]] — finds defects in benchmarks after they are built; this note is about building graded items with a known grade to begin with
- [[llm-judge-validation-gap]] — the reason a human-calibrated, graded benchmark matters: most judge studies were never checked against human scores

[^c1]: arxiv-2512-20159 — "of a natural language instruction on how to perform the code transformation, and a score ceiling"
[^c2]: arxiv-2512-20159 — "equals to min"
[^c3]: arxiv-2512-20159 — "return null"
[^c4]: arxiv-2512-20159 — "scores of 3 and 4 must pass all tests, while those targeting scores of 1 or 2 must fail at least one."
[^c5]: arxiv-2512-20159 — "their 0-point score is absolute"
[^c6]: arxiv-2512-20159 — "leading to uncontrolled error types and unbalanced score distributions."
[^c7]: arxiv-2512-20159 — "Each rule defines a specific transformation mapping to a specific score"
[^c8]: arxiv-2512-20159 — "provides a balanced score distribution owing to"
[^c13]: arxiv-2512-20159 — "with 1962 programs in C++, Java, and Python"
[^c9]: arxiv-2512-20159 — "calibrate the target score to align with"
[^c10]: arxiv-2512-20159 — "We manually curate 45 perturbation rules."
[^c11]: arxiv-2512-20159 — "All rules should be generalizable across programming languages and domains"
[^c12]: arxiv-2512-20159 — "may not fully represent the complexity of real-world projects"
