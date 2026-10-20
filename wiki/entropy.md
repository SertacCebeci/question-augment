---
description: "The average uncertainty of a distribution. The expectation of [[surprisal]]. **Assumptions.** $X$ is a discrete random variable over a **finite** outcome set $\\mathcal{X}$,"
aliases: ["Shannon entropy", "H(X)", "information entropy"]
sources: ["shannon-1948", "cover-2006", "jaynes-1957"]
---
# Entropy

> The average uncertainty of a distribution. The expectation of [[surprisal]].

## Definition

**Assumptions.** $X$ is a discrete random variable over a **finite** outcome[^s1][^s2][^s3]
set $\mathcal{X}$, and the distribution $p$ over $\mathcal{X}$ is **given**.
Base-2 logarithms make the unit the bit.

$$H(X) = -\sum_x p(x)\log_2 p(x) = \mathbb{E}[-\log p(X)]$$

Shannon (1948) defines $H$ and proves the bounds below; he also characterises
it uniquely, up to the constant fixed by the log base, as the only functional
that is continuous in the $p(x)$, increasing in $n$ for the uniform
distribution on $n$ outcomes, and additive when a choice is decomposed into
successive choices. Cover & Thomas (2006) restate all of this in the standard
modern form.

## Core properties

Under the assumptions above:

- $H(X) \geq 0$, with equality iff $X$ is deterministic (all mass on one
  outcome).
- $H(X) \leq \log_2 |\mathcal{X}|$, with equality iff $p$ is uniform.
  **Maximum uncertainty = no option distinguishable from any other.**
- Depends only on the probabilities, not the values. Whether the name is
  "Ahmet" or "Mehmet" does not affect entropy; how many options and how they
  are distributed does.

## Relation to certainty

The weighted version of the $|possible\ worlds|$ count ([[possible-worlds]]):

```text
|worlds| = 1     →  H = 0        certainty
|worlds| = N     →  H ≤ log₂ N   with equality only under a uniform p
```

Arithmetic from the definition: with $N = 1000$ worlds, one holding $0.99$ of
the mass and the remaining $0.01$ spread uniformly over the other 999,
$H \approx 0.18$ bits against a ceiling of $\log_2 1000 \approx 9.97$ bits.
(Put the leftover $0.01$ on a single second world instead and $H \approx 0.081$
bits.) The count is large, the uncertainty is small either way.

*This wiki's inference, not Shannon's theorem:* the count and the measure can
therefore disagree by two orders of magnitude, so an asker who tracks how many
options remain is tracking the wrong quantity — the ordering that matters is by
$H$, not by $|W|$.

## Known as

| Field | Name there | exact / close | Why |
|---|---|---|---|
| Information theory | Shannon entropy | exact | the same functional on the same object — a distribution over a finite alphabet (shannon-1948) |
| Statistical mechanics | Gibbs / Boltzmann entropy | close | Jaynes (1957) identifies the two functionals, but the physical entropy carries $k_B$ and natural logs and is a property of a system's microstates, not of an observer's distribution over answers |
| Everyday / decision practice | "uncertainty" | close | names the same felt quantity, but with no outcome set enumerated and no $p$ declared it is not computed and cannot be ordered |

## Why it matters

*Everything in this section is this wiki's inference, not Shannon's theorem.*

Taking $H$ as the score for an asking episode makes the purpose of a question
the reduction of $H$, and makes the target state of distillation $H \approx 0$
— one world with all the mass. It also predicts that an answer which leaves
the distribution where it was buys nothing, however long it is.

That last step is a **conjecture, not arithmetic**: scoring a particular
free-text answer ("it depends") at zero bits requires an enumerated outcome set
and a calibrated $p$ over it, and a natural-language exchange supplies neither.
[[semantic-entropy]] is one attempt to construct the outcome set (clusters of
answers by mutual entailment) so that such a number exists at all; until a
partition is declared ([[question-as-partition]]) the claim is an ordering
intuition wearing a unit. See [[constraint-as-information]] for what a moving
answer does supply.

## Transfer

| | In its home field | Here |
|---|---|---|
| Observation | one draw from a known discrete distribution over a defined alphabet | one natural-language answer in an exchange |
| $p(x)$ | given by the model, or estimated from a source with known statistics | an estimate nobody calibrated, over an outcome set nobody enumerated |
| What survives | the weighting logic: concentrated mass means low uncertainty whatever the count, and $H = 0$ characterises the finished state | usable as an *ordering* over asking states, and as the definition of what distillation is aiming at |
| What does not | the numeric value, which presupposes a known $p$ over a defined alphabet | no computed bit values for question–answer pairs, and hence no claim that a particular answer is "worth zero" — that needs a partition first ([[question-as-partition]], [[semantic-entropy]]) |

## Limits

- The bounds and the uniqueness characterisation above hold only under the
  stated assumptions: finite $\mathcal{X}$, $p$ given. The asker's normal case
  violates both, so what transfers is the ordering, not the number.
- For continuous variables differential entropy is not invariant under
  reparametrisation and can be negative (cover-2006) — so "lower $H$" is not
  even well posed there without fixing a coordinate system.
- Requires a distribution over a **defined** outcome set. The outcome set is
  exactly what is missing on an unmodelled axis ([[unknown-unknowns]]).
- Measures uncertainty, not importance. A high-entropy axis may change no
  decision ([[value-of-information]]).
- `shannon-1948`, `cover-2006` and `jaynes-1957` carry `verified: prior` in
  `sources.json` — inherited from an earlier pass, not re-checked here.

## Related

[[conditional-entropy]] · [[mutual-information]] · [[maximum-entropy-principle]] · [[possible-worlds]] · [[twenty-questions]] · [[semantic-entropy]]

[^s1]: shannon-1948
[^s2]: cover-2006
[^s3]: jaynes-1957
