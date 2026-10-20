---
description: "Generate questions from a summary and its source, answer both, and score precision (answers agree) and recall (important questions answerable); unifying the two beats either alone, with no reference."
aliases: ["QAGS", "QuestEval", "QA-based evaluation", "question-answering-based summarization metric"]
sources: ["scialom-2021", "wang-2020"]
---
# Question-based summary evaluation

A text can be evaluated by asking questions of it. A question generator (QG) turns a text into question-answer pairs, and a question answerer (QA) answers them against another text. QuestEval runs this in two directions and combines them.[^c1]

## Mechanism

**Answerability is an explicit output.** A summary may not contain the answer, so the QA model must be able to say a question is unanswerable. The QA component therefore includes an unanswerable token among its possible outputs.[^c2]

**Question generation is filtered by answering.** Questions are generated from named entities and nouns as candidate answers. Any question the QA model answers incorrectly is dropped, so only self-consistent pairs remain.[^c3]

**Precision (consistency).** Questions are generated from the summary and answered against the source. The summary is inconsistent if the answer differs when conditioned on summary versus source. The score is the mean F1 between the two answers.[^c4] F1 is used here because a true negative must be detected: an answer that is merely answerable but means something different must not pass.[^c5]

**Recall (relevance).** Questions are generated from the source and tested for answerability on the summary. Recall uses the QA confidence of answerability rather than F1, so "ACL" and "Association for Computational Linguistics" are not penalised as different. The cost is that it ignores a summary that answers incorrectly.[^c6]

**Query weighting.** Not all source questions matter, because a summary is length-limited. A weighter is trained to label a question important if the human summary answers it, giving a probability of importance per question. It applies only to recall.[^c7] The weighter encodes a dataset policy ("what kind of questions are likely answered in the CNN/Daily Mail training summaries?"), not a universal notion of importance.[^c8]

**Unification.** The final score is the harmonic mean of precision and recall.[^c9]

## What was measured

Precision-only and recall-only metrics each track one human dimension. SummaQA (recall) correlated better with relevance than consistency (26.2 vs 8.3), and QAGS (precision) the reverse (9.1 vs 20.4). Unifying them raised the average correlation from 28.4 to 33.5.[^c10] The learned weighter helped most on relevance (37.5 to 39.2).[^c10] Reference-based metrics lose correlation as references fall from 11 to 1, while QuestEval needs none.[^c11]

## The precision half alone: QAGS

QAGS (wang-2020) is the consistency-only ancestor of the precision direction. Its premise is that questions asked of a summary and of its source get similar answers exactly when the summary is factually consistent.[^c14] The score generates K=20 questions from the summary, answers each against both texts with an extractive QA model, compares answers by token F1, and averages.[^c15] It correlated with human consistency judgments at 54.53 (CNN/DM) and 17.49 (XSUM), well above n-gram and BERTScore baselines.[^c16] The authors speculate the gain on CNN/DM comes from the QA model's sensitivity to fused sentences, where the answer from summary and source diverge.[^c17]

Ablations bound how much the instrument matters. Correlation stayed high across QG quality, though a QG model tuned on SQuAD instead of NewsQA lost a few points (51.53 vs 54.53 on CNN/DM), a domain-shift cost.[^c18] More questions helped with diminishing returns beyond about 50, and the stricter exact match lowered CNN/DM correlation to 45.97 versus F1's 54.53.[^c19] The inspectable question-answer pairs show which summary tokens are inconsistent.[^c20]

## Limits

- QAGS covers consistency only; it does not test relevance, which the recall direction adds.
- Human agreement was moderate to fair (Krippendorff alpha 0.51 and 0.34), so the ceiling of the correlation target is low, especially on XSUM; this is from the paper's reported figures, my reading of what that implies.
- The weighter learns one corpus's editorial policy; the paper itself notes that importance depends on the reader's point of view.[^c12]
- Answer candidates are entities and nouns, so facts expressed in other forms (relations, causality) are not probed. This is my inference from the generation procedure.
- Nucleus sampling to diversify questions did not help, so question coverage is bounded by the generator.[^c13]
- Correlation with human judgment was tested on news summarization datasets only; other genres and non-factoid content are untested.
- Correlation is not the same as validity: the metric inherits whatever the QA and QG models get wrong.

## Related

- [[answerability-delta-process-reward]] — also uses change in answer quality as a signal, there as a training reward
- [[gated-answerability-rule]] — answerability as a decision, here as a measurement
- [[calibrated-question-generation]] — question generation as the instrument that other work builds on
- [[attribution-aware-rl-reward]] — checking an answer against its source evidence

[^c1]: scialom-2021 — "QuestEval consists of a QG component QG and a QA component QA"
[^c2]: scialom-2021 — "Our QA component thus includes the unanswerable token"
[^c3]: scialom-2021 — "We filter out every question for which the QA model predicts an incorrect answer."
[^c4]: scialom-2021 — "A summary is deemed inconsistent with respect to its source text if, given a question, the answer differs when conditioned on S or D."
[^c5]: scialom-2021 — "for precision it is crucial to detect true negatives."
[^c6]: scialom-2021 — "but does not take into account possible model hallucinations"
[^c7]: scialom-2021 — "Note that the question weighter only concerns recall, and therefore is not applied when computing precision."
[^c8]: scialom-2021 — "what kind of questions are likely answered in the CNN/Daily Mail training summaries?"
[^c9]: scialom-2021 — "The final QuestEval score accounts for both"
[^c10]: scialom-2021 — "improving the average correlation by 18% (28.4 to 33.5)"
[^c11]: scialom-2021 — "the correlations decrease and the variance increases as the number of references decreases"
[^c12]: scialom-2021 — "point of view, which makes summarization evaluation challenging"
[^c13]: scialom-2021 — "with no success."
[^c14]: wang-2020 — "QAGS is based on the intuition that if we ask questions about a summary and its source, we will receive similar answers if the summary is factually consistent with the source."
[^c15]: wang-2020 — "(4) averaging the answer similarity metric over all questions."
[^c16]: wang-2020 — "QAGS obtains substantially higher correlations than all"
[^c17]: wang-2020 — "We speculate that this large increase"
[^c18]: wang-2020 — "The drop in performance indicates a"
[^c19]: wang-2020 — "Exact match is another common"
[^c20]: wang-2020 — "QAGS offers a natural form of interpretability: The answers and questions generated while computing QAGS indicate which tokens of a summary"
