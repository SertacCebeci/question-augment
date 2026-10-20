---
description: "A conformal risk control threshold test built from a sequential betting wealth process, certifying tighter abstention thresholds than variance-aware bounds especially under scarce calibration data."
aliases: ["e-CRC", "Betting-Based Conformal Risk Control"]
sources: ["kotte-2026"]
---
# Betting-based conformal risk control (e-CRC)

> A way to certify an [[abstention]] threshold that, instead of computing a
> single worst-case or variance-aware confidence bound, tracks how much
> money a sequential bettor would have made wagering that the risk stays
> below target — and certifies the threshold once that wealth crosses
> $1/\delta$. It dominates the classical Hoeffding and empirical-Bernstein
> bounds at every tested risk target, with the largest edge when
> [[calibration]] data is scarce.

## Definition / Mechanism

For each candidate threshold $\lambda$, over the calibration emit set
$E_\lambda$: "we construct a wealth process over the emit set Eλ: W0 = 1,
Wj = Wj−1(1 + κj(α − rj)), where κj is a Kelly-style bet clipped to [0, 0.5]
with κ1 = 0 (no bet before the first observation)." The test statistic is
the worst case over a fixed family of orderings: "The e-value is the
minimum wealth Wm over 22 pre-registered orderings of the emit set
(score-descending, score-ascending, and 20 seeded random permutations); if
this minimum reaches 1/δ, the test at λ passes."[^c1]

The validity guarantee (Theorem 1): "For i.i.d. calibration data and any
fixed threshold λ, the e-CRC test satisfies P(E[R(λ)] > α and λ certified)
≤ δ." The mechanism behind it: "Under H0 : E[R] ≥ α, non-negative bets make
the wealth {Wj} a non-negative supermartingale. By Ville's inequality
(Howard et al., 2021), P(supj Wj ≥ 1/δ) ≤ δ."[^c2]

## Known as

| Field | Name there | Match |
|---|---|---|
| Kotte (2026), §2.1 | e-CRC | exact — the paper's own abbreviation |
| Kotte (2026), §2.1 | Betting-Based CRC | exact — the section heading, same construction |

## Why it matters

Across 716 configurations, e-CRC certified strictly more than the Hoeffding
and empirical-Bernstein bounds at every risk target tested and never fewer:
"e-CRC never certifies fewer configurations than Bernstein at any tested
α." Its advantage concentrates exactly where calibration data is limited —
the regime an asking agent is most often in: "e-CRC's edge is largest under
scarcity (10% calibration: 4.2% vs. 1.9% Bernstein, 1.1% Hoeffding), which
matters in low-resource extraction."[^c3]

## Transfer

| | |
|---|---|
| **In its home field** | Testing-by-betting (Shafer, 2021; Waudby-Smith & Ramdas, 2024) turns a hypothesis test into a wealth process valid under Ville's inequality, developed for sequential and anytime-valid statistical testing generally |
| **Here** | Applied to certify a single abstention threshold for an LLM's [[structured-output|structured output]], competing directly against Hoeffding/Bernstein concentration bounds for the same certification decision |
| **What survives** | The finite-sample validity (Theorem 1) and the practical edge under small calibration sets carry over unchanged — it needs no distributional assumption beyond i.i.d. calibration data |
| **What does not** | The specific choice of 22 pre-registered orderings and the Kelly-clip parameter (0.5) are tuned/evaluated on this paper's structured-generation tasks; the asymptotic inclusion e-CRC ⊇ Bernstein is proved only under alternatives with E[R] < α, not as a finite-sample certificate |
[^c4]

## Limits

The finite-sample validity (Theorem 1) is proved for a fixed λ; extending it
to the scan-selected certified threshold relies on a fixed-sequence testing
argument (the paper's Appendix Lemma E.1), not re-derived here. The claim
that e-CRC statistically subsumes Bernstein is empirical/asymptotic, not a
finite-sample theorem: "We make no deterministic finite-sample claim for
this inclusion." Like the [[conformal-abstention-floor]] it certifies
against, e-CRC assumes exchangeable calibration/deployment data and is not
validated here under distribution shift.

## Related

[[conformal-abstention-floor]] · [[emit-only-feedback-obstruction]] · [[hierarchical-group-conditional-conformal-risk-control]] · [[calibration]]

[^c1]: kotte-2026
[^c2]: kotte-2026 — "For i.i.d. calibration data and any fixed threshold λ, the e-CRC test satisfies P(E[R(λ)] > α and λ certified) ≤ δ."
[^c3]: kotte-2026 — "e-CRC never certifies fewer configurations than Bernstein at any tested α"
[^c4]: kotte-2026 — "We make no deterministic finite-sample claim for this inclusion."
