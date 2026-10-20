---
description: "Query the parameter that could still flip the recommendation, not the Boutilier et al. (2006,"
aliases: ["CS strategy", "current solution strategy"]
sources: ["boutilier-2006"]
---
# Current solution (CS) query strategy

> Query the parameter that could still flip the recommendation, not the
> parameter with the most raw uncertainty.

## Definition / Mechanism

Boutilier et al. (2006, §5.3) select the next elicitation query by first[^s1]
computing the current minimax-optimal decision $\mathbf{x}^*$ and its
**adversarial witness** $\mathbf{x}^w$ — the feasible decision that
maximises regret against $\mathbf{x}^*$ under the current feasible utility
set (see `minimax-regret` (draft dropped)). The CS strategy then asks a bound query at the
midpoint of whichever utility parameter, among
$\{\mathbf{x}^*[k]:k\le K\}\cup\{\mathbf{x}^w[k]:k\le K\}$, currently has the
largest gap between its upper and lower bound. The intuition: narrowing
exactly the parameters that determine the *current* comparison between the
recommendation and its strongest rival is more targeted than narrowing
uncertainty everywhere. A time-bounded variant, CS-5, computes $\mathbf{x}^*$
and $\mathbf{x}^w$ approximately by stopping the anytime constraint-
generation procedure of §4.2 after five seconds.

## Why it matters

Across four problem families — small synthetic problems (45 instances, 10
GAI factors), a car-rental configuration problem (61.9 million
configurations, 435 utility parameters), a real-estate problem (47.8 million
configurations, 160 parameters) and larger synthetic problems (25–30
variables) — CS reduced average minimax regret nearly as fast as the
exhaustive, per-query myopically-optimal baseline (MY, computationally
infeasible beyond the smallest instances) and consistently beat
`halve-largest-gap` (draft dropped), the most-uncertain-state variant, and the
second-best strategy (Boutilier et al. 2006, Figs. 9–12). On the real-estate
problem CS drove average minimax regret from 40% of the optimal value to
under 5% in about 120 of 160 possible queries. This is a decision-focused
answer to stall 2's "which axis first?": it scores a candidate query by
whether it could still change *which decision wins*, not by how much
uncertainty it removes overall ([[expected-information-gain]]) or how
unpredictable its answer is ([[volume-removal]]).

CS is not free: the reported cost is 83 seconds per query on the real-estate
problem and 14 seconds on the synthetic problems, because the full minimax
computation is re-run after every answer. The CS-5 variant reaches "queries
virtually as effective" at 5 seconds per query (§5.5) — the anytime property
of the underlying constraint-generation algorithm (§4.2.2) means
approximating the minimax computation costs little query quality.

## Transfer

| | |
|---|---|
| **In its home field** | bound queries over factored (GAI) utility parameters, with $\mathbf{x}^*$ and $\mathbf{x}^w$ computed exactly or anytime-approximately by an MIP solver after every answer |
| **Here** | any asker selecting the next question when the goal is a decision, not full resolution of the state |
| **What survives** | attend to the specific comparison an adversary would exploit — the current best guess versus its strongest rival — rather than to whichever axis carries the most raw uncertainty |
| **What does not** | the need to compute $\mathbf{x}^*$ and $\mathbf{x}^w$ at every step, which needs the whole minimax-regret machinery (an enumerable or GAI-structured decision space) to exist and be cheap enough to re-run after each answer; an open-ended [[possible-worlds]] space with no such structure has no candidate $\mathbf{x}^w$ to compute |

## Limits

- No proof of guaranteed regret reduction: "if the answer lowers the upper
  bound on some $u_{\mathbf{x}^*[k]}$ or raises the lower bound on some
  $u_{\mathbf{x}^w[k]}$, [regret] is not guaranteed to be reduced (though it
  may)" (§5.3) — contrast `halve-largest-gap` (draft dropped), which has one.
- Evaluated only with bound queries, on configuration-style domains (car
  rental, real estate, synthetic GAI problems with at most 30 factors) with
  simulated users answering exactly and consistently to a fixed drawn
  utility function.
- The authors explicitly flag the comparison-query version of CS as
  untested: "we do not experiment with specific comparison query strategies
  here... we expect the CS strategy to perform quite well" (§5.6) — an
  expectation, not a result.
- Verified against the freely mirrored author copy of the paper, not the
  typeset ScienceDirect version.

## Related

`minimax-regret` (draft dropped) · `halve-largest-gap` (draft dropped) · [[optimistic-pessimistic-strategy]] · [[expected-information-gain]] · [[value-of-information]] · [[volume-removal]]

[^s1]: boutilier-2006
