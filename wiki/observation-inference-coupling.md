---
description: "A claim pairs a figure observation with a domain inference; models should flip their verdict when either part is perturbed, and they flip too rarely, least when both parts change."
aliases: ["epistemic sensitivity", "observation-inference pairs", "epistemic mismatch"]
sources: ["doi-10-48550-arxiv-2506-04585"]
---
# Observation-inference coupling

A scientific claim often has two parts. The observation is what the figure shows, something that can be checked by looking at a panel. The inference is what the authors conclude from it, and reading it needs domain knowledge. The MuSciClaims paper builds its claims on this split: they encode "observations from the figure and related inferences made with domain knowledge."[^o1] For each perturbation, the annotators marked whether it changed the observation, the inference, or both.[^o2]

That split makes a pair test possible. Take an original claim the figure supports and its perturbed version, which the figure contradicts. A model that reads both parts should give different verdicts: "they should predict support for the original and contradict for the perturbed claim."[^o3] The paper's measure is the share of such pairs on which the verdict changes: "We calculate sensitivity as the percentage of times models change predictions across the supported and refuted version of the same claim."[^o4] The perturbed claims come from the [[counterfactual-hard-negative]] construction, one targeted edit away from a true claim, so a flip is the expected behaviour and no flip is the error.

The measured result is that sensitivity is low: "Models are not sensitive enough to understand nuances in epistemic relationships," and they are worst "when both the observation and inference is modified."[^o5] The verdict follows less of the claim's internal structure than its wording. A model can notice that a claim is wrong without knowing which link broke. A test that changes only the inference, or only the observation, shows which link the model tracks. The same design logic appears in [[crossed-image-text-edit-families]], where a minimal edit to the image and one to the question are crossed, so that each cell has a fixed gold label and shows whether the answer follows the evidence or the wording.

## Limits

- The sensitivity measure counts changes of verdict. A model that flips on every input would score as sensitive, so the change rate alone does not show that the flips are correct. The expected behaviour (support for one member, contradiction for the other) is stated in the paper, but the reported number is the change rate. This is my reading.
- The pair test is run in the diagnostics on four models, on the biology subset: "We use our diagnostic tests to better understand the failure modes of 4o-mini, 4o, Sonnet and InternVL3."[^o6] Other models and other domains were not run through this test.
- The observation and inference labels come from the annotators' marking during perturbation. The text I read reports agreement only for whether a perturbation contradicts the supported claim: "all perturbed claims are indeed contradictions of the corresponding supported claims."[^o7] No agreement figure is given for the observation-or-inference label itself.
- The paper suggests that an analysis of model confidence "may provide more insight"[^o8] than the verdict alone, and does not run that analysis. The mechanism of the low sensitivity is therefore not isolated.

## Related

- [[counterfactual-hard-negative]] — the single-error contrast from which the perturbed claims are built.
- [[crossed-image-text-edit-families]] — the same two-variant design on image and question, where the gold label of each cell is fixed.
- [[detection-correction-gap]] — a model that detects a defect and still endorses the claim; a related split between noticing a flaw and acting on it.
- [[epistemic-leakage]] — "epistemic" here names the observation-inference link in a claim, not model uncertainty; the word is shared, the quantity is not.

[^o1]: doi-10-48550-arxiv-2506-04585 — "observations from the figure and related inferences made with domain knowledge"
[^o2]: doi-10-48550-arxiv-2506-04585 — "We collect annotations about whether it is the observation, the inference, or both, that are perturbed"
[^o3]: doi-10-48550-arxiv-2506-04585 — "they should predict support for the original and contradict for the perturbed claim"
[^o4]: doi-10-48550-arxiv-2506-04585 — "We calculate sensitivity as the percentage of times models change predictions across the supported and refuted version of the same claim"
[^o5]: doi-10-48550-arxiv-2506-04585 — "being the worst when both the observation and inference is modified"
[^o6]: doi-10-48550-arxiv-2506-04585 — "We use our diagnostic tests to better understand the failure modes of 4o-mini, 4o, Sonnet and InternVL3"
[^o7]: doi-10-48550-arxiv-2506-04585 — "all perturbed claims are indeed contradictions of the corresponding supported claims"
[^o8]: doi-10-48550-arxiv-2506-04585 — "may provide more insight"
