---
description: "An RL reward for a question-asking agent scored entirely on the effect it has on the answerer's next reply — its goal-relevance, novelty and induced brevity — never on the question's own text."
aliases: ["goal-relevance-novelty-succinctness reward", "inquisitive dialogue reward"]
sources: ["lin-2026-dual"]
---
# Elicited-response reward

> Score the question by what it pulls out of the answerer, not by anything
> about the question's own wording: "Unlike conventional dialogue rewards
> that primarily assess the agent's own utterance, our inquisitive setting
> focuses on how effectively the justice's utterance elicits information
> from the attorney's subsequent response."

## Definition / Mechanism

Lin, Deng, Wang & Yang train their dialogue policy with a scalar reward
that is a weighted sum of three components, each measured on the
attorney's *response* to the justice's question rather than on the
question itself.[^c1]

**Goal-relevance**: an LLM judge (Llama-3-8B) scores the maximum semantic
similarity between the attorney's response and any sub-conclusion of the
case's overall conclusion, "to incentivize probing related to the agent's
goal." **Novelty**: a length-normalized variant of Distinct-N (the
Expectation-Adjusted Distinct metric), adapted "to track newly introduced
tokens relative to the dialogue history" rather than merely distinct
tokens within one utterance — the reward rises with how much new content
the question pulls out that was not already on the table. **Succinctness**:
the negative log token-length of the attorney's response, rewarding
questions that produce short, direct answers, "treating it as evidence
that the justice's utterance ... was well-targeted."[^c2]

An ablation removing any one component reduces at least one of the four
evaluation metrics; removing novelty specifically "reduces OS from 4.34 to
4.29, suggesting that without encouraging fresh information, the dialogue
risks becoming less directional." A separate human evaluation (1–5 scale
on the same four metrics) confirms the same ordering: "Our full model
achieves the highest overall score (4.53), outperforming both SaulLM-7B
... and all ablated versions."[^c3]

## Why it matters

The map's other reward for training a question-asker is EIG treated as a
preference label ([[preference-optimization-for-questions]]) — a
task-independent, distributional quantity computed over possible answers
before any answer is observed. This reward needs no distribution over
answers and no [[entropy]] computation at all: it scores the answer that
actually arrived, using an LLM judge for topical relevance, a
lexical-novelty statistic for new content, and response length for
directedness. It substitutes cheap, observable proxies on the realized
answer for the unobservable expected information the answer might have
carried.

## Limits

The three weights combining the components into one scalar are not
reported as separately tuned or justified; the ablation shows each
component matters but not how sensitive the ranking is to the weights
chosen. All evidence is from one domain (Supreme Court oral argument) with
an LLM judge (Llama-3-8B) whose own relevance judgments are unverified
against a ground truth, and the succinctness component assumes short
answers are a virtue of a well-targeted question — true for this
adversarial, closed-answer setting but not a general property of good
questions.[^c4]

## Related

[[preference-optimization-for-questions]] · [[semantic-entropy]] · [[appraisal-gated-topic-switching]] · [[expected-information-gain]]

[^c1]: lin-2026-dual
[^c2]: lin-2026-dual
[^c3]: lin-2026-dual — "reduces OS from 4.34 to 4.29, suggesting that without encouraging fresh information, the dialogue risks becoming less directional"
[^c4]: lin-2026-dual
