---
description: "Bias is a relation of model, context and standpoint: a per-dimension profile of how much a score moves under context cues, not one score, is what separates models that tie on average."
aliases: ["CSF", "context sensitivity fingerprint", "contextual StereoSet"]
sources: ["arxiv-2601-10460"]
---
# Context Sensitivity Fingerprint

A single benchmark score answers "is this model biased?", a question the work treats as underspecified: bias is a relation of "model × context × standpoint".[^c1] The fingerprint replaces the scalar with a profile. Items (StereoSet sentences with stereotype, anti-stereotype and unrelated options) are held fixed while a factorial grid of framing cues is varied: location, year, style (for example gossip versus direct), and implied observer (similar versus dissimilar). For each model the profile reports the stereotype-selection rate, the per-item standard deviation of that rate across levels of each dimension (dispersion), and paired contrasts such as gossip minus direct, averaged over items.[^c2]

Because each contrast is computed within an item, item-level noise is constant and only the effect of the cue remains. The full grid is 360 contexts by 50 items; a budgeted protocol covers the full 4,229-item StereoSet with 72 contexts.[^c3]

## What was measured

Across 13 models, every model tested showed context-dependent bias.[^c4] Models with similar overall rates differ in which dimension moves them. At temperature 0 the observer dispersion was 0.031 for Claude Haiku 4.5 but 0.126 for DeepSeek v3.2 and 0.116 for Grok 4.1, while overall rates were 0.799, 0.703 and 0.777, so the ordering by average and by sensitivity differ.[^c5] Haiku "barely notices who is asking", whereas DeepSeek and Grok shift by over twelve points with the implied audience.[^c6] Three directional effects recurred: gossip framing raised stereotype selection for 5 of 6 frontier models, dissimilar-observer framing raised it for some, and 1990 contexts produced more stereotyping than 2030 for 4 of 6.[^c7] In the budgeted run the year effect held for all five open-weight models, but the gossip effect reversed in Llama and Mistral variants, which is why the authors report fingerprints and not a single score.[^c8] Effect sizes were stable across temperatures 0, 0.7 and 1 (variation under 0.01 for the models checked).[^c9]

The consequence for question design is that the same stereotype question, with the same options, gets different answers depending on cues the asker did not intend as content (who is implied to be listening, what year, a gossip register). The point for answering is that a model's answer is conditional on those cues, so evaluating it under one framing says little about others.

## Limits

- Contexts are English templates; "location" measures sensitivity to the mention of a place, not local cultural behaviour, so effects are prompt sensitivity, not cultural knowledge.[^c10]
- The forced typicality choice is a lab probe; the authors run only exploratory vignettes (four models) to suggest decision-like scenarios shift too, with no validity claims.
- Context sensitivity is not inherently bad: adapting to a deployment may be appropriate, and the fingerprint renders no judgement on which pattern is harmful.[^c11]
- Dimensions were chosen by analogy with social-psychology accounts of situational stereotype expression; the work does not claim they measure underlying beliefs.
- The sign of effects is model-family dependent (gossip), so no universal direction can be assumed. Mitigation effects on fingerprints were not tested.

## Related

- [[prompt-content-over-surface-form]] — contrasts surface-form variation with content; here cue variation alone moves outputs.
- [[forced-choice-safety-collapse]] — another case where forced-choice formats shape behaviour.
- [[absent-answer-forced-choice-bias]] — forced-choice design as a source of bias in measured answers.
- [[social-sycophancy]] — audience-dependent answers, akin to the observer effect.

[^c1]: arxiv-2601-10460 — "relation: model × context × standpoint."
[^c2]: arxiv-2601-10460 — "For each dimension (location, year, style, observer), we compute per-item standard deviation of"
[^c3]: arxiv-2601-10460 — "Full-grid: 360 contexts × 50 items = 18,000 probes per temperature"
[^c4]: arxiv-2601-10460 — "every model we tested shows context-dependent bias."
[^c5]: arxiv-2601-10460 — "Table 4: Context Sensitivity Fingerprint (CSF) summary on the full-grid intrasentence set at T =0."
[^c6]: arxiv-2601-10460 — "Claude Haiku barely notices who is asking"
[^c7]: arxiv-2601-10460 — "Third, the past is more stereotyped than the future: 1990 contexts produce higher"
[^c8]: arxiv-2601-10460 — "This is why we report"
[^c9]: arxiv-2601-10460 — "Effect directions remain stable across temperatures."
[^c10]: arxiv-2601-10460 — "We interpret effects as prompt"
[^c11]: arxiv-2601-10460 — "Context sensitivity is not inherently problematic."
