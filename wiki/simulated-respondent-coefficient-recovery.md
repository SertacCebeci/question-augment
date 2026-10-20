---
description: "Matching human response distributions does not make a simulated sample recover regression results: the best finetuned LLM reached sign F1 of about 0.77, with a 0.33 false-positive rate."
aliases: ["sign recovery of simulated data", "coefficient recovery", "F1(Sign)", "inferential fidelity of simulated respondents"]
sources: ["arxiv-2511-21218"]
---
# Simulated-respondent coefficient recovery

A simulated sample can be checked at two levels that are easy to confuse. One asks whether its responses look like human responses: their spread, their means, their distance from the human distribution. The other asks whether the statistical conclusions drawn from it match the conclusions drawn from the human data. The paper under this note measures the second level directly. It takes the six regression models of the original human experiment and refits them on LLM-generated responses, then asks whether the same coefficients come out significant with the same sign.[^r1]

The score is F1(Sign). It "jointly accounts for false positives and false negatives while also requiring that true positives have the correct sign."[^r2] Under this score the models do poorly. "The best-performing finetuned model achieves an F1(Sign) of only ≈ 0.769, and its false positive rate (FPR) remains high at ≈ 0.333."[^r3] The failure is not confined to the base model. The paper states that "all models produce inaccurate coefficient estimates, with the unfinetuned model and the models finetuned on only a single treatment group performing the worst."[^r4]

The mechanism of the split is the point of the note. The same finetuned models had improved on the first level. The abstract puts it this way: "finetuning on relatively small subsets of data substantially improves heterogeneity, alignment, and belief–action coherence".[^r5] Yet the second level did not follow. The authors' reading is that the distributional gains leave a bias that matters once the data are used for inference: the simulated datasets "still introduce non-negligible bias when used for formal statistical inference."[^r6] A sample can therefore look more like the humans and still produce a different significance pattern. A check on the marginal distributions is not a check on the regression.

What the note adds to the family of simulated-respondent checks is this level of fidelity. The variance and structure checks ask whether the simulator has the human spread or factor structure; a coefficient check asks whether the scientific conclusion survives. The paper's own recommendation is modest: finetuned models on as few as 30 observations are "better suited for in silico prototyping than base LLMs," and "should be viewed as complements to, rather than substitutes for, human subjects."[^r7][^r8] For asking, that means a simulated pilot can help shape an instrument, while a power or effect estimate that will be reported needs a human check. The paper does not say how large a human check must be.

## Limits

- One human dataset and one simulator. The sample is "data from 929 U.S. adults"[^r9] in a security attack experiment, and the simulator is GPT-4.1. Whether other populations or models show the same break is not tested here.
- Few tests. "there are 22 total coefficients across the six replicated" regression models, so an F1 score rests on a small number of coefficients, and, by my inference, a single coefficient flipping moves the score noticeably.
- The paper reports the failure but does not decompose its cause. It does not show whether the bias comes from the spread, the means, or the way the regressors are generated. Any link to [[simulated-respondent-variance-deficit]] is my inference.
- The regression result is a single outcome of one design; it does not show that finetuning cannot be made to recover coefficients with more data or a different method. The authors claim only that the tested models did not.
- The recommendation to use these models for prototyping is the authors'. The regression result does not by itself establish that a sample which fails inference is still useful for design; that step is not tested here.

## Related

- [[simulated-respondent-variance-deficit]] — the spread gap that distributional checks see; here finetuning narrowed the gap and inference still failed, so spread is not the whole story (my inference)
- [[simulated-respondent-structure-fidelity]] — a factor structure can match while score distributions and variances do not; this note is a further level, one step closer to the conclusion
- [[simulated-respondent-composite-fidelity]] — item-level agreement does not validate a composite; the same gap between a local match and a downstream quantity
- [[value-action-gap]] — the belief-action measure that the same finetuned models reduced, while the regression results did not follow

[^r1]: arxiv-2511-21218 — "we replicate the six regression models reported in the original study"
[^r2]: arxiv-2511-21218 — "jointly accounts for false positives and false negatives while also requiring that true positives have the correct sign"
[^r3]: arxiv-2511-21218 — "the best-performing finetuned model achieves an F1(Sign) of only"
[^r4]: arxiv-2511-21218 — "Overall, all models produce inaccurate coefficient estimates, with the unfinetuned model and the"
[^r5]: arxiv-2511-21218 — "finetuning on relatively small subsets of data substantially improves heterogeneity, alignment, and belief–action coherence"
[^r6]: arxiv-2511-21218 — "still introduce non-negligible bias when used for formal statistical inference"
[^r7]: arxiv-2511-21218 — "better suited for in silico prototyping than base LLMs"
[^r8]: arxiv-2511-21218 — "should be viewed as complements to, rather than substitutes for, human subjects"
[^r9]: arxiv-2511-21218 — "The sample we analyze consists of behavioral data from 929 U.S. adults"
