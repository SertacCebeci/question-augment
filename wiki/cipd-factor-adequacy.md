---
description: "Personalization adequacy scored against six LLM-mined cognitive factors, validated by whether the score prefers a user's own accepted answer over the community's top-voted one."
aliases: ["CoPA", "Community-Individual Preference Divergence", "CIPD"]
sources: ["arxiv-2604-14773"]
---
# CIPD factor adequacy

> On Stack Exchange, the answer a user accepts and the answer the crowd
> upvotes are both good — and often different. That gap is a free label
> for whether a scorer actually measures personalization.

## Definition / Mechanism

Su et al. (2026) start from **Community-Individual
Preference Divergence (CIPD)**: cases where a Stack Exchange asker accepts
one answer while the community's vote favors a different one, though both
are high quality. Because the asker's choice is observed and independent
of vote count, the divergence is a ground-truth signal for personalization
that costs no manual labeling: "Such divergence provides a natural and
scalable signal for evaluating personalization."
[^c1]

They mine CIPD threads at scale, have an LLM infer each user's decision
rationale for the accepted answer over the top-voted one, and cluster the
rationales by cross-model consensus into six reusable **cognitive
factors** — not lexical or topical dimensions, but properties of the fit
between a response and a reader's cognition.
[^c2]

Each user's 50 most recent interactions are turned into a per-factor
preference profile. A held-out response is then scored per factor on a
3-point Likert scale — mismatch, partial, full match — and normalized.
[^c3]

The factors are validated the same way they were mined: a profile built
from the CIPD question that produced it should score the user's own
accepted answer above the community's top-voted one. Scored this way, the
method beats direct LLM-as-judge Likert scoring and chain-of-thought
judging by a wide margin on accuracy and tie rate.
[^c4]

An ablation confirms no factor is redundant — dropping any one degrades
accuracy, tie rate and score margin together.
[^c5]

The same factors, inserted into system prompts, improve two independent
personalization benchmarks and backbones they were never mined from,
evidence the factors are properties of personalized adequacy in general,
not artifacts of Stack Exchange.
[^c6]

## Why it matters

Generic informativeness or calibration scores treat an answer as good or
bad independent of who is asking. CIPD factor adequacy is a concrete
recipe for the opposite: derive the axes an answer must satisfy for *this*
asker from behavioral data, then judge adequacy against those axes rather
than against a single reference answer — and it has a built-in check,
because the same divergence that produced the factors also tells you
whether your scorer can tell the two answers apart.

## Limits

The six factors are mined once, from StackExchange rationales inferred by
an LLM (Cohen's κ 0.73, 97% expert-agreement rate against manual
inspection, but still an LLM's reading of intent, not the user's own
words). The evaluator that applies them is itself an LLM judge, so the
gain over Direct/CoT baselines is a gain over a weaker judge configuration
of the same family, not a validation against a judge-free ground truth
beyond the CIPD accept/top-vote signal itself. Accuracy tops out at
51–55%, well short of reliably separating accepted from top-voted
answers, and Tie Rate stays 18–26% even with the full factor set.

## Related

- [[relevance-completeness-divergence]] — the negative result this method
  answers: generic relevance metrics do not track what a specific reader
  needed.
- [[dual-judge-completeness-recall]] — another adequacy score built as a
  structured per-item rubric rather than a single holistic judgment.
- [[ground-truth-admission-test]] — the same move in another field:
  admitting an evaluation construct only after it passes a falsifiable
  behavioral check.
- [[calibration]] — adjacent adequacy axis this method does not cover:
  confidence expression, as opposed to fit to a reader's cognitive
  profile.

[^c1]: arxiv-2604-14773 — "Such divergence provides a natural and scalable signal for evaluating personalization."
[^c2]: arxiv-2604-14773
[^c3]: arxiv-2604-14773
[^c4]: arxiv-2604-14773 — "our evaluation based on distilled factors consistently reduces Tie Rates to 18.24%–26.28% and improves Accuracy to 51.43%–55.37%, demonstrating that distilled factors enable the identification of granular features aligned with user intent."
[^c5]: arxiv-2604-14773 — "the results indicate that removing any individual factor leads to a degradation in performance in terms of Accuracy, Tie Rate, and Score Margin, thereby demonstrating the necessity of each factor in capturing the user preferences."
[^c6]: arxiv-2604-14773 — "incorporating these factors, yielded consistent and significant performance gains across two distinct benchmark, two different backbone models, and all evaluated personalization methods."
