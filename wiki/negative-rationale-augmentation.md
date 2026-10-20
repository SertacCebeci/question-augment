---
description: "Training data gains explanations of why each wrong option is wrong, written with the gold answer visible and used later with it hidden, so the model learns to reject distractors."
aliases: ["negative rationalization", "negative rationales", "discriminative rationale augmentation"]
sources: ["arxiv-2512-02456"]
---
# Negative-rationale augmentation

A positive rationale says why the right answer is right. A negative rationale says why a particular wrong option is wrong. The paper's argument is that positives alone teach too little: "Relying only on rationales from correct answers provides limited supervision", since the model sees only the reasoning paths that succeeded.[^c1] The gap matters most where telling correct reasoning from incorrect reasoning is the task itself.

The mechanism works on items the model already answers correctly. The authors treat a correct answer as evidence of understanding: "We assume that a correct prediction means that the model has a good understanding of the image and the question."[^c2] For each such item, the model is prompted with the image, the question, the correct answer and one incorrect option. It first describes the image, then explains why that option is not valid. The correct answer is in the prompt "to guide accurate reasoning".[^c3] Each explanation is stored as a tuple attached to the item and that wrong option.

At training time the situation is reversed. "Later, when used for training, the gold answer is withheld from the prompt, forcing the model to reason independently" about the distractors.[^c4] The training input is the image, question, choices and one wrong option; the target is the negative explanation. The model is thus trained to say why a given option fails without being told which option is right.

The authors report that the component adds to the gain: "incorporating negative rationalization augmentation yields an additional performance gain, as the model learns to better discriminate between correct and incorrect answers."[^c5] In a qualitative subjective analysis they go further and attribute the improvement to the negatives rather than to longer outputs: the improvement "stem not from longer rationales but from the complementary effect of negative rationales". That reading is theirs, drawn from 150 rationales per domain, and it is not a measured mechanism.[^c6]

A point the paper does not discuss, and that I raise as my own reading: the explanations are generated with the answer visible, which is the same visibility problem the paper names for the baseline's rationalization step. The defence in the method is that the answer is hidden when the explanation is used for training, and the negative example is about a distractor only. Whether that removes the shortcut, rather than moving it, is not tested here.

## Limits

- Negatives are produced only for items answered correctly. The distractors the model learns to reject are therefore ones it already handles on that item. Harder distractors, where the model is wrong, get no explanation under this scheme.
- The gain is reported on two splits, Language Science and Commonsense. The Natural Science split is where the baseline beat the method, so the effect is not shown on every domain.
- The "suppress spurious tokens" account rests on a qualitative reading of a small sample. No token-level or attention measurement is reported in the text I read.
- The method needs a multiple-choice set in which the wrong options are known. It does not transfer to open answers without a candidate list.
- The cost grows with the number of options: each correct item yields one explanation per wrong option, so the training set scales with choice-set size.

## Related

- [[distractor-strength-reward-signal]] — how attractive wrong options decide whether a reward trains reasoning or guessing; negative rationales target the same options, on the training side
- [[rationale-aware-reward]] — rewarding a model for quoting the helpful passage in noisy context, which also cuts distractor-driven reasoning, by a reward rather than by explanation data
- [[deferred-answer-exposure]] — the same visibility risk: an answer shown while the rationale is written can be rationalized; here the answer is hidden at training time
- [[perception-first-rationale-template]] — the template whose structured rationales this augmentation sits beside in the same training set

[^c1]: arxiv-2512-02456 — "Relying only on rationales from correct answers provides limited supervision"
[^c2]: arxiv-2512-02456 — "We assume that a correct prediction means that the model has a good understanding of the image and the question"
[^c3]: arxiv-2512-02456 — "included in the prompt to guide accurate reasoning"
[^c4]: arxiv-2512-02456 — "Later, when used for training, the gold answer is withheld"
[^c5]: arxiv-2512-02456 — "incorporating negative rationalization augmentation yields an additional performance gain"
[^c6]: arxiv-2512-02456 — "stem not from longer rationales but from the complementary"
