---
description: "A stopping rule built on a plug-in generalized-likelihood-ratio statistic with a self-normalized time-uniform boundary, giving finite-sample precision guarantees under unknown sampling variance."
aliases: ["unified precision-guaranteed stopping rule", "self-normalized GLR boundary"]
sources: ["arxiv-2604-07913"]
---
# Plug-in GLR stopping rule

> Calibrating a likelihood-ratio boundary on mean and variance uncertainty
> separately is what makes existing sequential tests conservative; calibrating
> the boundary directly on the self-normalized statistic that mixes both is
> what removes the slack.

## Definition / Mechanism

Contextual learning — mapping a context to an action through sequential data
collection, from any mix of offline, simulated or online sources — is cast as
one abstraction: observations adapted to a filtration, with a random stopping
time. "The stopping rule is defined as a stopping time τ with respect to the
filtration {Ft }t≥1" (Ding et al. (2026)).[^c1]

When the sampling variance at each context-action pair is unknown, the
ordinary generalized-likelihood-ratio (GLR) statistic for "does the current
best action dominate this challenger" needs the variance estimated too. The
paper's fix replaces it with a **plug-in GLR statistic** built from the
sample variance directly, then calibrates its stopping boundary from a new
time-uniform deviation inequality that controls the *self-normalized*
statistic in one step, rather than bounding the mean-deviation and the
variance-deviation separately and adding the two bounds: "we derive new
time-uniform deviation inequalities that directly control the
self-normalized GLR evidence and thus avoid the conservativeness caused by
decoupling mean and variance uncertainty."[^c2]

The stopping rule triggers once every challenger, at every context, is
dominated beyond its calibrated boundary. Two precision targets are given
this same mechanism: a context-wise (Weighted-PAC) criterion and an
aggregate policy-value (PAC) criterion, and each gets its own boundary
calibration from the same plug-in statistic. Under Gaussian sampling noise
independent across stages, the calibrated rule is proved to hit its target
error rate exactly: "the stopping rule τα,δ satisfies the corresponding
target guarantee: when r = 1, PI ≥ 1 − α; when r = 2, PII ≥ 1 − α."[^c3]

The boundary calibration is the same whichever sampling strategy picks the
next context-action pair — equal allocation, an optimal-computing-budget
allocator, a track-and-stop design — so the rule composes with any of them
instead of being tied to one experiment design. The same idea extends to a
structured linear setting via a mixture-martingale calibration for
directional, rather than worst-case, parameter deviation.

## Why it matters

A threshold-based stopping rule ([[sprt|SPRT]]) already shows that
calibrating on the right statistic, not the largest available bound, buys
sample efficiency without spending precision. This work shows the same trade
survives a harder setting — many simultaneous pairwise comparisons, unknown
variance, and an experiment run under an arbitrary, possibly adaptive
sampling policy: "our stopping rules require substantially fewer samples to
identify the correct policy with precision guarantee compared with JDK and
KN" (arxiv-2604-07913), where JDK is a variance-unknown GLR rule
calibrated the older, decoupled way. The generalizable point: when a
stopping statistic is built from several estimated nuisance parameters,
bounding each one's error separately and summing the bounds is not the
tightest valid boundary — bounding the statistic's own tail directly can be.

## Limits

The guarantee is proved under Assumption 1 (independent sampling noise
across stages) and Assumption 2 (Gaussian noise, known-form but unknown
variance) — "these assumptions... are standard in the literature on
sequential testing, BAI, and contextual learning" but are still assumptions,
not derived from the data. The unstructured setting scales with the number
of context-action pairs; the linear extension is offered specifically
because the unstructured boundary does not scale to large context spaces.
The comparison to prior work (JDK, KN, TS) is empirical, on synthetic
instances and two case studies, not a universal dominance proof.

## Related

- [[sprt]]
- [[stopping-rules]]
- [[cramer-rao-bound]]
- [[value-of-information]]
- [[generalized-binary-search]]

[^c1]: arxiv-2604-07913 — "The stopping rule is defined as a stopping time τ with respect to the filtration {Ft }t≥1"
[^c2]: arxiv-2604-07913 — "we derive new time-uniform deviation inequalities that directly control the self-normalized GLR evidence and thus avoid the conservativeness caused by decoupling mean and variance uncertainty."
[^c3]: arxiv-2604-07913 — "the stopping rule τα,δ satisfies the corresponding target guarantee: when r = 1, PI ≥ 1 − α; when r = 2, PII ≥ 1 − α."
