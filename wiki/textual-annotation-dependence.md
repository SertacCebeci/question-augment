---
description: "Removing a chart's printed numerals cuts multimodal models' numerical QA accuracy by 17.56 to 53.73 points, so answers rest on printed labels more than on the plotted marks."
aliases: ["annotation dependence", "label reliance in chart QA", "annotated versus unannotated gap", "numeral-removal drop"]
sources: ["arxiv-2512-14040"]
---
# Textual annotation dependence

A chart carries two sources of value: the marks it draws (bar heights, line inflections, sector angles) and the text printed on it (numerals at key points, legend words, axis labels). A question about a value can be answered from either. The measurement in ChartAgent is that general multimodal models lean heavily on the printed text. The authors state the finding as a limitation of current models: they are "heavily dependent on explicit textual annotations and the performance degrades markedly when key numerals are absent."[^a1]

The size of the effect is shown on ChartBench, which pairs annotated charts with unannotated ones and asks numerical questions of both. GPT-4o shows "an accuracy difference of 53.73% when answering numerical questions on annotated versus unannotated charts." Qwen3-VL, the model least affected, still shows an accuracy decline of 17.56 points.[^a2] The annotated side of the comparison is the one in which "charts feature precise numerical labels at key positions."[^a3]

The paper gives the mechanism as a habit of reasoning rather than a fact about the charts: the limitation is "a text-first reasoning paradigm that over-relies on explicit textual cues in charts (e.g., legends and data labels)."[^a4] This is the authors' account of why the drop occurs. The text does not test it separately from the drop itself.

The removal test is what turns the dependence from a comparison of two datasets into a measurement on fixed questions. Take charts that carry detailed labels, make a de-annotated version of each, and compare accuracy on the same questions. ChartAgent's authors selected 300 chart–question pairs from ChartBench and "conducted experiments with their corresponding de-annotated chart versions."[^a5] The reported result is an ordering, not a table in the text read: "in contrast to MLLMs whose accuracy drops sharply after annotation removal, ChartAgent is affected the least."[^a6]

What the removal test measures is the change in accuracy on a fixed question when the printed text is taken away. It does not measure whether the answerer used the text. It also cannot separate two causes: a model that reads the labels and loses them, and a model that cannot read the marks well enough to recover without them, both show a drop. Separating these would need a second condition that the read text does not contain. This distinction is my inference, not the paper's.

For the asker, the concept implies that whether a numerical question on a chart is answered from marks or from labels is a property of the chart-question pair, and that only the removal reveals it. A question whose key value is printed on the chart tests reading the label; the same question on the de-annotated chart tests measurement. That consequence is my reading of the measurement.

## Limits

- The ChartAgent drop on de-annotated charts is shown in a figure that the read text does not tabulate. The text gives only the ordering, "affected the least," and no number for the proposed method's drop.
- The dependence figures come from one benchmark. The text describes ChartBench as one that "targets charts with sparse textual annotations," which is the setting chosen for the test; transfer to other chart sources such as ChartQA is not shown in the slices read.
- The slices read do not say how the labels were removed from each chart, or whether removal left the marks themselves untouched. The size of the drop depends on both.
- The removal test's models are not named in the slice read, so it is not clear which of the models in the comparison produced the 17.56 and 53.73 point figures and which were run on the de-annotated set.
- The robustness is attributed to the tools by the authors: "integrated tool library and verifiable reasoning chain."[^a7] The ablation that credits the tool library reports accuracy on a ChartBench subset, not the drop under removal, so the removal result alone does not isolate the tools.

## Related

- [[literal-match-dependence]] — the retrieval analogue: evidence found through shared words rather than through the content it carries.
- [[perception-substitution-gap]] — the image-side version of the same logic: replace one modality and read the drop as where the error sits.
- [[text-answerability]] — the question-side version: an item answerable without the image at all.
- [[tool-integrated-reasoning]] — the agent setting the authors credit for the robustness to removed labels.

[^a1]: arxiv-2512-14040 — "heavily dependent on explicit textual annotations and the performance degrades markedly when key numerals are absent"
[^a2]: arxiv-2512-14040 — "exhibits an accuracy difference of 53.73% when answering numerical questions on annotated versus unannotated charts"
[^a3]: arxiv-2512-14040 — "charts feature precise numerical labels at key positions"
[^a4]: arxiv-2512-14040 — "a text-first reasoning paradigm that over-relies on explicit textual cues in charts (e.g., legends and data labels)"
[^a5]: arxiv-2512-14040 — "conducted experiments with their corresponding de-annotated chart versions"
[^a6]: arxiv-2512-14040 — "in contrast to MLLMs whose accuracy drops sharply after annotation removal, ChartAgent is affected the least"
[^a7]: arxiv-2512-14040 — "integrated tool library and verifiable reasoning chain"
