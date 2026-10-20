---
description: "A framework for questions with multiple valid answers, used to prompt LLMs toward high-order questions; the best-performing of three tested prompt groundings."
aliases: ["Divergent Questioning", "DQ framework"]
sources: ["ucar-2026"]
---
# Divergent Questioning

> A question with more than one defensible answer, used as an LLM prompt
> grounding; in one test it produced the highest rate of teacher-judged
> high-order questions of any framework tried, but rarely reached the
> taxonomy's top level.

## Definition / Mechanism

Divergent questioning "promotes exploration and creativity by encouraging
questions with multiple potential answers or interpretations (McNamara,
1981). Divergent questions stimulate discussion and critical thinking,
aligning well with the goals of high-order cognitive development,"
attributed by Uçar et al. (2026) to Gallagher and Aschner
(1963).[^c1]

As an LLM prompt grounding — tested alongside Bloom's Taxonomy and
[[claim-evidence-reasoning|CER]] — it produced "hypothetical scenarios and
asked students to imagine and respond to new situations using single
questions," with no explicit reference to the source text
Uçar et al. (2026).[^c2]

## Why it matters

Of the answerable questions generated under this grounding, 69.81% were
rated high-order by teachers — the highest rate of any of the five tested
groundings, ahead of Bloom's-Evaluate (64.71%) and roughly 28 points above
CER (41.82%); see [[high-order-question-framework-comparison]]. But the
framework rarely reached the taxonomy's highest rung: "the divergent
questioning prompt strategy is quite successful with 11.32% Create
questions" Uçar et al. (2026) — a third of Bloom's-Create
grounding's own 35.29% Create rate. High-order and highest-order are not
the same target, and this framework is strong on the first without being
strong on the second.[^c3]

## Transfer

| | |
|---|---|
| **Home field** | education for creativity/critical thinking: a question class defined by having multiple potential answers or interpretations (Gallagher & Aschner, 1963; McNamara, 1981, as cited in Uçar et al. 2026), not tied to any subject-matter taxonomy |
| **Here** | an LLM prompt instruction asking the model to generate an open, hypothetical, multi-answer question from a supplied text |
| **What survives** | the defining criterion — a question inviting more than one defensible answer — and, empirically, the highest teacher-judged high-order rate among the frameworks tested |
| **What does not** | any guarantee of reaching the *top* cognitive level: unlike Bloom's-Create, this grounding carries no explicit instruction toward creation/design, so it under-produces Create-level questions relative to a framework built around that level |

## Limits

- The claim about the framework's origin (Gallagher & Aschner, 1963;
  McNamara, 1981) is read from Uçar et al. (2026)'s account,
  not verified against either primary source directly.
- Per-language samples were small: in Basque only two answerable high-order
  questions were generated under this grounding at all, so the 69.81%
  aggregate figure is carried mainly by the other two languages.
- One domain (secondary-school physics), two LLMs, one prompt template per
  framework; no ablation isolates which part of the prompt (the "multiple
  answers" instruction vs. the hypothetical-scenario framing it produced)
  drives the result.

## Related

[[high-order-question-framework-comparison]] · [[claim-evidence-reasoning]] · [[divergent-convergent]]

[^c1]: ucar-2026 — "promotes exploration and creativity by encouraging questions with multiple potential answers or interpretations (McNamara, 1981). Divergent questions stimulate discussion and critical thinking, aligning well with the goals of high-order cognitive development."
[^c2]: ucar-2026 — "presented hypothetical scenarios and asked students to imagine and respond to new situations using single questions"
[^c3]: ucar-2026 — "the divergent questioning prompt strategy is quite successful with 11.32% Create questions"
