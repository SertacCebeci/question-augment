---
description: "Consistency-based confidence reads disagreement among equally correct answers as doubt, so confidence falls as answer count rises while accuracy rises; summing sampled probability mass repairs it."
aliases: ["multi-answer miscalibration", "semantic confidence aggregation", "answer-cardinality confidence drop"]
sources: ["arxiv-2602-07842"]
---
# Multi-answer confidence underestimation

Consistency-based confidence estimators assume that diverse sampled answers mean the model is unsure. That holds when a question has one correct answer. When several answers are valid, the model can split its samples across them and still be right every time. The estimate then drops, and it cannot be told apart from the drop caused by wrong answers.[^c1] The paper's example has two questions that both yield 18 of 20 correct samples. The single-answer one gets confidence 0.9. The multi-answer one splits 6/12 between two valid drugs and gets 0.3.[^c2]

## What was measured

On MACE, a benchmark of 12,000 factual questions in six domains with 1, 2, 4 or 6 correct answers each, the authors tested 15 calibration methods on four model families (7B to 72B).[^c3] Accuracy rose with the number of correct answers and estimated confidence fell. Methods that were state of the art on single-answer questions collapsed on mixed-cardinality sets.[^c4]

The drop was larger in bigger models. LLaMA 70B lost 0.154 confidence from one answer to six, against 0.056 for the 8B model.[^c5] The authors only speculate that larger models have broader knowledge coverage and so spread over more valid answers.[^c6]

## The repair: aggregate, do not take the mode

Semantic Confidence Aggregation (SCA) holds that confidence should reflect the aggregate over all valid answers and not the single most confident response. It also holds that inconsistency does not necessarily imply low confidence.[^c7] The method samples answers, clusters them semantically as in [[semantic-entropy]], and sums the token-level sequence probability inside each cluster. It then adds up the clusters whose mass exceeds a threshold tau.[^c8] The paper reports that tau = 0 performs about as well as the tuned threshold, so a plain sum over all sampled responses suffices and clustering can be skipped.[^c9] Two variants were compared: a normalized one and a frequency-count one.[^c10] SCA is reported to give the best calibration under mixed-answer settings while keeping single-answer performance.[^c11]

My reading, not the paper's claim: the failure is a mismatch between what the score measures (concentration of the answer distribution) and what calibration needs (total probability that the answer is acceptable). Both are one quantity only when the acceptable set has size one.

## Limits

- The question format fixes how many answers are correct. Real questions do not announce this, and the paper does not say how a user or model would know the cardinality.
- The explanation for the scale effect is a stated speculation, not a tested mechanism.
- The domains are factual questions built from Wikidata triples. Open-ended or opinion questions, where "correct" is graded, were not tested.
- Summation of sequence probabilities needs token probabilities, so black-box API use is limited.
- The method sections concentrate on one 70B model; other models are in an appendix I did not read.

## Related

- [[semantic-entropy]] — the clustering baseline whose low-diversity-means-confidence assumption fails here
- [[confidently-wrong-low-entropy-regime]] — the opposite failure: low entropy with wrong answers
- [[conformal-prediction]] — a set-valued alternative that also accepts several answers

[^c1]: arxiv-2602-07842 — "Disagreement among sampled correct answers yields low estimated confidence, indistinguishable from the low confidence caused by the presence"
[^c2]: arxiv-2602-07842 — "Despite achieving the"
[^c3]: arxiv-2602-07842 — "a benchmark of 12,000 question–answer pairs"
[^c4]: arxiv-2602-07842 — "as the number of correct answers increases, LLMs achieve higher QA accuracy but exhibit lower confidence"
[^c5]: arxiv-2602-07842 — "the 70B model exhibits"
[^c6]: arxiv-2602-07842 — "We speculate that this is"
[^c7]: arxiv-2602-07842 — "that response inconsistency (e.g., high entropy)"
[^c8]: arxiv-2602-07842 — "we compute its confidence as the"
[^c9]: arxiv-2602-07842 — "simply summing token-level probabilities over all sampled"
[^c10]: arxiv-2602-07842 — "Semantic Normalized Confidence"
[^c11]: arxiv-2602-07842 — "SCA achieves state-ofthe-art calibration performance under mixedanswer settings while preserving strong calibration on single-answer questions."
