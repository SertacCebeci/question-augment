---
description: "Among distributions consistent with the constraints, pick the one that Infinitely many distributions satisfy a given set of constraints."
aliases: ["MaxEnt", "Jaynes' principle", "principle of maximum entropy"]
sources: ["jaynes-1957"]
---
# Maximum entropy principle

> Among distributions consistent with the constraints, pick the one that
> **commits to the least**.

## The principle (Jaynes, 1957)

Infinitely many distributions satisfy a given set of constraints. MaxEnt says:[^s1]
choose the one with highest [[entropy]] — because it is the only one that assumes
**nothing beyond what the constraints force**.

$$p^* = \arg\max_p H(p) \quad \text{s.t.} \quad \mathbb{E}_p[f_i] = c_i$$

## Examples

| Known constraint | MaxEnt distribution |
|---|---|
| Support only | Uniform |
| Mean (positive reals) | Exponential |
| Mean + variance | Gaussian |

## Why it matters — what to assume on an unasked axis

*Conjecture (this wiki, not Jaynes): the unasked-axis norm below is our
reading of MaxEnt, not a result in it. Jaynes gives a rule for assigning a
distribution under stated constraints, not a norm for questioners and not a
diagnosis of model behaviour.*

If a question has not been asked, the questioner should assume **nothing** on
that axis — it should sit at the MaxEnt position.

The natural behaviour of models is the opposite: on an unasked axis they
silently pick the most likely value and move on. That **silent fork** reads,
on this analogy, as a MaxEnt violation.

```text
Correct:  question not asked → axis open, |worlds| wide
Wrong:    question not asked → model silently picked the most likely value
                               but recorded no constraint
```

The second is doubly harmful: the constraint goes unrecorded (inconsistency
surfaces later) and uncertainty appears smaller than it is (no question gets
asked).

## The opposite direction: minimising entropy

MaxEnt is an **inference** principle (what to assume); questioning is an
entropy-reduction process (what to ask). They do not conflict:

- On an unasked axis: MaxEnt — assume nothing
- On an asked axis: reduce entropy — impose a constraint

## Transfer

|  |  |
|---|---|
| **In its home field** | $p$ is a probability measure over a specified sample space; each constraint is a stated expectation $\mathbb{E}_p[f_i] = c_i$ of a measurable function; $H(p)$ has a value and the maximiser is computed. |
| **Here** | The object is the open set of worlds along one unasked axis of $W$ over natural-language descriptions. No support, no measure and no $f_i$ is supplied; an answer closes part of the axis but is not generally expressible as an expectation. "Highest entropy" has no computed value. |
| **What survives** | The qualitative directive — add no constraint the answers did not force — and the silent-fork test it licenses: was a value fixed on this axis without a recorded constraint? |
| **What does not** | The variational solution and its uniqueness, the exponential-family form, and the named distributions in the Examples table above. None is computable over natural-language worlds, so MaxEnt here selects no specific belief state; it only flags unrecorded commitments. |

## Limits

- Constraints must be stated as expectations over a defined support. "Assume
  nothing" still presupposes the support — the axis has to be *known to
  exist*.
- A principle of **inference**, not action: it says what to believe on an
  unasked axis, not whether to ask.
- The unasked-axis reading above is this wiki's conjecture and rests on the
  Transfer table's first two rows: if the axis admits no measure, the claim
  that a silent pick is a "violation" is an analogy, not a derivation.

## Related

[[entropy]] · [[kl-divergence]] · [[constraint-as-information]] · [[possible-worlds]]

[^s1]: jaynes-1957
