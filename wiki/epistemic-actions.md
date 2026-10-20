---
description: "An epistemic action gathers evidence to resolve a decision-critical unknown without modifying the agent's retained solution, unlike an interventional action that changes it."
aliases: ["epistemic action", "epistemic actions"]
sources: ["fu-2026"]
---
# Epistemic actions

> A gate on whether to probe before acting: gather evidence that would change
> the next move, without touching the solution the agent already holds.

## Definition / Mechanism

Iris, an autonomous ML-engineering agent, partitions the research actions in
its local plan into two disjoint types. Interventional actions construct or
modify a candidate solution and evaluate it; epistemic actions produce
discriminative evidence through analysis or diagnosis, without modifying the
solution currently retained.[^c1]

Each epistemic action centers on a decision-critical unknown: a question
whose possible answers would lead to qualitatively different subsequent
interventions. The agent introduces one when current evidence does not
distinguish among possible next steps, when progress stalls for unclear
reasons, or when an unexpected result must be traced to its source; once
evidence suffices to choose the next intervention, the agent proceeds
directly with interventional actions instead.[^c2]

## Why it matters

This is a trigger for *whether to probe at all before touching the
solution* — a binary gate — rather than a score that ranks candidate
questions the way [[expected-information-gain]] or [[value-of-information]]
do. Once the gate fires, which specific epistemic action to run (exploratory
data analysis, error stratification, feature-interaction probing, and
similar) is left to the agent's own assessment of the gap, with no fixed
taxonomy or scoring rule over the options — the paper reports no formal
selection criterion inside that step.[^c4]

In a controlled ablation (15 MLE-Bench tasks with datasets under 60 MB, one
run each, 6-hour budget), removing epistemic actions and forcing all
information gathering to go through actions that modify or evaluate a
candidate lowered both the above-median rate and the any-medal rate by 6.7
percentage points, while the gold-medal rate stayed at 20.0% — evidence that
probing without committing to a candidate change has a measurable, if
partial, effect distinct from acting more.[^c3]

## Limits

- The trigger condition ("evidence does not distinguish among possible next
  steps") is the agent's own judgement call as prompted, not a formal test:
  no threshold and no scoring function decide it, unlike
  [[value-of-information]]'s zero/non-zero criterion.
- The 6.7-point ablation effect is one configuration — 15 tasks, one run
  each, 6-hour budget, Qwen3.7-Max [[backbone-of-a-formula|backbone]] — inside the full Iris system;
  it is not a controlled study of the trigger rule isolated from Iris's
  other components (adaptive action topology, knowledge revision).
- The interventional/epistemic split is a binary the agent itself proposes
  case by case; nothing in the source bounds how many epistemic actions a
  well-behaved agent should take before probing becomes stalling.

## Related

[[value-of-information]] · [[expected-information-gain]] · [[bounded-rationality]] · [[information-paradigm]]

[^c1]: fu-2026
[^c2]: fu-2026 — "Each epistemic action centers on a decision-critical unknown: a question whose possible answers would lead to qualitatively different subsequent interventions. The agent introduces an epistemic action when the current evidence does not distinguish among possible next steps, when progress stalls for unclear reasons, or when an unexpected result must be traced to its source. When the available evidence is sufficient to choose the next intervention, research proceeds directly with interventional actions."
[^c3]: fu-2026 — "Removing epistemic actions lowers both Med+ and the any-medal rate by 6.7 percentage points, while the gold-medal rate remains at 20.0%. Information is then acquired only through actions that modify or evaluate candidate solutions, preventing Iris from directly investigating decision-critical unknowns before choosing the next intervention."
[^c4]: fu-2026
