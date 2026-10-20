---
description: "Disagreement on whether a prompt is harmful is mostly prompt-driven and peaks at mid-to-high harm, with a small systematic annotator-trait share; personalized prediction beats aggregate alignment."
aliases: ["pluralistic harm judgment", "harm-rating disagreement as signal", "trait-prompt interaction in harm ratings"]
sources: ["arxiv-2601-08951", "doi-10-48550-arxiv-2609-06646"]
---
# Structured annotator disagreement on harm

Judging how harmful a request is has no single answer for many prompts. PluriHarms had 100 Prolific annotators each rate all 150 prompts on a 0-100 scale, and recorded demographic and psychological traits for every annotator.[^c1] The prompts were generated at controlled synthetic harm levels (0.0 to 1.0). Those levels correlated with mean human rating (Spearman r = 0.59), and "intermediate-to-high harm levels are associated with higher human response variance and entropy".[^c2] Disagreement is therefore not spread evenly. It concentrates where a request is neither plainly benign nor plainly severe.

## Where the variance sits

Three mixed-effects regressions, with lasso selection, separate the sources.

- Prompt features dominate. A model of 42 retained features reached R2 = 0.273.[^c3] Positive predictors were direct, imminent dangers (child harm, self harm, criminal activity). Negative ones were indirect, non-physical or institutional domains (psychological harm, social harm).[^c4]
- Annotator traits alone explain little. Ten of 13 trait features were significant but gave R2 = 0.0232. The authors say this is limited "by design because most variation arises at the prompt level".[^c5] The strongest positive predictors were online toxicity experience and social media frequency. Education, gender and political affiliation were negative.[^c6]
- Trait interactions add more. A model with trait interactions reached R2 = 0.0686. Education amplified the effect of prosocial orientation, and political differences grew with toxicity experience.[^c7]

Model comparison by BIC improved most when prompt features were added. It improved further when traits and their interactions were added.[^c8] The authors read this as disagreement arising "from trait-prompt interactions rather than traits or prompts in isolation", which is the claim they set out to test in RQ3. They state that disagreement "is not simply noise".[^c9]

## What this does to prediction

On a 100-prompt alignment set and a 50-prompt test set, aligning models to aggregated ratings gave little benefit over zero-shot. Personalized alignment to individual annotators consistently beat aggregated methods, and personalized k-shot steering was strongest.[^c10] Treating safety as a probability rather than a binary label also helped.[^c11] For an answerer, the consequence is that a single consensus harm label discards information that recurs by annotator type.

## Same structure in temporal boundaries

A second instance comes from laughter localization, where the item is an interval and the answer is an onset and an offset. The authors state the finding as: "We show that this disagreement is structured rather than random noise."[^c12] Two patterns hold. Offsets spread more than onsets: "Offsets are markedly noisier" than onsets, and the authors trace this to the acoustic envelope, since a "sharp attack but gradual decay makes the endpoint acoustically the less determined boundary".[^c13][^c14] Intensity matters as well: "a chuckle is disagreed about 77% of the time versus only" 20% for full laughs.[^c15] The disagreement is also "predictable from event attributes (AUC 0.831)".[^c16]

The pattern resembles the harm result above, in that spread is largest for the less clear items. The mechanism differs: the laughter paper finds an acoustic cause, while the harm paper finds prompt and trait interactions. Whether the two share a cause is not tested. (my inference) For what this means when such labels are used as a reference, see single-reference-evaluation and [[human-spread-tolerance-band]]. This partly addresses the Limits bullet below for a non-rating item; it does not settle it.

## Limits

- The ratings come from one annotator pool, recruited on one platform, over 150 synthetic, DeepSeek-generated prompts. Generalization to real user queries was not tested here.
- Trait effects are small in variance terms (R2 of 0.02 to 0.07), and the traits are correlated with each other. Trait-to-rating links are associations, not causes.
- Harm levels were assigned by a generator, and human ratings track them only moderately (r = 0.59). "Disagreement peaks mid-range" is a descriptive pattern from this set.
- My inference, not the paper's: a model that tracks annotator type could also be used to tailor answers to a group's stereotype. The paper does not examine that risk.
- This note covers harm judgments. Whether disagreement on other question types has the same structure was not tested.

## Related

- [[rater-effects-latent-score-model]] — treats rater differences as latent parameters to correct for. PluriHarms instead treats them as signal to predict.
- [[cross-model-answer-disagreement-entropy]] — disagreement entropy among models, as against among human raters.
- [[qa-benchmark-demographic-skew]] — who the annotators are shapes what a benchmark measures.
- single-reference-evaluation — what scoring against one annotator does when the labels are a spread; the boundary case of this note's point about a single consensus label.
- [[human-spread-tolerance-band]] — a tolerance calibrated from the same kind of rater spread, for boundaries rather than ratings.

[^c1]: arxiv-2601-08951 — "We collected human annotations from 100 participants recruited on Prolific"
[^c2]: arxiv-2601-08951 — "intermediate-to-high harm levels are associated"
[^c3]: arxiv-2601-08951 — "The final model explained R2 = 0.273 of the variance from fixed effects, retaining"
[^c4]: arxiv-2601-08951 — "direct, imminent dangers (e.g., Child Harm, Self Harm, Criminal Activities)"
[^c5]: arxiv-2601-08951 — "most variation arises at the prompt level rather than"
[^c6]: arxiv-2601-08951 — "the strongest positive predictors were Online Toxicity"
[^c7]: arxiv-2601-08951 — "education amplified the influence of prosocial orientations (Factor 2)"
[^c8]: arxiv-2601-08951 — "The largest gain in fit came from adding prompt-level features"
[^c9]: arxiv-2601-08951 — "is not simply “noise,” but emerges from structured interactions between who the annotators are and"
[^c10]: arxiv-2601-08951 — "personalized alignment"
[^c11]: arxiv-2601-08951 — "treating prompt safety as a probabilistic variable rather than binary improves performance"
[^c12]: doi-10-48550-arxiv-2609-06646 — "We show that this disagreement is structured rather than random noise."
[^c13]: doi-10-48550-arxiv-2609-06646 — "Offsets are markedly noisier"
[^c14]: doi-10-48550-arxiv-2609-06646 — "sharp attack but gradual decay makes the endpoint acoustically the less determined boundary"
[^c15]: doi-10-48550-arxiv-2609-06646 — "a chuckle is disagreed about 77% of the time versus only"
[^c16]: doi-10-48550-arxiv-2609-06646 — "predictable from event attributes (AUC 0.831)"
