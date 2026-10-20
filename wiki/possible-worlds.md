---
description: "Uncertainty counted rather than measured: how many ways things could still ```text ``` Certainty is not a property of the event but of the observer: what makes an uncertain event certain is **infor…"
aliases: ["support of a distribution", "hypothesis space", "state space", "modal worlds"]
sources: ["shannon-1948", "cover-2006", "kripke-1963", "mitchell-1982"]
---
# Possible worlds

> Uncertainty counted rather than measured: how many ways things could still
> be.

## The statement

```text[^s1][^s2][^s3][^s4]
|possible worlds| > 1   →  uncertain
|possible worlds| = 1   →  certain
```

Certainty is not a property of the event but of the observer: what makes an
uncertain event certain is **information**, in whatever form it arrives.

## The counterpart in theory

The count bounds the measure, and only in one direction. For a random variable
on a **finite discrete** support, Shannon (1948) established — and Cover & Thomas (2006) restate as the standard form — that

$$H(X) \leq \log_2 \lvert\text{support}\rvert$$

with equality only for a uniform distribution. So $\log_2\lvert W\rvert$ is an
**upper bound** on the uncertainty, never an estimate of it. Counting is
therefore admissible in exactly one direction: a small count guarantees little
uncertainty; a large count guarantees nothing, because the mass may sit on one
world. The worked comparison of a count against its entropy is in [[entropy]]
§ *Relation to certainty* and is not repeated here.

## Practical consequence

"How many questions remain" is answered not by the number of open axes but by
the **weight** of what stays open. If 45 of 50 open axes are all but settled,
the real work sits in 5 axes. When the open axes are independent that weight is
the sum of their entropies; in general it is the joint entropy of the surviving
$W$, and the sum is an upper bound only (see Limits).

This is why progressing by counting gaps misleads: gap count is the wrong
metric, gap weight is the right one.

## Where certainty comes from

| Source | Theory |
|---|---|
| Observation | Bayesian update ([[bayesian-estimation]]) |
| Inference | Conditioning ([[conditional-entropy]]) |
| Commitment | Adding a constraint ([[constraint-as-information]]) |

All three do the same job: narrow the support, lower the entropy. Inference is
the odd one — nothing is observed, yet worlds disappear, because they were
already excluded by what was held. That is this note's row on stall 4: a
constraint's provenance differs, its effect on $W$ does not.

## Known as

| Field | Name there | exact / close | Why |
|---|---|---|---|
| Probability | support of a distribution | close | a support presupposes a measure carried on it; $W$ here is given without one, so the two coincide only once a distribution is imposed |
| Machine learning | hypothesis space | close | Mitchell's $H$ is declared in advance and stays fixed; what shrinks under answers is the version space, not $H$ ([[version-space]], mitchell-1982) |
| Control / dynamics | state space | close | the same enumeration of ways-things-could-be, but indexed by time and equipped with a transition map that $W$ has no counterpart for |
| Modal logic | modal worlds | close | the picture only. A Kripke model is a frame plus a valuation — worlds *and* an accessibility relation (kripke-1963). This note keeps the worlds and drops the relation, so nothing modal is inherited with the name |

## Transfer

| | Modal logic | Information theory |
|---|---|---|
| Home field | a frame: a set of worlds with an accessibility relation, plus a valuation; necessity and possibility are defined through that relation (kripke-1963) | a probability distribution on a finite discrete support; entropy and its bound $\log_2$ of the support size (shannon-1948, cover-2006) |
| Here | the asker's open world-set $W$: unenumerated, no relation between worlds asserted, no measure given | the size of $W$ read as a ceiling on how much asking is still owed |
| What survives | the counting picture, and with it the terminal condition "one world left" as the definition of *answered* | the inequality's direction — the count over-states uncertainty, so it is usable as a bound and never as a measure |
| What does not | the accessibility relation and everything defined through it: necessity, possibility, modal validity, and the frame conditions that separate one modal system from another | the bound itself, once the support is not finite or not enumerable — the asker's normal case; and any numerical entropy, since no distribution over $W$ is given |

## Limits

- Counting needs the worlds **enumerated**. The enumeration is the hard part
  ([[unknown-unknowns]]).
- "One world left $\Rightarrow$ certain" assumes the true world is inside $W$.
- The bound holds for a **finite discrete** support. On a continuous or
  open-ended $W$ it says nothing — and that is the state the asker starts in.
- The summed-entropy reading of "work remaining" assumes the open axes are
  **independent**. Entropy is subadditive — the joint entropy of several
  variables is at most the sum of their individual entropies, with equality
  only under independence (cover-2006) — so wherever axes are correlated, the
  common case, the sum overstates the remaining work. The quantity that is
  correct without that assumption is the joint entropy of the surviving $W$.
- `kripke-1963` was located provisionally here (PhilPapers / the *JSL* review
  of the Helsinki colloquium proceedings) and is unconfirmed until the
  verifier passes it; `shannon-1948` and `cover-2006` carry
  `verified: prior` — inherited, not re-checked in this revision.

## Related

[[entropy]] · [[version-space]] · [[constraint-as-information]] · [[typical-set]] · [[maximum-entropy-principle]] · [[unknown-unknowns]]

[^s1]: shannon-1948
[^s2]: cover-2006
[^s3]: kripke-1963
[^s4]: mitchell-1982
