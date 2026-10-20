---
description: "Supervising on the annotator label distribution instead of the majority label makes accuracy and distributional fit separate objectives that can trade off against each other in ensemble training."
aliases: ["soft labels", "soft target", "annotator label distribution", "label distribution learning", "perspectivist supervision"]
sources: ["doi-10-1007-s13222-026-00529-9", "doi-10-48550-arxiv-2209-03392"]
---
# Annotator distribution as target

Several annotators label one item and disagree. The conventional pipeline reduces them to one hard label by majority vote, and the authors' point is that this removes supervision: "Conventional approaches typically collapse these disagreements into a single ground truth, thereby discarding".[^c1] The alternative keeps two targets for the same item. The hard label is the majority vote, used to measure accuracy. The soft label is "normalised empirical class distributions encoding annotator disagreement".[^c2]

The mechanism is that a classifier is then scored on two axes that the hard label cannot both express. Accuracy is measured against the majority class. Calibration (cross-entropy) and distributional fit (Manhattan distance between predicted and empirical annotator distributions) are measured against the full spread of annotator choices. In MO-WEL the ensemble weights are optimised against "three complementary losses: F1 score, cross-entropy and" Manhattan distance, plus a regulariser.[^c3] The paper gives the choice of L1 distance as a reason: it "provides an interpretable, class-wise measure of distributional misalignment".[^c4]

The two axes pull against each other, and the paper reports this as a measured pattern rather than a side remark. In the ablation on ArMIS and MD-Agreement, each loss alone was compared against combinations. The authors summarise that "LCE reduces calibration error, and LMD enhances alignment with" annotator distributions, and that "optimising all three may introduce conflicts that slightly reduce performance."[^c5] Across 1295 coefficient settings, the correlation analysis gives the sharper form: the F1 weight "substantially boosts F1 but generally degrades MD", while the MD weight improves distributional alignment "at the cost of reduced F1" (my reading: the MD-favouring setting gives up hard accuracy).[^c6] So an evaluator that reports only F1 can rank a model differently from one that reports MD, and a training run that optimises one moves the other.

The source of the soft target also matters. Two ways of building predictors from the annotation space were compared. Random sampling draws one annotator's label per instance, "generating a pseudo-annotator view".[^c7] Major-contributor sampling trains on "the M most contributing annotators", which uses annotator identity.[^c8] The paper reports that random projections give higher F1 and lower CE, "suggesting that stochastic label projections yield greater predictor diversity", while the major-contributor version gives "stronger MD performance on datasets with highly consistent annotators."[^c9] My inference for a question-answer setting: which annotators supply the target can decide which distributional metric wins.

## Limits

- The ablation is reported for two of the four datasets: "Table 4 reports the results on ArMIS and MD-Agreement."[^c10] The paper then says "Similar patterns are observed on" ConvAbuse and HS-Brexit, but those tables are not the ones shown in the sections I read.
- Hyperparameters were tuned on one dataset: "tuning is conducted on the ConvAbuse dataset".[^c11] The search was small, "10 optimisation trials, after which the best configuration is" selected.[^c12] The same settings were then applied to every dataset.
- Calibration is not improved everywhere. "A slight CE degradation on ConvAbuse and HSBrexit suggests that optimisation prioritises accuracy and" distributional alignment over calibration.[^c13]
- The sections I read report point values in tables and do not show spread across seeds. Differences of a few thousandths in F1 (the regularisation ablation) carry little weight without that. (my reading)
- The distance choice is argued, not tested. The sections I read do not compare L1 against L2 or against cross-entropy on the same predictors, so the claim that L1 is "less dominated by large deviations" is the authors' rationale. (my reading)
- A soft target exists only where several annotations per item exist. The method's gain is measured on that kind of data, not on single-label corpora. (my inference)
- The work is a classification benchmark on short texts; multilabel and multilingual extensions are listed as future work: "Future work will explore extending MO-WEL to multilabel and multilingual settings".[^c14] Whether the same trade-off appears in generation or in answer evaluation was not tested.
- On categorical scoring, a soft-label baseline was weaker in one NLI study: "training with categorical labels performs better"[^c15] in predicting categorical labels. That study is on a different task and architecture, so it bears on the trade-off here only as a neighbouring result.

## Related

- [[structured-annotator-disagreement-on-harm]] — measures what disagreement on harm is made of and shows personalised prediction beats aggregate alignment; this note is about how a model is trained against the distribution and scored on two axes.
- [[rater-effects-latent-score-model]] — corrects for rater differences as latent parameters; here the annotator distribution is itself the target, not a nuisance to remove.
- [[exact-match-versus-weighted-agreement]] — the same split between counting every error alike and penalising by distance; the Manhattan term plays the distance role here.
- [[accuracy-calibration-gradient-conflict]] — another measured conflict between accuracy and calibration, but arising in RLVR gradients rather than in ensemble losses, so the mechanisms differ.
- [[set-valued-disagreement-label]] — the alternative for the same items: output the labels annotators chose as a set, not a distribution or a majority.

[^c1]: doi-10-1007-s13222-026-00529-9 — "Conventional approaches typically collapse these disagreements into a single ground truth, thereby discarding"
[^c2]: doi-10-1007-s13222-026-00529-9 — "Soft labels: normalised empirical class distributions encoding annotator disagreement."
[^c3]: doi-10-1007-s13222-026-00529-9 — "three complementary losses: F1 score, cross-entropy and"
[^c4]: doi-10-1007-s13222-026-00529-9 — "provides an interpretable, class-wise measure of distributional misalignment"
[^c5]: doi-10-1007-s13222-026-00529-9 — "optimising all three may introduce conflicts that slightly"
[^c6]: doi-10-1007-s13222-026-00529-9 — "substantially boosts F1 but generally degrades MD"
[^c7]: doi-10-1007-s13222-026-00529-9 — "generating a pseudo-annotator view"
[^c8]: doi-10-1007-s13222-026-00529-9 — "on the M most contributing annotators"
[^c9]: doi-10-1007-s13222-026-00529-9 — "This leads to stronger MD performance on datasets with highly consistent annotators"
[^c10]: doi-10-1007-s13222-026-00529-9 — "Table 4 reports the results on ArMIS and MD-Agreement."
[^c11]: doi-10-1007-s13222-026-00529-9 — "tuning is conducted on the ConvAbuse dataset"
[^c12]: doi-10-1007-s13222-026-00529-9 — "10 optimisation trials, after which the best configuration is"
[^c13]: doi-10-1007-s13222-026-00529-9 — "A slight CE degradation on ConvAbuse and HSBrexit suggests that optimisation prioritises accuracy and"
[^c14]: doi-10-1007-s13222-026-00529-9 — "Future work will explore extending MO-WEL to multilabel and multilingual settings"
[^c15]: doi-10-48550-arxiv-2209-03392 — "training with categorical labels performs better"
