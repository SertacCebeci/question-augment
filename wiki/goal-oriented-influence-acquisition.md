---
description: "Choosing the next label by its first-order influence on a stated goal functional gives uncertainty-aware acquisition through inverse curvature, with no posterior over parameters."
aliases: ["GOIMDA", "influence-maximizing data acquisition", "goal-oriented influence score"]
sources: ["arxiv-2602-19578"]
---
# Goal-oriented influence acquisition

Most acquisition rules for neural models score a candidate by predictive uncertainty, which is hard to estimate reliably.[^c1] Yao et al. (2026) instead name a goal functional G of the model parameters (test loss, predictive entropy, or the value of a recommended design) and pick the candidate whose labelling most changes G. The change is measured as the instantaneous rate at which upweighting the candidate moves G.[^c2]

## Mechanism

The score combines three parts: the goal gradient, the inverse Hessian of the training loss, and the candidate's sensitivity to the parameters.[^c3] The goal gradient and candidate sensitivity favour exploitation, meaning updates aligned with improving G. The inverse curvature acts as a local uncertainty proxy that favours directions the current data constrains least, which supplies exploration without a Bayesian posterior.[^c3]

For exponential-family models the score factors as a goal-alignment inner product in the curvature geometry times a prediction-bias term, the gap between the model's and the true conditional mean.[^c4] If the model is already right at a candidate, the bias is near zero and the predicted first-order gain is negligible. Large bias steers acquisition toward places where the model is wrong and where parameter updates reduce G.[^c4] The true conditional is unknown, so the bias is replaced by a first-order parameter-discrepancy surrogate.[^c5]

For canonical generalized linear models the authors show the rule shares the inverse-Hessian leverage factor of predictive-entropy acquisition, reweighted by goal alignment and prediction bias.[^c6] So it approximates entropy minimisation up to that correction.

Measured: on MNIST the number of labels to reach 90% accuracy was 374/422/441 (quartiles) for this method, versus 432/445/475 for BALD and 846/901/977 for random; at 95%, 1060/1150/1206 versus 1514/1589/1678 and 4265/4522/4731.[^c7] The abstract also claims fewer function evaluations than Gaussian-process Bayesian optimisation on noisy benchmarks and hyperparameter tuning.[^c1]

## Limits

The theory covers exponential-family and GLM settings; for deep networks the link to entropy minimisation is first-order and local, my reading of the paper's own framing. The expected-loss terms were approximated with a few jackknife samples, a cost not compared in the quote above. Gains over BALD at 80% accuracy are within the quartile ranges (88/108/116 against 104/109/117), so the advantage appears at higher accuracy. Sampling inputs is assumed free and labels costly; settings where questions themselves are costly or ambiguous were not tested. Nothing here is tested on language-model question selection; any transfer is my inference.

## Related

- [[expected-information-gain]] — the uncertainty-style score this rule approximates in GLMs.
- [[series-aggregated-acquisition]] — another way to cut the cost of uncertainty-based scoring.
- [[explicit-prior-cost-aware-exploration]] — exploration handled through an explicit prior rather than curvature.

[^c1]: arxiv-2602-19578 — "most approaches rely on predictive uncertainty estimates that are difficult to obtain reliably"
[^c2]: arxiv-2602-19578 — "the influence is measured by the instantaneous rate at which upweighting x gives"
[^c3]: arxiv-2602-19578 — "the inverse curvature term acts as a local uncertainty proxy that encourages"
[^c4]: arxiv-2602-19578 — "the second factor gates this directional effect by the"
[^c5]: arxiv-2602-19578 — "estimable parameter discrepancy, yielding a fully tractable acquisition rule"
[^c6]: arxiv-2602-19578 — "GOIMDA inherits the same Hθ−1 leverage factor that appears in predictive-entropy acquisition"
[^c7]: arxiv-2602-19578 — "GOIMDA requires fewer samples than BALD and random acquisition to achieve"
