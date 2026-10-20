---
description: "A closed Plan–Do–Study–Act loop answers, checks its own confidence, diagnoses a failed attempt and replans it, stopping at a confidence threshold or a cycle cap."
aliases: ["PDSA cycle", "Deming cycle", "plan-do-study-act", "PDSA controller", "closed-loop replanning"]
sources: ["arxiv-2511-17943"]
---
# Plan-do-study-act loop

A plan–do–study–act loop is a closed controller wrapped around an answer. The SciEducator system is described as "Rooted in the classical Deming Cycle from management science"[^p0], and it runs four stages per cycle. Plan builds "a diverse pool of candidate plans"[^p1] and retrieves domain knowledge into it: "retrieves domain knowledge K from an internal corpus".[^p2] Do has an evaluator "scores each plan with a composite of objective"[^p3] scores, then executes the chosen plan. The planner then estimates a confidence in the result: "the planner estimates a confidence score using the query Q".[^p4]

If confidence is low, Study diagnoses the failure. The planner looks for causes such as "tool failures, overly broad and irrelevant retrieval, or insufficient detail in video captions"[^p5] and gathers "new information" and knowledge.[^p6] Act then rebuilds the next pool, "adjusting structure, granularity,"[^p7] or query specificity, where "refine queries with more specific entities" is one of the examples.[^p8] The loop repeats until "Ci ≥ τ or a maximum number of cycles we choose."[^p9]

The distinctive part is the channel from diagnosis to the next plan. A bare retry would resample the same plan; here the stated cause decides what changes. In the paper's notation the next pool is a function of the failure analysis, the updated knowledge and the previous pool (my reading of its Eq. 8, not a quoted claim). The ablation names the two study-stage pieces separately, and in its table caption "F denotes failure analysis" beside the new knowledge, so the diagnosis and the acquired knowledge are two things it varies.[^p10]

On the cycle count, the paper caps cycles from 1 to 5 and reports that "performance improves significantly with" more of them.[^p11] The cap has a consequence: when it is reached, "the system was compelled to generate the most likely" answer from what has been accumulated.[^p12]

Transfer to asking (my inference, not the paper's claim). The study stage lists causes that sit in the shape of the question itself; "excessively broad search keywords" is among them.[^p13] If that holds, a loop like this treats a weak question as something to respecify against a named cause, not to re-ask unchanged. The paper does not test question-asking; this is a transfer.

## Limits

- The loop is tested on one benchmark the authors built, SciVBench: 500 QA pairs over physics, chemistry and everyday phenomena, with answers scored by an LLM judge, "using qwen3-max as the unified evaluator for".[^p14] No independent grader is reported in the text I read.
- The stop signal is the planner's own confidence estimate. The text gives no check of that estimate against correctness, so a confident wrong answer ends the loop early.
- The cycle cap can end a run below threshold, and then the output is forced rather than converged. Results at the highest cycle count therefore mix converged and forced answers.
- The ablations vary the number of cycles and remove study-stage pieces. They do not compare the loop against a single pass with the same number of tool calls, so the gain from iteration is confounded with extra retrieval and computation (my inference).
- "The first iterative self-evolving multi-agent system" is the authors' own priority claim.[^p15] The loop is shown to work inside this one system, not shown to beat other ways of iterating.

## Related

- [[plan-level-retrospection]] — a search agent that also discards a faulty plan and rebuilds it, but without a confidence gate or a cycle cap
- [[confidence-triggered-reflection]] — low confidence triggers a self-review inside one generation, not a replan across cycles
- [[stop-continue-criteria-in-retrieval-loops]] — the stop rule here is a confidence threshold with a cap, the adaptive kind that note finds rare in its corpus
- [[intrinsic-self-correction-convergence]] — repeated self-correction with no external feedback converges; the study stage here adds retrieval before each new round

[^p0]: arxiv-2511-17943 — "Rooted in the classical Deming Cycle from management science"
[^p1]: arxiv-2511-17943 — "a diverse pool of candidate plans"
[^p2]: arxiv-2511-17943 — "retrieves domain knowledge K from an internal corpus"
[^p3]: arxiv-2511-17943 — "scores each plan with a composite of objective"
[^p4]: arxiv-2511-17943 — "the planner estimates a confidence score using the query Q"
[^p5]: arxiv-2511-17943 — "tool failures, overly broad and irrelevant retrieval, or insufficient detail in video captions"
[^p6]: arxiv-2511-17943 — "seeks useful new information"
[^p7]: arxiv-2511-17943 — "adjusting structure, granularity,"
[^p8]: arxiv-2511-17943 — "refine queries with more specific entities"
[^p9]: arxiv-2511-17943 — "until Ci ≥ τ or a maximum number of cycles we choose."
[^p10]: arxiv-2511-17943 — "F denotes failure analysis"
[^p11]: arxiv-2511-17943 — "performance improves significantly with"
[^p12]: arxiv-2511-17943 — "the system was compelled to generate the most likely"
[^p13]: arxiv-2511-17943 — "excessively broad search keywords"
[^p14]: arxiv-2511-17943 — "using qwen3-max as the unified evaluator for"
[^p15]: arxiv-2511-17943 — "the first iterative self-evolving multi-agent system"
