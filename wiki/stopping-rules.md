---
description: "All four are valid, but they measure different things. No fixed question count; an error tolerance instead. Among all tests with the same two error probabilities,"
aliases: ["stopping condition", "termination criteria for inquiry"]
sources: ["wald-1948", "howard-1966", "shannon-1959"]
---
# Stopping conditions — four different answers

> All four are valid, but they measure different things.

## 1. Threshold-based — [[sprt]]

> Ask until uncertainty is low enough.

No fixed question count; an error tolerance instead. Among all tests with the[^s1][^s2][^s3]
same two error probabilities, the SPRT minimises the expected number of
observations (Wald & Wolfowitz 1948). **The question count is an output, not
a target.**

## 2. Decision-based — [[value-of-information]]

> Stop when no question's answer would change your decision.

Stop when $\max_q \mathrm{VoI}(q) < \mathrm{Cost}(q)$, with VoI the expected
gain in the decision's value from learning the answer (Howard 1966).
Information could still be gained but would be useless.

## 3. Tolerance-based — [[rate-distortion-theory]]

> Stop once you have reached the targeted fidelity.

Collecting $R(D)$ worth of information is enough, where $R(D)$ is the least
rate that meets a declared fidelity criterion $D$ (Shannon 1959). An answer
of "doesn't matter" raises $D$, lowers $R(D)$, and makes stopping early
**correct**.

## 4. Coverage-based — the frontier — [[issue-tree]]

> Continue until the list of unopened branches is empty.

No measurement, only bookkeeping. [[issue-tree]] is the note that carries
this row, and its limit is inherited here: a frontier is complete only over
the taxonomy in force when the tree was drawn. The theoretical counterpart
stated next is **this wiki's own formulation**, not a result from any cited
source — having at least one constraint on **every dimension** of the
[[possible-worlds|hypothesis space]], not an [[entropy]] threshold but a **support-definedness**
condition. The nearest formal relative the wiki holds is [[version-space]],
whose stopping test ($S = G$, one surviving hypothesis) is likewise
structural rather than a threshold and carries the same precondition: the
dimensions must be declared before the first answer.

## Comparison

| | Measures? | Stops early? | Weakness |
|---|---|---|---|
| SPRT | yes | no | weak guarantees for many hypotheses |
| VoI | yes | yes | requires knowing the decision |
| Rate–distortion | yes | yes | who supplies $D$? |
| Frontier | no | no | an untouched axis is invisible |

## Known as

| Field | Name there | exact / close |
|---|---|---|
| sequential analysis, decision theory | stopping condition | exact — the same object: the predicate that ends the sequence |
| research methods | termination criteria for inquiry | close — names a protocol's whole set of end conditions, which may include budget and fatigue as well as the four rules here |

## Transfer

| | |
|---|---|
| In its home fields | SPRT ends a hypothesis test; VoI ends the purchase of evidence before a decision; $R(D)$ is the least rate meeting a fidelity target — each with a declared model, a declared loss, or a declared distortion measure |
| Here | each is read as a rule for ending a question sequence: questions as observations, the surviving answer set as the hypothesis space |
| What survives | the shape of the stopping predicate, and what each demands as input — an error tolerance, a decision with a utility, a fidelity level. Naming that input is the real cost of adopting a row |
| What does not | the optimality. All three hold only relative to a fixed, correctly specified space; none is defined over the unmodelled axis that row 4 exists to catch, so this framework inherits no guarantee from its members |

## Why all four are needed

None suffices alone:

```text
SPRT alone       →  uncertainty on an unmodelled axis cannot be measured; stops early
Frontier alone   →  opens even trivial branches to the end
VoI alone        →  requires knowing the final decision; absent during exploration
```

**Conjecture (this wiki, unmeasured):** a questioner that stops early is
running 1 or 2; one that goes on for thirty rounds is running 4. The failure
of the first kind is **a threshold rule silently measuring zero uncertainty
on an unmodelled axis** — there is nothing there to measure, so it reads as
certainty. No study is cited for either attribution, and none is claimed.

## Limits

- A synthesis made in this wiki (framework); each row inherits the limits of
  its note, and each row's external result is attributed above to its own
  source.
- "None suffices alone" is argued, not proved.
- The **support-definedness** condition in row 4 is this wiki's own
  formulation. No cited source states it, and nothing here proves it
  equivalent to an empty frontier.
- The failure-mode attribution in *Why all four are needed* is
  **unmeasured**: who runs which rule, and which failure follows, is this
  wiki's conjecture and not a frequency claim about real askers. The
  descriptive literature on stopping-rule use in information search is not
  read here and would carve the rules differently.
- No rule here handles a hypothesis space that **changes** during asking —
  every row assumes the axes are fixed.

## Related

[[sprt]] · [[value-of-information]] · [[rate-distortion-theory]] · [[issue-tree]] · [[version-space]] · [[possible-worlds]]

[^s1]: wald-1948
[^s2]: howard-1966
[^s3]: shannon-1959
