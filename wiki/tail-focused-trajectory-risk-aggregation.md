---
description: "Scoring an agent trajectory by the max of per-step failure signals, then a top-k tail mean blended with the worst step, beats averaging when failures come from sparse critical episodes."
aliases: ["TRACER", "MAX-composite step risk", "sparse critical episode uncertainty"]
sources: ["arxiv-2602-11409"]
---
# Tail-focused trajectory risk aggregation

Uncertainty estimators built for single-shot text (token entropy, likelihood, self-consistency) average over a generation. In multi-turn tool-using dialogue, the argument of TRACER is that failures are triggered by sparse critical episodes (looping, incoherent tool use, user-agent miscoordination) even while local generation looks confident, so a global average "systematically underweight[s] the segments that determine success or failure".[^c1]

## Mechanism

Each step gets four component risks: content-aware surprisal, a repetition indicator, an agent action-observation mismatch, and a user coordination gap, each scaled by a weight. The step risk is their pointwise maximum, so the dominant signal is kept rather than diluted by summing weaker ones.[^c2] The trajectory score is then a convex mix of the top-k tail mean of step risks and the single worst step; the weight w "interpolates between chronic uncertainty patterns (captured by TMk ) and acute catastrophic breakdowns".[^c3]

The authors argue the aggregate is a coherent risk functional: the tail mean is a spectral risk measure (CVaR) and the max is a norm, so the blend is monotone, subadditive and 1-Lipschitz in the step signals.[^c4] Under two assumptions (step hazard bounded by a constant times step risk; the sum of the top-K risks bounded by eta) the breakdown probability is bounded by a constant times the expected tail mean plus an offset, "P(B) ≤ c K E[TMk (r)] + c η."[^c5]

## What was measured

On tau2-bench (airline, retail, telecom; three models) TRACER improved AUROC for failure prediction "by 4.7%–37.1% and AUARC by 6%–55%, depending on" model and domain, relative to the strongest baseline.[^c6] Among aggregation variants (additive, multiplicative, separate channels, max) "the MAX variant achieves the highest" AUROC in every model-domain pair, read by the authors as evidence that breakdowns are spikes, not sustained moderate uncertainty.[^c7] Failures were also flagged early, with the largest advantages "in the first 20% of execution".[^c8]

## Limits

- The probability bound is conservative (union bound plus worst-case dominance) and rests on assumptions, hazard-dominated-by-risk and tail sparsity, that are not tested empirically; the authors say so themselves.[^c9]
- AUROC differences between aggregation variants are modest in several cells (for example telecom 0.765 vs 0.753), with weights tuned per model and domain on validation data; no significance tests were read.
- Evaluated on one benchmark with simulated users; whether the same signals transfer to real users or other agent tasks is not shown. My inference: the max-composite choice also depends on the four signals being on comparable scales, which the weights alpha, beta, gamma must absorb.
- The score predicts task failure; it does not by itself say what question or intervention to issue.

## Related

- [[step-level-risk-calibrated-router]] — also penalises the tail of a trajectory-risk distribution (CVaR) to decide mid-run escalation
- [[conformal-risk-control-selective-judging]] — selective abstention from a scalar score, which TRACER's AUARC evaluates
- [[failure-count-help-trigger]] — a simpler trigger for seeking help during an agent run

[^c1]: arxiv-2602-11409 — "of token uncertainty systematically underweight the segments"
[^c2]: arxiv-2602-11409 — "failure signal at each step and avoids diluting sharp breakdown"
[^c3]: arxiv-2602-11409 — "The weight w interpolates between chronic uncertainty patterns (captured by TMk ) and acute catastrophic breakdowns"
[^c4]: arxiv-2602-11409 — "TMk is a spectral risk measure and ∥ · ∥∞ is a norm, ρk,w is a"
[^c5]: arxiv-2602-11409 — "P(B) ≤ c K E[TMk (r)] + c η."
[^c6]: arxiv-2602-11409 — "by 4.7%–37.1% and AUARC by 6%–55%, depending on"
[^c7]: arxiv-2602-11409 — "As shown in Table IV, the MAX variant achieves the highest"
[^c8]: arxiv-2602-11409 — "largest advantages in the first 20% of execution, highlighted"
[^c9]: arxiv-2602-11409 — "The bound is conservative by construction, relying on a union"
