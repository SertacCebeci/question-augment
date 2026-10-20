---
description: "The basic framework for deciding under uncertainty. The \"value\" of von Neumann & Morgenstern (1944), *Theory of Games and Economic Behavior*: anyone accepting the axioms over lotteries (completeness,"
aliases: ["EU theory", "von Neumann–Morgenstern utility"]
sources: ["von-neumann-1944", "allais-1953", "ellsberg-1961", "kahneman-1979"]
---
# Expected utility

> The basic framework for deciding under uncertainty. The "value" of
> information is defined from here.

## Framework

$$a^* = \arg\max_a \sum_s p(s)\,U(a,s)$$[^s1][^s2][^s3][^s4]

von Neumann & Morgenstern (1944), *Theory of Games and Economic Behavior*:
anyone accepting the axioms over lotteries (completeness, transitivity,
continuity, independence) behaves *as if* maximising the expectation of a
utility function over outcomes — and that utility is fixed only up to a
positive affine transformation.

## Known as

| Field | Name there | Relation |
|---|---|---|
| decision theory | EU theory | exact — the same maximisation rule and axiom set |
| economics, game theory | von Neumann–Morgenstern utility | close — names the utility function the representation theorem delivers, not the decision rule built on it |

## Why it matters

The definition of [[value-of-information]] rests on it: information is
valuable because it **causes a better action to be chosen**. This part is the
theorem's: VoI is a difference of two expected utilities, so with no utility
function the expression is undefined.

**Conjecture (this wiki).** [[expected-information-gain]] needs only a model
of $W$ and a prior; VoI needs, in addition, a utility and an action set.
Reading off what each definition requires as input: what can be
task-independent is EIG, not VoI — and of the four criteria in
[[stopping-rules]], the VoI-based one is usable only where the objective is
already known. This does not follow from the vNM theorem; it is this wiki's
inference, and it rests on the first bullet under *Limits*.

## Practical consequence

Same status — conjecture, not theorem: an exploration phase can be run
without an elicited utility function; a prioritisation phase cannot. That is
where [[blackwell-informativeness]] also lands, from the other direction: its
ordering is exactly the part of the comparison that holds for *every* utility
function, and it is partial for that reason.

## Transfer

| | |
|---|---|
| In its home field | choice among lotteries over a **known** outcome set, with a utility over outcomes and probabilities given |
| Here | choosing which question to ask next, where the "outcome" is the downstream action taken once the answer arrives |
| What survives | the argmax-over-expected-value logic, and the VoI definition built on it — a question is scored by the difference it makes to the best available action, not by what it reveals |
| What does not | the elicited utility function, and with it the enumerated outcome set: an open design task has neither, so no *numerical* VoI ordering of candidate questions travels — only the qualitative test "would any answer change what I do?" |

## Limits

- EIG is task-independent only given a parameterisation of $W$ and a prior
  over it; choosing the axes and the prior is itself a task-dependent step,
  so the asymmetry with VoI is one of degree, not kind. This is the
  assumption the conjecture above rests on.
- The axioms are systematically violated in choice experiments —
  independence by the Allais (1953) pattern, Savage's sure-thing principle by
  the Ellsberg (1961) [[efe-planning-as-variational-inference|ambiguity]] pattern; Kahneman & Tversky (1979) offered
  prospect theory as the descriptive successor, which is not yet in this
  wiki. The theorem itself is untouched: it is normative, not a prediction of
  behaviour.
- Requires a utility function and an action set. For an open design task
  neither exists yet; that is the tension this note names.
- Utility is over outcomes; a question's value is derived, never primitive.

## Related

[[value-of-information]] · [[expected-information-gain]] · [[bounded-rationality]] · [[blackwell-informativeness]] · [[stopping-rules]]

[^s1]: von-neumann-1944
[^s2]: allais-1953
[^s3]: ellsberg-1961
[^s4]: kahneman-1979
