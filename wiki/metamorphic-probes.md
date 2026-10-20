---
description: "A systematic way to derive dozens of questions from one, by borrowing the Metamorphic testing was introduced by T. Y. Chen, S. C. Cheung and S. M."
aliases: ["metamorphic probes", "question mutations", "specification mutation", "metamorphic specification mutation"]
sources: ["chen-1998", "segura-2016", "arxiv-2511-18249"]
---
# Metamorphic probes

> A systematic way to derive dozens of questions from one, by borrowing the
> input-mutation half of metamorphic testing and dropping its oracle half.

## Source idea

Metamorphic testing was introduced by T. Y. Chen, S. C. Cheung and S. M. Yiu[^s1][^s2]
in *Metamorphic Testing: A New Approach for Generating Next Test Cases*
(Technical Report HKUST-CS98-01, Hong Kong University of Science and
Technology, 1998). Its claim: even with no test oracle — no way to say what
the right output is — a **metamorphic relation** pairs a transformation of the
input with an expected consequence on the output. Run the program on both
inputs, compare the two outputs against the relation, and a violation is a
defect, without anyone knowing the correct answer.

Who uses it and where: Segura, Fraser, Sánchez and Ruiz-Cortés surveyed 119
metamorphic-testing papers (*A Survey on Metamorphic Testing*, IEEE
Transactions on Software Engineering 42(9):805–824, 2016) and report more than
twelve application areas, ranging from web services through simulation and
modelling to computer graphics.

## Question mutations

Here the "program" is a seed question and the transformation is applied to the
question, not to a program input. A base question — "How does a player acquire
X?" — spawns:

```text
INVERSE       How can X be lost?
ZERO          What if X is never acquired?
MAX           What if X is acquired without limit?
TEMPORAL      Can X exist before Y?
ORDER         What if Y happens before X?
ACTOR         Who else can affect X?
FAILURE       What if acquisition fails halfway?
REPEAT        What if it happens 1000 times?
CONCURRENT    What if X and Y happen simultaneously?
REMOVAL       Can the system work without X?
OBSERVABILITY How does the player know X happened?
BOUNDARY      What happens the first and last time?
```

## Known as

| Field | Name there | Relation |
|---|---|---|
| This wiki | question mutations / metamorphic probes | exact — this note's object |
| Software testing | metamorphic testing | close — the source technique; it pairs each input transformation with an expected output relation and checks it, which this catalogue does not |
| Software testing | metamorphic relation | close — the artifact the technique needs (input relation + expected output consequence); a mutation axis here is only its first half |
| Software engineering (LLM code generation) | metamorphic specification mutation | close — the same input-side operator applied to a task description, with a similarity gate on the variants and an oracle on the answers; see the section below |

`metamorphic testing` and `metamorphic relation` are **not** names for this
note's object. They denote a defect-detection procedure and its check
predicate, measured by fault-detection rate; this note's object is a
question-generation catalogue with no check and no such measure.

## Why it matters

The mutation list is a task-independent lens catalogue, like
[[context-free-questions]]: applying it needs only the seed question, not any
knowledge of what the answer would be.

**Conjecture (this wiki, untested):** one seed question × twelve mutations
should spread the resulting questions over more distinct axes than free
generation by the same model, which clusters. Nothing here is measured —
neither the axis spread, nor the expectation that a fixed catalogue is cheaper
or more reproducible than sampling many independent generations.

## Transfer

| | |
|---|---|
| In software testing | a program under test with deterministic outputs; a metamorphic relation transforms the input and states an expected consequence on the output; a violation is a defect, no oracle needed (Chen et al. 1998) |
| Here | the "program" is a seed question plus whatever source answers it; a mutation transforms the question along one axis and states **no** expected-consequence predicate on the answer |
| What survives | deriving many probes from one probe without an oracle; the axis-injection logic — the transformation catalogue is fixed in advance and independent of the answer |
| What does not | the check. With no expected output relation there is nothing to violate, so no defect detection follows — only question generation. Fault-detection effectiveness, the measure the surveyed literature reports, does not carry over |

## Theoretical placement

This is the **mechanised** form of hunting [[unknown-unknowns]]. If EIG cannot
be computed on an unmodelled axis, the remedy is to inject axes from outside.

It also pairs with [[cusum]]: mutations produce inconsistency, CUSUM catches
its accumulation — but only once a check is supplied separately, since the
mutations do not carry one.

## In code generation

Akhond and Uddin apply the same operator to programming specifications. Their
CodeMetaAgent has a Mutator that rewrites a task description under named
relations (negation, translation, sequential redefinition, paraphrase). The
authors present the relations as "semantic operators" inside the generation
loop, not as checks run after it.[^s3] A Reviewer compares each variant with
the original by a BERT-based similarity score, and "Variants whose similarity
scores fall below a defined threshold (0.8) are flagged as inconsistent".[^s4]
The surviving variants are each answered by the LLM, and the code is run
against the benchmark's oracle tests.

The mechanism therefore has two gates of different kinds. The mutation is
gated by a similarity score, which is not a test of equivalence. The answers
are scored by an oracle. The transfer table above says the question catalogue
has no check; in this paper a check is present, but it sits at the answer, not
at the mutation (my reading).

The reported effect is a gain in Pass@1 on code generation. "For GPT-OSS, the
CMA setup improved Pass@1 by +9% on HumanEval Pro and +17% on MBPP Pro."[^s5]
Table 3 gives positive Pass@1 gains for all four models (my reading), and the
authors conclude that "Applying CMA to problem descriptions consistently
increases code generation performance across models".[^s6]

## Limits

- The claim above rests on the twelve-item catalogue being a near-complete,
  domain-transferable set of axes. It is shown to be neither: it was written
  against a game-mechanics seed ("player acquires X"), it has no derivation,
  and no argument says a thirteenth axis would be redundant.
- It further assumes the answering source can answer a mutated question. A
  counterfactual mutation (`ZERO`, `MAX`) can push the question outside what
  any source covers, in which case the probe yields nothing.
- Mutations diversify **locally** — the axes are read off the seed question,
  so a seed on the wrong subject mutates into twelve wrong questions.
- No measurement of how many mutated questions turn out useful; the axis-count
  and cost claims in *Why it matters* are this wiki's conjecture, not results.
- `[?]` — `chen-1998` and `segura-2016` were located as official listings in
  this pass; the load-bearing sentences were not read against the full texts.
  Treat both as unverified until the verifier confirms.

- The gate measures similarity, not equivalence. A variant can stay close in
  wording and still change the requirement. The reviewer is a BERT model,
  chosen because "we choose the machine learning based model" to reduce
  dependence on LLMs.[^s9] The slices read report no human check of the
  variants that were kept (my inference).
- The text says each variant was "independently provided to the LLMs"[^s10],
  and also that the integrated configuration "combines" the relations "into a
  unified prompt-augmentation strategy".[^s8] These are different numbers of
  model calls; the slices read do not settle which produced the reported
  numbers.
- No control for extra prompting appears in the slices read. Without a
  baseline that spends the same calls on unlabelled rewrites, a gain cannot yet
  be credited to the relations rather than to more text per query (my
  inference).
- Coverage gains are small against a near-saturated baseline. The authors
  themselves say "While these numerical gains appear marginal".[^s7]
- Per-relation effects (RQ3) are not in the part read.

## Related

[[unknown-unknowns]] · [[context-free-questions]] · [[cusum]] · [[premortem]]

- [[rollout-question-augmentation]] — another textual operator that rewrites one question into several answer-preserving variants; the same move in another field, without a relation label.
- [[specification-channel-redundancy]] — the reverse measurement: under-specification costs HumanEval an average −11.8% Pass@1. Read with the gains above, the mutation axis looks like a specification axis (my inference).

[^s1]: chen-1998
[^s2]: segura-2016
[^s3]: arxiv-2511-18249 — "semantic operators"
[^s4]: arxiv-2511-18249 — "Variants whose similarity scores fall below a defined threshold (0.8) are flagged as inconsistent"
[^s5]: arxiv-2511-18249 — "For GPT-OSS, the CMA setup improved Pass@1 by +9% on HumanEval Pro and +17% on MBPP Pro."
[^s6]: arxiv-2511-18249 — "Applying CMA to problem descriptions consistently increases code generation performance across models"
[^s7]: arxiv-2511-18249 — "While these numerical gains appear marginal"
[^s8]: arxiv-2511-18249 — "all four MR transformations into a unified prompt-augmentation strategy"
[^s9]: arxiv-2511-18249 — "we choose the machine learning based model"
[^s10]: arxiv-2511-18249 — "independently provided to the LLMs"
