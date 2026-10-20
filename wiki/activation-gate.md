---
description: "A threshold-and-priority mechanism that decides which standing commitment surfaces now, then selects among act, ask, wait, monitor, defer, escalate or refrain by expected value under policy."
aliases: ["activation gate", "activation problem"]
sources: ["ferreira-2026"]
---
# Activation gate

> Before an agent can choose *what* to do it must decide *whether this
> moment calls for a decision at all* — a two-stage gate that first tests
> readiness against a moving threshold, then prices "ask" against action,
> waiting and refusal in the same currency.

## Definition / Mechanism

Ferreira (2026) formalizes the **activation problem** —
whether, when and in what mode an agent should behave at all — as a gate on
each standing commitment. Readiness $\lambda_{i,t}$ for commitment $i$ must
clear a context-sensitive bar $\vartheta_t$, set from appraised urgency,
harm, action risk, social sensitivity, interruption cost, permission
proximity and uncertainty: the bar "tightens with sensitivity, permission
proximity, interruption cost, action risk and uncertainty and relaxes under
urgency and potential harm, reflecting emergency override."[^c1]

Only commitments that clear the bar are eligible; a priority competition
then picks one winner, "the intention with the strongest weighted
activation," and opens a behavioral episode for it — a quieter commitment
that is timely is not blocked by a louder one that is not yet.[^c2]

Behavior is then selected from the permitted candidates of the winning
commitment plus a standing restraint set, by maximizing expected situated
value: $b^*_t=\{act, ask, wait, remember, summarize, escalate, delegate,
monitor, defer, inhibit, no\text{-}op,\dots\}$; "ask" competes in the same
selection as acting rather than being a fallback.[^c3]

Among permitted, adequate candidates the mechanism prefers the smaller
footprint — asking a narrower question or waiting beats acting once both
satisfy the commitment, making "doing more than warranted" a scored loss
rather than diligence.[^c4]

Choosing nothing is itself a selected, recorded behavior under the same
clearing condition, distinguishing deliberate restraint from default
silence in the agent's own history.[^c5]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Agent architecture (Ferreira 2026) | activation gate | exact — the formal mechanism (readiness, threshold, priority, selection) |
| Agent architecture (Ferreira 2026) | activation problem | close — the named problem the gate is proposed to resolve; broader than the mechanism itself |

## Why it matters

For stall 2 (which axis first), this gate is a two-level answer: readiness
and threshold decide *whether anything is timely at all*, and only then
does value-maximizing selection choose among asking, acting, waiting or
refraining for the commitment that won. It makes "ask nothing right now"
a first-class, auditable outcome rather than an absence of output.

## Transfer

| | |
|---|---|
| **In its home field** | Appraisal theory (Scherer) and affective computing (Picard) model human/agent emotion as arising from checks on novelty, goal relevance, coping potential and norm compatibility |
| **Here** | Those checks become gate-relevant components (urgency, action risk, social/emotional sensitivity, uncertainty) that raise or lower the threshold an agent's readiness must clear before it acts or asks |
| **What survives** | The structural mapping — urgency/harm to goal relevance, action risk to coping potential, social sensitivity to norm compatibility, uncertainty to novelty — as approximate analogues, per Ferreira's own comparison |
| **What does not** | Interruption cost and permission proximity have no counterpart in individual human appraisal theory; both presuppose a principal whose attention or authority boundary is at stake, so they apply only under delegation, not to the general case |

[^c6]

## Limits

This is a conceptual and formal framework: the paper "reports no empirical
results and claims no single implementation," so the threshold-relaxation
heuristics (urgency lowers the bar, sensitivity raises it) and the
smaller-footprint preference are stipulated design requirements, not
findings verified on a running system. The claim that "ask" belongs among
the gate's candidate behaviors rests on this framework's own taxonomy, not
on an optimality result comparable to [[value-of-information]]'s
would-the-answer-change-the-action test.

## Related

[[intervention-advantage]] · [[value-of-information]] · [[bounded-rationality]]

[^c1]: ferreira-2026 — "In general ϑt tightens with sensitivity, permission proximity, interruption cost, action risk and uncertainty and relaxes under urgency and potential harm, reflecting emergency override."
[^c2]: ferreira-2026 — "Priority then runs the competition among the eligible commitments. It compares their activation levels, weighted by their priorities pi and read in the light of the appraisal and returns the intention with the strongest weighted activation, the one the situation calls for most"
[^c3]: ferreira-2026 — "b∗t ∈ {act, ask, wait, remember, summarize, escalate, delegate, monitor, defer, inhibit, no-op, . . .}."
[^c4]: ferreira-2026
[^c5]: ferreira-2026
[^c6]: ferreira-2026 — "What has no counterpart is whose cost and whose boundary they weigh. Nevertheless, for the current work they are needed, because the appraiser here is an agent acting for someone else, under someone else’s authority."
