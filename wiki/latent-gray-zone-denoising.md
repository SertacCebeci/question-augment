---
description: "Abstention fine-tuning data is filtered by distance from a linear truthfulness-probe hyperplane, discarding boundary samples where response-accuracy labels are noisy."
aliases: ["GeoDe", "Geometric Denoising", "geometric denoising for abstention fine-tuning"]
sources: ["arxiv-2604-14324"]
---
# Latent gray-zone denoising

> The response was a lucky guess, or the refusal was a formatting
> accident — either way, the label the sample got is noise, and the noise
> lives in one place: near the decision boundary.

## Definition / Mechanism

An, Lou, Guo & Xu (2026) diagnose why abstention
fine-tuning — training a model to answer "known" questions and say "I
don't know" to "unknown" ones — degrades when known/unknown is assigned
purely by response-level correctness: "Relying on response-level accuracy
to partition "known" and "unknown" sets introduces significant label
noise—such as "lucky guesses" or formattingdriven failures." Probing
the model's hidden states shows these mislabeled cases cluster in a
**"gray zone"** — the region straddling the model's own latent decision
boundary, where internal belief is ambiguous — while samples far from
that boundary are cleanly separated by correctness.

**GeoDe (Geometric Denoising)** turns this diagnosis into a filter. A
logistic-regression probe $f_{probe}(x)=\sigma(w^\top x+b)$ is trained on
a diagnostic pass's hidden states $x=f_{LLM}(q)$ (either the last token of
the question before generation, TBG, or the last token of the generated
question+answer, SLT), labeled by whether the base model answered
correctly. Its distance $d(x)=(w^\top x+b)/\lVert w\rVert_2$ gives, for
any new sample, both a sign — the probe's known/unknown call — and a
magnitude: "d(x) has a clear geometric meaning that reflects the model's
confidence in answering the given question. d(x) > 0 means the model
believes it can answer correctly, while d(x) < 0 means the opposite, and
a larger |d(x)| value indicates stronger confidence." GeoDe keeps
only the top $X\%$ of the fine-tuning set by $|d(x)|$ — the samples the
probe is most confident about — discarding the ambiguous middle before
building the abstention dataset (correct answers kept verbatim; incorrect
ones relabeled "I don't know").

$X{=}25\%$ was optimal across benchmarks: "at X=25% on the majority of
metrics: on TriviaQA, this yields F1rel = 77.6, while on NQ it yields
F1rel = 61.6. When X is too small (e.g., 6.25%), performance drops due to
insufficient training data; when X is too large (e.g., 75%), noisy
boundary samples are reintroduced, degrading reliability." The
filter is agnostic to which extraction point is used: "TBG and SLT
exhibit comparable performance across benchmarks, with no single strategy
consistently outperforming the other."[^c4]

## Why it matters

The correction targets *where* label noise concentrates, not how much of
it there is — a proxy (geometric distance to a cheap linear probe) stands
in for the accuracy label the training procedure would otherwise trust
uniformly. It needs no extra annotation beyond the diagnostic pass already
required to build the known/unknown split, and composes with any
supervised abstention-tuning pipeline that starts from such a split.

## Limits

Validated only from 1.7B to 8B parameters; not evaluated at larger scale,
where the truth direction may not be well captured by a single linear
probe. Experiments are restricted to short-form QA and RAG; reasoning and
long-form generation are untested. Denoising the training set does not
remove abstention fine-tuning's own over-abstention risk — the authors
name this an open trade-off, **unverified** beyond their own caveat.

## Related

- [[abstention]] — the target behavior GeoDe fine-tunes toward.
- [[trajectory-geometry-uncertainty-probe]] — geometry of hidden-state
  computation as an inference-time confidence signal, not a training-set
  filter.
- [[density-ridge-selective-prediction]] — a different geometric
  abstention score (density-ridge distance), also inference-time.
- [[knowledge-boundary-aware-reward]] — addresses the same abstention-RL
  failure mode (reward-side, not data-side) by flipping reward sign
  instead of filtering training data.
- [[calibration-training]] — calibration as a trainable property of a
  set of answers, the broader family this data-curation step serves.

[^c4]: arxiv-2604-14324 — "TBG and SLT exhibit comparable performance across benchmarks, with no single strategy consistently outperforming the other."
