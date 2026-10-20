---
description: "An embodied agent module that filters implausible physical-interaction candidates and ranks the rest by a VLM-assigned heuristic priority score, in place of a formal information measure."
aliases: ["Prioritizer", "priority score", "VLM-assigned priority score"]
sources: ["lin-2026"]
---
# Priority-scored candidate ranking (the Prioritizer)

> When the candidate axes are physical interactions a robot must actually
> perform (weigh this can, lift that cup), one component of an embodied
> agent — the Prioritizer — decides which one goes first by a VLM-assigned
> heuristic score, not by an information measure.

## Definition / Mechanism

Lin et al. (2026)'s PhysCaP agent splits active perception into
a [[planner-dynamic-stopping|Planner]], which proposes candidate physical-property probes and decides
when to stop, and a Prioritizer, which "filters out implausible or
redundant plans and ranks the remaining candidates by a priority score"
using visual heuristics — e.g. it "may prioritize checking a potentially
ripe avocado (black) over clearly unripe ones (green)."[^c1]

No [[mutual-information|mutual information]], [[entropy]] or submodular objective is computed; the
score is a vision-language model's semantic prior over which candidate is
likely to resolve the task, applied after implausible candidates (a cup too
small to hide the target, a sealed can unlikely to be empty) are dropped
outright.[^c2]

Across three real-robot manipulation tasks and one simulated task, the full
Planner+Prioritizer system reached comparable or higher task success than
passive and naive-interactive baselines "with fewer interactions and
reduced execution time," while a variant with the Planner but without the
Prioritizer's ranking used more interactions and more time on the same
tasks (Table 1: e.g. 4.0 vs 2.5 interactions, 274s vs 239s on the
empty-can task).[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Embodied agents (PhysCaP, Lin et al. 2026) | Prioritizer | exact |
| Embodied agents (PhysCaP, Lin et al. 2026) | priority score / VLM-assigned priority score | exact |

## Why it matters

This is a working instance of stall 2 — which axis first — answered without
any of the field's usual machinery (EIG, adaptive-submodularity, GBS): a
learned semantic prior over candidates, re-applied after each probe. It is
evidence that in an embodied setting where the "axes" are costly physical
actions, a cheap heuristic ranking measurably beats sequential/no-ranking
exploration, even without an optimality proof.

## Limits

- The claim rests on one system, three real-world tasks (10 trials each)
  and one simulated task, all built on the same VLM [[backbone-of-a-formula|backbone]] family
  (Gemini 3.1 Pro, with an appendix claiming portability to others) — no
  independent replication.
- The "priority score" is an unspecified VLM judgement with no [[calibration]]
  or guarantee; it cannot be compared numerically to [[expected-information-gain]]
  or [[adaptive-submodularity]]'s greedy marginal gain — the improvement is
  measured only against ablated variants of the same system (Table 1), not
  against an information-theoretic baseline.
- Candidates are physical interactions proposed by the Planner in a fixed
  JSON list per step; the Prioritizer re-ranks that list, it does not
  generate candidates or model a [[possible-worlds|hypothesis space]] over world-states.
- No formalism is imported here — the mechanism is a heuristic, not a
  theorem — so no `## Transfer` section applies; the contrast with the
  formal selection criteria elsewhere on this stall is exactly the point.

## Related

[[adaptive-submodularity]] · [[value-of-information]] · [[expected-information-gain]] · [[planner-dynamic-stopping]]

[^c1]: lin-2026 — "Using visual heuristics, it filters out implausible or redundant plans and ranks the remaining candidates by a priority score."
[^c2]: lin-2026 — "an effective agent should eliminate infeasible candidates using visual constraints and prioritize only cups that could contain the hidden cube."
[^c3]: lin-2026 — "existing passive and naive interactive baselines either fail when physical properties are hidden or over-explore, whereas PhysCaP achieves comparable performance with fewer interactions and reduced execution time."
