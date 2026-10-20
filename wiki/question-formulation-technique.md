---
description: "The most structured protocol for teaching people to ask their own questions. The protocol as given by Rothstein & Santana (2011);"
aliases: ["QFT"]
sources: ["rothstein-2011", "right-question-institute"]
---
# Question Formulation Technique (QFT)

> The most structured protocol for teaching people to ask their own questions.
> Rothstein & Santana (2011), *Make Just One Change*; maintained by the Right
> Question Institute.

## Steps

The protocol as given by Rothstein & Santana (2011); the phase names below[^s1][^s2]
follow the Right Question Institute's current wording (`right-question-institute`).

```text
Design a QFocus     a stimulus — statement, phrase, image, problem — never a question
Introduce the rules the four production rules, stated before any question is written
Produce questions   generate as many as possible, under the rules
Improve questions   classify each as closed or open, then convert one of each
Prioritize          choose three, against a criterion stated in advance
Discuss next steps  decide what will be done with the three
Reflect             name what was learned and how it was produced
```

## Production rules (Produce phase)

1. Ask as many questions as you can
2. **Do not stop to discuss, judge, or answer the questions**
3. Write down every question exactly as it is stated
4. Change any statement into a question

The second rule is the load-bearing one: the ban on answering keeps the first
answer from fixing the frame while questions are still being produced.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Education | QFT | exact — the standard abbreviation used by Rothstein & Santana and the Right Question Institute |
| — | Right Question Institute | **not this concept** — the organisation that developed, trademarks and maintains the protocol; it appears here as attribution and as the source key `right-question-institute`, not as another name for the technique |

## Three types of thinking

Rothstein & Santana (2011) design the steps to stimulate three kinds of
thinking — divergent (widen), convergent (narrow), metacognitive (observe the
process); the Right Question Institute states the same claim in its current
description. This is the protocol's design intent, not a measured effect. The
same three phases appear in [[divergent-convergent]] and in [[question-burst]];
no source here extends them beyond those.

## Why it matters

The mechanism QFT contributes is the **enforced separation of production from
evaluation**: a large question set is produced before any of it is answered,
judged or discussed. [[question-burst]] enforces the same separation with a
timer and a volume floor, [[divergent-convergent]] states it as a principle;
QFT carries it in a rule read aloud before the phase starts and in the phase
boundary itself.

> **Conjecture (this wiki, not Rothstein & Santana):** answering during Produce
> is harmful, while answering during Prioritize and Discuss-next-steps is what
> makes those phases converge. This is a reading of the batch/adaptive
> distinction in [[channel-capacity]] — itself that note's conjecture, not a
> corollary of the coding theorem.

The Improve step's closed↔open conversion structurally resembles the
mass-splitting rule in [[twenty-questions]] — closed questions cut the space,
open ones widen what may enter it. What that resemblance does and does not
carry is below.

## Transfer

| | [[channel-capacity]] (Shannon 1948, 1956) | [[twenty-questions]] (prefix-code equivalence) |
|---|---|---|
| In its home field | a fixed noisy channel over i.i.d. uses; feedback returns each received symbol before the next is sent | a known distribution $\mu$ over objects; each yes/no question splits the remaining probability mass |
| Here | Produce is a batch of questions emitted before any answer arrives; the answers, if any, come back after Prioritize | Improve's closed/open editing move, read as a choice about how a question divides the space |
| What survives | the phase-separation logic — feedback buys route, delay and robustness, not reach, so withholding answers during Produce costs nothing in what can eventually be learned | the shape intuition — a question's value depends on how it partitions what is open, which is why the protocol makes the closed/open form an explicit, revisable property |
| What does not | the capacity theorem itself: there is no $C$ for a group of participants, and no $\log_2\lvert W\rvert$ bound that tells the Produce phase how many questions to yield | the theorem's preconditions — known $\mu$, binary noiseless answers, arbitrary subsets. Classroom questions are natural language, unanswered at that point, and never scored against a prior; nothing quantitative transfers |

## Limits

- The conjecture above assumes the value of rule 2 is informational (framing
  collapse). Rothstein & Santana's own rationale is participatory — no
  contribution is judged, so everyone keeps producing. The two rationales
  predict different things when a facilitator asks a group of one.
- Built for classrooms and civic settings; the evidence in `rothstein-2011` is
  practitioner report and case study, not a controlled comparison against
  unstructured question generation.
- Assumes a group and a facilitator. Nothing here measures a solo asker, and
  the "three types of thinking" claim is design intent, not a finding.
- The Prioritize step's "three most important" is a fixed number with no stated
  basis in either source.

## Related

[[question-burst]] · [[context-free-questions]] · [[channel-capacity]] · [[divergent-convergent]] · [[twenty-questions]]

[^s1]: rothstein-2011
[^s2]: right-question-institute
