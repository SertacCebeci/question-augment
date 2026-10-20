---
description: "Rather than committing to one rewritten stand-alone query, extract a Given the current, ambiguous, context-dependent utterance in a multi-turn dialogue, Jang, Lee,"
aliases: []
sources: ["jang-2026"]
---
# CompCQR: compositional query generation for conversational search

> Rather than committing to one rewritten stand-alone query, extract a
> handful of atomic pieces of the utterance once and enumerate every ordered
> subset of them as a distinct retriever query, then let coverage-then-precision
> aggregation pick the evidence — trading one best-guess reformulation for
> combinatorial redundancy at a fixed LLM-call budget.

## Mechanism

Given the current, ambiguous, context-dependent utterance in a multi-turn[^s1]
dialogue, Jang, Lee, Shin & Jung (2026) extract five atomic
components with two LLM calls: the original utterance $q$; an LLM-rewritten
stand-alone query $\tilde q$ and its anticipated answer $\tilde a$ (first
call); a follow-up query $q_f$ and its anticipated answer $a_f$ (second
call). Every ordered subset of these five components, at every length from 1
to 5, is concatenated into its own query string — $5+20+60+120+120=325$
distinct query variants, produced by string permutation alone, with no
further LLM calls. Each variant is sent to the same retriever (dense or
sparse); the 325 resulting ranked lists are fused by Reciprocal Rank Fusion,
which favours documents retrieved near the top by more of the variants — a
coverage step. A third LLM call reads the top of the fused list and selects
the single document most likely to support answering the original
utterance — a precision step. The whole pipeline costs 3 LLM calls, against
5 (LLM4CS), 6 (CHIQ-Fusion) or 16 (AdaRewriter) for training-free or hybrid
baselines that each produce far fewer query variants (2-16 per turn).

## Why it matters

Stall 3 asks how a question touches the axis; every other row on
Formulation treats the wording problem as: classify the [[efe-planning-as-variational-inference|ambiguity]],
then commit to one phrasing (or one rewrite) that resolves it. CompCQR's
answer is not to phrase better but to phrase *differently*, many times,
cheaply, and let the retriever's own aggregate response do the
disambiguating — a strategy available only because
[[retrieval-order-sensitivity]] shows a machine answering channel can be
queried at near-zero marginal cost and returns a different, partially
overlapping slice of evidence for each structurally distinct phrasing.
Measured across four conversational-search benchmarks (TopiOCQA, QReCC,
CAsT-19 and a fourth) with several open- and closed-source LLMs and both
dense and sparse retrievers, the authors report up to 22.5% relative MRR
improvement over the strongest prior baseline (Jang et al. 2026, abstract),
with reported MRR of 48.7 (TopiOCQA, dense, GPT-4.1-mini), 41.3 (TopiOCQA,
sparse), 61.5 (QReCC, dense) and 75.8 (CAsT-19, dense). A Shapley-value
decomposition finds the rewritten query's anticipated answer $\tilde a$ the
single most influential component (Shapley value 16.2 dense / 14.54 sparse)
and shows that *where* a component sits in the concatenation, not only
whether it is included, changes dense-retriever performance.

## Transfer

| | |
|---|---|
| Home field | Conversational information retrieval: a fixed, indexed corpus, graded relevance judgments, success scored by MRR/NDCG against gold passages. |
| Here | Any agent facing a general external answering channel that can be queried many times per turn at negligible cost, after an ambiguous, context-dependent utterance. |
| What survives | The strategic move: when one channel is cheap to re-query, generate a combinatorially large but computationally cheap set of structurally distinct phrasings of the same request instead of committing to one rewrite, then combine the returned evidence by maximising coverage first (fusion across phrasings) and precision second (a targeted reasoning pass over the fused result). |
| What does not | The retrieval-specific machinery — Reciprocal Rank Fusion's rank-based scoring, dense/sparse embedding matching, and MRR as the success metric — presumes a queryable, rankable evidence store; it does not transfer to a channel that cannot be asked hundreds of times at no social cost (a human respondent) or that returns no ranked list at all. |

## Limits

- Every number above is the authors' own, on four English
  conversational-search benchmarks with GPT-4.1-mini and other LLMs the
  wiki has not independently replicated.
- The abstract's "up to 22.5% relative MRR improvement over the previous
  state-of-the-art baseline" could not be pinned this pass to one specific
  baseline/dataset cell of the paper's results tables; a nearby comparison
  in the same table (CompCQR 48.7 vs ConvSearch-R1 50.5 MRR on TopiOCQA
  dense) runs the other way, so the headline figure is carried as the
  abstract's own claim, not as a verified single table cell.
- The method presumes a rankable retrieval index behind the "source"; it
  says nothing about querying a source that can be asked only once, or
  that returns no document list, so it does not generalise to the
  user-as-source case on Source.
- Training-free means no fine-tuning of the retriever or a rewriting
  model; the pipeline still needs a capable base LLM for the two-to-three
  prompt calls.

## Related

[[retrieval-order-sensitivity]] · [[survey-response-model]] · [[self-ask-decomposition]] · [[tree-search-methods]] · [[ambiguity-taxonomy]]

[^s1]: jang-2026
