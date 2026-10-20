---
description: "A question-asking policy that forbids the asker from ever advising, Hassan, Aboromi & Unkelos-Shpigel (2026) build **CASELy**,"
aliases: ["non-advisory Socratic dialogue", "CASELy"]
sources: ["hassan-2026"]
---
# Non-advisory Socratic dialogue

> A question-asking policy that forbids the asker from ever advising,
> interpreting or evaluating — only grounded reflective questions and a
> mirrored summary — tested, thinly, as raising a respondent's reported
> experience relative to a non-dialogue control.

## Mechanism

Hassan, Aboromi & Unkelos-Shpigel (2026) build **CASELy**, a[^s1]
conversational agent that helps higher-education students self-assess
social-emotional-learning (SEL) competencies. Its questioning policy is a
hard constraint on what the agent's turns may contain:

```text
1. Extract a structured reading of the respondent's own free-text answer
   (a five-dimension SEL competency analysis).
2. Ask exactly one open, reflective question per turn, worded only from
   the respondent's own prior input.
3. Never advise, recommend, interpret or evaluate the respondent's answer.
4. Close by mirroring the respondent's own language back as a summary,
   adding no synthesis or verdict of the asker's own.
```

The constraint shares one feature with the classical elenchus — the asker
asserts nothing of its own — but not its aim: [[socratic-method]] drives
toward a contradiction the interlocutor must resolve, while this policy
never argues at all; it only reflects.

## Why it matters

In a 4-participant pilot (3 in the dialogue condition, 1 no-dialogue
control), the dialogue group's overall User Experience Questionnaire-Short
(UEQ-S) score was 1.50 against 0 for the control. Semi-structured interviews
with the dialogue participants named three mechanisms for the difference:

1. **Transparency through visible grounding** — the respondent could see the
   agent was working from their own words, not a generic script.
2. **Preservation of user decision authority** — refusing to advise left the
   interpretive judgement with the respondent rather than the agent.
3. **Reduced fear of judgement** — a non-evaluative interlocutor lowered the
   perceived social cost of disclosure.

The mechanism a practitioner can take from this: an asking agent's
trustworthiness is not only a property of what it says, but of what it is
*structurally unable to say* — advice and interpretation withheld by
construction, not by an instruction the agent could ignore.

## Known as

| Field | Name there | Relation |
|---|---|---|
| This paper (HCI / education) | non-advisory Socratic dialogue | `exact` — the paper's own name for the policy |
| This paper's implementation | CASELy | `exact` — the one system tested under that policy |
| Clinical psychology (CBT) | Socratic questioning / guided discovery | **not this concept** — guided discovery still aims at the client constructing a new belief, and [[socratic-method]]'s own Known As records that no evidence there bears on trust or user experience; this note's object is a measured (if thin) trust/UX effect of refusing all advisory content, not a therapeutic technique |

## Transfer

| | |
|---|---|
| Home field | Hassan et al. (2026) frame their design as an application of human–automation trust-[[calibration]] research: a system earns *appropriate* trust when a user's reliance tracks its actual competence, not when trust is simply maximised. **This wiki has not verified that principle against a primary trust-calibration source** — the row reports hassan-2026's own secondhand characterization of the field, not a claim this wiki has traced to the trust-calibration literature itself (see `## Limits` and the corresponding gap). |
| Here | Applied to a question-asking dialogue agent by setting its declared competence to zero interpretive authority; the questioning policy itself (never advise, never interpret) is offered as the mechanism that keeps trust aligned with what the agent actually does. |
| What survives | The framing that visibly bounding a system's outputs to a narrow, checkable function — questions grounded only in the respondent's own words — lets a user judge the system's scope correctly ("transparency through visible grounding"). |
| What does not | The home field's calibration curves — trust tracked against measured system reliability over repeated trials — are absent here. This pilot has no repeated-reliability measure and no numeric trust score, only a one-shot UX questionnaire and three interview themes from three people; no calibration curve is actually computed, only asserted. |

## Limits

- $n=4$ (3 dialogue, 1 control), one higher-education software-engineering
  cohort; the paper itself calls this a pilot and reports no inferential
  statistic. The UEQ-S contrast (1.50 vs 0) is a descriptive difference
  between one respondent's aggregate score and three respondents' aggregate
  score, not a tested effect — it should not be read as "measurably"
  established beyond this one pilot.
- The three trust mechanisms are researcher-coded themes from three
  semi-structured interviews, with no reported inter-rater check.
- Anonymity (randomly generated identifiers) is part of the described setup
  and is not reported as varying between the dialogue and control
  conditions; "reduced fear of judgement" may be partly an effect of
  interacting with any non-human evaluator rather than specifically of the
  non-advisory constraint, and this two-condition pilot does not separate
  the two.
- The `## Transfer` row's "home field" principle (appropriate reliance
  tracking actual competence, not maximised trust) is reported only as
  hassan-2026's own secondhand framing of human–automation trust-calibration
  research; this wiki has not located or read the underlying trust-calibration
  source itself, so the import rests on the paper's characterization of that
  field, not on a primary source this wiki has verified — a gap, not a
  finding.
- Read from the arXiv HTML rendering of `hassan-2026` (arXiv:2609.14818)
  through an automated extraction pass, not from a direct read of an
  archived PDF text layer — section and page numbers are not cited here
  because they were not reliably recoverable this way; `[?]` until the
  verifier confirms against an archived copy.
- Tested in one self-assessment domain (SEL competencies); the paper's own
  framing toward "sensitive domains" generally is the authors' claim, not a
  tested generalisation.

## Related

[[socratic-method]] · [[change-talk-evocation]] · [[abstention]] · [[calibration]]

[^s1]: hassan-2026
