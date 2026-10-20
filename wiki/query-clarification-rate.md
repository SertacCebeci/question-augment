---
description: "The proportion of transactions in which the answerer asks anything at all The quantity is the share of transactions containing **at least one question intended to find out more about the user's inf…"
aliases: ["clarification rate", "rate of query negotiation", "reference interview occurrence"]
sources: ["dewdney-1994", "gers-1985", "radford-2011", "ross-2004"]
---
# Query clarification rate

> The proportion of transactions in which the answerer asks anything at all
> about the question before answering it. Measured on professional reference
> staff since the mid-1980s, it sits near a half face-to-face.

## Definition / Mechanism

The quantity is the share of transactions containing **at least one question[^s1][^s2][^s3][^s4]
intended to find out more about the user's information need** — the coding
criterion used in the Library Visit Study, which counts well-formed open
questions, closed questions such as "Are you writing a paper on this topic?",
and even a strategic repetition of the user's key words (Nilsen 2004).

| Setting | Rate | Source |
|---|---|---|
| Face-to-face reference encounters | clarification in 49% | Gers & Seward (1985) `[?]`, as reported by Radford et al. (2011) |
| Library Visit Study, physical desks (261 visits, phases 1–2) | 49% overall; 51% in 1991–93, 48% in 1998–2000 | Nilsen (2004); phase-1 figure from Dewdney & Ross (1994), via Radford et al. |
| Virtual reference desk (42 reports, 2003) | 20% | Nilsen (2004) |
| Live chat, 592 QuestionPoint transcripts sampled from 651,687 sessions (2004–06) | librarians 74% (436); users volunteered clarification in 23% (136); 96% (568) of interactions offered an opportunity | Radford et al. (2011), fig. 1 |
| Of 854 clarifying questions librarians asked in that corpus | 33% open (285), 67% closed (569) | Radford et al. (2011) |
| Follow-up ("Does this completely answer your question?") | asked in 12% of encounters | Gers & Seward `[?]`, via Radford et al. |
| Follow-up variants | 37% face-to-face (Dewdney & Ross, via Radford et al.); 50% (219 of 436 clarifying librarians) in chat | Radford et al. (2011) |
| Answerer verifies its understanding back to the asker | 20% (87 of 436); corrects a misunderstanding 2% (7) | Radford et al. (2011), fig. 4 |

**What the rate buys.** Radford et al. report Gers & Seward as finding that
"librarians who do not negotiate the query almost never provide a correct
answer, while those who do negotiate provide a correct answer 62 percent of
the time," and that closing with the follow-up question raises correctness to
76% against 52% without it. In the chat corpus the association is reported as
a decomposition of the *correct* answers: of 98 correctly answered
ready-reference questions, 73% (72) had been clarified, 21% (21) had not, and
5% (5) needed no clarification (fig. 8). Across all 134 usable ready-reference
questions, librarians who clarified answered correctly 54% (72) of the time
and incorrectly 18% (24).

## Known as

| Name | Field | Relation |
|---|---|---|
| clarification rate | LIS | exact — the same proportion |
| rate of query negotiation | LIS | exact — the quantity named after Taylor's term for the process being counted |
| reference interview occurrence | LIS | exact — the Library Visit Study's own coding label for the numerator |
| clarification rate | dialogue evaluation | close — same name, computed on labels of when a question *was* needed, not on all transactions |
| ask-rate | LLM evaluation | close — *not* this concept: scored against ambiguity labels ([[clarification-benchmarks]]), a denominator this quantity does not use |
| query clarification, clarification request | IR, dialogue systems | *not* this concept — the move ([[clarification-request]]), not its frequency |

## Why it matters

1. **This is the field's actual answer to "does the interview recover the
   need".** It does not measure [[recovery-postulate|recovery]]. It measures *occurrence* of a
   clarifying move and correlates it with downstream answer accuracy. No study
   read here scores the recovered question against the asker's need, so
   [[levels-of-information-need]] remains untested from this direction.
2. **A low ask-rate is not an LLM artefact.** [[clarification-benchmarks]]
   records that models detect [[efe-planning-as-variational-inference|ambiguity]] and answer anyway. Trained professional
   answerers, whose job is the interview, clarify in about half of
   face-to-face encounters and use open questions in a third of their
   clarifications. Any mechanism proposed for the model deficit
   ([[preference-signal-against-asking]]) must explain why the human rate is
   similar ([[throughput-pressure-on-asking]]).
3. **The cheapest measured move is the last one, not the first.** The follow-up
   question is a single closing utterance with the largest reported accuracy
   difference (76% vs 52%) and one of the lowest observed rates (12%–50%).
4. **The answerer almost never displays its reading.** Verification of
   understanding at 20% and self-correction at 2% put a ceiling on how often
   an asker could catch a mis-recovered question before the answer arrives.

## Transfer

| | |
|---|---|
| **Home field** | evaluation of library reference service: trained professional answerers, a countable transaction, and coders working from transcripts or participant-observer reports |
| **Here** | any answerer's ask-rate — the share of received questions on which it asks something back before answering |
| **What survives** | the definition of the quantity (at least one question about the need, asked before the answer); the decomposition by form (open vs closed) and by stage (before, during, after the search); the follow-up question as a separately countable move; the practice of pairing the rate with a downstream correctness measure |
| **What does not** | comparability of the numbers — different instruments, denominators and decades; and the causal reading, since no design randomises clarification. The population is also specific: paid professionals whose role is the interview, only part of whom (the 2004–06 chat corpus) worked under a written behavioural standard |

## Limits

- **The Library Visit Study figures are cited under the key `ross-2004`; the
  2004 write-up is single-authored by Kirsti Nilsen.** Ross led earlier phases
  of the project and co-authored the 1994 phase-1 report, but is not an author
  of this article; in-text attribution here is to Nilsen.
- **Gers & Seward (1985) is `[?]` — unverified.** No official listing, DOI or
  accessible copy was found; the article is corroborated only by secondary
  bibliographies, including Radford et al.'s reference 15. Its figures (49%,
  62%, 76% vs 52%, follow-up in 12%) and the "almost never provide a correct
  answer" characterisation are quoted from Radford et al.'s literature review,
  not from the 1985 article. Every number attributed to Gers & Seward above
  carries that qualification.
- **The chat accuracy figures are not a rate comparison.** Figure 8 partitions
  the 98 *correct* answers by whether clarification occurred; Radford et al.
  report no matching partition of the incorrect ones, so 73% vs 21% is not
  "accuracy with clarification vs without". Only the 54%/18% pair shares the
  134-question denominator.
- **Rates across rows are not comparable.** The face-to-face figures come from
  participant-observer visits with small samples and self-generated questions;
  the 74% comes from post-hoc coding of a large random transcript sample.
  Radford et al. say so explicitly and attribute part of the difference to
  method rather than to behaviour.
- The denominator moves: Radford et al. exclude 258 of 850 transcripts that
  offered no opportunity to clarify, and the Library Visit Study counts a
  strategic repetition as an interview.
- **The accuracy association is not causal.** Nothing in these designs
  randomises clarification; librarians who clarify may differ in every other
  respect, and Radford et al. could restrict the accuracy analysis only to 134
  ready-reference questions with verifiable answers — the questions least in
  need of an interview.
- The claim in point 1 — that recovery is unmeasured — is a claim about the
  sources this cell read, not a proof that no such study exists.

## Related

[[levels-of-information-need]] ·
[[clarification-benchmarks]] · [[negative-closure]] ·
[[preference-signal-against-asking]] · [[willingness-to-return]]

[^s1]: dewdney-1994
[^s2]: gers-1985
[^s3]: radford-2011
[^s4]: ross-2004
