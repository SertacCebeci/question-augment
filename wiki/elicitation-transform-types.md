---
description: "Four ways a question can touch an axis that already exists in the model — Tiwari et al. (2026) fix a preference state — a particle population over utility weights, a set of active dimensions,"
aliases: []
sources: ["tiwari-2026"]
---
# Elicitation transform types

> Four ways a question can touch an axis that already exists in the model —
> a comparison, a rule probe, an axis-to-axis trade-off, or an open
> sentence — defined so that each reduces to the same kind of update on one
> shared posterior.

## Definition / Mechanism

Tiwari et al. (2026) fix a preference state — a particle[^s1]
population over utility weights, a set of active dimensions, and a set of
symbolic rules — and then define, for each of four question *formats*, a
likelihood $p(y \mid w, q)$ that turns a returned answer into an additive
update on every particle's log-weight ($\ell^{(i)} \mathrel{+}= \log
p(y \mid w^{(i)}, q)$):

- **Pairwise comparison** — a Bradley-Terry likelihood over two
  alternatives' utilities.
- **Rule elicitation** — a probe for a threshold or dependency between
  named dimensions, read into a Dirichlet posterior over whether a
  candidate rule holds.
- **Dimension dominance** — a Bradley-Terry likelihood over the *weights*
  of two dimensions directly, rather than over two decision alternatives.
- **Free-text statement** — an open sentence scored by having a language
  model return a signed activation for every active dimension, normalised
  into a prior-centred log-likelihood update.

A fifth type, [[dimension-proposal|dimension proposal]], grows the
active-dimension set itself rather than updating an existing one, and is
kept as a separate note because it answers a different question (which
axes exist, not how a question touches one that already does). Because
every one of the four types above ends in the same additive update on the
same particles, a single ranking criterion ([[cross-type-eig]]) can compare
a comparison question against an open sentence without a hand-set exchange
rate between them.

## Why it matters

The wiki's stall-3 map has answers for wording effects
([[survey-response-model]]), presupposition ([[presupposition-accommodation]])
and format restriction ([[structured-output]]), but nothing that says how a
*fixed menu of question formats* can be scored on one currency once the
underlying state is Bayesian rather than a raw answer log. This is a
concrete instance of formulation choice becoming a modelling choice: the
format a question takes (comparison, probe, trade-off, open sentence) is
fixed by which likelihood the format admits, and only formats with a
stated likelihood enter the ranking [[cross-type-eig]] runs over.

## Transfer

| | |
|---|---|
| **Home field** | sequential Monte Carlo / particle filtering (Bayesian statistics): a population of weighted particles approximating a posterior, updated by successive likelihood evaluations |
| **Here** | the particles represent a user's unknown utility weights, and the "observations" are answers to differently-formatted natural-language questions rather than i.i.d. draws from one sensor |
| **What survives** | the update rule itself — multiply in a likelihood, keep the particle population as the posterior — needs no change per question format, which is exactly what makes a shared ranking criterion possible |
| **What does not** | the standard filter's convergence guarantee is stated for a fixed, known likelihood family; here the free-text likelihood is itself an LLM's judgement rather than a modelled sensor, so the update is only as sound as that judgement, and the paper reports no [[calibration]] check on it |

## Limits

- The three fixed-axis likelihoods (pairwise, rule, dominance) are
  described by their functional form but their parameters (e.g. the
  Bradley-Terry temperature) are not reported as fitted or validated
  against real human answers in this paper — only against LLM-simulated
  personas.
- The free-text likelihood's quality depends entirely on the scoring LLM's
  own judgement of "signed activation per axis," which is not itself
  measured for accuracy against the personas' hidden true weights.
- Evaluated only in the portfolio-recommendation domain with a fixed
  75-item catalog; whether the four-type menu is exhaustive for other
  decision domains is not addressed.
- The Bradley-Terry form's own origin (paired-comparison psychometrics) is
  named on the paper's own citation; it is not independently verified
  against the original source in this pass.

## Related

[[cross-type-eig]] · [[dimension-proposal]] · [[survey-response-model]] · [[structured-output]] · [[bayesian-estimation]]

[^s1]: tiwari-2026
