---
description: "Answer only if a hard scientific-admissibility gate passes and the calibrated risk of answering is below the cost of abstaining; failing the gate forces abstention regardless of confidence."
aliases: ["constrained plug-in answerability rule", "answerability certificate", "scientific admissibility gate"]
sources: ["zhang-2026-bayesian"]
---
# Gated answerability rule

> Low risk is not entitlement to answer: a categorical admissibility check
> can force abstention even when the confidence threshold alone would clear
> it.

## Definition / Mechanism

Zhang, Song, Wang, Bhatt & Huang (2026) state and
prove a constrained plug-in Bayes rule (their Lemma 1) for choosing between
answering and abstaining. Let $r(H)$ be the conditional expected loss of
answering, $\tau_{abs}$ the fixed loss of abstention, and $G\in\{0,1\}$ a
hard scientific-admissibility gate. When the gate passes ($G=1$) the rule
reduces to Chow's classical threshold: "conditional risk of abstaining is
the constant τabs . The Bayes action minimizes conditional risk" — answer
iff $r(H)\le\tau_{abs}$.[^c1]

When the gate fails ($G=0$), abstention is forced independent of how low
$r(H)$ reads: answering is either removed from the feasible action set or
penalized above every attainable risk, so "abstention is the unique
feasible or risk-minimizing action." Substituting a monotone calibrated
surrogate $F(t,S)$ for the unobserved $r(H,S)$ yields the deployable rule
$\iota^\star = \mathbb{1}\{F(t,S)\le\tau_{id}\}\cdot G(t,S)$: both the
threshold and the gate must pass.[^c2]

## Why it matters

This extends Chow's reject-option threshold ([[abstention]]) with a second,
categorical veto: a state the risk threshold alone would clear must still
abstain if a named admissibility condition fails (stale evidence,
insufficient coverage, unresolved source [[efe-planning-as-variational-inference|ambiguity]] in the source paper's
domain). It gives "confident but not entitled to answer" a distinct formal
status from "not confident enough" — two different reasons to withhold that
a single risk threshold cannot separate.

## Transfer

| | |
|---|---|
| In its home field | A Bayes decision rule extending Chow's reject option with a task-specific feasibility gate, for a wastewater-surveillance answerer |
| Here | Any answerer choosing between committing to an answer and saying "I don't know" |
| What survives | The conjunction of a calibrated-risk threshold and a hard, named admissibility condition as the answer decision; the proof that $G=0$ forces abstention independent of the risk surrogate's value |
| What does not | The specific gate content (evidence coverage, recency, source-policy compatibility) is domain-built for influenza surveillance and needs redefinition elsewhere |

## Limits

- Proved only for the two-action case (answer/abstain) with a fixed
  $\tau_{abs}$ and an assumed monotone [[calibration]] map
  $r(H)\approx\phi(F(t,S))$; it does not cover graded commitment (partial
  answers).
- The gate $G$ is asserted as a scientific/domain judgement, not learned or
  probabilistically justified within the theorem — which conditions belong
  in $G$ is outside its scope.
- Read from the arXiv preprint's appendix proof (Zhang et al. 2026); not
  yet peer-reviewed — [?].

## Related

[[abstention]] · [[bellman-evidence-acquisition-policy]] · [[value-of-information]]

[^c1]: zhang-2026-bayesian — "conditional risk of abstaining is the constant τabs . The Bayes action minimizes conditional risk"
[^c2]: zhang-2026-bayesian — "abstention is the unique feasible or risk-minimizing action"
