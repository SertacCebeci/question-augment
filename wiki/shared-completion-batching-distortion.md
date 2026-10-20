---
description: "Generating several records in one autoregressive completion exaggerates cross-variable correlations in synthetic data, via earlier answers acting as context, while marginals can improve."
aliases: ["shared-completion batching", "answer-history contamination", "request-partition invariance failure"]
sources: ["doi-10-48550-arxiv-2609-32546"]
---
# Shared-completion batching distortion

When a language model answers for ten simulated respondents in one completion rather than ten separate ones, earlier answers become context for later ones. In a matched experiment on 2,000 European Social Survey profiles (profiles, examples, questions and decoding fixed), ten per request rather than one raised mean absolute error in within-country correlations by 48-58% for one model and 114-127% for another.[^c1] The paper names the desideratum violated "request-partition invariance": splitting the same profiles across requests should not materially change the quantities estimated.[^c2]

## What the distortion is

It is mostly inflated strength, not lost pattern. Batching raised mean |r| from 0.360 to 0.459 (Qwen) and 0.355 to 0.596 (Llama), against 0.193 in the human reference, yet the batched correlations kept a Spearman agreement of 0.864 and 0.866 with the human ordering.[^c3] After the best common shrinking multiplier, one- and ten-person error were both about 0.10, so simple weakening removes most of it (an oracle that uses evaluation answers, so not an available fix).[^c4]

## Answer history is a causal channel

Re-pairing the same preceding values (same marginals, same profiles) as positive versus negative history moved the correlation among newly generated respondents from 0.963 to -0.670 (Qwen/NHANES), showing earlier pairings shape later relationships.[^c5] Hiding preceding answers from the model state lowered correlation error (Qwen/NHANES at position ten: 0.367 to 0.197) but raised marginal error.[^c6] The gain at position two, with a single predecessor, shows history can matter without the model extracting a covariance matrix.[^c7] The paper leaves the internal computation open.[^c8]

## Marginals and correlations trade off

Batched outputs had lower marginal Wasserstein error than one-person outputs in all six settings, so one-person generation is not uniformly more accurate.[^c9] A post hoc map that repaired correlations lowered correlation error in all six settings while worsening marginals in each.[^c10] The paper's conclusion: request construction is part of the data-generating process and validity must be judged against the intended analysis.

## Limits

- Evidence is from survey-respondent simulation with two open models, three seeds and twenty countries; intervals omit uncertainty over new seeds and countries, and variable pairs are not independent replications.
- Some ten-person conditions fell below 99% validity; the ACS dataset gave weaker evidence (Llama's effect varied in direction).
- The correction results are exploratory (my reading of the paper's own label); the hidden-history intervention changes model state in ways (token gaps, runtime) that prevent apportioning shares of the penalty.
- Whether this transfers to non-survey generation, or to question answering generally, is not tested. That batching questions in one prompt biases later answers is my inference only.

## Related

- [[sycophantic-capitulation]] — another case where earlier context in a conversation bends later model output
- [[refinement-drift-under-forced-deliberation]] — prior generated text steering subsequent generation

[^c1]: doi-10-48550-arxiv-2609-32546 — "generating ten rather than one respondent per request increases mean absolute error in within-country correlations by 48–58% for Qwen3.8-27B and 114–127% for Llama-3.3-70B-Instruct across three seeds"
[^c2]: doi-10-48550-arxiv-2609-32546 — "splitting the same profiles across requests should not materially change the population quantities the sample is intended to estimate"
[^c3]: doi-10-48550-arxiv-2609-32546 — "Batching raises mean |r| from 0.360 to 0.459 for Qwen and from 0.355 to 0.596 for Llama"
[^c4]: doi-10-48550-arxiv-2609-32546 — "one- and ten-person MAE are both approximately 0.10"
[^c5]: doi-10-48550-arxiv-2609-32546 — "Changing history pairing from positive to negative moves target correlations from 0.963 to −0.670 for Qwen/NHANES"
[^c6]: doi-10-48550-arxiv-2609-32546 — "0.367 to 0.197 at ten"
[^c7]: doi-10-48550-arxiv-2609-32546 — "History can therefore matter without the model first extracting a covariance matrix from several preceding respondents."
[^c8]: doi-10-48550-arxiv-2609-32546 — "while leaving the model’s internal computation open"
[^c9]: doi-10-48550-arxiv-2609-32546 — "batched outputs have lower marginal Wasserstein error than one-person outputs in all six settings"
[^c10]: doi-10-48550-arxiv-2609-32546 — "The full map lowers mean correlation error in all six domain–model settings while worsening marginal accuracy in each"
