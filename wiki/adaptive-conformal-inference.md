---
description: "Adaptive Conformal Inference nudges the miscoverage level after each observed miss, giving long-run average coverage under arbitrary drift with no exchangeability; the guarantee is asymptotic."
aliases: ["ACI", "adaptive conformal prediction", "online conformal recalibration", "Gibbs-Candès adaptive conformal"]
sources: ["arxiv-2511-18225"]
---
# Adaptive conformal inference

Split [[conformal-prediction]] fixes one miscoverage level and one calibration set, and its coverage statement rests on exchangeability. Adaptive conformal inference (ACI) replaces the fixed level with a state that moves. Before each test point it picks a miscoverage level α_i and builds the prediction set at that level. When the true outcome is revealed it checks whether the set covered it, then moves the level by a step γ: a miss lowers α (the set widens), a hit raises it. The update is stated as "the update to the miscoverage level is"[^c1], and the newly observed pair is appended to the calibration set "to inform future prediction sets", so the set keeps being refit as data arrive.[^c2]

The mechanism is a feedback loop on the running error rate, not a model of the shift. The paper bounds the average miscoverage over N test points by a quantity that shrinks as N grows, and says that this "bounds the difference between the average observed miscoverage and the target miscoverage".[^c3] Taken as displayed, the right-hand side is of order 1/(Nγ), so the empirical miscoverage rate converges to the target: "the average miscoverage rate converges almost surely to the desired target".[^c4] The argument works because the adaptive level "is proven to remain within a bounded interval" [−γ, 1 + γ].[^c5] In my reading, that boundedness is what stops the update from running away when the score distribution moves. Because the argument uses the sequence of errors and the bounded level rather than the joint law of the data, the paper can say: "These guarantees do not depend on exchangeability."[^c6]

The step size sets the trade-off. Choosing γ = 0 recovers the online variant with an updating calibration set.[^c7] The paper's own statement of the trade-off is that "the coverage becomes too volatile; if it is too low, the system will not adapt fast enough to the changes in" the distribution.[^c8] In the paper's hardware experiment, the adaptive version with γ = 0.03 "consistently maintains coverage closer to the nominal level than the online QCP" variant.[^c9] The contrast here is between two online procedures with the same score, not between ACI and a static conformal set on drifting data.

## Limits

- The guarantee is asymptotic in the number of test points: "guarantees are asymptotic in the number of test points."[^c10] The finite-sample result the paper adapts from Gibbs and Candès needs i.i.d. pairs and a hidden Markov structure, and the paper concedes that "the assumptions required by this theorem are unlikely to hold exactly in our setting."[^c11]
- The guarantee is about the long-run average of errors. It says nothing about any single window or any conditional set. The paper's local-coverage plots are moving averages, which is an empirical view, not a theorem.[^c12] An average can sit at 1 − α while particular regions are over- or under-covered; this is my inference from the form of the bound, and the paper does not test it.
- ACI needs each outcome revealed before the next prediction: "AQCP is inherently sequential: it updates the miscoverage level using observed outcomes".[^c13] The paper says it is therefore "not directly applicable in batch prediction settings."[^c14] Where only emitted answers are observed, the wiki's [[emit-only-feedback-obstruction]] note reports ACI missing its target, so the feedback model matters as much as the update rule.
- The step size was fixed at γ = 0.03, and the paper names "a systematic step-size sensitivity analysis" as future work.[^c15]
- The hardware evidence comes from one day of runs, which "does not fully characterise longer-term drift or more structured perturbations."[^c16] The paper also declines to attribute the difference between QCP and AQCP stability to noise: "since fluctuations are expected when testing with finite samples."[^c17]

## Related

- [[conformal-prediction]] — the static, exchangeability-based guarantee that ACI relaxes.
- [[time-dependent-conformity-scores]] — the score-level drift that motivates the adaptive update in this paper.
- [[time-uniform-conformal-prediction]] — anytime validity under i.i.d. data; ACI instead gives asymptotic average coverage with no i.i.d. assumption.
- [[training-conditional-cumulative-regret]] — ACI's average-coverage check cannot see vacuous sets; a per-round regret can.
- [[emit-only-feedback-obstruction]] — ACI when the feedback reveals only emitted answers.

[^c1]: arxiv-2511-18225 — "the update to the miscoverage level is"
[^c2]: arxiv-2511-18225 — "appends the newly observed point"
[^c3]: arxiv-2511-18225 — "This bounds the difference between the average observed miscoverage and the target miscoverage"
[^c4]: arxiv-2511-18225 — "the average miscoverage rate converges almost surely to the desired target"
[^c5]: arxiv-2511-18225 — "is proven to remain within a bounded interval"
[^c6]: arxiv-2511-18225 — "These guarantees do not depend on exchangeability."
[^c7]: arxiv-2511-18225 — "Choosing γ = 0 recovers QCP with an updating calibration set."
[^c8]: arxiv-2511-18225 — "the coverage becomes too volatile; if it is too low, the system will not adapt fast enough to the changes in"
[^c9]: arxiv-2511-18225 — "consistently maintains coverage closer to the nominal level than the online QCP"
[^c10]: arxiv-2511-18225 — "guarantees are asymptotic in the number of test points"
[^c11]: arxiv-2511-18225 — "the assumptions required by this theorem are unlikely to hold exactly in our setting"
[^c12]: arxiv-2511-18225 — "Moving average coverage of AQCP"
[^c13]: arxiv-2511-18225 — "AQCP is inherently sequential: it updates the miscoverage level using observed outcomes"
[^c14]: arxiv-2511-18225 — "not directly applicable in batch prediction settings"
[^c15]: arxiv-2511-18225 — "a systematic step-size sensitivity analysis"
[^c16]: arxiv-2511-18225 — "does not fully characterise longer-term drift or more structured perturbations"
[^c17]: arxiv-2511-18225 — "since fluctuations are expected when testing with finite samples"
