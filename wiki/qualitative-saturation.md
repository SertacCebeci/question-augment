---
description: "The one literature that measured \"enough\" by counting what came back rather Glaser & Strauss (1967) named **theoretical saturation**: stop collecting on a category when further data yield no new pr…"
aliases: ["data saturation", "thematic saturation"]
sources: ["braun-2021", "glaser-1967", "guest-2006", "guest-2020", "hennink-2017", "hennink-2022", "malterud-2016"]
---
# Qualitative saturation

> The one literature that measured "enough" by counting what came back rather
> than by thresholding what remains — and found the answer depends entirely on
> what unit you count.

## Definition / Mechanism

Glaser & Strauss (1967) named **theoretical saturation**: stop collecting on a[^s1][^s2][^s3][^s4][^s5][^s6][^s7]
category when further data yield no new properties of it. The stopping
variable is not the analyst's residual uncertainty but the **novelty rate of
returned answers**.

Guest, Namey & Chen (2020) made this computable with three parameters:

| Parameter | Meaning | Their recommendation |
|---|---|---|
| **Base size** $B$ | interviews used to fix the denominator of already-known themes | 4 (they report base size has almost no effect) |
| **[[run-length|Run length]]** $R$ | window of subsequent interviews over which new themes are counted, runs overlapping by one | 2 or 3 |
| **New information threshold** $T$ | new themes in the run as a proportion of base themes | $\le 5\%$, or $0\%$ |

Saturation is reported as $B{+}R$ at $T$. Across their three coded interview
datasets (Tables 2–4), at run length 2 the $\le 5\%$ threshold was crossed at
$6{+}2$, $6{+}2$ and $8\text{–}9{+}2$ interviews, and the $0\%$ threshold at
$11{+}2$, $11{+}2$ and $12{+}2$ — so a stricter threshold roughly doubles the
cost. Validation was retrospective bootstrapping of already-completed
datasets.

Two structural properties follow from the form of the rule:

1. **The stop is a lagging indicator.** You cannot know the run was empty
   without paying for $R$ further questions. Overshoot is not waste; it is the
   measurement.
2. **The stopping point is set by the counting unit.** Hennink, Kaiser & Marconi (2017) coded one dataset twice: **code saturation** — no new codes —
   at 9 interviews; **meaning saturation** — enough to understand each code —
   at 16–24. Same data, same analysts, a factor of two. They gloss the
   difference as "heard it all" versus "understand it all".

Absolute counts across the field: Guest et al. (2006) found saturation within
the first 12 of 60 interviews, with the basic elements of metathemes present
by 6. Hennink & Kaiser's (2022) systematic review of 23 empirical tests puts
the range at 9–17 interviews, or 4–8 focus groups, **for homogeneous
populations with narrow aims**; broader aims or theoretical saturation need
more.

## Known as

This note's object is the operational novelty-rate stopping rule; **data
saturation** and **thematic saturation** name it. The neighbouring names below
are *different objects*, not synonyms — they are listed so the word does not
carry them in silently.

| Name | Relation | What saturates | Source |
|---|---|---|---|
| data saturation, thematic saturation | exact — this note | new themes per run, under $B/R/T$ | guest-2020 |
| theoretical saturation | close — different object, latest to arrive | properties of a category in the emerging theory | glaser-1967 |
| code saturation | close — different object, one unit of the count | the codebook: no new codes appear | hennink-2017 |
| meaning saturation | close — different object, the other unit | the understanding of each code | hennink-2017 |

The evidence that these are different objects is measured, not verbal:
hennink-2017 ran two of them on one dataset and got 9 versus 16–24. The
umbrella word and its four uses are disambiguated in [[saturation]].

## Why it matters

Every other rule on stall 7 thresholds a quantity the asker maintains — a
[[likelihood-ratio|likelihood ratio]] ([[sprt]]), a posterior [[entropy]], a [[value-of-information|value of information]].
Saturation thresholds the **answers' novelty**, which needs no model of $W$,
no prior and no utility. It is the only stopping rule here that a questioner
with an unformalised [[possible-worlds|hypothesis space]] can actually run.

The price is stated by its own literature. Because the rule counts novelty
rather than coverage, it cannot distinguish "the space is exhausted" from
"this respondent pool is homogeneous" — which is why hennink-2022 conditions
every number on population homogeneity and narrow aims. And the choice of
counting unit is a free parameter worth a factor of two in cost.

## Transfer

| | Home field | Here |
|---|---|---|
| Setting | many respondents, one interview each, transcripts coded by analysts | one answerer, a sequence of questions, constraints recorded |
| Unit counted | new codes / themes per interview | new constraints per question |
| What survives | the novelty-rate rule with declared $B$, $R$, $T$; the mandatory $R$-question overshoot; the finding that the stopping point is set by the counting unit |
| What does not | the sample-size numbers (9–17). They index heterogeneity of a *population* of respondents, and there is no population when one answerer is asked repeatedly. Also: the bootstrapping validation is retrospective on completed datasets, so it shows the rule would have been *consistent*, never that the codebook was complete |

## Limits

- The rule's own validation (guest-2020) resamples datasets whose collection
  had already stopped, so nothing in it bounds the themes that were never
  collected — the failure mode of [[unknown-unknowns]] is invisible to a
  novelty counter by construction.
- The six crossing points above are read from guest-2020's Tables 2–4 for run
  length 2 only; the run-length-3 columns give later crossings ($7{+}3$ to
  $16{+}3$), so the reported $B{+}R$ is a function of $R$ as well as of the
  data, and no single pair of integers characterises a dataset.
- Braun & Clarke (2021) reject the premise: information redundancy presupposes
  that meaning resides in the data waiting to be found; under reflexive
  thematic analysis interpretation never exhausts, so no novelty count can
  terminate. Their objection is to the *concept*, not to the arithmetic.
- Malterud, Siersma & Guassora (2016) propose **information power** instead —
  sample size judged by study aim, sample specificity, use of established
  theory, quality of dialogue and analysis strategy — explicitly non-countable,
  and so not a stopping rule in the sense this map needs.
- All counts assume a single analyst team and a fixed coding scheme; codebook
  drift would show as spurious novelty.

## Related

[[stopping-rules]] · [[saturation]] · [[sprt]] · [[adaptive-submodularity]] · [[unknown-unknowns]] · [[elicitation-protocols]]

[^s1]: braun-2021
[^s2]: glaser-1967
[^s3]: guest-2006
[^s4]: guest-2020
[^s5]: hennink-2017
[^s6]: hennink-2022
[^s7]: malterud-2016
