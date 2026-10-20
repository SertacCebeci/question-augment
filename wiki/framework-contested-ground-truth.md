---
description: "A causal question is framework-contested when two consistent perspectives predict opposite signs; LLM accuracy is lower on such items, and lower still when the truth sides with the market."
aliases: ["ideology-contested items", "ideology-contested triplets", "perspective-divergent causal sign", "intervention-truth versus market-truth items"]
sources: ["doi-10-48550-arxiv-2604-21334"]
---
# Framework-contested ground truth

Some causal questions have a sign that the evidence does not fix until a framework is chosen. Two internally consistent accounts of which mechanism dominates can predict opposite signs for the same policy and outcome. The paper calls these items ideology-contested, meaning "instances where intervention-oriented (progovernment) and market-oriented (pro-market) perspectives predict divergent causal signs."[^c1] Its example is a minimum wage increase, which a market framing expects to reduce hiring, while an intervention framing can read it "to sustain employment under an intervention-oriented framework".[^c2] The two accounts differ in how they weigh the same policy's labour-cost effect against its demand or job-matching effects.

The contest belongs to the question, and in this work it is found by asking models rather than experts. Four LLMs were queried once per triplet, blind to the published result, for an intervention-oriented sign and a market-oriented sign. A triplet entered the contested set only when at least three of the four models "assigned different signs to the two perspectives", and the majority signs for the two sides then decided whether the item was contested.[^c3] The corpus is "10,490 context-annotated causal triplets derived from top-tier economics" journals.[^c4] The procedure "yields 1,056 ideology-contested triplets (10.1% of the full set)".[^c5] Two economics professors then reviewed a subset of 126, and "inter-rater agreement reached 93.33%".[^c6][^c7]

Once the contest is fixed, reliability splits by side. Across models, the contested items were harder than the rest: closed-source models "average 61.3% on ideology-contested items versus 74.5% on non-contested items".[^c8] Within the contested set, items whose ground truth matched the intervention side were answered better than those matching the market side. Closed-source models averaged "72.9% on intervention-truth items but only 63.1% on market-truth items", a gap of +9.7 points, and open-source models show a wider one.[^c9] Eighteen of the 20 models show the positive gap: "Of the 20 models, 18 exhibit a positive" value.[^c10]

The gap is not explained by item difficulty, on the paper's check. Matching intervention-truth and market-truth items one to one within theme and difficulty cell left the gap largely unchanged, and the authors conclude that the asymmetry "is therefore not attributable to differential item difficulty".[^c11]

What the contest changes for asking. The paper argues that a single score hides the structure: "aggregate accuracy alone is an insufficient metric for evaluating" LLMs in economic analysis, because a model "can achieve reasonable average performance while masking large directional disparities within ideologically contested cases."[^c12][^c13] On this reading the unit of reliability is the side the truth falls on, not the item taken alone. My inference, which the paper does not test: for a framework-dependent question, one accuracy number averages two different reliabilities, so the report should give one per side.

Mechanism. The paper does not isolate a single cause. Its base-model result points to a source before tuning: "A potential source of this directional tendency may lie in pretraining".[^c14] Instruction tuning did not remove the gap in Qwen 3-8B; it "substantially widens both the accuracy gap" and the directional bias.[^c15] The authors' summary is that the pattern arises from an interaction of pretraining, alignment and the empirical literature the models learned from.

## Limits

- The contest is produced by model judgments. Four LLMs set the two framing signs by majority, so a framing that all four share would never register as contested. The expert check covers 126 of the 1,056 items and tests the stability of the labels, not whether these two framings are the ones an economist would pick (my inference).
- The side gap and the base rate are not separated. The ground-truth labels "lean toward" the intervention side, 58.1% against 41.9%, and the models' average predictions "closely track this base rate".[^c16][^c17] A model that favours the majority sign would show the same side gap with no ideology in it. The difficulty check does not address this, and the paper does not test it.
- The truth side comes from published estimates. The authors concede that "heterogeneity may themselves generate distributional skew in the benchmark", and that "the published literature may still reflect selection in which questions".[^c18][^c19]
- The paper does not establish ideology as the cause: "these results do not imply that the observed bias reflects ideological preference alone".[^c20]
- A correct answer on a contested item may be recall of the paper rather than reasoning across frameworks: the authors say models "may do so either by recalling paper-specific empirical claims".[^c21]
- The pattern is not universal. "The Claude family is a notable exception", with a slight market-truth advantage for Sonnet 4.6 and Opus 4.6.[^c22] The study is one benchmark, one domain, and one snapshot of 20 models.

## Related

- [[error-direction-versus-magnitude]] — the signed-error idea, here applied to a two-sided sign with a directional error bias
- [[shared-error-pattern]] — errors shared by most judges versus packed into a subgroup; the side gap is a subgroup-shaped pattern
- [[difficulty-enriched-item-sampling]] — the item-difficulty confound that the paper's matching is meant to rule out
- [[epistemic-framework-routing]] — choosing a reasoning framework before answering; on these items the framework chosen decides the truth side
- [[default-tone-skew]] — another default lean in LLM outputs, measured on a different axis

[^c1]: doi-10-48550-arxiv-2604-21334 — "perspectives predict divergent causal signs"
[^c2]: doi-10-48550-arxiv-2604-21334 — "to sustain employment under an intervention-oriented framework"
[^c3]: doi-10-48550-arxiv-2604-21334 — "models assigned different signs to the two perspectives"
[^c4]: doi-10-48550-arxiv-2604-21334 — "of 10,490 context-annotated causal triplets derived from top-tier economics"
[^c5]: doi-10-48550-arxiv-2604-21334 — "This procedure yields 1,056 ideology-contested triplets (10.1% of the full set)"
[^c6]: doi-10-48550-arxiv-2604-21334 — "Two economics professors independently reviewed a representative"
[^c7]: doi-10-48550-arxiv-2604-21334 — "inter-rater agreement reached 93.33%"
[^c8]: doi-10-48550-arxiv-2604-21334 — "models average 61.3% on ideology-contested items versus 74.5% on non-contested items"
[^c9]: doi-10-48550-arxiv-2604-21334 — "72.9% on intervention-truth items but only 63.1% on market-truth items"
[^c10]: doi-10-48550-arxiv-2604-21334 — "Of the 20 models, 18 exhibit a positive"
[^c11]: doi-10-48550-arxiv-2604-21334 — "is therefore not attributable to differential item difficulty"
[^c12]: doi-10-48550-arxiv-2604-21334 — "aggregate accuracy alone is an insufficient metric for evaluating"
[^c13]: doi-10-48550-arxiv-2604-21334 — "masking large directional disparities within ideologically contested cases"
[^c14]: doi-10-48550-arxiv-2604-21334 — "A potential source of this directional tendency may lie in pretraining"
[^c15]: doi-10-48550-arxiv-2604-21334 — "it substantially widens both the accuracy gap"
[^c16]: doi-10-48550-arxiv-2604-21334 — "the ground-truth labels themselves lean toward"
[^c17]: doi-10-48550-arxiv-2604-21334 — "predictions closely track this base rate"
[^c18]: doi-10-48550-arxiv-2604-21334 — "heterogeneity may themselves generate distributional skew in the benchmark"
[^c19]: doi-10-48550-arxiv-2604-21334 — "the published literature may still reflect selection in which questions"
[^c20]: doi-10-48550-arxiv-2604-21334 — "these results do not imply that the observed bias reflects ideological preference alone"
[^c21]: doi-10-48550-arxiv-2604-21334 — "they may do so either by recalling paper-specific empirical claims"
[^c22]: doi-10-48550-arxiv-2604-21334 — "The Claude family is a notable exception"
