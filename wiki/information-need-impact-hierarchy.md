---
description: "Shapley attribution over six categories of missing SWE-issue information finds error information drives task success most, though issues omit it least often — frequency of a gap and its cost diverge."
aliases: []
sources: ["arxiv-2604-14624"]
---
# Information-need impact hierarchy

> The information a task description omits most often is not the
> information whose absence hurts it most.

## Definition / Mechanism

Vijayvargiya, Viswanathan & Neubig (2026) annotate 112[^s1]
highly underspecified SWE-Bench Verified issues into six categories of
missing information (error information, expected behavior, implementation
details, external references, reproduction steps,
version/environment), then generate 1,500 controlled underspecified
rewrites of 500 issues by deleting random subsets of these categories.
Running an agent (OpenHands + Seed OSS 36B) on 700 of these rewrites and
computing SHAP values isolates each category's marginal contribution to
binary task success (test-suite pass), holding the others' presence or
absence fixed. Overall, underspecification alone drops success from 43.8%
to 23.7% across the 700 instances.

Attribution and occurrence frequency rank categories in different, partly
inverted orders. "Error Information has the highest mean SHAP value
(0.183), followed by Implementation Details (0.0982). Expected Behavior
(0.0572) and External References (0.0355) show lower mean contributions."
 Yet the category with the highest impact is not the one most often
missing: "Expected Behavior is the most frequently missing category (65%
of issues) yet shows only moderate association with task success.
Conversely, Error Information is absent in 33% of underspecified issues
but has the highest mean SHAP value." The paper's reading: concrete
diagnostic signals (a stack trace, a failure point) let an agent narrow
its search directly, where an abstract goal restatement does not.

## Why it matters

A clarification policy that asks about whatever is missing most often —
the natural target if a system is trained on raw omission frequency — asks
about the wrong thing on average. Prioritizing by measured contribution to
the outcome, not by how commonly a slot goes unfilled, is a distinct and
separately-established design choice; [[staged-clarification-reward-pipeline]]
is the training mechanism built to encode exactly this ordering.

## Limits

- "Bootstrap confidence intervals overlap across categories, reflecting the
  limited sample size; we therefore interpret the ordering as an indicative
  trend rather than a statistically significant ranking." — the
  hierarchy is not shown to be statistically distinct category-by-category.
- Single domain (SWE-Bench issues), single agent backbone, and a codebook
  built by two annotators on 112 issues; the six categories and their
  ranking are not shown to transfer to other task-oriented domains.
- Category annotation for the SHAP analysis is itself an LLM judge (GPT-5)
  applying the codebook, not a human per-instance check — unverified
  against the two-annotator codebook development sample alone.

## Related

[[ask-f1-selective-escalation-metric]] · [[shapley-uncertainty-localization]]
· [[question-budgets]] · [[staged-clarification-reward-pipeline]] ·
[[answerable-clarification-strategies]]

[^s1]: arxiv-2604-14624
