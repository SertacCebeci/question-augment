---
description: "An LLM pipeline that turns a learner's minimal pen mark into four ranked candidate questions across predefined categories, cutting the physical cost of formulating a query."
aliases: ["Question Autocompletion"]
sources: ["rhee-2026"]
---
# Question Autocompletion

> Given a sparse ink mark (an underline, a circled term, a keyword), an LLM
> pipeline proposes four full candidate questions in fixed content
> categories, ranked by a confidence score, so the learner selects an axis
> to ask about instead of composing its wording.

## Definition / Mechanism

In Penquiry V2, when a learner marks a minimal region of a document, the
system sends the context text, a cropped image of the region, and the
learner's annotated crop to an LLM, which returns four candidate questions
— one per predefined content category (Definition, Description,
Interpretation, Knowledge-based) — each with a confidence score; the
highest-confidence candidate is shown first, and the learner can page
through the others or refine one by adding more ink. "the system analyzes
the action within its local context to dynamically generate four
autocomplete question candidates... The LLM evaluates the user's sketch to
calculate a confidence score for each category, displaying the
autocompleted question with the highest confidence."[^c1]

## Why it matters

It is a working instance of axis selection under a nearly-empty input: the
axis (which category of question to ask) is chosen by the system's
confidence ranking rather than by the asker deciding first and then
wording it, and the asker's only remaining act is to accept, page to an
alternative category, or add ink to refine. In a within-subjects study
(N=16), 74.9% of submitted queries used an autocompleted candidate rather
than free-form text.[^c2]

## Transfer

| | Home field (HCI systems research) | Here (this wiki) | Survives | Does not |
|---|---|---|---|
| Confidence-ranked candidate generation | Rank *k* LLM-generated question drafts by a model-internal confidence score and default to the top one | Offered as a live selection-under-[[efe-planning-as-variational-inference|ambiguity]] mechanism for stall 2 | The idea that a system can rank candidate axes and present one by default while keeping the rest reachable | Any guarantee that the confidence score tracks true informativeness — the paper reports adoption and downstream effects, not a [[calibration]] check of the score itself |

## Limits

The claim rests on one lab-based, within-subjects study of 16 university
students using one document domain (a climate-science textbook) and one
underlying model (GPT-4o) for both drafting and scoring; the reported
NASA-TLX gains over the prior version were directional, not significant —
"Although Penquiry V2 showed a noticeable trend toward lower physical and
temporal demands, the differences between the two versions did not reach
statistical significance."[^c3]

The one significant behavioural result is a temporal shift toward more
knowledge-based questions over a session (18.85% early to 40.43% late,
Friedman p = 0.015), which the authors read as scaffolding but which is
also consistent with participants simply running out of easier questions
to ask first.[^c4]

Qualitative reports also describe a failure mode this note's claim does
not cover: the proactive suggestions "could sometimes hinder learners...
generated candidate questions may anchor learners to system-framed
perspectives or narrow the range of alternatives they consider."[^c5]

## Related

[[expected-information-gain]] · [[bounded-rationality]] · [[value-of-information]]

[^c1]: rhee-2026
[^c2]: rhee-2026 — "The effectiveness of the Question Autocompletion is evidenced by its high adoption rate, with 74.9% of all submitted queries utilizing autocompletion."
[^c3]: rhee-2026 — "Although Penquiry V2 showed a noticeable trend toward lower physical and temporal demands, the differences between the two versions did not reach statistical significance."
[^c4]: rhee-2026 — "Results revealed a significant progressive increase in the proportion of knowledge-based questions: 18.85% (early), 37.19% (mid), and 40.43% (late) (Figure 9; Friedman test, 𝑝 = 0.015; Wilcoxon signed-rank test for early vs. late, 𝑝 = 0.019)."
[^c5]: rhee-2026 — "generated candidate questions may anchor learners to system-framed perspectives or narrow the range of alternatives they consider, highlighting a potential risk of over-steering."
