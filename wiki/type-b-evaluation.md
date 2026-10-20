---
description: "How a component with no repeated observations gets a standard deviation GUM (JCGM 100:2008) 4.3.1: for an estimate $x_i$ **not** obtained from repeated observations,"
aliases: ["Type B evaluation", "Type B standard uncertainty"]
sources: ["jcgm-2008"]
---
# Type B evaluation of standard uncertainty

> How a component with no repeated observations gets a standard deviation
> anyway — and the rule that it then enters the sum on exactly the same terms
> as the statistical components.

## Definition / Mechanism

GUM (JCGM 100:2008) 4.3.1: for an estimate $x_i$ **not** obtained from[^s1]
repeated observations, the associated standard uncertainty $u(x_i)$ "is
evaluated by scientific judgement based on all of the available information
on the possible variability of $X_i$". The admissible pool is listed, and it
is short:

- previous measurement data;
- experience with or general knowledge of the behaviour and properties of
  relevant materials and instruments;
- manufacturer's specifications;
- data provided in [[calibration]] and other certificates;
- uncertainties assigned to reference data taken from handbooks.

Judgement becomes a number by assigning an *a priori* distribution and taking
its standard deviation:

| What is known | $u(x_i)$ | GUM |
|---|---|---|
| quoted as a multiple of a standard deviation ("240 µg at the three standard deviation level") | quoted value ÷ multiplier (→ 80 µg) | 4.3.3 |
| quoted at a 90 / 95 / 99 % level of confidence, normality assumed | ÷ 1,64 / 1,96 / 2,58 | 4.3.4 |
| bounds $\pm a$, no other knowledge | $a/\sqrt{3}$ (rectangular) | 4.3.7, eq. 7 |
| bounds $\pm a$, values near the bounds less likely | $a/\sqrt{6}$ (triangular) | 4.3.9, eq. 9b |
| "a fifty-fifty chance of lying in $a_-$ to $a_+$" | $1{,}48\,a$ | 4.3.5 |
| "about two chances out of three" | $a$ | 4.3.6 |

Three clauses fix its standing.

1. **It is a category of method, not of nature.** The A/B split "applies to
   uncertainty and [is] not [a substitute] for the words 'random' and
   'systematic'"; the uncertainty of a correction for a known systematic
   effect may be obtained by a Type A evaluation in some cases and a Type B in
   others, "as may the uncertainty characterizing a random effect" (3.3.3).
   3.3.4: the classification "is for convenience of discussion only" and "is
   not meant to indicate that there is any difference in the nature of the
   components resulting from the two types of evaluation". Both are quantified
   by variances or standard deviations and both enter equation (10)
   identically.
2. **It is not the weaker one.** 4.3.2: a Type B evaluation "can be as
   reliable as a Type A evaluation, especially in a measurement situation
   where a Type A evaluation is based on a comparatively small number of
   statistically independent observations."
3. **It must not be double-counted.** 4.3.10: a Type B component enters the
   combination "only to the extent that the effect does not contribute to the
   observed variability of the observations" — the part already visible in the
   statistics is already counted.

Type A uncertainty comes from an observed frequency distribution, Type B from
an assumed distribution based on degree of belief; the GUM says flatly that
"both approaches employ recognized interpretations of probability" (3.3.5).

## Known as

| Field | Name there | exact / close |
|---|---|---|
| Metrology — the GUM 4.3 | Type B evaluation of standard uncertainty | exact |
| Metrology — INC-1 (1980), category B | components "évaluées par d'autres moyens" (evaluated by other means) | exact — the originating recommendation, reproduced in GUM Annex A.1 |
| Metrology — convenience naming | Type B standard uncertainty, Type B variance | close — the GUM's own names for the *output* $u(x_i)$, $u^2(x_i)$ (4.3.1) |

Not this concept: **"systematic uncertainty"** is not another name for it —
GUM 3.3.3 forbids the substitution, and INC-1 (1980), quoted in Annex A.1,
says the expression *incertitude systématique* invites misinterpretation and
must be avoided. **Epistemic uncertainty** is not an alias either: the pair in
[[uncertainty-decomposition]] splits by the *nature* of the unknown, and GUM
3.3.4 says this split is explicitly not about nature.

## Why it matters

On stall 10 this is the clause that changes what a practitioner writes. An
answerer's non-statistical grounds for doubt — evidence that may be stale, a
specification read off someone's sheet, a value taken from a handbook, plain
experience with the instrument — normally leave the answer as adverbs or
leave it entirely. The GUM requires each to appear as a **line with a number
and a named basis**, converted by a declared distribution, and then forbids
treating it as second class in the sum ([[uncertainty-budget]]). The
observable consequence: two answerers with identical observed variance can
legitimately report different uncertainties, and the difference is auditable
line by line instead of being a difference in temperament.

## Transfer

| | |
|---|---|
| In its home field | an input quantity with physical bounds and a documented provenance (certificate, specification, handbook), whose variance enters a first-order propagation |
| Here | an answerer's non-statistical grounds for doubt, entered as named components with numbers rather than as hedging |
| What survives | the enumeration of judgement-derived components; the equal-standing rule (3.3.4) and the non-inferiority claim (4.3.2); the double-counting ban (4.3.10), which in this setting forbids counting an acknowledged weakness twice — once in a self-consistency spread and again as a caveat |
| What does not | the conversions. $a/\sqrt{3}$ and $1{,}48a$ are derived from bounds on a physical quantity with a defined interval; an answer in words has no $a_-$ and $a_+$, so the discipline imports and the arithmetic does not. The non-inferiority claim is practitioner guidance in a consensus standard, with no measurement behind it |

## Limits

- The GUM itself limits the claim: 4.3.11 says the discussion of Type B
  evaluation "is meant only to be indicative" and that evaluations "should be
  based on quantitative data to the maximum extent possible". These are rules
  of thumb with a distributional justification, not a procedure.
- **Nothing here tells you what the components are.** GUM 3.3.2's ten sources
  are a checklist, and an unrecognized effect contributes to the error rather
  than to the uncertainty. This note's value therefore depends on a
  completeness it does not supply.
- No measurement is cited — neither by the GUM nor here — that Type B
  components improve the coverage of the resulting interval. The claim that
  auditable lines beat a hedge is this note's inference from the reporting
  rules, not a finding.
- The rectangular-distribution default is a maximum-[[entropy]] choice under
  bounds, and GUM 4.3.9 itself notes that step discontinuities in a
  probability distribution "are often unphysical"; the choice of distribution
  is a modelling decision the standard leaves to judgement, which is the same
  judgement the evaluation was supposed to discipline.

## Related

[[uncertainty-budget]] · [[uncertainty-decomposition]] · [[calibration]] · [[verbal-probability-expressions]] · [[guard-band]]

[^s1]: jcgm-2008
