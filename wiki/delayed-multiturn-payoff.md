---
description: "Questioning a subtle target shows no gain for a turn, then jumps; a salient target saturates after one question, so a shallow turn budget looks sufficient for both until tested on the hard case."
aliases: ["non-linear turn-depth effect"]
sources: ["arxiv-2604-03040"]
---
# Delayed multi-turn payoff

> On an easy target one question is already enough; on a hard target the
> first extra question looks equally useless — until the next one lands.

## Definition / Mechanism

Bekit, Karim, Nguyen & Yilmaz (2026) run a video
anomaly detector (QVAD) that lets an LLM agent ask a vision-language model
up to two rounds of follow-up questions when its own stated anomaly
probability stays below a fixed threshold, each question conditioned on
the ambiguity the agent names in its own prior-turn reasoning. Held fixed
across datasets — same model, same threshold, same two-turn cap — the
*shape* of the accuracy-vs-turns curve still depends on the target: for
visually salient anomalies (explosions, fighting) one question already
resolves the case and a second buys almost nothing; for a subtle,
long-duration anomaly the first follow-up question changes accuracy not
at all, and the payoff arrives only at the second.[^c1]

The same ablation frames this as the paper's central claim for its
agentic loop — that iterated questioning strictly helps over a static,
single-shot prompt — while noting the *size* of that help is set by how
hard the target is, not by the mechanism.[^c2]

## Why it matters

Most turn-budget results in this wiki (e.g.
[[multi-turn-clarification-plateau]]) report a *monotonic-then-flat* or
*monotonic-then-degrading* curve averaged over a task mix. This is a
different shape at the level of one target: a flat run of turns that show
no visible progress, followed by a jump, on the harder instances only.
Averaging over easy and hard targets together — the usual way a turn
budget gets tuned — would report the flat run as evidence the extra
question is worthless, when it is evidence the question before the payoff
was necessary but not sufficient on its own. A stopping rule read off
early-turn deltas on an easy-target benchmark and then reused as a
uniform budget will systematically under-question the hard case, because
the curve gives no signal to reward continuing until the turn that pays
off.

## Limits

Two datasets, two points of comparison ("salient" vs. "subtle"), and a
turn cap fixed at 2 by the authors' own design choice, so it is
unverified whether a subtle-target curve keeps rising past turn 2 or
plateaus there too. "Salient" and "subtle" are also confounded with
dataset identity (multi-scene surveillance footage vs. a single-scene,
open-set benchmark), not manipulated independently, so the paper cannot
rule out that some other property of ComplexVAD, not anomaly subtlety
per se, produces the delayed jump. No statistical test is reported on
the turn-by-turn AUC differences.

## Related

- [[multi-turn-clarification-plateau]] — the opposite-shaped curve
  (returns fall off, not delay) from averaging turns over a task mix.
- [[clarification-timing-decay]] — turn position also matters there, but
  as a monotonic decay of value, not a flat-then-jump curve.
- [[expected-information-gain]] — the quantity a per-turn stopping
  threshold like QVAD's is a cheap proxy for.

[^c1]: arxiv-2604-03040 — "For XD-Violence, the gains are marginal, suggesting a “saturation effect”. The anomalies in this domain (e.g., explosions, fighting) are visually salient, allowing the VLM to resolve them with minimal reasoning depth. In stark contrast, in ComplexVAD a non-linear performance jump is observed. Accuracy remains stagnant at Turn 1 but surges dramatically at Turn 2 (from ≈50% to 68% AUC). This indicates that for subtle, long-term anomalies, a single exploratory question is insufficient; the agent requires a multistep deductive chain to formulate a precise hypothesis that isolates the irregularity."
[^c2]: arxiv-2604-03040 — "We observe a clear performance progression from the static baseline (Turn 0) to the refined state (Turn 2), though the magnitude of improvement is contingent on the anomaly’s complexity."
