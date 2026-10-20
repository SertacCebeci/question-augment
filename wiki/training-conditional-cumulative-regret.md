---
description: "Summing per-round gaps between conditional coverage and 1-alpha certifies online conformal sets under drift; long-term average coverage can be exact while this regret grows linearly."
aliases: ["training-conditional cumulative regret", "cumulative coverage-gap regret", "online conformal regret"]
sources: ["arxiv-2602-16537"]
---
# Training-conditional cumulative regret

Online [[conformal-prediction]] is usually judged by whether the running average of coverage indicators converges to 1 - alpha, as in Adaptive Conformal Inference. That check cannot detect empty or vacuous sets. The metric studied by Liang, Ren and Chen replaces it with a per-round quantity: the coverage probability of the round-t set, conditional on all past data and internal randomness, minus 1 - alpha, summed over t.[^c1]

## Mechanism

At each time t the training-conditional coverage is the probability that Y_t lies in C_t given the past data Z_{1:t-1} and the internal randomness U. The gap to the nominal level is "the regret incurred at time t". Cumulative regret is the expected sum of these gaps over the horizon.[^c2] This ties predictive inference to online-learning regret analysis.

The per-round form matters because it differs from long-term coverage. Long-term coverage is the gap of the average, and regret is the average of the gaps. Fact 2.1 states two things. First, long-term coverage minus (1 - alpha) is at most regret/T, so sublinear regret implies calibrated long-term coverage. Second, for alpha at most 1/2 there is an algorithm whose sets are each either empty or all of R, whose long-term coverage is exactly 1 - alpha, and whose regret is at least alpha*T.[^c3] So the converse fails: exact average coverage is compatible with linear regret.

## Rates under drift

For independent data with drifting distributions, the paper analyses two regimes, measured on the score distributions by Kolmogorov-Smirnov distance rather than on raw data. With pretrained scores and drift-detection-driven recalibration windows, regret is at most roughly sqrt((N_cp+1)T) with N_cp change points, and roughly sqrt(T) + (KS_T)^{1/3} T^{2/3} under smooth drift with total variation KS_T.[^c4] A matching minimax lower bound, Omega of the same orders, holds for every score-based non-anticipating algorithm, so the rates are optimal up to logarithmic factors.[^c5] The authors read the T^{2/3} term as showing that the evolving score distribution, not sampling noise, dominates regret under smooth drift.[^c4]

For scores trained online, they use a full-conformal-style method that relies on stability of the fitting algorithm rather than permutation symmetry, and match the lower bound only under restrictions on the prediction sets.[^c6]

## Limits

- The guarantees need independent data with unknown drift; the adversarial setting that motivated time-averaged coverage is excluded, so they do not transfer there (the paper itself says it moves beyond adversarial regret by assuming independence).[^c7]
- The optimality claim for online-trained scores holds only under restrictions on the prediction sets; bounds hold up to logarithmic factors.
- Real-valued responses and one-dimensional scores only; I did not read the proofs or the experiments.
- Whether this metric changes how a question-answering system should be calibrated is my inference, not tested here.

## Related

- [[conformal-prediction]] — the finite-sample coverage framework this metric evaluates in streams
- [[calibration]] — coverage gap is a conditional calibration error
- [[round-wise-regret-conformal-acceptance]] — a different regret (controller action) with per-round conformal coverage
- [[turn-valid-coverage]] — per-turn validity in sequential settings

[^c1]: arxiv-2602-16537 — "training-conditional cumulative regret metric"
[^c2]: arxiv-2602-16537 — "which aggregates the training-conditional coverage gaps over time and captures the deviation from the target coverage rate."
[^c3]: arxiv-2602-16537 — "an algorithm can achieve perfectly calibrated long-term coverage while still incurring training-conditional regret that grows linearly with T"
[^c4]: arxiv-2602-16537 — "the regret scales proportionally to the square root of the number of change points N"
[^c5]: arxiv-2602-16537 — "Evidently, the minimax regret lower bounds in Theorem 3.2 match the achievable regret of Algorithm 2"
[^c6]: arxiv-2602-16537 — "stable learning algorithms, and establish non-asymptotic upper bounds on the training-conditional"
[^c7]: arxiv-2602-16537 — "A non-adversarial setting with independent data"
