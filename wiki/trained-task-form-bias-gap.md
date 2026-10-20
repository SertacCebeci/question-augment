---
description: "Posed as question answering, the same content draws more stereotyped answers from a multitask model than posed as NLI; novel prompt templates in the trained form do not close the gap."
aliases: ["task-form bias gap", "input-form bias effect", "trained-form bias exposure", "form-dependent bias in prompt-based models"]
sources: ["doi-10-48550-arxiv-2205-11605"]
---
# Trained-task-form bias gap

Akyürek et al. hold the content of a social-bias item fixed and change only the form in which it is encoded. The model studied is T0, a text-to-text model fine-tuned on many tasks through prompts. One form is question answering, the format of BBQ and of several training datasets; the other is premise-hypothesis natural language inference, the form that is unlike T0's training examples.[^c1] The result they report is that "acts more biased in question answering form,"[^c1] and that QA "results in more bias than NLI, a novel input form."[^c2]

The effect is a difference in what the model does with the same scenario. In BBQ, the QA form (negative and non-negative questions) produced bias scores of about 43.6 for gender and 37.2 for religion, against 4.5 and 14.0 for the NLI conversion of the same items. For race the two forms were level, about 12.6 and 12.8.[^c3] The authors' summary is that "QA and QAn predictions are substantially more biased than NLI predictions for gender and religion domains."[^c4] On their new NLI benchmark BBNLI, the QA form "results in higher bias across more subtopics."[^c5]

The mechanism the authors give is about what the model falls back on when a question is familiar. Because QA datasets used in training are themselves likely to contain biases, "which makes it easy for T0 to exhibit stereotypical associations learned during the" training when it meets the QA form.[^c6] A second observation concerns abstention. An ambiguous scenario should lead to an "unknown" answer, but in QA "T0 fails to remain abstained and almost always makes a choice between" the target and non-target group.[^c7] In the familiar form the model is also more likely to "rely on spurious correlations when providing answers rather than generating a correct answer."[^c16] This is the authors' reading, and they call it likely rather than tested.

The natural control is a novel prompt template in the same QA form. Those templates reduced the bias but did not remove the gap, and the authors take this as evidence that the task is what matters: "We speculate that the novelty of task has a greater effect on biased outputs than the novelty prompt templates."[^c8] Their claim is that "such associations cannot be consistently prevented by simply using novel prompt templates,"[^c9] which is a reading of the template results and not a separate experiment.

What the form changes is the question itself. Re-encoding a question as an entailment problem changes which answer the model is able to give, and so changes which stereotype it can express. My inference, from the paper's numbers: a bias measurement is a measurement of the model together with the task form, so a figure reported for one form does not transfer to another. The authors' proposed use follows the same logic: "alternative input formulations to those appeared in training may be used to alleviate biases without much sacrifice on performance."[^c10]

## Limits

- One model, T0pp (the best-performing T0 checkpoint), sampled five times per example with three templates per form.[^c11] Whether the gap holds for other multitask or instruction-tuned models is not tested.
- The gap is domain-dependent: race shows no QA–NLI difference in BBQ (see above), so the form effect is not uniform across stereotype types.
- The explanation through training-data bias is a hypothesis. The authors propose a test as future work: "whether limiting the set of training tasks to those" that are not popular "would result in less biased predictions."[^c12] They have not run it.
- Novel prompts changed scores strongly per subtopic, but the change "is not reflected in the mean."[^c13] A single aggregate hides subtopic-level swings in both directions.
- NLI is not bias-free: "While scores for NLI are also positive, they are much smaller in comparison."[^c14]
- BBNLI was written by the authors and covers three domains; "we were not able to include every ethnicity, gender, and religious point of view."[^c15] The gap is measured only on the stereotypes that were included.

## Related

- [[paired-stereotype-bias-score]] — the score used to measure the gap, and its companion accuracy gap
- [[answer-format-dependent-bias-measurement]] — the answer format of the instrument changes measured bias; here it is the task framing of the input
- [[format-familiarity-confound-in-fine-tuned-gains]] — the same familiarity logic applied to output-format and instruction exposure in tabular fine-tuning
- [[prompt-content-over-surface-form]] — surface prompt changes matter less than content; this note's form change alters the task, not only the surface
- [[short-form-check-blindness-to-open-ended-bias]] — another case where the question format decides which bias becomes visible

[^c1]: doi-10-48550-arxiv-2205-11605 — "acts more biased in question answering form,"
[^c2]: doi-10-48550-arxiv-2205-11605 — "bias than NLI, a novel input form."
[^c3]: doi-10-48550-arxiv-2205-11605
[^c4]: doi-10-48550-arxiv-2205-11605 — "Further, QA and QAn predictions are substantially more biased than NLI predictions for gender and religion domains."
[^c5]: doi-10-48550-arxiv-2205-11605 — "form results in higher bias across more subtopics."
[^c6]: doi-10-48550-arxiv-2205-11605 — "which makes it easy for T0 to exhibit stereotypical associations learned during the"
[^c7]: doi-10-48550-arxiv-2205-11605 — "T0 fails to remain abstained and almost always makes a choice between"
[^c8]: doi-10-48550-arxiv-2205-11605 — "outputs than the novelty prompt templates."
[^c9]: doi-10-48550-arxiv-2205-11605 — "prevented by simply using novel prompt templates,"
[^c10]: doi-10-48550-arxiv-2205-11605 — "to those appeared in training may be used to alleviate biases without much sacrifice on performance."
[^c11]: doi-10-48550-arxiv-2205-11605 — "In all of our experiments we use the bestperforming checkpoint of T0-suite"
[^c12]: doi-10-48550-arxiv-2205-11605 — "whether limiting the set of training tasks to those"
[^c13]: doi-10-48550-arxiv-2205-11605 — "effect is not reflected in the mean."
[^c14]: doi-10-48550-arxiv-2205-11605 — "While scores for NLI are also positive, they are much"
[^c15]: doi-10-48550-arxiv-2205-11605 — "not able to include every ethnicity, gender, and religious point of view."
[^c16]: doi-10-48550-arxiv-2205-11605 — "rely on spurious correlations when providing answers rather than generating a correct answer"
