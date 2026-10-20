---
description: "A code-assessment chatbot splits asking from grading into two agents, grounds questions in static/dynamic analysis facts, and follows up only when the grader flags an answer as vague."
aliases: ["Hybrid Socratic Framework"]
sources: ["arxiv-2604-07304"]
---
# Code-fact-grounded Socratic assessment

> Ask nothing the code-analysis engine didn't already prove, and only
> follow up when the grader itself flags the answer as too vague to be
> a real explanation.

## Definition / Mechanism

Frankford et al. (2026) propose a "Hybrid Socratic
Framework" for verifying, by chatbot, that a student who submitted
functionally-correct code actually understands it. Three design choices
make its asking distinct from a generic explain-your-code prompt.

First, questioning and grading are two separate agents rather than one
model call doing both: splitting the generative task into two
specialized agents separates questioning from evaluation — an
**Instructor Agent** formulates each Socratic question from facts a
static/dynamic analysis engine extracted from the student's own
submission (a specific variable update, branch condition, loop
boundary, or runtime state), and a **Verifier Agent** compares the
student's answer against a reference reason grounded in those same
facts. The purpose is "to turn deterministic evidence from the
code-analysis layer into guided questioning that triggers explanation
rather than solution copying."[^c1]

Second, what to ask next is driven by a persistent per-student tracker,
not a fixed question order: the State Space and Knowledge Tracker
"maintains a persistent model of the student's understanding by
tracking knowledge components and misconceptions across turns" — e.g.
a student who explains variable scope but not pointer arithmetic is
steered toward pointer-arithmetic follow-ups next.[^c2]

Third, a follow-up question is issued only on a specific trigger from
the grading agent, not on every turn or a fixed hint ladder: "when the
Verifier Agent detects vague or generic language, the Instructor Agent
should issue a follow-up that narrows the reasoning space, such as
changing the input, asking for the next trace state, or focusing on a
specific branch."[^c3]

The measure that closes the loop is a two-tier score that makes a
correct multiple-choice selection alone insufficient: "Score = 20 +
(Similarity × 0.8)," so the base 20 points from Tier 1 (selection)
caps well below a passing grade unless the Tier 2 free-text explanation
also scores well against the grounded reference.[^c4]

## Why it matters

This differs from [[argument-grounded-socratic-questioning]] in what
the question is grounded in — deterministic program-execution facts
from a code-analysis engine rather than a mined argument graph — and
in what gates a follow-up: there, the writer's own verbalization closes
a thread; here, the *grader's* vagueness detection *opens* one. It
overlaps with [[decision-centric-design]] in separating a
signal-producing component from the component that acts on it, but
splits along a different seam — asking versus grading, rather than
sufficiency-estimate versus action-policy — and the split's purpose is
explicitly anti-gaming: a runtime-specific, potentially randomized
question is harder for a student to answer by pasting the question
into another LLM than a generic "why does your code work?" would be.

## Limits

- The framework is proposed, not evaluated: "the proposal is intended
  as a design synthesis rather than a validated end product."[^c5]
- The proof of concept is a demo, not a study: it "does not yet
  constitute a production-ready APAS component," lacks integration
  with deterministic unit/regression testing, has limited language
  support, and has seen no classroom deployment.[^c6]
- No measurement exists yet of whether fact-grounding or the
  vagueness-triggered follow-up actually reduces copy-pasted or
  LLM-generated explanations relative to an ungrounded baseline — the
  anti-gaming claim is the paper's design rationale, not a result.
- The "vague or generic language" trigger and the knowledge tracker's
  misconception-prioritization rule are stated as prompt instructions
  to the LLM agents, not as a separate classifier with its own
  accuracy figure — their reliability is unverified.

## Related

[[argument-grounded-socratic-questioning]] · [[decision-centric-design]]
· [[socratic-method]] · [[gated-socratic-scaffolding]] ·
[[staged-socratic-hint-policy]]

[^c1]: arxiv-2604-07304 — "The overall purpose of the prompt is therefore to turn deterministic evidence from the code-analysis layer into guided questioning that triggers explanation rather than solution copying."
[^c2]: arxiv-2604-07304
[^c3]: arxiv-2604-07304
[^c4]: arxiv-2604-07304 — "Score = 20 + (Similarity × 0.8)"
[^c5]: arxiv-2604-07304 — "The proposal is intended as a design synthesis rather than a validated end product."
[^c6]: arxiv-2604-07304 — "It demonstrates the end-to-end conversational flow, but it does not yet constitute a productionready APAS component."
