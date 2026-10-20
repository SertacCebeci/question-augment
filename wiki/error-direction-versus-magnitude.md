---
description: "A scorer's signed error, whether it over- or under-scores, is a quantity separate from average error size, can flip under prompting, and bears on fairness."
aliases: ["directional scoring error", "lenient versus harsh scoring", "overestimation and underestimation", "signed scoring error", "sign-blind error metric"]
sources: ["doi-10-35377-saucis-1835608", "doi-10-48550-arxiv-2604-21334", "arxiv-2512-04099"]
---
# Error direction versus error magnitude

A scorer's error has two parts that a single summary merges. Magnitude is how far a score sits from the expert score. Direction is whether it sits above or below. Mean absolute error and RMSE report only the first. The Turkish short-answer study adds a directional analysis because global metrics "only show the average error magnitude", while the direction and frequency of errors are a separate matter.[^d1] It classes a positive difference between model and expert as overestimation and a negative one as underestimation, and it reports the share of each: "were classified as overestimation, while negative differences were classified as underestimation."[^d2]

Direction changed with the prompt and the model. On the binary item Q1 under zero-shot scoring, GPT-4o (52%), Gemini 1.5 Pro (31%) and GPT-4.1 (29%) "showed a strong tendency to under-score", while over-scoring was concentrated in LLaMA 3.1 8B (20%) and Gemini 2.0 Flash (11%).[^d3] The authors summarise the zero-shot pattern as most models underestimating, with a minority overestimating.[^d4] Under one-shot scoring the balance moved: "for under-scoring increased (particularly in Gemini 1.5 Pro, GPT-4o, and Gemma 2), while the over-scoring rate generally decreased."[^d5] The Discussion states the reversal more broadly: "Under one-shot conditions, the general trend reversed."[^d6] The per-model shares show that this is a summary over heterogeneous models, not a rule each model followed.

The authors connect a consistent tilt to validity. Because "a model’s tendency to consistently assign high or low scores directly affects" the fairness and predictability of scoring, they treat direction as a consequential-validity question, not a technical detail.[^d7] My inference, which the study does not test: two scorers with the same MAE, one always lenient and one always harsh, would not be interchangeable for a selection decision, because the errors do not cancel across students.

A two-sided version of the same idea appears when an item has only two possible directions. On items where a model's answer can lean toward one of two framings, the paper defines a directional error bias from the errors that lean each way, "directional error bias are then formalized as", normalised by all errors in the subset.[^d8] Among the 20 models of that study, "Among the 20 models, 15 exhibit Bdir > 0", so most models' wrong answers lean one way.[^d9] The tilt also survives one-shot in-context examples: "One-shot in-context steering also fails to reliably reverse the bias".[^d10] The ordinal scorer above reversed under one-shot prompting,[^d6] so the two-sided case in [[framework-contested-ground-truth]] looks more persistent. Both measures rest on one reference set of signs, so a tilt may partly reflect that reference.

The distinction also matters when the score feeds a decision that reads only the sign. A cryptocurrency forecasting paper trains its model on squared error and then tests it on a trading rule, "a simple sign-based rule", that goes long on a positive predicted return and short otherwise.[^d11] The authors name the mismatch: "standard error metrics like MSE, which are indifferent to the direction of an error."[^d12] On ETHUSDT the lowest-error model, PMformer, "resulted in a negative Total ROI (-0.67%)", while another model earned a small positive return.[^d13] On BTCUSDT PMformer "achieved the highest statistical accuracy" and also the highest directional accuracy (59.8%), yet FEDformer had a "higher Total ROI (+38.1%) and Sharpe Ratio (4.54)".[^d14][^d15][^d16] The authors draw the general lesson as "a pronounced disconnect between statistical accuracy and practical trading utility".[^d17] My inference, which the paper does not test: a magnitude loss spends its fit on the size of errors that a sign rule never reads, so it can rank models differently from the decision that will use them. Which quantity is trained and which is reported is then a choice of objective, not a default.

## Limits

- The shares are per model and per item, on 254 responses for Q1 and 145 for Q2. The sections read give no interval for them, so a 29% against 31% difference is not a ranking.
- Direction is measured against one expert score set. The authors use "the single set of expert scores" as ground truth, so a sign flip may reflect noise in the reference as well as the model.
- The sections read report direction per item, not per score level. The middle-of-scale pattern is a separate analysis (see [[intermediate-score-error-peak]]), and the two are not combined here.
- Whether the tilt affects particular groups of students is not measured. The fairness link is asserted as a consequence of the tilt, not shown.
- The trading evidence is one 10 % chronological test split, two assets, and one value per model in the tables read, with no interval; the BTC-ETH contrast is not a significance result. The authors attribute the ETH loss to features their set did not capture,[^d18] and name transaction costs as one reason an accurate forecast may not pay.[^d19]

## Related

- [[llm-judge-biases]] — lenient and harsh tendencies of judges, which is the same sign-of-error idea in pairwise verdicts and in length
- [[intermediate-score-error-peak]] — the error by true score level, which the sign alone does not show
- [[exact-match-versus-weighted-agreement]] — a second way a summary statistic can hide the structure of the errors
- [[framework-contested-ground-truth]] — the two-sided case: a directional error bias on items whose two framings predict opposite signs
- [[metric-criterion-decoupling]] — the paper-level version of the same mismatch: a metric chosen by its form is not tied to the decision it should test
- [[residual-variance-fine-tuning-objective]] — squared error as a fitting objective whose minimum need not be the quantity that matters downstream

[^d1]: doi-10-35377-saucis-1835608 — "which only show the average error magnitude, the direction and frequency of the models’ errors were evaluated"
[^d2]: doi-10-35377-saucis-1835608 — "were classified as overestimation, while negative differences were classified as underestimation"
[^d3]: doi-10-35377-saucis-1835608 — "models showed a strong tendency to under-score"
[^d4]: doi-10-35377-saucis-1835608 — "most models (especially GPT-4o and Gemini 1.5 Pro) exhibited a tendency toward underestimation"
[^d5]: doi-10-35377-saucis-1835608 — "for under-scoring increased (particularly in Gemini 1.5 Pro, GPT-4o, and Gemma 2), while the over-scoring rate generally decreased"
[^d6]: doi-10-35377-saucis-1835608 — "Under one-shot conditions, the general trend reversed"
[^d7]: doi-10-35377-saucis-1835608 — "a model’s tendency to consistently assign high or low scores directly affects"
[^d8]: doi-10-48550-arxiv-2604-21334 — "directional error bias are then formalized as"
[^d9]: doi-10-48550-arxiv-2604-21334 — "Among the 20 models, 15 exhibit Bdir > 0"
[^d10]: doi-10-48550-arxiv-2604-21334 — "One-shot in-context steering also fails to reliably reverse the bias"
[^d11]: arxiv-2512-04099 — "a simple sign-based rule"
[^d12]: arxiv-2512-04099 — "standard error metrics like MSE, which are indifferent to"
[^d13]: arxiv-2512-04099 — "resulted in a negative Total ROI (-0.67%)"
[^d14]: arxiv-2512-04099 — "PMformer achieved the highest statistical"
[^d15]: arxiv-2512-04099 — "higher Total ROI (+38.1%) and Sharpe Ratio (4.54)"
[^d16]: arxiv-2512-04099 — "the highest directional accuracy"
[^d17]: arxiv-2512-04099 — "a pronounced disconnect between statistical accuracy and practical trading utility"
[^d18]: arxiv-2512-04099 — "our feature set and modeling approach did not fully capture"
[^d19]: arxiv-2512-04099 — "too small relative to transaction costs or volatility to exploit"
