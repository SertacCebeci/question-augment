---
description: "Treating explanation mentions as a classifier of impactful interventions makes correlation depend on class balance and favor concise text; F-AUROC over length-instruction settings removes both."
aliases: ["F-AUROC", "faithfulness AUROC", "faithfulness as classification"]
sources: ["doi-10-48550-arxiv-2503-13445"]
---
# Verbosity-controlled faithfulness AUROC

Frame a counterfactual faithfulness test as classification: whether an inserted word changed the model's prediction is the ground truth, and whether the explanation mentions it is the classifier's prediction. True and false positive rates then expose a tradeoff between comprehensiveness (mention many) and specificity (mention few).[^c1]

Correlation-based scores depend on the class balance. With k the ratio of impactful to non-impactful interventions, the phi-CCT is a function of TPR, FPR and k; when impactful interventions are rare, a classifier needs very low FPR to score high regardless of TPR.[^c2] In practice only 1.4% of interventions changed Qwen's predicted class on ComVE, so correlation penalized false positives more than false negatives and rated concise explanations as more faithful than comprehensive ones.[^c3] Verbosity thus moves the score without changing what the model knows about its own decision.

F-AUROC fixes this by prompting the same model with several length instructions ("very concise" to "very comprehensive", plus empty), taking the area under the convex hull of the resulting (FPR, TPR) points plus the trivial corners. It is no more than 0.5-gameable, the minimum possible value.[^c4] It needs no token probabilities, so it applies to proprietary models.[^c5]

Measured over 75 models from 13 families: faithfulness rises with size within a family and with task accuracy, and F-AUROC has the strongest association with accuracy.[^c6] Instruction-tuning gave control over verbosity but did not clearly expand the sensitivity-specificity frontier.[^c7]

## Limits

- The stronger F-AUROC link to accuracy is read by the authors as reduced noise; that is their interpretation, not a test of validity against a ground truth of faithfulness.
- Tasks are "natural" commonsense tasks, where plausibility and faithfulness likely do not conflict; the authors flag that adversarial or hidden-reasoning settings are untested.[^c8]
- Random word insertions after naturalness filtering define impact; other intervention types were not studied.
- The hull assumes the thresholds are attainable by the model; a model ignoring length instructions yields a degenerate hull (my reading).

## Related

- [[alpha-gameability-of-faithfulness-metrics]] — the formal criterion F-AUROC is checked against
- [[capability-auditability-tradeoff]] — scale and capability versus the ability to audit
- [[hint-adherence-without-acknowledgement]] — mention-versus-influence gap in explanations
- [[extractive-abstractive-verifiability-tradeoff]] — another conciseness-versus-checkability tradeoff

[^c1]: doi-10-48550-arxiv-2503-13445 — "this framing highlights the tradeoff between comprehensiveness and"
[^c2]: doi-10-48550-arxiv-2503-13445 — "a classifier must achieve very low FPR to attain high correlation, regardless of TPR."
[^c3]: doi-10-48550-arxiv-2503-13445 — "where only 1.4% of interventions change Qwen’s predicted class."
[^c4]: doi-10-48550-arxiv-2503-13445 — "Theorem 4. F-AUROC is no more than 0.5-gameable on any dataset."
[^c5]: doi-10-48550-arxiv-2503-13445 — "Because F-AUROC doesn’t require"
[^c6]: doi-10-48550-arxiv-2503-13445 — "F-AUROC has the highest association, suggesting that its lack of sensitivity to"
[^c7]: doi-10-48550-arxiv-2503-13445 — "it doesn’t clearly expand the frontier of sensitivity vs. specificity"
[^c8]: doi-10-48550-arxiv-2503-13445 — "for an accurate model, there is likely no conflict between"
