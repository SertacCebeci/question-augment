---
description: "A distribution-free calibration framework that turns any non-conformity score into a prediction set with a finite-sample coverage guarantee, without a parametric error model."
aliases: ["CP", "conformal calibration"]
sources: ["karimi-2026", "arxiv-2512-15068", "arxiv-2512-14221", "arxiv-2512-00453", "arxiv-2511-18225"]
---
# Conformal prediction

> Turn an arbitrary score into a threshold with a guarantee that holds in
> finite samples, no distributional assumption beyond exchangeability.

## Problem

A scoring rule (a probability, an [[entropy]], a distance) has no built-in
error rate: "accept if score $\le 0.5$" is a guess unless the threshold is
calibrated against held-out outcomes, and most [[calibration]] methods
(Platt scaling, isotonic regression) need a parametric or asymptotic
argument to bound the resulting error.

## Definition / Mechanism

As used by Karimi, Meyappan & Samavi (2026), citing Vovk,
Gammerman & Shafer (2005) [?]: given a calibration set
$D_{cal}=\{(x_i,y_i)\}_{i=1}^M$ and a non-conformity score
$S:\mathcal{X}\times\mathcal{Y}\to\mathbb{R}_{+}$, fix a miscoverage level
$\alpha\in(0,1)$ and set $\tau_\alpha$ to the empirical $(1-\alpha)$-quantile
of $\{S(x_i,y_i)\}$. For a new point drawn exchangeably with the
calibration set, the prediction set $C(x)=\{y: S(x,y)\le\tau_\alpha\}$
satisfies
$$P(y_{M+1}\in C(x_{M+1}))\ge 1-\alpha,$$
with no assumption on the model or the data distribution beyond
exchangeability of calibration and test points.[^c1]

Karimi et al. apply the same mechanics twice in one pipeline: a
prompt-level threshold $\hat\tau=\mathrm{Quantile}_{1-\alpha}(I_0)$ over an
uncertainty score restricted to prompts whose returned response was
correct, giving an accept/abstain rule with the guarantee
$P(\hat u(x_{new})\le\hat\tau \mid E(x_{new})=0)\ge 1-\alpha$ (their
Theorem 1); and a response-level non-conformity score $S(x,y_i)$ combining
prompt uncertainty with response atypicality, giving a prediction *set*
over sampled responses with the same coverage form (their Theorem 2).[^c2]

Used as a query rule rather than a prediction set, the same quantile construction budgets labels instead of bounding errors. In the CRSAIL work of arxiv-2512-00453 the score is the distance from a visited state to its K-th nearest labelled state. The threshold is the empirical (1 − α) quantile of that score over unlabelled on-policy states, and α is described as a tuning knob for the expected fraction of states sent to the expert.[^c5] The guarantee's premise is the weak point when the calibrated policy keeps changing; see Limits and [[state-novelty-query-rule]].

## Transfer

| | |
|---|---|
| **Home field** | Statistics: distribution-free set prediction for any exchangeable calibration/test split |
| **Here** | An LLM's accept-or-abstain decision on a prompt, and a prediction set over its sampled responses, used to decide whether an answer is trustworthy enough to return |
| **What survives** | The finite-sample, distribution-free coverage guarantee itself, and the quantile-of-calibration-scores construction — it needs no assumption about how the underlying score (token entropy, [[semantic-entropy|semantic entropy]], an adjusted score) was produced |
| **What does not** | The guarantee is marginal (averaged over the calibration/test exchange), not conditional on the specific prompt; and it presupposes a correctness label $E(x)$ on calibration prompts, which most open-ended axis or design questions in this wiki's frame do not have |

## Limits

- Read here only through karimi-2026's description and use of the
  framework; the originating text (Vovk, Gammerman & Shafer, 2005) was not
  read directly, so its statement is marked [?] and attributed via the
  citing paper.
- Exchangeability, not i.i.d., is the only assumption — but it still fails
  under distribution shift between calibration and deployment prompts,
  which karimi-2026 does not test.
- The guarantee bounds the *rate* of coverage failures across many
  decisions, not any single one.
- The guarantee can hold while the set is nearly useless. Calibrated on the positives, the threshold sits at their upper tail; where that tail overlaps the faithful responses, the target flags almost all of them. On HaluEval the threshold reaches 0.999 entailment and the false positive rate is 100%.[^c3] See [[hard-tail-recall-threshold]].
- Missing inputs break the marginal reading. A guarantee averaged over all
  points says nothing about any one missingness pattern: the paper states
  conformal prediction "fails to guarantee coverage when faced with missing
  covariates."[^c4] Pattern-level validity needs an explicit correction, see
  [[imputation-reweighted-conformal]].

- Used to budget queries, the coverage statement is weaker still. The calibration states along one trajectory are temporally correlated, so exchangeability fails, and the authors call the coverage statement an idealized reference rather than a strict guarantee.[^c6][^c7] The query rate therefore follows α only approximately, and the paper calibrates once rather than recalibrating with the current policy.

- Exchangeability can also fail inside the score. When the score is computed from samples whose noise drifts over time, the scores can lose exchangeability even though the data are exchangeable, and the rank argument behind the guarantee no longer applies.[^c8] See [[time-dependent-conformity-scores]], and [[adaptive-conformal-inference]] for the online recalibration the quantum-processor paper proposes in response.

## Related

[[semantic-entropy]] · [[adaptive-conformal-semantic-entropy]] · [[calibration]] · [[hard-tail-recall-threshold]] · [[imputation-reweighted-conformal]] · [[state-novelty-query-rule]] · [[adaptive-conformal-inference]] · [[time-dependent-conformity-scores]]

[^c1]: karimi-2026 — "P(yM +1 ∈ C(xM +1 )) ≥ 1 − α , (11) where α ∈ R(0,1) is the miscoverage level and C is the prediction set"
[^c2]: karimi-2026 — "Theorem 1 (Conformal coverage for prompt acceptance)."
[^c3]: arxiv-2512-15068 — "Since virtually all faithful responses also fall below 99.9% certainty, the FPR collapses to 100%"
[^c4]: arxiv-2512-14221 — "fails to guarantee coverage when faced with missing covariates"
[^c5]: arxiv-2512-00453 — "into a principled tuning knob for controlling the expected"
[^c6]: arxiv-2512-00453 — "should be viewed as an idealized reference rather"
[^c7]: arxiv-2512-00453 — "distributed across time steps, so exchangeability is violated"
[^c8]: arxiv-2511-18225 — "This breaks the usual exchangeability assumption"
