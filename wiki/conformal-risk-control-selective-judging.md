---
description: "A linearized-loss conformal threshold bounds the error rate among accepted LLM judgments at a user level alpha under exchangeability, accepting more than Clopper-Pearson-style conservative tests."
aliases: ["SCOPE", "selective conformal pairwise evaluation", "FDR-controlled LLM judging"]
sources: ["arxiv-2602-13110"]
---
# Conformal risk control for selective judging

A judge answers only when its uncertainty score s(x) is at most a threshold λ and abstains otherwise. The question is how to pick λ so that the error rate among answered cases is provably at most α. SCOPE does this with a conformal calibration step on labeled pairs.

## Mechanism

The target is a false-discovery-rate style ratio: expected error among accepted judgments. A ratio is unstable when few are accepted, so it is replaced by the linear loss L = S(x,λ)·(E(x) − α), where S marks acceptance and E marks error. E[L] ≤ 0 implies FDR ≤ α.[^c1] Each accepted correct judgment adds −α to a running sum, a safety margin. Each accepted wrong one adds 1 − α and spends it.

For finite samples the calibration sum must be at most −1. That absorbs the worst possible loss of one unseen test point. Feasibility need not be monotone in λ, because newly admitted samples may contribute either −α or (1 − α), so SCOPE takes the largest feasible λ.[^c2] If none is feasible it abstains on everything.

The motivation is that thresholds tuned to match validation behavior can exceed the desired risk on new samples, while conservative bounds such as Clopper-Pearson reach the constraint by rejecting many queries.[^c3]

## What was measured

With BPE scores from [[bidirectional-preference-entropy]], at α = 0.10 the empirical FDR was about 0.097–0.099 across benchmarks, and the paper reports up to 2.4× more accepted judgments than vanilla baselines under the same risk constraint.[^c4] Results averaged 1000 random 50/50 calibration/test splits. On MT-Bench with Qwen-7B, coverage was 0.246 against 0.102 for naive calibration while staying under the bound.

## Limits

- The guarantee is marginal, over calibration and test draws. It is not per-instance or per-subgroup. Conditional validity, as in [[mondrian-conformal-prediction]], is not claimed.
- It needs exchangeable human-labeled calibration pairs. Under distribution shift, such as a new judge, new task mix or adversarial responses, the bound is not supported.
- The risk is measured against human preference labels, which are themselves noisy. Binary pairs with ties removed, 2,000 sampled instances per benchmark.
- Reported FDR sits just under α, so the bound is tight on average. Variance across single splits is not what the headline number shows.

## Related

- [[conformal-prediction]] — the general exchangeability machinery this specializes
- [[conformal-abstention]] — abstaining under a conformal guarantee
- [[betting-based-conformal-risk-control]] — another route to risk control with a margin budget
- [[bidirectional-preference-entropy]] — the uncertainty score fed to the threshold
- [[judge-coverage-overestimation]] — a judge-reliability failure that a calibrated abstention targets

[^c1]: arxiv-2602-13110 — "The key observation is that E[L(x, λ)] ≤ 0 implies"
[^c2]: arxiv-2602-13110 — "Because newly admitted samples may contribute either −α or (1 − α), the feasibility of"
[^c3]: arxiv-2602-13110 — "thresholding confidence scores offers no finite-sample statistical guarantee that a target accepted-set error will be respected at deployment; thresholds tuned to match validation behavior can exceed the desired risk on new samples."
[^c4]: arxiv-2602-13110 — "S COPE consistently satisfies the target risk bound (empirical FDR ≈ 0.097–0.099"
