---
description: "The proportion of a reasoning trace's tokens generated after the model first voices uncertainty measures how far a model continues fabricating instead of stopping."
aliases: ["GapRatio", "Gap Ratio"]
sources: ["arxiv-2604-19656"]
---
# Ungrounded-reasoning gap ratio

> Detecting a gap and stopping at it are two different events in the same trace — the ratio is the distance between them, in tokens.

## Definition / Mechanism

Anonymous (2026) define GapRatio to quantify how much
of a reasoning trace continues *after* the model has already, in its own
words, registered that something is missing: "GapRatio = (T_total −
T_suspect)/T_total, where T_total is the total tokens generated and
T_suspect is the token position where the model first expresses
uncertainty." A GapRatio near 1 means the model voiced doubt almost
immediately and then generated a long trace anyway — [[gril|fabricating]]
through the gap rather than stopping at it; a GapRatio near 0 means the
model stopped close to where it first doubted. The metric needs no ground
truth about the missing premise, only a way to locate the first
uncertainty-expressing span in the trace, so it can score any reasoning
transcript, not only ones from a matched clarify/solve training setup.

Evaluated across three public under-specified-question datasets, training
against a stage-specific detection reward pulled the ratio down in every
case: "GRIL reduces this metric across all evaluation datasets. On SVAMP,
the GapRatio drops from 0.63 to 0.27; on Formula, from 0.43 to 0.40; on
GSM8K, from 0.37 to 0.30."[^c2]

## Why it matters

Accuracy and premise-detection rate both describe whether a model
eventually gets the right answer or names the right gap; neither describes
what happens between noticing and acting. GapRatio isolates that interval,
so it can distinguish a model that detects late but stops immediately from
one that detects early but keeps reasoning past its own doubt — two
failure shapes an aggregate success-rate number conflates. It gives a
[[detection-to-abstention-gap|detection-to-action gap]] a token-level
timeline instead of a single before/after count.

## Limits

Locating "the token position where the model first expresses uncertainty"
depends on a lexical or pattern match over hedging phrases ("let us
assume" and similar); the paper does not report this detector's own
precision or recall, so a GapRatio drop could partly reflect a change in
how a model phrases doubt rather than in when it stops reasoning.
`unverified`: whether GapRatio tracks fabrication severity linearly, or
only ordinally — a trace with GapRatio 0.5 is not established to contain
twice the fabricated content of one at 0.25. The metric is reported only
on math-style benchmarks derived by the same premise-deletion procedure as
the paper's training data.[^c3]

## Related

[[gril]] · [[detection-to-abstention-gap]] · [[abstention]] · [[calibration]]

[^c2]: arxiv-2604-19656 — "GRIL reduces this metric across all evaluation datasets. On SVAMP, the GapRatio drops from 0.63 to 0.27; on Formula, from 0.43 to 0.40; on GSM8K, from 0.37 to 0.30."
[^c3]: arxiv-2604-19656 — "our insufficient queries are synthetically constructed by deleting constraints from math datasets, which may introduce artifacts and cover only a narrow set of missing-information types, limiting generalization beyond arithmetic-style problems"
