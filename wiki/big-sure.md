---
description: "A black-box LLM uncertainty score from the normalized squared spectral energy of a bipartite entailment graph between low-temperature anchor and high-temperature probe responses."
aliases: ["SURE score", "BiG-SURE", "cross-temperature semantic uncertainty"]
sources: ["bhattacharya-2026"]
---
# BiG-SURE

> A black-box [[calibration|reliability]] score for one already-returned LLM answer: does it
> survive being probed at a higher temperature, or does it drift?

## Problem

A returned answer needs a reliability score before it is trusted as a
constraint (stall 5) or committed to as the answerer's output (stall 10),
but black-box deployments expose no logits and no internal state — only
the ability to sample more text at a chosen temperature.

## Definition / Mechanism

Bhattacharya, Phadke and Ganapathy sample $M$ low-temperature **anchor**
responses $A=\{a_1,\dots,a_M\}$ (stable, near-greedy) and $N$
high-temperature **probe** responses $H=\{h_1,\dots,h_N\}$, the probes
drawn from the original prompt and from meaning-preserving paraphrases of
it. "Low-temperature responses are used as stable anchors, while
high-temperature responses act as probes that reveal semantic drift."[^c1]

An NLI entailment model scores every anchor-probe pair,
$W_{ij}=\mathrm{sem\text{-}sim}(a_i,h_j)\in[0,1]$, forming a bipartite
similarity graph. The score is its normalized squared spectral energy:
"We define normalized confidence and compute the Semantic Uncertainty and
Reliability Estimate (SURE) score as, $E_{norm}(W;\theta)=E_{SURE}(W;\theta)/MN$,
$U_{norm}(W;\theta)=1-E_{norm}(W;\theta)$", where
$E_{SURE}=\sum_i\sigma_i^2=\sum_{i,j}W_{ij}^2$ is the squared Frobenius
norm of $W$ — the method "defines confidence through the normalized
squared spectral energy of this matrix, with uncertainty given by its
complement."[^c2]

$U_{norm}\in[0,1]$; it is 0 iff all sampled responses are semantically
identical and 1 iff every probe is semantically disjoint from every
anchor.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| LLM uncertainty estimation | SURE score | exact — the normalized spectral-energy quantity itself |
| LLM uncertainty estimation | BiG-SURE | close — the paper's name for the whole framework (the anchor/probe sampling protocol plus the SURE score); the score is the load-bearing object |

Not this concept: [[semantic-entropy]] (Kuhn 2023; Farquhar 2024) clusters
responses by entailment and takes entropy over cluster proportions at one
fixed temperature; BiG-SURE takes no clusters and no entropy, and
compares two temperature regimes against each other rather than scoring
dispersion within one sample set — a different computation, cited by this
source as a baseline it improves on.

## Why it matters

This is a second black-box construction for the same target the wiki
already names at stalls 5 and 10 — whether a returned answer is fit to
stand as a constraint, or fit to be committed to rather than hedged — built
without semantic clustering. The paper reports it beats the
semantic-entropy family and graph-based baselines on [[abstention]] AUROC:
"On TRIVIA-QA, SURE obtains an average AUROC of 0.753 ± 0.017, improving
over the strongest baseline average, Deg (0.722 ± 0.007)... On SVAMP,
SURE obtains 0.877 ± 0.022, outperforming the strongest baseline average,
SNNE (0.846 ± 0.018)."[^c3]

The authors claim novelty for the cross-temperature design itself: "To
the best of our knowledge, SURE is the first attempt to leverage
cross-temperature sampling dynamics in LLM responses for uncertainty
quantification."[^c4]

## Transfer

| | |
|---|---|
| **Home field** | Spectral graph theory / signal processing: energy of a bipartite similarity matrix (its squared Frobenius norm, equivalently the sum of squared singular values) as an agreement score between two node sets |
| **Here** | scoring one LLM answer's reliability from the agreement between a stable low-temperature sample and a diverse high-temperature sample of the same (paraphrased) prompt |
| **What survives** | the spectral-energy-as-agreement computation and its boundedness in $[0,1]$; the anchor/probe asymmetry (one set fixed as reference, the other as test) is a reusable pattern for any "does this answer hold up under perturbation" check |
| **What does not** | the paper validates only on factual/short-answer QA (text, multilingual, multimodal) with a ground-truth match label for AUROC; it gives no guarantee for open-ended or design questions where no such label exists, and needs an NLI entailment backend whose own errors propagate into $W$ |

## Limits

- My claim that this bears on stalls 5 and 10 rests on treating
  "abstention AUROC against a correctness label" as a proxy for "is this
  answer fit to commit to" — the paper never poses the question in those
  terms; it is a QA-abstention benchmark, not a study of question asking.
- Requires $M+N$ generations per input plus $O(MN)$ entailment calls, and
  an entailment model as a fixed external dependency (DeBERTa-large NLI,
  or its multilingual variant); errors in that model are not characterized
  here.
- Evaluated only where a fixed ground-truth answer exists to define
  correctness; no result on underspecified or design-type inputs.

## Related

[[semantic-entropy]] · [[entropy]] · [[calibration]]

[^c1]: bhattacharya-2026 — "Low-temperature responses are used as stable anchors, while high-temperature responses act as probes that reveal semantic drift."
[^c2]: bhattacharya-2026
[^c3]: bhattacharya-2026
[^c4]: bhattacharya-2026
