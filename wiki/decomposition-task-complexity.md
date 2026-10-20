---
description: "Decomposition exercises get harder along three dimensions, repetition, code-pattern composition and data dependency, each graded 0 to 3; the grading is proposed, not yet tested on students."
aliases: ["code structuring complexity", "code structuring complexity framework", "decomposition task complexity", "bottom-up decomposition difficulty"]
sources: ["arxiv-2512-06178"]
---
# Decomposition task complexity

A code-structuring exercise gives a student unstructured code and asks them to pull out the meaningful functions hidden in it. Haldeman, Ohmann and Denny propose that how hard such an exercise is depends on three separable features of the code, not on its length alone. Their stated aim is "systematically assessing the complexity of code structuring tasks".[^c1] Each feature is graded on four levels, 0 to 3.

The first feature is repetition. At level 1 the snippets are identical copies of each other.[^c2] At level 2 they are near-identical, and the parts that differ can be passed as a parameter. At level 3 the tasks are similar in structure with a linear relation between them, so the student has to find the scaling and not only the shared shape.[^c3] The paper's level-3 example is a program that draws fish of different sizes, where the head, tail and body each scale with the size variable.

The second feature is code-pattern composition. Two patterns in one program can be concatenated (one after the other), included (one inside the other), or interleaved (pieces of the two mixed). The authors rank these in that order. Their ranking rests on the nesting that inclusion requires and on Ginat's finding that students struggle most with the interleaved case, which the paper cites rather than measures itself.[^c4] The authors are explicit that the link between relation type and difficulty is a theory: "We theorize that the complexity in separating the different tasks" of a program depends on how the tasks relate.[^c5] They also note that concatenation sits below inclusion: "We rank concatenation at a lower level of complexity than inclusion."[^c6]

The third feature is data dependency. The paper names two sources of complexity: "the order of the statements that form a dependency" path, and whether different dependency paths share a dependency.[^c7] A sequential task has its statements in dependency order. A shared-dependency task has one computed value, such as the inner area of a garden problem, that two goals both need, so the value has to be factored out once. A non-sequential task has its statements out of order with no shared dependency between them. This level sits between the other two because, as the authors say, the placement "may obfuscate the components of each task", so the student cannot rely on the layout and must comprehend the code to see the parts.[^c8]

Each exercise is tagged with one level per dimension. The authors built an online repository of labelled exercises on that basis, so an instructor can filter by complexity.[^c9] Their central claim is that "repetition, pattern composition and data dependency are the main drivers of code structuring complexity."[^c10]

My inference, not the paper's claim: the same three axes might describe a question that has to be split into sub-questions. Repeated sub-questions that differ only in one parameter would be the analogue of repetition, interleaved sub-questions the analogue of interleaved patterns, and sub-questions with a shared intermediate the analogue of shared dependency. The paper never tests this, and it is about code, so the transfer is a hypothesis.

## Limits

- The framework is a proposal. The authors say so: "we would like to explore empirical validation of the framework with students."[^c11] Nothing in the paper shows that the levels separate task difficulty for learners. The authors' own wording is that studies "would allow us to evaluate whether the categories do indeed differentiate task difficulty."[^c12]
- The levels are ordinal labels. The authors state that they make no claim about the size of the step from one level to the next, and that "one in one dimension is equivalent to the level one in the other" is not implied.[^c13]
- Only vertical complexity, measured by lines of code, is treated. The authors set horizontal complexity aside because they judge it rarer in refactoring patterns.[^c14] Cyclomatic complexity is not used.
- The exercise inventory "was curated by the authors", so the labels reflect their judgement, and no inter-rater check of the tagging is reported in the sections read.[^c15]
- The scope is procedural code at the introductory level. The paper does not claim the axes hold for object-oriented code, for expert programmers, or for natural-language questions.

## Related

- [[function-level-step-decomposition]] — there the boundary between reasoning steps is drawn by a prompt, not found in the code; this framework instead reads the boundary from repetition and dependency structure in the code itself (my reading).
- [[backward-chaining-subgoal-decomposition]] — top-down decomposition from a target. The paper works the other way: "we refer to bottom-up decomposition" as code structuring.[^c16]
- [[dependency-aware-subquestion-scheduling]] — ready-set scheduling of dependent sub-questions; the shared and non-sequential levels describe the same kind of ordering problem in code (my inference).
- [[output-structure-complexity-gradient]] — another graded complexity ladder, here for output format rather than code structure.

[^c1]: arxiv-2512-06178 — "systematically assessing the complexity of code structuring tasks"
[^c2]: arxiv-2512-06178 — "snippets of code are identical copies of each other"
[^c3]: arxiv-2512-06178 — "tasks that are similar in structure with a linear relation"
[^c4]: arxiv-2512-06178 — "has empirically shown that students have the most"
[^c5]: arxiv-2512-06178 — "We theorize that the complexity in separating the different tasks"
[^c6]: arxiv-2512-06178 — "We rank concatenation at a lower level of complexity than inclusion"
[^c7]: arxiv-2512-06178 — "the order of the statements that form a dependency"
[^c8]: arxiv-2512-06178 — "may obfuscate the components of each task"
[^c9]: arxiv-2512-06178 — "create an online interactive repository of code structuring exercises"
[^c10]: arxiv-2512-06178 — "repetition, pattern composition and data dependency are the"
[^c11]: arxiv-2512-06178 — "we would like to explore empirical validation of the framework with students"
[^c12]: arxiv-2512-06178 — "whether the categories do indeed differentiate"
[^c13]: arxiv-2512-06178 — "one in one dimension is equivalent to the level one in the other"
[^c14]: arxiv-2512-06178 — "focus on vertical complexity, which is reflected by LOC"
[^c15]: arxiv-2512-06178 — "was curated by the authors"
[^c16]: arxiv-2512-06178 — "we refer to bottom-up decomposition"
