---
description: "Stated confidence and a model's own answer-token probability can disagree; aligning the stated number to the internal one is a target separate from accuracy calibration."
aliases: ["confidence-probability alignment", "verbalized-internal confidence alignment", "verbalized vs internal confidence gap"]
sources: ["arxiv-2512-11998"]
---
# Verbalized–internal confidence alignment

A language model can express confidence in two places. The *internal*
confidence is the probability it gives the answer token: it is "quantified as
the probability of predicting a particular output token semantically linked to
an answer".[^a1] The work reads it as "the computed softmax probability of the
answer" letter in the output.[^a2] The *verbalized* confidence is the number the
model writes, "expression of its confidence level as a certainty percentage in
its output answer".[^a3] Alignment is how well these two numbers agree on the
same response. Kumar et al. (2024) introduced the measurement as a correlation
between verbalized certainty and "its internal confidence, quantified using
answer" token probabilities.[^a4]

The mechanism that makes this a separate object is the reference. Each response
gets a calibration error ε = Cv − Ci, the stated percentage minus the token
probability. The work defines it as "internal confidence Ci subtracted from its
verbalized confidence Cv for each response".[^a5] The reference is the model's
own internal number, not the truth. The authors "instead treat Ci as a reference
signal of" the model's internally expressed uncertainty.[^a6] Accuracy is not
in the comparison at all. So a response can be fully aligned and wrong, and a
model can score well on accuracy-based [[calibration]] and still be misaligned
between its two confidences. This is the wiki's reading of the design; the work
states that its method "is not focused on accuracy-based calibration".[^a6]

Alignment is measured on the distribution of ε, not on its average accuracy.
The work uses four numbers per model and dataset. Spearman's ρ between Cv and
Ci measures association. The authors note that "ρ only measures the strength of
a monotonic correlation and does not reference the" perfect line y = x.[^a7] The
other three are the standard deviation of ε, the mean absolute ε, and the
standard error of the mean ε. Because these use y = x as the zero point, they
"isolate the overall bias within the Cv of the models".[^a8]

The work's one intervention is a preference-trained objective (DPO, see
[[dpo-implicit-reward]]) that moves the stated number toward the internal one.
The effect was uneven across three open-weight instruct models on four QA sets.
Gemma-2-9B-Instruct "showed the strongest and most consistent improvements in
metrics after DCA".[^a9] Mistral-7B-Instruct showed "a large reduction in ρ from
0.20 to 0.06" on TruthfulQA.[^a10] The authors conclude that the method "is
ineffective for these models on certain tasks".[^a11] They suggest the result is
"more modeldependent than task-dependent".[^a12] What the work establishes is
that the target can be moved and that the movement depends on the model; it
does not establish a general recipe.

## Limits

- **The target needs logits.** The authors say the method "is limited to models
  with access to internal logits", and "This makes it inapplicable to"
  closed-source models.[^a13] The concept itself does not require this, but the
  measurement does.
- **The internal number is only a reference.** The work says the method "will be
  most useful if the internal" confidence "is better calibrated against accuracy
  than its verbalized confidence".[^a14] If the token probability is itself
  miscalibrated, alignment to it aligns to the wrong thing. The work does not
  test this condition.
- **Alignment can be bought at the top of the scale.** Gemma's confidence
  distributions "were already heavily" skewed to 90–100% before training. The
  authors write that the gains "may partially be due to a collapse towards high
  confidence values".[^a15] A small mean |ε| can therefore reflect a flat
  confidence scale, not two numbers that track each other.
- **Accuracy can fall.** The preference pairs include "some incorrect answer"
  choices, and Mistral's accuracy "demonstrated lower accuracies after" training.[^a16][^a17]
  A model aligned to its own uncertainty is not thereby more correct.
- **Scope of what was tested.** Three models, four datasets, one prompt template.
  The body text read contains no ablation that separates the training step from
  the choice of target. Whether the same movement would follow from prompting
  alone was not measured here; that is an open question, not a finding.

## Related

- [[calibration]] — accuracy-referenced calibration; this note's reference is the model's own token probability, so an ECE on accuracy does not measure it
- [[sequence-likelihood-confidence]] — a token-probability confidence measured for discrimination, which is the internal side of this comparison
- [[log-score-verbalized-confidence-reward]] — trains verbalized confidence against an outcome score, not against the internal probability
- [[reasoning-contamination-of-verbalized-confidence]] — a different source of verbal–internal mismatch: where in the generation the confidence is written

[^a1]: arxiv-2512-11998 — "quantified as the probability of predicting a particular output token semantically linked to an answer"
[^a2]: arxiv-2512-11998 — "the computed softmax probability of the answer"
[^a3]: arxiv-2512-11998 — "expression of its confidence level as a certainty percentage in its output answer"
[^a4]: arxiv-2512-11998 — "its internal confidence, quantified using answer"
[^a5]: arxiv-2512-11998 — "internal confidence Ci subtracted from its verbalized confidence Cv for each response"
[^a6]: arxiv-2512-11998 — "We instead treat Ci as a reference signal of"
[^a7]: arxiv-2512-11998 — "ρ only measures the strength of a monotonic correlation and does not reference the"
[^a8]: arxiv-2512-11998 — "overall bias within the Cv of the models"
[^a9]: arxiv-2512-11998 — "showed the strongest and most consistent improvements in metrics after DCA"
[^a10]: arxiv-2512-11998 — "a large reduction in ρ from 0.20 to 0.06"
[^a11]: arxiv-2512-11998 — "is ineffective for these models on certain tasks"
[^a12]: arxiv-2512-11998 — "the effectiveness of DCA may be more modeldependent than task-dependent"
[^a13]: arxiv-2512-11998 — "This makes it inapplicable to"
[^a14]: arxiv-2512-11998 — "will be most useful if the internal"
[^a15]: arxiv-2512-11998 — "alignment may partially be due to a collapse towards high confidence values"
[^a16]: arxiv-2512-11998 — "preference dataset include some incorrect answer"
[^a17]: arxiv-2512-11998 — "demonstrated lower accuracies after"
