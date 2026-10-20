---
description: "A question can arrive **well-formed and wrong**: not vague, not compromised, Dewdney & Michell (1996) apply linguistic analysis to reference questions as initially presented and sort the failures i…"
aliases: ["communication accidents"]
sources: ["dewdney-1996", "radford-2011"]
---
# Communication accident

> A question can arrive **well-formed and wrong**: not vague, not compromised,
> but a corrupted token the asker cannot repair either — because the asker is
> faithfully repeating someone else's error, or has rebuilt a term it forgot.

## Definition / Mechanism

Dewdney & Michell (1996) apply linguistic analysis to reference questions as[^s1][^s2]
initially presented and sort the failures into four kinds of **communication
accident**:

| Kind | What went wrong |
|---|---|
| Simple failure of hearing | the channel dropped or altered the string |
| Pronunciation or homophone | the asker's rendering maps onto a different word the answerer knows |
| Secondhand | the asker repeats to the answerer a misinterpretation made earlier, by someone else |
| Creative reconstruction | the asker has forgotten the term and rebuilds a plausible substitute for it |

The last two are the load-bearing ones, because in both the asker is not
uncertain: it is confidently transmitting a token that is already wrong, and
the token is well-formed enough that nothing in the utterance flags it. The
remedies the paper discusses are **restatement** — playing the received
question back — together with neutral and follow-up questioning.

The accident survives into the search when it is never played back. Radford et al. (2011) record a live-chat instance in which a user asking about starting
*driving* classes at fifteen mistyped the word as *diving*; the librarian
searched, reported several minutes later on when scuba diving classes are
appropriate, and the user had to correct the answerer. The authors observe that
a single clarification — scuba diving or sky diving? — would have exposed the
typo immediately. In the same corpus, librarians verified their understanding
back to the user in 20% (87 of 436) of their clarifications and corrected a
misunderstanding in 2% (7).

## Known as

| Name | Field | Relation |
|---|---|---|
| communication accident | library and information science | exact — Dewdney & Michell's term |
| mishearing, mondegreen | linguistics, folklore | *not* this concept — those name the corrupted string; the accident here includes the secondhand and reconstructed cases in which no one misheard anything at the desk |
| clarification request | dialogue systems | *not* this concept — the repair move ([[clarification-request]]), not the failure it repairs |

"Query corruption in transmission" is this note's own gloss on the mechanism,
not a term any field uses; no source read here names the object that way.

## Why it matters

1. **It is a third deformation, and it needs a different repair.**
   [[levels-of-information-need]] has the asker compress a need toward what it
   thinks the answerer stocks; [[efe-planning-as-variational-inference|ambiguity]] has the wording underdetermine the
   need. Here the wording is determinate and false. Eliciting the situation and
   the use (neutral questioning) will not surface it; playing the received
   string back will.
2. **The asker cannot be the check.** In a secondhand accident the asker is
   relaying an imposed query — 26% of the 592 analysed chat transcripts were
   imposed queries, and in a further 46% the origin of the question was never
   established either way — so asking "is this what you meant?" gets a sincere
   yes.
3. **Fluency defeats most of the level-typed confidences.** An answerer that
   parses the corrupted token successfully proceeds with maximum confidence.
   Read against Schlangen's levels in [[clarification-request]], the failure
   passes the contact, recognition, parsing and reference-resolution
   confidences alike, because the received string is well formed and resolves;
   the one level-typed confidence that can fire on it is **contextual
   relevance** — the same check point 4 names.
4. **The cheap detector is plausibility, not comprehension.** The observed
   catch is a semantic oddity check — a 15-year-old and diving classes — and
   verification back to the asker, which is done in a fifth of clarifications.

## Transfer

| | |
|---|---|
| **Home field** | face-to-face public library reference: an acoustic channel between strangers, a collection whose vocabulary the asker does not share, and a librarian who can restate immediately |
| **Here** | any answerer receiving a written or transcribed question, including one relayed through a form, a ticket, an agent, or a speech recogniser |
| **What survives** | the four-way split, with typing and transcription errors taking the place of mishearing; the two cases in which the asker cannot repair the string; the restatement remedy |
| **What does not** | the acoustic repair cues (prosody, immediate "sorry?") and the co-presence that makes restatement free; and the coverage claim — the taxonomy was built on desk transcripts, and no source read here reports how often each kind occurs |

## Limits

- The 1996 article was not read in this pass. The four categories are taken
  from its published abstract, which names them; no counts, no coder
  agreement and no examples from it are claimed here.
- Radford et al. (2011) is confirmed to exist and to report clarification,
  follow-up and openness rates, but the granular counts used here — the 87 of
  436 verifications, the 7 corrections, and the imposed and origin-undetermined
  counts — and the diving/driving transcript could not be checked against the
  paper's full text this pass `[?]`.
- The chat example is a single documented instance in a paper about something
  else. It shows the mechanism is live in text; it establishes no rate.
- The taxonomy is a classification of failures observed at a desk, not a
  detector: nothing here tells an answerer which received strings to distrust,
  and the plausibility check in point 4 is this wiki's reading of the example,
  not a method either source proposes.
- Point 3 is this wiki's reading of Schlangen's level taxonomy applied to this
  failure mode — which levels a corrupted-but-fluent token passes is an
  inference here, not a claim of either cited source.
- Point 2 joins Dewdney & Michell's secondhand category to Radford et al.'s
  imposed-query counts; the two literatures are not linked by either source.

## Related

[[levels-of-information-need]] ·
[[clarification-request]] · [[query-clarification-rate]] ·
[[third-position-repair]]

[^s1]: dewdney-1996
[^s2]: radford-2011
