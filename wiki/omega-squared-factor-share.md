---
description: "Omega-squared gives the share of score variance a factor accounts for in a factorial design, turning significance into magnitude; marginal shares add up only when interactions are weak."
aliases: ["omega squared", "ω²", "ω2 effect size", "variance share per factor", "factor share of score variation"]
sources: ["arxiv-2601-02224"]
---
# Omega-squared factor share

Omega-squared (ω²) is an effect-size measure for a factor in a one-way ANOVA. It is the proportion of the variation in the scores that the factor accounts for, so a factor's ω² is a statement about how much of the spread the factor explains, where a p-value only says whether the spread is unlikely to be chance. The study reports it as "the proportion of variance in scores attributable to the factor (e.g., ω 2 = .06 for XAI means 6% of score variation is due to XAI choice)."[^c1]

The mechanics are simple. The study runs one-way ANOVA for each research question, reports ω² beside the p-value, and reads magnitude against conventions borrowed from Field (2013): "interpret: < .01 negligible," with small, medium and large bands up to "medium, > .14 large."[^c2] Because several evaluation dimensions were tested together, the authors apply the Benjamini-Hochberg correction and report both raw and corrected p-values.[^c3] With these numbers the paper can say, for example, that on Expert Relevancy the LLM factor has ω² = .50 while the XAI factor has ω² = .02, which is why the study's headline is that "LLM choice dominates all other factors (ω 2 up to .50)."[^c4]

What the measure buys is a ranking of factors on one scale. A reader who sees only p-values could conclude that every factor matters, since with enough scores almost any difference is significant. ω² says that one factor explains roughly 25 times the variance of another on the same dimension, which is a claim about where to spend effort. This is the use the note records: choose the factor whose ω² is large before tuning the small ones.

The transfer to other fields has one condition. A one-way ω² is the share of the variance that a single factor accounts for on its own, and the shares of several factors add up to the whole only when the factors do not interact. The study reports that the interactions are not small: "The strong Strategy×LLM interactions" have ω² between .28 and .41, and "the significant XAI×LLM interactions" show that the benefit of XAI "depends on the generator."[^c5][^c6] Under those interactions the marginal shares are averages over the other factors' levels. The XAI share of .02 is an average across three LLMs; on Expert Relevancy the raw gain is 0.3 points for GPT-4o and none for Llama-3 (a score-point difference, not an ω², so the two scales are not directly comparable). The marginal ω² therefore answers "how much does this factor matter on average over this design," not "how much does it matter for a given generator."

## Limits

The ranking is only as good as the levels chosen. The study uses three LLMs, and it says plainly that "other LLMs (e.g., Claude, Gemini)" were not tested, so "LLM choice dominates" is a claim about these three models and this pool of options, not about LLMs in general.[^c7] A factor whose levels are chosen by the experimenter can be inflated or deflated by the choice of levels, and ω² does not report that.

The paper's own count is inconsistent. Section 3.7 says "We define four evaluation dimensions," while the paragraph that applies the correction says "Because we test five evaluation dimensions simultaneously."[^c8] The abstract and conclusions say four. The inconsistency does not change the ω² values, but it means the number of tests behind the correction is not clearly stated.

The ω² values here are point estimates from one dataset of 660 explanations drawn from three test instances. The paper reports no interval for them in the main text, and robustness checks (Welch ANOVA, Games-Howell) are deferred to an appendix that the note has not read. Treat the ratios as descriptive of this design. Reading a factor's ω² as a property of the factor, separate from the design it was measured in, is the step the data do not license.

## Related

- [[attribution-narration-bottleneck]] — the study whose headline ratio, LLM .50 against XAI .02, this measure produced.
- [[interpretability-paradox-in-narrated-explanations]] — a model-type comparison read through the same variance shares.
- [[query-type-variance-in-qpp]] — another reading of variance shares, there from a fitted model's explained variance rather than an ANOVA; the same question of what a share does and does not say applies.

[^c1]: arxiv-2601-02224 — "as a measure of effect size – the proportion of"
[^c2]: arxiv-2601-02224 — "interpret: < .01 negligible"
[^c3]: arxiv-2601-02224 — "we apply Benjamini-Hochberg"
[^c4]: arxiv-2601-02224 — "dominates all other factors (ω 2 up to .50), with"
[^c5]: arxiv-2601-02224 — "The strong Strategy×LLM interactions"
[^c6]: arxiv-2601-02224 — "The significant XAI×LLM interactions reveal"
[^c7]: arxiv-2601-02224 — "other LLMs (e.g., Claude, Gemini)"
[^c8]: arxiv-2601-02224 — "Because we test five evaluation dimensions"
