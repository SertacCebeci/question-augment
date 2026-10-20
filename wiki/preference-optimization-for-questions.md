---
description: "Not through prompts but through weights: [[expected-information-gain|expected information gain]] turned"
aliases: ["DPO for question quality", "EIG-rewarded questioning", "learning to ask by preference optimization"]
sources: ["mazzaccara-2024", "acikgoz-2025"]
---
# Preference optimization for questions

> Not through prompts but through weights: [[expected-information-gain|expected information gain]] turned
> into a preference label, and the ranking ability that survives the domain
> it was trained on.

## Mechanism

Mazzaccara, Testoni and Bernardi (Findings of EMNLP 2024) install[^s1][^s2]
question-selection ability by preference optimization rather than by
prompting:

```text
1. Sample many candidate questions from the model for each game state
2. Score each candidate by EIG against the enumerated candidate set Ω
   (the model itself annotates the yes/no answer to each candidate)
3. Pair optimal (EIG = 1) against suboptimal (EIG < 0.8) candidates
4. Train with DPO on those pairs
```

The evidence base is narrow and worth stating exactly. The setting is the
[[twenty-questions|20-questions]] game with polar questions and a *closed* candidate set:
$|\Omega| = 8$ over six McRae categories, 10,000 training games, 55,000
preference pairs, one base model (Llama 2-chat 7B). EIG is exactly
computable because $\Omega$ is enumerable and answers are binary; a question
is optimal when it halves $\Omega$.

The transfer evaluation is five held-out sets of 29–90 candidate sets each:
unseen concepts in seen categories, unseen categories, celebrities, and sets
of different size ($|\Omega| = 16$ and $29$). DPO raised success-at-1 on the
in-category set from 56.7% to 68.9% with fewer questions asked (7.1 → 5.2),
and on the hardest out-of-distribution set (BigBench, $|\Omega| = 29$) from
17.2% to 31.0% — the latter *without* an EIG gain (0.31 → 0.28), so on that
set the transfer shows in task success, not in the trained criterion.

## Known as

| Field | Name there | Match |
|---|---|---|
| LLM training | preference optimization for questions | exact |
| LLM training | DPO for question quality | exact — names the algorithm used |
| information-theoretic dialogue | EIG-rewarded questioning | exact — names the label source |
| NLP (paper title fragment) | learning to ask by preference optimization | exact |

**Not this concept.** Bare *learning to ask* names the whole research line,
including RL-reward training of proactivity (below), which optimises a
different objective and is measured on different quantities. It is not an
alias here.

## Why it matters (prompt-level counterpart)

What this wiki takes is not the fine-tuning recipe but the **criterion**:

> Questions can be ranked by EIG, and the ranking survives a change of
> domain.

The prompt-level counterpart — generate $N$ candidates, rank by an EIG
proxy, ask the best — is this wiki's inference, not the paper's result; it
is the practical use of the generation/recognition asymmetry from
[[question-asking-as-program-generation]]. See `## Transfer` for what does
not come with it.

## RL-reward training of proactivity — a neighbouring object

Acikgoz et al., *SpeakRL* (arXiv 2512.13159, December 2025) put clarification
and proactive interaction into an RL reward directly, rather than into
preference pairs derived from EIG: a reward formulation for balancing asking
against acting, trained on a synthetic task-oriented dialogue set, reporting
+20.14 points absolute task completion over the base model without more
turns. It is a different object from this note's — no information-theoretic
label, no enumerable $\Omega$ — and belongs in its own note.

## Transfer

| | |
|---|---|
| **In its home field** | EIG computed exactly over an enumerable candidate set $\Omega$ with binary answers and a scorer; used to label DPO preference pairs; the ability is installed in the weights. |
| **Here** | An EIG *proxy* over $N$ sampled candidate questions, evaluated at inference time by a model that was not trained on it. |
| **What survives** | The shape *rank-by-EIG-then-ask*, and the evidence that a ranking learned on one candidate distribution helps on others — the ability was not tied to the training categories or to $|\Omega| = 8$. |
| **What does not** | The oracle EIG (open answer spaces need a surrogate of unstated quality); the weight update, which is where the ability was actually placed; and the measured cross-domain result, which was measured for the DPO-trained model only — nothing in the paper tests prompt-time reranking. |

## Limits

- One paper, one 7B base model, one game format: polar questions over a
  closed candidate set. The authors name the closed set, the polar
  question/answer format, and the single model size as their own limits.
- EIG here is computed from the model's *own* yes/no annotation of each
  candidate, and assumes every candidate in $\Omega$ is equally likely; both
  assumptions are the paper's, and both break on ambiguous questions.
- The EIG ranking — trained or prompt-level — presupposes an enumerable
  candidate answer/world set and a scorer over it. Where the space of answers
  is open, EIG is a proxy of unstated quality and the rule "ask the
  highest-EIG candidate" has no defined quantity to rank by.
- The prompt-level counterpart (generate $N$, rank, ask) is inferred here and
  untested anywhere in the cited work.
- `acikgoz-2025` is an arXiv preprint read at abstract level only, not peer
  reviewed; the paragraph citing it claims nothing beyond the existence of
  the reward formulation and the reported number.

## Related

[[expected-information-gain]] · [[question-asking-as-program-generation]] · [[clarification-benchmarks]] · [[preference-signal-against-asking]]

[^s1]: mazzaccara-2024
[^s2]: acikgoz-2025
