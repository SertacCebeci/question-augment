---
description: "An interactive clinical-QA benchmark and Expert/Patient system where the Expert abstains from a diagnosis when unconfident and asks a follow-up question instead."
aliases: ["MEDIQ", "MediQ-Expert"]
sources: ["li-2024"]
---
# MediQ — interactive clinical question-asking benchmark

## Definition / Mechanism

Li et al. (2024) convert two static multiple-choice medical QA datasets
(MedQA, CraftMD) into an interactive task by disclosing only a patient's
age, gender and chief complaint at turn 0 and holding the rest of the
patient record $K$ back. A **Patient system** answers follow-up questions
by retrieving supporting atomic facts from $K$; an **Expert system** must
decide, each turn, whether its current knowledge $K_{t-1}$ is sufficient to
answer the multiple-choice question or whether to ask a question $q_t$ that
expands it toward $K^{*} \subseteq K$, the information actually needed.[^c1]

The Expert is broken into five modules: initial assessment, an
**[[abstention|Abstention]] Module** that outputs a yes/no "answer now vs. ask" decision,
question generation, information integration (appending the new
question–answer pair to the log), and decision making.[^c2]

The Abstention Module is the load-bearing piece: it is tested as six
variants — BASIC (an implicit choice baked into one generation), Numerical
confidence (a 0–1 score against a threshold), Binary (yes/no on "enough
information"), Scale (a 5-point Likert confidence rating against a
threshold), each optionally combined with Rationale Generation (a reasoning
chain before the confidence judgment) and Self-Consistency (repeating the
judgment $n$ times and taking the mean/mode).[^c3]

## Why it matters

Prompting an LLM to just choose between asking and answering (BASIC) makes
things worse, not better: on iMedQA, the interactive BASIC Expert scores
11.3% relative accuracy lower than a non-interactive baseline given the
same starting information — "the final accuracy is even lower than its
non-interactive counterpart (Initial) with the same initial information (a
average of 11.3% relative drop)," and for most samples "no model chooses to
ask any questions."[^c4]

A dedicated Abstention Module recovers this: "Scale Abstention (1-5
confidence rating) with rationale generation and a self-consistency factor
of 3 achieves the best performance, outperforming the BASIC interactive
setup by 22.3% and the non-interactive Initial setup by 12.1%," while
"self-consistency alone degrades performance unless paired with rationale
generation" — and even the best configuration leaves "a 10.3% gap ...
compared to an upper bound when full information is presented at once."[^c5]

For stall 2 (which axis first) this locates the failure one step earlier
than axis choice: before an LLM can select *which* question to ask, it must
first decide *whether* to ask at all, and that decision — not question
selection — is where naive prompting fails.

## Transfer

| | |
|---|---|
| In its home field | selective classification: a classifier abstains from a single terminal label when a confidence score falls below a threshold, evaluated as a risk–coverage tradeoff on i.i.d. labelled data |
| Here | a multi-turn Expert abstains from a terminal diagnosis in favor of one more question, evaluated as final-answer accuracy and conversation length on a clinical MCQ benchmark |
| What survives | the binary structure — a confidence signal gates a terminal commitment — and the finding that the signal must be a deliberated judgment (reasoning chain, repeated sampling), not a bare score |
| What does not | any risk or coverage guarantee: MediQ reports only point accuracy differences under a grid-searched threshold (Appendix D), with no bound on error at a stated coverage |

## Limits

- All headline numbers are for GPT-3.5 on iMedQA under a grid-searched
  threshold (Appendix D); the paper reports the pattern generalizes across
  Llama-3-8B/70B and GPT-4 on iMedQA and iCraftMD (via the interactive
  B EST column) but the exact percentages above are not established for
  every model.[^c6]
- The Patient system itself is imperfect (Fact-Select factuality 89.1,
  relevance 79.9 in Table 1), so some of the residual 10.3% gap to the
  full-information upper bound is attributable to lossy question answering,
  not only to imperfect question-asking.[^c7]

## Related

[[abstention]] · [[calibration]] · [[semantic-entropy]] · [[clarification-benchmarks]] · [[value-of-information]]

[^c1]: li-2024 — "The Patient system has access to the entire patient record K = {k0 , k1 , . . . , kn }, and the necessary information to answer the multiple choice question is K∗ ⊆ K. At the start of the t-th turn, the knowledge available to the Expert system is denoted as Kt−1 = {k0 , . . . , ki }."
[^c2]: li-2024 — "breaking down the task into five medically-grounded steps: (1) initial assessment, (2) abstention, (3) question generation, (4) information integration, and (5) decision making"
[^c3]: li-2024 — "0. BASIC: As a baseline, the model is asked to implicitly indicate its abstain decision by either generating an atomic question or producing an answer to the MCQ."
[^c4]: li-2024 — "the final accuracy is even lower than its non-interactive counterpart (Initial) with the same initial information (a average of 11.3"
[^c5]: li-2024 — "Overall, Scale Abstention (1-5 confidence rating) with rationale generation and a self-consistency factor of 3 achieves the best performance, outperforming the BASIC interactive setup by 22.3% and the non-interactive Initial setup by 12.1%."
[^c6]: li-2024 — "Analysis and ablations use GPT-3.5 results on iM ED QA only."
[^c7]: li-2024 — "Fact-Select 89.1 79.9"
