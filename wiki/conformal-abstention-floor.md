---
description: "A distribution-free lower bound on how often a selective predictor must abstain to certify a risk target below its base error rate, attained and closed-form."
aliases: ["sharpened two-sided abstention floor", "feasibility frontier", "distribution-free abstention lower bound"]
sources: ["kotte-2026"]
---
# Conformal abstention floor

> When a selective predictor's base error rate µ exceeds the risk target α
> it is asked to certify, no distribution-free method — however good its
> score, however much [[calibration]] data — can hit that target without
> abstaining on a computable minimum fraction of inputs. The floor is not a
> property of a particular [[abstention]] policy; it is a property of the
> deployment.

## Definition / Mechanism

For a score $s(x,\hat y)$, threshold $\lambda$, base risk $\mu = E[R]$ and
$M = \operatorname{ess\,sup} R \le 1$: "when µ > α, no distribution-free
method certifies without abstaining on ≥ (µ − α)/(M − α) of examples, so the
first question is 'is µ < α?'"[^c1]

The bound is tight, not merely a lower bound: "The bound is attained: the
two-point law R ∈ {0, M} paired with a perfectly ordering score meets it
with equality, and a general law reaches it iff P(R = M) ≥ (µ − α)/(M − α);
it is thus a tight feasibility frontier." When every per-example miss counts
as a complete failure (M = 1, the case on the paper's F1/exact-match
losses), this reduces to "any valid method must abstain on ≥ (µ − α)/(1 − α)
examples, regardless of bound tightness, score quality, or calibration
size."[^c2]

The achievable abstention above this floor decomposes further: "a
marginal-only dispersion gap (= 0 iff P(R=M) ≥ floor) and a score-only
ordering gap (= 0 iff the calibrated score E[R | S] orders risk perfectly
at the operating point)" — so a better-ranked score can close the gap to
the floor, but never go below it.[^c3]

## Known as

| Field | Name there | Match |
|---|---|---|
| Kotte (2026), Prop. 3 | sharpened two-sided abstention floor | exact — the paper's own name for the bound |
| Kotte (2026), §2.2 | feasibility frontier | exact — same object, emphasising attainment over "lower bound" |

## Why it matters

Deployed on 716 model-dataset-score-α configurations, the floor predicted
where certification would fail before any bound was run: "for NQ-Open (µ =
0.80) nothing certifies even at α = 0.20, the floor at work." Checking
whether the base risk µ is below the target α is a cheap test that settles
feasibility before any conformal procedure is calibrated — for an agent
deciding whether to answer or defer, this is the mechanism (not a heuristic)
that says when deferring is the only option regardless of how the deferral
policy is designed.[^c4]

## Transfer

| | |
|---|---|
| **In its home field** | Reject-option theory (Chow, 1970) gives the optimal *known-distribution* threshold; [[crc-confident-error-control|conformal risk control]] (Angelopoulos et al., 2024) certifies a threshold distribution-free but does not, by itself, say when certification is impossible |
| **Here** | Used as a pre-check on whether an asking/abstention policy can be certified at all before the policy is chosen — an axis-independent floor on how often "abstain and ask" is unavoidable |
| **What survives** | The floor's distribution-freeness and tightness travel intact: it needs no assumption about the score or the abstention mechanism, only i.i.d. calibration/deployment data and a bounded loss |
| **What does not** | The bound says nothing about *which* axis or question to ask instead of abstaining, and it assumes exchangeability between calibration and deployment — it is silent, and known to fail, under the distribution shift this same paper studies separately |
[^c5]

## Limits

The floor is a population statement; the paper's own plug-in correction for
a finite audit of µ and M adds a sampling-error term $\varepsilon/(M-\alpha)$
that the tables in this paper do not carry (they report the conservative
$M=1$ instance). It assumes calibration and deployment data are
exchangeable — the paper's own cross-dataset shift experiments (§3.5–3.6)
show the floor's guarantee, like CRC's, does not survive violated
exchangeability without further machinery ([[emit-only-feedback-obstruction]]).
The source is a single-author, not-yet-peer-reviewed arXiv preprint (v2,
2026-09-07); its 716-configuration evaluation is confined to six open-weight
LLMs and four [[structured-output|structured-generation]] tasks (NER, JSON, QA, classification).

## Related

[[emit-only-feedback-obstruction]] · [[hierarchical-group-conditional-conformal-risk-control]] · [[abstention]] · [[calibration]]

[^c1]: kotte-2026
[^c2]: kotte-2026
[^c3]: kotte-2026
[^c4]: kotte-2026 — "for NQ-Open (µ = 0.80) nothing certifies even at α = 0.20, the floor at work."
[^c5]: kotte-2026 — "Under distribution shift, the exchangeability assumption underlying CRC is violated, and static thresholds can fail badly (our experiments show 60–88% violation rates)."
