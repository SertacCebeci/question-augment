---
description: "LLM grader confidence piles up near the top (86% above 0.8, 89.5% unanimous votes), so a midpoint threshold never fires; thresholds must be set from each model-method's observed scores."
aliases: ["confidence floor", "top-skewed confidence distribution"]
sources: ["arxiv-2603-29559"]
---
# Top-skewed confidence floor

When an LLM grader reports how sure it is, the scores do not spread over [0, 1]. They cluster at the top, so the lowest scores actually produced sit far above the nominal minimum. That lowest observed region is a "confidence floor". An intuitive cut such as 0.5 therefore routes almost nothing to human review, and the usable range of the signal is a narrow band near the top.

## What was measured

In a study of seven LLMs (4B to 120B parameters) grading student answers on RiceChem, SciEntsBank and Beetle, pooling self-reported and token-probability confidence gave this: "86% of predictions exceed 0.8; only 0.62% fall below 0.2".[^c1] Self-consistency is discrete by construction (5 samples): "89.5% of outputs are 5/5 (1.0), 6.1% are 4/5 (0.8), and 4.5% are 3/5 (0.6)".[^c2] For the best-calibrated model (GPT-OSS-120B, self-reported), the histograms show confidence clustering "in the 0.7–0.9 range, with fewer than 1% of predictions below 0.6".[^c3]

The authors' practical reading is that thresholds "should be set relative to each model/method's observed scores rather than an intuitive midpoint".[^c1]

## Why it matters for asking and answering

A confidence number is only informative about where the model's own distribution places the answer, not about its face value. A threshold has to be read against that distribution. The top-skew also bounds how much a gate can discriminate. Average AUC for correctness prediction was only about 0.57 to 0.67, so the few low-confidence cases are only weakly enriched in errors (AUC 0.668 for the best model; the paper's own table values for small models are near 0.57).[^c4] My inference: with the mass this concentrated and the ranking this weak, coverage at a fixed risk is small. This fits the reported coverage at a 10% risk threshold being near zero for several conditions (for example 0.000 to 0.006 on RiceChem for small models).[^c5]

## Limits

- Only binary rubric grading of student answers was tested; no other task type.
- Prompts and token sets were not released in the text I read, so the skew may depend on the prompt wording. The 1-to-10 verbalized scale is itself coarse.
- The paper gives no procedure for choosing the threshold, only the instruction to base it on observed scores. How to set one is untested here.
- The skew was reported pooled; a few model-dataset runs exceed 1% below 0.2, so it varies by run.
- The link from skew to low coverage is my inference, not a tested claim.

## Related

- [[calibration]] — the property the skew makes hard to exploit at fixed thresholds
- [[ue-method-scale-dependence]] — which uncertainty method works best also shifts with model scale
- [[vote-margin-gate]] — a gate on agreement among samples, whose discreteness is the skew's extreme form
- [[verbal-confidence-commit-readiness-dissociation]] — verbal confidence tracks something other than truth

[^c1]: arxiv-2603-29559 — "86% of predictions exceed 0.8; only 0.62% fall below 0.2"
[^c2]: arxiv-2603-29559 — "89.5% of outputs are 5/5 (1.0), 6.1% are 4/5 (0.8)"
[^c3]: arxiv-2603-29559 — "with fewer than 1% of predictions below 0.6"
[^c4]: arxiv-2603-29559 — "average AUC of 0.668 across all three datasets"
[^c5]: arxiv-2603-29559
