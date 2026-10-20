---
description: "A four-parameter choice model splitting bandit action into value-guided choice, a UCB-like and a Thompson-like exploration signature, and a noise floor."
aliases: ["UCB-like/Thompson-like decomposition", "choice-level exploration model"]
sources: ["xiong-2026-thinking"]
---
# Exploration-signature decomposition

> A choice-level model that turns "did the agent explore?" into four fitted
> numbers instead of one accuracy score, so a selection rule can be scored
> for evidence use and information-seeking separately rather than assumed
> from aggregate performance.

## Definition / Mechanism

For a two-armed choice with empirical mean rewards $\bar r_a$ and warm-up
counts $n_a$, define the standard-error proxy $s_a = 10/\sqrt{n_a}$, value
difference $V=\bar r_L-\bar r_R$, relative uncertainty $RU=s_L-s_R$, and
total uncertainty $TU=\sqrt{s_L^2+s_R^2}$. The probability of choosing the
left arm is

$$P(a_i=L)=\Phi\!\left(\frac{V_i+\gamma RU_i}{\sqrt{\lambda^2+\eta^2 TU_i^2}}\right).$$

"A positive γ shifts choice toward the less-observed arm, producing a
UCB-like signature. The parameter η makes choice variability increase with
total uncertainty, producing a Thompson-like signature. These components
constitute UCB-like and Thompson-like exploration, respectively, whereas λ
sets an uncertainty-independent noise floor (Gershman 2018)."[^c1]

Fit to the action-logit difference between the two options, the four terms
— $V$ (value-guided action), $\gamma$ (UCB-like), $\eta$ (Thompson-like),
$\lambda$ (noise floor) — separate genuine information-seeking from choice
that merely looks exploratory because it is noisy. The names are
deliberately only descriptive: "these behavioral analogies do not imply
that a model internally implements either algorithm" (Xiong, Yan, Ji-An et al. 2026).[^c2]

## Why it matters

Stall 2's other rows score a *candidate question* by expected information
or [[expected-utility|expected utility]] before it is asked. This model instead scores an
*already-made choice* after the fact, decomposing it into how much of the
choice tracked known value versus how much tracked the two textbook
exploration signatures — so a claim like "the agent explored more" can be
checked against a fitted number instead of read off overall accuracy or
reward.

## Transfer

| | |
|---|---|
| **Home field** | Computational cognitive modeling of exploration–exploitation in human and animal bandit tasks (Gershman 2018) |
| **Here** | Scoring an agent's action selection under uncertainty — exploiting known value, pulling toward the less-known option (UCB-like), or growing more variable as uncertainty grows (Thompson-like) — from logged choices rather than assumed from aggregate accuracy |
| **What survives** | The four-term split itself, fit directly to action-logit differences: a value term, a relative-uncertainty term, a total-uncertainty term, and a separate noise floor, giving exploration a fitted magnitude instead of a label |
| **What does not** | The fitted γ, η are named "behavioral analogies" only — the source explicitly disclaims that a high γ or η means the model runs UCB or [[thompson-sampling|Thompson sampling]] as an algorithm; the model was fit to two-armed, matched-horizon, warm-up-history trials, not to open-ended selection among more than two axes |

## Limits

The decomposition needs a countable warm-up history per option ($n_a$,
$\bar r_a$) and a forced two-way choice; reading its γ/η as a general
measure of "does this agent seek information when selecting a question" for
open-ended, many-axis selection is this wiki's extrapolation beyond the
two-armed setting the model was fit to, not a claim the source makes.

## Related

[[thompson-sampling]] · [[expected-information-gain]] · [[value-of-information]]

[^c1]: xiong-2026-thinking — "A positive γ shifts choice toward the less-observed arm, producing a UCB-like signature. The parameter η makes choice variability increase with total uncertainty, producing a Thompson-like signature. These components constitute UCB-like and Thompson-like exploration, respectively, whereas λ sets an uncertainty-independent noise floor (Gershman 2018)."
[^c2]: xiong-2026-thinking — "These behavioral analogies do not imply that a model internally implements either algorithm."
