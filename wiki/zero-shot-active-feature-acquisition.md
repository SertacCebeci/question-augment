---
description: "A zero-shot active-feature-acquisition method — elicit from an LLM only the sufficient statistics of a discriminative MRF, then let a classical algorithm plan which feature to ask next."
aliases: ["zero-shot AFA", "disciplined elicitation", "LLM-elicited discriminative MRF"]
sources: ["perets-2026"]
---
# Zero-shot active feature acquisition via LLM elicitation

> When no labeled data exists to fit an acquisition model, ask the LLM only
> for what it can be trusted to return — not which feature to ask next, but
> the sufficient statistics of the model that decides that.

## Definition / Mechanism

Active feature acquisition (AFA) selects, at each round, which unobserved
feature to query next given a partial observation, using a model of how
features relate to a hypothesis. Perets et al. (2026) give a
zero-shot route that needs no labeled data: an LLM is asked only for the
unary deviation of each feature under a hypothesis and the pairwise
co-variation between features — "the unary deviations and pairwise
co-variations that are the sufficient statistics of a Markov random field
(MRF)".[^c1]

A classical [[planner-dynamic-stopping|planner]], not the LLM, then queries this elicited MRF to decide
what to observe next: "the LLM populates a formal probabilistic model
offline; a classical algorithm plans over it online".[^c2]

Because the LLM reliably returns only the discriminative contrast between
two hypotheses (how a feature differs between them), not each hypothesis's
distribution in isolation, the elicited model is a *difference*-MRF — a
log-odds surface, not two separate class-conditionals. That leaves the
per-class distributions that a standard acquisition criterion needs —
including conditional [[mutual-information|mutual information]] (CMI), "an informationtheoretic
feature selection criterion established in the AFA literature [23, 8]" —
underdetermined: any class-conditional pair inducing the same log-ratio is
equally consistent with it.[^c3]

The framework closes this gap with a maximum-[[entropy]] construction: "the
unique class-conditional pair consistent with the elicited log-ratio that
introduces no information beyond it", which makes CMI-driven feature
scoring computable again from discriminative-only elicitation.[^c4]

## Why it matters

For stall 2, this gives a working axis-selection answer when there is no
labeled data to fit an acquisition model at all: elicit a difference-model
from an LLM once, then score candidate features with a classical,
verifiable criterion over that model instead of asking the LLM to decide.

## Transfer

| | |
|---|---|
| Home field | Statistical relational modeling: a Markov random field's unary and pairwise potentials are fit from labeled data or a known generative process; sufficient statistics summarize observed samples. |
| Here | The potentials are elicited once, offline, from an LLM's parametric domain knowledge, with no labeled data at all; what is elicited is discriminative-only (a contrast between two hypotheses, not either distribution). |
| What survives | The separation of "what the statistics are" (an elicitation problem, given to the LLM) from "which feature to ask next" (a planning problem, given to a classical algorithm), and a maximum-entropy device for making a discriminative-only elicitation usable by criteria that classically need both class-conditionals. |
| What does not | Exact inference over the MRF — the source notes MRFs "are hard to track exactly and admit only approximate inference," so the planner runs on mean-field approximations — and any labeled-data [[calibration]] of the potentials, which a standard AFA pipeline would have and this one entirely lacks. |

## Limits

- Evaluated on one clinical cohort (Inflammatory Bowel Disease diagnosis,
  up to 216 features), one MRF class (unary + pairwise potentials, ternary
  features); generality to other domains or richer graphical structure is
  untested.
- The maximum-entropy closure is a modeling choice, not a guarantee: it
  picks the class-conditional pair introducing least information beyond
  the elicited contrast, not the true pair, so bias in the LLM's contrast
  estimate propagates unchecked into every downstream score.
- `perets-2026` is an unreviewed arXiv preprint [?] at the time of writing.

## Related

[[sufficient-statistic]] · [[maximum-entropy-principle]] · [[value-of-information]] · [[optimal-decision-tree]]

[^c1]: perets-2026 — "the unary deviations and pairwise co-variations that are the sufficient statistics of a Markov random field (MRF)"
[^c2]: perets-2026 — "the LLM populates a formal probabilistic model offline; a classical algorithm plans over it online"
[^c3]: perets-2026 — "an informationtheoretic feature selection criterion established in the AFA literature [23, 8]"
[^c4]: perets-2026 — "the unique class-conditional pair consistent with the elicited log-ratio that introduces no information beyond it"
