---
description: "Hiding the reference answer from the extractor and the source image from the judge lowers reward-model false positives, since each grader could otherwise copy or infer the answer."
aliases: ["minimal exposure", "reference withholding for graders", "target leakage in reward models", "image-blind judge"]
sources: ["doi-10-48550-arxiv-2605-30244", "doi-10-48550-arxiv-2608-25580"]
---
# Minimal exposure in grading

A grader that scores a response against a reference can get the right score for the wrong reason. The reference may let it match the answer key without finding the answer in the response, and an image may let it answer the task itself and credit the response for that answer. Minimal exposure is the rule of giving each grader only what its own step needs. In the RLR3 framework, the extractor on the verifiable path "does not see" the verifier's target arguments, and the judge on the fuzzy path sees the text prompt, the response, the criterion and the textual reference, "excluding the source image."[^c1] The reason is stated directly: "if the target arguments were visible, the extractor might copy the required values from them instead of extracting them from the response."[^c2] For the judge: "The judge might infer the task answer even when the response does not state it."[^c3]

Both paths also use the same text-only model, "share the same parameters" in the paper's words, so the restriction is a property of inputs, not of two different models.[^c4]

The effect is measured on a reward model's false-positive rate, not on a policy's training run. Making the target visible raises the rate: "exposure shows higher FPRs on no-final-answer responses (15.7% vs. 11.5%)" under unlimited exposure, against the default.[^c5] The authors read this as a copy shortcut: "exposing target values creates a shortcut for GenRM to copy or anchor on the reference answer instead of."[^c6] Giving the judge the image shows the same direction. The authors hypothesize "that visual access makes the model more likely to infer" the answer and fill the arguments with it, which raises false positives on incomplete responses.[^c7]

What the mechanism is: the false positive needs a source of the answer other than the response. Withholding the reference removes one source, and withholding the image removes another. The response is then judged on what it contains. This is a claim about information flow, not about the grader's skill; a stronger grader that copies the reference more fluently gets no benefit from the restriction (my inference from the copy-shortcut reading).

## Limits

- The measured gaps are small in absolute terms. Against the default, unlimited exposure moves no-final-answer false positives from 11.5% to 15.7% and adversarial from 18.0% to 22.4%; the authors do not claim a large effect and their scoring accuracy on regular responses stays near 95%.[^c8]
- The evidence is a constructed audit: abnormal responses built by an LLM, plus a red-team adversarial set. It does not show that minimal exposure changes what a policy learns during RL, though the paper's claim is about online reward exploitation. The text I read contains no training run comparing exposure settings.
- Withholding the reference from the extractor is possible only because a deterministic verifier compares the extracted value with the target. On the fuzzy path the judge does receive the textual reference, so the restriction there is partial: the image is withheld but the answer key is not (my reading of the paper's design).
- One model family (Qwen3-VL-30B-A3B as the policy, a GenRM trained on the same rubric data) was audited.
- Withholding the image moves the visual reading upstream, it does not remove it. In V-Rubrics the rubric verifier receives the response and a criterion, not the image,[^c11] yet the criteria are written from the image beforehand, since the annotation protocol "converts the image, instruction, and reference response" into criteria.[^c10] The authors name the cost: "ambiguities or mistakes introduced when visual evidence is converted into criterion text can propagate directly into the reward."[^c9] The restriction protects the grader from copying, not the reward from an error made before grading; that second kind of error is outside what this note measures.

## Related

- [[verifiability-routed-criterion-reward]] — the routing that creates the two graders this restriction applies to.
- [[judge-master-key-false-positives]] — the opposite failure: a reference-based judge credits content-free responses when the reference is present; here the reference is kept from the extractor for that reason.
- [[deferred-answer-exposure]] — the same word, exposure, applied to the reasoner's own trajectory: when a candidate answer is revealed before reasoning, the reasoning rationalizes it.
- [[llm-judge-biases]] — other systematic judge errors that no input restriction is designed to remove.

[^c1]: doi-10-48550-arxiv-2605-30244 — "excluding the source image"
[^c2]: doi-10-48550-arxiv-2605-30244 — "the extractor might copy the required values from them instead of extracting them from the response"
[^c3]: doi-10-48550-arxiv-2605-30244 — "The judge might infer the task answer even when the response does not state it."
[^c4]: doi-10-48550-arxiv-2605-30244 — "both execution paths adopt text-only LLM and share the same parameters"
[^c5]: doi-10-48550-arxiv-2605-30244 — "exposure shows higher FPRs on no-final-answer responses (15.7% vs. 11.5%)"
[^c6]: doi-10-48550-arxiv-2605-30244 — "target values creates a shortcut for GenRM to copy or anchor on the reference answer instead of"
[^c7]: doi-10-48550-arxiv-2605-30244 — "We hypothesize that visual access makes the model more likely to infer"
[^c8]: doi-10-48550-arxiv-2605-30244 — "Although the absolute gaps are modest, they matter"
[^c9]: doi-10-48550-arxiv-2608-25580 — "into criterion text can propagate directly into the reward"
[^c10]: doi-10-48550-arxiv-2608-25580 — "converts the image, instruction, and reference response"
[^c11]: doi-10-48550-arxiv-2608-25580 — "the verifier receives a and rj , not the raw image"
