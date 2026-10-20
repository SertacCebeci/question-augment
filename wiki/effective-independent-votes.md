---
description: "An intraclass-correlation estimate of how many of a multi-vote LLM-judge panel's votes are statistically independent; a 16-vote panel measured at roughly two effective votes."
aliases: ["effective independent votes", "n_eff", "neff"]
sources: ["dooskin-2026", "arxiv-2603-20640", "doi-10-48550-arxiv-2602-09341", "doi-10-48550-arxiv-2609-22512"]
---
# Effective independent votes

> A panel of 16 LLM-judge votes is not 16 pieces of evidence: measured by
> how much they actually vary together, most of that panel is one voter
> repeating itself.

## Definition / Mechanism

Dooskin & Squoosh Technical Staff (2026) compute a
one-way intraclass correlation (ICC) on the binary per-vote calls of a
counterbalanced LLM-judge panel, grouped by test, and convert it to an
effective sample size $n_{\text{eff}}$ — the number of statistically
independent votes the panel's correlation structure is equivalent to:
"One-way ICC on the binary votes grouped by test gives ρ = 0.34–0.51 across
the three judges: a 16-vote panel carries neff ≈ 1.9–2.6 effective
independent votes."[^c1]

The same diagnostic applied to a 15-person human-expert baseline on the
identical task gives the same collapse: "a one-way ICC of ρ = 0.54 implies
neff ≈ 1.8 effective independent experts out of 15 — the same collapse we
measured for LLM panels in §6.3 (neff ≈ 2 of 16 votes)."[^c2]

The paper treats this number as explanatory rather than incidental: it is
offered as the single quantity that "jointly explains why unconditional κ
is flat in panel size, why gated calls reproduce 31/31 across runs..., and
why unanimity must not be read as accumulating evidence."[^c3]

The underlying finding is that panel *agreement* and panel *accuracy* come
apart: judges that differ in model or prompt agree with each other at
κ = 0.74–0.88 while each agrees with ground truth at only ≈ 0.2, and a
held-out cohort's unanimous calls reproduced an earlier run's calls on
31/31 overlapping tests — "perfect test–retest [[calibration|reliability]]" — while scoring
κ = −0.100 against the real outcome: "Unanimity in an LLM panel is one
deterministic prior expressed many times, not independent evidence
accumulating."[^c4]

Diversifying the panel (mixing models or prompts 8+8) does not rescue this:
mixed panels perform within noise of pure panels at the unanimity gate,
"Juries of correlated jurors are still one juror."[^c5]

## Why it matters

This gives a scalar test for a failure mode that otherwise looks like
success: a panel whose votes are reproducible and whose members agree with
each other can still be worthless as a constraint on the world, because the
"votes" are correlated draws from one shared prior rather than independent
observations. Wherever this wiki treats an answerer's repeated or
multi-member response as several constraints — averaging votes, counting
agreement as confirmation — $n_{\text{eff}}$ is the number that says how
many of those responses actually are independent constraints, not how many
were collected.[^c6]

## Transfer

| | |
|---|---|
| Home field | psychometrics: intraclass correlation measures how much of the variance in repeated ratings is between-subject (real signal) versus within-rater noise, for human raters scoring different subjects |
| Here | binary calls from LLM-judge panel members (or human experts) scoring the same test item, converted to $n_{\text{eff}}$ = effective independent voters out of the nominal panel size |
| What survives | the ICC-to-$n_{\text{eff}}$ conversion itself, and the qualitative conclusion — reproducible consensus among correlated raters is not accumulating evidence |
| What does not | ICC's usual between-subjects/within-rater variance decomposition assumes raters are a random sample from a rater population; LLM-judge "panel members" are prompt/sampling variants of one or few underlying models, so the paper reads a low ICC as shared *prior*, not rater noise — a different generative story than psychometrics assumes, untested here against an alternative decomposition |

## Closed form under equicorrelation

For N exchangeable unbiased estimators with common variance and pairwise correlation ρ, the mean has variance σ²/N_eff with N_eff = N/(1+(N−1)ρ); as ρ → 1 variance stays near σ² however large N is.[^c9] This is the analytic counterpart of the ICC estimate above, and a debate paper uses it to motivate keeping only mutually disagreeing agent messages ([[disagreement-retention-in-debate]]).

The same algebra appears in a multi-agent reasoning paper, applied to correctness rather than to judge votes: with $\rho$ the average pairwise correlation of correctness indicators, the variance of the majority count is $p(1-p)[1+(N-1)\rho]/N$, which is $p(1-p)/N_{\text{eff}}$ in this note's notation. That paper uses it to argue that a majority can be wrong while a correct minority exists ([[confabulation-consensus]]); the algebra matches the closed form above.[^c10]

## Error-indicator variant

The same arithmetic can be applied to errors instead of votes. For a calibration item with a trusted label, each judge's error is 1 when its vote differs from that label; the mean pairwise correlation of those error indicators, ρ̄, gives n_eff = n/(1+(n−1)ρ̄) on the same closed form. On a ten-judge open-weight bank evaluated on RewardBench calibration pairs, the mean pairwise error correlation was 0.21, and the work reads it as "the ten judges only provide roughly as much" independent information as about 3.5 judges.[^c11] The variant measures shared mistakes, not shared agreement, and the work states the consequence for unanimity: "Because the same correlation applies to correct votes, even unanimous 10-of-10 agreement contains only 3.51".[^c12] The number is a loss-of-information summary and nothing more: "This value summarizes the loss of independent information; it does not predict" majority-vote accuracy, nor "imply that 3.5 judges could replace the full bank."[^c13] The shape of the shared errors is a separate question, treated in [[shared-error-pattern]].

## Limits

- Reported on three panel configurations (two models, two prompts) on one
  task and one corpus; the ρ = 0.34–0.51 range is this paper's own
  measurement, not a general constant — the paper does not claim panels
  elsewhere will show the same ICC.[^c7]
- The $n_{\text{eff}}$ estimate and the "shared prior, not independent
  evidence" interpretation are presented as EXPLORATORY in the paper's own
  tiering, not CONFIRMED.[^c8]
- The diagnostic requires ground truth on at least a subset of items to
  distinguish agreement from accuracy (§6.3's inter-judge-vs-truth
  comparison); on a domain with no labelled outcomes, $n_{\text{eff}}$ from
  ICC alone would show panel members disagree or agree, not whether either
  pattern tracks truth.

## Related

[[vote-margin-gate]] · [[abstention]] · [[pseudo-ensemble]] · [[calibration]]

[^c1]: dooskin-2026 — "One-way ICC on the binary votes grouped by test gives ρ = 0.34–0.51 across the three judges: a 16-vote panel carries neff ≈ 1.9–2.6 effective independent votes."
[^c2]: dooskin-2026 — "a one-way ICC of ρ = 0.54 implies neff ≈ 1.8 effective independent experts out of 15 — the same collapse we measured for LLM panels in §6.3 (neff ≈ 2 of 16 votes)"
[^c3]: dooskin-2026 — "This single number jointly explains why unconditional κ is flat in panel size, why gated calls reproduce 31/31 across runs (§6.2), and why unanimity must not be read as accumulating evidence."
[^c4]: dooskin-2026 — "Unanimity in an LLM panel is one deterministic prior expressed many times, not independent evidence accumulating."
[^c5]: dooskin-2026 — "Juries of correlated jurors are still one juror [4]."
[^c6]: dooskin-2026 — "measure inter-judge κ against your judges’ agreement with ground truth before attributing meaning to consensus. Consensus among correlated judges is reproducible, persuasive, and — on this task, out of sample — not evidence."
[^c7]: dooskin-2026 — "One-way ICC on the binary votes grouped by test gives ρ = 0.34–0.51 across the three judges"
[^c8]: dooskin-2026 — "The prior crosses models and prompts, measured (EXPLORATORY)"
[^c9]: arxiv-2603-20640 — "denotes the effective number of independent responses that would yield the same variance."
[^c10]: doi-10-48550-arxiv-2602-09341 — "increasing the number of agents alone does not guarantee increasingly reliable majority decisions under persistent positive correlation"
[^c11]: doi-10-48550-arxiv-2609-22512 — "the ten judges only provide roughly as much"
[^c12]: doi-10-48550-arxiv-2609-22512 — "Because the same correlation applies to correct votes, even unanimous 10-of-10 agreement contains only 3.51"
[^c13]: doi-10-48550-arxiv-2609-22512 — "This value summarizes the loss of independent information; it does not predict"
