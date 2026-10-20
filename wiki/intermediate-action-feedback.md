---
description: "Deep Research agents propose natural-language actions across four report-improvement categories for users to select, then separately judge execution — splitting what-to-do from how-well-done."
aliases: ["DRACULA", "action selection and execution protocol", "action preferences and execution judgments"]
sources: ["arxiv-2604-23815"]
---
# Intermediate action feedback

> Instead of scoring the finished report, or asking a clarifying question
> before writing it, show the user a menu of candidate next moves and let
> them pick — then judge separately whether the picked moves were carried
> out well.

## Definition / Mechanism

Balepur, Hamada, Kishore, Feldman, Singh, Siangliulue, Chang, Rudinger, Choi, Boyd-Graber, Downey & Naik (2026)
build DRACULA on a two-step feedback protocol for Scientific Deep Research
(DR) agents — systems that synthesize papers into multi-section reports.
Instead of rating the finished report (the field's default) or asking the
user a clarifying question before generating it, the system proposes eight
natural-language **actions** — decisions the agent could take to improve
the report, e.g. "Add a section on datasets" — and the user selects the
subset they want: "In our feedback protocol, users issue a query and we
propose actions for them to select from. We then show a report reflecting
the selected actions, which users judge for execution quality."
[^c1]

The two judgments are kept separate and collected independently:
`lselect` (did the user want this action) and `lexec` (was the action
carried out well), so a report's failure is attributable to the wrong
action being proposed/picked versus the right action being poorly
executed.

Actions are deliberately not phrased as questions: "We use actions as they
clearly describe how a DR system will attempt to improve a report, unlike
other designs such as follow-up questions that focus on clarifying
intent."
[^c2]

A clarifying question elicits missing information about intent before
acting; an action proposes a concrete edit to the artifact itself, and
the user's selection *is* the elicited preference — no separate
interpretation step is needed. To keep proposals broad, actions are
generated to cover four fixed categories: "Content (what the report
covers), Style (how the report is written), Specificity (how to treat the
query scope), and Research Ideas (how to adapt to the researcher's
goals)."
[^c3]

Half the actions per query are conditioned only on the query ("generic"),
half also on papers the user has flagged as relevant ("paper"), giving
eight candidates per query.

Nineteen expert CS researchers ran this protocol over five weeks (~450
hours), yielding "8,103 binary selections as preferences on proposed
actions and 5,230 binary judgments for action execution, each with
rationales."
[^c4]

The paper's own use of this data locates where the difficulty actually
sits: "Users rate our tested models as more successful at executing
selected actions than at proposing useful ones... a key challenge in DR
is not just executing actions, but knowing which actions users want
executed."
[^c5]

Separating the elicitation step (which action to propose and whether the
user wants it) from the execution step (whether the agent carried it out)
is what makes that attribution measurable at all — a report-only rating
or a single question-answer exchange collapses both into one score.

## Why it matters

Report-only feedback and pre-generation clarifying questions both fold
"what does the user want" and "did the system do it" into a single
judgment. The action-selection/action-execution split turns "asking" into
picking from a generated menu rather than answering an open question, and
makes it possible to show — empirically, not by assumption — that
*generating* useful candidates, not *executing* selected ones, is the
harder half of the problem for a long-horizon agent.

## Limits

- Actions are LLM-generated (GPT-4.1, Claude-4 Sonnet, Gemini-2.5 Flash,
  DeepSeek-V3), so the menu itself can omit an action a user would have
  wanted but was never offered; the protocol measures preference over
  *proposed* actions, not over the space of all possible actions.
- Built and evaluated on one DR system (MyScholarQA) with 19–20 paid
  expert annotators in CS subfields; the four action categories and the
  generic/paper conditioning were chosen by the authors, not derived from
  a broader survey of DR use cases.
- The rarity of system-limitation rejections (§3.2) is a qualitative
  reading of rejection rationales on this system and these users, not a
  general claim that execution is always easy relative to proposal.

## Related

[[information-need-reification]] · [[checklist-clarification-tradeoff]] · [[decision-centric-design]] · [[value-of-information]]

[^c1]: arxiv-2604-23815
[^c2]: arxiv-2604-23815 — "We use actions as they clearly describe how a DR system will attempt to improve a report, unlike other designs such as follow-up questions that focus on clarifying intent (Wang et al., 2025a)."
[^c3]: arxiv-2604-23815
[^c4]: arxiv-2604-23815 — "In total, DRACULA has 8,103 binary selections as preferences on proposed actions and 5,230 binary judgments for action execution, each with rationales (§2)."
[^c5]: arxiv-2604-23815
