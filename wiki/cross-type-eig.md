---
description: "Score a pairwise comparison, a free-text prompt and an axis proposal on Tiwari et al. (2026) elicit a user's preference weights with five structurally different question types — pairwise comparison,"
aliases: []
sources: ["tiwari-2026"]
---
# Cross-type expected information gain

> Score a pairwise comparison, a free-text prompt and an axis proposal on
> the same scale by reducing every question type to a likelihood update on
> one shared posterior, then correct the raw score so no type is starved or
> favoured by construction.

## Definition / Mechanism

Tiwari et al. (2026) elicit a user's preference weights with[^s1]
five structurally different question types — pairwise comparison, rule
elicitation, dimension dominance, free-text statement, dimension proposal
(see [[elicitation-transform-types]] and [[dimension-proposal]]) — held over
one particle population $\{(w^{(i)}, \pi^{(i)})\}$. Because every type
reduces to a likelihood $p(y\mid w, q)$ over the same particles, one score
ranks all of them:

$$\mathrm{EIG}(q) = H(\text{ranking}) - \sum_{o \in O_q} P(o)\, H(\text{ranking} \mid o)$$

$H(\text{ranking})$ is the [[entropy]] of the portfolio ranking the current
posterior induces; for each hypothetical outcome $o$ of question $q$, every
particle's log-weight is counterfactually updated and the ranking's entropy
is recomputed, so the score is an expected entropy drop **on the decision
the posterior is used for**, not on the raw weights $w$ themselves — the
same move [[current-solution-strategy]] makes for minimax regret instead of
information. Because a single formula spans five unlike likelihoods, the
paper multiplies the raw score by three correction factors before ranking —
an effective-sample-size discount, a realized-success multiplier that
tracks how much each type's past use *actually* reduced entropy rather than
only its predicted score, and a curvature bonus — and adds two rules that
override the ranking directly: a force-switch that suppresses a type after
repeated dominance, and a resolved-axis deprioritization that down-weights
dimensions whose posterior weight variance is already low.

## Why it matters

This is the mechanism that lets one active-question policy choose among
question types that share nothing at the surface (a two-item comparison, an
open sentence, a proposed new axis) without a hand-set weight between them
— ordinary [[expected-information-gain]] usage compares candidates of one
type only. Evaluated on a portfolio-recommendation domain (5 personas, 50
simulated runs each, 15 elicitation turns), the system built on this
criterion reached a turn-1 regret of 0.278 against 0.651–0.678 for two
published elicitation baselines (Handa et al.'s OPEN and Austin et al.'s
PEBOL) and a turn-5 regret of 0.038 against 0.461–0.560 (Tiwari et al.
2026, Tables 2–3).

## Transfer

| | |
|---|---|
| **Home field** | [[bayesian-experimental-design|Bayesian experimental design]]: EIG defined for one likelihood over one design space, maximised over designs of a single type |
| **Here** | an elicitation loop offering five differently-shaped question types against one shared particle posterior, where a design-space-style single-type comparison does not by itself decide which type to prefer |
| **What survives** | the entropy-reduction logic and the counterfactual-averaging computation — score a candidate by how much its *hypothetical* answers would concentrate the posterior, without needing the real answer first |
| **What does not** | the raw score is not comparable across types without correction: the paper's own account of a late-turn "bounce-back" (regret rising again after turn 5 in an ablation, attributed to "competition among diverse transforms") shows an infrequently-used type can still score artificially high under plain EIG and disturb an already-concentrated posterior |

## Limits

- The three correction factors and two escape rules are described
  mechanically, not derived from a stated optimality criterion, and no
  ablation isolates this selection rule from the population-prior
  ([[population-prior-mining]]) and axis-discovery ([[dimension-proposal]])
  components that ship with it in the paper — the cold-start numbers above
  are a property of the whole system, not of this criterion alone.
- The corrections do not fully solve the problem they target: the paper
  reports the bounce-back above as an observed, open effect, not one the
  corrections are shown to remove.
- All results are from particle-filter simulations (N=200 particles)
  against LLM-simulated personas holding a hidden *linear* utility over 75
  fixed portfolios; no human-subject evaluation is reported, and the paper
  names this as its own future work.
- Read from the arXiv v1 HTML rendering, not the typeset PDF; equation and
  table numbers are as they appear in that rendering.

## Related

[[expected-information-gain]] · [[current-solution-strategy]] · [[volume-removal]] · [[elicitation-transform-types]] · [[dimension-proposal]] · [[population-prior-mining]]

[^s1]: tiwari-2026
