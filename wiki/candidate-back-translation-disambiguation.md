---
description: "Locates what a disambiguation question should ask by generating several formally valid readings of a request and diffing their natural-language renderings against the source text."
aliases: ["Ambiguity Inquirer", "back-translation ambiguity localization"]
sources: ["fang-2026-clarifystl"]
---
# Candidate-generation and back-translation for disambiguation

> Wording a disambiguation question does not start from the ambiguous text; it starts from the set of formal readings the text is still consistent with, rendered back into language the asker already used.

## Definition / Mechanism

Once [[vagueness-then-ambiguity-clarification-pipeline|ClarifySTL]]'s [[efe-planning-as-variational-inference|Ambiguity]] Detector flags a requirement, its Inquirer does not ask about the ambiguity directly: "the Ambiguity Inquirer generates multiple STL candidates and back-translates them into natural language. It compares these natural language versions with the original requirement, analyzes which parts need clarification, and formulates queries for the user."[^c1]

The worked example shows the question naming the fork rather than the whole sentence: for a requirement whose candidate readings diverge on when a time window starts, the generated query is "Does 'next 30 seconds' start from the first time 𝑥1 exceeds 0.2, or from the entire 10-150 second interval?"[^c2]

## Why it matters

The mechanism is what fills in Task 2 ("what to ask") of [[clarifying-interaction-decomposition]] for this domain: instead of a generic ambiguity flag, the question is generated from an explicit enumeration of the formal readings still open. Removing the Inquirer and falling back to a bare few-shot prompt degrades the pipeline measurably: "when the Inquirer is removed, the number of iterations per requirement increases, indicating higher labor costs... the metric-based evaluation metrics decrease, which suggests that the lack of the Inquirer partially causes annotators to provide inaccurate clarification responses."[^c3]

## Limits

- Demonstrated only where back-translation is close to deterministic — STL formulas have a template-based natural-language rendering; whether diffing generalizes when candidate readings are free text with no formal generator is untested here.
- The ablation (^c3) isolates "Inquirer present vs. bare few-shot prompt," not the back-translation-and-diff step against other query-generation strategies, so its contribution relative to a simpler "ask about the flagged span" baseline is not measured.
- Presupposes the Ambiguity Detector has already localized which requirement is ambiguous; it says nothing about generating candidates before a detector has fired, so it answers stall 3 (how the question touches the axis) and not stall 2 (whether to ask at all).

## Related

[[vagueness-then-ambiguity-clarification-pipeline]] · [[clarifying-interaction-decomposition]] · [[ambiguity-taxonomy]]

[^c1]: fang-2026-clarifystl — "the Ambiguity Inquirer generates multiple STL candidates and back-translates them into natural language. It compares these natural language versions with the original requirement, analyzes which parts need clarification, and formulates queries for the user."
[^c2]: fang-2026-clarifystl
[^c3]: fang-2026-clarifystl
