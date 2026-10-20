---
description: "Fixing a dataset and a deterministic success criterion narrows the solution space, so a solver cannot swap in an easier, familiar variant; the paper argues this sharpens measurement."
aliases: ["semi-structured assessment", "semi-open-ended project", "deterministic success criteria", "fixed problem instance with a pass metric"]
sources: ["arxiv-2512-10758"]
---
# Solution-space pinning

An open prompt leaves the solver to choose which problem to solve, and the choice is not neutral. The paper's example is a fully open prompt such as "analyze a dataset of your choice".[^c1] Its claim is that the unconstrained choice lets the solver pick an instance inside its own familiar territory: "we prevent the AI from choosing an easier, more familiar problem for which it has been heavily trained".[^c2]

Pinning, as the paper defines it, has two parts: "specifying a particular dataset or problem instance" and "defining deterministic success criteria".[^c3] The criterion does more than fix a target. The paper says a deterministic metric "ensures that students must optimize for correctness" and not rely on "AI-generated outputs that merely appear plausible".[^c4] The proposition is that a project with this structure "is a more reliable measure of student competency than a fully open-ended project".[^c5]

The paper's comparison is observational. A fully open 2024 project was set against a semi-open 2025 project. The two showed "no meaningful differences in creative direction, data modality, or analytical framing",[^c6] but the open design "was associated with narrower data coverage, convergence toward highly discoverable inflation datasets, and fewer modeling approaches per project".[^c7] That is the paper's evidence that open choices converge.

The concept this changes is what a question specifies. An answer is the product of two choices: which problem to solve, and how to solve it. Pinning fixes the first, so that a score reflects the second. My reading: the constraint sits in the question, not in the answering, and that is what makes the answers comparable across solvers. The logic is the one behind any fixed item.

## Limits

- The premise is argued from citation. The paper states that "LLMs consistently follow the path" of least resistance, preferring familiar patterns, and cites work it does not test here.[^c8]
- Citations are unresolved at the point the argument needs them. The claim that detection tools are unreliable reads "as AI detection tools are notoriously unreliable", and the references in that passage appear as "[?], [?]" in the text read.[^c9]
- The convergence finding is a comparison of two cohorts. The paper does not run a model on the open and pinned projects to check that the pinned one is harder for it.
- "More reliable" is asserted. The text read reports no reliability coefficient for the pinned project. The reliability claim rests on the argument and on the observed spread, and my reading is that it is not measured here.
- Pinning trades against discoverability. The paper's own observation is that open projects drift toward "highly discoverable" datasets, and a pinned popular dataset is discoverable too. My inference: the constraint holds only as far as the instance is unfamiliar to the solver, and the paper does not say how to tell.
- A deterministic threshold tells the solver what to optimize. The paper's example is a score target on a held-out set. Whether that moves effort toward the metric and away from the problem is not tested.

## Related

- [[interconnected-problem-chaining]] — the paper's other proposition, which constrains the sequence of sub-problems rather than the instance solved.
- [[item-writing-guidelines]] — the older tradition of fixing what a question asks, written for human answerers.
- [[option-matching-shortcut]] — a closed format can be reached by matching choices; pinning removes a different freedom, the choice of problem.
- [[short-form-check-blindness-to-open-ended-bias]] — a question's format decides what a check can see, the same question of what a constrained measurement reveals.

[^c1]: arxiv-2512-10758 — "analyze a dataset of your choice"
[^c2]: arxiv-2512-10758 — "we prevent the AI from choosing an easier, more familiar"
[^c3]: arxiv-2512-10758 — "specifying a particular dataset or problem instance"
[^c4]: arxiv-2512-10758 — "that merely appear plausible"
[^c5]: arxiv-2512-10758 — "reliable measure of student competency than a fully open-ended project"
[^c6]: arxiv-2512-10758 — "creative direction, data modality, or analytical framing"
[^c7]: arxiv-2512-10758 — "convergence toward highly discoverable inflation"
[^c8]: arxiv-2512-10758 — "LLMs consistently follow the path"
[^c9]: arxiv-2512-10758 — "as AI detection tools are notoriously unreliable"
