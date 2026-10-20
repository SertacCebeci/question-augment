---
description: "A recall-oriented generator then a precision-oriented verifier trades recall for precision on candidate lists; on an EU Taxonomy benchmark it gave only a modest F1 gain."
aliases: ["generate-then-verify", "candidate generation and verification", "high-recall generation with verification filter", "two-stage generate-and-filter", "generate-then-validate"]
sources: ["arxiv-2512-24289", "arxiv-2512-10110"]
---
# Generate-then-verify candidate pipeline

A task that asks for a list of items has two kinds of error: missed items (low recall) and wrong items included (low precision). A single prompt tends to move along one axis at the cost of the other. The generate-then-verify pipeline splits the job in two. A first call is told to be broad, and a second call takes that list and keeps only what it can support. The idea is that the two jobs can be separated and each scored on its own output. The paper frames its multi-agent test in exactly these terms: it asks whether "a pipeline that combines candidate generation with a verification step" can improve on single-step prediction.[^c1]

The mechanism shows up in the single-step baselines first. On EU Taxonomy activity identification, the best single-step run reached an F1 of 0.311, with concise company metadata.[^c2] The models sat at different points on the trade-off. Gemini Flash 2.5 and Mistral favored recall, with recall up to 0.526, while Llama favored precision.[^c3] Another run reached the highest precision, 0.348, which the authors read as a sign that models suit different workflow stages.[^c4]

The pipeline then uses that difference. In the parallel design, the highest-recall model generated candidate activities from the full report; at that stage the table reports precision 0.2110 and recall 0.5404. A summary of the report was then the context for a verification agent that filtered the candidate list.[^c5] The verification step raised precision from 0.211 to 0.3436, while recall fell to 0.4016 and F1 reached 0.3285 (the recall and F1 values are read from the table).[^c6] The authors describe this as a modest gain over the best single step.[^c8]

Two structural points follow from this arrangement. First, the verifier only filters a list, so it cannot add items the generator missed; end-to-end recall is capped by the generator's recall (my inference from the design). The verification trades recall for precision, and whether F1 rises depends on how much precision is bought per unit of recall lost. Here the trade bought about 0.017 F1 over the best single step. Second, what each stage reads matters. The sequential variant summarised the report first and generated candidates from the summary. The workflow underperformed the baseline, with a final F1 of 0.2957, which the authors attribute to information loss in the summary.[^c7]

The paper's context results suggest why the split is useful. It reports that "concise context favors precision, while full-text context aids discovery."[^c12] A recall-heavy generator benefits from the full text, and a precision-heavy verifier can work from a compressed view. The parallel design did roughly this: the generator read the full report, and the verifier read a summary. The paper does not isolate this choice, so the reading is mine.

The same shape appears in a second setting, where it is called generate-then-validate. A small language model writes multiple-choice questions for a learning objective, and the pipeline "begins with a high generation target (e.g., 200 questions per LO)".[^c14] Of the 8,200 candidates, syntactic filtering left the pool at "we retained 6,043 questions",[^c15] and the two probability-based checks ended with "produced a final pool of 3,205 questions covering all 41 LOs".[^c16] The authors justify the discard by volume: "It is unrealistic to expect an SLM to succeed in one shot", and the hope is that a large number of tries yields good items by the law of large numbers.[^c17] The filter structure matches the one above: the later stages can only remove items, so the yield is capped by what the generator produced (my inference). What differs is the verifier. Here the checks read the generator's own probabilities rather than a second prompt; see [[answer-label-confidence-filter]] and objective-conditioned-log-probability-gain.

## Limits

- The pipeline was tested on a sample of 50 companies, with one model family (Gemini Flash 2.5) as the generator.[^c10] The gap between 0.311 and 0.3285 is small. The text I read reports no significance test, and with 50 companies the difference may sit within sampling noise.
- "significantly improved precision" is the authors' wording. No test is reported in the text read, so the claim here concerns the size of the shift, not its statistical reliability.
- The ground-truth labels were produced by an LLM (Gemini-Flash-2.0) with a zero-shot prompt, an LLM self-verification step, and a final human review.[^c11] F1 measures agreement with that label set, not with the regulation itself.
- The text does not separate the verifier's contribution from the choice to give it a summary rather than the full report. Whether a full-report verifier would gain more, or lose recall in some other way, is not tested.
- Verification here relies on verbalised judgements from prompted models. The same paper finds that model confidence is poorly calibrated for this task: ECE reaches 0.684 with the full report, and the highest-recall model was the most poorly calibrated.[^c9][^c13] A verifier's "keep" is therefore not a usable probability; this is the paper's finding about confidence, not a test of the verifier.
- Only prompting strategies were tested. No fine-tuned generator or verifier was compared.
- In the second setting the generator and the validator are the same small model (Phi-2 writes and checks the items). The validation gain is measured by Gemini as a surrogate judge, and people judged only "creating an evaluation set of 64 MCQs".[^c18] The authors state that the validation steps "as they significantly enhance the quality of the generated questions";[^c19] that rests on the surrogate judge and on one set of 41 objectives, not on the items' truth.

## Related

- [[medium-context-sweet-spot-for-numeric-prediction]] — the same "more text is not always better" pattern, here on numeric prediction; the pipeline's split is one way to avoid giving full text to the precision step.
- [[multi-agent-process-verification-unreliability]] — verifying intermediate steps raises accuracy only noisily; here the verifier's gain is one modest number on one task.
- [[llm-filtered-pseudo-relevance-feedback]] — an LLM judge filters a top-k list before the list is used; the same filter-then-use shape, in retrieval.
- [[pessimistic-min-judge-aggregation]] — how several judges' verdicts are combined into one reward; a different question from a single verifier.
- [[answer-label-confidence-filter]] — the answer-side validation stage of the generate-then-validate setting; it reads the generator's own label probabilities, not a second model's verdict.
- objective-conditioned-log-probability-gain — the alignment stage of the same setting, which scores each question against its objective by a log-probability gain.

[^c1]: arxiv-2512-24289 — "a pipeline that combines candidate generation with a verification step"
[^c2]: arxiv-2512-24289 — "highest F 1-score (0.311) when provided with concise company metadata."
[^c3]: arxiv-2512-24289 — "favored high recall (up to 0.526), while Llama"
[^c4]: arxiv-2512-24289 — "achieved the highest precision (0.348), suggesting"
[^c5]: arxiv-2512-24289 — "This summary was then used as the context for a verification agent to filter the candidate"
[^c6]: arxiv-2512-24289 — "The verification step significantly improved precision (from 0.211 to 0.3436), resulting"
[^c7]: arxiv-2512-24289 — "This workflow underperformed the baseline, with a final F 1-score of"
[^c8]: arxiv-2512-24289 — "This modestly outperforms the best single-step model (0.311) and"
[^c9]: arxiv-2512-24289 — "highest recall, was also the most poorly calibrated,"
[^c10]: arxiv-2512-24289 — "We tested two architectures on a sample of"
[^c11]: arxiv-2512-24289 — "LLM (Gemini-Flash-2.0) with a zero-shot prompting strategy, followed by an LLM-based selfverification step"
[^c12]: arxiv-2512-24289 — "concise context favors precision, while full-text context aids discovery"
[^c13]: arxiv-2512-24289 — "at 0.684 when using the full report."
[^c14]: arxiv-2512-10110 — "begins with a high generation target (e.g., 200 questions per LO)"
[^c15]: arxiv-2512-10110 — "we retained 6,043 questions"
[^c16]: arxiv-2512-10110 — "produced a final pool of 3,205 questions covering all 41 LOs"
[^c17]: arxiv-2512-10110 — "It is unrealistic to expect an SLM to succeed in one shot"
[^c18]: arxiv-2512-10110 — "creating an evaluation set of 64 MCQs"
[^c19]: arxiv-2512-10110 — "as they significantly enhance the quality of the generated questions"
