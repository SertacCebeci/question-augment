---
description: "A writing-support chatbot phrases each Socratic question from a specific extracted claim-premise relation and withholds its comment marker until the writer verbalizes the fix themselves."
aliases: []
sources: ["arxiv-2604-07167"]
---
# Argument-grounded Socratic questioning

> A question that names the writer's own claim and premise, not a
> template, and a system that will not check the box until the writer
> says the fix out loud.

## Definition / Mechanism

Hugenroth et al. (2026)'s Critical Inker is a writing
tool that extracts an argumentation graph from an essay (claims, premises,
independent vs. jointly-acting reasons) and validates each support
relation with a chain-of-thought prompt before a Socratic chatbot engages
the writer about the flaws found. Two design choices make the chatbot's
asking distinct from a generic clarification loop.

First, the question's wording is bound to the specific edge of the
argument graph it targets, not a fixed template: rather than asking
generic questions like "Is this claim supported?", Critical Inker's
chatbot references specific logical relationships extracted from the
argument graph: "You claim X because Y, but I am curious, how does Y
actually support X?"
[^c1]

The chatbot's system prompt additionally forbids it from stating the
correction itself — a "reasoning assistant" persona that "interestedly
inquires" about the user's intent rather than supplying one.
[^c4]

Second, the loop's completion criterion is the writer's own utterance, not
the chatbot's judgment of elapsed turns or a fixed hint ladder: only when
the user identifies the issue themselves will the Socratic chatbot create
a comment marker reminding the user about what they want to change.[^c2]
Until that happens the flaw stays open and the chatbot keeps probing the
same relation; nothing is marked resolved on the chatbot's own say-so.

Third, the dialogue is single-threaded through a generated plan: it tracks
the conversation state against a generated plan (A.3) ensuring it only
addresses one logical flaw at a time, deferring every other detected flaw
until the current one is closed.[^c3]

## Why it matters

This bundles two separable levers on *what* an agent asks and *when* it
stops asking about one thing: content specificity (grounding the question
in a mined graph edge, not a generic prompt) and a verbalization gate on
closing that sub-dialogue (the agent's own confidence or turn count never
substitutes for the writer saying the fix). It differs from
[[gated-socratic-scaffolding]], whose gate is a separate evaluator agent
judging *whether to speak at all*, and from
[[staged-socratic-hint-policy]], whose gate is an escalating ladder of
hint specificity keyed to learner stalling. Here the gate is on *what
closes an already-open thread*, and the specificity comes from a mined
graph edge rather than an author-written stage.

## Limits

- The mechanism itself is evaluated only qualitatively, in a pilot with 4
  participants in the Socratic condition, 7 total split across two
  conditions: Visual Feedback (n=3), where logical flaws were directly
  highlighted with explanations, or Socratic Chatbot (n=4), where the
  system guided users through targeted questions to identify issues
  themselves.
[^c7]
- There is no controlled comparison against a non-argument-grounded or
  non-gated Socratic baseline; the 91.2% relation-overlap figure the paper
  reports is the accuracy of the underlying argument-mining pipeline, not
  of the questioning mechanism's effect on reflection.
[^c8]
- The gate can misfire against the writer's own text — one participant
  reported that the chatbot "asked a question which was answered in the
  subsequent sentences," i.e. it can probe a relation the writer had
  already resolved elsewhere in the essay, since the graph it questions
  from is a snapshot, not re-checked against later-written context
  mid-dialogue.
[^c6]
- The intended effect has only self-reported, unverified qualitative
  support — one participant said the tool "let me think for myself
  instead of just writing it for me" — not benchmarked against the
  paper's own Visual Feedback alternative on any shared outcome measure.
[^c5]
- The system is described as "a prototype in development"; the argument
  graph on which every question is grounded is itself LLM-extracted and
  only 91.2%-accurate against human annotation, so a wrongly extracted
  relation propagates into a wrongly grounded question.

## Related

[[socratic-method]] · [[gated-socratic-scaffolding]] ·
[[staged-socratic-hint-policy]] · [[socratic-physics-critic]] ·
[[structural-disagreement-clarification]]

[^c1]: arxiv-2604-07167 — "Rather than asking generic questions like "Is this claim supported?", Critical Inker’s chatbot references specific logical relationships extracted from the argument graph: "You claim X because Y, but I am curious, how does Y actually support X?""
[^c2]: arxiv-2604-07167 — "Only when the user identifies the issue themselves will the Socratic chatbot create a comment marker reminding the user about what they want to change."
[^c3]: arxiv-2604-07167 — "It tracks the conversation state against a generated plan (A.3) ensuring it only addresses one logical flaw at a time."
[^c4]: arxiv-2604-07167 — "For the chatbot modality, we designed a system prompt that strictly forbids direct correction (A.4). The instructions emphasize a “reasoning assistant” persona that “interestedly inquires” about the user’s intent."
[^c5]: arxiv-2604-07167 — "let me think for myself instead of just writing it for me"
[^c6]: arxiv-2604-07167 — "it asked a question which was answered in the subsequent sentences"
[^c7]: arxiv-2604-07167 — "we conducted a small-scale pilot study with 7 participants recruited online and randomly assigned to one of two conditions: Visual Feedback (n=3), where logical flaws were directly highlighted with explanations, or Socratic Chatbot (n=4), where the system guided users through targeted questions to identify issues themselves."
[^c8]: arxiv-2604-07167 — "The model achieved a relations overlap of 91.2%."
