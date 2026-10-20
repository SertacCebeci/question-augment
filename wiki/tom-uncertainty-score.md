---
description: "UKA scores each candidate dialogue response by how much simulated user reactions disagree across competing need-hypotheses, then trades that against knowledge support to pick the next response."
aliases: ["ToM uncertainty", "ToM uncertainty score", "Theory-of-Mind uncertainty"]
sources: ["xu-2026-user"]
---
# ToM uncertainty score

> Instead of scoring a question by [[entropy]] over an explicit posterior, score a
> candidate *response* by how much simulated user reactions to it disagree
> across the asker's competing hypotheses about what the user needs.

## Definition / Mechanism

Xu et al. (2026) propose User-Aware Active Knowledge
Acquisition (UKA) for emotional-support dialogue. At each turn the system
holds a set of $M$ competing hypotheses about the user's latent need,
generates $N$ candidate responses, and for each candidate $c_j$ runs a
Theory-of-Mind (ToM) simulator that produces simulated next-turn user
replies under every hypothesis, embedding each as $e_i = e(u_i, c_j)$. The
ToM uncertainty score is the average cross-hypothesis disagreement of those
embeddings:

$$S_u(c_j) = 1 - \frac{1}{M}\sum_{i=1}^M \cos(e_i, \mu), \quad \mu = \frac{1}{M}\sum_{i=1}^M e_i$$

"The ToM uncertainty score Su (cj ) favors responses whose action-conditioned
user reactions differ across competing need hypotheses, yielding more
informative feedback for belief updating and knowledge writing."[^c1]

A second score, knowledge support $S_k(c_j)$, is the candidate's average
cosine similarity to its nearest retrieved knowledge entries. UKA combines
the two with an explicit train/test asymmetry: "training favors responses
that expose missing knowledge, whereas testing favors responses supported by
the acquired memory while retaining mild diagnostic value" — training picks
$\arg\max_{c_j}\, S_u(c_j) - S_k(c_j)$ (explore past the knowledge
boundary), test picks $\arg\max_{c_j}\, S_k(c_j) + \gamma\, S_u(c_j)$
(grounded, with residual diagnostic value).[^c2]

## Why it matters

This is a selection criterion for *what to say next* that plays the role
[[expected-information-gain|EIG]] and [[volume-removal|volume removal]] play
for *which question to ask next*, but built without a hand-specified
likelihood model: disagreement is read off embeddings of simulated LLM
rollouts rather than an entropy or KL term over an explicit posterior.

## Transfer

| | |
|---|---|
| **Home field** | active learning's disagreement/uncertainty-based instance selection (cited generically by the authors to Settles 2009; Lewis & Gale 1994), where a learner scores unlabeled instances by model uncertainty or committee disagreement to choose what to label next |
| **Here** | selecting which full natural-language *response* an emotional-support dialogue agent should produce next, where the "labels" are simulated user reactions under competing need-hypotheses rather than ground-truth annotations |
| **What survives** | the shape of the criterion — score a candidate action by how much it would make competing hypotheses disagree, then subtract or add a groundedness term depending on whether the goal is exploration (training) or reliable support (test) |
| **What does not** | any entropy- or KL-based guarantee: $S_u$ is a cosine-similarity disagreement statistic over ToM-simulated embeddings, not a proven information measure, so results like EIG's non-negativity or volume removal's degeneracy theorem (Bıyık et al. 2019, Theorem 1) do not transfer — the paper reports empirical wins on three benchmarks (§5), not a bound on $S_u$ itself |

## Limits

- $S_u$ and $S_k$ are reported only as ablations and benchmark-average scores
  across four LLM backbones and three emotional-support benchmarks (ESConv,
  ExTES, Sentient Eval); no formal guarantee is given for the disagreement
  statistic itself, unlike the entropy-based criteria on this stall's map.
- The ToM simulator's reactions are themselves LLM-generated (not real user
  replies) at both train and test time; a systematic bias in the simulator
  would bias $S_u$ the same way at both stages.
- $\gamma$ (the test-time trade-off weight) is fixed at 1 by the authors'
  default and not shown to be robust to other settings in the extract read
  here.

## Related

[[expected-information-gain]] · [[volume-removal]] · [[generalized-binary-search]] · [[value-of-information]]

[^c1]: xu-2026-user — "The ToM uncertainty score Su (cj ) favors responses whose action-conditioned user reactions differ across competing need hypotheses, yielding more informative feedback for belief updating and knowledge writing."
[^c2]: xu-2026-user — "training favors responses that expose missing knowledge, whereas testing favors responses supported by the acquired memory while retaining mild diagnostic value"
