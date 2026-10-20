---
description: "Score two answerers by whether their answers to a *shared* question agree in Shnayder, Agarwal, Frongillo & Parkes (2016), EC'16; read in the extended version, arXiv 1603.03151."
aliases: ["CA mechanism", "correlated agreement mechanism"]
sources: ["dasgupta-2013", "kong-2019", "shnayder-2016"]
---
# Correlated agreement

> Score two answerers by whether their answers to a *shared* question agree in
> the direction their signals are correlated, minus the same score on questions
> they did not share. Answering the same thing regardless of what one saw then
> earns exactly zero; no strategy beats truth; and it needs two answerers and
> three questions, not a population. It verifies against a peer, not against
> the state: agreement driven by a signal the two share is paid as truth.

## Definition / Mechanism

Shnayder, Agarwal, Frongillo & Parkes (2016), EC'16; read in the extended[^s1][^s2][^s3]
version, arXiv 1603.03151. Two agents with signals $S_1, S_2$ on $n$ values;
$m \ge 3$ a priori identical tasks, at least one shared; *stochastic
relevance* (their eq. 1): distinct signals induce distinct posteriors on the
other agent's signal. The **Delta matrix** (Definition 2.1)
$\Delta_{ij} = P(S_1{=}i, S_2{=}j) - P(S_1{=}i)P(S_2{=}j)$ encodes the
correlation structure; every row and column sums to zero.

**Multi-task mechanism with score matrix $S$ (Definition 3.1).** Bonus tasks
$M_b$ are shared; penalty tasks $M_1, M_2$ are not. For each bonus task $k$,
draw $\ell \in M_1$, $\ell' \in M_2$ and pay both agents
$S(r_1^k, r_2^k) - S(r_1^\ell, r_2^{\ell'})$. Agents must not know which tasks
are bonus. Expected payment on a bonus task is $E(F,G) = \sum_{ij} \Delta_{ij}
S(F_i, G_j)$ (their eq. 16), so an *uninformed* strategy — the same report for
every signal — earns exactly zero whatever $S$ is, because rows of $\Delta$ sum
to zero.

Two properties (Definitions 2.7, 2.8): **strongly truthful** — $E(\mathbb I,
\mathbb I) \ge E(F,G)$ for all $F,G$, with equality only when both play the same
permutation; **informed-truthful** — the same, with equality allowed for any
pair of informed strategies.

**The CA mechanism (Definition 5.1): $S = \mathrm{Sign}(\Delta)$** — score 1
where the report pair is positively correlated, 0 otherwise. The designer needs
only the sign structure.

- **Theorem 5.2.** CA is informed-truthful and proper for all worlds.
- **Theorem 4.4.** MSDG — $S$ = identity, the $n$-signal extension of Dasgupta & Ghosh (2013) — is strongly truthful iff the world is *categorical* (seeing
  a signal makes every other signal less likely: $\mathrm{Sign}(\Delta) =
  \mathbb I$). Binary positively-correlated worlds are categorical, which gives
  Dasgupta & Ghosh's result with a shorter proof.
- **Theorem 5.9.** CA is strongly truthful when $\mathrm{Sign}(\Delta)$ has no
  two identical rows or columns (*clustered signals*, Definition 5.4) and no
  *paired permutations* (Definition 5.7) — and is maximal: no mechanism using
  only the sign structure is strongly truthful on more worlds.
- **Theorem 5.10.** For some symmetric three-signal worlds no multi-task
  mechanism is strongly truthful, even with full knowledge of $\Delta$.
- **Theorem 5.13 (CA-DF).** With the sign structure estimated from the reports
  themselves (tasks split in halves, each half's score matrix fitted on the
  other), $m = O(n^3 \log(1/\delta)/\epsilon^2)$ tasks give
  $(\epsilon,\delta)$-informed truthfulness.

**Measured.** 325,523 peer assessments on 104 questions from 17 MOOC courses:
the categorical condition holds for about a third of the three-signal models
and for none larger (their Fig. 1); grading signals are ordinal — a 2/5
correlates positively with a 3/5; CA is strongly truthful up to paired
permutations "in roughly half of the worlds" (their Fig. 3).

## Known as

| Name | Field | Relation |
|---|---|---|
| CA mechanism | mechanism design | exact |
| correlated agreement | mechanism design | exact |
| multi-task peer prediction | mechanism design | **not this concept** — the class (Definition 3.1) parametrised by $S$; CA is the member $S = \mathrm{Sign}(\Delta)$ |
| Dasgupta–Ghosh mechanism, MSDG | mechanism design | **not this concept** — the member $S = \mathbb I$, strongly truthful only in categorical worlds (Theorem 4.4) |
| output agreement | human computation | **not this concept** — pays for matching with no penalty task; the subtraction is what CA adds |
| informed truthfulness, strong truthfulness | mechanism design | properties of a mechanism, not names for this one |
| $f$-mutual information mechanism | mechanism design | close — Kong & Schoenebeck (2019) state that with the sign structure known, a linear transform of CA is an unbiased estimator of total-variation mutual information (Shnayder et al., footnote 4; Kong & Schoenebeck, Theorem 6.6); see [[mutual-information-paradigm]] |

## Why it matters

1. **Who verifies: a second answerer over a batch, corrected for chance.** The
   penalty task is what turns "they agree" into evidence — agreement on a
   shared question minus agreement on unshared ones is the sample analogue of
   $\Delta$. Raw agreement, which [[novice-expert-problem]] warns against, is
   the special case with the subtraction left out.
2. **Two agents, three tasks.** The population guarantees of
   [[bayesian-truth-serum]] ($n \to \infty$) never reach an asker with two
   sources; this one does, provided the asker can put several a priori similar
   questions to both and hide which are shared.
3. **Signal-independent agreement is priced at zero; signal-driven agreement
   is paid whatever drives the signal.** The zero is for the strategy that
   ignores the signal, whatever the score matrix. It is *not* a guard against
   [[coincident-failure]], which is shared failure *with* a shared signal —
   two sources reading the same ambiguous question the same wrong way. $\Delta$
   is the signals' own joint law (Definition 2.1); if the signals are
   correlated through a shared misreading rather than through the item, that
   correlation is in $\Delta$ and CA pays agreement on it exactly as it pays
   truth. The two concepts are orthogonal: CA removes the uninformed
   answerer, coincident failure is about what the informed answerers share.
4. **Strong truthfulness has a measured domain.** On the one real dataset, the
   stronger property fails for about half the worlds and Theorem 5.10 says no
   mechanism can supply it for some. What an asker can buy in general is
   *informed* truthfulness — no strategy beats truth and shirking loses — not
   uniqueness.
5. **The price is exchangeability and concealment.** The reduction of per-task
   strategies to one strategy (their Lemma 2.5) needs tasks in independent
   random order and the bonus set hidden; drop either and the answerer can
   play each question separately.

## Transfer

| | |
|---|---|
| **Home field** | two payment-maximising agents; $m \ge 3$ a priori identical, exchangeable tasks in independent random order; a finite signal alphabet; a common-knowledge signal law with stochastic relevance; a designer who knows $\mathrm{Sign}(\Delta)$ or estimates it from many tasks |
| **Here** | an asker with two sources and a batch of similar questions, scoring their answers with no ground truth |
| **What survives** | the penalty-task subtraction as the correction for chance agreement; the zero payment of signal-independent answering; the two-agent, three-task feasibility; and the finding that "categorical" — one answer excludes the rest — is the exception among graded answers |
| **What does not** | the payment theorems, for an answerer with no payoff; the a priori identical tasks, since a session's questions are not exchangeable and arrive in a meaningful order, so Lemma 2.5's reduction fails; the estimate of $\Delta$, which costs $O(n^3/\epsilon^2)$ questions; the intended-signal assumption (their §5.5) — real answers have attributes to coordinate on that the model excludes; and any protection against a shared wrong signal, which the mechanism pays as truth |

## Limits

- The claim that blind agreement pays zero rests on bonus and penalty tasks
  being draws from the *same* joint law: exchangeable tasks in random order.
  Without that, the subtraction over- or under-corrects.
- The penalty subtraction corrects for agreement under the signals' own joint
  law; it cannot separate correlation through the item from correlation
  through a shared route to the answer ([[coincident-failure]]). Items 1 and 3
  rest on reading the peer's correlation with the reporter as correlation
  through the item. CA verifies against a peer, not against the state.
- Strong truthfulness is bounded above by Theorem 5.10; what the note claims
  for all worlds is informed truthfulness only.
- The MOOC estimate of $\Delta$ treats student reports as truthful (their
  footnote 12); the "half the worlds" figure is conditional on that.
- Theorem 5.13's rate is for CA-DF; with $\mathrm{Sign}(\Delta)$ known, the
  theorems need only $m \ge 3$ but say nothing about the variance of the
  payment.
- Dasgupta & Ghosh (2013) is cited for the binary mechanism and its strong
  truthfulness as restated by Shnayder et al. (Theorem 4.4); its own theorem
  numbering is not used. Kong & Schoenebeck (2019) is cited only for the
  total-variation reading of CA in ## Known as, not for any of the theorems
  above.

## Related

[[peer-prediction]] · [[mutual-information-paradigm]] · [[bayesian-truth-serum]] · [[coincident-failure]] · [[novice-expert-problem]] · [[uninformative-equilibrium]]

[^s1]: dasgupta-2013
[^s2]: kong-2019
[^s3]: shnayder-2016
