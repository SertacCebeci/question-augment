---
description: "A rubric judge that returns correct, missing or wrong, scoring omission at zero and error at negative, separates leaving content out from asserting falsehood; a binary verdict cannot."
aliases: ["three-state criterion scoring", "correct-missing-wrong verdict", "negative credit for errors", "omission versus error scoring"]
sources: ["openalex-org-w7202416508"]
---
# Three-state criterion scoring

A rubric judge can answer one of two ways per criterion: satisfied or not, or one of three verdicts, correct, missing, or wrong. The three-state form gives correct +1, missing 0, and wrong −1. What it encodes is a difference between two ways of failing a criterion. A response that leaves a point out has said nothing false about it; a response that asserts the opposite has. A binary reward gives both the same zero. In the authors' words, "Because missing and incorrect content both receive no" credit, so the reward "cannot distinguish omission from an incorrect assertion about the same criterion."[^c1] The three-state judge is built to make that split. Its wrong verdict is kept narrow: it is "reserved for a factual error, fabrication, contradiction, reversal, or substitution concerning the criterion," and "imprecision alone is not automatically wrong."[^c2]

The mechanism works through the reward, not through the judge's accuracy. A missing criterion costs nothing, so a response is never penalised for a point it did not try to make. A wrong criterion subtracts, so a response that adds a false claim can end up below one that adds nothing. Under binary scoring, the more content a response contains, the more criteria it can hit. The authors name this as a route to reward hacking: "a longer answer can mention content associated with more criteria and accumulate more positive" credit, whether or not the added content is supported.[^c3] Negative credit removes that gain, since the same length now carries a risk of −1 per error.

The measured effect is on medical benchmarks. With consensus criteria held fixed, moving from binary to three-state scoring raised the medical average from 49.26 to 51.51, with gains of 3.69 points on HealthBench-Hard and 6.80 on PubMedQA.[^c4] The generalization scores changed little or fell.[^c5] The binary runs reached a higher training reward, 0.780–0.802 against 0.751–0.753, yet under the matched setting they ended with the lower medical average.[^c6] So the reward level is not the quality measure, and a rubric's reward can rise while the policy gets worse.

## Limits

The comparison is one ablation on one training seed; the paper states that "All policy comparisons use one training seed." The three-state gain is shown on medical benchmarks only, and the generalization scores did not move with it. The line between wrong and imprecise is drawn by a judge prompt, and nothing in the parts I read checks that two judges, or a clinician, draw it the same way (my inference from what is reported). Omissions are scored as neutral, so a response is never rewarded for leaving out a point it should have made; the scheme trades that for not penalising silence (my inference). The method says nothing about whether the criteria themselves are the right ones; that is the rubric's problem, not the judge's.

## Related

- [[rubric-presence-absence-asymmetry]] — rubric reward is mostly presence-based; three-state scoring is a separate question, about what a failed criterion means, and the two can be combined.
- [[violation-enumerated-rubric-verdict]] — another way to give a rubric verdict error information: an item counts as met only if the grader lists no violated guideline.
- [[false-credit-propagation]] — a flat rubric sum can credit a criterion whose licensing condition is absent; the negative sign here is a deliberate penalty for error, not a condition check.
- [[constitutive-rubric-criteria]] — whether a judge can grade a criterion from the rubric and response alone is orthogonal to how many verdicts it returns.
- [[pairwise-judge-over-scalar-reward]] — the scalar reward this scheme produces is what the pairwise step later acts on when it ties.

[^c1]: openalex-org-w7202416508 — "Because missing and incorrect content both receive no"
[^c2]: openalex-org-w7202416508 — "reserved for a factual error, fabrication, contradiction, reversal, or substitution concerning the criterion"
[^c3]: openalex-org-w7202416508 — "a longer answer can mention content associated with more criteria and accumulate more positive"
[^c4]: openalex-org-w7202416508 — "Keeping Consensus Rubrics fixed, Three-State scoring raises the medical average by 2.25 points, from 49.26 to"
[^c5]: openalex-org-w7202416508 — "the three generalization scores change little or decline"
[^c6]: openalex-org-w7202416508 — "they obtain a lower medical"
