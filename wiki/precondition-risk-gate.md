---
description: "Abstain from the method, not the answer: decompose its assumptions into independent risk dimensions, calibrate each to a failure probability, gate on a utility threshold before inference runs."
aliases: ["Causal-Audit", "precondition-aware risk gate", "assumption-violation risk profile"]
sources: ["arxiv-2604-02488"]
---
# Precondition risk gate

> The reject option need not wait for the answer: Ruiz et al. (2026) move it
> upstream of inference, gating on the calibrated risk that the *method's*
> preconditions are violated, before the method is ever run.

## Definition / Mechanism

Causal-Audit targets **silent failure**: "algorithms produce spurious causal
graphs without warning" when time-series data violate a discovery method's
assumptions — no low-confidence signal accompanies the wrong output, because
the output is confident.[^c1]

The gate has three stages. Stage I computes effect-size diagnostics across
independent assumption families (nonstationarity, irregularity, persistence,
confounding proxies), each diagnosed by several named statistics — e.g.
persistence risk from the integrated autocorrelation time
$\tau_{int} = \frac12 + \sum_{\ell=1}^\infty \rho(\ell)$, giving an effective
sample size $T_{eff} \approx T/(2\tau_{int})$ far below the nominal $T$ when
autocorrelation is high. Stage II turns each family's diagnostics into a
**calibrated failure probability** $R_k = P(Y{=}0 \mid d_k) \in [0,1]$ via
logistic aggregation, isotonic post-processing and bootstrap resampling,
yielding an uncertainty interval per dimension, not a point estimate.[^c2]

Stage III is the decision rule. Framed as expected-utility maximization over
actions $a \in M \cup \{\text{Abstain}\}$ with a three-way utility — $u_+$ for
successful use of a method, $-u_-$ for method failure, $-u_\varnothing$ for
abstention's opportunity cost, with $u_- \gg u_\varnothing$ — the argmax
collapses to a closed-form threshold: recommend method $m$ only when
$R_m < \theta_{abstain} \equiv \frac{u_+ + u_\varnothing}{u_+ + u_-}$; abstain
when every candidate method exceeds it.[^c3]

This is a three-outcome generalization of [[abstention|Chow's cost-based
threshold]]: instead of thresholding one classifier's own posterior
confidence, it thresholds a *separately diagnosed* risk that the tool is
inapplicable to this input at all, aggregated from several independent,
named violation dimensions rather than one scalar score. On the paper's
synthetic atlas (500 datasets, 10 violation families) the four risk
dimensions independently reach AUROC $>0.95$ with calibration slopes in
$[0.9,1.1]$ and ECE $<0.05$; the resulting policy cuts the false-positive
rate among recommended datasets by 62% (0.38 → 0.14) at 68% coverage, and
abstains on 78% of severe-violation cases.[^c4]

## Why it matters

Selective prediction abstains on *this instance* because the answerer's own
confidence is low; here the abstention trigger is diagnosed independently of
the method's output, from properties of the input alone, decomposed into
named, separately falsifiable dimensions instead of one opacity score. A
practitioner deriving an abstention rule for any tool-mediated answerer gets
a template: enumerate the tool's stated assumptions as independent families,
diagnose each with dimension-specific statistics, calibrate each to a
probability with an uncertainty interval, and only then apply a utility
threshold — rather than reading a single end-to-end confidence off the
answer the tool already produced.

## Transfer

| | |
|---|---|
| In its home field | time-series causal discovery: a fixed catalog of methods with documented, checkable statistical assumptions (stationarity, regular sampling, bounded persistence, no latent confounding), and ground-truth DGPs available for calibration |
| Here | any tool-mediated answering step, where "the answer" is produced by a method whose own preconditions can be named and diagnosed separately from its output |
| What survives | decomposing reliability risk into independent, named dimensions rather than one score; calibrating each with an uncertainty interval, not a point estimate; the closed-form utility threshold $\theta_{abstain}=(u_++u_\varnothing)/(u_++u_-)$ for a 3-outcome (succeed / fail / abstain) utility |
| What does not | the specific diagnostics (autocorrelation, unit roots, VIF) are statistical-time-series-specific; the calibration guarantee needs labelled DGPs with known ground truth, which most answering settings lack |

## Limits

- Calibration is corpus-relative: the four risk models are fit and validated
  on the paper's own synthetic DGP atlas; external validation is a
  recommend-or-abstain *consistency* check against 21 benchmark cases, not a
  recalibration, so the probabilities are unverified for the general claim
  that they transfer to unseen data-generating processes.[^c6]
- The method-specific components (risk calibration, decision thresholds) are
  currently fit for exactly two causal-discovery methods (PCMCI+, VAR-based
  Granger); extending the gate to a new method requires new calibration data,
  not just a new assumption list.
- Confounding risk is explicitly a proxy, not a test: "Neither multicollinearity
  nor parameter instability constitutes a direct test for latent confounding;
  rather, they serve as observable proxies" — so that dimension's calibrated
  probability answers a different question than the other three.[^c7]

## Related

[[abstention]] · [[informed-abstention-framework]] · [[calibration]] · [[decision-theoretic-grounding]] · Commitment

[^c1]: arxiv-2604-02488 — "When violations go undetected, algorithms produce spurious causal graphs without warning"
[^c2]: arxiv-2604-02488 — "Stage II transforms these diagnostics into calibrated risk scores with uncertainty intervals via logistic aggregation, isotonic post-processing, and bootstrap resampling."
[^c3]: arxiv-2604-02488 — "with Rm as the estimated failure risk for method m. When Rm ≥ θabstain for all methods m ∈ M, the framework recommends abstention"
[^c4]: arxiv-2604-02488 — "The default framework reduces the selective false positive rate by 62% (from 0.38 to 0.14) while maintaining 68% coverage"
[^c6]: arxiv-2604-02488 — "On 21 external evaluations from TimeGraph (18 categories) and CausalTime (3 domains), recommend-or-abstain decisions are consistent with benchmark specifications in all cases."
[^c7]: arxiv-2604-02488 — "Neither multicollinearity nor parameter instability constitutes a direct test for latent confounding; rather, they serve as observable proxies for conditions empirically associated with elevated false positive rates in structure learning."
