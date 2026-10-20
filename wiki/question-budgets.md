---
description: "Same mathematics, different cost → different behaviour. The counts are illustrative orders of magnitude, not calibrated thresholds, and the cost row is an assumed ordering,"
aliases: ["question budget", "two-budget split", "ask-cost asymmetry"]
sources: ["mark-2008"]
---
# The question budgets

> Same mathematics, different cost → different behaviour.

## The split

| | Agent asking itself | Asking the user |
|---|---|---|
| Cost | ~0 | very high (assumed — see Limits) |
| Count (order of magnitude, illustrative) | $10^3$–$10^4$ | $10$–$30$ |
| Source | Model's latent knowledge + commitment | The user's intent |
| DPI | Binding ([[data-processing-inequality]]) | Not binding — new information |
| Selection rule | Every question with EIG > 0 | Only VoI ≫ Cost |

The counts are illustrative orders of magnitude, not calibrated thresholds,[^s1]
and the cost row is an assumed ordering, not a measurement — both are
qualified in *Limits*. The arithmetic behind the selection rules —
$\text{Net} = \mathrm{VoI}(q) - \mathrm{Cost}(q)$, Howard (1966) — belongs to
[[value-of-information]]; what this note adds is the split by *source* and the
third budget below.

## What the lens buys, and what it cannot decide

It buys one thing: a rule that names a threshold is incomplete until it names
which budget it is about. It cannot price the user's attention (no cost
measure lives here — see *Limits*), and it does not select which question goes
in which budget: it says only that a question whose answer exists in weights
or context has no business in the user budget.

## Why this split does not contradict itself

The apparent contradiction between *"the aim is never to ask many questions"*
and a practice of thousands of questions dissolves if the two rules are read
as being about two different budgets:

```text
"Ask few questions"      →  about the USER budget
"Ask 10,000 questions"   →  about the AGENT budget
```

On that reading a rule that names only one of the budgets is incomplete rather
than wrong. This is a disambiguation this wiki proposes, not a result: it holds
only if the two practices really are indexed by the source of the answer, which
neither slogan states.

## The asymmetry — a conditional inference

Under the DPI reading of the agent in [[data-processing-inequality]] ($X \to Y
\to Z$ with $Y$ = weights + context), and while a user answer costs orders of
magnitude more than a self-question, the two budgets do not substitute for one
another:

- Self-questioning surfaces what is already in weights and context; it adds no
  *new* information about the user's intent ([[data-processing-inequality]]).
- The user cannot absorb $10^4$ questions at the assumed cost.

So the architecture **this wiki derives** is two-layered: a small number of
high-VoI user questions, on top of which sit many cheap agent questions. Both
premises are stated above because both can fail — if either does, the
conclusion goes with it.

## The third budget: the external world

One more category should not be forgotten: reading files, searching,
executing.

```text
Cost   :  low but nonzero
Source :  real external information (outside the agent's Y, so the DPI bound
          on self-questioning does not apply)
Rule   :  look here before asking the user
```

The rule *never ask what you can look up* places exactly this budget ahead of
the user budget.

## Limits

- **The cost ordering is asserted, not measured.** No source in this wiki
  prices a user's attention in the units $\mathrm{VoI} - \mathrm{Cost}$ needs.
  The nearest evidence is HCI's, and it does not give that number: Mark, Gudith
  & Klocke (CHI 2008) `mark-2008` interrupted 48 subjects with a supervisor's
  questions and found interrupted tasks completed in *less* time with no loss
  of quality, at the price of more stress, frustration, time pressure and
  effort on a modified NASA-TLX — a cost on a workload scale, not a utility.
  If user cost falls (an ambient or asynchronous channel), the two-layer
  architecture and the VoI ≫ Cost rule collapse into the single VoI > 0 rule.
- **"Binding" is an imported modelling choice, not a theorem here.** It is the
  DPI applied to the agent read as $X \to Y \to Z$ with $Y$ = weights +
  context ([[data-processing-inequality]] *Limits*); the bound is relative to
  information already present and is not observable. So "the agent cannot
  learn the user's intent by asking itself" is a bound on *new* information —
  not a claim that self-questioning is useless. The transfer tables for both
  imports live in [[data-processing-inequality]] and [[value-of-information]],
  not here.
- The counts $10^3$–$10^4$ and $10$–$30$ are illustrative; nothing in this
  wiki calibrates them.
- Assumes self-questions are near-free. At scale they are not (context,
  latency, the cost of reading the answers back) — which erodes the same
  ordering from the other side.

## Related

[[value-of-information]] · [[data-processing-inequality]] · [[sprt]] · [[constraint-as-information]]

[^s1]: mark-2008
