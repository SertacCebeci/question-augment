---
description: "Agents that retrieve discrete facts well can still collapse on predictive questions; across ten LLMs on expert crypto tasks, retrieval scores ran far above prediction scores."
aliases: ["retrieval-prediction imbalance", "retrieval-prediction split", "retrieval versus prediction task gap"]
sources: ["arxiv-2512-00417"]
---
# Retrieval-prediction asymmetry

A task put to an agent can be placed on two axes: how far it asks for finding one discrete fact (retrieval) against turning evidence into an inference or forecast (prediction), and whether it is simple (one data point) or complex (several points from several sources). The CryptoBench work uses this grid as a diagnostic. Simple retrieval is defined by the act of "and extract a single, discrete piece of information from a" source.[^r1] Simple prediction asks the agent to "perform a basic inference, calculation, or predictive judgment" from a few data points.[^r2] Complex prediction asks for "multi-step inference, the synthesis of information from multiple, potentially conflicting sources, and the formulation" of a forecast or recommendation.[^r2b]

The measured result is that the two axes do not move together. "Across nearly all models, retrieval tasks are handled substantially better than prediction tasks, revealing a systematic retrieval-prediction imbalance."[^r3] The imbalance is sharpest in individual models: "models that perform strongly on retrieval exhibit near-random performance on predictive tasks."[^r4] The authors put the top of the field in the same terms: "this proficiency vanishes when tasks require even simple predictive reasoning."[^r5]

The failures the authors saw in prediction answers were of a different kind from retrieval errors. Agents "fail to correctly integrate multiple retrieved data points, or hallucinate unsupported predictions," and the authors add that these "are especially prevalent in predictive tasks."[^r6] They read the gap as structural: "failures are not merely due to task difficulty but reflect deeper architectural limitations."[^r7] That reading is theirs, and the text does not separate it from the scoring effect described below.

For asking, the mechanism that matters is the split itself. A question that an agent can answer by locating a value says little about whether the same agent can answer a question that asks what the value implies. A question can be typed by its cognitive demand before any answer is judged, so that a high score on one kind is not read as a high score on the other. This is my inference from the diagnostic use the authors make, not a claim they test: they show the asymmetry across models, not that typing questions improves anyone's answers.

## Limits

- One benchmark, one month. The work reports 50 questions drawn for a single window, and its prediction quadrants are a minority of them: the figure gives "Simple Prediction (12%)" and "Complex Prediction (20%)".[^r8] By those shares that is roughly 16 prediction items, so per-quadrant figures rest on few questions (my arithmetic).
- The score on prediction items comes from an LLM judge. "The LLM-judge is provided with the original question" together with the response trace, the gold answer and a rubric.[^r9] The sections read do not report a check of the judge's agreement with human graders on forecasts. Judges can be wrong in ways the authors do not measure (see [[llm-judge-biases]]).
- Cognitive demand is confounded with how fixed the answer is. Retrieval items have a value to find; prediction items have a gold answer only because experts agreed on it. The text says a question entered the set "if it achieved unanimous consensus across all" stages.[^r10] Some of the gap may come from how verifiable each kind of answer is, and the grid does not separate the two.
- The quadrant assignments are the authors' judgment. The text read reports no inter-rater figure for them.
- The setting is one agent framework, a single web-browsing tool, live crypto platforms. The text does not test whether the imbalance survives other tools, other domains, or a non-agentic setting in the same way.

## Related

- [[analytical-information-need]] — analytical needs ask for a conclusion from several pieces of evidence, the same line between fact and inference, but framed as a search problem rather than an agent benchmark.
- [[analytical-search]] — the search paradigm for needs of the predictive kind; the asymmetry above is a measured case of why such needs are harder to serve.
- [[llm-judge-biases]] — how judge scoring can distort results; a limit on any prediction score graded this way.

[^r1]: arxiv-2512-00417 — "and extract a single, discrete piece of information from a"
[^r2]: arxiv-2512-00417 — "Tasks here require the agent to perform a basic inference, calculation, or predictive judgment"
[^r2b]: arxiv-2512-00417 — "multi-step inference, the synthesis of information from multiple, potentially conflicting sources, and the formulation"
[^r3]: arxiv-2512-00417 — "Across nearly all models, retrieval tasks are handled substantially better than prediction tasks"
[^r4]: arxiv-2512-00417 — "models that perform strongly on retrieval exhibit near-random performance on predictive tasks"
[^r5]: arxiv-2512-00417 — "this proficiency vanishes when tasks require even simple predictive reasoning"
[^r6]: arxiv-2512-00417 — "integrate multiple retrieved data points, or hallucinate unsupported predictions"
[^r7]: arxiv-2512-00417 — "indicating that failures are not merely due to task difficulty but"
[^r8]: arxiv-2512-00417 — "Complex Prediction (20%)"
[^r9]: arxiv-2512-00417 — "The LLM-judge is provided with the original question"
[^r10]: arxiv-2512-00417 — "final dataset if it achieved unanimous consensus across all"
