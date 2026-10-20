---
description: "Signed score over pro- and anti-stereotypical versions of one item: 0 when both get the same answer, +1 when answers follow the stereotype, -1 when they run against it; accuracy gaps are a companion."
aliases: ["BBQ bias score", "complete-set bias score", "pro-anti bias score", "pro-anti accuracy difference"]
sources: ["doi-10-48550-arxiv-2205-11605"]
---
# Paired stereotype bias score

Accuracy alone cannot show bias. A model can be right on most items and still answer stereotypically on the rest, and a model can be wrong in a way that is unrelated to any group. Parrish et al. (2021) proposed a bias score for this reason, and Akyürek et al. adopt it: "Because accuracy falls short of capturing the bias" in predictions "beyond those that are answered correctly."[^c1]

The score is computed over pairs of versions of the same item. In BBQ, an ambiguous context is paired with a negative and a non-negative question, and the answers are compared with the stereotype's target and non-target groups. Akyürek et al. extend the construction to NLI, where pro-stereotypical and anti-stereotypical versions of one example differ by swapping the groups: the pro and anti versions "of the same example are obtained by swapping" the target and non-target groups.[^c2] The score for the complete set of an example is signed. It "evaluates to 1 when" the answer to the pro-stereotypical version is yes and to the anti-stereotypical version is no; it is -1 in the opposite case, and 0 when the predictions are the same.[^c3] Scores "can take values between -1 and 1 for the complete set of an example."[^c4] In the tables they multiply by 100, following Parrish et al.[^c5]

Two properties follow from the definition. First, an answer that is the same for the pro and anti versions contributes nothing, whatever it is. Second, a forced choice is what creates the score, because the preferred answer to these stereotype hypotheses is "exclusively neutral."[^c6] A model that abstains on both versions scores 0, while one that picks the group the stereotype names scores positive. The authors describe the same failure as one where T0 "fails to remain abstained," My inference is that the score tracks abstention as much as group preference.[^c12] My inference: a low score can mean either unbiased answering or consistent abstention, and only the accuracy alongside it tells them apart.

For disambiguated BBQ items, the score is anchored to accuracy: "Note that 100% mean accuracy results in a bias score of 0."[^c7] Because a wrong answer on a disambiguated item also moves the score, the authors add a companion measure, the difference between accuracy on pro-stereotypical and anti-stereotypical versions. They say that this "is an alternative indicator of biases exhibited by the model."[^c8] A higher accuracy on the stereotype-consistent version is read as a form of allocational bias, which the authors cite from Blodgett et al.: the model's better handling of pro-stereotypical scenarios "suggests another form of bias," which the authors "called allocational bias (Blodgett et al., 2020)."[^c9] On the disambiguated items the accuracy gap reproduces the ordering of the bias score, with QA more biased than NLI "when accuracies are similar."[^c10]

## Limits

- The score is a property of the answer distribution, not of truth. Zero means consistent answers across the pair, which may be consistent abstention or consistent error.
- The authors' tables report one model (T0pp) with five sampled predictions per example. The variance of the score across seeds is not reported; the seed-spread question is treated in [[multi-seed-bias-score-averaging]].
- Scale is a convention: the numbers are multiplied by 100, so a value of 43 is not a probability and cannot be compared with scores from another paper that uses a different scale.
- The accuracy gap is only a companion. The authors call it "an alternative indicator," and they do not show that it measures the same construct as the bias score.
- The BBNLI pairs are hand-written and filtered by the authors, so the score measures the stereotypes the authors chose.[^c11]

## Related

- [[trained-task-form-bias-gap]] — the gap in this score between the QA and NLI forms
- [[multi-seed-bias-score-averaging]] — the seed variance this score's single-run reporting leaves out
- [[masking-vs-mitigating-bias-reduction]] — an aggregate bias score can fall for reasons that are not mitigation
- [[answer-format-dependent-bias-measurement]] — the answer format of the instrument changes what the score reports
- [[short-form-check-blindness-to-open-ended-bias]] — forced-choice scores can miss stereotypes that appear in open-ended answers

[^c1]: doi-10-48550-arxiv-2205-11605 — "Because accuracy falls short of capturing the bias"
[^c2]: doi-10-48550-arxiv-2205-11605 — "of the same example are obtained by swapping"
[^c3]: doi-10-48550-arxiv-2205-11605 — "bias score evaluates to 1 when"
[^c4]: doi-10-48550-arxiv-2205-11605 — "this paper can take values between -1 and 1 for the"
[^c5]: doi-10-48550-arxiv-2205-11605 — "scores by 100 following Parrish et al. (2021)."
[^c6]: doi-10-48550-arxiv-2205-11605 — "this dataset is exclusively neutral."
[^c7]: doi-10-48550-arxiv-2205-11605 — "that 100% mean accuracy results in a bias score of 0."
[^c8]: doi-10-48550-arxiv-2205-11605 — "This metric is an alternative indicator of biases exhibited by the model"
[^c9]: doi-10-48550-arxiv-2205-11605 — "called allocational bias (Blodgett et al., 2020)."
[^c10]: doi-10-48550-arxiv-2205-11605 — "bias than NLI when accuracies are similar."
[^c11]: doi-10-48550-arxiv-2205-11605 — "not able to include every ethnicity, gender, and religious point of view."
[^c12]: doi-10-48550-arxiv-2205-11605 — "T0 fails to remain abstained and almost always makes a choice between"
