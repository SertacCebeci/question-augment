---
description: "An LLM-judge scorer that estimates agent-trajectory confidence from the fraction of resampled trajectories judged outcome-equivalent to the reference, not from lexical or action match."
aliases: ["TER", "trajectory equivalence rate"]
sources: ["bouchard-2026"]
---
# Trajectory equivalence rate (TER)

> A black-box confidence score for an agent trajectory: resample the
> trajectory, ask an LLM judge whether each resample reaches the same
> task-relevant outcome as the reference, and score by how often it
> agrees — outcome equivalence, not text or action match, and not
> correctness.

## Definition / Mechanism

Bouchard and Chauhan (2026) define TER for a reference trajectory $F$ and
$m$ resampled trajectories $\tilde F$: "a separate LLM judge $J$ reads two
full trajectories and decides whether they reach the same task-relevant
outcome. To avoid information leakage, the trajectory-equivalence judge is
shown only the trajectory transcripts and never observes the hidden task
instructions or the reward. Importantly, the judge assesses outcome
equivalence rather than correctness, so TER remains a consistency measure
rather than an explicit LLM-as-a-judge correctness score."[^c1]

"This scorer measures the fraction of resampled trajectories the judge
deems outcome-equivalent to the reference trajectory."[^c2]

Across the paper's benchmarks, TER and the symbolic action-set-consistency
scorer most often occupy the top ranks among black-box consistency
variants: TER reaches 0.868 AUROC (Qwen3.5-9B, airline) but falls to 0.342
on gpt-4o-mini/telecom, "where the 11% success rate leaves the judge
comparing mostly failure-failure pairs."[^c3]

## Why it matters

TER is a concrete, deployable way to price an agent's confidence in its
own completed trajectory (stall 7, stopping) without a ground-truth label:
resample, judge outcome-equivalence, and use the agreement rate as the
stop/continue or answer/ask signal. It generalises single-turn semantic
equivalence clustering ([[semantic-entropy]]) from *what an answer means*
to *what a whole action sequence achieved*, replacing bidirectional NLI
entailment with an LLM judge's task-outcome equivalence call.

## Transfer

| | |
|---|---|
| **Home field** | single-turn semantic-equivalence clustering (bidirectional NLI entailment over paraphrased answers, as in [[semantic-entropy]]) |
| **Here** | equivalence over whole multi-turn agent trajectories, judged by an LLM on outcome rather than entailment |
| **What survives** | the resample-then-cluster-by-equivalence structure, and its role as a confidence proxy uncorrelated with lexical form |
| **What does not** | the entailment model's tractable binary relation — TER needs a general-purpose LLM judge, not an NLI classifier, and its [[calibration|reliability]] degrades when the success base rate is low enough that most sampled pairs are same-class by chance (failure-failure agreement inflating apparent consistency) |

## Limits

- Evaluated with one judge model (gemini-flash-lite) on four benchmarks;
  judge quality and prompt design are unverified variables the paper does
  not ablate.
- Confidence drops sharply at low success base rates (0.342 AUROC at an
  11% success rate) because the judge then compares mostly failure
  pairs, which look equivalent regardless of trajectory quality.
- Requires sampling $m$ additional full trajectories plus a judge call per
  pair, a cost this wiki cannot assume is available at the moment a
  stopping decision must be made.
- The relation to [[semantic-entropy]] is an analogy this wiki draws
  (same resample-and-cluster structure, different equivalence relation
  and unit of analysis) — the source paper does not claim the connection.

## Related

[[trajectory-uncertainty-quantification]] · [[semantic-entropy]] · [[sprt]]

[^c1]: bouchard-2026 — "a separate LLM judge J reads two full trajectories and decides whether they reach the same task-relevant outcome. To avoid information leakage, the trajectory-equivalence judge is shown only the trajectory transcripts and never observes the hidden task instructions or the reward. Importantly, the judge assesses outcome equivalence rather than correctness, so TER remains a consistency measure rather than an explicit LLM-as-a-judge correctness score."
[^c2]: bouchard-2026
[^c3]: bouchard-2026 — "TER reaching 0.868 for Qwen3.5-9B"
