---
description: "Pay an answerer the mutual information between its report and a *peer's* Kong & Schoenebeck (2019), *ACM TEAC* 7(1), art. 2; read in the arXiv v2 (1605.01021, 2018),"
aliases: ["MIP", "mutual information paradigm"]
sources: ["dasgupta-2013", "kong-2019", "miller-2005", "prelec-2004"]
---
# Mutual information paradigm

> Pay an answerer the mutual information between its report and a *peer's*
> report. Any lie, hedge or shortcut is a post-processing of the answerer's
> signal, and the data-processing inequality says post-processing cannot raise
> mutual information — so truth is the best-paying strategy whatever the
> others do, and no ground truth appears anywhere.

## Definition / Mechanism

Kong & Schoenebeck (2019), *ACM TEAC* 7(1), art. 2; read in the arXiv v2[^s1][^s2][^s3][^s4]
(1605.01021, 2018), which the authors state is the journal version. Setting
$(n, \Sigma)$: $n$ agents, each receiving a private signal $\Psi_i \in \Sigma$
and holding a prior over the joint law; the mechanism sees only the reports
$\hat\Psi_i$. A strategy is a transition matrix from signals to reports;
truth-telling $\mathbf T$ is the identity; a *permutation strategy* relabels
signals consistently.

**Definition 3.1 (information-monotone).** A functional $MI(X;Y)$ is
information-monotone if it is symmetric, non-negative (zero when $X \perp Y$),
and satisfies the data-processing inequality: for any transition matrix $M$
with $Y \perp M(X) \mid X$, $MI(M(X);Y) \le MI(X;Y)$. *Strictly* so if the
inequality is strict for every non-permutation $M$.

**The paradigm MIP($MI$).** Each agent $i$ reports $\hat\Psi_i$; a reference
agent $j \ne i$ is drawn uniformly; $i$ is paid $MI(\hat\Psi_i; \hat\Psi_j)$.

**Theorem 3.3.** When $MI$ is (strictly) information-monotone with respect to
every agent's prior, MIP($MI$) is (strictly) *dominantly truthful* — truth
maximises $i$'s expected payment whatever the others play — and (strictly)
*truth-monotone* — a truthful agent switching to a non-truthful strategy lowers
*every* agent's expected payment. The proof is three lines: a strategy $s_i$ is
a transition matrix, so $MI(s_i(\Psi_i); \hat\Psi_j) \le MI(\Psi_i; \hat\Psi_j)$.
In the authors' words, "applying any strategy to the information is
essentially data processing and thus erodes information."

**Theorem 3.8.** $f$-mutual information, $MI^f(X;Y) = D_f(U_{X,Y}, V_{X,Y})$ —
the $f$-divergence between the joint and the product of marginals — is
information-monotone for strictly convex $f$, and strictly so on fine-grained
joints. KL gives Shannon's $I(X;Y)$; $|x-1|$ gives total variation.
**Corollary 3.10**: MIP($MI^f$) is (strictly) dominantly truthful.

**It is not yet a mechanism.** The authors call the paradigm "wishful thinking":
the payment needs the joint law over signals, which the mechanism does not
have. A mechanism is an unbiased estimator of that payment, and the family's
members are estimators under different budgets:

| Budget | Estimator | Result |
|---|---|---|
| infinitely many a priori similar questions, random order, no prior | the pair's report table (Theorem 6.3) | detail-free, minimal, (strictly) dominantly truthful; Dasgupta & Ghosh (2013) is the total-variation member for binary signals (Claim 6.7), and there truth is informative-truthful and strongly focal rather than dominant (Theorem 6.6) |
| one question, a known common prior | Miller et al.'s (2005) score minus the prior's score (Theorem 7.5) | pays Bregman mutual information $BMI(\Psi_i;\Psi_j)$ at truth |
| one question, a second-order report, $n \to \infty$ | Prelec's (2004) information score (Lemma 7.9) | pays $I(W; \Psi_i \mid \Psi_j)$ at truth; Prelec's focality results follow from the DPI (Theorem 7.8 ii–iii) |

The bridge between the log score and Shannon information is **Theorem 5.2**:
the expected log-score gain of the posterior over the prior equals
$I(X;Y \mid Z)$.

**Ceiling ([[emit-only-feedback-obstruction|Proposition 8]].8, Corollary 8.9).** A mechanism that does not know
the prior cannot pay truth strictly more than a permutation strategy, for any
definition of truth. "Strictly better than every *non-permutation* strategy"
is the most any detail-free mechanism can offer.

## Known as

| Name | Field | Relation |
|---|---|---|
| MIP | mechanism design | exact — the authors' abbreviation |
| mutual information paradigm | mechanism design | exact |
| $f$-mutual information mechanism, Bregman mutual information mechanism | mechanism design | **not this concept** — two mechanisms (Theorems 6.3, 6.4) that estimate the paradigm's payment in the multi-question setting |
| information elicitation without verification | mechanism design | **not this concept** — the problem; the family of mechanisms is [[peer-prediction]] |
| peer prediction (Miller, Resnick & Zeckhauser 2005) | mechanism design | **not this concept** — recovered as the Bregman member in the single-question, known-prior setting (Theorem 7.5) |
| mutual information | information theory | **not this concept** — [[mutual-information]] is the KL member of the class the paradigm quantifies over |

## Why it matters

1. **It names what verifies an unverifiable answer.** Not the world, not the
   asker's judgement, and not a model's own opinion: a *second report*, whose
   mutual information with the first is positive only through what both
   sources know. That is the answer to stall 4 for the case Source
   leaves open — a subjective answer with no check.
2. **It is the wiki's DPI turned on the answerer.**
   [[data-processing-inequality]] says the asker cannot manufacture information
   by processing; Theorem 3.3 says the answerer cannot manufacture payment by
   processing its signal. Same inequality, opposite party — and it holds for
   any information-monotone functional, with no payment needed to state it.
3. **It retires the search for a sharper score.** Proposition 8.8: no
   detail-free mechanism separates truth from a consistent relabelling. The
   residual [[efe-planning-as-variational-inference|ambiguity]] is a bound, not a defect of the rule in use.
4. **It explains the family's spread.** [[bayesian-truth-serum]],
   [[correlated-agreement]] and the original method are estimators of one
   quantity under three budgets — many questions, a known prior, or a
   second-order report. Choosing a member is choosing what to pay for the
   estimate.

## Transfer

| | |
|---|---|
| **Home field** | $n \ge 2$ expected-payment-maximising agents with priors over a joint signal law, signals related only through the item, a mechanism that can pay, and — for any actual mechanism — infinitely many a priori similar questions, or a known common prior, or a second-order report |
| **Here** | an asker deciding what could stand as the check on a subjective, unverifiable answer, and whether its own model can be that check |
| **What survives** | the identification of the verifier with a second report; the DPI direction — every answerer strategy is a channel and loses information; and the permutation ceiling |
| **What does not** | the payment property, which needs an agent maximising expected payment; the estimator, since the asker's usual setting has one question and one answerer and neither route gives an unbiased estimate there; and the reference agent's independence — $N$ samples of one model are not a peer ([[tree-search-methods]]) |

## Limits

- The claim that truth is dominant rests on the *paradigm's* payment, which
  needs the joint law. Every implementable mechanism is an estimator; Theorem
  6.3 is stated for infinitely many questions and the paper gives no
  finite-question rate ([[correlated-agreement]] gives one, for a different
  mechanism).
- Dominant truthfulness is proved in the zero-effort model. With costly effort
  (their §4) the property becomes "dominantly informative" and needs convexity
  of the functional, which Bregman mutual information lacks (their remark after
  Corollary 5.7).
- The reference agent's signal must depend on the reporter's only through the
  item (Assumption 7.6 for BTS; the joint-law framing throughout). Where two
  sources share a route to the answer, mutual information pays for the shared
  route ([[coincident-failure]]).
- Nothing here says the truthful equilibrium is *played*;
  [[uninformative-equilibrium]] is the one measurement, on a different
  mechanism.
- Theorem numbers are those of arXiv v2; the TEAC copy was not checked for
  renumbering. `dasgupta-2013`, `miller-2005` and `prelec-2004` are cited as
  restated in this paper's §6.2 and §7, not from their own text.

## Related

[[data-processing-inequality]] · [[mutual-information]] · [[peer-prediction]] · [[bayesian-truth-serum]] · [[correlated-agreement]] · [[peer-as-verifier]]

[^s1]: dasgupta-2013
[^s2]: kong-2019
[^s3]: miller-2005
[^s4]: prelec-2004
