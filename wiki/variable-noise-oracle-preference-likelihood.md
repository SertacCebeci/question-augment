---
description: "Maps an answerer's self-reported confidence to the observation-noise scale of a pairwise probit likelihood, so an unsure comparison constrains the fitted posterior less than a sure one."
aliases: ["variable-noise oracle", "confidence-aware probit likelihood", "VPL confidence mapping"]
sources: ["arxiv-2604-20210", "zhang-2026"]
---
# Variable-noise oracle (confidence-mapped preference likelihood)

> Do not treat every comparison an answerer makes as equally informative;
> ask how sure they were, and let that set how much the answer moves you.

## Definition / Mechanism

In pairwise preference learning a decision maker (human or agent) is shown
two options and returns which one they prefer; a probabilistic model —
here a Gaussian-process posterior over a latent utility $f$ — is fit to
the accumulated comparisons and used to pick the next pair and to
recommend a final option. [[zhang-2026|Zhang, Zhu, Pourebadi Khotbehsara,
Dao, Bıyık & Culbertson (2026)]] add a second output to every comparison
besides the binary preference: "A confidence score 𝑐𝑡 ∈ {1, . . . , 5}
(Likert scale: 1 = Very" — unsure to very sure.[^c1]

That confidence is not logged as metadata; it is mapped, through a
monotone function $u(\cdot)$ with $u(1) > \cdots > u(5) > 0$, straight into
the noise term of the probit likelihood that fits the posterior — "with
$u(1) > \cdots > u(5) > 0$, so lower confidence" scores a comparison as
noisier the less sure the answerer was. A low-confidence answer
therefore constrains the posterior less than a high-confidence one on the
same pair, because it is modelled as coming from a noisier channel, not
because its binary label is discounted or its weight in a loss is
hand-tuned. The paper names this explicitly: "we treat the user as a
variablenoise oracle via the mapping $u(c)$, which modulates the"[^c3]

The mechanism is deliberately **decoupled from query selection**. The
acquisition step that picks the next pair to show (an expected-
information-gain criterion, see [[expected-information-gain]]) must score
candidate pairs *before* the answer — and therefore before the confidence
— exists, so it falls back to a fixed nominal noise scale $\sigma_{nom}$
for that one lookahead computation only: "at selection time, we use a
fixed nominal noise scale 𝜎nom for lookahead evaluation." The confidence-derived
noise is used only once the answer and its confidence both exist, at the
posterior-update step (MAP + Laplace).

## Why it matters

Most active preference learning treats every comparison label as coming
from one fixed-noise channel and scores the next query only by the
*model's* uncertainty over the latent utility (as in [[qeubo]] or plain
[[expected-information-gain]] over $f$). This mechanism adds a second,
per-observation uncertainty signal — the answerer's own report of how sure
they were — and routes it to a different place than the model's own
posterior uncertainty: it reweights how much *this* answer counts, rather
than which *future* question to ask. A practitioner building a preference
elicitor with a self-report channel available (a Likert scale, a slider,
an "I'm not sure" button) now has a concrete place to put it: the
likelihood's noise term, not a discard threshold or a separate weighting
heuristic.

## Limits

- Read from one paper's method section (`zhang-2026`), not independently
  replicated; the mapping $u(\cdot)$ itself is not specified beyond its
  monotonicity, so the note does not know how the confidence-to-noise
  curve was chosen or how sensitive results are to it. Named `unverified`
  here.
- The decoupling from query selection is a limit the paper itself states,
  not a strength: the acquisition step cannot account for the fact that a
  confident answer will constrain the posterior more than an unsure one,
  because confidence is unknown until after the query is chosen. The
  lookahead is computed under a nominal noise level that may not match
  the answer that comes back.
- Validated only in a $N=13$ user study and a matched simulation over a
  synthetic vibrotactile-preference domain (40 pairwise rounds each); the
  claim that this beats a fixed-noise probit likelihood is not isolated
  by an ablation in what was read here.

## Related

[[qeubo]] · [[expected-information-gain]] · [[volume-removal]] · [[calibration]]

[^c1]: zhang-2026
[^c3]: zhang-2026
