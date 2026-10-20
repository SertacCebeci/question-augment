---
description: "When several agents share one user, which of them may interrupt them — and In a compound system the agent that notices the uncertainty and the agent that talks to the user may differ. Uncoordinated,"
aliases: ["MAC", "multi-agent clarification"]
sources: ["acikgoz-2026"]
---
# Multi-agent clarification

> When several agents share one user, which of them may interrupt them — and
> the measured answer is not "exactly one".

## Problem

In a compound system the agent that notices the uncertainty and the agent[^s1]
that talks to the user may differ. Uncoordinated, two failure modes: several
agents ask the same thing (the user is overwhelmed), or each assumes another
will ask (nobody asks).

## Mechanism

MAC (Acikgoz et al., IWSDS 2026) is a supervisor/expert hierarchy over the
five MultiWOZ domains. Per user turn $u_t$:

1. The supervisor computes `is_ambiguous`($u_t$). If true it emits
   `<clarify>question</clarify>` to the user and the turn **ends** — routing
   does not happen, so no expert is running to duplicate the question.
2. Otherwise it emits `<route>domain</route>` and hands the (possibly already
   clarified) request to that domain expert.
3. The expert re-tests [[efe-planning-as-variational-inference|ambiguity]] against its own API schema and database, and
   emits either `<clarify>` or `<response>`.
4. **One clarification reaches the user per turn**, as a latency bound; an
   expert may come back on later turns until the dialogue passes 20 turns.

Duplication is prevented not by a queue but by **disjoint scopes**: their
taxonomy gives the supervisor seven domain-agnostic [[ambiguity-taxonomy|ambiguity types]] (domain,
intent, vague goal, contextual disambiguation, conflict, noise, unfamiliar
domain) and the expert five domain-specific ones (slot underspecification,
value vagueness, constraint conflict, entity not found, confirmation of an
inferred value). The supervisor has no database access, so a slot-level
question is not formulable there. A specialist does not "wait while queued" —
control has not reached it.

## Findings

MultiWOZ 2.4 test split (1,000 dialogues, five domains), `gpt-4o-2024-08-06`
as every node and as the user simulator, five runs:

| Who may clarify | Success max@5 | Success avg@5 | Avg. turns |
|---|---|---|---|
| neither | 54.5 | 53.72 ± 0.92 | 6.53 |
| experts only | 55.6 | 54.88 ± 1.04 | 5.53 |
| supervisor only | 57.1 | 55.50 ± 1.86 | 5.11 |
| both | 62.3 | 58.40 ± 2.10 | 4.86 |

Clarification raises success **and shortens** the dialogue (+7.8 points
max@5, 6.53 → 4.86 turns). Ablating the supervisor's ambiguity/vagueness
handling costs 6.20 points; ablating the expert's slot-blocking clarification
costs 2.18. Both levels are load-bearing: concentrating the right to ask at
either single point is measurably worse than splitting it by scope.

## Why it matters

The Router box in [[compound-ai-systems]] is therefore not the sole asker.
What it owns is the **outlet** — one clarification per turn — and the scope
partition that decides whose question it is. The user budget of
[[question-budgets]] is the shared resource, and the per-turn rate limit is
what shares it; where the authority sits follows what each level can see, not
a principle of centralisation.

This wiki infers, and does not measure: once the outlet is one question per
turn and more than one level may fill it, an ordering is needed, and MAC
settles it by role. Settling it by content — [[value-of-information]] against
the shared budget — predicts a failure mode MAC does not test: a
supervisor-level question pre-empting a higher-value expert question in the
same turn, which should show up as success gains that saturate as the
supervisor's taxonomy is widened.

## Known as

| Field | Name there | Match |
|---|---|---|
| AI systems (dialogue) | multi-agent clarification | exact |
| AI systems (dialogue) | MAC | close — MAC is Acikgoz et al.'s specific supervisor/expert instance; this note is the arrangement of ask-authority it instantiates |

## Transfer

| | |
|---|---|
| In decision theory | [[value-of-information]] ranks candidate observations by [[expected-utility|expected utility]] gain net of cost, for one decision-maker with one utility function |
| Here | the router would rank the clarifications competing for the single per-turn slot, across specialists |
| What survives | the necessity of an ordering — the slot is scarce and the budget is shared, so some comparison must happen |
| What does not | the common utility scale. Questions from different MultiWOZ domains have no shared utility in MAC; its arbitration is by taxonomy and role, and no VoI ranking is computed or measured anywhere in the source |

## Limits

- One benchmark (MultiWOZ 2.4), task-oriented dialogue, and the "user" is a
  `gpt-4o` simulator pursuing a fixed goal — the cost of an interruption is
  not measured on a person.
- The mechanism assumes **one principal whose attention is a single shared
  budget**, and that the level holding the authority can see enough to phrase
  its own question. MAC satisfies the second by *not* centralising phrasing.
  Where agents serve different principals, or the question is only formulable
  in a specialist's local state, the arrangement degrades: the router can
  forward but not compose, and "one question per turn" becomes a bound per
  principal, not per system.
- Turn counts are taken under a 20-turn cap; no latency or user-effort
  measure is reported.
- The VoI ordering in *Why it matters* is this wiki's conjecture, not the
  source's finding.

## Related

[[compound-ai-systems]] · [[question-budgets]] · [[value-of-information]] · [[elicitation-protocols]] · [[clarification-request]]

[^s1]: acikgoz-2026
