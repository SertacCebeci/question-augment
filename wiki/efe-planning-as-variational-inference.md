---
description: "Minimizing one variational free-energy functional on a generative model augmented with three epistemic priors provably decomposes into expected-free-energy plan cost plus a complexity term."
aliases: ["EFE-based planning as variational inference", "epistemic priors (risk", "ambiguity", "novelty)"]
sources: ["nuijten-2026"]
---
# EFE planning as variational inference

> Goal-seeking and information-seeking action selection do not need two
> objectives bolted together: adding three specific priors to a generative
> model and minimizing one variational free energy functional produces the
> instrumental/epistemic split as a byproduct, not a design choice.

## Definition / Mechanism

For an agent with generative model $p(y,x,u,\theta)$ and a preference prior
$\hat p(x)$ over future states, Nuijten, van de Laar & de Vries (2026)
define a Variational Free Energy functional $F[q]$ over the generative model
augmented with a preference prior and three **epistemic priors** — over
plans $\tilde p(u)\propto\exp(H[q(x\mid u)])$ (a risk term), over states
$\tilde p(x)\propto\exp(\mathbb E_{q(\theta\mid x)}[-H[q(y\mid x,\theta)]])$
(an ambiguity term), and over observation-state pairs
$\tilde p(y,x)\propto\exp(D_{KL}[q(\theta\mid y,x)\Vert q(\theta\mid x)])$ (a
novelty term). Their main result demonstrates that minimizing a Variational
Free Energy functional with appropriately chosen priors yields a
decomposition into expected plan costs (the EFE) plus a complexity term.[^c1]

The three epistemic priors correspond one-to-one to risk-, ambiguity- and
novelty-seeking behavior: the epistemic priors account for entropic
contributions from conditional state, observation, and parameter beliefs,
corresponding to the risk, ambiguity, and novelty terms, respectively; the
paper identifies the specific epistemic priors that induce risk-minimizing,
ambiguity-reducing, and novelty-seeking behavior.[^c2]

Across a deterministic T-maze, a stochastic Reactivity Maze and a
partially-observable MiniGrid DoorKey task, the results demonstrate that
the epistemic priors from Proposition 1 are necessary and sufficient for
inducing the information-gathering behavior that distinguishes active
inference from standard planning-as-inference methods: removing them
(the `Fmarginal`/`Fplanning` ablations) collapses information-seeking, and
restoring them (`Factive`) recovers it.[^c3]

## Why it matters

For stall 2 (which axis first), this is a formal existence proof that a
single scalar objective — one variational free energy, no separately-tuned
exploration bonus — can select between a goal-directed action and an
information-seeking one, provided the model carries the right priors. It
gives [[active-inference-context-acquisition]]'s expected-free-energy
action score a derivation: EFE is not an ad hoc combination of
instrumental and epistemic terms, it is what falls out of ordinary
variational inference once the generative model is augmented this way.

## Limits

- The decomposition (Proposition 1) requires the specific factorization
  $q(y,x,u,\theta)=q(y,\theta\mid x)q(x\mid u)q(u)$ and the three priors
  exactly as chosen in (6a)-(6c); a different factorization or different
  prior choice is not covered by the proof.
- "Necessary and sufficient" is an empirical claim validated on three
  small environments (T-maze, Reactivity Maze, MiniGrid DoorKey), not a
  proof that the priors are necessary in general — the paper's own DoorKey
  result shows the priors "neither help nor hinder" when the task is pure
  spatial navigation without a latent cue to discover.
- The generative model, plan and action spaces are all discrete and
  finite in the validation; nothing here establishes the decomposition
  scales to continuous or language-structured action spaces (e.g. natural
  language questions).

## Related

[[active-inference-context-acquisition]] · [[mutual-information]] · [[expected-information-gain]] · [[bounded-rationality]]

[^c1]: nuijten-2026 — "Our main result demonstrates that minimizing a Variational Free Energy functional with appropriately chosen priors yields a decomposition into expected plan costs (the EFE) plus a complexity term."
[^c2]: nuijten-2026 — "The epistemic priors account for entropic contributions from conditional state, observation, and parameter beliefs, corresponding to the risk, ambiguity, and novelty terms, respectively."
[^c3]: nuijten-2026 — "The results demonstrate that the epistemic priors from Proposition 1 are necessary and sufficient for inducing the information-gathering behavior that distinguishes active inference from standard planning-as-inference methods."
