---
description: "People recognise a good question far more reliably than they can produce In a modified Battleship game (a $6\\times6$ grid, three hidden ships,"
aliases: ["generation-recognition asymmetry", "question generation vs question evaluation"]
sources: ["rothe-2016", "rothe-2017", "rothe-2018"]
---
# Question asking as program generation

> People recognise a good question far more reliably than they can produce
> one — so asking well is a generate-then-rank problem, not a single-shot
> one (Rothe, Lake & Gureckis 2016, 2017, 2018).

## Mechanism

In a modified Battleship game (a $6\times6$ grid, three hidden ships, about[^s1][^s2][^s3]
1.6 million possible boards) participants ask one free natural-language
question about a partly revealed board. Each question is hand-translated
into a program in a lambda-calculus DSL — `(size Blue)`, `(> (size Red)
(size Blue))` — that executes against any hypothesised board and returns the
answer. Because a question is a program, three things become computable for
it: [[expected-information-gain]] over the [[possible-worlds|hypothesis space]], a complexity
term (negative log probability under the question grammar, an MDL-style
penalty), and the answer type. That is what makes "how good was this
question?" a measured quantity rather than a judgement.

## Evidence — two tasks, one asymmetry

**Generation.** 40 participants on Mechanical Turk, 18 board contexts, one
question each: 720 questions, 605 analysable. Per context, the correlation
between how often a question was generated and its EIG was mean $r = 0.16$
(95% HDI $[0.08, 0.23]$); against the cost-sensitive expected-savings model,
$0.04$ $[-0.06, 0.15]$. In all 18 contexts the mode of the question-quality
histogram sat substantially below the top of the available EIG range — people
asked mid-quality questions, not the best one (Rothe et al. 2018, Exp. 1).

**Evaluation.** 45 participants ranked six questions per context — sampled
from those produced in Exp. 1 — from best to worst. The mean per-context
correlation between average rank score and EIG was $r = 0.89$ $[0.84, 0.94]$;
for expected savings, $0.78$ $[0.66, 0.89]$ (Exp. 2). A replication with
answers actually delivered and a paid guessing phase (41 participants) gave
$r = 0.87$ for EIG and $0.86$ for expected savings (Exp. 3). The difference
between the evaluation and generation correlations had 100% of its posterior
mass above zero.

**Generating and recognising are different abilities.** Humans recognise a
good question when they see it and do not spontaneously produce it.

## Why it matters

The architectural consequence — **this wiki's inference from the asymmetry,
not a result of the study** — is that a single-shot generator inherits the
weak half of the measurement, while a generate-$N$-then-rank pipeline puts
the strong half (ranking, $r \approx 0.89$) in the loop. This is a second
justification for large question volumes: not only coverage but building a
**candidate pool**, with ranking as a separate step.

The descriptive standing of EIG is split by these results, and the split is
the useful part. EIG describes **evaluation**: it tracks human rank
orderings at $r \approx 0.89$ with no free parameters. It does not describe
**generation**: Rothe et al. (2017) report no correlation at all between
generation frequency and EIG alone, and the 2018 figure is $r = 0.16$. What
does predict generation is EIG *plus* the complexity term — the full program
model of Rothe et al. (2017) reaches an average Spearman $\rho = 0.64$ with
held-out human question frequencies, while its complexity-agnostic variant
reaches $-0.36$. So the theory has descriptive validity for rating and
rank-ordering, and for generation only in its complexity-penalised form —
never as EIG maximisation, which is exactly what Exp. 1 shows people do not
do. In the per-participant model comparison the cost-sensitive expected-
savings model beat EIG for 36/45 (Exp. 2) and 30/41 (Exp. 3) participants:
what people rank is closer to [[value-of-information]] than to pure
information.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Cognitive science | generation–recognition asymmetry (Exp. 1 vs Exp. 2, Rothe et al. 2018) | exact |
| Cognitive science | question generation vs question evaluation | exact — the pair of tasks whose gap is this object |

*Not* aliases of this concept: "Battleship question study" names the
paradigm and "Rothe–Lake–Gureckis" names the authors — both stay in
`sources`, neither is a name for the asymmetry. Memory research's
recall-versus-recognition advantage is a different object (retrieval of
stored items, not the quality of a produced question) and is not indexed
here.

## Transfer

| | |
|---|---|
| **Home field** | [[bayesian-experimental-design|Bayesian experimental design]] and decision theory: EIG, and the cost-sensitive expected-savings utility, score a *design* against an explicit prior over an enumerable hypothesis space |
| **Here** | the same functionals are used not to select but to *measure* — free natural-language questions are compiled to programs and scored, turning "was that a good question?" into a number comparable across people |
| **What survives** | the pre-answer ranking logic: scoring a question from the distribution of its answers alone reproduces human rank orderings ($r \approx 0.89$, no fitted parameters) |
| **What does not** | the enumerable prior. Both scores require a hypothesis space you can sum over and an answer function written by hand; outside such a domain neither EIG nor expected savings can be computed for a natural-language question, so this measurement cannot be repeated on an open-domain asker |

## Limits

- Generate-$N$-then-rank was **not measured**: generation and evaluation were
  separate tasks with separate participants, and no participant ranked
  candidates they had generated. The pipeline claim above is this wiki's
  inference, not a finding.
- One paradigm (Battleship) and a DSL that fixes what counts as a question;
  13% of collected questions were discarded as invalid or ambiguous and ~3%
  as computationally intractable to formalise, so the measured question space
  is the expressible one.
- One lab, one line of work — CogSci 2016, the NIPS 2017 model, the 2018
  journal version. Exp. 3 is the same authors' conceptual replication of
  Exp. 2, not an independent one.
- The evaluation result is a preference over six curated questions per
  context, sampled to span EIG and frequency; it does not show people can
  rank an unrestricted set.
- Extension of the asymmetry to LLMs is a hypothesis stated in this wiki and
  untested by any of these experiments.

## Related

[[expected-information-gain]] · [[value-of-information]] · [[constraint-seeking]] · [[twenty-questions]] · [[divergent-convergent]]

[^s1]: rothe-2016
[^s2]: rothe-2017
[^s3]: rothe-2018
