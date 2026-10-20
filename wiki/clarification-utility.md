---
description: "A metric U = Acc / (1 + AskRate) that scores a clarification policy over a whole interaction run, so higher accuracy bought with more frequent asking does not automatically score higher."
aliases: ["Clarification Utility", "CU"]
sources: ["he-2026-pact"]
---
# Clarification Utility

> A single number for "did asking pay for itself over the whole run":
> accuracy divided by one plus how often the agent asked, so a policy that
> buys the same accuracy with fewer questions scores strictly higher.

## Definition / Mechanism

He, Li, Ma et al. (2026) define, at interaction step $t$,
$A_t \in [0,1]$ as the post-action assistance score and $q_t$ as the number
of clarification questions asked at that step; over $T$ steps with
$K=\sum_{t=1}^T q_t$ total questions,

$$U = \frac{\sum_{t=1}^T A_t}{T+K} = \frac{\mathrm{Acc}}{1+\mathrm{AskRate}}$$

where $\mathrm{Acc}=\frac1T\sum_t A_t$ and $\mathrm{AskRate}=K/T$. The
source states the design intent directly: "Clarification Utility favors
methods that achieve higher assistance accuracy with fewer clarification
questions."[^c1]

The metric is bounded, $0 \le U \le 1$, reduces to $U=\mathrm{Acc}$ when no
question is asked ($K=0$), and "when $K>0$, the metric penalizes additional
clarification unless it improves the final assistance outcome."[^c2]

On the paper's household-assistance benchmark, comparing eight ask
policies against a no-clarification baseline, higher ask rate did not
track higher utility: "ASK-RL, our primary learned instantiation, and
ASK-L2D achieve strong task accuracy with lower ASK rates, suggesting a
better accuracy–question trade-off," while a prompting baseline "asks most
frequently" without a matching utility gain.[^c3]

## Why it matters

It gives stall 2 a single post-hoc scalar for "was this sequence of
selection decisions worth it," complementing decision-time criteria (mutual
information, EIG, VoI) that price one question before it is asked: CU
scores a whole trajectory of ask/act choices after the fact, against a
realized accuracy rather than an expected one.

## Limits

- Uses one fixed cost per clarification question regardless of level. The
  source states this directly: "Clarification Utility also uses the same
  cost for each clarification question. This makes the metric simple and
  easy to compare across methods, but it does not model finer differences
  between intent-level and task-level questions."[^c4]
- $A_t$ is instantiated in this paper as binary assistance correctness
  judged against a simulated ground truth or an LLM judge; the metric's
  behaviour with a continuous or human-graded $A_t$ is not reported here.
- Defined and evaluated only on this paper's own multi-day, simulated
  Habitat 3.0 collaboration benchmark; `he-2026-pact` is a single 2026
  arXiv preprint, `queued` (unverified beyond the provisional check) in
  `wiki/meta/sources.json`.
- The harmonic-style trade-off ($1+\mathrm{AskRate}$ in the denominator)
  is the paper's own choice of functional form; no argument is given here
  for why this form, rather than e.g. a weighted difference, best prices
  the accuracy–question trade-off.

## Related

[[value-of-information]] · [[pact-ask-or-act]] · [[expected-information-gain]] · [[semantic-entropy]]

[^c1]: he-2026-pact — "Clarification Utility favors methods that achieve higher assistance accuracy with fewer clarification questions."
[^c2]: he-2026-pact — "when K > 0, the metric penalizes additional clarification unless it improves the final assistance outcome."
[^c3]: he-2026-pact — "ASK-RL, our primary learned instantiation, and ASK-L2D achieve strong task accuracy with lower ASK rates, suggesting a better accuracy–question trade-off."
[^c4]: he-2026-pact — "Clarification Utility also uses the same cost for each clarification question. This makes the metric simple and easy to compare across methods, but it does not model finer differences between intent-level and task-level questions."
