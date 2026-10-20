---
description: "A foundation-model task's evaluator is picked from a profile of the task (io, constraints, likely failure modes, labels available) rather than a fixed metric; the profile is still partial."
aliases: ["synthesised evaluator", "eval synthesis", "task-specific evaluator synthesis", "meta-model-driven evaluation"]
sources: ["arxiv-2512-04442"]
---
# Task-profile evaluator synthesis

When a foundation-model output has no metric and no labelled dataset, the usual options are a person reading each output or a model judging it. TaskEval proposes a third: the evaluator is derived from a profile of the task. The paper opens on the gap: "The oracle problem in FM evaluation, deciding correctness without ground truth remains unresolved."[^c1]

The mechanism has three parts. The first is a profile. A task-agnostic meta-model is filled in from the task description and a sample input: "The meta-model captures essential elements of a task based on the task description".[^c4] The facets the paper plans to model include input and output specification, task type, evidence and grounding requirements, constraints such as schema, units and ranges, reasoning mode, evaluation objectives and reference sources.[^c3] The meta-model is borrowed from model-driven engineering: "Our approach combines meta-modelling [2] from model-driven" engineering with domain modelling.[^c22] What survives that transfer is the idea that one task is an instance of a shared schema; what the paper has not shown is that the schema fits tasks it was not built from.

The second part is the choice of eval. The profile selects failure modes and binds them to strategy templates.[^c23] The demonstrator's four families are "as a) summarize, b) visualize, c) Judge, and d) logic program".[^c5] Whether an eval is custom or existing "is based on the task and dimensions of evaluation that are expressed by the user".[^c6]

The third part is a labelling interface. The evaluator is built so that human correction becomes a label: "labelled data is collected as people interact with the system."[^c7]

An example shows the shape. For chart data extraction the selected eval is a visualisation. "Visualise strategy that redraws the chart from the" extracted points, shown beside the original image, and a correction is a numeric cell edit in the extracted table.[^c8] For document question answering the eval combines a visualisation with a judge, highlighting the source spans that support each answer claim.[^c24]

The measured part is two small checks. For charts the question was "whether the regenerated plot matched the extracted points", and the paper reports "28 were correct (93%)" on 30 charts.[^c9][^c10] For document QA the check was whether the answer was mainly sourced from the passage with the most highlighted words, and "27 met this criterion (90%)."[^c11] The abstract's figures are these two numbers: "A preliminary evaluation on the quality of our selected evals shows" 93% and 90%.[^c12]

What these numbers measure is my reading, not the paper's. They check the evaluator's own output for consistency: a regenerated plot against the extraction, an answer against one passage. They do not check the FM output against the chart or against a true answer. The shape is a reconstruction check, an output passed through a second transformation and compared with the original, which [[round-trip-invertibility-consistency]] tests in a different setting.

## Limits

- The meta-model is a plan. "We anticipate needing to come up with criteria" for the context of an FM task, and the paper says the meta-model will be refined later.[^c13][^c21]
- The profile has to be elicited. The paper expects that "It is unlikely that a user will include this" on first pass, so an interaction protocol fills it in. That protocol is described but not evaluated in this text.[^c14]
- Two tasks, both with a checkable structure. "Experimental evaluation of the generalisability of TaskEval." is listed as future work.[^c15] Objective tasks, where "evaluation can be confirmed as right/wrong", and subjective ones are named as untested extensions.[^c18]
- The evaluator is written by FMs, so it inherits their errors: "evaluator which means the evaluator also needs to be evaluated!"[^c16] The paper's answer to this is a planned workflow, not a result.
- The risk the paper names is a profile too thin to carry over: "context our approach will not generalise well to unseen FM tasks."[^c19]
- No baseline. Nothing here compares the synthesised evaluator with a hand-built one or with a human reviewer, so the 93% and 90% cannot be set against an alternative from this text.
- Judge-type evals inherit the weakness the paper attributes to LLM-as-a-judge methods, "that are inconsistent and themselves require evaluation."[^c17] The judge side is treated in [[llm-judge-score-instability]].

## Related

- [[program-computed-ground-truth]] — also avoids a human answer key, but builds the key by running a program; here the output is an evaluator with no key at all.
- [[llm-judge-score-instability]] — the known weakness of the judge strategy that this approach includes as one option.
- [[round-trip-invertibility-consistency]] — exact reconstruction as a test; the regenerated plot here is a similar reconstruction, applied to an output rather than to a model's inverse.

[^c1]: arxiv-2512-04442 — "The oracle problem in FM evaluation, deciding correctness without ground truth remains unresolved."
[^c2]: arxiv-2512-04442 — "The task-agnostic Meta-model represents the essential properties of an FM task and elements required for creating an eval."
[^c3]: arxiv-2512-04442 — "We plan to investigate multiple facets including"
[^c4]: arxiv-2512-04442 — "The meta-model captures essential elements of a task based on the task description"
[^c5]: arxiv-2512-04442 — "as a) summarize, b) visualize, c) Judge, and d) logic program"
[^c6]: arxiv-2512-04442 — "custom eval or use an existing eval is based on the task and dimensions of evaluation that are expressed by the user"
[^c7]: arxiv-2512-04442 — "labelled data is collected as people interact with the system."
[^c8]: arxiv-2512-04442 — "Visualise strategy that redraws the chart from the"
[^c9]: arxiv-2512-04442 — "whether the regenerated plot matched the extracted points"
[^c10]: arxiv-2512-04442 — "28 were correct (93%)"
[^c11]: arxiv-2512-04442 — "27 met this criterion (90%)"
[^c12]: arxiv-2512-04442 — "A preliminary evaluation on the quality of our selected evals shows"
[^c13]: arxiv-2512-04442 — "We anticipate needing to come up with criteria"
[^c14]: arxiv-2512-04442 — "It is unlikely that a user will include this"
[^c15]: arxiv-2512-04442 — "Experimental evaluation of the generalisability of TaskEval."
[^c16]: arxiv-2512-04442 — "evaluator which means the evaluator also needs to be evaluated!"
[^c17]: arxiv-2512-04442 — "that are inconsistent and themselves require evaluation"
[^c18]: arxiv-2512-04442 — "objective tasks (i.e. evaluation can be confirmed as right/wrong)"
[^c19]: arxiv-2512-04442 — "context our approach will not generalise well to unseen FM tasks."
[^c21]: arxiv-2512-04442 — "refine our hierarchical task-agnostic meta-model"
[^c22]: arxiv-2512-04442 — "Our approach combines meta-modelling [2] from model-driven"
[^c23]: arxiv-2512-04442
[^c24]: arxiv-2512-04442
