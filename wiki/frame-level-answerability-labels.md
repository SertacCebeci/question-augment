---
description: "Re-sampling one video at several frame budgets and labelling each clip answerable or not makes guessing detectable, because only a refusal scores on the unanswerable clips."
aliases: ["multi-level frame sampling ground truth", "VirtueBench answerability labels", "evidence-sufficiency labelling by input budget"]
sources: ["arxiv-2603-07071"]
---
# Frame-level answerability labels

Standard long-video benchmarks score an answer right or wrong against the full video, but a model sees only a sampled subset of frames. When the key frame is missing, a model that guesses can be right by luck and a model that says so is marked wrong; the VirtueBench authors state that guessers "may coincidentally produce the correct answer" and so look better than honest models.[^c1]

## Mechanism

VirtueBench keeps one question and one source video, and cuts several clips at different frame budgets (64 to 1024 frames). Annotators then answer from each clip alone. If the clip lacks the evidence, the gold answer is the fixed string "The video does not provide enough information." Annotators also give timestamps for the evidence behind each answer, and two annotators review every instance.[^c2]

Scoring follows the label. On an answerable clip the answer must match the reference. On an unanswerable clip, a judge model first checks whether the response is a refusal, and the answer counts as correct only if "refusal is detected in the previous step."[^c3] The same question is therefore right to answer at one budget and right to refuse at another, so a model cannot do well by always answering or by always refusing.

The share of unanswerable clips falls as the budget rises, "clear decreasing trend as the number of frames increases", and the number of unanswerable levels per instance (0 to 5) is roughly evenly spread.[^c4] The benchmark thus covers three situations: never answerable, answerable only at higher budgets, and always answerable.[^c5] Reported per-level unanswerable rates run from 38.4% at 64 frames to 14.8% at 1024 frames (read from the figure text; the chart labels are my reading of the extract).

## What it measures

Accuracy is split into a refusal subset and a non-refusal subset, so abstention skill and answering skill are reported separately. Across 25 models the headline is wide variation in refusal accuracy, over 70% for the best and nearly 0% for the worst.[^c6]

## Limits

- The label depends on human annotators judging what a clip shows; "answerable" is a human judgement, not a property verified against model behaviour.
- Scoring uses a GPT-4o judge for both refusal detection and correctness, and the work does not report judge error rates in the slices I read.
- The design assumes the missing evidence is the only cause of unanswerability; it does not cover false-premise or ambiguous questions, which were discarded.
- Evaluation prompts tell the model to refuse; see [[instruction-gated-refusal]] for how much that matters.
- Built on questions drawn from existing video benchmarks, so the findings are about video QA with open-ended answers only.

## Related

- [[abstention-informedness]] — scores abstention as a classifier of eventual error; here the gold label is built into the input budget instead of derived from a forced guess
- [[instruction-gated-refusal]] — what the same benchmark shows when the honesty instruction is removed
- [[calibrated-accuracy]] — another correction for lucky guesses in accuracy
- [[adversarial-unanswerable-questions]] — unanswerability created by editing the question, not by shrinking the evidence

[^c1]: arxiv-2603-07071 — "while those that guess may coincidentally produce the correct answer and"
[^c2]: arxiv-2603-07071 — "they are required to specify timestamps corresponding"
[^c3]: arxiv-2603-07071 — "refusal is detected in the previous step."
[^c4]: arxiv-2603-07071 — "clear decreasing trend as the number of frames increases"
[^c5]: arxiv-2603-07071 — "only at higher frame levels"
[^c6]: arxiv-2603-07071 — "different model families, with refusal accuracy ranging from"
