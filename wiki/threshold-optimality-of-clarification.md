---
description: "Clarification strictly dominates answering directly whenever its weighted interaction cost is less than the weighted drop in expected future epistemic risk it buys."
aliases: ["Proposition 1 Pustejovsky Krishnaswamy 2026", "clarification dominance condition"]
sources: ["arxiv-2604-25136"]
---
# Threshold optimality of clarification

> Clarification is not virtuous by default — it wins only when the risk it
> removes is worth more than the delay it costs, at a rate set by two fixed
> weights.

## Definition / Mechanism

Pustejovsky & Krishnaswamy (2026) state and prove a
dominance condition (their Proposition 1) inside a risk-sensitive control
objective that trades off task reward, an intervention cost $C_{fric}$
weighted by $\lambda$, and expected epistemic risk $R_{risk}$ weighted by
$\eta$. At a decision point with belief state $b_t$ and history $h_t$, let
$a_c$ be a clarifying action and $a_a$ a direct answer. Given that
clarification strictly lowers expected future risk —

> "Risk reduction: Clarification yields strictly
> lower expected future epistemic risk:
> E[Rrisk (bt+1 ) | ac ] < E[Rrisk (bt+1 ) | aa ]."[^c2]

— and that its cost is finite, the theorem gives the exact condition under
which clarifying beats answering:

> "Then clarification strictly dominates direct answering whenever:
> λ Cfric (ac ) <
> η (E[Rrisk (bt+1 ) | aa ] − E[Rrisk (bt+1 ) | ac ])"[^c1]

The proof follows by decomposing the risk-sensitive objective's Q-value
into task reward, weighted risk, and weighted cost, and applying Bellman
optimality once the risk-reduction gain $\eta\Delta_{risk}$ exceeds the cost
penalty $\lambda C_{fric}(a_c)$.

The two weights alone fix a threshold on how much risk reduction justifies
the delay:

> "The ratio η/λ defines an implicit clarification threshold: it specifies how much
> epistemic risk reduction is required to justify the
> interaction cost of delaying task completion."[^c3]

When $\eta \gg \lambda$, even a small expected risk reduction warrants
asking; when $\lambda \gg \eta$, only severe uncertainty or hazard does.

## Why it matters

This gives a normative target, not an algorithm: it says what an
ask-or-answer policy *should* converge to if it is optimizing a
risk-sensitive objective, independent of how that objective's risk term is
estimated. The [[friction-functional]] is offered elsewhere in the same
work as exactly such an estimator — a tractable surrogate for the
$R_{risk}$ this theorem otherwise leaves as a latent, inaccessible quantity.

## Limits

The theorem assumes the agent has (or approximates) $E[R_{risk}(b_{t+1})]$
under both actions — quantities defined over an unobserved belief state
$b_t$, not measured directly; the paper is explicit that "the agent does not
need direct access to the latent belief state $b_t$ or the true risk
functional $R_{risk}$," but that concession also means the threshold itself
is never evaluated exactly, only approximated by a learned proxy. The proof
is a sketch (a few sentences invoking Bellman optimality), not a full
derivation, and the weights $\lambda,\eta$ are free parameters with no
stated procedure for setting them.

## Related

- [[friction-functional]] — the tractable proxy this theorem's latent risk
  term is meant to be estimated by.
- [[clarification-channel-theorem]] — a different, independently-derived
  threshold-dominance result for when asking beats a no-query rule, over a
  binary-channel model rather than a general belief-state risk.
- [[frictive-intervention]] — clarification is one of the six action
  classes this theorem's dominance condition selects among.
- [[risk-conditioned-trust-region]] — a training method built to approach
  this threshold without evaluating it directly.
- [[abstention]] — the same style of cost-versus-risk threshold, applied to
  withholding an answer rather than delaying one.

[^c1]: arxiv-2604-25136 — "Then clarification strictly dominates direct answering whenever: λ Cfric (ac ) < η (E[Rrisk (bt+1 ) | aa ] − E[Rrisk (bt+1 ) | ac ])"
[^c2]: arxiv-2604-25136 — "Risk reduction: Clarification yields strictly lower expected future epistemic risk: E[Rrisk (bt+1 ) | ac ] < E[Rrisk (bt+1 ) | aa ]."
[^c3]: arxiv-2604-25136 — "The ratio η/λ defines an implicit clarification threshold: it specifies how much epistemic risk reduction is required to justify the interaction cost of delaying task completion."
