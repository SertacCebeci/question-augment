---
description: "EgoAsk picks the next personalized-knowledge gap to ask about by removing gaps memory already answers, then favoring the one tied to current activity, not a value computation."
aliases: ["activity relevance", "D3 selection strategy"]
sources: ["hu-2026"]
---
# Activity-relevance gap selection

> EgoAsk chooses the next personalized-knowledge question not by scoring
> expected information or decision value, but by two cheap filters: is this
> gap already answered in memory, and is it tied to what the user is doing
> right now.

## Definition / Mechanism

For a target object, an LLM-based "knowledge discovery agent" first
enumerates candidate personalized-knowledge needs from the household tasks
the object could support — for each need it "propose[s] 2 hypothetical
answers and explain[s] how each would affect the robot's choice of object or
operation," which fixes what counts as a live candidate before any
selection happens.[^c1]

Candidates are then narrowed in two steps. First, memory-based filtering
removes what is already known: "the system retrieves memory by user and
object identity, and an LLM checks whether the retrieved knowledge answers
each candidate need. If a need is only partially answered, the system
retains the unanswered part. Known needs are excluded, while needs recently
skipped or declined are deferred." Second, among the survivors, "activity
relevance guides which missing information to ask about" — the gap selected
is the one connected to the object interaction the user is performing at
that moment, distinct from "contextualized questioning," which only governs
how the chosen question is phrased.[^c2]

## Why it matters

This is a selection rule for stall 2 that names no value function at all:
it does not rank candidates by expected [[entropy]] drop or by a downstream
decision they would change (contrast [[value-of-information]],
[[expected-information-gain]]). It substitutes two heuristics — "not already
known" and "relevant to what is happening now" — for a value computation,
on the claim that this keeps the answer's context available to the
informant rather than requiring them to reconstruct it later.

## Limits

- Single 2026 arXiv preprint, not independently verified by this wiki [?];
  the selection rule itself is not ablated against an EIG- or VoI-scored
  baseline in the paper, so its advantage over value-based selection is
  this wiki's inference from the design rationale, not a measured
  comparison.
- The rule presupposes the candidate-generation and memory-filtering steps
  already work (accurate object grounding, correct LLM judgement of what
  memory already answers); a failure in either step silently narrows or
  wrongly widens the candidate set before activity relevance is applied.
- Evaluated only in one domain (household object teaching via smart
  glasses) with 18 participants; generality to other axis-selection
  settings is untested here.

## Related

[[value-of-information]] · [[expected-information-gain]] · [[gap-monitoring-burden]] · [[proactive-expertise-clarification]]

[^c1]: hu-2026 — "the prompt asks the agent to propose 2 hypothetical answers and explain how each would affect the robot’s choice of object or operation"
[^c2]: hu-2026 — "the system retrieves memory by user and object identity, and an LLM checks whether the retrieved knowledge answers each candidate need. If a need is only partially answered, the system retains the unanswered part. Known needs are excluded, while needs recently skipped or declined are deferred."
