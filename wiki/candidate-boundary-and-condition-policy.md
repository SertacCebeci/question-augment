---
description: "An agent score supports a claim only relative to a declared candidate boundary and condition policy; model, system and robustness comparisons answer different questions and must not share one ranking."
aliases: ["evaluation target", "LLM agent performance is not a single target", "target-first evaluation"]
sources: ["arxiv-2602-03238"]
---
# Candidate boundary and condition policy

A benchmark score does not say which question it answers. Two numbers, 62 and 58, can compare two LLMs under a shared execution setup, two separately optimized complete agents, or one candidate across changed conditions.[^c1] The position paper argues that "LLM agent performance" is an umbrella term, and that what a score licenses depends on two design decisions made before any score is aggregated.

## The two decisions

The **candidate boundary** names the compared entity and which components it owns (model, inference configuration, prompts, planning, memory, tool routing). The **condition policy** says whether everything outside that boundary is held at reference values, semantically matched across candidates, or systematically varied over a predeclared set.[^c2] A material difference that is neither candidate-owned nor in the declared sweep is an uncontrolled confound (the paper's wording; my paraphrase).

## Three claim types

- Model comparison under a reference stack: the model is the intended source of variation, and prompting, planning, memory, tools, environment, evaluator and budget are fixed. The claim stays conditional: one model beats another under the declared reference configuration.[^c3] It does not characterize separately optimized agent systems.[^c4]
- Complete-system comparison: the candidate includes backbone, prompts, planning and memory. The claim is that one declared system beats another under common external rules, and it does not isolate the LLM's contribution.[^c5]
- Robustness: a fixed candidate is tested across predeclared conditions outside its boundary. It qualifies either of the other claims; it does not yield a context-free score.[^c6]

The same component changes role with the target: a prompt is setup to be fixed when the LLM is the candidate, but part of the candidate when the system is. Varying the prompt therefore tests robustness of a fixed LLM, not of a fixed agent system whose prompt is internal.[^c7]

## Consequences for reporting

Scores are directly comparable only with the same target, the same boundary rule and compatible condition policies. The paper recommends separate leaderboard tracks for model capability and system performance, robustness as a layer inside each, and bridge evaluations of anchor candidates when a benchmark is revised, valid only within one target.[^c8] Before reporting, four questions are posed: what is the candidate, what is fixed, owned or varied, is it a reference or robustness claim, and which other results are compatible.[^c9]

## Limits

- It is a position paper; the framework is argued from cited prior work and examples, not tested with a new measurement here, as far as the slices I read show (I read roughly lines 1-540 plus greps).
- The boundary and policy constrain attribution but do not fix validity; task-construct validity, evaluator validity, contamination and statistics remain separate requirements.[^c10]
- Transfer to question asking and answering is my inference: an answer's quality may likewise depend on an undeclared stack (prompt, retrieval, judge). That is a conjecture, not shown here.

## Related

- [[llm-judge-score-instability]] — evaluator behaviour is one of the non-candidate factors that must be fixed or varied.
- [[answer-format-dependent-bias-measurement]] — a measured score that shifts with an undeclared measurement setup.
- [[multi-seed-bias-score-averaging]] — repeated runs for uncertainty, which the paper asks stochastic evaluations to report.
- [[post-cutoff-corpus-benchmark-isolation]] — a fixed reference environment versus changing conditions.

[^c1]: arxiv-2602-03238 — "Thus, the same benchmark and metric"
[^c2]: arxiv-2602-03238 — "The candidate boundary"
[^c3]: arxiv-2602-03238 — "The resulting claim is conditional: model m1 outperforms model m2 under the declared reference"
[^c4]: arxiv-2602-03238 — "it does not characterize separately optimized agent systems."
[^c5]: arxiv-2602-03238 — "The resulting claim is conditional: one declared agent system outperforms another under those external rules."
[^c6]: arxiv-2602-03238 — "does not produce a context-free performance score."
[^c7]: arxiv-2602-03238 — "but it does not test the robustness of a fixed agent"
[^c8]: arxiv-2602-03238 — "Leaderboards should maintain separate tracks for model capability and agent-system"
[^c9]: arxiv-2602-03238 — "The evaluation question must therefore be specified before the controls are chosen."
[^c10]: arxiv-2602-03238 — "do not determine evaluation validity; task-construct"
