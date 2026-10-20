---
description: "Refusal is scored by an LLM judge over sampled answers, giving a signed confidence in [-1, 1] that catches government-aligned answers and deflection which pattern matching misses."
aliases: ["refusal confidence score", "LLM-as-a-judge refusal score", "judge-based refusal detection", "c(x) refusal score"]
sources: ["arxiv-2512-16602"]
---
# Judge-scored refusal confidence

A refusal can be measured by pattern matching, looking for stock phrases such as "I'm sorry" or "As an AI assistant." That measure fails on current reasoning models, which do not usually refuse in those words. The paper reports that the pattern approach was "ineffective for state-of-the-art models, which exhibit" more complex behaviour.[^c1] Their refusals are a government-aligned answer, a counter-narrative, or a topic change: "often produce answers in the form of government propaganda" rather than a refusal.[^c2] The fix the paper proposes is to let a second model judge each answer, and to turn that judgement into a continuous score rather than a yes or no.

## Mechanism

For each prompt x, the target model is sampled several times, "we sample K candidate answers" (the paper uses K = 5 with greedy decoding in its vector runs).[^c3] A separate judge model labels each answer as refusal or non-refusal under a fixed rubric, giving a label z_k in [−1, +1], with +1 for refusal.[^c4] The answers are then weighted by their likelihood under the target model. Each answer's mean token log-probability is turned into a softmax with temperature τ = 1.0, so that "to emphasize more probable completions, we compute a" weighted average.[^c5] Positive and negative weighted parts are then subtracted: the refusal confidence score c(x) lies in [−1, 1], where c(x) > 0 is a refusal and c(x) < 0 is compliance.[^c6] For reasoning models the judge sees and scores only the final answer, "both the judge input and c(x) are" computed on the answer segment.[^c7]

Two things make the score usable downstream. First, it is continuous, so a prompt can be a weak refusal rather than a hard one, and a neutral band (|c(x)| ≤ 0.15 in the paper) can be set aside. Second, the same score serves three purposes in the paper: labelling prompts for the steering vector, setting the coefficients that match projection size to refusal strength, and evaluating the steered model by the "refusal confidence percentage," the share of prompts with c(x) > 0.[^c8]

## What was measured

The judge was GPT-OSS-20B, used with sampling settings in the paper's Section 4.2.[^c9] The paper's main claim for the judge is methodological: the approach "categorizes compliance and refusal for any state-of-the-art model with minimal human effort."[^c11] The text read reports no agreement statistic between the judge and human labels, so the score is validated only by the paper's downstream effects (refusal removal and capability retention).

## Limits

- One judge model, one rubric. The rubric sits in an appendix that the text read does not include, so the exact operational definition of "refusal" is not visible here.
- No human agreement is reported in the sections read. The judge's notion of refusal is the measure's notion, and that includes any bias the judge has about political content (see [[llm-judge-validation-gap]] and [[llm-judge-biases]]).
- The benchmark's refusal target is itself a judgement. The authors accept a refusal rate of 30–40% on the political set because the set "includes some prompts that could be considered" harmful, so a perfect judge would not return 100%.[^c10]
- Circularity risk (my inference): the same judge labels the training prompts, weights the vector, selects the configuration on validation, and scores the result. Gains on the judge's own score are partly built in, so the paper's separate check on non-refusal likelihood shift matters more than the refusal numbers.
- The score measures refusal confidence on prompts. It does not measure whether the answer is true or balanced; the paper says so itself in its limitations.

## Related

- [[mean-difference-steering-vector]] — the vector whose labels this score supplies
- [[ridge-whitened-steering-direction]] — weights its prompts by these scores
- [[refusal-signal-dimensionality]] — the layer correlation computed against this score
- [[llm-judge-validation-gap]] — what a judge's score does and does not establish
- [[llm-judge-biases]] — systematic judge preferences that would enter the refusal label
- [[script-level-obfuscation]] — a related refusal measurement that reads over-refusal beside unsafe compliance

[^c1]: arxiv-2512-16602 — "ineffective for state-of-the-art models, which exhibit"
[^c2]: arxiv-2512-16602 — "refusal output space, but often produce answers"
[^c3]: arxiv-2512-16602 — "we sample K candidate answers"
[^c4]: arxiv-2512-16602 — "classified by a judge model J as either a refusal or"
[^c5]: arxiv-2512-16602 — "To emphasize more probable completions, we compute a"
[^c6]: arxiv-2512-16602 — "The resulting refusal confidence score c(x) ranges"
[^c7]: arxiv-2512-16602 — "both the judge input and c(x) are"
[^c8]: arxiv-2512-16602 — "The refusal confidence percentage is defined as the proportion of prompts with"
[^c9]: arxiv-2512-16602 — "We use GPT-OSS-20B (OpenAI, 2025) as the judge"
[^c10]: arxiv-2512-16602 — "includes some prompts that could be considered"
[^c11]: arxiv-2512-16602 — "categorizes compliance and refusal for any state-of-the-art model with minimal human effort"
