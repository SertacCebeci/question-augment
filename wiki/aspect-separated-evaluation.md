---
description: "One LLM pass per assessment aspect, each checked against the reference, is proposed to curb loss of focus and hallucination; the gain was measured only together with other changes."
aliases: ["multi-step prompting", "per-aspect assessment prompts", "stepwise aspect evaluation", "aspect-by-aspect grading"]
sources: ["arxiv-2511-18221"]
---
# Aspect-separated evaluation

When a language model grades an answer, the grading criteria can be asked of it in one prompt or in several. A unified prompt asks for every criterion at once. The alternative splits the grading into steps, and each step asks for one criterion. In the circuit-analysis homework study, the earlier baseline was the unified kind: "Five aspects of student work were assessed with a unified prompt:" completeness, method, final answer, arithmetic accuracy and unit correctness.[^c1] The authors name the problem with that design as a load problem: "that GPT-4o must consider all aspects of the assessment" at the same time, "which can lead to a loss of focus and an increased likelihood of hallucinations."[^c2]

The split works like this. Each step receives the same material, namely the reference solution, the student's solution and the problem-specific context, and "focuses on evaluating a specific aspect of the student's work."[^c3] The steps are not one per criterion. Final answer and arithmetic are merged, because "Since a correct final answer often implies" no arithmetic error, so "the evaluation of arithmetic calculations and final answers is combined into a single step."[^c4] The four resulting steps cover final answer and arithmetic, completeness, method and units. A last pass summarises the step outputs, so a student can read one overview instead of four reports.

Each step can carry its own acceptance rule. The method step, for example, tells the model that a student "may use an alternative method" and that "If the final answer is correct, assume the method used was valid."[^c5] A unit rule is written into the units step, so that a value in cents can be converted and compared with a value in dollars. A single unified prompt would have to hold all of these rules at once.

The mechanism the authors give is attentional. "By isolating each evaluation focus," the approach is said to "mitigate GPT-4o's tendency to hallucinate."[^c6] My reading, not the paper's test: a step that asks about one thing leaves the model less to track in each call, so fewer irrelevant judgements fill the output. This is the same budget logic that [[hint-induced-focus-narrowing]] uses for hints, run in the other direction. There, a cue narrows what a judge looks at; here, the step is the narrowing, and it is chosen so that nothing is left out of the set of steps.

The measured result is for the whole package, not for the split alone. On 87 raw student solutions, the correct-response rate, where a response counts as correct "if GPT-4o accurately evaluates all aspects," rose "from 74.71% to 97.70% after applying" the enhanced prompting and augmented data.[^c7][^c8] Of 13 previously wrong examples, "11 were correctly addressed using" the enhanced methods.[^c9] The enhancement combined the step split, extra problem context and targeted hints, so the table does not show what the split contributed by itself.

## Limits

- The split was never tested alone. The 74.71% to 97.70% figure, and the 11 of 13 repaired examples, come from prompts that also carried augmented context and hints. The paper reports no run of the unified prompt with context added and no run of the steps without hints.[^c8]
- The sample is small and the test cases were not held out. The enhancement was checked "on the examples shown in TABLE II, which include cases where" GPT-4o had erred before, and the hints were written "to address the common errors shown in TABLE" II.[^c10][^c11] The gain is therefore on the error cases the design was built from.
- One model, one course. The authors say the framework is "broadly applicable for addressing limitations in other LLMs," but no other model was run.[^c12]
- The split merges arithmetic into the final-answer step on the assumption that a correct answer implies correct arithmetic. That assumption is the authors' and is not tested here; the paper's own example "GPT-4o still fails to provide a correct" assessment in a notation case shows a step can still err.[^c13]
- The steps read circuit diagrams only through text summaries that were prepared by hand. The authors list "integrating information from circuit diagrams into the framework" as future work.[^c14]

## Related

- [[hint-induced-focus-narrowing]] — the same attention-budget concern, seen from hints placed in a single judge prompt; the two papers measure opposite sides of the trade-off
- [[typed-error-reflection]] — a second pass that checks one output against named error types, rather than one pass per aspect of the solution
- [[recursive-rubric-decomposition]] — splits the criteria themselves into finer items; this note splits the judging calls over a fixed set of aspects

[^c1]: arxiv-2511-18221 — "Five aspects of student work were assessed with a unified prompt:"
[^c2]: arxiv-2511-18221 — "simultaneously, which can lead to a loss of focus and an"
[^c3]: arxiv-2511-18221 — "focuses on evaluating a specific aspect of"
[^c4]: arxiv-2511-18221 — "calculations and final answers is combined into a single step."
[^c5]: arxiv-2511-18221 — "If the final answer is correct, assume the method used was valid."
[^c6]: arxiv-2511-18221 — "By isolating each evaluation focus,"
[^c7]: arxiv-2511-18221 — "considered correct if GPT-4o accurately evaluates all aspects"
[^c8]: arxiv-2511-18221 — "response rate increases from 74.71% to 97.70% after applying"
[^c9]: arxiv-2511-18221 — "responses contained errors, 11 were correctly addressed using"
[^c10]: arxiv-2511-18221 — "examples shown in TABLE II, which include cases where"
[^c11]: arxiv-2511-18221 — "designed to address the common errors shown in TABLE"
[^c12]: arxiv-2511-18221 — "enhancement framework proposed in this paper is broadly"
[^c13]: arxiv-2511-18221 — "GPT-4o still fails to provide a correct"
[^c14]: arxiv-2511-18221 — "integrating information from circuit diagrams into the framework"
