---
description: "Hallucinated answers show sharper spikes in a probe's uncertainty score over induced follow-up turns; the max second-order difference of that sequence separates them across domains."
aliases: ["SpikeScore", "maximum second-order difference of uncertainty score", "post-answer continuation instability"]
sources: ["doi-10-48550-arxiv-2601-19245"]
---
# SpikeScore: post-answer instability as a cross-domain hallucination signal

A single-answer uncertainty score (a trained probe such as SAPLMA) separates hallucinated from factual answers inside the domain it was trained on, but its threshold drifts when the domain changes. SpikeScore moves the signal from the level of the score to its shape over time. The model's first answer is fed back as context and a library of natural follow-up questions is asked, producing K = 20 continuation turns. The probe scores each continuation, giving a score sequence. SpikeScore is the maximum absolute second-order difference of that sequence, the point of greatest local curvature.[^c1]

The motivating observation is that models contradict themselves across turns, especially when the user shifts stance. The authors hypothesize this is an explicit manifestation of internal uncertainty or confidence instability.[^c2] In case studies, dialogues that start from a hallucination show rapid rises followed by steep drops in the probe score. Dialogues that start from a factual answer stay comparatively flat.[^c3]

Three empirical regularities were measured, training the probe on one of six datasets and testing on the other five (Llama-3.1-8B-Instruct for the figures):

- Expectation invariance: the mean SpikeScore of the hallucination domain is more than twice that of the non-hallucination domain.[^c4]
- Standard deviation: the hallucination-to-factual ratio of standard deviations lies between 1 and 2.5.[^c5]
- Controlled coefficient of variation of SpikeScore in the hallucination domain, which Theorem 1 needs.[^c6]

Given those conditions, Theorem 1 gives a probabilistic lower bound on separability (a Cantelli-type bound on AUROC). The authors claim the bound "may extend across domains under the examined conditions".[^c7] The paper also reports that SpikeScore beats the coefficient of variation of the score sequence. They argue global variation misses fine-grained local differences.[^c8] Combining SpikeScore with SAPLMA or SEP beats the training-free scores they tried (perplexity, reasoning score, in-context sharpness), and the paper reports that it beats the generalization-oriented methods PRISM and ICR Probe.[^c9]

The transferable idea (my reading, not the paper's claim): what is stable across domains may be the dynamics of confidence under repeated probing, not its level.

## Limits

- The cross-domain guarantee rests on three conditions that were observed on six datasets and four models. They are not derived. The authors themselves hedge ("may extend").
- The paper notes that some individual domains fall below the mixture-level bound even when the average AUROC is higher.
- Needs about 20 extra generation turns per question plus a trained probe, so it costs far more than single-pass scores. The cost is not benchmarked here.
- The follow-up questions come from a fixed prompt library, so whether the effect depends on the prompt style is untested in what I read.
- Detection only. It says nothing about correcting the hallucination.

## Related

- [[trajectory-uncertainty-quantification]] — also scores uncertainty over a trajectory rather than one output.
- [[audio-llm-trustworthiness-uncertainty-instability]] — instability of uncertainty as a trust signal in another modality.
- [[contextual-inertia]] — multi-turn behavior in which earlier context shapes later answers.

[^c1]: doi-10-48550-arxiv-2601-19245 — "We design SpikeScore, defined as the maximum second-order difference of SAPLMA scores along the induced continuation"
[^c2]: doi-10-48550-arxiv-2601-19245 — "We hypothesize that this behavior represents an explicit manifestation of internal uncertainty or confidence instability."
[^c3]: doi-10-48550-arxiv-2601-19245 — "In contrast, such spikes are notably absent in dialogues initiated from factual responses."
[^c4]: doi-10-48550-arxiv-2601-19245 — "the expectation of SpikeScore for the hallucination domain is more than twice that for the non-hallucination domain"
[^c5]: doi-10-48550-arxiv-2601-19245 — "Observation 2 (Standard Deviation Differences.)"
[^c6]: doi-10-48550-arxiv-2601-19245 — "Observation 3 (Controlled Coefficient of Variation.)"
[^c7]: doi-10-48550-arxiv-2601-19245 — "our analysis suggests that this bound may extend across domains under the examined conditions"
[^c8]: doi-10-48550-arxiv-2601-19245 — "focusing solely on global variation may overlook fine-grained differences"
[^c9]: doi-10-48550-arxiv-2601-19245 — "integrating our SpikeScore with SAPLMA or SEP achieves substantially better overall performance than training-free methods"
