---
description: "Calibrating an LLM's abstention threshold per language nearly matches an oracle; English-only calibration is simplest but weaker; pooled calibration trades off between the two."
aliases: ["language-specific threshold calibration"]
sources: ["alfarano-2026"]
---
# Multilingual threshold calibration for selective prediction

> [[abstention|Selective prediction]] (accept if uncertainty $u<t$, else
> abstain) needs one number, $t$, per deployment — and in a multilingual
> system, *where* that number is calibrated changes the trade-off between
> how many errors are caught and how much correct coverage is sacrificed.

## Definition / Mechanism

Alfarano, Bacciu & Mansour (2026) compare three strategies
for setting the abstention threshold $t$ (accept the prediction if
uncertainty score $u<t$, else defer to human review) of a 22-language
selective-prediction system, each threshold chosen "by maximizing F1-score
for error detection on validation data": $t_{EN}$, tuned on English data
only and applied to every language; $t_{GLOBAL}$, tuned on pooled
multilingual data; and $t_{LANG}$, language-specific thresholds transferred
to their own target language — measured with Claude Sonnet 4.5 against an
oracle upper bound tuned directly on the target test language.[^c1]

$t_{EN}$ gives "43% relative error reduction (from 13.5% to 7.7%) and
maintaining high coverage with only 6.6% of correct predictions filtered
out." $t_{GLOBAL}$ delivers "56% error reduction at the cost of moderate
coverage loss (13.5% false negatives)." $t_{LANG}$ "achieves the strongest
practical performance with 60% error reduction and 8.1% error detection,
nearly matching Oracle thresholds tuned on target data itself (93.0 vs. 93.4
accuracy), though this comes at the expense of filtering out 14.4% of
correct predictions." The Oracle strategy itself "establishes the
performance ceiling at 62% error reduction but requires target-specific
[[calibration]] data, limiting its practical applicability."[^c2]

## Why it matters

On stall 10, this gives the answerer's commit-or-abstain threshold a
deployment-level choice rather than one default number: which of the three
calibration strategies to use trades off safety-critical error detection
($t_{LANG}$), minimal-data simplicity ($t_{EN}$), and a balanced
accuracy-coverage point ($t_{GLOBAL}$).

## Limits

- Measured with one model (Claude Sonnet 4.5) and F1-optimized thresholds on
  two specific QA datasets; whether the ranking of the three strategies
  holds for other models or objectives (optimizing recall instead of F1,
  for instance) is not tested.[^c3]
- The oracle strategy is not itself deployable (it needs target-language
  calibration data absent by construction from the problem this note
  addresses); it only bounds the other three.
- This reuses [[abstention]]'s accept/abstain decomposition unchanged; what
  is new here is only the choice of calibration data across languages, not
  a new selection function.

## Related

[[abstention]] · [[reasoning-language-ue-bottleneck]] · [[ue-method-scale-dependence]]

[^c1]: alfarano-2026 — "We select t by maximizing F1-score for error detection on validation data, comparing three calibration strategies: (1) tEN , optimized on English data only and applied to all languages; (2) tGLOBAL , optimized on pooled multilingual data; and (3) tLANG , using language-specific thresholds transferred to corresponding target languages."
[^c2]: alfarano-2026 — "43% relative error reduction (from 13.5% to 7.7%) and maintaining high coverage with only 6.6% of correct predictions filtered out."
[^c3]: alfarano-2026
