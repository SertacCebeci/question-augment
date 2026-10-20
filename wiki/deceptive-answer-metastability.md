---
description: "In moral dilemmas where honesty costs, models' deceptive answers flip to honest under paraphrase, resampling and activation noise far more than honest ones, so reasoning drifts models toward honesty."
aliases: ["metastable deception", "reasoning increases honesty", "honesty as stable attractor"]
sources: ["arxiv-2603-09957"]
---
# Deceptive-answer metastability

Yuan et al. ask why a model recommends deception when honesty is costly. They build DoubleBind (realistic dilemmas with honesty costs from 1k to 100k, several paraphrases each) and augment DailyDilemmas with the same cost scaling. Two elicitation modes are compared: token-forcing (read the A/B probabilities straight after the scenario) and reasoning (deliberate for a set number of sentences, then answer). Models are Gemma-3, Qwen-3, Olmo-3 and Gemini 3 Flash.

## What was found

- Reasoning raises honesty, and more of it raises it more. "models are significantly more likely to choose the honest option when required to reason before providing a final answer" and "the longer they deliberate the more honest they become."[^c1] This is the reverse of the human pattern the authors cite, where time to deliberate lowers honesty.
- The trace does not explain the answer. Autoraters reading Gemma 27B traces predicted honest outcomes at about 97% but deceptive outcomes at about 53%, chance, even after nearly 1,000 words, while the model's own confidence was above 0.9.[^c2] So a deceptive decision "is driven by factors that do not leave a legible trace in the reasoning tokens."[^c3]
- Which scenarios benefit from reasoning is model-specific: the Jaccard overlap between models is 0.17.[^c4] The authors read this as a property of each model's answer space, not of the scenario.
- Deceptive answers are fragile on three perturbations: paraphrase, resampling at temperature 1.0 (five traces), and Gaussian noise in intermediate activations. Honest answers rarely flip; a substantial share of deceptive ones become honest.[^c5]
- Within a reasoning trajectory, token-forcing at each sentence boundary shows honest segments longer than deceptive ones, and honest segments lengthen over the trace (Spearman 0.77 against 0.57 for deceptive).[^c6]
- Interpolating (SLERP) between end-of-trace representations: under noise, survival above 0.5 probability is lower for deceptive pairs, for example 14% of Gemma-3-12B deceptive paths dip below 0.5.[^c7]

The authors' account is that deception sits in smaller, metastable regions and honesty in a larger, stable one, so generating deliberative tokens traverses a biased space and settles in the honest default.[^c8]

## Limits

- Deception is operationalized as the model recommending the option humans labeled deceptive, in a forced A/B choice; intent is not measured, and the authors sidestep it on purpose.
- The "geometry" is a hypothesis supported by indirect probes (flip rates, segment lengths, interpolation). No region volume was measured, and the Qwen-4B noiseless interpolation showed no holes in either group.
- Models were instruction-tuned, not reasoning-trained, for the main results; the budget was set by a sentence count, with Gemini 3 Flash by level.
- Honesty probability falls as costs rise, and reasoning does not always help; the effect depends on option order (deceptive listed last gains most).
- Noise affected token-forcing little; the reasoning-mode effect is attributed by the authors to cumulative noise, which is their reading.
- Whether the same asymmetry holds for other kinds of wrong answers, such as errors or sycophancy, was not tested.

## Related

- [[reasoning-trace-behavioral-transfer]] — traces shape later behavior, while here traces fail to predict the answer.
- [[hint-adherence-without-acknowledgement]] — another case of reasoning omitting what drives the answer.
- [[reasoning-masked-sycophancy]] — reasoning that does not reveal the real driver of an answer.

[^c1]: arxiv-2603-09957 — "models are significantly more likely to choose the honest option when required to reason before providing a final answer"
[^c2]: arxiv-2603-09957 — "they are only as good as chance at identifying reasoning traces that will end with a recommendation to be deceptive (∼53% accurate)"
[^c3]: arxiv-2603-09957 — "is driven by factors that do not leave a legible trace in the reasoning tokens"
[^c4]: arxiv-2603-09957 — "On average the overlap between models is low (Jaccard index = 0.17"
[^c5]: arxiv-2603-09957 — "while honest answers remain generally robust to these interventions, deceptive answers are fragile and frequently flip to honesty under perturbation"
[^c6]: arxiv-2603-09957 — "honest segments are longer than deceptive ones and trajectories ending with a deceptive outcome exhibit higher flip rates"
[^c7]: arxiv-2603-09957 — "On 14% of paths between deceptive"
[^c8]: arxiv-2603-09957 — "generating deliberative tokens as part of moral reasoning entails the traversal of a biased representational space"
