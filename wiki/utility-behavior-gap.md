---
description: "Elicited pairwise-choice utility rankings in LLMs predict held-out choices near-perfectly but do not predict which incentive raises generation quality, across 7 models and 4 tasks."
aliases: ["utility-behavior gap", "utility incentive gap"]
sources: ["zhou-2026-when"]
---
# Utility-behavior gap

> A coherent, high-accuracy utility ranking obtained from pairwise preference elicitation does not
> function as an incentive: offering an LLM its own "preferred" outcome as a success-contingent
> consequence does not raise the quality of what it produces, even though the same pipeline detects
> quality shifts from other cues.

## Definition / Mechanism

Zhou & Ackerman fit a Thurstonian utility model to each of 7 instruction-tuned LLMs' pairwise choices
over outcomes in 4 domains (religions, animal species, countries, policies), then use the fitted
ranking to construct matched generation prompts that attach success on a writing task (essay, grant
abstract, incident postmortem, translation) to either a high- or a low-ranked outcome for that same
actor, holding the task, item and judging rubric fixed. Blind LLM judges compare the two artifacts
without seeing the consequence text. The fitted rankings reproduce held-out pairwise choices with a
mean accuracy of 0.944 (min 0.889, max 1.000) across 28 actor-domain cells, confirming the preferences
are coherent.[^c1]
Despite that coherence, none of the 28 actor-task cells shows the high-utility artifact winning above
chance after correction, and the aggregate high-side win rate is 51.2% (95% CI 48.7–53.6) — statistically
indistinguishable from the 50% chance line.[^c2]
The null is not a dead pipeline: on the same tasks and judges, a direct effort exhortation shifts output
quality in 25 of 28 cells (aggregate win rate 76.8%, CI 71.8–81.8), and role-play and harmful-outcome
cues also move judged quality — so the apparatus can detect a real incentive effect when one exists,
and simply does not detect one from the elicited utility.[^c3]
The authors name the dissociation a "utility-behavior gap": a coherent pairwise ranking established by
choice does not imply that the ranked outcome carries generation-time motivational force.[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Preference elicitation / LLM safety (this note) | utility-behavior gap | — |
| Economics (stated-preference / hypothetical-bias literature) | stated–revealed preference gap | analogy — same *shape* (an elicited ranking does not predict the corresponding real-stakes choice), different mechanism and population; not established as the same object here |

## Why it matters

Preference elicitation on this wiki's stall 2 (selection) is used to pick or weight a query by the
answerer's revealed utility (see [[volume-removal]], [[current-solution-strategy]]). This finding is a
caution on the *use* of an elicited ranking once obtained, not on how to elicit it: a ranking that
predicts held-out choices well is not, by itself, evidence that acting on it (e.g. rewarding an agent
with its top-ranked outcome) will change the agent's behavior. Anyone using elicited utility as an
incentive signal for an LLM-based asker or answerer needs an independent behavioral check, not just a
holdout-accuracy check on the elicitation.

## Limits

The claim rests on one experimental paradigm — competition framing, four writing task families, seven
mid-2026 instruction-tuned models via OpenRouter, and LLM judges rather than human raters — and the
authors themselves note the latest frontier models were not tested for cost reasons; a null here is a
null for *this* incentive-delivery mechanism (a success-contingent sentence inside the prompt) and does
not rule out other channels (e.g. reward-model training rather than prompting) transferring utility into
behavior.

## Related

[[volume-removal]] · [[current-solution-strategy]] · [[optimistic-pessimistic-strategy]] · [[expected-utility]]

[^c1]: zhou-2026-when — "Across all cells, the mean held-out accuracy is 0.944, with a minimum of 0.889 and a maximum of 1.000"
[^c2]: zhou-2026-when
[^c3]: zhou-2026-when
[^c4]: zhou-2026-when — "These findings reveal a utility–behavior gap: coherent pairwise rankings do not necessarily imply generation-time incentives, and in fact in the case of these preferences elicited through standard techniques, they affirmatively do not serve as behavioral incentives."
