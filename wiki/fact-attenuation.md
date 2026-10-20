---
description: "A policy-relevant fact discovered by one agent component is progressively dropped from the summary handed to the next, and the drop rate rises with how many component boundaries the fact must cross."
aliases: ["fact attenuation", "attenuation at the handoff boundary"]
sources: ["li-2026-governance"]
---
# Fact attenuation

> Decomposing one agent loop into a pipeline or an orchestrator-subagent
> topology does not change what facts a component discovers; it changes
> whether those facts survive the handoff to the component that must act
> on them.

## Definition / Mechanism

Li & Wang (2026) define constraint distance as the
number of component boundaries a policy-triggering fact must cross between
the tool call that discovers it and the action it obliges or forbids, and
fact attenuation as that fact being present in the tokens generated at
discovery but absent from every subsequent handoff on the path to the
acting component: "Policy-relevant facts discovered by one component are
attenuated at the handoff boundary before reaching the component that must
act on them."[^c1]

Across 626 episodes on 100 KYC/AML task variants, three architectures
sharing identical tools and policy text were compared at constraint
distance 2: a single ReAct loop (0 boundaries), a fixed intake-research-decide
pipeline (2 boundaries), and an orchestrator with scoped subagents (2
boundaries, but each round-trip re-summarizes). On a 32B open-weights
model, "D1 drops 56% of discovered facts at distance 2 and D2 drops 85%,"
while gpt-4.1-mini attenuates only 3% and 6% under the same conditions,
with the ordering single-loop < pipeline < orchestrator preserved across
both models.[^c2]

The mechanism is direction-agnostic: on a paired pair of mirror tasks, the
same summarization loss suppresses a risk signal on one task and an
exculpating finding on the other — "the same mechanism produces both
under-escalation and over-escalation, depending on whether the dropped
fact was a risk signal or an exculpating one."[^c3]

A further asymmetry: the orchestrator elicits more trigger facts than the
single loop (its delegation prompts ask more targeted questions) but then
loses most of what it elicits — "D2 then attenuates 22 of those 27 facts
(81%), while D0 attenuates none. The architecture that is better at
finding policy-relevant information is worse at carrying it."[^c4]

## Why it matters

This is a measured cause of an agent's escalation decision that has
nothing to do with the agent's uncertainty, competence, or stopping rule:
the fact needed to trigger an obligatory question or escalation is
discovered correctly and then lost in a handoff summary before the
component that would act on it ever sees it. Architecture choice — not
policy access mode (in-context vs. retrieval-on-demand showed no
systematic difference) — is what drives the effect.[^c5]

## Limits

The result rests on one benchmark domain (KYC/AML compliance), two models
(a 32B open-weights model and gpt-4.1-mini), and a scripted substring
verifier that the authors themselves note "measures phrasing alongside
governance." Governed success on the single-loop baseline was itself only
8/596 episodes (1.3%), so the attenuation signal is read off a weak
anchor. The authors state they have not shown the effect holds at
frontier-model scale, generalizes beyond KYC/AML, or survives better
handoff prompting — this note's claim is bounded to what the paper
measured, not a general law of decomposition. `li-2026-governance` is a
2026 arXiv preprint, not yet peer-reviewed.

## Related

[[bayesian-self-escalation]] · [[collective-uncertainty]]

[^c1]: li-2026-governance — "Policy-relevant facts discovered by one component are attenuated at the handoff boundary before reaching the component that must act on them."
[^c2]: li-2026-governance — "On Qwen2.5-32B, D1 drops 56% of discovered facts at distance 2 and D2 drops 85%. On gpt-4.1-mini the rates fall to 3% and 6%, but the ordering is preserved."
[^c3]: li-2026-governance — "the same mechanism produces both under-escalation and over-escalation, depending on whether the dropped fact was a risk signal or an exculpating one"
[^c4]: li-2026-governance — "D2 then attenuates 22 of those 27 facts (81%), while D0 attenuates none. The architecture that is better at finding policy-relevant information is worse at carrying it."
[^c5]: li-2026-governance — "No systematic difference appeared. Decomposition, not policy access mode, drives the effect."
