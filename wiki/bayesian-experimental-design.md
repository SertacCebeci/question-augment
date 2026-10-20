---
description: "By what criterion to choose the next experiment (question). The academic Choose a design $\\xi$, observe outcome $y$, update belief about $\\theta$. Goal: pick the $\\xi$ maximising expected utility."
aliases: ["BED"]
sources: ["lindley-1956", "chaloner-1995", "ryan-2016", "rainforth-2023", "kiefer-1959"]
---
# Bayesian experimental design

> By what criterion to choose the next experiment (question). The academic
> form of sequential asking.

## Framework

Choose a design $\xi$, observe outcome $y$, update belief about $\theta$. Goal:[^s1][^s2][^s3][^s4][^s5]
pick the $\xi$ maximising [[expected-utility|expected utility]].

$$\xi^* = \arg\max_\xi \mathbb{E}_{y}\big[U(\xi, y)\big]$$

Lindley's (1956) contribution: **take information gain as the utility** →
[[expected-information-gain]]. Chaloner & Verdinelli (1995) put the whole
literature in this one decision-theoretic form: a criterion *is* a choice of
$U$, and the named criteria are special cases of it.

## Sequential BED

Experiments are chosen one at a time, each conditioned on prior outcomes.
Exactly what sequential questioning does.

The difficulty: a truly optimal sequential design requires evaluating all
future branchings (dynamic programming, exponential cost). In practice the
next design alone is optimised — the **myopic/greedy** approach — and both
modern surveys of the field (Ryan et al. 2016; Rainforth et al. 2023) treat
this one-step-ahead form as the standard adaptive procedure.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Bayesian statistics | BED | exact |
| Classical design of experiments | optimal experimental design (OED) | close |

Classical OED (Kiefer 1959) is **not** an alias. It fills the same role —
rank designs before running them — but is a different object: no prior over
$\theta$, and criteria defined on the Fisher information matrix of a
parametric model rather than on a posterior. The Bayes criteria reduce to it
only in limiting cases.

## Alternative criteria

| Criterion | What it optimises | Established by |
|---|---|---|
| D-optimality | Volume of parameter uncertainty (determinant of the information matrix) | Kiefer 1959 |
| A-optimality | Average variance (trace) | Kiefer 1959 |
| EIG / Bayes-D | Information gain | Lindley 1956 |
| Decision-theoretic | Quality of the final decision | Chaloner & Verdinelli 1995 (unifying form); Ryan et al. 2016 (survey) |

The last is the right one when questions serve a build: the goal is not to
learn $\theta$ but to **decide correctly**. See [[value-of-information]].

## Transfer

| | |
|---|---|
| **In its home field** | A parameter $\theta$ with an explicit prior, a design space of admissible $\xi$, a written likelihood $p(y \mid \xi, \theta)$, and a utility whose expectation is computable or estimable. |
| **Here** | An implicit belief state, a question in free natural language, an unbounded answer space, no written likelihood over answers. |
| **What survives** | The move of ranking candidate questions by *expected* value **before** hearing the answer; and the criterion taxonomy — asking which $U$ you are maximising (parameter precision vs. information vs. decision quality) is a live question even with no model. |
| **What does not** | The optimum itself. Without a likelihood there is no $\arg\max$, only an ordering by judgement. The D/A-optimality machinery does not transfer at all — it needs a parametric model with a [[fisher-information|Fisher information]]. No optimality guarantee comes across. |

## Consequence — conjecture (this wiki)

**Conjecture.** For a questioner with no model, asking one question at a time
without lookahead is a defensible default rather than a concession.

Two supports, neither of them a proof. (i) The field itself does this: the
standard adaptive BED procedure is myopic (Ryan et al. 2016; Rainforth et al.
2023). (ii) A greedy selection rule has a $(\ln n + 1)$ guarantee in
[[optimal-decision-tree]].

The second support does not carry. That bound holds for a **finite, given**
test set, noiseless outcomes and uniform test costs (see that note's Limits).
Sequential BED in general has none of these: continuous design spaces, noisy
$y$, and payoff that may arrive only after several experiments. So the
$O(\log n)$ guarantee is not inherited here; it is an analogy, and the
conjecture rests on practice plus that analogy, not on a theorem.

## Limits

- Expected utility needs a generative model of outcomes. In practice EIG is
  estimated, and the estimators are the hard part (Ryan et al. 2016;
  Rainforth et al. 2023).
- Myopic greedy can be badly non-optimal when payoff is delayed across several
  experiments — this is the known failure mode of the conjecture above.
- The borrowed $O(\log n)$ guarantee holds only under a finite discrete test
  set, noiseless observations and uniform costs. General sequential BED meets
  none of the three, so the note's own greedy claim is an inference, not a
  bound.
- Says nothing about where designs (questions) come from; it only ranks them.
- Source status: `lindley-1956`, `ryan-2016` and `rainforth-2023` entered the
  wiki with `status: url` and were verified only by prior; DOIs are now
  recorded for all three plus `chaloner-1995` and `kiefer-1959`. The claim
  that myopic design is the *standard* adaptive procedure is attributed to
  the two surveys without a section number — cite the papers, not a page.

## Related

[[expected-information-gain]] · [[value-of-information]] · [[blackwell-informativeness]] · [[adaptive-submodularity]] · [[optimal-decision-tree]]

[^s1]: lindley-1956
[^s2]: chaloner-1995
[^s3]: ryan-2016
[^s4]: rainforth-2023
[^s5]: kiefer-1959
