---
description: "Context can change how strongly choices respond to price and quality, a quantity separate from the choice-rate shift it causes; in 12 LLMs the two come apart."
aliases: ["attention reweighting", "context-induced feature reweighting", "marginal rate of substitution shift", "feature sensitivity shift"]
sources: ["doi-10-48550-arxiv-2609-22225"]
---
# Feature-sensitivity reweighting

A choice between a standard and a premium product can move in two ways. The choice rate can shift, or the weight the decision-maker puts on each feature can shift. The two are different quantities. In the paper's valuation, the premium product is chosen when the quality gain, weighted by attention, outweighs the price increase: "The DM chooses the jam with the higher valuation".[^c1] The attention weights are "context-dependent", so a change in context changes the ratio of quality weight to price weight. Under a hedonic category that ratio rises. The marginal rate of substitution, the extra price a buyer accepts for a quality gain, goes up: "Context induces asymmetric feature sensitivity: Hedonic context raises the marginal".[^c2]

This is the second half of the cognitive account in [[problem-categorization-context-effect]]. There the category sets the weights. Here the weights are the object of measurement, and they are not read off the choice rate.

## How it is measured

The paper fits, for each model and each sweep, a logit regression of premium-versus-standard choice on the log feature ratio, with a hedonic indicator and an interaction term. The key coefficient is the interaction: the change in sensitivity to the feature ratio between hedonic and functional cues. The regression is set up so that the coefficient "maps the marginal rate of substitution" onto a regression coefficient.[^c3] Two sweeps supply the variation: a price sweep of "generating 88,000 problems" and a quality sweep of 44,000 more.[^c4] The human prediction is a positive interaction in both sweeps: "Human evidence and theory predict" that hedonic cues attenuate price sensitivity and amplify quality sensitivity.[^c5]

## What the LLMs do

The choice-rate effect is present everywhere. Hedonic cues raise premium choice in every model, "hedonic cues than functional cues, consistent with" the human effect.[^c6] The weight effect is not. "they do not reweight feature sensitivities similarly", and "Only 26% of model-cue combinations are less price sensitive and more quality".[^c7] A further 62% show the human pattern in one feature but not the other, and 12% show the opposite.[^c8] Heterogeneity is large: "the purchase trigger cues least (0/10 models)" show the human-like pattern in none of the models.[^c9]

Two results cut the other way. Aggregated by cue type, "reasoning frame cues induce significant humanlike sensitivities", but aggregated by model across cues, only four of ten models show the pattern.[^c10] Reasoning helps in one place: the reasoning frame cue "induces human-like sensitivity effects" in Qwen models only in thinking mode, with "sensitivity effects in all four Qwen models only" under that cue.[^c11] The paper calls this fragile.

The sensitivities are not noise. Every LLM has a negative price sensitivity and a positive quality sensitivity under both cues, "positive quality sensitivity under both hedonic and" functional, and the models "respond consistently to feature variation".[^c12] So the failure is in how the weights move with context, not in whether the models respond to price and quality at all.

## Limits

- The weights are implied, not observed. The paper says: "is tenuous, so we estimate LLM attention via regression as implied weights on problem features".[^c13] "Attention" here means the model behaves as if a feature matters more. Nothing in the note shows the model has an attention mechanism of this kind.
- A failed reweighting is not proof of a different mechanism. The paper reads divergence as evidence that LLM and human decision mechanisms are distinct, and it says "Behavioral similarity does not imply mechanistic correspondence".[^c14] My reading is narrower: a fitted interaction that is near zero shows that the regression finds no reweighting. It does not show that no reweighting occurs inside the model, since the regression can miss weights that are not linear in the log ratio. The paper's robustness check uses differences in feature values instead of ratios, and "robust to different regression specifications" is the paper's claim.[^c15]
- Commercial frontier models are outside this analysis. GPT and Gemini are run with default reasoning and "and logits are unavailable, are run with medium" is the stated reason, so the feature result rests on the open models only.[^c16]
- One setting only: "We test one canonical economic setting: binary choice between" two products.[^c17] Risk, intertemporal and social choice, where the theory also applies, are untested.
- The paper leaves the proper measurement of LLM attention open: "We leave the proper measurement" of it "for future work".[^c18]

## Related

- [[problem-categorization-context-effect]] — the mechanism that is supposed to set the weights; its signatures hold on choice rates while this note's weight shift fails.
- [[bounded-rationality]] — bounded-attention accounts would predict that more capable models reduce this kind of context sensitivity; the paper finds scale and reasoning do not reliably do so.
- [[anchor-salience-bias]] — another case where surface presentation redirects a model's focus; there the target is which document span a generator asks about, not the weight on a decision feature.

[^c1]: doi-10-48550-arxiv-2609-22225 — "The DM chooses the jam with the higher valuation"
[^c2]: doi-10-48550-arxiv-2609-22225 — "Context induces asymmetric feature sensitivity: Hedonic context raises the marginal"
[^c3]: doi-10-48550-arxiv-2609-22225 — "a form that maps the marginal rate of substitution"
[^c4]: doi-10-48550-arxiv-2609-22225 — "generating 88,000 problems"
[^c5]: doi-10-48550-arxiv-2609-22225 — "Human evidence and theory predict"
[^c6]: doi-10-48550-arxiv-2609-22225 — "hedonic cues than functional cues, consistent with"
[^c7]: doi-10-48550-arxiv-2609-22225 — "they do not reweight feature sensitivities similarly"
[^c8]: doi-10-48550-arxiv-2609-22225 — "The remaining 62% of model-cue"
[^c9]: doi-10-48550-arxiv-2609-22225 — "the purchase trigger cues least (0/10 models)"
[^c10]: doi-10-48550-arxiv-2609-22225 — "reasoning frame cues induce significant humanlike sensitivities, while only four out of ten models"
[^c11]: doi-10-48550-arxiv-2609-22225 — "sensitivity effects in all four Qwen models only"
[^c12]: doi-10-48550-arxiv-2609-22225 — "respond consistently to feature variation"
[^c13]: doi-10-48550-arxiv-2609-22225 — "is tenuous, so we estimate LLM attention via regression as implied weights on problem features"
[^c14]: doi-10-48550-arxiv-2609-22225 — "Behavioral similarity does not imply mechanistic correspondence"
[^c15]: doi-10-48550-arxiv-2609-22225 — "robust to different regression specifications"
[^c16]: doi-10-48550-arxiv-2609-22225 — "and logits are unavailable, are run with medium"
[^c17]: doi-10-48550-arxiv-2609-22225 — "We test one canonical economic setting: binary choice between"
[^c18]: doi-10-48550-arxiv-2609-22225 — "We leave the proper measurement"
