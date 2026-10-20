---
description: "Estimates whether an LLM should ask a clarifying question by simulating the user's answers to a greedily-generated clarifying question and scoring entropy over the NLI-clustered intents."
aliases: ["Intent-Sim", "INTENT-SIM"]
sources: ["zhang-2023"]
---
# Intent-Sim

> Deciding whether to ask a clarifying question by simulating the
> conversation the question would start, not by scoring the original
> answer's confidence.

## Definition / Mechanism

Zhang & Choi (2023) estimate the utility of clarifying on
input $x$ as the [[entropy]] over **simulated user intents**: "In our proposed
method, I NTENT-S IM, we disentangle these two factors by explicitly
estimating the [[efe-planning-as-variational-inference|ambiguity]] of a given input, which we quantify as the entropy
over simulated user intents."[^c1]

The algorithm (their Figure 2): (1) greedily generate one clarifying
question $q$ from $x$; (2) sample $S$ user responses $a_i$ to $q$ at
temperature $T$; (3) build an equivalence graph over the $a_i$ using an NLI
model — two responses are joined if the clarifying-QA pairs $[q;a_i]$ and
$[q;a_j]$ entail each other in either direction; (4) take connected
components as distinct simulated intents, with empirical probability
$\hat p(c\mid x) = |c|/S$; (5) return $u = H(\hat p(\cdot\mid x))$, the
Shannon entropy of that distribution: "We then simulate different user
intents by sampling multiple responses to the clarifying question... we
then cluster sets of semantically equivalent responses using a DeBERTa-large
NLI model... Finally, we compute our uncertainty estimate by computing the
entropy of this distribution over semantically [equivalent responses]."[^c2]

This score is Task 1 of [[clarifying-interaction-decomposition]]: it decides
*when* to ask, not what to ask or how to use the answer.

## Why it matters

It disentangles **aleatoric** uncertainty (the input genuinely admits
several readings) from **epistemic** uncertainty (the model lacks the
knowledge to answer) — a system with low aleatoric and high epistemic
uncertainty should not ask a clarifying question, since clarification
cannot supply missing world knowledge; Intent-Sim measures only the former,
because it clusters over hypothetical user *answers to a clarifying
question*, not over the model's own answer distribution.

Empirically it beats a Likelihood baseline, a Self-Ask baseline, and
[[semantic-entropy]] applied to the original answer distribution at
identifying which predictions benefit from clarification, under a fixed
interaction budget: "When only allowed to ask for clarification on 10% of
examples, our system is able to double the performance gains over randomly
selecting examples to clarify," and it "performs the best at identifying
when asking for clarification will improve expected performance in four out
of six of the LLM-plus-task settings evaluated in this work" across
QA/MT/NLI and GPT-3/LLaMA-2.[^c3]

## Transfer

| | |
|---|---|
| **Home field** | [[semantic-entropy]]'s cluster-then-entropy computation: sample $N$ answers to one fixed question, cluster by bidirectional NLI entailment, take entropy over cluster proportions, as a confabulation detector |
| **Here** | apply the same clustering machinery to simulated *answers to a clarifying question about the input*, not to answers to the input itself — the entropy measures ambiguity of $x$, not correctness of a generated answer |
| **What survives** | the sample-cluster-entropy pipeline and the NLI-entailment equivalence test |
| **What does not** | the target event (confabulation risk → input ambiguity) and the object sampled (direct answers → hypothetical user responses to a system-generated clarifying question, itself a single greedy sample and so a second source of error the semantic-entropy setup does not have) |

## Limits

- The clarifying question $q$ is generated once, greedily; if that single
  question fails to expose the input's real ambiguity, the simulated
  responses cluster on the wrong axis and the entropy estimate is wrong
  regardless of how good the answer-simulation step is.
- Best on only 4 of 6 LLM-task settings tested, not uniformly best; the
  paper reports it "consistently outperforms" baselines in aggregate but
  the per-setting AUROC table shows exceptions (e.g. LLaMA-2/MT).
- Validated only where the "user" can be simulated by resampling the same
  LM's own responses (self-supervision); against a real external source of
  answers (stall 4) the $S$ simulated responses are not available at the
  same cost.
- Requires an NLI entailment model as the equivalence test, whose errors
  propagate into the intent partition and hence into the entropy score —
  the same dependency [[semantic-entropy]] has on its entailment model.

## Related

[[clarifying-interaction-decomposition]] · [[semantic-entropy]] · [[clarification-only-aleatoric-uncertainty]] · [[uncertainty-decomposition]] · [[expected-information-gain]]

[^c1]: zhang-2023 — "In our proposed method, I NTENT-S IM, we disentangle these two factors by explicitly estimating the ambiguity of a given input, which we quantify as the entropy over simulated user intents."
[^c2]: zhang-2023 — "We then simulate different user intents by sampling multiple responses to the clarifying question"
[^c3]: zhang-2023 — "When only allowed to ask for clarification on 10% of examples, our system is able to double the performance gains over randomly selecting examples to clarify"
