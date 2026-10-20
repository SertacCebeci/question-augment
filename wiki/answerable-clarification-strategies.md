---
description: "Comparing questions to a hidden fully-specified reference operationalizes answerability; distributional analysis finds four strategies that predict it: evidence, specificity, scope, actionability."
aliases: []
sources: ["arxiv-2604-14624"]
---
# Answerable clarification strategies

> A question can target exactly the information that would fix the task
> and still be worthless, if the person being asked cannot supply the
> answer.

## Definition / Mechanism

Vijayvargiya, Viswanathan & Neubig (2026) operationalize
answerability by comparing a generated clarifying question against the
fully-specified original issue, held out from the model that generated the
question: "A question is considered answerable if it requests information
that is missing from the underspecified issue but present in the
fully-specified version." A GPT-5 judge sorts each question into
answerable, unanswerable (the requested information is not in the
fully-specified issue either) or redundant (already in the underspecified
issue).

Running this classification over questions from two models (GPT-5, GPT-5
nano) across 500 issues and measuring which of ~60 candidate linguistic and
structural characteristics separate answerable from unanswerable questions
(Vargha–Delaney effect size, p < 0.05) yields four recurring strategies:

| strategy | what it asks for | answerable example | unanswerable example |
|---|---|---|---|
| Ground in Evidence | concrete artifacts the user can directly share | "Share the stack trace" | "What is the middleware execution order?" |
| Demand Specificity | precise values, not abstract descriptions | "Which Python version?" | "What is the optimal version?" |
| Minimize Scope | the smallest unit isolating the issue | "Provide a 10-line script demonstrating this" | "Describe your entire architecture" |
| Ensure Actionability | actions the user can perform or directly observe | "Run pytest -v and share output" | "What would happen if you refactored?" |

[^c2.1][^c2.2][^c2.3][^c2.4]

The same four strategies emerge from both models' outputs, "suggesting that
these strategies reflect general properties of answerable question
formulation rather than model-specific artifacts." Separately, at the
level of a whole clarification set rather than one question, "increasing
the number of questions does not consistently improve performance. Success
rates plateau despite larger clarification sets. At the same time, the
proportion of answerable questions decreases as question count increases."
[^c4]

## Why it matters

Task relevance and answerability are shown to be orthogonal axes: a
well-formulated question can target a low-impact category
([[information-need-impact-hierarchy]]) and still be answerable, and a
question naming a high-impact category can still fail if phrased so the
user cannot supply it ("What internal error handling logic failed?"). A
policy optimized only for what to ask, without also optimizing how to
phrase it against what the asker can plausibly know, leaves value on the
table on this axis alone.

## Limits

- Answerability is approximated by comparison to the paper's own
  fully-specified reference issue, not by asking a real user: "Real user
  capability may be lower or higher than this proxy."[^c5]
- The four strategies are derived from a post-hoc grouping of ~60
  statistically-significant characteristics by the authors, not from an
  independent validation set or inter-rater check on the grouping itself.
- Single domain (GitHub issue clarification) and two models from one
  family (GPT-5, GPT-5 nano); not shown to hold for open-ended or
  conversational (non-software) clarification.

## Related

[[information-need-impact-hierarchy]] · [[staged-clarification-reward-pipeline]]
· [[multi-turn-clarification-plateau]] · [[gated-answerability-rule]] ·
[[question-budgets]]

[^c2.1]: arxiv-2604-14624
[^c2.2]: arxiv-2604-14624
[^c2.3]: arxiv-2604-14624
[^c2.4]: arxiv-2604-14624
[^c4]: arxiv-2604-14624 — "Figure 3 shows that increasing the number of questions does not consistently improve performance. Success rates plateau despite larger clarification sets. At the same time, the proportion of answerable questions decreases as question count increases."
[^c5]: arxiv-2604-14624 — "Answerability is approximated using the full issue as a proxy. Real user capability may be lower or higher than this proxy."
