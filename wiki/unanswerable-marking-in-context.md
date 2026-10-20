---
description: "Keeping a sub-question that retrieval could not answer in the generation prompt, marked as unanswerable, yields more grounded text than dropping it from the prompt."
aliases: ["unanswerable-question marking", "explicit not-enough-information marker", "highlighted unanswerable sub-questions"]
sources: ["doi-10-48550-arxiv-2408-10490"]
---
# Unanswerable marking in the generation context

When a model writes long-form text from a plan, each planned question goes to a search and then to an answering model. If the answering model is not confident, the question has no answer to give. The context can then do one of two things: drop the question, or keep it with its answer field set to unanswerable. Godbole et al. compare the two and keep the second as their default. In their pipeline, a question that the QA model is not confident about is kept, and its answer is marked: "we keep the question but mark the" answer as unanswerable.[^c1]

The reason given is that a gap the writer does not see is a gap it fills. The authors hypothesize that these questions "could lead to hallucinations from the model, especially if text is generated to provide an answer to them."[^c2] My reading of the mechanism: a question with no marker is a slot the writer must complete, and it completes it from parametric memory. A marked question tells the writer that the evidence does not cover that slot, so the writer can skip it.

The marked form carries an instruction. Instead of an answer, the question is followed by "Not enough information. Skip this question."[^c3] The comparison is against removing the question from the context. The paper reports that "explicitly highlighting unanswerable questions leads to more grounded generation."[^c4] On the Researcher and News Events sets with text-unicorn-001, "Highlighting unaswerable questions leads to increase in the AIS metric."[^c5]

The gap is not rare. The authors note that some generated questions "will not necessarily be answerable even when considering the second round of search."[^c6] So the marking is a routine part of plan-based retrieval, not an edge case.

## Limits

- The effect is one comparison on two of the paper's datasets, with one model. The text I read does not give the effect on the other sets, and the paper's second model (Mistral, in its later section) was not read for this point.
- Unanswerable is decided by a confidence threshold on the QA model's response.[^c7] A miscalibrated threshold would mark answerable questions as gaps, or pass real gaps as answered. The threshold was not varied.
- The marker is one fixed string. A different wording, or a model that ignores the skip instruction, was not tested.
- AIS scores whether a statement is supported by the sources. It does not score whether a skipped slot leaves the text less informative. The paper reports a length and attribution trade-off in a neighbouring comparison: "this prompt allows for a trade-off between generation length and attribution."[^c8] A marked gap may lower length as well as errors; the paper's measures do not separate the two.
- The mechanism above (a slot the writer fills from memory) is my inference. The paper states the hypothesis and shows the metric moves; it does not inspect what the writer does at a marked slot.

## Related

- [[abstention]] — the answerer declining to answer; here the context reports a gap and tells the writer to skip that one item, not to refuse the output.
- [[plan-before-search-anchoring]] — the plan supplies the sub-questions whose gaps get marked.
- [[memory-induced-unawareness]] — the same mechanism from the other side: a context with no marker for what is unfilled raises hallucination, in a personal-assistant setting.

[^c1]: doi-10-48550-arxiv-2408-10490 — "we keep the question but mark the"
[^c2]: doi-10-48550-arxiv-2408-10490 — "could lead to hallucinations from the model, especially if text is generated to provide an answer to them."
[^c3]: doi-10-48550-arxiv-2408-10490 — "we follow the question with the response Not enough information. Skip this question."
[^c4]: doi-10-48550-arxiv-2408-10490 — "explicitly highlighting unanswerable questions leads to more grounded generation."
[^c5]: doi-10-48550-arxiv-2408-10490 — "Highlighting unaswerable questions leads to increase in the AIS metric."
[^c6]: doi-10-48550-arxiv-2408-10490 — "will not necessarily be answerable even when considering the second round of search"
[^c7]: doi-10-48550-arxiv-2408-10490 — "We determine if a question is unanswerable by confidence threshold on the QA model"
[^c8]: doi-10-48550-arxiv-2408-10490 — "this prompt allows for a trade-off between generation length and attribution"
