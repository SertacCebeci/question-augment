---
description: "LM judges prefer their own answer even when it is objectively worse; on QuALITY, stronger judges show more of this harmful self-preference, measured against ground-truth labels."
aliases: ["self-enhancement bias", "self-preference bias", "egotistical judging", "harmful self-preference"]
sources: ["arxiv-2512-05379"]
---
# Harmful self-preference

Self-preference is a language-model judge choosing its own answer over another model's answer when both are compared in a pairwise judgment. The work separates the harmless case, where the judge's answer is the better one, from the harmful case, where the competitor is objectively better. Harm can only be labelled where quality is objectively known, so the authors build their testbed on multiple-choice reading comprehension: QuALITY questions, "with human-annotated correct answers", answered by five instruction-tuned models that also serve as judges.[^c1][^c2] The paper's framing of the bias is that judges "prefer its own incorrect or unsafe answers over correct answers from other models", which is the case where the bias does damage.[^c3]

The protocol controls for two things before any label is assigned. Each pairwise comparison is run twice with the candidates swapped, and "a decision by the judge is only considered valid if it remains consistent across these two queries"; inconsistent decisions are ambiguous and dropped.[^c4] Pairs whose answers are of comparable quality are also removed, so that every remaining decision can be scored correct or incorrect against the ground truth.

The measured result is that capability does not remove the bias. Stronger judges are more accurate overall and in self-evaluation, but their accuracy falls further in the harmful cases, where their own answer is wrong. DeepSeek-V3 ends below the two Llama-4 models on those cases, which the authors read as a stronger tendency to stick to its own reasoning when it is wrong.[^c5] The paper states that "a tendency that occurs in the three larger models" and that, although these models are more accurate judges, "stronger models significantly overestimate their own accuracy" when asked to estimate their standing.[^c5][^c6]

This sits beside the general judge biases recorded in [[llm-judge-biases]], where self-enhancement appears as one entry among position and verbosity effects. What this paper adds is a measurement that uses correctness labels rather than agreement with a human ranking, so the self-favouring can be counted as harm. The mechanism the authors propose for it is that the judge can recognise its own output, covered in [[judge-self-recognition]]; what survives when surface style is neutralised is covered in [[shared-belief-self-preference]].

## Limits

- Five models, one dataset (the QuALITY validation set, 2,086 examples), and one multiple-choice format. Open-ended answers, where no single correct label exists, were not tested, and the harmful/harmless split is undefined there.[^c7]
- The judge's two roles are simulated by two different prompts. The paper notes that "the model receives different prompts in its two roles and does not behave exactly the same", so "self-evaluation" is not one fixed situation.[^c8]
- Every judge decision is made at temperature zero.[^c9] How the bias moves under sampling is not reported.
- The ordering of stronger and weaker judges rests on five models. The claim that more capable judges show more harmful self-preference is a comparison across this small set, not a trend fitted over model scale.
- The work measures the bias; it does not reduce it here. The mitigation experiments are a separate step, and their limits are in the linked notes.

## Related

- [[llm-judge-biases]] — the broad family of judge biases; self-enhancement is named there without a ground-truth measurement
- [[cross-generator-judge-bias-index]] — a measured spread of self-enhancement across generators, which cannot separate self-preference from general leniency
- [[author-cue-review-bias]] — an author-identity cue that moves a judge with correctness held fixed; harmful self-preference is defined only where correctness is labelled

[^c1]: arxiv-2512-05379 — "with human-annotated correct answers"
[^c2]: arxiv-2512-05379 — "We evaluate self-preference using five instruction-tuned"
[^c3]: arxiv-2512-05379 — "judge prefers its own incorrect or unsafe answers over correct answers from other models"
[^c4]: arxiv-2512-05379 — "A decision by the judge is only considered valid if it remains consistent across these two queries"
[^c5]: arxiv-2512-05379 — "a tendency that occurs in the three larger models"
[^c6]: arxiv-2512-05379 — "stronger models significantly overestimate their own accuracy"
[^c7]: arxiv-2512-05379 — "We use the validation set of"
[^c8]: arxiv-2512-05379 — "the model receives different prompts in its two roles and does not behave exactly the same"
[^c9]: arxiv-2512-05379 — "We set the temperature to zero for all judge decisions"
