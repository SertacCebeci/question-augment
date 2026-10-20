---
description: "Framing a forecast task as a fictional-money bankroll game raised accuracy 2.4 points in a pilot, short of significance, and steepened gains across rounds; the mechanism is untested."
aliases: ["incentive framing of forecasts", "fictional prediction market framing", "bankroll framing", "payoff framing"]
sources: ["arxiv-2512-05998"]
---
# Payoff framing of forecasts

The same forecasting task can be worded as a neutral accuracy request or as a payoff game. In the pilot, the Control prompt asked for a plain correct/incorrect forecast and told the model to "Focus on being accurate."[^p1] The Incentive prompt gave each predictor a bankroll of 1,000,000 coins, asked for a stake on each forecast, and instructed the model to maximise its final balance, "not to maximize accuracy."[^p19] Only the wording and the output format changed between conditions; "Nothing about the underlying model weights changes."[^p2]

The accuracy effect was small. Incentive runs reached 81.5% against 79.1% in Control, a difference of 2.4 points.[^p3] The author's own reading is that "accuracy gains were modest and did not reach statistical significance (p = .089) in this pilot."[^p4] The confidence interval "spans zero, indicating the true effect could plausibly range from slightly negative to very" large.[^p5] The paper's headline is therefore not that the game makes models more accurate: "The key finding is not that fictional money makes models smarter."[^p6]

The learning effect was larger. From Round 1 to Round 4 accuracy rose by 12.0 points in Incentive runs against 2.9 in Control, with t(16) = 2.87 and p = .011.[^p7] Per predictor, the Incentive gain was positive in every case, and "Just one of the nine Incentive cases saw a decrease in performance between rounds."[^p8] The author's account is that a bankroll drop is a louder signal than a wrong label, but this is a guess: "It could be that this numerical" signal reaches the model more strongly than a token does.[^p9] Control runs also received a per-round summary of which baselines were right or wrong,[^p10] so the feedback content was shared, and what differed is the numerical framing of the outcome.

## Limits

- **Framing and format move together.** The Incentive condition changes the prompt's goal and the output format at once: "The output format (same prediction but adding a stake)."[^p11] The pilot cannot say whether the accuracy or learning effect comes from the payoff wording, from the requirement to stake, or from the running bankroll. The author states two mechanisms, goal shaping and confidence channelling, as likely drivers and does not isolate either.[^p12]
- **Small and manual.** "Nine runs per condition via web UIs is underpowered and noisy."[^p13] The predictors were run by hand in web interfaces, and the paper describes the study as exploratory: "the goal of this pilot is to explore effect sizes and assess protocol viability, not to test definitive hypotheses."[^p14]
- **The money is fictional and the framing is thin.** "done to convince the Predictor Models that LLMCoin mattered, which may have" muted any effect, as the author concedes.[^p15] A stronger or real-stakes framing was not tested, so the size of the effect under other framings is unknown.
- **One domain.** "All items are clean math/logic questions with hard ground truth."[^p16] The author expects that results may not carry over to subjective work such as writing, planning, summarization, quality, or safety assessment.[^p17] Whether a payoff frame helps on fuzzy judgments is not established.
- **Constraint slips in the same runs.** Three Incentive runs exceeded the per-round bankroll limit by about 0.2%, and the paper "retained but flagged" them, noting they "slightly overstate" what a constraint-respecting strategy would earn.[^p18] The accuracy result does not depend on this, but the bankroll numbers do.

## Related

- [[stake-as-confidence-signal]] — the stake channel that the same payoff framing produced; the stake, not the accuracy, is where the framing shows a measurable signal.
- [[mandate-incentive-framing-split]] — the same lever, the wording of an outcome, measured on safety behaviour in agents rather than on forecast accuracy.

[^p1]: arxiv-2512-05998 — "Focus on being accurate."
[^p2]: arxiv-2512-05998 — "Nothing about the underlying model weights changes."
[^p3]: arxiv-2512-05998 — "Difference: +2.4 pp (Incentive > Control)"
[^p4]: arxiv-2512-05998 — "accuracy gains were modest and did not reach statistical significance (p = .089) in this pilot."
[^p5]: arxiv-2512-05998 — "spans zero, indicating the true effect could plausibly range from slightly negative to very"
[^p6]: arxiv-2512-05998 — "The key finding is not that fictional money makes models smarter"
[^p7]: arxiv-2512-05998 — "Incentive runs improved by 12.0 pp on average versus"
[^p8]: arxiv-2512-05998 — "Just one of the nine Incentive cases saw a decrease in performance between rounds"
[^p9]: arxiv-2512-05998 — "It could be that this numerical"
[^p10]: arxiv-2512-05998 — "After each round, the Predictor received a summary of which Baselines were"
[^p11]: arxiv-2512-05998 — "The output format (same prediction but adding a stake)."
[^p12]: arxiv-2512-05998 — "Two mechanisms likely drive this:"
[^p13]: arxiv-2512-05998 — "Nine runs per condition via web UIs is underpowered and noisy."
[^p14]: arxiv-2512-05998 — "explore effect sizes and assess protocol viability, not to test definitive hypotheses."
[^p15]: arxiv-2512-05998 — "done to convince the Predictor Models that LLMCoin mattered, which may have"
[^p16]: arxiv-2512-05998 — "All items are clean math/logic questions with hard ground truth."
[^p17]: arxiv-2512-05998 — "generalize to more subjective tasks like writing, planning, summarization, quality, or"
[^p18]: arxiv-2512-05998 — "They are retained but flagged in the analysis."
[^p19]: arxiv-2512-05998 — "to maximize accuracy."
