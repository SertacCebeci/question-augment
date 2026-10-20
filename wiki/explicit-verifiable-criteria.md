---
description: "Prompts that state each success condition as an explicit, checkable criterion were met more reliably than harder prompts that left conditions implicit; unnamed tools and sizes caused the errors."
aliases: ["explicit verifiable criteria", "criterion explicitness", "specification clarity over complexity", "checkable success conditions"]
sources: ["arxiv-2512-01174"]
---
# Explicit verifiable criteria

A prompt can carry its success conditions in two ways: as a general description of what is wanted, or as a list of conditions that a checker could test one at a time. DrawingBench uses the second form throughout. Each of its 250 drawing prompts is scored against up to eight rule-based criteria (required tools, required colours matched to hex codes, minimum segments, minimum canvas coverage, a maximum action count, a position constraint, a size constraint and a corner placement), and the scorer returns "deterministic 0-1 scores" for each.[^e1]

The difficulty classes show what the stated form does. Hard prompts average 4.2 explicit constraints, against 2.8 for Medium, and every Hard prompt carries a position constraint, against 62% of Medium prompts.[^e2][^e11] Hard then scored above Medium on the second turn, 0.973 against 0.958, although its spatial demands are greater.[^e12] The authors' reading is that "Specification clarity matters more than task complexity,"[^e3] with the mechanism that "When criteria are deterministic, models" reliably meet their requirements.[^e4] The sentence continues "reliably satisfy requirements regardless of complexity."[^e5]

The failures point the same way. The commonest tool error arose when the prompt did not name the tool: "Tool selection omissions (appearing in 18 tasks) predominantly occurred when task descriptions mentioned tools implicitly rather than explicitly."[^e6] Some models answered "draw a red circle" with "pen-based circular" strokes instead of the circle tool.[^e7] Coverage failures followed prompts with no size, where "models often drew geometrically correct but undersized shapes."[^e8] The authors conclude that "specification ambiguity, rather than model capability limitations, drives many errors."[^e9]

What transfers is a separation between two things a prompt can have. A prompt can be long and detailed, or it can be explicit about what counts as success. [[prompt-specificity-effect]] measures the first, through perplexity and across tasks where detail adds structure to a procedure. The DrawingBench evidence concerns the second. An unnamed condition must be guessed by the answerer, and a wrong guess gives no sign, because nothing in the prompt names the criterion that was missed. My inference is that the conditions a checker would test are the part an answerer can satisfy reliably only when they are named, so detail that names no checkable condition should help less. The paper's first prompt-design principle points the same way: "(1) Clarity: unambiguous instructions,".[^e10]

## Limits

- The difficulty classes are the authors' construction, and the Hard tier is small: by my count from Table 2 it holds 21 of the 250 prompts, so the 100% rate rests on few tasks. The sections read report point rates and no interval for the Hard-Medium difference.
- Explicitness is never varied alone. Hard prompts differ from Medium in category, length and spatial content as well as in constraint count. The claim is a correlation across classes, not an intervention on one prompt's wording.
- The criteria are checkable by construction, because the scorer is rule-based. Whether explicit conditions that no checker can test help is not tested here. Over-specification can also constrain reasoning, a risk [[prompt-specificity-effect]] reports, and this text does not test it.
- One task family (drawing on a canvas, text-only input), four models, and a single feedback turn. The claim does not reach open-ended questions where no checker can exist (my inference).
- The attribution of errors to missing criteria (18 tool omissions, 12 coverage failures) uses the authors' error categories and examples. The link from one missing criterion to one error is read from examples, not measured per prompt.

## Related

- [[prompt-specificity-effect]] — general prompt detail, measured by perplexity; this note isolates checkable success conditions within that dimension
- [[agentic-iteration-gap-under-localized-verifier-feedback]] — the feedback side of the same kind of task: a checker that names the violated rule
- [[specific-actionable-self-feedback]] — a critique helps when it names where the problem is; a criterion stated in the prompt does the same job before the first draft

[^e1]: arxiv-2512-01174 — "deterministic 0-1 scores"
[^e2]: arxiv-2512-01174 — "Hard tasks averaged 4.2 explicit constraints"
[^e3]: arxiv-2512-01174 — "Specification clarity matters more than task complexity"
[^e4]: arxiv-2512-01174 — "When criteria are deterministic, models"
[^e5]: arxiv-2512-01174 — "reliably satisfy requirements regardless of complexity."
[^e6]: arxiv-2512-01174 — "Tool selection omissions (appearing in 18 tasks) predominantly occurred when task descriptions mentioned tools implicitly rather than explicitly."
[^e7]: arxiv-2512-01174 — "some models generated pen-based circular"
[^e8]: arxiv-2512-01174 — "models often drew geometrically correct but undersized shapes"
[^e9]: arxiv-2512-01174 — "than model capability limitations, drives many errors"
[^e10]: arxiv-2512-01174 — "(1) Clarity: unambiguous instructions,"
[^e11]: arxiv-2512-01174 — "have position constraints vs. 62% for Medium"
[^e12]: arxiv-2512-01174 — "Hard tasks achieved the highest Turn 2 performance (0.973)"
