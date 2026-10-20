---
description: "A per-user contextual-bandit layer around a frozen LLM agent that learns, from scalar feedback on the chosen action alone, when to seek information versus act, with a proven regret bound."
aliases: ["FABLE", "Factorized Adaptive Bandit Layer for Execution", "factorized residual contextual bandit"]
sources: ["jin-2026"]
---
# FABLE (Factorized Adaptive Bandit Layer for Execution)

> A policy layer placed outside a frozen, possibly black-box LLM agent that
> learns, per user, when to consult memory, when to seek information (ask
> the user) and how to respond — from one scalar feedback signal per round —
> and comes with a regret guarantee against the best allowed action.

## Definition / Mechanism (Jin et al. 2026)

FABLE treats one interaction's execution choice as a joint action
$a=(m,\tau,s)$ over memory mode $m$, information-acquisition mode $\tau$
(including "ask user"), and response behaviour $s$, drawn from a
feasible set $A_t$ that external permission/safety rules restrict before
any exploration happens. It formulates personalizing a frozen agent as
"online learning of a per-user execution policy over a factorized action
space, from scalar feedback observed only for the selected action, subject
to externally specified feasibility constraints."[^c1]

Expected feedback is not learned from scratch: it is decomposed as a fixed,
prespecified default-and-cost score plus a linear residual term
$\phi(c,a)^\top\theta^\star$ that captures the target user's departure from
that default. Only the residual is updated online, via Bayesian
([[thompson-sampling|Thompson-sampling]]-style) posterior sampling over $\theta$, and the feature
map $\phi$ is factorized (main effects for $m,\tau,s$, context interactions,
and pairwise component interactions) so that one observed outcome updates
the shared directions of related joint actions rather than one flat
per-combination arm.[^c2]

Under a linear residual-reward model and a calibrated Gaussian sampling
scale $\nu_t=\sqrt{9d\log(t/\delta)}$, FABLE attains, with probability at
least $1-\delta$, regret $R_n=\tilde O(d^{3/2}\sqrt n)$ against the best
action available in the feasible set at each round (Theorem 1), and the
same order in expectation when $\delta=n^{-2}$.[^c3]

On a four-domain tau2-bench evaluation (240 episodes/policy), the full
FABLE policy is the only comparator that tops all three reported columns:
highest observed personalized reward, highest alignment, and tied-highest
task success. Removing the onboarding prior produced the largest measured
loss (+0.163 alignment, +0.071 personalized reward, full minus
no-onboarding); the paired gain in task success over the host baseline
(+0.017) had a 95% CI crossing zero, so no task-success improvement is
claimed.[^c4]

## Why it matters here

Stall 2 asks which axis of $W$ to query first. FABLE answers a narrower,
concrete version of that question for an LLM agent: whether to ask the
user at all (versus retrieving memory or acting directly) is one component
of a jointly-chosen, per-round action, selected by a learned posterior over
a *user-specific* residual value rather than by a fixed policy or prompt
rule. It is the first method on this stall's map that ties the
ask-vs-act decision to a stated, provable regret bound while keeping the
underlying LLM frozen.

## Transfer

| | |
|---|---|
| **Home field** | Linear contextual bandits and Thompson sampling (Agrawal & Goyal 2013's saturated-action regret argument, adapted) |
| **Here** | Choosing, per interaction and per user, whether an LLM agent's next move includes asking a clarifying question, among a joint choice of memory/information/response actions |
| **What survives** | The regret-bound machinery (feasible-oracle comparator, calibrated posterior-sampling scale) and the trick of learning only a *residual* against a known baseline, letting sparse per-user feedback update shared feature directions across related joint actions |
| **What does not** | The guarantee holds only under a linear residual-reward model, bounded features, and a supplied nonempty feasible set (Assumptions 1–3) checked here for a specific action catalog (18 combinations in tau2-bench); it says nothing about whether the learned information-acquisition decisions track actual information value — there is no EIG or [[entropy]] term — and posteriors are kept independent per user, so nothing here transfers across users |

## Limits

The regret bound is a feasible-oracle guarantee under a linear
residual-reward model with prespecified default/cost scores and bounded
features (Assumptions 1–3); it is not evidence that the learned policy's
ask/act split tracks the true [[value-of-information|value of information]], and it was checked
against a synthetic verbosity-alignment metric plus tau2-bench's native
reward, not against real user judgments of when a clarifying question was
warranted. The task-success gain over the host baseline was not
statistically distinguishable from zero, so the method's practical
selection benefit for stall 2 is demonstrated only on preference-sensitive
metrics, not on end-task success.

## Related

[[thompson-sampling]] · [[information-ratio]] · [[information-directed-sampling]] · [[value-of-information]] · [[bounded-rationality]]

[^c1]: jin-2026 — "We formulate personalization of a frozen agent as online learning of a peruser execution policy from scalar feedback observed only for the executed action."
[^c2]: jin-2026 — "FABLE models expected feedback as E[yt | Ct = c, at = a] = b(c, a)+ϕ(c, a)⊤ θ⋆ −λ cost(c, a),"
[^c3]: jin-2026 — "Then, with probability at least 1 − δ, √ Rn = e O(d3/2 n)."
[^c4]: jin-2026 — "FABLE (full) is the only policy at the top of all three columns in Table 2: it has the highest observed personalized reward and alignment and ties FABLE (frozen) for the highest observed task success."
