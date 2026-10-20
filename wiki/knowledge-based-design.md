---
description: "Self-, user- and context-knowledge requirements that gate a tutoring robot's Socratic questioning and slide-grounded feedback, validated by a manipulation check and a responsible-behavior scale."
aliases: ["KBD", "knowledge-based design"]
sources: ["vonschallen-2026"]
---
# Knowledge-based design

> Which knowledge a tutoring robot has access to — about itself, the
> learner, and the material — determines which asking strategy it uses at
> each turn: a robot built from three named knowledge categories used
> [[staged-socratic-hint-policy|Socratic]] questioning, slide-grounded explanation and feedback far more
> consistently than an otherwise identical robot without them.

## Definition / Mechanism

Vonschallen, Kaufmann & Oberle (2026) operationalize a
prior Knowledge-Based Design (KBD) framework into Teachy Mini, a tutoring
robot on the Reachy Mini platform. KBD sorts the information a tutoring
agent needs into three categories that jointly gate its behavior: "the
robot's role should be adaptive, with the default being a study buddy...
the robot's user-knowledge should encompass learner-specific information
such as learning goals, learning progress, motivation type, emotional
state, academic background, and preferred learning style... the robot
should have context-knowledge about official learning materials,
course-related information, educational strategies, and... the physical
learning environment."[^c1]

Context-knowledge is what licenses Socratic questioning as an asking
strategy rather than mere personalization: "the robot was instructed to
use scaffolding strategies, including Socratic questioning (i.e.,
questions that guide learners to examine their reasoning and think for
themselves), targeted hints, simplified explanations, and corrective
feedback." The three knowledge types are delivered by dynamic system
prompting (self-knowledge, stable role instructions), retrieval-augmented
generation over uploaded lecture slides (context-knowledge), and regex-
triggered stateful prompt injection keyed to onboarding answers and
detected conversational states such as confusion (user-knowledge).[^c2]

## Findings

In a two-group between-subjects study (N = 24), a qualitative manipulation
check coded 655 transcript segments from six sessions and found the KBD
condition used Socratic questions far more than the non-KBD control robot
built on the same platform and language model: "Socratic Question [KBD:
116; CTRL: 1]."[^c3]

On the study's own Responsible Behavior scale, the KBD group scored
significantly higher than control: "The KBD group (M = 5.49, SD = 1.23)
reported significantly higher perceived alignment with responsible robot
behavior than the control group (M = 4.47, SD = 0.95), t(20.65) = 2.277,
p = .034, CI = [0.087, 1.950], d = 0.930. H4 was therefore supported." An
exploratory path model found this perceived alignment, not KBD directly,
predicted motivation and acceptance.[^c4]

None of the three other pre-registered hypotheses reached significance:
system acceptance showed "no significant difference between conditions,
t(19.43) = 0.057, p = .955... H1 was therefore not supported," and
objective/subjective learning effectiveness were likewise not supported
(N = 24 is underpowered against the study's own a priori power target of
42).[^c5]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Educational-agents (this paper) | Knowledge-Based Design (KBD) | exact — the abbreviation this wiki uses as the concept's title. |

## Why it matters

This is a case where the axis a tutoring agent asks about next is not
chosen by a value function over answers (as elsewhere on this stall) but
gated by which of three named knowledge categories the system currently
holds: no context-knowledge (slides) means no Socratic follow-up, only
generic explanation. The behavioral gap is measured directly (655 coded
segments), while the downstream benefit — beyond perceived responsible
behavior — is not, in a 24-participant preliminary trial.

## Transfer

| | |
|---|---|
| **Home field** | Responsible-AI design frameworks (Value Sensitive Design, AI for Social Good): abstract ethical principles for what a system should uphold. |
| **Here** | KBD translates "responsible tutoring" into three concrete, checkable knowledge holdings (self/user/context) that a system prompt and RAG pipeline can instantiate turn by turn. |
| **What survives** | The mapping from principle to knowledge category to observable behavior held up under a manipulation check: the KBD robot's transcripts differ from the control's in exactly the coded categories the framework names. |
| **What does not** | The chain from "more consistent Socratic questioning" to better acceptance, motivation, or learning is not established here — three of four hypotheses were null in this sample. |

[^c6]

## Limits

- N = 24, one institution, one domain (research-methods slides), one
  language (German); the authors call the study preliminary and the
  sample underpowered for its own a priori target of 42.
- The manipulation check coded only 6 of 24 transcripts (3 per condition)
  for illustrative, not statistical, purposes — the 116-vs-1 Socratic
  count is a qualitative contrast, not a tested effect size.
- The KBD framework's origin (self-/user-/context-knowledge as the
  complete and correct partition) is attributed to the authors' own prior
  interview study, cited here but not independently read by this wiki.
- Only H4 (perceived responsible behavior) was supported; learning,
  motivation and acceptance gains are not shown, so "used more
  consistently" should not be read as "worked better."

## Related

[[gated-socratic-scaffolding]] · [[state-gated-strategy-routing]] · [[socratic-method]] · [[value-of-information]]

[^c1]: vonschallen-2026
[^c2]: vonschallen-2026 — "The robot was instructed to use scaffolding strategies, including Socratic questioning (i.e., questions that guide learners to examine their reasoning and think for themselves), targeted hints, simplified explanations, and corrective feedback."
[^c3]: vonschallen-2026 — "Socratic Question [KBD: 116; CTRL: 1]"
[^c4]: vonschallen-2026 — "The KBD group (M = 5.49, SD = 1.23) reported significantly higher perceived alignment with responsible robot behavior than the control group (M = 4.47, SD = 0.95), t(20.65) = 2.277, p = .034, CI = [0.087, 1.950], d = 0.930. H4 was therefore supported."
[^c5]: vonschallen-2026
[^c6]: vonschallen-2026
