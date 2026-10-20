---
description: "A binary accept/reject decision made on an uncertain measurement is at its JCGM 106:2012 separates two kinds of limit."
aliases: ["guard band", "guarded acceptance", "guarded rejection", "stringent acceptance", "stringent rejection", "positive compliance", "positive non-compliance"]
sources: ["jcgm-2012-conformity"]
---
# Guard band — the acceptance limit offset by the uncertainty

> A binary accept/reject decision made on an uncertain measurement is at its
> *worst* exactly at the limit where it is invoked. Metrology's answer is not
> to sharpen the measurement or to add a third output: it is to move the
> limit by a declared multiple of the uncertainty, in the direction of the
> costlier error, under a rule documented before the measurement.

## Definition / Mechanism

JCGM 106:2012 separates two kinds of limit. A **tolerance limit** (3.3.4) is[^s1]
a specified bound on permissible values of the *property*; an **acceptance
limit** (3.3.8) is a specified bound on permissible *measured* values. The
**guard band** (3.3.11) is the "interval between a tolerance limit and a
corresponding acceptance limit", and a **decision rule** (3.3.12) is a
"documented rule that describes how measurement uncertainty will be accounted
for with regard to accepting or rejecting an item, given a specified
requirement and the result of a measurement".

Four risks are named, and they are four different numbers: **specific**
consumer's risk (3.3.13, the probability that a *particular accepted* item is
non-conforming) and specific producer's risk (3.3.14, that a particular
rejected item is conforming); **global** consumer's and producer's risk
(3.3.15–16, over a future measurement drawn from a production process).

**Simple acceptance** (8.2) sets the acceptance limit equal to the tolerance
limit — the rule also called *shared risk*. Its failure mode is the load-
bearing fact here (8.3.1.2): with a symmetric unimodal PDF for the measurand,
the probability of accepting a non-conforming item, or of rejecting a
conforming one, "can be as large as 50 %" when the measured value lies very
close to the tolerance limit.

**Guarded acceptance** (8.3.2) pulls the acceptance limit inside the tolerance
interval: the length parameter $w = T_\mathrm{U} - A_\mathrm{U} > 0$, commonly
taken as $w = rU$ with $U = 2u$ (coverage factor $k=2$) and the multiplier $r$
chosen to assure a minimum conformance probability for an accepted item;
$r = 1$, i.e. $w = U$, is a common choice (8.3.2.3). The worked example at
8.3.2.3 is the default rule of **ISO 14253-1:1998** — the edition JCGM 106
cites as its reference [21] and adapts as its figure 10 from that standard's
figure 7 — which took $w = U = 2u$ at each of two tolerance limits; JCGM 106
states its aim as keeping the probability of accepting a non-conforming item
at most 2,3 % for any measured value inside the acceptance interval under a
normal PDF, the maximum occurring when the measured value coincides with an
acceptance limit.

**Guarded rejection** (8.3.3) does the opposite — an acceptance limit *outside*
the tolerance interval, $w < 0$ — "often employed when one wants clear
evidence that a limit has been exceeded prior to taking a negative action".
Its worked example: a 100 km/h speed limit measured with 2 % relative standard
uncertainty gives a ticketing threshold of about 107 km/h for 99,9 %
confidence that the limit was exceeded.

So the geometry is the whole mechanism: **direction** of the offset is set by
which of the two errors is worse, **size** by the declared uncertainty times a
chosen multiplier. The two risks trade against each other — 8.3.1.3 says
either probability can be reduced "at the cost of increasing the other" — and
no choice of band removes both.

## Known as

| Field | Name there | exact / close |
|---|---|---|
| Metrology — conformity assessment (JCGM 106 3.3.11) | guard band; guarded acceptance / guarded rejection | exact |
| Dimensional metrology (ASME B89.7.3.1:2001, reference [2] of JCGM 106) | stringent acceptance / stringent rejection | exact — the NOTEs to 8.3.2.1 and 8.3.3.1 read "Guarded acceptance is also known as stringent acceptance" and "Guarded rejection is also known as stringent rejection" |
| Analytical chemistry (Hibbert 2007, reference [18] of JCGM 106) | positive compliance for acceptance / positive non-compliance for rejection | exact — named in the same two NOTEs, as alternative names for the same two rules |
| Dimensional metrology (ISO 14253-1:1998) | conformance zone inside a specification zone | close — the same geometry with the two intervals renamed (JCGM 106, after figure 10), not another name for the rule |

Not this concept: **simple acceptance** ("shared risk") is the rule with a
zero guard band, not another name for it; the **measurement capability index**
$C_\mathrm{m} = T/(4u)$ (3.3.17) describes whether the measurement is good
enough for the tolerance, and is not a decision rule; **tolerance limit** and
**acceptance limit** name the two objects the band lies between.

## Why it matters

On stall 10 the wiki already has a third output priced by a number
([[abstention]]: name a cost, a risk level or a coverage level, and threshold
an uncertainty score). The guard band is a different move and the wiki has it
nowhere else: the output stays **binary**, and what shifts is the *threshold*,
by the answerer's own declared uncertainty. Two consequences for a
practitioner. First, the decision rule is a documented artifact agreed before
the measurement (3.3.12), so an asker knows in advance what will be done with
the residual rather than reading a hedge afterwards. Second, the rule cannot
even be stated until an [[uncertainty-budget]] exists — $U$ and $k$ are its
inputs — which makes the uncertainty statement a precondition for the
decision instead of a decoration on it.

## Transfer

| | |
|---|---|
| In its home field | a scalar measurand, a specification with one or two tolerance limits set by someone else, a post-measurement PDF for the measurand obtained per the GUM, and a binary accept/reject |
| Here | a threshold decision by an answerer whose estimate of the thresholded quantity is itself uncertain |
| What survives | the geometry (offset the limit by a multiple of the declared uncertainty, in the direction of the costlier error); the 50 %-at-the-limit argument, which holds for any symmetric unimodal PDF; the requirement that the rule be documented before the decision; the fact that the two risks are traded, never jointly removed |
| What does not | the numbers. $r$, the 2,3 % and the 99,9 % rest on a normal (or scaled and shifted $t$) PDF for a scalar measurand and on a tolerance interval supplied from outside. An answerer's stall-10 quantities have no externally given tolerance limit, so the wiki inherits the form of the rule and must supply the limit itself — and with no PDF for its statistic, the offset can be declared but not calibrated to a risk |

## Limits

- JCGM 106 assumes throughout (Introduction) that the measurement result is
  expressed in a manner compatible with the GUM and that corrections have been
  applied for all recognized significant systematic effects. The band prices
  the **declared** uncertainty only: an under-declared budget yields a
  confidently wrong guard band, and nothing in the document detects that.
- The $r = 1$ default is reported here as of 2012 and is not to be taken as
  the current standard default. This note reads only JCGM 106:2012, which
  cites ISO 14253-1:1998; the 2017 revision of ISO 14253-1 is reported to have
  replaced that default with a smaller band ($w = 0{,}83U$, false-acceptance
  probability below 5 %), and was not read here. Any claim in this note about
  the *size* of the customary offset is therefore a claim about the 1998 rule
  as JCGM 106 reproduces it, not about current practice.
- The document states explicitly that choosing the tolerance limits and the
  acceptance limits "are business or policy decisions" whose general treatment
  is beyond its scope. It supplies the arithmetic of risk, not the costs that
  set $r$ — the same gap [[abstention]] has.
- Its scope is a single scalar property with a binary outcome; a third option
  such as "perform another measurement" is named in the Introduction as an
  extension and is not treated.
- The claim that this is a *distinct* commitment mechanism rather than a
  variant of thresholding an uncertainty score is this note's own reading of
  the two literatures, which do not cite each other.

## Related

[[uncertainty-budget]] · [[type-b-evaluation]] · [[abstention]] · [[guarded-threshold]] · [[roc-curve]] · [[discordant-recommendation]]

[^s1]: jcgm-2012-conformity
