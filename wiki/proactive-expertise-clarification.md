---
description: "PASSING has a conversational agent proactively probe a user's own expertise level through a two-stage inquiry strategy before it tailors an answer, rather than asking about the query's content."
aliases: ["PASSING", "Passing", "expertise clarification", "expertise-probing strategy"]
sources: ["cao-2026", "arxiv-2601-11534"]
---
# Proactive expertise clarification

> Before answering, ask who is asking — not what they meant. PASSING selects
> a question that targets the user's own proficiency, not the query's
> [[efe-planning-as-variational-inference|ambiguity]], and does so in an average of 1.2 turns.

## Definition / Mechanism

Cao & Huang (2026) start from the finding that "a user's
expertise on the specified query is difficult to infer from the query text",
so a system that only reads the query cannot decide how much to explain.
PASSING closes this by treating expertise assessment as its own dialogue act:
"Passing must probe the user's expertise on a given query via strategic
interaction."[^c1]

The probe is generated in two stages every turn. A **What-to-Ask** strategy
first "select\[s] diagnostic targets" — which facet of the user's expertise
still needs assessment; a **How-to-Ask** strategy then determines "how those
targets are elicited conversationally", i.e. the phrasing of the inquiry.
Slot-filling uses a schema of five dimensions drawn from the Dreyfus model of
skill acquisition (Knowledge Scope, Components, Perspective, Action,
Commitment), and both strategy layers are induced through LLM self-play
rather than hand-written.[^c2]

## Why it matters

This is a stall-2 mechanism that selects an axis outside the query's own
content: the target of the question is the asker's ability, not the world
state the query is about. It is explicitly contrasted with the wiki's other
proactive mechanisms: "Unlike existing studies that focus on proactively
clarifying query ambiguities, we center on clarifying the user's expertise
in order to tailor responses for better user comprehension."[^c3]

Reported gains, against unspecified baselines in the paper's own evaluation:
"+288% in query-level expertise estimation accuracy", "+4.1% on answer
comprehensibility", "+42.5%" kappa (estimate stability) improvement, reached
"with an average of only 1.2 inquiry turns."[^c4]

A passive route to the same variable. Adeseye et al. do not ask about the user's expertise at all; their AI interviewer infers it from the conversation so far. The expertise module works "via previous conversations", with the LLM scoring "technical terminology, insight depth, and academic relevance" against a four-level rubric.[^c5] Their pilot reports levels changing within one interview: "Some participants started as Novices but moved to advanced knowledge".[^c6] My inference, not the paper's: the two routes differ in cost and in what they can see. A probe spends a turn and aims at the facet still unknown; passive inference spends no turn but sees only what the answerer happened to reveal. The Adeseye text read for this note reports no accuracy for its level assignments, so which route tailors questions better is not settled here.

## Transfer

| | |
|---|---|
| **Home field** | skill-acquisition theory (the Dreyfus model): a developmental staging of expertise from novice to expert along several dimensions, over a person's learning history |
| **Here** | a static, per-query assessment schema: the five dimensions become slots a single short dialogue must fill before the current answer is generated |
| **What survives** | the five-way decomposition of "expertise" into separately probeable facets (Knowledge Scope, Components, Perspective, Action, Commitment) |
| **What does not** | the developmental claim itself — that a learner passes through ordered stages over time; PASSING never places a user on that trajectory, it only fills the five slots once |

## Limits

- Single arXiv preprint (2026), read from the paper's own HTML rendering, not
  yet independently verified by this wiki [?]; the reported percentage gains
  are relative to baselines the paper names but this note did not read in
  full, so their absolute size is unknown here.
- The claim that expertise is "difficult to infer from the query text" is
  the paper's own motivating premise, not something this note tests
  independently.
- The Transfer row's account of what survives from the Dreyfus model is this
  note's reading of a schema description, not a claim Cao & Huang make about
  skill-acquisition theory; no primary Dreyfus source was read for this note.

## Related

[[clarification-request]] · [[clarification-benchmarks]] · [[ambiguity-taxonomy]] · [[value-of-information]]

[^c1]: cao-2026
[^c2]: cao-2026 — "select diagnostic targets"
[^c3]: cao-2026
[^c4]: cao-2026 — "+288% in query-level expertise estimation accuracy"
[^c5]: arxiv-2601-11534 — "via previous conversations"
[^c6]: arxiv-2601-11534 — "Some participants started as Novices but moved to advanced knowledge"
