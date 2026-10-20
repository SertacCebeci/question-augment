---
description: "Single-turn LLM confidence-scoring families transfer to multi-turn agent trajectories unevenly — no family is uniformly reliable across models and domains."
aliases: ["trajectory-adapted UQ", "agent trajectory uncertainty quantification", "trajectory-level confidence scoring"]
sources: ["bouchard-2026"]
---
# Trajectory-level uncertainty quantification

> Whether the three standard families of LLM confidence scoring — token
> probability, resampled self-consistency, and self-reported reflexive
> confidence — still separate success from failure once the scored unit is
> a whole multi-turn agent trajectory rather than one generation.

## Definition / Mechanism

Bouchard and Chauhan (2026) evaluate three single-turn uncertainty-quantification (UQ) families, adapted to score a whole tool-using agent trajectory $F$ rather than one generation, across five LLMs and four multi-turn tool-use datasets (BFCL-v4 and three τ²-bench domains). White-box scorers aggregate per-turn token-probability statistics (sequence probability, length-normalized sequence probability, top-K [[entropy]]) across turns using a chosen aggregator (mean, min, first, last). Black-box scorers resample additional trajectories and measure consistency with the reference, either over the final message, over the symbolic action-type sequence, or via an LLM judge of whole-trajectory outcome equivalence. Reflexive scorers ask the model to self-report confidence or a True/False success judgment once, over the trajectory transcript.[^c1]

No family is uniformly reliable: "no single family or scorer is reliable across benchmarks and models, and performance depends on where uncertainty is read, how per-turn signals are aggregated, the domain, and the model being scored."[^c2]

White-box scores are highly sensitive to the aggregator choice: on one τ²-bench cell, switching the aggregation rule for the same base score moves AUROC from a strong point estimate down to 0.228, and "the mean aggregator applied to SP and LNSP, the scorers used in Oh et al. (2026), is approximately at or below chance for every model" on the airline domain.[^c3]

Reflexive scoring — a single extra pass asking the model to judge its own trajectory — is the most consistently competitive low-cost baseline: "Reflexive scores are more robust in aggregate and require only one extra pass over the transcript, making them a strong practical baseline." Black-box self-consistency is frequently the strongest family overall, but requires sampling additional trajectories, and its symbolic-action variants ([[trajectory-equivalence-rate|trajectory-equivalence rate]], action-set consistency) rank above final-message agreement.[^c4]

## Why it matters

This bears on the point where an agent decides whether it has enough
information to commit rather than ask or act further (stall 7,
stopping): the paper shows the confidence signal an agent would use to
make that call is not portable from single-turn LM evaluation by
default. A stopping rule built on raw token-probability confidence
(e.g. treating low sequence probability as a signal to ask a
clarifying question) can be at or below chance in exactly the
aggregation regime that looks natural (mean over turns), while a
one-pass reflexive self-report is often close to the best available
signal at far lower cost than resampling trajectories.

## Transfer

| | |
|---|---|
| **Home field** | single-turn LLM confidence estimation: white-box token-probability scores, black-box resampled self-consistency, reflexive self-report, each validated on one generation with a correctness label |
| **Here** | scoring a whole interactive multi-turn tool-use trajectory for a binary success label |
| **What survives** | the three-family taxonomy itself, and the relative robustness ordering in most tested cells — reflexive as cheap and comparatively stable, black-box consistency (measured over actions/outcome, not final text) often strongest |
| **What does not** | the aggregation-free [[calibration|reliability]] of token-probability scores — turning a per-turn score into a trajectory score introduces an aggregator choice with no validated default, and the paper finds this choice alone can flip a scorer from predictive to anti-correlated on the same model and domain |

## Limits

- Evaluated on four multi-turn tool-use benchmarks (BFCL-v4, τ²-bench
  retail/airline/telecom) and five LLMs; whether the ranking transfers to
  other agent domains (e.g. open-ended clarification dialogue) is untested.
- Confidence intervals are wide (median half-width 0.10 AUROC on columns
  with ≥ 20 minority-class trajectories); several bold "best" cells in the
  paper's main table are not statistically resolved rankings.
- Black-box consistency scores require sampling extra trajectories, which
  this wiki cannot assume is affordable at the point a stopping decision
  must be made cheaply.
- Only greedy-trajectory success is scored (observation uncertainty is
  explicitly out of scope, following Oh et al. 2026), so the result says
  nothing about uncertainty attached to environment observations.

## Related

[[semantic-entropy]] · [[sprt]] · [[value-of-information]]

[^c1]: bouchard-2026 — "We study whether three common families of single-turn UQ methods transfer to this setting. Across five LLMs and four multi-turn tool-use datasets from BFCL-v4 and τ 2 -bench, we evaluate white-box scorers based on action-token probabilities, black-box consistency scorers based on resampled trajectories, and reflexive scorers based on model self-assessment of the trajectory."
[^c2]: bouchard-2026 — "no single family or scorer is reliable across benchmarks and models, and performance depends on where uncertainty is read, how per-turn signals are aggregated, the domain, and the model being scored."
[^c3]: bouchard-2026 — "switching the aggregation for that same base score moves AUROC to 0.228. On airline, the mean aggregator applied to SP and LNSP, the scorers used in Oh et al. (2026), is approximately at or below chance for every model."
[^c4]: bouchard-2026 — "Reflexive scores are more robust in aggregate and require only one extra pass over the transcript, making them a strong practical baseline."
