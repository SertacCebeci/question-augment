---
description: "Having an agent write task rubrics while planning, then carry them through research, review and synthesis, makes the rubric the structure of the run rather than only a grading sheet read at the end."
aliases: ["rubric-guided scaffold", "rubric-conditioned stage scaffold", "self-generated rubric scaffold", "rubric as shared interface", "stage-structured reasoning scaffold"]
sources: ["doi-10-48550-arxiv-2605-10899"]
---
# Rubric-first planning scaffold

In most deep-research agents a rubric shows up at the end, as the judge's checklist for a finished report. The proposal studied here moves it to the front. The agent writes "task-specific rubrics" during planning, and then "carries them through four stages: planning, research, review, and answer synthesis."[^a1] The argument is that rubrics should serve "as the shared interface that structures" the run, its judging and its memory, not "merely as final-answer evaluators."[^a2]

Each stage is a separate decision mode with a light internal schema.[^a3] During research the agent alternates between tool calls and a state evaluation, and once the evidence is judged sufficient it moves to review and then to the answer.[^a9] The rubrics guide the search, serve as on-policy references for the judge, and leave traces that can be distilled into reusable reflections.[^a10] Splitting the run this way is argued formally. Theorem 1 says that a stage label can raise the value of a policy when the same local context calls for different actions at different stages. The statement requires two task-relevant stages whose optimal action sets are disjoint on a set of contexts with positive probability; under that condition, "explicit stage information is beneficial."[^a4] The motivation in prose is that "the same local context may call for different actions across planning, searching, reviewing" in a long research trajectory.[^a5] A flat policy has to infer its decision mode from local context alone, and the stage label removes that inference.

The measured effects are these. The structured scaffold improves the quality of supervised distillation, and it also makes later RL more effective. Without the scaffold, the paper reports that RL gains are "small and unstable for 600 steps, suggesting that rubric-conditioned stages provide useful structure" for exploration and credit assignment.[^a6] In a prompt-level test with Gemini-3.1-Pro on the same search backend, "our scaffold outperforms a standard ReAct prompt on DRB."[^a7]

The rubrics used here are prospective: written before the run, from the question. The memory that later runs draw on is built the other way, from outcomes after the run, and the paper keeps the two apart. Bank items are retrospective, because "the prospective rubrics generated during planning, bank items encode outcome-aware lessons."[^a8] See [[judge-scored-reflection-memory]] for that side. The stage judge that scores the run against stage rubrics is in [[stagewise-judged-credit]].

## Limits

- The scaffold bundles two things: stage structure and rubric conditioning. The comparisons I read set the scaffold against a flat ReAct prompt and against structured versus unstructured SFT checkpoints. None of them separates stage-only from rubric-only. My inference is that the paper's gain cannot be credited to rubrics specifically.
- The rubrics are self-generated, and the judge that scores them is Gemini Flash. [[rubric-formation-gap]] reports that self-generated rubrics help over no rubric but miss whole categories, such as refusal logic in safety items, that human-written rubrics supply. That gap is not measured in this paper, and the planning rubric is never checked against an outside reference in the parts I read.
- Theorem 1 is an abstract statement under an assumption block (Assumption 1), and its proof is deferred to an appendix I did not read. It says stage information cannot hurt the value under the stated conditions. It does not give the size of the gain, and it does not say that a language model can recover the stage from its own text.
- The backbone is an 8B model distilled from Qwen3-8B on structured traces. Transfer to other models is not shown in the reading.
- The work is about writing long research answers. Whether a question-asker gains from the same rubric-first structure, or only an answerer, is not tested here. This is my inference from the scope of the paper.

## Related

- [[rubric-formation-gap]] — self-generated rubrics help but leave out items that human rubrics supply; this scaffold depends on self-generated ones
- [[expert-report-derived-atomic-rubrics]] — criteria taken from expert text, the alternative source of rubric items
- [[stagewise-judged-credit]] — the per-stage judge that scores each stage against the rubrics written at planning
- [[judge-scored-reflection-memory]] — retrospective rubrics written after a run, which the prospective planning rubrics are kept apart from
- [[rubric-aware-on-policy-self-distillation]] — a rubric used as a teacher's steering signal rather than as the structure of a run

[^a1]: doi-10-48550-arxiv-2605-10899 — "the agent generates task-specific rubrics and carries them through four stages"
[^a2]: doi-10-48550-arxiv-2605-10899 — "rubrics should serve not merely as final-answer evaluators, but as the shared interface that structures"
[^a3]: doi-10-48550-arxiv-2605-10899 — "each with a lightweight internal schema"
[^a4]: doi-10-48550-arxiv-2605-10899 — "explicit stage information is beneficial"
[^a5]: doi-10-48550-arxiv-2605-10899 — "the same local context may call for different actions across planning, searching, reviewing"
[^a6]: doi-10-48550-arxiv-2605-10899 — "small and unstable for 600 steps, suggesting that rubric-conditioned stages provide useful structure"
[^a7]: doi-10-48550-arxiv-2605-10899 — "our scaffold outperforms a standard ReAct prompt on DRB"
[^a8]: doi-10-48550-arxiv-2605-10899 — "the prospective rubrics generated during planning, bank items encode outcome-aware lessons"
[^a9]: doi-10-48550-arxiv-2605-10899 — "the agent iterates between tool use and state evaluation"
[^a10]: doi-10-48550-arxiv-2605-10899 — "serve as on-policy references for the judge"
