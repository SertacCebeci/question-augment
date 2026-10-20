---
description: "A question whose premise is false has **no correct answer of the type it **The object (Hu et al."
aliases: ["false premise question", "FPQ", "false-premise question answering"]
sources: ["hu-2023", "kim-2021", "kim-2023", "vu-2023", "yu-2023", "arxiv-2512-01852"]
---
# False-premise questions

> A question whose premise is false has **no correct answer of the type it
> requests** — answering in that type endorses the premise. This is a
> separately benchmarked failure and it is common in real questions. On
> hand-written commonsense FPQs the answerer already holds the fact and fails
> to act on it; on naturally occurring questions the bottleneck is verifying
> the premise.

## Definition / Mechanism

**The object (Hu et al. 2023).** A false-premise question (FPQ) is one whose[^s1][^s2][^s3][^s4][^s5]
*support triple* is false: *"How many eyes does the sun have?"* asks for the
missing slot of `<sun, has_property, eye>`, which is false. *"Does the sun
have eyes?"* is **not** an FPQ — it asks *about* the triple instead of
building on it. The defect is in what the question takes as given, not in its
topic.

**Why answering is not neutral (Kim et al. 2023).** An answer whose type
matches the question's request necessarily endorses the failed presupposition:
any number given for *"How old was Mark Zuckerberg when he founded Google?"*
asserts that he founded it. There is no acceptable reply inside the answer
set; the acceptable reply leaves it — *"He did not found Google."*

**Base rates.** Yu et al. (2023, CREPE) annotate 8,400 Reddit information-
seeking questions and find **25%** carry false presuppositions. Kim et al. (2021) attribute **~21%** of unanswerable Natural Questions to unverifiable
presuppositions.

**Measured behaviour.**

| Evidence | Finding |
|---|---|
| Hu et al. 2023, pilot | Bloom-176B, OPT-175B, Jurassic-1, GPT-3 and Macaw all answer FPQs as if the premise held, yet answer correctly when asked *directly* whether the premise is true — the knowledge is present and not activated |
| Kim et al. 2023, 602 expert-annotated queries (301 with a flagged assumption, 246 false / 55 unverifiable) | best models: **56%** human-judged acceptability end-to-end, **64%** on assumption detection, **72%** on verification |
| Vu et al. 2023 (FreshQA) | all models, regardless of size, struggle on the false-premise subset |
| Hu et al. 2023, fine-tuning | **256** FPQ examples lift models above 1B past 70% accuracy; with general-question replay, 86.7% of FalseQA FPQs are rebutted at a **1.4%** false-rebuttal rate on valid questions |

**Multilingual benchmark (BHRAM-IL).** A benchmark in Hindi, Gujarati, Marathi, Odia and English puts false premises in a *semantically incorrect* category, described as a grammatically correct question that is semantically invalid.[^s6] Its items were synthesized by an LLM as ill-posed prompts covering category errors, anachronisms, geographically incongruous statements and false premises, then manually filtered.[^s7] Within that category the false-premise subcategory shows the largest drop: "questions show the most substantial performance" decline, and models "stated false information as true" — accepting an assertively stated falsehood as true.[^s8][^s9] The paper's reading is that larger models prioritize continuing the premise, a suggestion it does not test; its own claim is that scale "alone does not guarantee robustness to semantically inconsistent prompts", and the sharpest example is one model, GPT-OSS 20B.[^s10][^s11]

## Known as

| Name | Field | Relation |
|---|---|---|
| false premise question, FPQ | NLP evaluation (Hu et al. 2023) | exact |
| false-presupposition question (dataset: CREPE) | NLP / semantics (Yu et al. 2023; Kim et al. 2021) | close, **not an alias** — restricted to genuine linguistic presuppositions; FalseQA's support triple need not be presupposition-triggered. *CREPE* and *FalseQA* are dataset names, not names of the concept |
| questionable assumption, (QA)² | NLP evaluation (Kim et al. 2023) | **close, not an alias** — deliberately broader: 55 of its 301 flagged assumptions are *unverifiable* rather than false, and it admits propositions the asker merely believes and the question does not presuppose |
| loaded question | informal logic | close — names the rhetorical fault; no measurement |
| presupposition accommodation | pragmatics | close — the update rule that explains the endorsement ([[presupposition-accommodation]]) |

## Why it matters

1. **The defect is invisible in the answer's form.** The reply is fluent,
   in-type and confident. Nothing on the answer channel distinguishes it from
   a good answer, so an asker checking replies rather than premises will never
   see it.
2. **Detectability is not weirdness.** Kim et al. (2023) report that
   naturally occurring questionable assumptions do not stand out as bad
   questions; recognising them needs narrow topical knowledge. FalseQA's
   hand-written commonsense violations are the easy tail — a premise checker
   tuned on them will miss the ones users actually ask.
3. **The bottleneck differs by regime.** For commonsense FPQs the model
   already holds the fact (Hu et al.), so the fix is behavioural. For natural
   questions the bottleneck is evidence: Yu et al. find models identify
   presuppositions moderately well and fail at verifying them, mainly through
   retrieval; (QA)²'s verification subtask sits at 72%.
4. **A premise check has two costs, and both are measurable.** Missed
   rebuttals and over-rebuttal of valid questions (1.4% under replay). A
   checker reported on one of the two is unscored.

## Transfer

| | |
|---|---|
| **Home field** | open-domain QA evaluation: one question, one turn, a static public corpus, crowdsourced or expert labels of premise validity |
| **Here** | an agent deciding, before spending a turn, whether its own draft question carries an unverified premise — and, as answerer, whether to fill the requested slot at all |
| **What survives** | endorsement-by-answer-type; the order of magnitude of the base rate in user-authored questions; the two-cost scoring; the separation of *knowing* the premise is false from *acting* on it |
| **What does not** | the single-turn constraint — every benchmark here scores a rebuttal and none scores asking back, so nothing establishes when a clarification beats a correction ([[clarification-benchmarks]]); and the assumption of a verifiable public corpus, since an agent's premises are frequently about the asker's own situation, which no retrieval can check |

## Limits

- **The three datasets do not measure one class.** FalseQA is false-by-world-
  knowledge and hand-written; CREPE is genuine presupposition failure in
  natural questions; (QA)² admits unverifiable and merely-believed
  assumptions. The percentages above are not comparable across rows, and this
  note's claims hold only where all three agree: the endorsement mechanism and
  the failure to act.
- FalseQA was written by 20 annotators from GenericsKB seed words and is
  deliberately out of natural distribution. Its error-type breakdown describes
  the annotators' imagination, not any population of questions.
- Kim et al.'s 6% flag rate over 12,000 scraped queries is a floor, not a base
  rate — the authors note that the annotation task is hard and search results
  mislead the annotators.
- `[?]` The CREPE question count (8,400) and the (QA)² model figures
  (56/64/72), the 6% flag rate and the topical-knowledge finding were
  confirmed against the papers' listings and secondary summaries, not
  re-derived from primary text; the orders of magnitude, not the exact values,
  are what this note uses.
- The endorsement claim is about the **type** of the answer, not about the
  answerer's belief; no source cited shows an internal state changing.
- Everything here is single-turn QA over questions posed by humans. That an
  agent's *own* sub-questions carry false premises at any comparable rate is
  **this wiki's inference** and is measured by no source cited here.

## Related

[[presupposition-accommodation]] · [[question-as-partition]] · [[clarification-benchmarks]] · [[abstention]] · [[sycophantic-capitulation]] · [[third-position-repair]]

[^s1]: hu-2023
[^s2]: kim-2021
[^s3]: kim-2023
[^s4]: vu-2023
[^s5]: yu-2023
[^s6]: arxiv-2512-01852 — "SemInc contains semantically incorrect questions"
[^s7]: arxiv-2512-01852 — "(category errors, anachronisms, geographically incongruous statements, false premises)"
[^s8]: arxiv-2512-01852 — "questions show the most substantial performance"
[^s9]: arxiv-2512-01852 — "stated false information as true, demonstrating vulnerability to presupposition errors"
[^s10]: arxiv-2512-01852 — "alone does not guarantee robustness to semantically inconsistent prompts"
[^s11]: arxiv-2512-01852 — "larger models (e.g., GPT-OSS 20B)"
