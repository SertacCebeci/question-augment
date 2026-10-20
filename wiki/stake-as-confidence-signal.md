---
description: "A wager's size, not a stated probability, carried the confidence in an LLM betting pilot: accuracy rose with stake, from about 74% on tiny bets to about 99% on the largest."
aliases: ["bet size as confidence", "wager-based confidence elicitation", "stake channel", "betting as a confidence signal"]
sources: ["arxiv-2512-05998"]
---
# Stake as a confidence channel

When a model must forecast whether another model answers a question correctly and must also say how much it would stake on that forecast, the size of the stake carries information about how sure it is. The pilot that tested this ran 5,400 predictions per condition, and the author's summary is that "Stake size and accuracy tracked each other closely."[^c1] Bets were grouped by size. Tiny stakes of 1 to 1,000 coins "corresponded to mid-range accuracy (74%)."[^c2] Mid-sized stakes were about 76% correct, large stakes of 10,000 to 40,000 about 89%, and bets of 40,000 coins and up were nearly all right: "bets 40,000 coins and higher (n = 170), only 2 of those were incorrect."[^c3]

The mechanism the author proposes is that a bet gives the model a numerical channel that a yes/no label lacks. A "Yes" from the model "looks identical whether its internal belief is 0.55 or 0.95."[^c4] In the betting setup the model "compresses its internal probability distribution into a single, actionable scalar: the stake."[^c5] The author names two drivers, "goal shaping" (the prompt keeps "maximize" in front of the model) and "confidence channeling" (a numerical slot separate from hedged prose). The paper says "Two mechanisms likely drive this", which is a hypothesis, not a test of either driver.[^c6]

What survives the transfer is the shape of the channel: wherever a model commits a quantity under a budget, the size of the commitment can be read as a grade of the commitment, and the grade can be ordered against outcomes. What does not survive is the reading of that grade as a probability. A stake is not a probability in this setup. Each bet pays even odds, so a stake's value to the model is set by the bankroll and not by any scoring rule that rewards a stated belief for being right in proportion to its quality (this is my reading of the design). The author says so directly: the next step is "Proper scoring rules (e.g., Brier, log scores) instead of crude even-odds bets."[^c7] For a strictly proper rule applied to a stated confidence, see [[log-score-verbalized-confidence-reward]].

## Limits

- **Stake may track item easiness rather than confidence.** The predictor that sized its bets best "concentrat[ed] large bets on structurally easy items for" the strong baselines.[^c8] The paper preregistered a difficulty-based accuracy analysis, but "These were not run in the present pilot."[^c9] Nothing in the text separates the stake curve from the difficulty curve, so the curve may be a difficulty curve.
- **The base rate sets a floor the paper does not compute.** Pooled over the six baselines, the answers were 280 of 300 correct for the current tier and 157 of 300 for the prior tier.[^c10] Adding those gives 437 of 600, or 72.8%, which is what a forecaster scores by always answering "correct" (my arithmetic, not the paper's). The predictors reached 79.1% in Control and 81.5% in Incentive.[^c11] Many predictions "assumed it would be 100% of the time" for the strong baselines.[^c12] Large stakes on those calls may mostly reflect that the baseline is strong.
- **The bins pool non-independent bets.** The author notes the "non-independent error structure" of the data and warns against strong claims from it.[^c13] The top bin has 170 bets from nine runs, so its 99% is a small-sample figure.
- **No comparison with a stated probability.** The paper says a useful signal arrives "without asking for explicit probabilities or complex scoring."[^c14] It never elicits probabilities on the same items, so whether stakes carry more information than verbal confidence is not established here.
- **"Calibrated" is not measured.** The conclusion calls the predictors "calibrated, risk-aware forecasters."[^c15] No calibration measure appears in the paper. What was measured is a monotone pattern of accuracy over stake bins; calibration in the sense of [[calibration]] was not.
- **One domain.** "All items are clean math/logic questions with hard ground truth."[^c16] Whether stake tracks confidence on fuzzy judgments is untested.

## Related

- [[calibration]] — the stated-probability standard against which a stake channel would have to be measured; the pilot does not do that.
- [[log-score-verbalized-confidence-reward]] — a strictly proper scoring rule over stated confidence, the alternative to even-odds stakes.
- [[payoff-framing-forecast-accuracy]] — the same pilot's prompt framing, which is what makes the stakes appear; measured on accuracy, not on the stake.

[^c1]: arxiv-2512-05998 — "Stake size and accuracy tracked each other closely."
[^c2]: arxiv-2512-05998 — "Tiny stakes of 1-1,000 LLMCoin corresponded to mid-range accuracy (74%)."
[^c3]: arxiv-2512-05998 — "bets 40,000 coins and higher (n = 170), only 2 of those were incorrect"
[^c4]: arxiv-2512-05998 — "internal belief is 0.55 or 0.95"
[^c5]: arxiv-2512-05998 — "a single, actionable scalar: the stake."
[^c6]: arxiv-2512-05998 — "Two mechanisms likely drive this:"
[^c7]: arxiv-2512-05998 — "Proper scoring rules (e.g., Brier, log scores) instead of crude even-odds bets"
[^c8]: arxiv-2512-05998 — "concentrating large bets on structurally easy items for"
[^c9]: arxiv-2512-05998 — "These were not run in the present pilot"
[^c10]: arxiv-2512-05998 — "Current-generation (Gemini, Sonnet, R2): 280/300 (93.3%)"
[^c11]: arxiv-2512-05998 — "Control accuracy: 79.1%"
[^c12]: arxiv-2512-05998 — "many of the cases assumed it would be 100% of the time"
[^c13]: arxiv-2512-05998 — "non-independent error structure"
[^c14]: arxiv-2512-05998 — "without asking for explicit probabilities or complex scoring"
[^c15]: arxiv-2512-05998 — "Models behaved less like black boxes and more like calibrated, risk-aware forecasters."
[^c16]: arxiv-2512-05998 — "All items are clean math/logic questions with hard ground truth."
