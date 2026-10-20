---
description: "A support state need only be compressed down to the partition that preserves the optimal action; the approximate version bounds expected policy regret and reduces to a rate-distortion problem."
aliases: ["support sufficiency", "action-sufficient compression", "decision-sufficiency quotient", "rate-regret function"]
sources: ["walsh-2026"]
---
# Action-sufficient compression

> How much of a support state must survive compression before a system may
> act, verify, abstain, or defer — stated first as an exact partition, then
> as a bounded-regret relaxation.

## Definition / Mechanism

Walsh (2026) fixes a full support state $H$, a finite action
set $\mathcal{A}$, and a consequence geometry $Z$ giving the payoff of each
action under $H$. A compression $g:\mathcal{H}\to\mathcal{S}$ is *exactly
action-sufficient* for $Z$ if the policy computed from $g(H)$ always matches
the full-information optimal policy $\pi^*(H,Z)$. The paper's first result:
for fixed $Z$, the coarsest exactly action-sufficient compression is the
quotient of support space by policy equivalence — two support states may be
merged exactly when they require the same optimal action. "For fixed
consequence geometry Z, the coarsest exactly action-sufficient compression is
the quotient map $q_Z:\mathcal H\to\mathcal H/\sim_Z$ … which maps each
support state H to its policy-equivalence class $[H]_Z$."[^c1]

This makes precise when a scalar summary (e.g. confidence alone) is not
enough: "If a confidence cell contains support states that require different
optimal actions… confidence-only compression is not exactly action-sufficient
for Z" — because equal confidence can hide a sign change in the utility gap
between two actions along an axis (e.g. provenance) that confidence does not
track.[^c2]

Bounded systems relax exactness to $\varepsilon$-action-[[sufficient-statistic|sufficiency]]: expected
regret $\mathbb{E}_H[R_g(H,Z)]\le\varepsilon$. In the finite single-cycle
case this becomes a rate-regret problem: "define the rate-regret function
$R_Z(\varepsilon)=\min_{p(\hat a\mid H)} I(H;\hat A)$ subject to
$\mathbb{E}[d_Z(H,\hat A)]\le\varepsilon$", where the regret distortion
$d_Z(H,a)$ is the utility gap between the optimal action and $a$.[^c3]

The Lagrange-optimal solution to that problem takes the standard
rate-distortion Gibbs form: "$p_\beta(\hat a\mid H) = p_\beta(\hat a)
\exp[-\beta d_Z(H,\hat a)] / \sum_{a'} p_\beta(a')\exp[-\beta d_Z(H,a')]$",
with $\beta\ge 0$ the Lagrange multiplier trading regret against retained
information.[^c4]

## Transfer

| | |
|---|---|
| Home field | Information theory — Shannon rate-distortion (source, reproduction alphabet, single-letter distortion, Gibbs-form optimum) |
| Here | Decision theory — the "source" is a support/belief state, the "reproduction alphabet" is a finite action set, and distortion is policy regret rather than reconstruction error |
| Survives | The Markov reduction $H\to S\to\hat A$, the data-processing bound $I(H;\hat A)\le I(H;S)$, and the Lagrangian/Gibbs-form solution shape |
| Does not | Reconstruction semantics: the criterion never asks how close $\hat A$ is to $H$, only whether the chosen action matches the optimal one — so a compression can discard everything about $H$ except the bit that moves the policy, unlike lossy source coding, which cares about $H$ itself |

## Limits

The claim rests on a fixed, known consequence geometry $Z$ and a
well-defined optimal policy $\pi^*$ per support state; a system whose payoff
structure is itself uncertain has no fixed partition to quotient by. `walsh-2026`
is a single-author preprint (status: queued, unverified [?]) that presents
this as an interpretive specialization of known rate-distortion machinery,
not a new generic decision-theoretic theorem — the paper says so itself.

## Related

[[rate-distortion-theory]] · [[value-of-information]] · [[sufficient-statistic]] · [[data-processing-inequality]]

[^c1]: walsh-2026 — "For fixed consequence geometry 𝑍, the coarsest exactly action-sufficient compression is the quotient map 𝑞𝑍 : ℋ → ℋ/∼𝑍 , (7) which maps each support state 𝐻 to its policy-equivalence class [𝐻]𝑍 ."
[^c2]: walsh-2026 — "If the total regret induced by confidence cells exceeds 𝜀, then scalar confidence is not 𝜀-action-sufficient for 𝑍."
[^c3]: walsh-2026 — "define the rate-regret function 𝑅𝑍 (ε) = min 𝐼 (𝐻; 𝐴̂) 𝑝( 𝑎 ̂ ∣∣ 𝐻 ) subject to 𝔼[𝑑𝑍 (𝐻, 𝐴̂)] ≤ 𝜀. (19)"
[^c4]: walsh-2026
