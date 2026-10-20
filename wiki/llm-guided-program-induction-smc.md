---
description: "A bounded set of weighted particles, each a mental program mixing language and code, approximates the hypothesis posterior and is updated by LLM-proposed revisions plus reweighting."
aliases: ["LLM-SMC-S", "LLM-guided sequential Monte Carlo", "mental programs"]
sources: ["piriyakulkij-2026"]
---
# LLM-guided program induction by sequential Monte Carlo

> Keep $|W|$ tractable by never writing it down: hold a small weighted
> population of candidate hypotheses, let an LLM propose revisions of them as
> evidence arrives, and reweight-and-resample instead of enumerating.

## Mechanism

Piriyakulkij, Acquaviva, Langenfeld, Tenenbaum & Ellis (2026)
represent a hypothesis $h$ as a mental program with two parts — a natural-
language description and a Python implementation — so that a prior favouring
short descriptions and a likelihood favouring programs whose execution
matches the evidence together define $p(h\mid e_{1:T})\propto p(h)\prod_{t\le T} p(e_t\mid h)$,
updated online as examples $e_1,e_2,\dots$ arrive. Because this posterior is
intractable over the open-ended space of possible programs, the model tracks
only $K$ weighted particles: on each new observation, an LLM proposes revised
hypotheses conditioned on the *entire* current particle set (not one particle
at a time, departing from standard SMC), each particle is reweighted by how
well it explains the evidence so far, and resampling prunes low-probability
particles and multiplies high-probability ones so weights stay uniform.[^c1]

At a search budget of 5 LLM-proposed hypotheses per step, the model matched
average human accuracy on 250 held-out algorithm-induction tasks (Rule et
al.'s benchmark) better than a hand-engineered search over up to 500,000
programs, and fit trial-by-trial learning curves best (by MSE) for 70/100 of
the easier tasks.[^c2]

## Why it matters

The particle count $K$ functions as an explicit, tunable stand-in for
"how small is $|W|$ held to" (stall 7): reducing $K$ from 70 to 20 reproduced
a human cognitive-load manipulation (a concurrent distractor task) as
*stronger* anchoring in a sequential number-concept task, and separately, the
fit between model and human accuracy on the Zendo rule-induction task followed
a U-shaped curve in $K$ — more particles (more compute) did not monotonically
improve the match to bounded-rational human behaviour.[^c3]

## Limits

- The anchoring/garden-pathing replication (number concepts, Thaker et al.'s
  task) and the Zendo compute-budget curve are both comparisons of one
  specific particle count schedule to one specific human dataset; neither is
  a general law relating $K$ to fit quality outside these two tasks.
- The "propose from the whole particle set, not per-particle" step departs
  from standard SMC and its own convergence guarantees are not established
  in the paper — the method is validated by fit to human data, not by a
  proof that it approximates $p(h\mid e_{1:T})$ with any stated error.
- The natural-language prior and code likelihood are both themselves LLM
  calls; systematic LLM biases (e.g. favouring certain phrasings) enter the
  "posterior" undetected and are not separated from genuine evidence.
- `piriyakulkij-2026` is an arXiv preprint (Sep 2026), not yet peer-reviewed.

## Related

[[particle-approximated-eig-selection]] · [[bounded-rationality]] · [[possible-worlds]] · [[expected-information-gain]]

[^c1]: piriyakulkij-2026
[^c2]: piriyakulkij-2026
[^c3]: piriyakulkij-2026 — "We model this cognitive load by reducing our number of particles, which replicates the effect."
