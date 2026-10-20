---
description: "Expected information gain about which generative model is true, not its parameters: an action is scored by how much its outcome would separate rival structures before one is committed to."
aliases: ["information gain over models", "structure information gain", "active reasoning", "active model selection"]
sources: ["arxiv-2512-21129"]
---
# Structure information gain

Expected free energy, as used in active inference, already carries two
information-gain terms: one over latent states and one over parameters of a
generative model. The three-ball paper adds a third, "information gain that
pertains to the structure of" the generative model.[^c1] Structure here means
the rival hypotheses about how outcomes are generated, each a reduced model of
the same parent, treated as a random variable over which a prior is placed.

The quantity is the expected KL divergence between the posterior over models
with and without the outcome that a policy would produce: "The expected
information gain is the expected KL divergence between the posterior probability
of a model with, and without, the outcomes under a particular policy."[^c2] The
predictive posteriors over models that it needs are evaluated by
[[bayesian-model-reduction]], so each candidate action is scored without
refitting any candidate. The action it prefers is the one expected to make the
leading model stand out from the rest. The paper calls the resulting behaviour
"active reasoning" or active reduction.

## What it contributes, as measured

The effect is measured as a contribution, not as a standalone term. Removing
the model and parameter information-gain terms together changes the mean
discovery time, "reducing from 28.5 to 19.4 trials", in the paper's
three-ball simulations.[^c3]
The model term matters late in evidence accumulation: "the expected information
gain over models becomes important at later stages of evidence accumulation",
that is, when only a few plausible models remain.[^c4] The state and parameter
terms are not independent of it. Without any information gain the performance
"fell from an average" score of 150 to 51, and the paper reads the gap as "a
synergistic effect of resolving uncertainty about both states" and parameters.[^c5]

## Transfer

| | |
|---|---|
| **Home field** | Bayesian optimal experimental design, where the index is a hypothesis or a parameter and the design is an experiment (Lindley-style expected information gain) |
| **Here** | the index is a set of discrete, reduced likelihood models; the design is one action of a partially observed agent, scored for its next step only |
| **What survives** | the criterion itself: rank an action by how much its outcome would separate candidate structures before the answer is known, and only then commit to one |
| **What does not** | the closed-form scoring: it holds because the candidates are Dirichlet reductions of one parent. Models that are not nested in a common parent have no such shortcut, and the text does not address them |

## Limits

- **One step.** The paper restricts the term to the next action: "Note that this
  expected information gain does not lend itself to evaluation over sequences of
  actions."[^c6] Longer planning uses the other terms, and the model term is
  switched on after the best model has been selected.
- **Predictive, not posterior.** The Q over models is a predictive posterior
  under the model average: "Note that Q here is a predictive posterior, as
  opposed to an approximate posterior over models."[^c7]
- **It selects, it does not commit.** The term "does not, in and of itself,
  commit to using a new model."[^c8] Commitment is a separate threshold
  ([[bayesian-model-reduction]]), so a high-gain action can be taken with no
  model yet selected.
- **The hypothesis space is given.** "An outstanding issue is the elaboration of
  alternative models."[^c9] The paper reduces the rule search to a set of 81
  isomorphism-constrained likelihood mappings,[^c12] and notes that mutual-information
  considerations alone are weak: "sparsity is a necessary but not sufficient"
  condition.[^c10] What counts as a rival is decided before the term can act.
- **Simulation only.** All results are numerical, on one task whose structure
  was built in by hand. Among the 64 games one committed early to the wrong
  model.[^c11] The text offers no evidence about how the term behaves on unstructured
  questions.

## Related

- [[expected-information-gain]] — the same functional with parameters or
  states as the index; this note is the case where the index is the model
  itself.
- [[bayesian-model-reduction]] — the post-hoc evaluation of the predictive
  posteriors over models that makes this term cheap.
- [[active-inference-epistemic-decomposition]] — the parameter-level
  novelty term of the same expected free energy, decomposed exactly.
- [[mutual-information]] — the maximum-mutual-information constraint the paper
  uses to motivate which rival models are worth entertaining.

[^c1]: arxiv-2512-21129 — "we introduce a third sort of information gain that pertains to the structure of"
[^c2]: arxiv-2512-21129 — "The expected information gain is the expected KL divergence between the"
[^c3]: arxiv-2512-21129 — "reducing from 28.5 to 19.4 trials"
[^c4]: arxiv-2512-21129 — "the expected information gain over models becomes important"
[^c5]: arxiv-2512-21129 — "a synergistic effect of resolving uncertainty about both states"
[^c6]: arxiv-2512-21129 — "information gain does not lend itself to evaluation over sequences of actions"
[^c7]: arxiv-2512-21129 — "Note that Q here is a predictive posterior, as opposed to an approximate posterior"
[^c8]: arxiv-2512-21129 — "It does not, in and of itself, commit to using a new model"
[^c9]: arxiv-2512-21129 — "An outstanding issue is the elaboration of alternative models"
[^c10]: arxiv-2512-21129 — "sparsity is a necessary but not sufficient"
[^c11]: arxiv-2512-21129 — "was applied prematurely"
[^c12]: arxiv-2512-21129 — "the three-ball paradigm offers 81 possible likelihood mappings"
