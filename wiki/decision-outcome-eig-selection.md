---
description: "Scores a tradeoff question by the entropy reduction it causes in a downstream decision's option distribution, not the preference posterior, and stops once that distribution is confident."
aliases: ["decision-aware question selection", "decision-focused EIG"]
sources: ["arxiv-2604-18122"]
---
# Decision-outcome EIG selection

> Not every question that shrinks uncertainty about *you* shrinks uncertainty about *what you should pick* — so score the second thing, not the first.

## Definition / Mechanism

Jain et al. (2026) build D<small>ECISIVE</small>, a
document-grounded decision assistant that separates an objective
option-scoring matrix $S$ (option $\times$ factor, extracted from source
documents) from a latent, per-user preference vector $w^*$ over the same
$K$ factors. Uncertainty about $w^*$ is tracked by a set of $P=500$
weighted "persona" particles sampled from a uniform Dirichlet prior, each a
candidate $w^{(p)}$; a user's answer to a pairwise tradeoff question
($f_a \succ f_b$) reweights the particles by a sigmoid update
$\pi^{(p)} \leftarrow \pi^{(p)}\cdot\sigma(\kappa\cdot(w_a^{(p)}-w_b^{(p)}))$,
which down-weights but never zeroes an inconsistent particle.[^c1]

The candidate-question score is not computed over this particle posterior
directly. Each particle, combined with $S$, votes for one option
($\arg\max_i (Sw^{(p)})_i$); marginalizing the particle weights over these
votes gives a decision distribution $\chi\in\mathbb{R}^M$ over the $M$
options. A candidate question comparing factors $a,b$ is scored by the
expected reduction in $\chi$'s entropy across its two simulated answers,
$\mathrm{EIG}(a,b) = H(\chi) - \mathbb{E}_{\text{resp}}[H(\chi^{(\text{resp})})]$,
and the maximizer is asked. This restricts questioning to the trade-offs
that could still flip the leading option, ignoring factors any persona
agrees do not change the outcome.[^c2]

The dialogue stops on a decision-stability rule rather than a fixed turn
count or a threshold on preference uncertainty: it terminates once
$\max_i \chi_i \geq \tau$ (they fix $\tau=0.85$), then recommends the
option with the highest expected weighted utility under the final
particle-weighted belief.[^c3]

## Why it matters

Two axes of belief exist here — over the answerer's preferences, and over
the decision those preferences imply — and they need not shrink together:
a factor both personas already agree matters little can still carry
residual entropy in $w^*$ without moving $\chi$. Scoring and stopping on
the second axis, not the first, is what lets the system ask fewer
questions than a comparable dialogue baseline while reaching a
substantially higher decision accuracy: on Education and Finance it
reaches a confident decision in 5-6 questions on average and under 2 in
Hiring, "fewer than Active Preference Inference (∼7.5-9.7 questions) and
comparable to B3 (∼4-7 questions), but with substantially higher
accuracy."[^c4]

## Limits

- The question-generation candidate set is the fixed $\binom{K}{2}$ set of
  factor pairs extracted per scenario ($K\approx 11$ on average); the paper
  does not test open-ended or free-text questions, only tradeoff pairs
  over a pre-extracted, closed factor list — unlike
  [[particle-approximated-eig-selection]], where both the hypothesis
  space and the candidate question set are themselves LLM-generated and
  open-ended.
- Evaluated against a deterministic user simulator that always answers by
  comparing the true $w_a^*, w_b^*$ (with a separate Bradley-Terry noise
  ablation); no human-user study.
- The 0.85 confidence threshold is a fixed hyperparameter reported to work
  well, not derived from a cost-of-error analysis; a stopped-early wrong
  recommendation is possible whenever the persona population's collective
  confidence outruns its correctness (Top-1 accuracy is 79-90%, not 100%,
  at the point the rule fires) — this gap is unverified in the extract.
- `arxiv-2604-18122` is an unreviewed arXiv preprint (Apr 2026).

## Related

[[expected-information-gain]] · [[particle-approximated-eig-selection]] · [[bayesian-experimental-design]] · [[value-of-information]]

[^c1]: arxiv-2604-18122
[^c2]: arxiv-2604-18122 — "Not all questions are equally informative. To maximize efficiency, we select questions that reduce uncertainty in the final decision, rather than just in the preference weights."
[^c3]: arxiv-2604-18122 — "Instead of asking a fixed number of questions, we employ a dynamic stopping criterion based on decision stability. The dialogue terminates when the confidence in the most likely option exceeds a threshold (maxi χi ≥ τ , with τ = 0.85)."
[^c4]: arxiv-2604-18122 — "D ECISIVE requires only 5-6 questions on average to reach a confident decision in Education and Finance, and under 2 questions in Hiring where candidates are more clearly differentiated. This is fewer than Active Preference Inference (∼7.5-9.7 questions) and comparable to B3 (∼4-7 questions), but with substantially higher accuracy."
