---
description: "An exact identity splits active-inference planning into a reward term, a planning-uncertainty term, and an epistemic term separating into ambiguity and novelty (parameter information gain)."
aliases: ["entropy-corrected form of active inference", "EFE-based planning objective", "ambiguity-novelty decomposition of expected free energy"]
sources: ["nuijten-2026-what"]
---
# EFE entropy-correction decomposition

> Whether to ask (gather information) or act now falls out of an exact
> algebraic split of the planning objective into a reward term and two
> uncertainty terms — one of which, novelty, is an expected-information-gain
> term over the agent's own latent parameters.

## Definition / Mechanism

Nuijten et al. (2026) start from a prior result — Expected Free Energy (EFE)
minimization rewritten as Variational Free Energy (VFE) minimization on a
generative model augmented with "epistemic priors" over which variables are
controlled, inferred, or observed. Theorem 1 proves this augmented VFE
equals the original (predictive) VFE plus explicit [[entropy]]-correction terms,
"an exact algebraic identity," not an approximation.[^c1]

Combined with a separate planning correction (an action-uncertainty penalty
that turns marginal inference into policy optimization), the full
EFE-based planning objective is a sum of three pieces: a reward
(cross-entropy-to-preferences) term, a planning-correction term, and an
epistemic-correction term. The epistemic term itself splits into two
named quantities the paper identifies with standard active-inference
usage: **[[efe-planning-as-variational-inference|ambiguity]]**, the expected entropy of the observation given the
current state and parameters (an expected-loss-of-precision term), and
**novelty**, the expected information gain about the latent parameters
$\theta$ — "the remaining … term enters negatively and rewards novelty,
the expected information gain about θ." Ambiguity depends only on the
observation kernel at a state already reachable; novelty depends on the
full joint posterior over observations, states and parameters.[^c2]

## Known as

| Field | Name there | Relation |
|---|---|---|
| This paper (Nuijten, Lukashchuk, de Vries & van de Laar, 2026) | entropy-corrected form of active inference / EFE-based planning objective | exact |
| Active inference (per the paper's own attribution to Da Costa et al. 2020) | ambiguity / novelty split of epistemic value | close — same two quantities, named in the field before this paper's algebraic derivation of them as entropy corrections |

## Why it matters

The paper's own grid-world experiments show the split is not cosmetic: a
message-[[proactive-expertise-clarification|passing]] scheme that treats the epistemic priors as ordinary,
recomputed factors (an "alternating heuristic") captures ambiguity but not
novelty, while the full joint variational scheme (AIF-MP) captures both.
Where an action's only epistemic value is novelty — a reading that narrows
an unknown parameter without itself changing the observation model, as in
RockSample and Wumpus World — only the novelty-aware scheme finds any value
in checking: AIF-MP retrieves 98.7% of good rocks (reward 4.01) in
RockSample and reaches 40.7% success in Wumpus World, while the
ambiguity-only heuristic performs at the level of a [[planner-dynamic-stopping|planner]] with no
epistemic term at all (0% rock retrieval; 5.0% vs. a 5.5% no-epistemic
baseline in Wumpus World).[^c3]

## Transfer

| | |
|---|---|
| **Home field** | Active inference / variational message passing: a full generative model over actions, states, parameters and observations, planned by message passing on a graphical model |
| **Here** | An asking agent choosing whether an information-gathering action (a "question") is worth its cost, versus acting on current beliefs |
| **What survives** | The exact decomposition into reward + planning-uncertainty + (ambiguity − novelty), and the identification of novelty with expected information gain about a latent parameter — the same object this wiki tracks as [[expected-information-gain]] |
| **What does not** | The derivation needs a closed generative model with an explicit, low-dimensional latent $\theta$ and a defined observation kernel; it does not by itself say how to build such a model for open-ended natural-language questions, where no $\theta$ is given in advance |

## Limits

- Theorem 1 is exact only for the specific epistemic-prior construction of
  the paper it builds on (Nuijten et al. 2026b) — priors (7a)-(7c) — not
  for an arbitrary choice of augmenting priors.
- The ambiguity/novelty separation is demonstrated on three synthetic
  grid-world benchmarks with a small, enumerable parameter space (up to 25
  configurations); no result is reported at higher-dimensional or
  continuous $\theta$.
- The planning correction the paper composes with (turning marginal
  inference into policy optimization) is attributed to prior work the
  paper cites but this note has not independently read; it is reported
  here only as the paper describes it.

## Related

[[active-inference-context-acquisition]] · [[expected-information-gain]] · [[mutual-information]] · [[value-of-information]]

[^c1]: nuijten-2026-what
[^c2]: nuijten-2026-what — "The first sum is the planning correction; the second sum is the EFE correction. Only their combination yields proper EFE-based planning."
[^c3]: nuijten-2026-what — "AIF-MP is the only method that checks and samples, retrieving 98.7% of good rocks for an average reward of 4.01. Every baseline, including Nuijten-MP, walks straight to the exit (reward 1.00, zero retrieval)"
