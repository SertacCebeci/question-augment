---
description: "Atomic, content-bearing rubrics extracted from expert-written reports and expert-reviewed let a judge grade research reports without its own knowledge; the best agents pass under half."
aliases: ["content-bearing rubrics", "expert-article rubric extraction", "DeepResearch Bench II rubrics", "deterministic checklist-based evaluation (DCE)", "atomic Y/N checklist"]
sources: ["arxiv-2601-08536", "arxiv-2601-00561"]
---
# Expert-report-derived atomic rubrics

A way to grade long open-ended answers (research reports) without letting the judge or an LLM invent the criteria. Take an expert-written article, derive a task from it, and derive the rubric from the article's own content. The rubric then carries the answer, so the judge compares a report against stated facts and inferences, not against its own internal knowledge.

## Mechanism

The authors criticise two prior designs: criteria defined by an LLM (possible misalignment and anchoring bias with human experts) and human-written but coarse rubrics, which need judge knowledge and let seemingly correct hallucinations pass.[^c1] Their rubrics are binary and must satisfy four constraints: essential to answering the task; atomic and indivisible; directly encoding target content rather than a topic ("stated that labor loss in small cities is due to job-structure mismatch" rather than "gave reasons for labor loss"); and every numeric value explicitly verified.[^c2] Each rubric falls in one of three dimensions: information recall, analysis, presentation. The task score is the proportion of rubrics passed.[^c3]

Construction runs four stages: LLM extraction, self-evaluation iteration, manual revision, expert review. In the self-evaluation stage each rubric set is applied to its own source article; if recall or analysis accuracy is below 90%, the generation is treated as hallucinated and regenerated.[^c4] Domain experts then spent over 400 human-hours checking that recall rubrics are essential and consistent with the source, and that analysis rubrics encode reasoning rather than lookup.[^c5] The result is 132 tasks, 22 domains, 9,430 rubrics.

## What it measured

With Gemini-2.5-Pro as judge, scoring 50 rubrics per pass, the best agent (OpenAI o3 Deep Research) scored 45.40 total; the lowest, Tongyi, 29.89. Recall and analysis were low (about 23-50) while presentation was high (about 75-92), so the shortfall is in content, not form.[^c6] Against human labels on ten reports, judge agreement was 91.75% accuracy and 89.57 F1 at batch 50; GPT-5 gave 78.28 F1 and Gemini-2.5-Flash 79.79.[^c7] Very small batches (5 rubrics per pass) were worse and far more costly than 50.[^c8]

Scores did not vary significantly with research topic, and only Grok varied marginally with language.[^c9]

The same binary, atomic form appears where no expert article exists. In AEGIS, a benchmark for unified multimodal models, a multimodal LLM is asked to process a reference response and its keywords, then to produce atomic yes/no questions, each tied to one key part of the reference. A judge answers each item for a model's response, and the score is the share answered yes.[^c12] On a 10% sample checked by experts, the overall agreement of the judge's decisions with human verification was 90.7%.[^c13][^c14] Agreement was lower for interleaved generation, which the authors trace to its image-text consistency items.[^c15][^c16] The choice of judge also mattered: Gemini-2.5-Pro tracked humans better than GPT-5 on editing and interleaved tasks, which the authors put down to better reasoning.[^c17]

## Limits

- The judge agreement check used only ten reports; it is a small sample.
- Source leakage cannot be fully excluded: the agents were only told via a prompt blocklist not to read the source articles, and the authors admit this is a suboptimal workaround.[^c10]
- Rubrics encode what one expert article said; a correct report that reaches the same conclusion differently, or adds valid points, may fail items. This is my inference, not tested.
- The user-background aspect of presentation was acknowledged as not fully realized.[^c11]
- The benchmark grades reports, not question asking; any bearing on how questions are posed or clarified is my inference. No ablation compared this rubric style against coarse human rubrics at fixed judge.
- The 90.7% agreement comes from a 10% sample, and the checklist is only as sound as its reference answer, which an LLM drafted before a human revised it.[^c18] Whether checklist scores track answer quality beyond that reference is not tested in the AEGIS paper. (my inference)

## Related

- [[rubric-formation-gap]] — shows human rubrics beat model-written ones in pairwise judging; this is a construction recipe for human-grounded rubrics
- [[llm-judge-biases]] — judge failure modes the content-bearing rubric tries to avoid
- [[judge-coverage-overestimation]] — a different worry about what judges credit
- [[breadth-oriented-information-seeking]] — the information-seeking side of research agents
- [[recursive-rubric-decomposition]] — another route to atomic criteria
- [[dependency-aware-checklist-scoring]] — credits a checklist item only when its prerequisites also hold, a stricter use of atomic items than the flat share here
- [[weight-stratified-criterion-pass-rate]] — atomic criteria with clinician weights, where the same kind of rubric is read by weight class rather than as one share passed

[^c1]: arxiv-2601-08536 — "allow seemingly correct hallucinations from the DRA to pass"
[^c2]: arxiv-2601-08536 — "each rubric must be atomic and indivisible"
[^c3]: arxiv-2601-08536 — "the final task score is computed as the proportion of passed rubrics"
[^c4]: arxiv-2601-08536 — "the generation is considered unreliable due to potential hallucination"
[^c5]: arxiv-2601-08536 — "Over the course of more than 400 human-hours"
[^c6]: arxiv-2601-08536 — "even the best-performing agent still fails to satisfy more than half of the rubrics"
[^c7]: arxiv-2601-08536 — "Gemini-2.5-Pro demonstrates the highest alignment with human annotations across both metrics"
[^c8]: arxiv-2601-08536 — "a batch size of 50 offers the best balance"
[^c9]: arxiv-2601-08536 — "showing no significant topic-based variation"
[^c10]: arxiv-2601-08536 — "this approach cannot guarantee 100% prevention of model"
[^c11]: arxiv-2601-08536 — "this aspect"
[^c12]: arxiv-2601-00561 — "to process a reference response and its corresponding keywords"
[^c13]: arxiv-2601-00561 — "we sample 10% questions in AEGIS"
[^c14]: arxiv-2601-00561 — "the overall consistency achieves 90.7%"
[^c15]: arxiv-2601-00561 — "the interleaved generation task is relatively lower"
[^c16]: arxiv-2601-00561 — "By manually analyzing these questions, we find that the complex"
[^c17]: arxiv-2601-00561 — "A feasible explanation is that Gemini-2.5Pro has better reasoning capabilities"
[^c18]: arxiv-2601-00561 — "an LLM generated a draft response, which was"
