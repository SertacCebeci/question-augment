---
description: "A post-hoc conformal method that thresholds a user-chosen uncertainty score (not a nonconformity score) to give both a participation-rate bound and a bound on correctness conditioned on participating."
aliases: ["CA", "Conformal Abstention", "conditional correctness guarantee", "participation guarantee"]
sources: ["arxiv-2604-27914"]
---
# Conformal abstention

> Conformal prediction guarantees a set contains the truth; this guarantees
> something an answerer can act on directly — that when it chooses to
> answer, it is very likely right, and that this bound holds without ever
> computing the intractable score conformal prediction usually needs.

## Definition / Mechanism

Xu, Chen, Xie & Xiong (2026) replace the non-conformity
score of standard [[conformal-prediction|conformal prediction]] — intractable
for open-ended generation, since ground truth can take many semantically
equivalent forms — with an arbitrary user-specified **uncertainty score**
$u = r(\hat y|x)$ correlated with correctness (e.g. perplexity). Calibrating
a threshold $\tau$ as the usual conformal quantile of calibration
uncertainty scores defines a kept region $K := \{x : r(x) \le \tau\}$: the
model answers on $K$ and abstains outside it. "the abstention decision
relies on prediction confidence rather than the non-conformity scores used
in CP, which are intractable for open-ended generation"[^c1]

This alone gives a standard **participation guarantee** — the marginal rate
of not abstaining is bounded near $1-\alpha$: "P(Xn+1 ∈ K) = P(Un+1 ≤ τ ) ∈
[1 − α, 1 − α + 1/n + 1)"[^c2]

The paper's further contribution is a **conditional correctness guarantee**:
a bound on $P(J_{n+1}=1 \mid X_{n+1}\in K)$, the probability a kept
(non-abstained) answer is actually correct — not the joint probability of
answering-and-being-wrong that prior conformal-risk-control abstention
targets. It is derived by showing the uncertainty score and correctness
indicator remain exchangeable under the deterministic transformation
$(x,y)\mapsto(r(f(x)|x),\xi(x,y,f(x)))$ (an instance of a general
exchangeability-preservation theorem), which licenses restricting attention
to the calibration subset with correct predictions and applying Bayes' rule
to the participation bound: "P(Jn+1 =1 | Xn+1 ∈ K)=P(Xn+1 ∈ K |
Jn+1 =1)P(Jn+1 =1)/P(Xn+1 ∈ K) ≥ 1−β/1 − α + 1/(n + 1) · c/n"[^c3]

The motivating distinction from prior conformal-risk-control abstention
(bounding $P(\text{answer wrong})$ jointly with participation) is that
participation is observable at deployment while joint miss-rate is not:
"since model participation is directly observable, the conditional
probability of correctness given participation is a more useful and
practically relevant than the joint probability. Our theoretical framework
explicitly targets this conditional guarantee."[^c4]

## Why it matters

This gives stall 10 (commitment / abstention) a guarantee phrased in the
quantity an answerer's audience actually cares about — not "the system
rarely both answers and errs" but "given that it chose to answer, it is
right with at least this probability" — and it removes the requirement,
inherited from classical conformal prediction, of a tractable
non-conformity score over an open-ended output space.

## Limits

The guarantee is marginal, not per-query: it says nothing about any single
kept example, only about the calibration/deployment distribution as a
whole, and it inherits the standard conformal requirement of exchangeable
calibration and test data. Tightening it (raising $1-\beta$) is only
possible by making correct predictions score more confidently than
incorrect ones — the theorem bounds correctness given a good uncertainty
score, it does not supply one; that gap is what motivates
[[representation-geometry-calibration]] in the same paper.

## Related

[[conformal-prediction]] · [[abstention]] · [[crc-confident-error-control]] · [[conformal-abstention-floor]] · [[representation-geometry-calibration]]

[^c1]: arxiv-2604-27914 — "the abstention decision relies on prediction confidence rather than the non-conformity scores used in CP, which are intractable for open-ended generation"
[^c2]: arxiv-2604-27914 — "P(Xn+1 ∈ K) = P(Un+1 ≤ τ ) ∈ [1 − α, 1 − α + 1/n + 1)"
[^c3]: arxiv-2604-27914
[^c4]: arxiv-2604-27914 — "since model participation is directly observable, the conditional probability of correctness given participation is a more useful and practically relevant than the joint probability. Our theoretical framework explicitly targets this conditional guarantee."
