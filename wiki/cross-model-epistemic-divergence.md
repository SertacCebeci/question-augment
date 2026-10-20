---
description: "Epistemic uncertainty as the gap between a model's cross-model response similarity and its own self-similarity; added to self-consistency it gives a total-uncertainty abstention signal."
aliases: ["epistemic uncertainty via inter-model response similarity", "EU", "total uncertainty", "TU", "Uepistemic"]
sources: ["arxiv-2604-17112"]
---
# Cross-model epistemic divergence

> Self-consistency measures whether a model agrees with **itself**; this
> measures whether it agrees with **other, comparably capable models** —
> and it is precisely where the first signal goes quiet that the second
> speaks.

## Definition / Mechanism

Hamidieh, Thost, Gerych, Yurochkin & Ghassemi (2026)
decompose an LLM's predictive uncertainty on a prompt into an aleatoric
term (AU, the usual self-consistency: expected dissimilarity between two
responses independently resampled from the *same* model — "degree-based
semantic dispersion," equivalent to [[semantic-entropy]]'s underlying
measure) and an epistemic term (EU) read off a small, scale-matched
**auxiliary ensemble** of other models: sample responses from the
reference model and from each auxiliary model, and take the gap between
the average *cross-model* similarity and the reference model's own
*self*-similarity. "When the average similarity in responses between ω
and other sampled models matches the self-similarity of ω's responses,
then... the epistemic uncertainty is low... [when there] is a
disagreement in how models respond... the epistemic uncertainty is
high."[^c2]

Total uncertainty is defined additively, $TU = AU + EU$, and
in practice EU is never estimated directly — it is the arithmetic
remainder $TU - AU$ once both are computed from the pooled response set.
The method needs only generated text (no logits, no hidden states), so
it runs against black-box API models as auxiliaries.

The paper's motivating case is a query a model answers the same wrong
way every time: self-consistency reads this as confident (AU near 0),
while other comparably capable models diverge from it, so EU is high
and $TU = AU+EU$ still flags the failure. "Two models confidently
produce distinct, incorrect answers to a factual question, which
results in low intra-model variability (AU) but high semantic
disagreement across models (EU)."[^c1]

Restricted to the lowest 5% of AU
scores — exactly the region self-consistency calls safest — incorrect
responses still carry significantly higher EU than correct ones.[^c3]

## Why it matters

Self-consistency is silent exactly where models are confidently and
collectively wrong; EU is a signal built from the same black-box access
(sampled text, no ground truth) that stays informative in that regime.
On selective-prediction evaluation across five 7–9B models and ten
long-form tasks, TU beats AU and EU alone on both accuracy at fixed
coverage and area under the risk–coverage curve: "total uncertainty
achieves higher selective accuracy and in all cases lower AURC compared
to aleatoric and EU alone... TU yields better abstention behavior than
AU or EU alone."[^c4]

An answerer that only tracks its own resampling
variance is blind to a failure mode a second opinion catches for free.

## Limits

- EU's discriminative power is dataset-dependent in a
  counter-intuitive direction: across tasks it correlates *positively*
  with how redundant the auxiliary models' correct answers are and
  *negatively* with how much they complement each other — "the opposite
  of the naive intuition that 'more disagreement ⇒ higher epistemic
  utility.'"[^c5]

  EU works best when there is one correct answer models
  phrase similarly and diverge only when wrong; on tasks with many
  distinct correct phrasings, or where the auxiliary ensemble shares
  training data or architecture with the reference model, disagreement
  stops tracking correctness.[^c6]
- Correctness itself is judged by another LLM (Llama-3-70B-Instruct);
  the reported AUROC and selective-risk numbers inherit that judge's
  errors.
- Cost scales with the auxiliary ensemble size (here $m=5$ models,
  2 samples each vs. 10 self-samples for AU alone at matched budget);
  the paper does not test whether a much smaller or larger auxiliary
  set changes the tradeoff qualitatively.

## Related

[[semantic-entropy]] · [[cross-model-answer-disagreement-entropy]] · [[heterogeneous-lora-ensemble-uncertainty]] · [[uncertainty-decomposition]] · [[calibration]]

[^c1]: arxiv-2604-17112
[^c2]: arxiv-2604-17112
[^c3]: arxiv-2604-17112
[^c4]: arxiv-2604-17112
[^c5]: arxiv-2604-17112
[^c6]: arxiv-2604-17112
