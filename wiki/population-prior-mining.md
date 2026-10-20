---
description: "Before the first question is asked, mine an auditable prior over Tiwari et al. (2026) set the starting point of elicitation from a source other than the current user: an offline pass over populatio…"
aliases: []
sources: ["tiwari-2026"]
---
# Population-prior mining

> Before the first question is asked, mine an auditable prior over
> preference dimensions from population data — every mined rule is a
> sentence a developer can accept, edit or drop before it is trusted.

## Definition / Mechanism

Tiwari et al. (2026) set the starting point of elicitation[^s1]
from a source other than the current user: an offline pass over population
survey data (demographics, item ownership, behavioural proxies) that mines
segment-level rules with an inductive-logic-programming system (ILASP). A
demographic or ownership value is a candidate antecedent; a binned
behavioural value is the consequent. A rule is emitted only when a
segment's mean deviates from the population mean by more than a declared
threshold ($\delta_{\min}$, 10 points on a 0–100 scale in the paper) and
the segment is at least 5% of the population, with a confidence equal to
the fraction of that segment's members on the asserted side (example
given: "seniors ⇒ 'time horizon' below baseline," confidence 0.8). The
population's per-dimension distribution then seeds the same particle prior
[[cross-type-eig]] starts from, warm-started per user by an intake profile
before any question is asked. Every mined rule is rendered as an English
sentence and passed through a developer steering checkpoint: each
conjunct — dimension, direction, threshold, confidence — is individually
inspectable, and the developer may accept, edit or drop it before it is
cached.

## Why it matters

This is a source for a preference-elicitation constraint that no existing
note answers: Source already lists population-level channels for
*aggregating many current answerers* ([[surprisingly-popular-algorithm]],
[[correlated-agreement]]); this one instead prices a prior from a
population the current user is not part of, with the audit step as the
check on whether that transfer is trusted. Standing alone, the effect is
small and mixed: in the paper's ablation (Table 2), adding this prior to a
pairwise-only system without axis discovery moved Normalized Regret
Reduction by no more than 0.03 in either direction across four of five
personas, and worsened it for one (0.096 to 0.063). The larger gains came
only once the prior was combined with letting the axis set grow at
runtime ([[dimension-proposal]]) — the population prior mainly matters as
the seed that mechanism and [[cross-type-eig]] build on, not as a
standalone lever.

## Transfer

| | |
|---|---|
| **Home field** | inductive logic programming / answer-set programming: a rule-induction system that returns a hypothesis (here, per-segment deviation rules) from labelled examples under a declared bias |
| **Here** | the "examples" are population survey rows re-purposed as positive evidence for a segment's deviation from the population mean, and the "hypothesis" is a set of soft priors over a *different* user's preference dimensions |
| **What survives** | the confidence-scored, individually-inspectable rule format — each mined statement is a sentence a non-specialist developer can audit before it is trusted |
| **What does not** | any completeness or optimality guarantee the induction system itself carries; the deviation threshold (10 points) and minimum-support cutoff (5%) are stated as this paper's own chosen constants, not derived from the induction method, and no source is verified here for what the induction system itself guarantees |

## Limits

- The confidence attached to a mined rule is a population base rate
  (fraction of a segment on the asserted side), not a calibrated posterior
  over whether the rule holds for the *current* user — it is a prior
  strength, and the paper does not report how often the checkpoint's edits
  changed the eventual recommendation.
- The standalone effect is small and sometimes negative (see Why it
  matters); the mechanism's value in this paper's own evidence is
  conditional on the axis-discovery transform also being present.
- Requires a developer to supply behavioural variables, demographic
  attributes and item-ownership indicators up front, plus review time at
  the checkpoint — an initialization cost the paper does not amortize
  against the elicitation-turn savings it reports.
- The rule-induction system's own properties (cited by Tiwari et al. 2026
  as Law et al. 2020) are not independently verified in this pass; only
  Tiwari et al.'s use of it is described here.

## Related

[[cross-type-eig]] · [[dimension-proposal]] · [[novice-expert-problem]] · [[objectives-generation-deficit]] · [[correlated-agreement]]

[^s1]: tiwari-2026
