---
description: "Scores an abstaining model by the ratio of its accuracy to its hallucination rate, integrated over risk thresholds and taken as a log-gain over the risk-free point t = 0."
aliases: ["accuracy-to-hallucination ratio", "SNR gain", "signal-to-noise hallucination ratio", "log-scale SNR gain"]
sources: ["arxiv-2512-19920"]
---
# Hallucination SNR gain

A model that answers every question has an accuracy and a hallucination rate, and the two trade against each other once refusal is allowed. The signal-to-noise ratio used by Wu et al. puts them into one number: the share of answers that are correct, divided by the share that are hallucinated. "defined as the ratio of accuracy to hallucination rate under a specified risk preference t."[^c1] At a fixed threshold t, accuracy Acc(t) is the probability that the model answers and the answer is valid, and hallucination Hal(t) is the probability that it answers and the answer is invalid; SNR(t) is their ratio.[^c2]

The single-threshold ratio is not the quantity the paper reports. It extends SNR to an interval of thresholds "by averaging the accuracy and hallucination across the risk" range, so that the interval SNR is the ratio of the two averaged quantities, not the average of ratios.[^c3] The reported quantity is the gain over the full spectrum, taken on a log scale against the risk-free point: SNR-Gain = log of SNR([0, 1]) divided by SNR(0).[^c4] The stated reason for measuring against t = 0 is that the gain is "relative to the risk-free baseline at t = 0."[^c5]

The direction the measure is built to reward is named in the text: "As t increases, a significant increase in SNR(t) indicates effective hallucination mitigation and the model's capability to distinguish between correct and incorrect responses."[^c6] A model whose refusals are indiscriminate does not raise SNR as t rises, because refusing the valid and the invalid alike leaves the ratio where it was. A model that refuses mainly the answers it would have got wrong does.

The reported values illustrate the scale. On BeyondAIME, a 4B model reaches a log-scale gain of 0.806 when it may refuse a whole response, against 0.207 for GPT-5 on the same measure.[^c7] When restricted to flagging individual claims the gain is 0.183, against 0.019 for Gemini-2.5-Pro.[^c8] These are the paper's figures for its own setting; they are not comparisons on a shared scale across different papers.

## Limits

The ratio has no value where the hallucination rate is zero. By the formula the text gives, a model that never answers has Acc(t) = 0 and Hal(t) = 0 at every t, so the ratio is undefined there. How the paper treats that case was not visible in the parts I read; this is my reading of the definition, not a stated result.

The interval measure is an average over t. The formula integrates over t without weighting, which implies a uniform weighting of thresholds; the text does not discuss a different weighting, and a user whose thresholds cluster in a narrow band would see a different gain. This is my inference from the integral, not a finding.

The headline in-domain numbers come from one benchmark of competition mathematics, which the text calls "challenging" and "in-domain." Cross-domain, the abstract reports a calibration result for SimpleQA, "achieves a zero-shot calibration error on par with frontier models including Grok-4 and Gemini-2.5-Pro," not the same SNR gain, so the gain is not shown to transfer.[^c9]

The measure needs each answer labelled valid or not. The claim-level labels come from an LLM judge, so the ratio inherits that judge's errors on both the numerator and the denominator.[^c10]

The measure also scores a model's answers, not what it asks next, and it does not say what a refusal costs the user. A ratio cannot tell a refusal that loses a correct answer from a refusal that saves a wrong one unless the accuracy term is read separately.

## Related

- [[risk-averaged-abstention-reward]] — the threshold-specific reward whose family of thresholds this gain integrates over.
- [[ra-f1]] — a single score for an answer-or-abstain policy as the harmonic mean of precision and accuracy; it fixes one operating point, where this measure integrates over thresholds.
- [[score-separability]] — abstention raises selective accuracy only when the score separates correct from incorrect answers; the SNR gain rises under the same condition, so the two measure one underlying property from different sides.
- [[unnecessary-abstention-aware-recall]] — counts correct answers turned into refusals; a complementary check on over-refusal that the SNR gain only shows through lost accuracy.

[^c1]: arxiv-2512-19920 — "defined as the ratio of accuracy to hallucination rate under a specified risk preference t."
[^c2]: arxiv-2512-19920 — "Acc(t) = E[valid(y) ∧ a(t) = ANS],"
[^c3]: arxiv-2512-19920 — "by averaging the accuracy and hallucination across the risk"
[^c4]: arxiv-2512-19920 — "SNR-Gain = log"
[^c5]: arxiv-2512-19920 — "risk-free baseline at t = 0."
[^c6]: arxiv-2512-19920 — "As t increases, a significant increase in SNR(t) indicates effective hallucination mitigation and the"
[^c7]: arxiv-2512-19920 — "it adaptively refuses an entire response, substantially outperforming GPT-5 (0.207)."
[^c8]: arxiv-2512-19920 — "superior to 0.019 for Gemini-2.5-Pro."
[^c9]: arxiv-2512-19920 — "achieves a zero-shot calibration error on par with frontier models including Grok-4 and"
[^c10]: arxiv-2512-19920 — "which is determined by an LLM Judge"
