---
description: "Stripping the final answer from a reasoning trace and checking whether the remaining steps support the conclusion measures inconsistency apart from accuracy; a correct answer can still fail."
aliases: ["trace inconsistency rate", "TIR", "reasoning-answer misalignment", "reasoning-answer alignment"]
sources: ["arxiv-2512-22712"]
---
# Answer-blind trace support

A reasoning trace can be scored without its conclusion. The procedure removes the final answer, keeps the steps, and asks an evaluator what answer those steps support, choosing among the original options or marking the trace "inconclusive".[^c1] The name "answer-blind" is mine; the paper does not use it. The evaluator is a human annotator or a model, and it reads the question but not the model's answer.[^c2] A trace is consistent when the answer it supports matches the answer the model gave.

The primary metric is the Trace Inconsistency Rate (TIR), "the proportion of cases where reasoning fails to support" the model's conclusion, "regardless of answer correctness".[^c3][^c4] The mechanism rests on two separate checks. Correctness compares the model's final answer with the gold label. Consistency asks "whether the reasoning trace logically supports the model" in its stated conclusion.[^c5] Crossing them gives four cases: a correct answer with support, a correct answer without it, an incorrect answer with support, and an incorrect answer without it. The fourth cell is what a plain accuracy score cannot see: the model reaches the right option while its steps point elsewhere, "getting the right answer for the wrong reasons".[^c6]

The paper reports that this gap is not only a side effect of wrong answers: "this misalignment occurs both when models answer correctly" and when they answer incorrectly.[^c7] Its failure taxonomy, built by annotation, places the main cause in evidence: failures "primarily from evidential errors", such as unsupported claims and ambiguous facts, followed by illogical steps.[^c8]

The language result follows from the same measure. Over 65k traces from GlobalMMLU, six languages and six models, the paper finds that "Reasoning traces in nonLatin scripts show at least twice as much misalignment" than Latin-script traces.[^c9] Accuracy falls across resource levels, but alignment "disproportionately drops over two-fold", so an accuracy-only evaluation of multilingual reasoning gives an incomplete picture.[^c10]

Reading the trace in English requires translation. The paper back-translates non-English traces to English before judging them,[^c11] so a translation error would enter the non-English scores directly.

## Limits

- The procedure needs a closed option set. The evaluator maps a trace to one letter or to "inconclusive"; a free-text answer has no such target, and the paper does not test one.
- The data are multiple-choice items in "7 fact-retrieval centric domains".[^c12] Reasoning-heavy tasks such as competition mathematics are not in the evaluation; the paper's own related-work section lists math benchmarks it does not use here.
- Back-translation quality was checked on only "a small sample of translations".[^c13] The script comparison therefore rests partly on unverified translation.
- Human agreement is modest. Logical coherence reached only "fair consistency" (κ = 0.39).[^c14] The automated evaluator agreed with human consensus at κ of about 0.43 to 0.53, on a validation set of 24 items "after excluding human disagreements".[^c15] The claim that automated scoring can stand in for human judgment is thin at that size.
- The automated evaluator is "Llama-4-Scout-Instruct as an automated" evaluator,[^c16] which is also one of the six models whose traces it judges. My inference: a shared model family may share blind spots with the traces it reads, and the paper's text does not test for this.
- A trace that supports the answer is not shown to have produced it. Support is judged by inference from the steps; no intervention on the steps is reported, so this measure does not test causal faithfulness.
- The "at least twice" figure is the paper's own, from one annotation and one model set; I did not find an interval for it in the text I read.

## Related

- [[trace-conditioned-answer-consistency]] — also re-reads a completed trace, but as a single-model uncertainty score fitted on correctness labels; this note scores support by an outside evaluator with the answer removed, and needs no correctness label.
- [[cot-reasoning-faithfulness-by-truncation]] — a causal test of whether the answer depends on the reasoning; the answer-blind test asks whether the steps imply the answer, a different property.
- [[supported-faithfulness-score]] — checks each claim against evidence; the answer-blind test checks only the conclusion the steps reach.
- [[reasoning-language-ue-bottleneck]] — the same question of reasoning in low-resource languages, measured through uncertainty estimation rather than trace support.

[^c1]: arxiv-2512-22712 — "removing the final answer, allowing us to evaluate what conclusion the reasoning itself supports"
[^c2]: arxiv-2512-22712 — "examine both the original question and the model"
[^c3]: arxiv-2512-22712 — "the proportion of cases where reasoning fails to support"
[^c4]: arxiv-2512-22712 — "regardless of answer correctness"
[^c5]: arxiv-2512-22712 — "Whether the reasoning trace logically supports the model"
[^c6]: arxiv-2512-22712 — "getting the right answer for the wrong reasons"
[^c7]: arxiv-2512-22712 — "this misalignment occurs both when models answer correctly"
[^c8]: arxiv-2512-22712 — "primarily from evidential errors"
[^c9]: arxiv-2512-22712 — "Reasoning traces in nonLatin scripts show at least twice as much misalignment"
[^c10]: arxiv-2512-22712 — "disproportionately drops over two-fold"
[^c11]: arxiv-2512-22712 — "back-translate non-English responses to English"
[^c12]: arxiv-2512-22712 — "7 fact-retrieval centric domains"
[^c13]: arxiv-2512-22712 — "small sample of translations"
[^c14]: arxiv-2512-22712 — "fair consistency on logical coherence assessment"
[^c15]: arxiv-2512-22712 — "after excluding human disagreements"
[^c16]: arxiv-2512-22712 — "Llama-4-Scout-Instruct as an automated"
