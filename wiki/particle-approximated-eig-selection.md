---
description: "An LLM proposes a finite pool of candidate questions or experiments; each is scored by expected information gain approximated over a small set of SMC particles, and the arg max is asked."
aliases: ["particle-approximated expected information gain", "LLM-guided active inquiry"]
sources: ["piriyakulkij-2026"]
---
# Particle-approximated EIG selection

> A way to make [[expected-information-gain|EIG]] selection computable when the
> [[possible-worlds|hypothesis space]] is open-ended natural language: replace "sum over $\theta$"
> with "sum over a handful of LLM-maintained particles," and replace "the
> candidate set of all questions" with "a handful an LLM just proposed."

## Mechanism

Piriyakulkij, Acquaviva, Langenfeld, Tenenbaum & Ellis (2026)
maintain a small population of $K$ weighted particles $\{h^i\}$ — mental
programs mixing a natural-language description with executable code — as an
approximation to the posterior $p(h\mid e_{1:t})$, updated by LLM-guided
Sequential Monte Carlo (their "LLM-SMC-S"). To pick the next experiment or
question $\xi$, an LLM proposes a finite set of candidate $\xi$'s (since the
true candidate set — "infinitely many" experiments — cannot be enumerated),
and each is scored by

$$\xi^* = \arg\max_\xi \; \mathbb{E}_{e\sim p(e\mid \xi, e_{1:t})}\Big[D_{KL}\big(p(h\mid e_{1:t}, e)\,\|\,p(h\mid e_{1:t})\big)\Big]$$

with the three distributions ($p(h\mid e_{1:t})$, $p(e\mid\xi,e_{1:t})$,
$p(h\mid e_{1:t},e)$) all computed over the current particle set standing in
for the hypothesis space, rather than over an explicit enumerable prior.[^c1]

In a web-shopping proof-of-concept — a finite space of candidate products
plays the role of $h$, and $\xi$ is a natural-language question to the
customer — the model's questions gave higher average expected reward and
higher measured [[entropy]] reduction per question than a vanilla LLM prompt and
than ReAct (an LLM prompted to reason before acting), across four sequential
questions.[^c2]

## Why it matters

This is a second practical route to computing EIG in an LLM setting beside
the [[semantic-entropy]]-over-sampled-answers route in [[expected-information-gain]]:
here the intractable sum is truncated on *both* sides — a finite proposed
candidate pool standing in for all possible questions, and a finite particle
population standing in for the posterior over hypotheses — rather than by
sampling only the answer distribution.

## Transfer

| | |
|---|---|
| **Home field** | [[bayesian-experimental-design|Bayesian experimental design]] (Lindley 1956): EIG over an explicit prior and an enumerable design space, computed exactly or by a principled nested-Monte-Carlo estimator |
| **Here** | an open-ended natural-language hypothesis space with no written prior and no enumerable design space |
| **What survives** | the score-before-answering logic and the arg max criterion itself — EIG is still computed from the *distribution* of an answer, not the answer received |
| **What does not** | any error bound on the approximation. Both truncations (finite LLM-proposed candidates, finite particles) are unquantified: the paper reports that its selections beat two LLM baselines on one task's reward and entropy-reduction curves, not a bound on how far the particle-based EIG estimate sits from the true value |

## Limits

- The information-gain claim rests on one task (a synthetic web-shopping
  assistant with an assumed finite, enumerable product space and an exact
  Bayesian update over it) — the "beyond code" section is explicitly a
  proof-of-concept, not the paper's main experimental line (which is
  induction over list functions, number concepts, and Zendo rules, not
  question selection).[^c3]
- No ablation isolates the particle approximation from the candidate-proposal
  step: better questions could come from better proposals, a better score, or
  both, and the paper does not separate them.
- Baselines are two LLM prompting strategies (vanilla, ReAct), not a
  classical enumerable-EIG or [[value-of-information]] baseline computed
  without particles.
- `piriyakulkij-2026` is an arXiv preprint (Sep 2026), not yet peer-reviewed.

## Related

[[expected-information-gain]] · [[question-asking-as-program-generation]] · [[value-of-information]] · [[semantic-entropy]]

[^c1]: piriyakulkij-2026 — "we treat humans as considering different experiments ξ, and pick the experiment which maximizes expected information gain, under their particle-based approximate probabilistic beliefs"
[^c2]: piriyakulkij-2026
[^c3]: piriyakulkij-2026 — "As a proof-of-concept, we assume a finite hypothesis space of products a customer can purchase, and perform exact Bayesian belief updates."
