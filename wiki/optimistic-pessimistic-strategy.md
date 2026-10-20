---
description: "Most of the best strategy's regret reduction, at about one-hundredth the Boutilier et al. (2006, Defn 4,"
aliases: ["OP strategy", "optimistic-pessimistic strategy"]
sources: ["boutilier-2006"]
---
# Optimistic-pessimistic (OP) query strategy

> Most of the best strategy's regret reduction, at about one-hundredth the
> per-query cost, by never computing minimax regret at all.

## Definition / Mechanism

Boutilier et al. (2006, Defn 4, §5.4) define an **optimistic state**[^s1]
$\mathbf{x}^o \in \arg\max_{\mathbf{x}\in\mathrm{Feas}(X)}\max_{u\in\mathbf{U}}u(\mathbf{x})$
and a **pessimistic state**
$\mathbf{x}^p \in \arg\max_{\mathbf{x}\in\mathrm{Feas}(X)}\min_{u\in\mathbf{U}}u(\mathbf{x})$
— each obtainable by solving one ordinary, precise constraint-optimization
problem (fixing every utility parameter at its upper or lower bound
respectively), with no minimax-regret computation at all
(contrast `minimax-regret` (draft dropped), [[current-solution-strategy]]). The OP
strategy asks a bound query at the midpoint of whichever utility parameter,
among those appearing in $\mathbf{x}^o$ or $\mathbf{x}^p$, currently has the
largest gap.

## Why it matters

On the car-rental, real-estate and large synthetic problems, OP reduced
average minimax regret at a rate close to [[current-solution-strategy]] —
on the real-estate problem it "performs almost identically" (§5.5) — while
costing about 0.1 seconds per query against CS's 14–83 seconds, since it
never solves the minimax program except optionally to test for termination.
This is the paper's answer to selection under a tight compute budget: two
ordinary optimizations recover most of the regret-reduction quality that the
full adversarial computation buys, at roughly two orders of magnitude less
work per query. Together with CS, the concluding section names OP as one of
"the most promising of these strategies" (§6).

## Limits

- OP has no proof of any regret-reduction guarantee (unlike
  `halve-largest-gap` (draft dropped)) and no argument ruling out the kind of stall the
  paper's second-best (SB) strategy exhibits.
- Reported only on the four problem families tested (car rental, real
  estate, small and large synthetic GAI problems, up to 45 trials each) with
  simulated users answering exactly and consistently to one drawn utility
  function — never against an inconsistent or adversarial real respondent.
- Restricted to bound queries; the paper does not define or test an OP
  variant for comparison queries.
- Nothing in the paper bounds how far $\mathbf{x}^o$ and $\mathbf{x}^p$ can
  drift from the true adversarial pair $(\mathbf{x}^*,\mathbf{x}^w)$ that
  [[current-solution-strategy]] targets directly — the proxy's quality is an
  empirical finding on these four families, not a proved property.
- Verified against the freely mirrored author copy of the paper, not the
  typeset ScienceDirect version.

## Transfer

| | |
|---|---|
| **In its home field** | a GAI-factored COP where $\mathbf{x}^o$ and $\mathbf{x}^p$ are each obtainable by one ordinary IP/MIP solve |
| **Here** | any selection step where the two extreme "most optimistic" / "most pessimistic" outcomes are cheap to compute while the true adversarial pair is not |
| **What survives** | attending to the parameters that separate the best-case and worst-case realizations is a usable, far cheaper proxy for attending to the parameters that separate the current recommendation from its strongest rival |
| **What does not** | the cost saving is specific to problems where $\mathrm{Feas}(X)$ is small or structured enough that two ordinary optimizations are cheap; there is no general argument for why the proxy tracks the adversarial pair rather than diverging from it |

## Related

`minimax-regret` (draft dropped) · [[current-solution-strategy]] · `halve-largest-gap` (draft dropped) · [[value-of-information]]

[^s1]: boutilier-2006
