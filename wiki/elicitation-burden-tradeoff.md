---
description: "A formal user-LLM model in which the optimal number of preference-clarifying questions trades linear query burden against expected mismatch, and is non-monotonic in inequality aversion."
aliases: ["optimal querying policy"]
sources: ["park-2026-when"]
---
# Elicitation-burden tradeoff

> How many clarifying questions should a generative model ask before it
> answers? Not "as many as possible" and not "none" — a number set by how
> noisy the population's preferences are and how much the objective cares
> about the user least likely to be served by a guess.

## Definition / Mechanism

Park, Donahue & Raghavan (2026) model a user's preferences
as an $n$-bit vector drawn from a two-cluster Bernoulli mixture (cluster
probability $\alpha$, per-bit flip probability $p$). Before generating, the
LLM may query $k$ of the $n$ bits directly; the rest it must infer. The
user's utility is linear in both costs: $U(k, B) = n - k - B$, where $B$ is
the number of guessed bits that come out wrong. "The user's utility depends
on (1) how many questions they had to answer, and (2) how close the
generated output is to their true preferences."[^c1]

Under plain [[expected-utility]] maximization the optimal $k$ is not monotone in
anything obvious: "there exists a noise rate $p$ when it is optimal to ask a
single query and a noise rate $p$ where it is optimal to ask no queries" for
equal-sized clusters ($\alpha=1/2$, Lemma 2), and "there exist values of $n$
where it maximizes expected utility to ask no questions for all values of
$p$" once one cluster is a large majority (Lemma 3). Asking is worth its
cost only when the revealed bits are informative enough about which cluster
the user belongs to; near $p=1/2$ a query is pure cost.[^c2]

The paper then replaces the utilitarian objective with a CES social-welfare
function indexed by an inequality-aversion parameter $\gamma$ ($\gamma=0$
utilitarian, $\gamma=1$ Nash, $\gamma\to\infty$ maximin) and re-derives the
optimal $k$. "The optimal number of queries is non-monotonic as a function
of $\gamma$ for $p>0$" (Lemma 6): raising $\gamma$ from 0 first *increases*
the optimal query count — because weighting the worst-off user raises the
[[value-of-information|value of information]] about which cluster they are in — before the marginal
cost of further queries outweighs that benefit and the optimal count falls
back down.[^c3]

An empirical check on the sushi preference dataset (5000 users, 10 binary
features, decision-tree query ordering, explicit per-query cost $c=0.3$)
reproduces the qualitative shape: "it is not until $k=3$ queries that the
preference information learned is sufficiently valuable to increase
welfare... welfare becomes optimal at $k=4$" under the utilitarian objective,
while "when $\gamma=5$, we see that the optimal $k$ increases to 9. As
$\gamma$ further increases to 10, we see that it becomes optimal for welfare
to directly elicit a user's entire set of preferences."[^c4]

## Why it matters

This gives the "which axis first, and how many" question on stall 2 a
mechanism instead of a slogan: the right amount of clarification is set
jointly by (a) how correlated/noisy the preference population is, (b) how
skewed the population's clusters are, and (c) how much the objective is
willing to sacrifice majority-serving efficiency to represent an atypical
user — not a fixed "ask 3 questions" policy.

## Transfer

| | |
|---|---|
| **In its home field** | Welfare economics: a one-parameter CES family of social welfare functions, indexed by an inequality-aversion parameter, used to compare policies by how much weight they place on the worst-off individual (Atkinson-style) |
| **Here** | The same family reweights an LLM's expected per-user utility to decide how many clarifying questions to ask before generating content for a population of users |
| **What survives** | The qualitative direction — more inequality-aversion raises the value of information about atypical/minority users — and the three named special cases ($\gamma=0,1,\infty$) as interpretable anchors |
| **What does not** | The result is proved only inside this paper's linear-utility, two-cluster Bernoulli-mixture model with a per-query cost equal (or fixed) across users; it assumes the LLM knows the population's preference distribution exactly and that per-user utilities are cardinally comparable — neither holds for a deployed system |

## Limits

- The claim above rests on a stylized preference generator (a two-cluster
  Bernoulli mixture) and a linear cost/benefit ratio of 1 between a query
  and a correctly-guessed bit; the authors note "the Bernoulli mixture model
  fits some data well but may not generalize to other domains," and the
  empirical section uses one dataset (sushi rankings, $n=10$) at one cost
  value ($c=0.3$).
- The model assumes the LLM has full knowledge of the population's
  preference distribution ($p$, $\alpha$) — an assumption the paper itself
  flags as often violated.
- All users are modelled as facing the same per-query cost; the paper notes
  this varies with the individual and the question's specificity in
  practice.

## Related

[[value-of-information]] · [[question-budgets]] · [[expected-utility]] · [[bounded-rationality]]

[^c1]: park-2026-when — "The user’s utility depends on (1) how many questions they had to answer, and (2) how close the generated output is to their true preferences."
[^c2]: park-2026-when — "there exists a noise rate p when it is optimal to ask a single query and a noise rate p where it is optimal to ask no queries"
[^c3]: park-2026-when — "The optimal number of queries is non-monotonic as a function of γ for p > 0."
[^c4]: park-2026-when
