---
description: "In medical MCQA, adding an explicit abstain option widens conformal prediction sets far more than adversarial perturbation does, while scale and chain-of-thought barely help abstention."
aliases: ["MedAbstain", "abstention-aware uncertainty inflation", "explicit abstention option effect"]
sources: ["arxiv-2601-12471"]
---
# Abstention-option uncertainty inflation

MedAbstain evaluates medical multiple-choice QA (MedQA, AMBOSS) in four variants of each question: the original (NA), one with an added "abstain" option at a random position (A), one with an adversarially perturbed question (NAP), and both (AP). Uncertainty is measured through the size of [[conformal-prediction]] sets (LAC and APS scores), which works for black-box models. Accuracy and abstention rate are tracked beside it.[^c1]

## What was measured

Offering the abstention option raises set size across nearly all models. The paper reports that "abstention, rather than perturbation, is the primary driver of model uncertainty."[^c2] The AP variant gives the largest increase, A comes next, and NAP gives a much smaller one, often near zero for APS. Accuracy moves little: the A-versus-NA accuracy change is about zero on AMBOSS, and the AP-versus-NA change is the most negative, though modest.[^c3]

So the option works as a prompt for the model to reconsider its confidence, not as a harder question. Set size rises together with abstention rate, which the authors read as uncertainty acting as a signal the model can use to abstain.[^c4]

The headline negative result is that high-accuracy models "often fail to abstain with uncertain" inputs, and that "scaling model size or advanced prompting brings little improvement."[^c1] Chain-of-thought did not reduce the inflation, "indicating that explicit reasoning does not reduce the model's uncertainty."[^c5] Few-shot prompting had only a small effect on abstention and uncertainty.[^c6]

An exception is GPT-4.1, where accuracy and set size both rose from NA to A. The authors say this implies different calibration and "demanding further investigation."[^c7]

## Limits

- Only multiple-choice medical QA was tested. The claim that it generalizes to agentic action selection is the authors' and was not tested here.
- Set size is a proxy for uncertainty, not a measure of whether abstention was correct. Whether the widened sets coincide with the questions a model should decline is not shown by the quoted passages (my reading).
- Perturbations were adversarial rewrites of the question. Other stressors, such as missing information, were not compared.
- The GPT-4o and GPT-4.1 families break the pattern, so it is not universal.

## Related

- [[abstention]] — the general behavior this benchmark probes
- [[conformal-abstention]] — a different use of conformal methods, thresholding an uncertainty score to guarantee correctness
- [[conformal-prediction]] — the set-size uncertainty measure
- [[calibration]] — the GPT-4.1 exception is described as a calibration difference

[^c1]: arxiv-2601-12471 — "high-accuracy models often fail to abstain with"
[^c2]: arxiv-2601-12471 — "suggesting that abstention, rather than perturbation, is the primary driver of model uncertainty."
[^c3]: arxiv-2601-12471 — "δAcc(A − N A) ≈ 0"
[^c4]: arxiv-2601-12471 — "The direct correlation between the abstention"
[^c5]: arxiv-2601-12471 — "indicating that explicit"
[^c6]: arxiv-2601-12471 — "Few-shot seems to have a negligible impact on abstention and uncertainty"
[^c7]: arxiv-2601-12471 — "demanding"
