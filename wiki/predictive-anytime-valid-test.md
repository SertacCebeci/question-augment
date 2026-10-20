---
description: "Reject when the null-world probability that the planned fixed-sample test would reject exceeds a Monte Carlo-calibrated threshold: anytime-valid, near fixed-test power, no martingale needed."
aliases: ["predictive anytime-valid testing", "predicted rejection probability stopping rule", "anytime-valid bootstrap test"]
sources: ["arxiv-2602-13872"]
---
# Predictive anytime-valid test

A sequential test can be built by treating the unfinished experiment as a prediction problem. At interim size n of a planned N, the only uncertainty about the final fixed-sample decision is the unobserved future data. Assuming the null is true, one computes Q_n, the probability that the classical test would reject at size N given the data so far.[^c1] The null is rejected the first time Q_n reaches a threshold gamma.[^c2]

## Mechanism

Future observations are treated as missing data drawn under the null, so Q_n needs only forward simulation of the null (or a closed form, as for a one-sided normal mean).[^c3] The threshold gamma is set by Monte Carlo from two numbers: the target overall Type I error alpha and a smaller fixed-sample level alpha-tilde. The stated default is 0.95 alpha.[^c4]

The older route, stochastic curtailment, takes Q_n to be a martingale and bounds the error with Doob/Ville inequalities. The authors say that route is inadmissible: a Monte Carlo threshold has the same Type I error and more power, because it loses nothing to the inequality. It also removes the martingale constraint, so nonparametric tests, composite nulls and bootstrap tests can be made anytime-valid.[^c5]

## What was measured

All of these are the authors' own simulations or one trial re-analysis:

- Typical examples: about 20% fewer samples when the null is false. The cost of the conservative alpha-tilde is about 0.5% power, and about 2% extra maximal sample size recovers it.[^c6]
- One-sided normal example: at theta = 0.13, power was 0.90 for the fixed test, 0.91 for the predictive test and 0.44 for an e-process test.[^c7]
- Existing e-process methods often need near 2N to match fixed-test power.[^c8]
- International Stroke Trial, log-rank test, 19,397 participants: Q_t crossed gamma = 0.95 at 7 months of a 15-month span, reaching the fixed-test conclusion.[^c9]

## What it means for asking and answering

An asker who monitors an inquiry gets an explicit stopping rule: stop when the planned final answer is already nearly determined. The answer stays the classical test's answer. The price of the freedom to peek is one stated parameter, alpha-tilde < alpha.[^c10]

## Limits

- The comparison with e-processes is the authors' simulation on standard problems. The 0.44 versus 0.91 gap is one effect size in one design and does not show that e-processes are uniformly worse. Other e-process designs, such as those that target the alternative, were not shown here.
- It needs the null distribution of the fixed test statistic, known or simulable.[^c11] There is no guarantee when the null cannot be simulated.
- The proofs, the Type I error calibration and the futility extension are in a Supplementary Material that I did not read. The main text only asserts them.
- It needs a planned maximal N. An inquiry with no horizon has no Q_n.
- Stopping for efficacy is the case developed in the main text. It makes no claim about estimation or about the stopped estimate's bias.
- The paper is a preprint. The IST illustration is a single re-analysis.

## Related

- [[stochastic-curtailment]] — the martingale-based ancestor, which this construction generalizes by dropping the martingale requirement
- [[sprt]] — likelihood-ratio sequential testing that replaces the fixed test instead of preserving it
- [[robust-log-optimal-e-value]] — the e-process family the paper says pays a power penalty
- [[e-detector]] — another anytime-valid construction built on evidence accumulation

[^c1]: arxiv-2602-13872 — "Assuming the null hypothesis is true, we compute the probability that a fixedsample test would reject the null hypothesis at its planned endpoint."
[^c2]: arxiv-2602-13872 — "the null hypothesis is rejected as soon as the predictive probability that the fixed-sample test"
[^c3]: arxiv-2602-13872 — "Because these simulations involve"
[^c4]: arxiv-2602-13872 — "reasonable default choice is 0.95α"
[^c5]: arxiv-2602-13872 — "there is no need for a martingale constraint on the test statistics"
[^c6]: arxiv-2602-13872 — "The practical cost of this conservatism in terms of power is minimal, to the order of"
[^c7]: arxiv-2602-13872 — "the power values for the fixedsample test, the predictive anytime-valid test, the e-process anytime-valid test are 0.90, 0.91, and"
[^c8]: arxiv-2602-13872 — "often require"
[^c9]: arxiv-2602-13872 — "crosses the stopping threshold, of γ = 0.95, at 7 months"
[^c10]: arxiv-2602-13872 — "requiring one user set parameter"
[^c11]: arxiv-2602-13872 — "Our approach applies whenever"
