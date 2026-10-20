---
description: "A score for an answer that will never be resolved: take a second report — Prelec (2004), *Science* 306, 462–466."
aliases: ["BTS"]
sources: ["prelec-2004", "witkowski-2012"]
---
# Bayesian truth serum

> A score for an answer that will never be resolved: take a second report —
> what the answerer thinks *others* will say — and reward the answer that turns
> out **more common than collectively predicted**.

## Definition / Mechanism

Prelec (2004), *Science* 306, 462–466. Each of $n$ respondents supplies two[^s1][^s2]
reports about the same question:

```text
information report  x_i   the respondent's own answer (binary: 0/1)
prediction report   y_i   the frequency of answer 1 it expects in the population
```

The score has two additive parts. Writing $\bar x_{-ij}$ for the (Laplace-
smoothed) arithmetic mean of information reports excluding $i$ and $j$, and
$\bar y_{-ij}, \bar y'_{-ij}$ for the geometric means of the prediction reports
excluding $i$ and $j$, Witkowski & Parkes (2012, eq. 6) state the finite-$n$
version as

```text
u_i =  Σ_{j≠i} [ x_i ln( x̄_-ij / ȳ_-ij ) + (1-x_i) ln( (1-x̄_-ij) / ȳ'_-ij ) ]   information score
     + Σ_{j≠i} [ x̄_-ij ln( y_i / x̄_-ij ) + (1-x̄_-ij) ln( (1-y_i)/(1-x̄_-ij) ) ]  prediction score
```

The information score is a log-ratio of **actual to predicted** endorsement:
it pays for an answer that is *surprisingly common*, not for an answer that is
common. The prediction score is a log scoring rule on the respondent's forecast
of the others' answers. Prelec's headline claim is that the combination
"removes all bias in favor of consensus: truthful answers maximize expected
score even for respondents who believe that their answer represents a minority
view" (2004, abstract).

**Theorem 1 (Prelec 2004, as stated by Witkowski & Parkes 2012).** BTS is
strictly Bayes–Nash incentive compatible for $n \to \infty$ and all admissible
priors — truthful means reporting one's true signal *and* predicting the true
posterior frequency of high signals.

**Theorem 2 (Witkowski & Parkes 2012).** BTS is *not* Bayes–Nash incentive
compatible or interim individually rational for $n = 3$. Their Example 1 — two
states, $\Pr(T{=}2)=0.7$, $\Pr(S{=}h \mid T{=}2)=0.8$, $\Pr(S{=}h \mid
T{=}1)=0.1$, giving posteriors $p_{\{h\}} = 0.764$, $p_{\{l\}} = 0.339$ —
gives a truthful agent an expected score of $-0.450$ against $+0.298$ for a
misreport. How large $n$ must be "depends on the prior and is hard to
characterize" (Witkowski & Parkes 2012, p. 1494).

**Proposition 3 (Witkowski & Parkes 2012).** The BTS score is unboundedly
negative for prediction reports $y_i \in \{0,1\}$: the mechanism is not
numerically robust and can pay less than nothing.

## Known as

| Name | Field | Relation |
|---|---|---|
| BTS | mechanism design, experimental economics | exact — the standard abbreviation of the mechanism |
| information score | mechanism design | **not this concept** — one of the two additive components of the score, meaningless without the prediction score |
| surprisingly common criterion | mechanism design | **not this concept** — the criterion the information score implements; [[surprisingly-popular-algorithm]] applies the same criterion with no payment at all and is measured by accuracy rather than by incentive compatibility |
| peer prediction | mechanism design | **not this concept** — both a different mechanism (Miller, Resnick & Zeckhauser 2005) and the family name; see [[peer-prediction]] |
| robust Bayesian truth serum (RBTS) | mechanism design | **not this concept** — Witkowski & Parkes's own replacement, a different formula with a different theorem ($n \ge 3$, ex post individually rational, binary signals only) |

## Why it matters

1. **The only score on Commitment that never needs the answer
   resolved.** [[calibration-training]], [[outcome-feedback]] and the held-out
   threshold of [[abstention]] all require outcomes to arrive. BTS uses the
   *other answerers' reports* as the standard, so a question that can never be
   settled is still scorable.
2. **It adds a report rather than rescaling one.** The answerer must supply a
   second-order statement — how often it expects each answer among others — and
   the commitment is scored against that, not against a self-reported
   confidence. [[sycophantic-capitulation]] shows post-hoc self-reported
   confidence is not admissible; this is a different channel.
3. **It rewards a defensible minority answer.** Because the payoff is the ratio
   of actual to predicted endorsement, an answerer who knows something the
   crowd does not is paid *more* for saying it, which is the opposite of what a
   consensus score does.
4. **The guarantee does not reach a single answerer.** Theorem 1 is a limit
   result and Theorem 2 kills $n = 3$ outright, with truth paying $-0.450$
   against a misreport's $+0.298$ in a concrete prior. An asker with one
   answerer inherits the *report format* and none of the incentive property.

## Transfer

| | |
|---|---|
| **Home field** | $n$ risk-neutral expected-payment-maximising Bayesian agents, a common prior over a state (admissible: at least two distinct, fully mixed, positive-probability states) shared by all agents but not needed by the mechanism, conditionally independent signals, the same question put to all, and a scorer that can pay |
| **Here** | an asker scoring how far an answerer committed, on a question whose answer will never come back |
| **What survives** | the two-report format (answer + predicted distribution of others' answers) and the surprisingly-common criterion; the demonstration that truth-telling can be an equilibrium with *no ground truth anywhere in the mechanism*; and the fact that consensus-rewarding scores are the thing being corrected |
| **What does not** | the incentive theorem — it is an $n \to \infty$ result and provably fails at $n = 3$; the payments, since an answerer with no payoff function is not this model's agent; the conditional independence, since repeated samples from one model are not $n$ agents ([[tree-search-methods]]); and the boundedness one would need to use the score as a reward signal (Proposition 3) |

## Limits

- The claim that an unresolvable commitment can be *scored* rests on there
  being a population of answerers drawing signals from one shared prior. Where
  the wiki's usual setting holds — one asker, one answerer, one question — no
  theorem cited here applies, and what remains is a report format with an
  unproven property.
- Truth-telling is an **equilibrium, not a dominant strategy**. Nothing in
  either theorem says it is the equilibrium that gets played; see
  [[uninformative-equilibrium]] for the one experiment on the question.
- The original *Science* paper was not obtained for this note. The formulas,
  the two theorems and Proposition 3 above are cited to Witkowski & Parkes
  (2012), who present the binary case of Prelec's finite-$n$ mechanism; the
  "surprisingly common" criterion and the minority-view claim are cited to
  Prelec's own abstract. The equation and theorem numbering of the 2004 paper
  is therefore not stated here.
- Prelec's own experimental validation of BTS is not read or cited here.

## Related

[[peer-prediction]] · [[surprisingly-popular-algorithm]] · [[uninformative-equilibrium]] · [[partition-equilibrium]] · [[abstention]] · [[outcome-feedback]]

[^s1]: prelec-2004
[^s2]: witkowski-2012
