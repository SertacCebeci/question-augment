---
description: "An acquisition function that scores a pairwise query by the posterior expected utility of the best option after seeing the answer, provably one-step Bayes-optimal when responses are noise-free."
aliases: ["qEUBO", "expected utility of the best option"]
sources: ["astudillo-2023", "dispoto-2026", "arxiv-2512-14263"]
---
# qEUBO

> Do not score a query by how much it would tell you about the utility
> function; score it by how much better the option you would then pick
> becomes.

## Definition / Mechanism

qEUBO ("[[expected-utility|expected utility]] of the best option") is an acquisition function
for **preferential Bayesian optimization**: a decision maker has a latent
utility $u(x)$ over candidate options, observed only through pairwise
comparisons, and a Gaussian-process posterior is fit over $u$ from the
comparisons seen so far. Rather than scoring a candidate query by how much
it would reduce [[entropy]] or posterior volume over $u$ (as
[[volume-removal]] and information-gain criteria do), qEUBO scores it by
the expected value, under the current posterior, of $\max$ utility among
the query's options *after* the decision maker's answer updates that
posterior — the same "look one step ahead at what you would then choose"
move as the knowledge-gradient acquisition function in ordinary Bayesian
optimization. Astudillo, Lin, Bakshy & Frazier (2023)
"propose the expected utility of the best option (qEUBO) as a novel
acquisition function for PBO."[^c1]

When the decision maker's answers are noise-free, the paper shows qEUBO
"is one-step Bayes optimal and thus equivalent to the popular knowledge
gradient acquisition function," and that under noisy answers it "enjoys an
additive constant approximation guarantee to the one-step Bayes-optimal
policy."[^c2]

Asymptotically, "qEUBO's Bayesian simple regret converges to
zero at a rate $o(1/n)$ as the number of queries, $n$, goes to infinity,"
which the paper contrasts with an alternative whose regret "can fail to
converge to zero."[^c3]

## Why it matters

This is a selection criterion built on the same axis — which pairwise
question to pose next — as [[volume-removal]] and
[[expected-information-gain]], but it prices a candidate query by its
effect on the *decision* the posterior will support rather than by the
entropy or volume removed from the posterior itself: a query can reduce
uncertainty about $u$ without changing which option currently looks best,
and qEUBO scores that query low where an information-theoretic criterion
would not. Dispoto, Restelli & Ventre (2026) deploy this
exact mechanism inside a decision-support agent: a portfolio manager is
shown 8 initial random pairs of portfolios, a `PairwiseGP` model (Chu &
Ghahramani's Gaussian-process preference model) is fit to the choices, and
qEUBO then picks each of 20 further pairs to show, after which the
posterior-mean preference-weight vector is read off and fixed.[^c4]

## Transfer

| | |
|---|---|
| **Home field** | preferential Bayesian optimization: choosing the next pairwise query to optimize an unknown, noisily-observed utility over a continuous or discrete option set |
| **Here** | any asker choosing which pairwise (or $K$-way) question to pose next to an answerer whose choices reveal a latent utility or preference weighting |
| **What survives** | the reframing itself — score a candidate question by the downstream decision it would improve, not by the uncertainty it would remove — and the one-step Bayes-optimality argument that justifies it when answers are close to noise-free |
| **What does not** | the noise-free Bayes-optimality proof and the $o(1/n)$ regret rate assume a well-specified GP prior over $u$ and a probit/softmax response model calibrated to the real answerer; dispoto-2026's own use reports an identifiability problem the guarantee says nothing about — different preference-weight vectors can induce near-identical option rankings when the underlying objectives are correlated, so a low-regret query sequence need not recover a unique $u$ |

## Limits

- The Bayes-optimality and regret results are one-step-lookahead guarantees
  over the modelled GP posterior; they say the *next* query is priced
  correctly under that model, not that the recovered utility is unique or
  that the model is well specified for a real human answerer.
- The equivalence to knowledge gradient and the regret bound are read from
  the paper's abstract and its stated theorems, not derived here; this note
  does not reproduce the proof.
- dispoto-2026 is the only reported deployment read for this note: 8
  initialization queries, 20 active-learning queries, one simulated
  portfolio-manager domain. It is illustration of the mechanism in use, not
  independent evidence for the guarantees above.
- `astudillo-2023` is cited from its abstract and the paper's own
  claims; the verifier locates the exact wording against the archived
  extract once it exists.
- Applied over the leaves of a tree instead of a GP, qEUBO's between-leaf
  comparisons are used, but inside a single leaf it degenerates: the leaf
  has a constant predictive mean and symmetric comparison probability, so
  "within a single leaf, qEUBO collapses."[^c5] The tree-surrogate paper
  therefore samples within-leaf pairs by a separate rule, used only in its
  discrete item-set experiments.[^c5]

## Related

[[volume-removal]] · [[expected-information-gain]] · [[cross-type-eig]] · [[value-of-information]] · [[current-solution-strategy]] · [[pairwise-consistency-split]] — a greedy tree surrogate on which this acquisition rule is run over leaf posteriors

[^c1]: astudillo-2023
[^c2]: astudillo-2023 — "is one-step Bayes optimal and thus equivalent to the popular knowledge gradient acquisition function"
[^c3]: astudillo-2023
[^c5]: arxiv-2512-14263 — "within a single leaf, qEUBO collapses"
[^c4]: dispoto-2026 — "we employ the expected utility of the best option (qEUBO) acquisition function to dynamically generate the most informative candidate pairs for the PM to evaluate next. After 20 iterative active learning steps, the elicitation process concludes, and we extract the Λ𝑃𝑀 vector that maximizes the posterior mean"
