---
description: "\"Probably\" is a private number. Its mapping to $[0,1]$ is stable inside one Wallsten, Budescu, Rapoport, Zwick & Forsyth (1986) measured the meaning of terms such as *doubtful*, *probable*,"
aliases: ["words of estimative probability", "WEP", "linguistic probabilities", "probability phrases", "vague probability terms", "verbal probabilities"]
sources: ["budescu-1985", "budescu-2009", "budescu-2012", "erev-1990", "karelitz-2004", "kent-1964", "mandel-2021", "tang-2024", "teigen-1999", "wallsten-1986", "wintle-2019"]
---
# Verbal probability expressions

> "Probably" is a private number. Its mapping to $[0,1]$ is stable inside one
> speaker and not shared between two, so a hedged answer is not yet a
> constraint.

## Definition / Mechanism

Wallsten, Budescu, Rapoport, Zwick & Forsyth (1986) measured the meaning of[^s1][^s2][^s3][^s4][^s5][^s6][^s7][^s8][^s9]
terms such as *doubtful*, *probable*, *likely* as **membership functions** over
the $[0,1]$ probability interval: $\mu_W(p)$ is the degree to which
probability $p$ belongs to the vague concept named by word $W$. Using a
pair-comparison procedure over spinners, they recovered a function per term
per subject; the derived values predicted the same subjects' judgments in an
independent task. Their result on the shape of the disagreement is the
load-bearing one: **individual differences were large but stable.**

Budescu & Wallsten (1985) is the split behind that: within-subject
variability in assigning numbers to phrases is real but considerably smaller
than between-subject variability. Kent (1964), working on National
Intelligence Estimates, had found the same failure operationally — readers
of the same word *probable* took it as ~75% and as ~30% — and proposed a
fixed lexicon as the fix.

Three further findings constrain what any fix can be.

| Finding | Source |
|---|---|
| A published lexicon does not repair reading. Readers of 2007 IPCC sentences assigned numbers that departed from the IPCC guidelines **even with the guidelines in hand**, misreading the statements regressively (toward the middle). | Budescu, Broomell & Por (2009) |
| What does help is a **dual verbal–numerical** presentation: it raises differentiation between terms, consistency across readers, and agreement with the guideline — independent of the reader's ideology. | Budescu, Por & Broomell (2012) |
| **Communication mode preference paradox**: senders prefer to emit words, receivers prefer to receive numbers. Format is contested between the two ends of the same channel. | Erev & Cohen (1990) |
| **Directionality**: phrases are positive ("some chance") or negative ("quite uncertain"). Two phrases judged to carry the *same* numeric probability drive opposite decisions and predictions. | Teigen & Brun (1999) |

Karelitz & Budescu (2004) show the translation route: convert a sender's
phrase through the sender's own lexicon into the receiver's, rather than
through a shared standard.

## Why it matters

An answer of "probably" cannot enter a likelihood ratio, an EIG update or a
stopping threshold ([[constraint-as-information]], [[likelihood-ratio]]).
Three consequences for a questioning procedure:

1. **Do not resolve a hedge by decree.** Stipulating a lexicon in the prompt
   is exactly the intervention Budescu et al. (2009) tested and found weak.
   The measured remedies are per-speaker translation (Karelitz & Budescu) or
   dual format.
2. **Ask for word and number together.** The CMP paradox says a schema that
   accepts only words gets replies the asker cannot use, and one that accepts
   only numbers fights the answerer's default. Both fields, or the constraint
   is lost.
3. **The polarity of the asker's own hedge is a design variable.** Teigen &
   Brun's directionality effect operates at fixed probability, so an agent
   reporting its own uncertainty picks the user's decision by choosing the
   phrase — the answer-side analogue of the wording effects in
   [[survey-response-model]].

For an LLM answerer, Tang, Shen & Kejriwal (2024) find that GPT-3.5 and GPT-4
align with human numeric interpretations for some estimative words and not
others, with divergence under Chinese-language and gendered-role contexts.
The word→number map is not safe to assume even between two models.

## Transfer

| | |
|---|---|
| **Home field** | lay or expert readers assigning numbers to decontextualised probability phrases, or reading a published report; many respondents, one direction |
| **Here** | an agent receiving one hedged reply from one answerer inside a task, and emitting hedges of its own |
| **What survives** | the stability/sharedness split (a per-answerer lexicon is learnable, a universal one is not); the failure of stipulated guidelines; dual format; directionality as a wording variable |
| **What does not** | the numeric peaks of any published lexicon — they are population- and context-specific; and the measurement itself, which needs repeated elicitation the agent has no budget for on the first hedge |

## Limits

- Correction to the dual-format row: in an experiment with N = 1,202 readers of the NATO five-term scheme, the combined verbal+numeric format beat verbal-only on three agreement measures, but the purely numeric format was just as good as the combined one; omitting the words cost nothing, omitting the numbers cost agreement.[^s10] Verbal-only answers were also pulled to 50%: those readers were 6.4 to 9.0 times as likely to give a "fifty-fifty" best estimate, which can mean either a first-order probability or "I don't know", so a 50% in a verbal channel is ambiguous.[^s11] Only the range-dependent overlap measure gained from numerically bounding a verbal scheme.[^s12] Read together with Budescu et al., the dual format works because of its numbers (this reading is the note's own inference).
- Placement of the numbers matters, not only their presence (Wintle et al. 2019, 924 readers of ICD 203 statements): bracketing the numeric range in the text raised overlap with the intended range to 66% against 32% for words alone, while a click-through table or a hover tooltip reached only about 40%.[^s13] Readers mostly did not use guidelines kept one step away: 47% of the Table group clicked at all, and the Tooltip group's 46% reported using it.[^s14] Even restricted to active users the gain stayed below the bracketed one (44% and 49%).[^s14] The numbers have to sit in the answer itself; this is the note's own reading of those results.
- Membership functions are context-sensitive: Budescu, Por & Broomell (2012)
  review evidence that the same term's numeric reading moves with the event's
  perceived base rate and severity. A lexicon learned on one topic does not
  transfer to another.
- Most of this evidence is elicited numbers, not behaviour. Teigen & Brun
  (1999) is the exception that shows the decision moving.
- The dual-format result was obtained on readers of a report, not on a
  dialogue partner asked once; no source here tests it in interactive
  clarification.
- Tang et al. (2024) test how a model *reads* estimative words. Whether a
  model's emitted hedge faithfully tracks its own internal probability is not
  established by any source in this note.
- Kent (1964) is a practitioner's essay in *Studies in Intelligence*, not a
  controlled study; it is cited here for the operational failure, not for the
  percentages.

## Related

[[calibration]] · [[survey-response-model]] · [[elicitation-protocols]] · [[constraint-as-information]] · [[likelihood-ratio]] · [[semantic-entropy]]

[^s1]: budescu-1985
[^s2]: budescu-2009
[^s3]: budescu-2012
[^s4]: erev-1990
[^s5]: karelitz-2004
[^s6]: kent-1964
[^s7]: tang-2024
[^s8]: teigen-1999
[^s9]: wallsten-1986
[^s10]: mandel-2021 — "agreement using the purely numeric format was just as good as the combined format"
[^s11]: mandel-2021 — "by increasing the proportion of fifty-fifty responses, verbal probabilities increase ambiguity"
[^s12]: mandel-2021 — "only one (based on the proportion"
[^s13]: wintle-2019 — "correspondence was 66%, compared with 32% in the control"
[^s14]: wintle-2019 — "only 91 of 200 participants (46%) in the Tooltip condition"
