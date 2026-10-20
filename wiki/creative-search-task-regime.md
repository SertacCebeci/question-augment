---
description: "Which creative search mode pays off depends on the task: low constraint with specific goals favors transformation, high constraint favors local exploration, loose goals favor analogy."
aliases: ["task regime for creative search", "constraint and objective specificity", "creative search regime"]
sources: ["arxiv-2511-20471"]
---
# Task regime for creative search

The work does not rank its three creative modes in general. It compares them across task regimes defined by two properties of the problem: degree of constraint and objective specificity.[^d1] Constraint is how strongly the problem's requirements restrict the feasible space; specificity is how precisely the desired outcome is defined. The two properties are the ones the authors say shape the creative search problem itself, since they set the size of the admissible space and the criterion by which candidates are judged.[^d2]

The mechanism given for each pattern is the one the authors attach to the search operators. Low constraint leaves room to change the rules: "A lower degree of constraint leaves greater flexibility in the rule-generation" stage, so transformation has more admissible rule sets to choose from.[^d3] Low specificity widens the analogue search: "a less specific objective permits broader notions of relevance and similarity", so more distant domains count as relevant.[^d4] High constraint narrows the space for the other way round: "A higher degree of constraint narrows the admissible solution space", which leaves local exploration around a candidate as the better-guided move.[^d5]

The measured pattern follows that reasoning. On Bridge and Electricity, which are low-constraint with high specificity, "Among matched GPT-4o reasoning methods, T-UoT performs strongest on Bridge and Electricity".[^d6] On Society, low-constraint with low specificity, "C-UoT shows the complementary pattern on Society".[^d7] On HypoArena, which is high-constraint, "E-UoT achieves the strongest overall performance, ranking first in both" biomedical and machine-learning tasks.[^d8] Averages are not the whole picture: the paper reports that "C-UoT is top-ranked on 15/100 HypoArena tasks" under its primary judge, so the mode that loses on average can still win particular tasks.[^d9]

A practical reading, which is mine and not the paper's: before choosing how to search for an answer, locate the task on the two axes. Where constraint is high and the goal is precise, the search should stay near a known candidate; where constraint is low and the goal is precise, the rules themselves are worth varying; where the goal is loose, looking for a distant analogue is the cheaper bet.

## Limits

The regime labels are the authors' own characterisation of each task: "We therefore characterize tasks by degree of constraint and objective specificity".[^d10] Constraint is not measured on a scale, and the low-constraint regime rests on three novel tasks the authors built, plus HypoArena for the high-constraint side. A pattern across three tasks is a narrow base.

The explanation is attached after the fact. The paper says "The observed performance patterns are consistent with the search mechanisms of T-UoT, C-UoT, and" E-UoT; consistency is not a test that varying constraint or specificity moves the ranking.[^d11]

The ranking also depends on the backbone. With GLM-4-9B, "OnePrompt ranks first while E-UoT remains the strongest structured method, indicating backbone dependence".[^d12] A regime that favours a mode on one model may not favour it on another.

The HypoArena ranking is judged by one model, Gemma-3-12B, as the primary judge, and the human panel exists only for the novel tasks: "Ten PhD students provide human judgments" on those.[^d13] The within-task reversals are small in count but real: "combinational and transformational search can still uncover stronger hypothesis directions on" particular problems, which the regime averages do not show.[^d14]

## Related

- [[boden-creativity-modes]] — the three modes whose relative standing this note tracks; that note defines what each one changes.
- [[solution-space-pinning]] — fixing a deterministic success criterion narrows the solution space; a constraint on the evaluation side of the same narrowing that the regimes here describe on the problem side.
- [[two-axis-cognitive-demand]] — another two-axis classification of tasks, from education; its axes are operation and depth, not constraint and specificity, so the two cannot be merged without a new argument.

[^d1]: arxiv-2511-20471 — "task regimes characterized by two properties that directly shape the creative"
[^d2]: arxiv-2511-20471 — "Objective specificity captures how precisely the desired outcome is defined"
[^d3]: arxiv-2511-20471 — "A lower degree of constraint leaves greater flexibility in the rule-generation"
[^d4]: arxiv-2511-20471 — "a less specific objective permits broader notions of relevance and similarity"
[^d5]: arxiv-2511-20471 — "A higher degree of constraint narrows the admissible solution space"
[^d6]: arxiv-2511-20471 — "Among matched GPT-4o reasoning methods, T-UoT performs strongest on Bridge and Electricity"
[^d7]: arxiv-2511-20471 — "C-UoT shows the complementary pattern on Society"
[^d8]: arxiv-2511-20471 — "E-UoT achieves the strongest overall performance, ranking first in both"
[^d9]: arxiv-2511-20471 — "C-UoT is top-ranked on 15/100 HypoArena tasks"
[^d10]: arxiv-2511-20471 — "We therefore characterize tasks by degree of constraint and objective specificity"
[^d11]: arxiv-2511-20471 — "The observed performance patterns are consistent with the search mechanisms of T-UoT, C-UoT, and"
[^d12]: arxiv-2511-20471 — "indicating backbone dependence"
[^d13]: arxiv-2511-20471 — "Ten PhD students provide human judgments"
[^d14]: arxiv-2511-20471 — "combinational and transformational search can still uncover stronger hypothesis directions on"
