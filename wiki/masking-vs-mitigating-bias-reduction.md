---
description: "An aggregate bias-reduction score can fall for two reasons — genuine decorrelation from the confound, or added noise that masks it — and the two predict opposite generalization."
aliases: ["variance-based vs decorrelation-based bias reduction", "masking versus mitigating bias"]
sources: ["arxiv-2604-06097"]
---
# Masking or mitigating a bias

> A lower aggregate bias score can mean the confound stopped mattering, or
> only that the scores got noisier. The two look identical on the aggregate
> metric and opposite on everything downstream.

## Definition / Mechanism

Take an intervention meant to reduce a measured bias — here, query
rewriting applied before dense retrieval, against four surface biases
(brevity, literal overlap, position, repetition) scored by a paired
|t|-statistic between bias-amplified and control documents. The
|t|-statistic falls when the mean score gap narrows **or** when its
variance grows; the two are conflated in one number. Goyal, Mukherjee, Saxena, Phukan, Chandrasekharan & Sundaram (2026)
separate them by also computing the Spearman correlation ρ between
retrieval score and the raw bias-inducing feature (document length,
query–document term overlap, answer position, query-term frequency) before
and after the intervention. Reducing overall bias, measured by the
|t|-statistic, does not imply reducing sensitivity to the bias-inducing
feature. Simple LLM rewriting cuts the |t|-statistic the most (8.72 to
4.02) while *raising* |ρ| for position and repetition — "the mechanism
appears to be increased retrieval score variance—noisier scores reduce the
statistical power to detect systematic preferences, lowering
|t|-statistics without addressing underlying bias sensitivity."[^c2]
Pseudo-document methods (HyDE, Query2Doc) with continual pretraining
instead lower |ρ| across several features at once — "bias reduction
through principled decorrelation from bias-inducing features."[^c3]

## Why it matters

The two mechanisms make opposite predictions once biases stop acting
alone. On an adversarial subset where several bias features are combined
in one document pair, the variance-reducing method (simple rewriting)
"provides minimal improvement on FOIL despite achieving the largest
reduction in individual bias metrics," while the decorrelating methods
gain 9–13× over baseline. An aggregate score computed on isolated
confounds cannot certify robustness to their combination; only the
correlation test can, because it is checking the mechanism the aggregate
score is silent about. The same split applies to any setting where an
intervention is judged by a single average effect on a known confound —
a rewritten question, a debiased prompt, a fairness-audited classifier —
whenever that confound can co-occur with others in the field.

## Limits

Demonstrated on one benchmark (ColDeR, built from Re-DocRED) and four
predefined bias features; the paper does not claim the variance/
decorrelation split is exhaustive of how an aggregate metric can be
gamed, only that it is the split observed here. The correlation test
itself assumes the bias feature is known and measurable — it cannot
detect decorrelation from an unnamed confound. Whether variance-based
reduction ever helps downstream (generation-stage) quality despite
failing the adversarial retrieval test is not evaluated.

## Related

- [[format-restriction-effect]]
- [[retrieval-order-sensitivity]]
- [[reformulation-pattern-library]]
- [[mcq-answer-position-bias]]

[^c2]: arxiv-2604-06097 — "The mechanism appears to be increased retrieval score variance—noisier scores reduce the statistical power to detect systematic preferences, lowering |t|-statistics without addressing underlying bias sensitivity."
[^c3]: arxiv-2604-06097 — "Pseudodocument methods, particularly the CPT variants, achieve bias reduction through principled decorrelation from bias-inducing features."
