---
description: "A selective-prediction score subtracting a learned conflict-detector's risk from confidence, beating confidence-only ranking when retrieved evidence disagrees."
aliases: ["CAS", "conflict-aware score", "conflict-aware selective prediction"]
sources: ["han-2026-when"]
---
# Conflict-aware abstention score

> Raw confidence is not enough to know when to answer: when the retrieved
> evidence for a question is itself contradictory, a second signal —
> a learned detector of "confidently wrong" — has to be mixed in before
> ranking examples for abstention.

## Definition / Mechanism

Han, Lan & Kilicoglu (2026) evaluate biomedical yes/no QA
under five retrieval conditions built from one correct and one incorrect
evidence document: no context (NC), correct-only (CC), incorrect-only (IC),
and both documents present in either order — correct-first (CIC) or
incorrect-first (ICC). The **conflict-aware score (CAS)** ranks held-out
examples for selective prediction as
$s_{CAS}(x) = (1-\alpha)\,c(x) - \alpha\,r(x)$, where $c(x)=\max(p_{YES},p_{NO})$
is raw confidence, $r(x)\in[0,1]$ is "the predicted probability that
prediction $x$ is confidently wrong, produced by the within-condition
logistic detector," and $\alpha=0.5$ in the main experiments; $\alpha=0$
recovers confidence-only ranking (Conf) and $\alpha=1$ a detector-only
ranker. "Larger r pushes sCAS down so that likely-wrong examples are
deprioritized, while larger c pushes it up."[^c1]

The detector $r(x)$ is a logistic model trained separately per evidence
condition on an 80/20 split, using confidence, [[entropy]], logit margin, and
question/document sentence-embedding features, with the positive class
defined as confidently wrong predictions (threshold $\tau=0.7$).[^c2]

Under the train-threshold transfer protocol — the abstention threshold is
chosen on training data only and applied unchanged to held-out test data —
CAS beats Conf specifically in the two conditions where confidence-only
abstention is weakest: "In 'IC', the lift is positive for all six models at
all three operating points, with mean gains of 7.2, 20.4, and 33.4
percentage points as coverage becomes more selective... The same pattern
holds in 'ICC', although the gains are smaller. Mean lift is 3.6 points at
75% coverage, 10.4 points at 50%, and 14.4 points at 25%."[^c3]

Conf itself is unreliable in those same conditions: "In 'IC', the mean gain
of Conf is negative at all three operating points (−1.2, −0.9, and −2.1
points), showing that raw confidence often fails to identify safer
examples."[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Retrieval-augmented biomedical QA (Han et al. 2026) | CAS | exact — the paper's own abbreviation |
| Retrieval-augmented biomedical QA (Han et al. 2026) | conflict-aware score | exact — the paper's spelled-out term |

## Why it matters

This is a concrete instantiation of [[abstention]]'s selection function $g$
for the case where the *source of unreliability is not the model but the
evidence set itself*: instead of a single confidence threshold, $g$ is a
weighted combination of confidence and a learned estimate of how likely the
retrieved context is conflicting or misleading. It shows the two signals are
not redundant — confidence alone degrades exactly where evidence conflict is
highest (IC, ICC), and the mixture recovers usable selective accuracy there
without touching the conditions where confidence already works (CC, NC).

## Limits

- $\alpha=0.5$ is fixed in the main results as "a balanced midpoint"; the
  paper reports sensitivity to $\alpha$ only in an appendix figure not read
  here, so how CAS degrades away from that midpoint is not established by
  this note's evidence.
- The detector is trained and evaluated within the same evidence condition
  (a separate model per NC/CC/IC/CIC/ICC); the paper does not establish that
  a detector trained on one conflict condition transfers to another.
- Evaluated on one benchmark (HealthContradict, 920 yes/no biomedical
  questions) and six open-weight models 4B–14B parameters; whether the gain
  holds for free-form QA or larger models is untested here.
- The detector needs labelled "confidently wrong" examples to train on,
  which requires ground truth — CAS is a held-out evaluation method, not
  demonstrated as a zero-label deployment technique.

## Related

[[abstention]] · han-2026-when · [[answer-stability-abstention]] · [[semantic-entropy]]

[^c1]: han-2026-when — "Larger r pushes sCAS down so that likely-wrong examples are deprioritized, while larger c pushes it up."
[^c2]: han-2026-when — "The predictor is trained separately for each target evidence condition on an 80/20 split using uncertainty signals and sentence-embedding features, with the positive class defined as confidently wrong predictions (τ = 0.7)"
[^c3]: han-2026-when
[^c4]: han-2026-when
