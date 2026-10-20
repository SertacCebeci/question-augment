---
description: "**This wiki's inference, not a result.** Every mechanism that elicits truth Three steps; the first two are the sources', the third is this wiki's. **1. The verifier is a peer,"
aliases: ["peer as verifier"]
sources: ["gao-2014", "kong-2019", "lu-2024", "prelec-2004", "shnayder-2016"]
---
# Peer as verifier

> **This wiki's inference, not a result.** Every mechanism that elicits truth
> without a ground truth gives one answer to "who verifies a subjective
> answer?": a second source whose signal depends on the first only through the
> state. That is the independence the wiki finds scarce everywhere else — so
> for the one-answerer case the family supplies a format and a diagnostic, and
> no mechanism.

## The claim

Three steps; the first two are the sources', the third is this wiki's.[^s1][^s2][^s3][^s4][^s5]

**1. The verifier is a peer, and only a peer.** [[mutual-information-paradigm]]
pays $MI(\hat\Psi_i; \hat\Psi_j)$ for a reference agent $j \ne i$ (Kong & Schoenebeck 2019, Theorem 3.3); [[correlated-agreement]] scores agreement with
a second agent on shared tasks minus unshared ones (Shnayder et al. 2016,
Definition 3.1); [[bayesian-truth-serum]] scores against the population's
actual versus predicted frequencies (Prelec 2004); [[generative-peer-prediction]]
scores against a second human report with a model estimating the conditional
(Lu et al. 2024, Definition 4.2). In none is the world, the asker, or a model's
own opinion the standard. With one answerer the payment $MI(\hat\Psi_1;\cdot)$
has nothing to pair with — it is undefined, not small.

**2. What the peer must satisfy.** Signals conditionally independent given the
state (Kong & Schoenebeck Assumption 7.6; Lu et al. §3.1, "i.i.d. conditioned
on the item"; Shnayder et al.'s $\Delta$ over one joint law) plus stochastic
relevance. The wiki already holds three measurements of that condition:
[[coincident-failure]] — independently produced sources fail together on the
ambiguous parts of the question; [[tree-search-methods]] — $N$ samples of one
model are not $N$ sources; [[novice-expert-problem]] — agreement is evidence
only after an independence check the novice cannot perform.

**3. Therefore (this wiki).** The price of verifying an unverifiable answer is
exactly one conditionally independent second source, and every measurement in
the wiki says that source costs more than it looks: between two humans the
shared route is the question's own [[efe-planning-as-variational-inference|ambiguity]]; between two model samples it is
the weights. Theorem 3.3's data-processing step is [[data-processing-inequality]]
read from the answerer's side — and it cuts the other way too. If the asker
manufactures a peer from its own model by conditioning on the first answer, the
[[mutual-information|mutual information]] between the two measures the model's fidelity to the
answer, not to the state; a high score then rewards agreement with the user,
which is [[sycophantic-capitulation]] priced as truth. For the case
Source leaves open — one user, a specification question — the family
therefore yields: (a) the report format survives (an answer plus either a
second report or a prediction of others); (b) the check cannot be run without a
second answerer; (c) a model may occupy the *prior's* seat, as in GPPM, but not
the peer's.

**What the asker can still use: the conditioning.** An MI-type score between
two reports measures shared information, and its two readings — shared route
(high, wrong) and shared state (high, right) — are separable only by a third
source or by conditioning out what both could have said without looking. GSPPM
does the second with a synopsis of the item (Lu et al., Definition 4.3,
Corollary 4.8). This wiki infers, and no source states, that for an asker the
synopsis is the question's own text and context: conditioning the pair-score on
it is the operational check against [[coincident-failure]], whose Transfer row
says the asker cannot otherwise estimate its sources' correlation from the
answers in hand.

**What would refute it.** A mechanism that is strictly truthful with $n = 1$
and no verification. Kong & Schoenebeck's [[emit-only-feedback-obstruction|Proposition 8]].8 gives a permutation
ceiling for every detail-free mechanism and their proof of Theorem 3.3 needs
$j \ne i$, but no cited theorem states the $n = 1$ impossibility outright, and
this note does not claim one. A second refutation: a measured case where a
model-manufactured peer, conditioned on the first answer, scores a wrong
answer *lower* than a right one at a rate the model's own accuracy does not
explain.

## Known as

Not a term of art. "Peer as verifier" is this wiki's name for the composition
of the elicitation-without-verification family's shared structure with the
wiki's own independence findings; the phrase should not be searched for in the
literature. Its parts are [[mutual-information-paradigm]],
[[correlated-agreement]] and [[generative-peer-prediction]].

## Transfer

| | |
|---|---|
| **In its home field** | incentive properties of payment rules over $n \ge 2$ agents drawing signals from one joint law |
| **Here** | read as a statement about what can stand in for verification when an asker has one answerer and no ground truth |
| **What survives** | the identification of the verifier with a conditionally independent second report; the data-processing direction, which makes a model conditioned on the first answer a channel from it rather than a peer |
| **What does not** | the arithmetic — nothing here bounds how far a one-answerer check falls short, only that it is not the family's object; and the incentive reading, since an unpaid answerer's truthfulness is a separate empirical question |

## Limits

- **A conjecture, typed as one.** No source composes [[peer-prediction|peer prediction]] with the
  one-answerer case; Gao et al. (2014) is the closest and measures 3–4 players.
- The reading of the synopsis as "the question's own text and context" is this
  wiki's; Lu et al. define it as a commonly known summary of the *item*, and a
  question is not an item.
- The claim that a model-manufactured peer scores sycophancy relies on the
  model's second answer being a function of the first answer plus weights — the
  Markov chain the DPI note flags as assumed, not verified; a model with tool
  access breaks it.
- Nothing here says whether a single unpaid answerer is truthful.
  [[uninformative-equilibrium]]'s unpaid control was two-thirds truthful with
  3–4 players, and that is the only number the wiki has.
- Step 3's "costs more than it looks" is a direction, not a quantity; the
  three cited measurements are on programs, model samples and testimony, not
  on paired human answers to one question.

## Related

[[mutual-information-paradigm]] · [[correlated-agreement]] · [[generative-peer-prediction]] · [[coincident-failure]] · [[data-processing-inequality]] · [[tacit-knowledge]]

[^s1]: gao-2014
[^s2]: kong-2019
[^s3]: lu-2024
[^s4]: prelec-2004
[^s5]: shnayder-2016
