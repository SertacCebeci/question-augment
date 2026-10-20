---
description: "Conditions an LLM's clarify/abstain/answer decision on its own K sampled generations via the prompt, raising QA accuracy over prompt-only baselines."
aliases: ["BAG", "Belief-Augmented Generation"]
sources: ["baan-2026"]
---
# Belief-Augmented Generation

> A prompt-only mechanism that lets an LLM decide whether to answer, ask a
> clarifying question, or abstain by reasoning over its own sampled belief
> state rather than a single generation — the answerer's commit-or-defer
> decision, grounded in the model's own uncertainty instead of a heuristic.

## Definition / Mechanism

An LLM defines a distribution over responses; sampling $K$ generations for
a fixed input yields a *belief state* $B_\theta(x)=(Y^{(1)},\dots,Y^{(K)})$
(Baan et al. 2023). Belief-Augmented Generation (BAG) is a two-stage
procedure: first the model is sampled $K$ times for the user's question;
then those $K$ generations are fed back into a second prompt that asks the
model to analyse them and choose one of three conversational strategies —
**clarify**, **abstain**, or **answer** — and execute it. "We call our
method Belief-Augmented Generation or BAG: conditioning generation
directly on the belief state (rather than external documents in RAG) via
the prompt." BAG+ repeats the procedure on later turns (e.g. after a
clarification exchange), resampling and re-deciding a strategy from the
updated belief state; it requires no training, no external data, and works
on closed models accessed only by sampling. The mechanism costs $K$
samples plus one more prompt to reason over them — comparable to other
sample-based methods it unifies (MBR, [[semantic-entropy|semantic entropy]], self-consistency,
verbalised uncertainty) — but the one decision now determines three things
at once: whether to answer, how to answer, and whether/how to clarify.[^c1]

## Known as

| Field | Name there | Relation |
|---|---|---|
| LLM uncertainty / interaction research | BAG | exact — the paper's own abbreviation for Belief-Augmented Generation |

## Why it matters

Evaluated on AmbigQA-derived ambiguous QA across six LLMs (Qwen3, OLMo2,
OLMo3, Gemini-2.5-Flash) with a human-reference LLM judge, a single BAG
round beats the standard direct-answer baseline in 17/18 model–prompt
configurations, and a prompt-only baseline that names the same strategies
without belief-state conditioning (SAG) in 15/18: "The best prompt variant
per model improves over the standard one intent baseline by 12.4 points
averaged across models (a 34% relative improvement) ... and over SAG by
10.2 points." Applying BAG at both turns (BAG+) improves further, by 18.5
points averaged across models over baseline and 15.1 points over an oracle
that receives the disambiguated question directly.[^c2]

The strategy decisions are also more faithful to the model's own
uncertainty than prompting for the same three strategies without the
sampled belief state: "BAG is more faithful to the predictive distribution
than SAG, answering directly when [[entropy]] is low, increasingly clarifying
and abstaining as entropy increases," whereas "the prompt-only SAG is not
aligned with belief state entropy."[^c3]

Without any such mechanism, models almost never choose to clarify or
abstain: "Direct generation without any augmentation strategy rarely
clarifies or abstains at all: classifying generations with Gemini-2.5-Flash
we find they only do so on 3% of the questions." This is the same
under-asking deficit [[clarification-benchmarks]] documents across many
benchmarks; BAG is offered as one mechanism that closes part of it by
grounding the decision in sampled uncertainty rather than a bare
instruction to consider asking.[^c4]

## Limits

- Evaluated only on one task family (multi-turn ambiguous factual QA from
  AmbigQA) and six models; the paper itself states "disentangling when to
  clarify from when to abstain, however, remains challenging" — the
  mechanism does not resolve this, it operationalises a decision between
  them.
- Accuracy is scored by an LLM judge (Gemini-2.5-Flash), reported at a 97%
  correctness rate against a small manual check, not a fully human-graded
  metric.
- Requires the ability to draw $K$ independent samples from the same model
  under the same prompt; the reported cost is parallelisable but real —
  reasoning-mode sampling was found to cost "7x more output tokens than
  direct generation, for just 2 more accuracy points" in one preliminary
  test, and brevity-inducing prompts that cut cost also strip the verbal
  cues (hedging, interpretation markers) that make a belief state
  informative.
- Compares against a prompt-only baseline (SAG) and a disambiguation
  oracle on one paper's own runs; no independent replication is cited.

## Related

[[clarification-benchmarks]] · [[semantic-entropy]] · [[value-of-information]]

[^c1]: baan-2026 — "We call our method Belief-Augmented Generation or BAG: conditioning generation directly on the belief state (rather than external documents in RAG) via the prompt."
[^c2]: baan-2026 — "The best prompt variant per model improves over the standard one intent baseline by 12.4 points averaged across models (a 34% relative improvement), ranging from 5.8 (OLMo2-7B) to 25.7 (Qwen3-8B), and over SAG by 10.2 points."
[^c3]: baan-2026 — "BAG is more faithful to the predictive distribution than SAG, answering directly when entropy is low, increasingly clarifying and abstaining as entropy increases."
[^c4]: baan-2026 — "Direct generation without any augmentation strategy rarely clarifies or abstains at all: classifying generations with Gemini-2.5-Flash we find they only do so on 3% of the questions."
