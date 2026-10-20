---
description: "Exact-match accuracy counts every scoring error alike, while quadratic weighted kappa penalizes a score by its distance from the expert score, so the two can diverge."
aliases: ["quadratic weighted kappa", "QWK", "weighted kappa", "accuracy versus QWK"]
sources: ["doi-10-35377-saucis-1835608"]
---
# Exact-match agreement versus weighted agreement

A scorer compared with expert scores can be summarized in two ways that answer different questions. Exact-match accuracy asks whether the score is the same. Quadratic weighted kappa (QWK) asks how far apart the scores are, and it counts a disagreement by its size. The Turkish short-answer study names the difference in measurement terms: "accuracy treats all errors equally."[^e1] Under accuracy, a response that is a 4 but is scored 0 "is penalized the same as a minor deviation (Score 3)."[^e2] Weighted kappa is the study's answer to that: it "accounts for the severity of the disagreement between the predicted score and the ground truth."[^e3]

The two statistics do diverge on the same scorer. On Q1, accuracy ran "from 0.48 to 0.85", while QWK ran "from 0.15 to 0.66".[^e4][^e5] The authors read the high QWK values on the multi-level item as showing that most errors were "near-misses" (adjacent categories) "rather than random or gross failures."[^e6] Their pedagogical reading is that a scorer may be weak at exact grading in borderline cases and still "capture the ordinal progression of student proficiency."[^e7]

Two mechanics, both my inference from the standard quadratic weight and not stated in the sections read. First, with quadratic weights a miss of four levels costs sixteen times a miss of one level, so a scorer whose errors are adjacent keeps QWK high while its exact-match rate stays modest. Second, for a binary item the quadratic weights reduce to the unweighted case, so QWK on Q1 is the chance-corrected agreement of the two categories. The gap between Q1 accuracy and Q1 QWK there comes from the chance correction and the label balance, not from near-misses. The study's near-miss reading applies only to the multi-level item.

## Limits

- The near-miss claim is the authors' reading of high QWK. The sections read give no count of adjacent-category errors, so the claim that most errors were adjacent is not measured directly here.
- The quadratic weight is a convention. It fixes which errors count as small; a linear or domain-specific weight would rank the same errors differently, and the study does not compare them.
- High weighted agreement is not decision consistency. The authors say the models "show relative consistency but have limited absolute decision consistency," so a good QWK can sit beside many exact misses.[^e8]
- The label distribution shapes both statistics. On Q2, 71 of 145 responses are at score 0, so kappa-type measures are sensitive to how the rare middle scores are distributed. The study does not report a chance baseline for either statistic in the sections read.
- Both statistics measure agreement with one expert score set, which the study takes as ground truth.

## Related

- [[intermediate-score-error-peak]] — where on the scale the misses fall; adjacent misses at the middle are the ones weighted agreement forgives most
- [[error-direction-versus-magnitude]] — a second summary that hides structure, here the sign of error rather than its size
- [[temperature-scaled-deferral-gate]] — a deferral threshold that trades coverage for QWK on the answers it keeps

[^e1]: doi-10-35377-saucis-1835608 — "accuracy treats all errors equally"
[^e2]: doi-10-35377-saucis-1835608 — "misclassifying a high-scoring response (Score 4) as completely incorrect (Score 0) is penalized the same as a minor deviation (Score 3)"
[^e3]: doi-10-35377-saucis-1835608 — "it accounts for the severity of the disagreement between the predicted score and the ground truth"
[^e4]: doi-10-35377-saucis-1835608 — "Accuracy rates for Q1 range from 0.48 to 0.85."
[^e5]: doi-10-35377-saucis-1835608 — "QWK values for Q1 range from 0.15 to 0.66."
[^e6]: doi-10-35377-saucis-1835608 — "rather than random or gross failures"
[^e7]: doi-10-35377-saucis-1835608 — "they can still capture the ordinal progression of student proficiency"
[^e8]: doi-10-35377-saucis-1835608 — "the models show relative consistency but have limited absolute decision consistency"
