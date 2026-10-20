---
description: "A generated output is scored without a gold reference: source and output become triplets, are aligned, and missing and extra facts are counted and weighted."
aliases: ["referenceless evaluation", "reference-free source-grounded scoring", "triplet alignment metric"]
sources: ["arxiv-2512-15907"]
---
# Reference-less scoring by source alignment

A generated output can be scored without a gold answer by checking it against the source it was produced from. In the TAB R E X framework, built for generated tables, the check has three stages. Source text and output are each converted into knowledge-graph triplets; the paper's stated aim is to convert "both reference text and generated tables into structured graphs" so that the table "can be judged directly against the textual evidence."[^c1] The two graphs are then aligned in two passes: a deterministic pass "aligns triplets with identical or" schema-normalized subject–predicate pairs, and an LLM-assisted pass resolves what is left, such as paraphrases and abbreviations.[^c2] Every matched pair carries a difference record, and unmatched triplets are counted on one side or the other: facts the source has and the output lacks, and facts the output has that the source does not support.[^c3]

The score is a function of those counts. The paper's own summary is that "Because all quantities are derived directly from A, the score remains reference-less, and fully explainable."[^c4] The word "reference-less" here does not mean ungrounded. The source plays the role a reference would play, but it is re-read for each output rather than fixed in advance. The authors' diagnosis of prior metrics is that they "rely on fixed references that limit generalization."[^c5]

Missing and extra counts are kept apart and weighted separately. Raising the weight on missing facts "favors sensitivity (rewarding comprehensive coverage)"; raising the weight on extra facts "favors specificity (penalizing hallucinated entries)."[^c6] The paper presents this as a dial: the metric offers "tunable trade-offs between sensitivity (coverage) and specificity (hallucination control)."[^c7] Here the two words name the two counts that are weighted, not the two rates measured in the evaluation. The benchmark measures sensitivity and specificity as true-positive and true-negative rates on perturbed tables, a separate use of the same terms.[^c8]

Against a reference-free alternative that scores through generated questions, the authors argue that the question-answer signal "often penalizes harmless re-orderings or formatting," whereas explicit alignment of extracted facts separates meaningful discrepancies from surface variation.[^c9] This is the authors' argument and their comparison, not a general result.

What survives the transfer: the idea that an output is judged by an explicit correspondence to its source, with omission and insertion counted apart, so that the weight on each is a visible choice. What does not obviously survive: the rule-based unrolling of tables into triplets, which is specific to structured data. Whether the same alignment works for free-text answers to questions is my inference, not something the paper tests.

## Limits

- Tested only on tables. The benchmark, TAB R E X-BENCH, spans six domains and twelve perturbation types, but the authors state its scope as "English and synthetic perturbations."[^c10] Real-world noise and multilingual data are untested.
- The pipeline depends on language models for extraction and alignment, and the authors say this "adds computational cost and mild variability."[^c11] A score that moves between runs is a weaker measure than one that does not.
- The method handles structured digital tables only: "The current implementation supports only structured digital tables."[^c12]
- Reference-less is only as good as extraction. A fact the source-to-triplet step misses cannot be counted as missing, and a spurious source triplet produces a false missing count. The paper reports no error analysis of the extraction stage in the parts I read. This is my inference.
- The chosen weights encode which error matters more, a normative setting in its own right (see [[evaluation-choices-encode-error-priorities]]). The paper shows the trade-off can be moved, not which setting is right for a given task.

## Related

- [[evaluation-choices-encode-error-priorities]] — the separate weights on missing and extra facts are one place where the choice of which error counts is made explicit
- [[question-based-summary-evaluation]] — another reference-free scorer; it works through generated questions answered on both sides rather than through triplet alignment
- [[weighted-nugget-recall]] — the reference-based counterpart, scoring atomic facts against a fixed set
- [[three-test-metric-validity-audit]] — checks metrics by perturbation sensitivity, the same kind of test the TAB R E X-BENCH is built for

[^c1]: arxiv-2512-15907 — "converts both reference text and generated tables into structured graphs"
[^c2]: arxiv-2512-15907 — "a deterministic pass aligns triplets with identical or"
[^c3]: arxiv-2512-15907 — "counts of missing (MI), extra (EI), and"
[^c4]: arxiv-2512-15907 — "Because all quantities are derived directly from A, the score remains reference-less, and fully explainable."
[^c5]: arxiv-2512-15907 — "fixed references that limit generalization"
[^c6]: arxiv-2512-15907 — "favors sensitivity (rewarding comprehensive coverage)"
[^c7]: arxiv-2512-15907 — "tunable trade-offs between sensitivity (coverage) and specificity (hallucination control)"
[^c8]: arxiv-2512-15907 — "compute truepositive and true-negative rates (sensitivity and"
[^c9]: arxiv-2512-15907 — "often penalizes harmless re-orderings or formatting"
[^c10]: arxiv-2512-15907 — "English and synthetic perturbations"
[^c11]: arxiv-2512-15907 — "which adds computational cost and mild variability"
[^c12]: arxiv-2512-15907 — "The current implementation supports only structured digital tables"
