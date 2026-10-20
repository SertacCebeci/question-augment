---
description: "For LLM numeric interval prediction, compact decision-relevant context helps slightly, but adding rich narrative or lifecycle detail often lowers accuracy back toward the zero-context level."
aliases: ["context-as-noise effect", "more context is not always better", "medium-context sweet spot"]
sources: ["arxiv-2601-10132", "arxiv-2512-24289", "arxiv-2512-05576", "arxiv-2511-19730"]
---
# Medium-context sweet spot for numeric prediction

The study asks an LLM to predict the next gap, in days, between a user's repeated purchases. It uses three zero-shot prompt levels. Zero context gives historical intervals only. Medium adds product metadata and summary statistics. High adds recency features and user lifecycle information.[^c1] The models were GPT-4o, Gemini-2.5 Pro and Claude 3.5 Sonnet, on a proprietary grocery set and on Instacart.[^c2]

The reported pattern is non-monotonic. Medium context "consistently improves both model metrics and business-oriented accuracy", while high-level narrative context "often degrades performance, sometimes matching the zero-context baseline".[^c3] The authors call this a context-as-noise effect: focused, decision-relevant information helps, and semantically rich but temporally irrelevant details distract.[^c4] Their case study (Claude 3.5 outputs) reports that models overweight narrative details surfaced by high-context prompts, which diverts them from the underlying temporal structure.[^c5]

The table shows the size and the inconsistency of the effect. On proprietary data, GPT-4o MAPE goes 73.03 (zero), 66.78 (medium), 76.59 (high). Claude-3.5 goes 64.27, 57.45, 59.61. Gemini-2.5 goes 63.79, 67.79, 71.38, so medium did not help there, and its MAPE rose with each added level.[^c6] The gains are modest, and the ordering varies by model and metric.

A second paper, on EU Taxonomy activity identification (arxiv-2512-24289), shows a similar pattern in classification rather than regression. The average F1 across runs was 0.2264 with the full annual report and 0.2493 with concise company metadata, and the authors state that "providing more data is not always better."[^c9] They attribute the drop to "the extensive, noisy text of a full report impedes" zero-shot inference.[^c10] In the granular binary task, reported for Gemini Flash 2.0, metadata alone gave precision 67.86% and recall 10.80%; the full report doubled recall to 20.45% and cut precision to 48.65%.[^c11] The authors read this as a trade-off: concise context favors precision, while full-text context aids discovery.[^c12]

A tool-using clinical agent shows a threshold of the same kind, with reasoning context measured in tokens. On CURE-Bench the authors report a "sharp performance decline (from 94% to 87.93%) when reasoning contexts exceed" 12,000 tokens.[^c13] They read the decline as noise: the raw evidence "introduces noise that overwhelms the model" in its attention.[^c14] The figure's labelled groups hold between 15 and 127 cases each, one of them "(n=58)", so the decline compares small groups rather than a fitted curve.[^c15]

The sign of the effect can also flip with the kind of data. In a materials-science study of LLM-guided experiment selection, the narrative report format hurt on a dataset with many compositional inputs: on matbench_steels the report prompts needed 55% of the data, against 18% for the compact parameter format, and the authors attribute this to descriptive text adding "unnecessary complexity".[^c17] On the procedural Membrane dataset the narrative format was the stronger one.[^c18] The paper states the same split in its own words: datasets with many independent variables "favor parameter-format" prompts.[^c19] Read together, these suggest the sign follows whether the added text bears on the target rather than how much text there is. My inference: the paper compares two formats on four datasets and runs no ablation that separates the two causes.

For asking, the implication is that the question is the quantity of context only up to a point. What matters is whether the added information bears on the quantity being asked about. This is my reading of the authors' account, not a tested mechanism.

## Limits

- The "noise" and "overweighting" mechanism is the authors' interpretation from a small set of qualitative examples. No ablation separates which high-context fields (recency, lifecycle) cause the drop.
- Medium and high differ in content type as well as in amount, so length and relevance are confounded.
- Only zero-shot prompting, three models, and one task (discrete repurchase intervals, gaps over 20 days removed) were tested. Few-shot prompting and prompt tuning were left to future work.[^c7]
- The paper is a 4-page short paper. No significance tests are reported in the text I read, and Gemini-2.5 does not follow the medium-best pattern on proprietary MAPE.
- The same paper finds LLMs beat statistical baselines but trail an ML model such as XGBoost on error metrics. That is a separate finding about the model class, not about context.[^c8]
- The classification result is one paper on one dataset, and the text read reports no significance test. Its noise explanation is the authors' reading, and its task (multi-label activity identification) differs from the interval task here, so the two are not shown to share one mechanism.[^c9]

- The 12,000-token result comes from one backbone (TxAgent, an 8B model) on one benchmark. Context length is confounded with difficulty: the authors describe harder test cases as "a distribution shift toward more complex cases requiring a higher average number of tool calls and longer context".[^c16] The text read contains no ablation that removes the raw evidence while holding the question fixed, so the noise reading is the authors' interpretation.

## Related

- [[context-pollution-naive-tool-addition]] — a similar finding in agents: added material lowers performance below baseline.
- [[parametric-knowledge-gates-retrieval-noise-damage]] — retrieved noise hurting answers, with a gate on when it does.
- [[post-cutoff-corpus-benchmark-isolation]] — naive injection can fall below no-context prompting.
- [[rag-bias-reduction-versus-cot-bias-increase]] — context and deliberation as separate levers.
- [[generate-then-verify-candidate-pipeline]] — the same paper's pipeline gives full text to a recall-heavy generator and a summary to a precision-heavy verifier.

[^c1]: arxiv-2601-10132 — "Zero-context isolates pure numeric reasoning from"
[^c2]: arxiv-2601-10132 — "we consider GPT-4o, Gemini-2.5"
[^c3]: arxiv-2601-10132 — "often degrades performance, sometimes matching the zero-context"
[^c4]: arxiv-2601-10132 — "This suggests a context-as-noise effect: focused, decisionrelevant information aids temporal reasoning"
[^c5]: arxiv-2601-10132 — "show that high-context prompts surface narrative details that models overweight"
[^c6]: arxiv-2601-10132 — "GPT-4o-Z"
[^c7]: arxiv-2601-10132 — "advanced prompt tuning strategies to future work."
[^c8]: arxiv-2601-10132 — "they consistently underperform dedicated machine-learning models"
[^c9]: arxiv-2512-24289 — "providing more data is not always better."
[^c10]: arxiv-2512-24289 — "the extensive, noisy text of a full report impedes"
[^c11]: arxiv-2512-24289 — "highly precise (67.86%) but had very low recall"
[^c12]: arxiv-2512-24289 — "concise context favors precision, while full-text context aids discovery"
[^c13]: arxiv-2512-05576 — "sharp performance decline (from 94% to 87.93%) when reasoning contexts exceed"
[^c14]: arxiv-2512-05576 — "introduces noise that overwhelms the model"
[^c15]: arxiv-2512-05576 — "(n=58)"
[^c16]: arxiv-2512-05576 — "a distribution shift toward more complex cases requiring a higher average number of tool calls and longer context"
[^c17]: arxiv-2511-19730 — "data (55%) and underperformed some traditional"
[^c18]: arxiv-2511-19730 — "report-format prompt is particularly effective"
[^c19]: arxiv-2511-19730 — "datasets containing many independent variables (e.g., compositions) favor parameter-format"
