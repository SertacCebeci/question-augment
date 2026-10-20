---
description: "Measuring [[entropy]] over **meaning** rather than tokens in an LLM. Where the Token-level entropy is misleading."
aliases: ["semantic uncertainty", "meaning-cluster entropy"]
sources: ["farquhar-2024", "kossen-2024", "kuhn-2023", "doi-10-48550-arxiv-2609-26035", "arxiv-2512-04359", "arxiv-2512-05156", "arxiv-2512-04351", "arxiv-2512-03107", "arxiv-2511-16275"]
---
# Semantic entropy

> Measuring [[entropy]] over **meaning** rather than tokens in an LLM. Where the
> theory becomes practice — and where the practice stops being validated.

## Problem

Token-level entropy is misleading. A model may say the same thing ten[^s1][^s2][^s3]
different ways — token entropy is high but the model is **certain**.
Conversely it may lock onto a single phrasing and be wrong. Kuhn, Gal and
Farquhar (ICLR 2023) named this *semantic equivalence*: probability mass split
across paraphrases is not uncertainty about the world.

## Definition / Mechanism

Introduced as **semantic uncertainty** by Kuhn et al. (2023); extended and
evaluated at scale by Farquhar, Kossen, Kuhn and Gal (*Nature* 630, 625–630,
2024).

1. Sample $N$ answers to the **same fixed question**
2. Cluster answers by **meaning**, via bidirectional entailment (two answers
   share a cluster iff each entails the other under an NLI model)
3. Compute entropy over cluster probabilities

$$H_{\text{sem}} = -\sum_c p(c)\log p(c), \qquad c = \text{meaning cluster}$$

Farquhar et al. add a **discrete** variant that takes $p(c)$ from cluster
proportions alone, so the measure runs on models that expose no token
probabilities. Their target event is the **confabulation**: a generation that
is wrong *and arbitrary* — one that varies across resamples of an identical
input. Systematic errors a model reproduces consistently are explicitly out of
scope, and score low. Reported result: mean AUROC 0.790 over 30 task–model
combinations (TriviaQA, SQuAD, BioASQ, NQ-Open, SVAMP, FactualBio) against
0.691 for naive entropy and 0.698 for P(True).

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| LLM uncertainty estimation | semantic uncertainty (Kuhn et al. 2023) | exact — the originating name for this measure |
| LLM uncertainty estimation | semantic entropy (Farquhar et al. 2024) | exact — same construct, plus the discrete variant and the confabulation framing |
| Information theory | meaning-cluster entropy | exact — descriptive restatement of $H$ over the entailment partition |

Not this concept: a **semantic entropy probe** (Kossen et al. 2024) is a
linear classifier on hidden states trained to predict $H_{\text{sem}}$ from a
single generation. It is measured differently (probe AUROC against an SE
label) and is a separate object.

## Why it matters

The measure separates two things token entropy conflates: *dispersion of
form* and *dispersion of meaning*. That is what a reader of an answer needs at
stall 5 — a returned answer that is one of many mutually non-entailing answers
the same source would have given is not yet a constraint.

**Beyond this, and marked as such: the following is this wiki's inference,
untested.** No study cited here evaluates either use.

- *Selection (stall 2).* If an axis question's answers cluster into many
  meanings, the axis is open; if into one, it is settled. This is at best a
  **biased surrogate** for [[expected-information-gain]]: $H_{\text{sem}}$ is
  the entropy of the model's answer distribution, not $I(\theta; Y_q)$, so the
  ranking of axes it induces carries no guarantee — see the Transfer row of
  [[expected-information-gain]].
- *Consistency (stall 6).* $H_{\text{sem}}$ **alone does not** separate a
  genuinely underspecified design from sampling noise: two stable, mutually
  contradictory readings give $\approx 1$ bit, and $N$ unrelated one-off
  answers give up to $\log N$ bits — both high, and the ordering runs the
  wrong way for a magnitude threshold. The candidate discriminator is the
  *structure* of the partition, not its entropy: few clusters that reappear
  under independent resampling = the design admits several readings; many
  singleton clusters that do not reappear = arbitrary generation, which is the
  event Farquhar et al. call confabulation. Whether cluster reappearance is
  stable enough to threshold on is untested here.

## Transfer

| | |
|---|---|
| **Home field** | LLM confabulation detection: short factual QA with a ground-truth answer, $N$ samples of one fixed question, bidirectional-entailment clustering by an NLI model, AUROC against a correctness label |
| **Here** | free-text answers about an underspecified design; clusters over answers to an axis question, with no ground truth and no fixed correct answer to score against |
| **What survives** | the cluster-then-entropy computation itself, and the certainty/dispersion distinction it buys — invariance to paraphrase is a property of the construct, not of the dataset |
| **What does not** | the validation (factual QA and biography only), the [[calibration]] of $H_{\text{sem}}$ against confabulation risk, and any guarantee that $H_{\text{sem}}$ ranks candidate axes the way EIG would |

## Used as a training difficulty score

The measure has also been put to work in training. For each training query the policy's sampled answers are grouped by final answer and the entropy over the groups is computed; "Before training, we compute the semantic entropy" for every query, from the starting policy, and the dataset is sorted by it for a curriculum.[^s8] The use inherits the measure's blind spot: a policy that is confidently wrong on a question shows low dispersion there and would be scheduled as easy. That consequence is this wiki's inference; the training paper does not test it. See [[semantic-entropy-curriculum]].

## Cost

$N\times$ sampling per candidate question, plus $O(N^2)$ entailment calls to
build the partition — Farquhar et al. report a 5-to-10-fold generation
overhead. The cost is bearable only where sampling is parallel and the answers
are self-generated; against a human or a paid tool as the source (stall 4),
$N$ resamples of one question are not available at all. Kossen et al. (2024)
trade the sampling for a linear probe on hidden states, which requires
white-box access and an SE-labelled training set.

## Limits

- The two uses in *Why it matters* — axis selection and the
  contradiction/noise discriminator — are **this wiki's inference, untested**;
  the map rows on stalls 2 and 6 rest on them, not on a study.
- As a proxy for EIG it is biased: it measures the model's answer dispersion,
  not $I(\theta; Y_q)$ ([[expected-information-gain]]).
- Clustering by entailment needs an entailment model whose errors propagate
  into the partition and hence into $H$.
- Measures the **model's** uncertainty, not specification uncertainty; a
  confidently wrong model has low semantic entropy — by construction, since
  consistent error is not the target event.
- Validated on factual QA and biography generation, not on design questions.
- Token-level signals are not a safe stand-in for sampling-based ones, and the sign can flip. In one measured end-to-end pipeline, expression gated on mean answer-token probability ranked correctness below chance, while gating on sampling consistency discriminated.[^s4][^s5] The paper's reading is that, on an overconfident model, high token probability lifts fluent hallucinations into the assert category.[^s6] The below-chance logit result is "unresolved at the fact level", and the study is one model on a constructed benchmark.[^s7] Compare [[provenance-gated-assertion]], where the same confidence signals gate assertion.
- Dispersion of the answer alone ignores the context. Halperin argues for the change from context to answer instead, and for entropy production as the measure; the paper's own test of that claim is a correlation with its faithfulness score on simulated and ten real triplets, not a check against correctness labels. This is the paper's argument, not a result established here. See [[semantic-entropy-production]].[^s20]
- The clustering step is itself a weak point, on one later paper's account: the authors say "accurate semantic clustering is inherently brittle, i.e., a single response can belong to multiple plausible clusters", so one answer can be counted in more than one meaning.[^s21] A dispersion score on sample embeddings avoids the cluster boundary, but gives up the entailment judgement for the sentence encoder's geometry; see [[radial-dispersion-score]] for that trade and its limits. The paper's claim that this is more robust is measured by AUC on four QA and maths sets, not against human equivalence judgements.
- Dispersion of the model's own answers does not look at the evidence. ECLIPSE, a retrieval-grounded detector, states the gap as semantic entropy "which cannot distinguish honest uncertainty from evidence-ignoring behavior".[^s22] On its own 200-sample financial QA set, with constructed perturbations, the entropy-only baseline is the one it "outperform[s]" at AUC 0.50 in the abstract.[^s23] The same paper's Figure 1 legend gives that baseline 0.68, so the baseline value is not stable inside the paper. Its entropy estimate uses K = 10 samples, and the authors say this "yields noisy entropy estimates that may miss multimodal" structure.[^s24][^s25] Whether the evidence term helps on naturally occurring errors is not tested there.

## Related

[[entropy]] · [[expected-information-gain]] · [[cusum]] · [[renyi-ulam-problem]]

- [[radial-dispersion-score]] — a clustering-free dispersion of the same sampled answers, scored by distance from their centroid
- [[centroid-cancellation]] — why a centroid-based trace score saturates when answers split into opposed groups
- [[semantic-entropy-production]]
- [[structural-entropy]] — SE as the one-layer case of a family of structural entropies over a response graph; the equality is proved for a constructed quotient graph, not for the NLI graph of sampled answers[^s26]

[^s1]: farquhar-2024
[^s2]: kossen-2024
[^s3]: kuhn-2023
[^s4]: doi-10-48550-arxiv-2609-26035 — "ranks correctness below chance end to end (AUC 0.41, conversation-clustered)"
[^s5]: doi-10-48550-arxiv-2609-26035 — "gating on sampling consistency discriminates (AUC 0.66)"
[^s6]: doi-10-48550-arxiv-2609-26035 — "On this overconfident model the pattern is consistent with high token"
[^s7]: doi-10-48550-arxiv-2609-26035 — "unresolved at the fact level"
[^s21]: arxiv-2512-04351 — "accurate semantic clustering is inherently brittle, i.e., a single response can belong to multiple plausible clusters"
[^s20]: arxiv-2512-05156 — "the present work suggests that it is entropy production, rather than"
[^s8]: arxiv-2512-04359 — "Before training, we compute the semantic entropy"
[^s22]: arxiv-2512-03107 — "which cannot distinguish honest uncertainty from evidence-ignoring behavior"
[^s23]: arxiv-2512-03107 — "outperforming a semantic entropy-only baseline (AUC 0.50)"
[^s24]: arxiv-2512-03107 — "Entropy only: 0.68"
[^s25]: arxiv-2512-03107 — "This yields noisy entropy estimates that may miss multimodal"
[^s26]: arxiv-2511-16275 — "there exists a semantic graph such that the one-dimensional structural entropy of this graph is equal to semantic entropy"
