---
description: "Steering a confidence-linked direction in a reasoning model's activations cut its reflection and backtracking steps several-fold, at a small accuracy cost the paper calls not significant."
aliases: ["confidence reasoning vector", "entropy-linked reflection", "reflection and backtracking as confidence-linked behaviour"]
sources: ["arxiv-2512-23988", "arxiv-2512-13979"]
---
# Reflection–confidence coupling

A reasoning trace contains moves a reader can count. **Reflection** re-examines earlier steps. **Backtracking** abandons the current path for another one. The mechanism the paper reports is that both can be reduced by editing one activation direction, and that the direction chosen to lower the model's entropy also lowers them. The edit is applied at inference, not in training: "During inference, this vector is injected into the hidden representation of the last token at each reasoning step."[^c1]

The confidence direction is found by optimisation rather than labels. The paper adopts "as our proxy objective and seek to identify decoder columns that are closely associated with entropy."[^c2] Its score vector is tuned to minimise the entropy of the next-token distribution over activations from the MATH500 training set, and the top-scoring columns form the vector. On AIME 2025 with DeepSeek-R1-1.5B, the intervention moved the counts: reflection steps "from 90.53 to 33.77, and backtracking steps decrease from 35.50 to 5.93."[^c3] Accuracy went from 23.33% to 20.00%. The paper says "this corresponds to only a single question out of 30," and that the drop "is therefore not statistically significant."[^c4][^c5]

The coupling is also geometric. The confidence columns "partially overlap with the reflection and backtracking regions identified in Figure 2" in the SAE decoder space.[^c6] The paper reads this as a hypothesis, not a result: "backtracking behaviors may contribute to higher entropy."[^c7] For the reflection vector itself, scaling the intervention strength moved the count of reflection steps on AIME25 across α from −1.5 to 1.5 as {58.6, 73.6, 90.5, 131.0, 166.9}, with the counts "consistently evolving in accordance with the intervention strength."[^c8]

What this adds for asking and answering: the re-checking an answerer does is not only a verdict on its final answer. It is a countable behaviour that moves with a confidence-like signal in the activations. Whether a model should keep revisiting a committed answer is then partly a question about how often that behaviour occurs, and the paper shows the frequency can be shifted. (My inference, not the paper's: the paper does not show that a shift in frequency changes which answers are correct.)

A second paper reaches the coupling from the correctness side, with a different direction. Its reflection direction is a labelled difference of means between reflection and non-reflection steps, and a logistic classifier on its projections predicts whether the answer is right. The paper reports that "Reflection-based features achieve higher AUROC and F1 scores despite lower dimensionality" than the final-layer embedding.[^c12] Per-token entropy before a reflection step is higher than before a non-reflection step: "steps immediately preceding reflection exhibit significantly higher entropy."[^c13] The same paper reads reflection as partly redundant: "Reflections are largely redundant in stronger models," with suppression at one setting cutting QwQ-32B's tokens "by 32.4% on GSM8k and 20.9% on MATH-500" at small accuracy cost.[^c14][^c15] Here the direction is tested against correctness, which the entropy-optimised vector above is not. The two directions are not shown to be the same object. (My inference.)

## Limits

- The accuracy evidence is thin. The 23.33% to 20.00% change is one question out of 30, which the paper itself calls not significant.[^c5] The worked example in its Figure 6 is one problem, and the paper notes that the answer is the same across conditions: "consistently produces the same final answer."[^c9]
- Entropy is a proxy. The vector is optimised for low next-token entropy, not for correctness. Low entropy is not shown here to mean a right answer. (My inference: the paper's own citations on entropy-based filtering suggest the link is plausible but it is not tested in this work.)
- The labels are a judge's. Reflection and backtracking were assigned by "The classification is performed using an LLM-as-a-judge approach."[^c10] The agreement analysis is in an appendix I did not read.
- Direction is untested. The paper shows that removing the confidence direction removes reflection. It does not show that reflection raises entropy; "may contribute" is the authors' hedge.
- Scale. The step-count evidence is one model, DeepSeek-R1-1.5B. The Qwen3-8B extension is reported only in a figure whose values were not in the text I read.
- The paper's stronger claim is a test-time method that combines three confidence vectors and "improves reasoning accuracy by up to 4.66 points while achieving a 13.69% reduction in token usage."[^c11] That is the authors' own procedure, with no variance reported in the text I read, and it is not established here.
- The correctness probe is a GSM8k result. The classifier is trained "on the GSM8k training set" and evaluated on the GSM8k test set, with three models and a single feature construction.[^c16] The table's layout in the text I read is hard to align to models, so the per-model AUROC values are not quoted here. Whether the probe transfers to other tasks is untested.

## Related

- [[sae-reasoning-behavior-vectors]] — how the reflection, backtracking and confidence directions are found as decoder columns, without labels
- [[cognitive-heads]] — the same behaviours (backtracking, verification) located in attention heads and labelled by keyword rather than a judge
- [[entropy]] — the proxy the confidence direction is optimised for
- [[sae-uncertainty-correctness-dissociation]] — SAE features for uncertainty and for incorrectness are separable; this paper does not test its confidence direction against correctness
- [[abstention]] — the stop-or-withhold decision that a confidence signal would feed
- [[step-boundary-steering]] — the same kind of reflection direction, applied only at step starts rather than every token

[^c1]: arxiv-2512-23988 — "During inference, this vector is injected into the hidden representation of the last token at each reasoning step"
[^c2]: arxiv-2512-23988 — "as our proxy objective and seek to identify decoder columns that are closely associated with entropy"
[^c3]: arxiv-2512-23988 — "from 90.53 to 33.77, and backtracking steps decrease from 35.50 to 5.93."
[^c4]: arxiv-2512-23988 — "this corresponds to only a single question out of 30"
[^c5]: arxiv-2512-23988 — "is therefore not statistically significant"
[^c6]: arxiv-2512-23988 — "these columns partially overlap with the reflection and backtracking regions identified in Figure 2"
[^c7]: arxiv-2512-23988 — "backtracking behaviors may contribute to higher entropy"
[^c8]: arxiv-2512-23988 — "consistently evolving in accordance with the intervention strength"
[^c9]: arxiv-2512-23988 — "consistently produces the same final answer"
[^c10]: arxiv-2512-23988 — "The classification is performed using an LLM-as-a-judge approach"
[^c11]: arxiv-2512-23988 — "improves reasoning accuracy by up to 4.66 points while achieving a 13.69% reduction in token usage"
[^c12]: arxiv-2512-13979 — "Reflection-based features achieve higher AUROC and F1 scores despite lower dimensionality"
[^c13]: arxiv-2512-13979 — "steps immediately preceding reflection exhibit significantly higher entropy"
[^c14]: arxiv-2512-13979 — "Reflections are largely redundant in stronger models"
[^c15]: arxiv-2512-13979 — "reduces token usage by 32.4% on GSM8k and 20.9% on MATH-500"
[^c16]: arxiv-2512-13979 — "train the classifier on the GSM8k training set"
