---
description: "A forced-best-guess-after-abstention protocol scores abstention as a classifier for eventual error, summarized by Youden's J over its sensitivity and specificity."
aliases: ["I-CALM two-stage evaluation protocol", "Jabs", "abstention informedness", "error capture rate", "correct answer retention", "ECR", "CAR"]
sources: ["arxiv-2604-03904"]
---
# Abstention informedness

> A lower error rate among the answers a model actually surfaces proves
> nothing on its own — it might just be refusing everything. Force a
> guess out of every abstention, then score the abstain decision itself
> as a classifier for whether that guess would have been wrong.

## Definition / Mechanism

Zong et al. note that "a lower false-answer rate among answered questions
is not, by itself, sufficient evidence of better abstention: a model can
reduce the risk of surfaced answers simply by refusing more often."[^c1]
Their two-stage protocol separates the [[abstention]] decision from its
correctness readout: Stage 1 lets the model answer or abstain on the
question as usual; for every question it abstains on, Stage 2 forces a
best guess it is not allowed to withhold, "This allows us to estimate
whether abstentions are concentrated on questions that would otherwise
have been answered incorrectly, while also measuring how often correct
answers are unnecessarily withheld."[^c2]

Treating the abstention decision as a prediction that the eventual
candidate answer is wrong turns it into a binary classifier, scored by
its sensitivity and specificity: the **error capture rate**
$\mathrm{ECR}=P_n(S=0\mid C=0)$ is the fraction of eventual errors an
abstention intercepted, and the **correct answer retention**
$\mathrm{CAR}=P_n(S=1\mid C=1)$ is the fraction of eventual correct
answers the model still surfaced. The two are combined into one
number by Youden's J: "$J_{abs}=\mathrm{ECR}+\mathrm{CAR}-1
=P_n(S=0\mid C=0)-P_n(S=0\mid C=1)\in[-1,1]$. A value of 1 denotes
perfect targeting of erroneous candidates, 0 denotes no population-level
association between abstention and eventual correctness, and positive
values indicate that the policy abstains more frequently on erroneous
than correct candidates."[^c4]

## Why it matters

$J_{abs}$ is what lets the paper distinguish a policy that abstains
*more* from one that abstains *better*: coverage and the surfaced
false-answer rate alone cannot separate targeted abstention from
indiscriminate refusal, because a policy that always abstains drives the
surfaced-answer error rate to zero while capturing no information about
which candidates were actually wrong. Scoring every ablation and every
baseline in the paper by $J_{abs}$ is what supports its component-level
claims (e.g. that a given change moved the model toward broader
withholding rather than sharper targeting).

## Limits

- The forced Stage-2 guess is elicited by an explicit second prompt, not
  a spontaneous behavior; a model primed to expect a forced follow-up
  might behave differently at Stage 1 than one that is not, and the
  paper does not report testing for this.
- $J_{abs}$ collapses two rates (ECR, CAR) into one scalar; two policies
  with the same $J_{abs}$ can trade sensitivity for specificity
  differently, so the protocol's per-run ECR/CAR pair carries information
  the single number discards.
- Defined only for the paper's own two-stage design on short-answer
  factual QA with one verifiable answer per question; the note does not
  establish how it composes when abstention itself is graded rather than
  binary, or when a question has no single reference answer.

## Related

[[abstention]] · [[i-calm]] · [[two-stage-abstention-paradigm]] · [[score-separability]] · [[calibration]]

[^c1]: arxiv-2604-03904 — "a lower false-answer rate among answered questions is not, by itself, sufficient evidence of better abstention: a model can reduce the risk of surfaced answers simply by refusing more often"
[^c2]: arxiv-2604-03904 — "This allows us to estimate whether abstentions are concentrated on questions that would otherwise have been answered incorrectly, while also measuring how often correct answers are unnecessarily withheld."
[^c4]: arxiv-2604-03904 — "Jabs = ECR + CAR − 1 = Pn (S = 0 | C = 0) − Pn (S = 0 | C = 1) ∈ [−1, 1]. A value of 1 denotes perfect targeting of erroneous candidates, 0 denotes no population-level association between abstention and eventual correctness, and positive values indicate that the policy abstains more frequently on erroneous than correct candidates."
