---
description: "Casts an LLM agent's mid-reasoning decision to escalate to a stronger model as Bayesian optimal stopping over a learned competence posterior, with a closed-form threshold."
aliases: ["Bayesian self-escalation", "self-escalation", "intra-generation delegation"]
sources: ["shaikh-2026"]
---
# Bayesian self-escalation

> A hierarchical LLM agent decides *while still generating* whether to keep
> going or transfer control to a stronger model, by tracking its own
> posterior probability of eventually succeeding rather than a router's
> pre-reasoning guess or a verifier's post-hoc score.

## Definition / Mechanism

Standard delegation either routes before generation starts or verifies
after it ends. Shaikh (2026) instead treats delegation mid-generation as an
optimal-stopping problem: at each step $t$ the agent maintains a belief
$B_t = \mathbb{P}(Y=1 \mid \mathcal{F}_t)$, its estimated probability of
eventual task success given everything generated so far, learned from
labelled trajectories rather than read off token-level [[entropy]] — "an
abstract competence posterior whose sufficient statistics are learned from
labelled trajectories, not read off raw entropy."[^c1]

A myopic (one-step-lookahead) closed-form threshold is derived
(Proposition 1): escalate when $B_t < \tau_t^{myo}$, a quantity fixed by
the cost, length and quality parameters of the problem. A full
dynamic-programming solution shows this shape is not just convenient but
optimal: "For each t there exists a threshold $\tau_t^\star$ such that the
optimal policy escalates at step t iff $B_t \le \tau_t^\star$" (Theorem 2)
— the optimal rule is a time-varying threshold on the belief, with no
assumed functional form imposed in advance.[^c2]

## Why it matters

Two guarantees bound the policy's behaviour. First, an oracle running the
thresholded rule on the true belief separates successes from failures
exponentially fast in the Chernoff-information rate of the underlying
signal process: "there is a constant $A_\tau < \infty$ ... such that
$\mathbb{P}(B_t \le \tau \mid Y=1) \le A_\tau e^{-tC}$." Second, once the
belief must be estimated from $n$ labelled [[calibration]] trajectories rather
than known exactly, the deployed policy's excess cost over the oracle is
bounded by how miscalibrated that estimate is and decays at rate
$O(1/\sqrt{n})$ — calibration, not the stopping rule itself, is the
binding constraint on performance.[^c3]

On a real model pair (Qwen2.5-Coder 1.5B junior, 7B senior, 257 MBPP
tasks), the resulting escalation frontier beat an equal-cost
post-hoc-routing baseline: "Streaming dominates post-hoc across the
frontier: to reach 75% accuracy it uses 30.2% less total compute (14,841
vs. 21,273 generated tokens)."[^c4]

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | Bayesian optimal stopping / sequential decision theory | intra-generation model escalation in hierarchical LLM agents |
| What survives | the threshold-on-a-posterior structure, and that the optimal rule is provably a threshold rule (no shape assumed) | unchanged — Theorem 2 is proved in this setting directly |
| What does not | the classical setting's known, analytic likelihood or state process | the posterior here is itself learned from labelled trajectories, so the guarantees are conditional on how well that estimate is calibrated, not on the stopping rule alone |

## Limits

The optimal-policy and separation results (Theorem 2, the Chernoff bound)
hold for the *oracle* belief $B_t$; the deployed system uses a plug-in
estimate $\hat B_t$, and the paper's own regret bound makes the achieved
performance conditional on calibration error, which is not itself bounded
by the stopping theory. The empirical validation is a single junior/senior
model pair on one benchmark (MBPP, 257 tasks) — coding tasks with a clear
pass/fail signal, unlike open-ended question-asking. `shaikh-2026` is a
2026 arXiv preprint, not yet peer-reviewed and its text extract is not yet
archived locally, so quotes here are drawn from the arXiv HTML rendering. [?]

## Related

[[sprt]] · [[odds-theorem]] · [[value-of-information]]

[^c1]: shaikh-2026
[^c2]: shaikh-2026
[^c3]: shaikh-2026
[^c4]: shaikh-2026 — "Streaming dominates post-hoc across the frontier: to reach 75% accuracy it uses 30.2% less total compute (14,841 vs. 21,273 generated tokens)."
