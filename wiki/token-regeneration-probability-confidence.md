---
description: "A diffusion LM scores its own output by one forward pass on the full unmasked sequence, averaging log-probability of regenerating chosen tokens; cheaper than Monte Carlo masking and more accurate."
aliases: ["DiSE", "diffusion self-evaluation", "sequence regeneration score"]
sources: ["arxiv-2603-02760"]
---
# Token-regeneration probability as self-evaluation confidence

A diffusion language model (dLLM) predicts all positions at once, so it can be asked to predict tokens that are already visible. The DiSE score feeds the complete sequence X back in and averages, over a chosen index set U of positions, the log-probability that the model regenerates each token under the full context: the mean of log p(x_i | X) over i in U.[^c1] The traditional alternative estimates sequence likelihood by masking l randomly sampled tokens, predicting them, and averaging over many Monte Carlo draws, because the exact expectation is intractable.[^c2]

## Mechanism

Masking-based estimates need N_mc forward passes and are noisy at small N_mc. The regeneration score needs one pass over a predefined position set, so cost and reliability are traded differently. The authors report that on LLaDA-Instruct-8B it beats the N_mc = 1 Monte Carlo baseline, which has similar cost, by 23.6% on ARC-Challenge and 8.9% on GPQA. Against the N_mc = 32 baseline it gives a 32x speedup with gains of 6.4% and 1.5%.[^c3]

Which positions enter U matters. In an ablation for uncertainty quantification, the last 10 non-end-of-text tokens tended to give the highest ROC-AUC, because they usually sit in the answer region. Earlier tokens say little about correctness, and including end-of-text tokens from the last block hurts.[^c4] For a questioner or answerer this means that confidence is best read where the committed answer lives, not averaged over the whole generation.

The score is also used as a real-time signal. The authors build a training-free flexible-length generation procedure that searches, assesses and stops to pick an output length from the model's self-assessment.[^c5] They report that DiSE correlates positively with semantic coherence and answer accuracy.[^c6]

## Limits

- Only diffusion LMs (LLaDA, Dream) are tested; autoregressive models already have an exact likelihood, so the transfer there is empty.
- Tokens the model sees are scored under their own presence in context. My inference is that this could inflate confidence for fluent but wrong text, since the paper's evidence is correlation with accuracy, not calibration under adversarial fluency.
- Gains are reported on a few benchmarks (ARC-Challenge, GPQA, Countdown, GSM8K, MATH500); I read only the headline results and selection ablation, not the full tables.
- Position choice (last 10 non-EOT) is tuned empirically; it presumes the answer sits at the end.

## Related

- [[same-model-self-verification-conditional-confidence]] — another same-model confidence signal whose value depends on baseline and task
- [[inconsistency-penalized-confidence]] — a different route to confidence from the model's own outputs
- [[outcome-distribution-entropy-detector]] — uncertainty read from output distributions

[^c1]: arxiv-2603-02760 — "model regenerating token xi at position i given the"
[^c2]: arxiv-2603-02760 — "Since the exact computation of this expectation"
[^c3]: arxiv-2603-02760 — "Even against the more expensive"
[^c4]: arxiv-2603-02760 — "tokens tends to yield higher ROC-AUC scores"
[^c5]: arxiv-2603-02760 — "guides the process of searching, assessing and stopping to determine the optimal generation length."
[^c6]: arxiv-2603-02760 — "positively correlated with both semantic coherence"
