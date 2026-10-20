---
description: "A question whose answer partitions the candidate set rather than testing one ```text HYPOTHESIS-SCANNING \"Is it because a dog bit him?\" targets one candidate CONSTRAINT-SEEKING \"Did it have to do w…"
aliases: ["constraint-seeking questions"]
sources: ["ruggeri-2015"]
---
# Constraint-seeking

> A question whose answer partitions the candidate set rather than testing one
> member of it — and the measured conditions under which asking one pays.

## The distinction

```text[^s1]
HYPOTHESIS-SCANNING   "Is it because a dog bit him?"       targets one candidate
CONSTRAINT-SEEKING    "Did it have to do with transport?"  partitions the set
```

Ruggeri & Lombrozo (2015) treat hypothesis-scanning as a *degenerate* case of
constraint-seeking — the partition {one hypothesis, everything else}. The two
are not opposite kinds of question; they are two points on one axis, and the
studies below count them as two separate proportions.

## Finding

Ruggeri & Lombrozo (2015, *Cognition* 143:203–216), two individual-interview
studies with Italian schoolchildren and students in Livorno. **Study 1:** 58
children in grade 2–3 ($M_{age} = 7.0$), 46 in grade 5 ($M_{age} = 10.2$), 70
young adults ($M_{age} = 17.5$). Task: causal attribution — "yesterday a man
was late for work, find out why" — with 10 candidate causes laid out on cards
together with their frequencies (out of 40); participants asked as many
yes/no questions as they wanted until they named the cause. Measures: number
of questions to solution, and the proportion of questions coded
constraint-seeking (inter-rater $\kappa = .95$).

- **Age.** Constraint-seeking share overall: 23% (younger children), 20%
  (older children), 51% (young adults); as the *first* question: 28 / 29 /
  77% (Study 1, Table 2). The rise sits between children and young adults —
  the two child groups did not differ (post hoc $p = 1.00$).
- **Information structure.** All three groups asked more constraint-seeking
  questions when the 10 candidates were equally frequent (41%) than when the
  frequencies were skewed (26%), with no age interaction: the sensitivity is
  already present at seven. The authors' own expected-information-gain
  computation for this task: under a uniform prior even the worst
  constraint-seeking split (2 vs 8) is worth 0.72 bits against 0.15 for a
  hypothesis-scanning question, with a 1-in-10 chance of an immediate win;
  under the skewed prior a scan of the modal cause is worth 0.81 bits with a
  1-in-4 immediate win.

**Study 2** (96 / 87 / 90 participants) repeats this without giving the
candidate set, so the structure must be inferred from prior knowledge.

**Replication.** The developmental trajectory descends from Mosher & Hornsby
(1966) and has been found repeatedly since; the adaptation-to-information-
structure result is claimed by the authors as the first of its kind, and this
note knows of no direct replication of it.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Developmental psychology | constraint-seeking question | exact |
| Information theory | the "split the mass" / EIG-maximal question | close — a criterion *over* questions, not a category of them ([[twenty-questions]], [[expected-information-gain]]) |

**Not this concept.** *Hypothesis-scanning question* is the contrast term,
measured as its own proportion in the same studies and with its own optimality
regime — a separate object, not an alias here. *Pseudoconstraint-seeking* —
constraint-seeking in form but singleton in extension ("did he arrive late
because of something to do with the bus?" when only one bus hypothesis
remains) — is a third coded category, and rises with age (3 / 12 / 24%) while
being no more informative than the scan it disguises.

## What this wiki reads into it

Not in the source: the developmental "shift" need not be a change of strategy
at all. One criterion — target $P(\text{yes}) \approx 0.5$, i.e. split the
probability mass ([[twenty-questions]]) — picks the constraint-seeking
question under a flat prior and the direct scan under a dominant one, so the
same rule can generate both regimes and the observed proportions become a
proxy measure of it rather than a strategy inventory. Ruggeri & Lombrozo go
as far as "a strategy cannot be optimal *tout court*; efficiency depends on
the information structure of the task"; the reduction to a single selection
rule is this wiki's, and the corresponding conjecture — that the same
substitution explains LLMs defaulting to scans — is untested.

## Transfer

| | |
|---|---|
| **Home field** | Information theory / twenty questions: known $\mu$ over a finite set, arbitrary-subset binary noiseless questions, expected question count bounded by $H \le \mathbb{E}[\#q] < H+1$ |
| **Here** | Children's natural-language questions over 10 given candidate causes with stated frequencies, coded post hoc into two classes |
| **What survives** | The selection criterion: maximise the split of probability mass. It subsumes both classes — scanning is the singleton partition — and predicts the measured swing between the uniform and skewed conditions |
| **What does not** | The [[entropy]] bound: with a restricted, natural-language question set the achievable count sits above $H$ (Filmus & Mehalel; see [[twenty-questions]]), and one-step greedy optimality is not the multi-step optimum. The criterion also needs the mass to be *estimable* — Study 2 removes the stated frequencies, and pseudoconstraint-seeking shows a coded class can diverge from the actual partition |

## Limits

- The claim above is about a coding of questions into classes, not about the
  questions themselves: the class is assigned by a rater from surface form,
  and the paper's own pseudoconstraint-seeking category is the case where
  form and partition come apart.
- One population (Italian, three schools, one town), one task family (20
  questions on a causal vignette) with a small, given candidate set; the age
  effect in Study 1 separates adults from children, not 7-year-olds from
  10-year-olds, so "children shift with age" is weaker here than in the older
  literature it replicates.
- The developmental gap may reflect working memory, vocabulary for
  higher-order features, or task familiarity rather than a strategy choice.
- `ruggeri-2015` is recorded `verified: prior`, not verifier-confirmed; the
  figures above were read from the published PDF (Cognition 143:203–216).

## Related

[[twenty-questions]] · [[expected-information-gain]] · [[generalized-binary-search]] · [[question-asking-as-program-generation]]

[^s1]: ruggeri-2015
