---
description: "Answering is a four-step process, and the question's wording enters at every Tourangeau & Rasinski (1988), formalised in Tourangeau, Rips & Rasinski (2000),"
aliases: ["Tourangeau four-stage model", "response effects", "question wording effects", "response bias", "context effects in attitude measurement", "CASM"]
sources: ["bishop-1986", "rugg-1941", "schuman-1981", "schwarz-1985", "schwarz-1991", "schwarz-1999", "tourangeau-1988", "tourangeau-2000"]
---
# The cognitive model of survey response

> Answering is a four-step process, and the question's wording enters at every
> step. Two phrasings with the same meaning are two different measurements.

## Definition / Mechanism

Tourangeau & Rasinski (1988), formalised in Tourangeau, Rips & Rasinski (2000), model an answer as the output of four stages:[^s1][^s2][^s3][^s4][^s5][^s6][^s7][^s8]

```text
comprehension  what is being asked, and about what
retrieval      which beliefs, episodes, facts come to mind
judgment       combine them into one verdict
response       map the verdict onto the offered format
```

The methodological payload is that **response effects localise to a stage**.
Each documented effect names the stage the wording perturbed:

| Stage | Effect | Evidence |
|---|---|---|
| Comprehension | forbid/allow asymmetry: logically complementary wordings of the same item do not produce complementary answers | Rugg (1941), split-ballot on public speeches against democracy; ~20-point gap |
| Retrieval / judgment | respondents read the **range of the response scale** as the population norm and report frequencies accordingly | Schwarz, Hippler, Deutsch & Strack (1985), TV-viewing frequency |
| Judgment (context) | part–whole order: asking the specific item first changes what the general item means | Schwarz, Strack & Mai (1991); marital/life satisfaction correlation $r = .32$ vs $r = .67$ by order |
| Response | pressure to answer manufactures answers: ~30% report an opinion on **fictitious** legislation; an explicit "no opinion" branch removes most of it | Bishop, Tuchfarber & Oldendick (1986) |

Schuman & Presser (1981) is the experimental catalogue behind this: form,
wording and context varied by split ballot across dozens of items. Schwarz (1999) is the compressed statement — *the questions shape the answers*.

## Why it matters

Three things change for anyone deriving a questioning procedure.

1. **Formulation is not a free variable.** [[twenty-questions]] treats a
   question as a set-partition and the phrasing as cosmetic. Rugg's result is
   that the partition and the phrasing are not separable: the same intended
   split, worded twice, cuts $W$ in two different places. Choosing the axis
   (stall 2) does not determine the question.
2. **An answer is a joint product of the world and the instrument.** A
   constraint recorded without the question that produced it is not
   reconstructible ([[constraint-as-information]]). The literal wording, the
   offered options, and the position in the sequence are all part of the
   datum.
3. **Forcing an answer creates a fake constraint.** Bishop et al. is the
   cleanest case of a question that returns confident content about nothing.
   An asking procedure that always requires an answer will narrow $W$ on
   noise; an explicit "don't know / not decided" branch is the defence, and it
   is a design choice at formulation time, not a repair afterwards.

The only measurement instrument the field offers is the **split ballot**:
randomise the wording across respondents and read the difference as the
instrument's contribution. A single wording asked once gives no way to
separate the answer from the question.

## Transfer

| | |
|---|---|
| **Home field** | attitude and behaviour self-reports, standardised instrument, lay respondent, no dialogue |
| **Here** | an agent asking a human one clarification question inside a task |
| **What survives** | the four stages as a diagnostic for *where* a bad answer went wrong; the range-of-options effect (an agent's offered options are a response scale); the order effect; "no opinion" as a required branch |
| **What does not** | effect magnitudes — they are item- and population-specific; and the split-ballot remedy, which needs many respondents and so is unavailable to an agent asking one person once |

## Limits

- The four-stage model is a framework: it says where an effect lives, not its
  sign or size. It predicts nothing about a new item.
- The evidence is strongest for attitude items with no fact of the matter.
  Whether a designer answering "should this be idempotent?" is equally
  malleable is untested here.
- Several context effects come from the social-cognition tradition of the
  1980s–90s; individual replication strength varies by item, and the
  literature reports both assimilation and contrast from the same
  manipulation depending on conversational framing (Schwarz, Strack & Mai
  1991 is itself an account of that instability).
- The transfer to an LLM *answerer* is not covered by any of these sources.

## Related

[[constraint-as-information]] · [[tacit-knowledge]] · [[elicitation-protocols]] · [[ambiguity-taxonomy]] · [[twenty-questions]] · [[grand-tour-question]]

[^s1]: bishop-1986
[^s2]: rugg-1941
[^s3]: schuman-1981
[^s4]: schwarz-1985
[^s5]: schwarz-1991
[^s6]: schwarz-1999
[^s7]: tourangeau-1988
[^s8]: tourangeau-2000
