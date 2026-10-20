---
description: "The cost of a decision lies not in being wrong but in being ```text TYPE 1 (one-way door) irreversible → decide slowly, ask many questions TYPE 2 (two-way door) reversible → decide fast,"
aliases: ["one-way door", "two-way door", "type 1 decision", "type 2 decision"]
sources: ["bezos-2015", "arrow-1974", "henry-1974", "dixit-1994"]
---
# Reversibility — two kinds of door

> The cost of a decision lies not in being wrong but in being
> **irreversible**.

## The distinction

```text[^s1][^s2][^s3][^s4]
TYPE 1 (one-way door)   irreversible  →  decide slowly, ask many questions
TYPE 2 (two-way door)   reversible    →  decide fast, learn by trying
```

The taxonomy has a named origin: Bezos's 2015 letter to Amazon shareholders
calls Type 1 decisions "consequential and irreversible or nearly
irreversible — one-way doors" that "must be made methodically, carefully,
slowly, with great deliberation and consultation", and Type 2 decisions
"changeable, reversible — they're two-way doors", which "can and should be
made quickly" by individuals or small groups. The failure mode it names —
large organisations running the heavy-weight Type 1 process on Type 2
decisions, yielding "slowness, unthoughtful risk aversion, failure to
experiment sufficiently" — is asserted from one firm's experience, not
measured.

## Why it matters — how to allocate the question budget

This is the criterion for deciding **where** the 10,000 questions go:

```text
Irreversible decision  →  high VoI  →  many questions, escalate to user if needed
Reversible decision    →  low VoI   →  delegate: let the agent choose, fix later
```

This wiki's reading: reversibility is the criterion for **who** answers, and
it adds a dimension to any typology of settled and open questions. Bezos's
letter is about who inside a company decides; that the same cut also decides
whether an agent may answer for itself or must escalate to the user is an
inference of this wiki, not a claim of the source.

## Theoretical placement

Arrow & Fisher (1974) and Henry (1974) established, in two-period models
with uncertain future benefits and the possibility of learning between the
periods, an **irreversibility effect**: an irreversible act carries an extra
cost — Arrow & Fisher's *quasi-option value*, the value of the information
that acting forecloses — so the optimal current level of the irreversible
act is lower than the level computed by ignoring the chance to learn. Dixit & Pindyck (1994) is the standard continuous-time treatment, under which the
option value of waiting, and hence the threshold that triggers the
irreversible act, rises with the volatility of the state.

The direction that transfers: buy time on type 1, spend it on questions;
close type 2 fast. Deciding type 2 questions quickly is **optimal in the
real-options model**; here the analogy supports only the direction — delay
pays more when the act is irreversible and uncertainty is high — not the
optimality claim, which is proved under a model this note does not supply
(see `## Transfer`).

This also connects to the choice of $D$ in [[rate-distortion-theory]]: in
reversible areas $D$ can be kept high.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Management practice (Amazon) | one-way door / two-way door | exact — Bezos's own terms for the two categories |
| Management practice (Amazon) | Type 1 decision / Type 2 decision | exact — the same cut, named by type in the same letter |
| Financial economics | option value of waiting | **close, not this concept** — a number computed under a stated stochastic process, payoff and numeraire (Dixit & Pindyck 1994), not a two-category classification of decisions; the quantity is what a reversible decision is worth, the concept here is which bin a decision falls in |
| Environmental economics | irreversibility effect / quasi-option value | close — the same asymmetry as a result about optimal levels (Arrow & Fisher 1974; Henry 1974), not as a taxonomy |

## Transfer

| | |
|---|---|
| **In its home field** | Irreversible capital investment under a stochastic state or price process, with a payoff function, a discount rate, and learning over time (Arrow & Fisher 1974; Henry 1974; Dixit & Pindyck 1994). |
| **Here** | A design or agent decision whose undoing has a cost, and a [[question-budgets|question budget]] to spend before committing. |
| **What survives** | The qualitative asymmetry: delay has positive value when the act is irreversible and uncertainty is high, and none when it is not — so close type-2 questions fast and buy time on type-1 ones. |
| **What does not** | The option-value formula and its optimality result. They need a stochastic model of the state, a payoff, and a numeraire in which delay and error are commensurable; a natural-language design decision supplies none of the three, so "optimal" does not travel — only "in this direction". |

## Limits

- The door metaphor is management practice with a named origin
  (bezos-2015), not a result; no measured effect supports it.
- The quasi-option results hold under their stated conditions — a specified
  state process, learning between decision points, a benefit function
  (linear or all-or-nothing in the classic proofs), and a common numeraire.
  Applying them to design decisions is by analogy, and the analogy carries
  the sign, not the magnitude.
- **Irreversibility is not stakes.** The mapping irreversible → high VoI
  holds only when the loss from a wrong irreversible choice is large; a
  cheap-but-permanent decision has low VoI, so reversibility ranks questions
  only after the loss scale is fixed ([[value-of-information]]).
- Reversibility is often unknown in advance — the decision about
  reversibility is itself a question.

## Related

[[value-of-information]] · [[rate-distortion-theory]] · [[bounded-rationality]] · [[constraint-as-information]]

[^s1]: bezos-2015
[^s2]: arrow-1974
[^s3]: henry-1974
[^s4]: dixit-1994
