---
description: "Before asking anything, find out what you already silently assumed: parse Sadeghi, Smith & Del Rey Fernández (2026, §4.3),"
aliases: ["Known/Guessed classification", "unsupported numerical choices"]
sources: ["sadeghi-2026"]
---
# Unsupported literal detection

> Before asking anything, find out what you already silently assumed: parse
> the artifact you generated and check every numeric commitment in it
> against what the input actually said.

## Definition / Mechanism

Sadeghi, Smith & Del Rey Fernández (2026, §4.3), translating a[^s1]
natural-language optimization problem into solver code with an LLM, sort
every numerical literal the generated program contains into exactly one of
two classes: **Known** — the value appears, in some decimal-equivalent
form, among the numeric tokens extracted from the original description —
or **Guessed** — no such match exists, so the LLM supplied the value on its
own. The match runs over the code's abstract syntax tree against a
regex-extracted token list from the source text, normalizing decimal forms
("40" vs "40.0"). Every Guessed literal becomes an open parameter: a
candidate axis the model has already committed to a value for, with
nothing in the input licensing that value.

## Why it matters

This gives stall 1 ("what are the dimensions of $W$?") a mechanical,
automatable generator for the specific case where $W$'s axes are read off
an artifact an LLM has already produced, rather than elicited from a person
directly: an unlicensed numeric commitment inside a generated artifact
*is* an undiscovered axis, and the check for one needs no domain model —
only the generated code and its source text. It operationalizes, for one
concrete artifact class, the wiki's own principle that an item resting on
no question is a hidden assumption (see [[sufficient-statistic]],
[[data-processing-inequality]]): here the "item" is a program literal and
the "question" is whatever textual evidence would have licensed it. Every
subsequent question the system asks (see
[[sensitivity-weighted-question-score]]) is drawn from exactly the set this
check flags.

## Limits

- Syntactic, not semantic: a number that happens to appear in the input
  text for an unrelated reason (a different quantity, a label, a date)
  would be misclassified as Known; the paper does not report a rate for
  this failure mode.
- Only catches literal numeric commitments. A value the input states in
  words ("a dozen trucks"), a derived or computed quantity, or a
  non-numeric modeling choice (which constraint to include, which variable
  is integer) leaves no literal to match and is invisible to this check.
- Demonstrated only on LP/MIP translation benchmarks (NL4OPT, NL4LP,
  ReSocratic, EasyLP, ComplexLP, IndustryOR, ComplexOR); nothing in the
  source shows the AST-vs-text-token match generalizing to artifacts other
  than generated optimization code.
- A Guessed literal that the [[question-budgets|question budget]] never reaches is left at the
  LLM's original guess with no flag surviving to the final output — the
  detection identifies the axis but does not, on its own, guarantee it is
  ever asked about or reported as unresolved.

## Related

[[sensitivity-weighted-question-score]] · [[sufficient-statistic]] · [[data-processing-inequality]] · [[objectives-generation-deficit]] · [[unknown-unknowns]]

[^s1]: sadeghi-2026
