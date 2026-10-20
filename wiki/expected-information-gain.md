---
description: "An estimate, before asking, of how much a question will teach you. EIG is mutual-information **indexed by a design $q$ and maximised over $q$**: the quantity is the same functional,"
aliases: ["EIG", "Lindley information", "expected KL gain", "information gain criterion"]
sources: ["farquhar-2024", "lewis-1979", "lindley-1956", "rainforth-2023", "arxiv-2512-21129", "arxiv-2512-04453"]
---
# Expected information gain (EIG)

> An estimate, before asking, of how much a question will teach you.

## Definition (Lindley, 1956)

EIG is [[mutual-information]] **indexed by a design $q$ and maximised over[^s1][^s2][^s3][^s4]
$q$**: the quantity is the same functional, but the object here is a
*selection criterion over a candidate set of questions*, not the general
dependence measure between two variables. That indexing is the whole content
of Lindley (1956) — $\arg\max_q$, not $I$ itself.

$$\mathrm{EIG}(q) = H(\theta) - \mathbb{E}_{y\sim p(y\mid q)}\big[H(\theta\mid y)\big] = I(\theta; Y_q)$$

Equivalently, the expected [[kl-divergence]] from prior to posterior:

$$\mathrm{EIG}(q) = \mathbb{E}_y\big[D_{KL}(p(\theta\mid y)\,\|\,p(\theta))\big]$$

## Key subtlety: computed without knowing the answer

EIG averages over **all possible answers**. You need not know the answer, only
its distribution. This is what makes question **selection** possible before
receiving any answer.

## Why $\geq 0$

Since $I \geq 0$, EIG can never be negative: **no question is harmful on
average — given a fixed $W$ and a truthful, presupposition-free question.**
The averaging is over answers only; if the act of asking itself moves the
belief state, the inequality is about a different object than the one that
actually updates. Even inside the assumption, a single answer can be harmful
(a misleading answer can worsen belief) — just not in expectation.

This answers the question of whether asking unnecessary questions is harmful:
harmless in information terms, **harmful in cost terms**. See
[[value-of-information]].

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Bayesian experimental design | expected information gain (Lindley 1956) | exact |
| Information theory | mutual information $I(\theta; Y_q)$ | close — [[mutual-information]] is the same functional without the design index and the $\arg\max_q$ |
| Bayesian statistics | expected KL from prior to posterior | exact |
| Active learning | expected model change / uncertainty sampling | close — proxies for the same quantity |

## Where it applies

The theory places EIG precisely:

```text
EIG is not an EXPLORATION engine.
EIG is a SELECTION engine.
```

EIG only selects questions **within the existing [[possible-worlds|hypothesis space]]**. For an
axis not represented in the space, EIG cannot be computed — because $\theta$
does not contain that variable. This is the formal statement of **an
unmodelled axis is invisible**.

## Computability

EIG is intractable in real problems — it involves nested expectations. Much of
modern [[bayesian-experimental-design|Bayesian experimental design]] research is about estimating it
(Rainforth et al. 2023). The practical route in the LLM setting: sample
candidate answers and measure with [[semantic-entropy]] (Farquhar et al. 2024).

## Transfer

| | |
|---|---|
| **Home field** | Bayesian experimental design: a parameter $\theta$ with an explicit prior, a design $q$, and repeated i.i.d. draws from a known likelihood $p(y\mid q,\theta)$ |
| **Here** | one natural-language answer from a user, tool or model; $\theta$ is an implicit belief with no written prior, and the answer space is unbounded free text |
| **What survives** | the score-before-answering logic — a question can be ranked from the *distribution* of its answers alone — and the sign result $I \geq 0$ under the assumptions in ## Limits |
| **What does not** | the exactness of the estimate. [[semantic-entropy]] over sampled answers (Farquhar et al. 2024) measures the *model's* answer dispersion, not $I(\theta;Y_q)$; it is a biased surrogate, so the induced *ranking* of candidate questions carries no guarantee, and nested-MC EIG estimators are themselves biased (Rainforth et al. 2023) |

## In a robot's goal posterior (Ghose et al.)

Ghose et al. use this criterion for a robot that must choose a question in collaborative cooking. Candidate questions come from task categories. The likelihood of each answer given each goal is read off attractor fields, meaning how strongly each answer is associated with each goal.[^s6] The value of a question is the expected drop in entropy of the goal belief, ΔH = H − E[H | ans]. "a good question partitions the plausible goals into groups depending on the answer."[^s7] My inference: with Shannon entropy this is the mutual information I(g; ans), so the paper's criterion is this note's EIG with the goal distribution as θ.

The paper also sets the answer distribution to be flat: "For simplicity, we assume that each possible human answer is equally likely."[^s8] So the expectation is a plain average over answers, not over the answer distribution the robot actually expects. The goal set is also not fixed. In the open case, "the goal set is unknown to the robot and potentially of infinite size."[^s9] EIG can only rank questions within the goals the robot has modelled, so the open-case results show the ranking working on goals the language model proposed, not that no goal was missed.

## Limits

- $I \geq 0$ assumes the act of asking does not itself alter $W$ or
  $p(\theta)$. Presupposition accommodation violates this
  ([[presupposition-accommodation]]; Lewis 1979) — a question with a false
  presupposition can score high and still delete the actual world, because the
  wording updates the context before any answer exists.
- Defined only over a modelled $\theta$. Silent on unmodelled axes — the
  note's central point.
- Intractable in general (a nested expectation); estimators are biased and
  high-variance (Rainforth et al. 2023).
- Measures information, not value. $\mathrm{EIG} > 0$ with
  $\mathrm{VoI} = 0$ is common.
- Assumes $p(y \mid q)$ is known or well estimated ([[calibration]]). The robot-posterior use above sets it flat instead.[^s8] My inference: a question whose answers are in fact lopsided is scored on a distribution the robot does not expect, so the ranking can be off even when the entropy arithmetic is right.
- Only over modelled goals. The open-case robot in the same paper generates its goal set with a language model, so the criterion is blind to any goal that model never proposes.[^s9]

## Related

[[mutual-information]] · [[bayesian-experimental-design]] · [[value-of-information]] · [[optimal-decision-tree]] · [[presupposition-accommodation]] · [[semantic-entropy]]
- [[generalized-binary-search]]
- [[structure-information-gain]] — the same functional with the index taken to be the generative model rather than a parameter[^s5]
- [[refractory-interruption-cost]] — the when-to-ask rule that pairs with this what-to-ask criterion in the same robot

[^s1]: farquhar-2024
[^s2]: lewis-1979
[^s3]: lindley-1956
[^s4]: rainforth-2023
[^s5]: arxiv-2512-21129 — "we introduce a third sort of information gain that pertains to the structure of"
[^s6]: arxiv-2512-04453 — "encode how strongly each answer is associated with the goal"
[^s7]: arxiv-2512-04453 — "a good question partitions the plausible goals into groups depending on the answer"
[^s8]: arxiv-2512-04453 — "For simplicity, we assume that each possible human answer is equally likely"
[^s9]: arxiv-2512-04453 — "the goal set is unknown to the robot and potentially of infinite size"
