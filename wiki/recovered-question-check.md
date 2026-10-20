---
description: "Every question-[[recovery-postulate|recovery]] procedure this wiki has read reads the question off"
aliases: ["draft-recovered question divergence check"]
sources: ["ko-2023", "riester-2019", "wu-2023"]
---
# Recovered-question check

> Every question-[[recovery-postulate|recovery]] procedure this wiki has read reads the question off
> the text that answers it. This wiki's inference: the answerer cannot use one
> to fix the question *before* replying — but it can draft a reply, recover the
> question that draft answers, and compare.

## Definition / Mechanism

**The observation the conjecture rests on.** In [[qud-parsing]] the question[^s1][^s2][^s3]
model is $P_q(q_i \mid D, i, a_i)$ — conditioned on the answer sentence and its
anchor. In [[qud-licensing-constraints]] the constraints select a question from
the given material of the assertion that answers it, and Parallelism needs two
answers before it applies. In [[question-under-discussion]] the question is
whatever the discourse must have been committed to for the moves made to have
been Relevant. All three are **retrodictive**: they take produced text and name
the question it answers. None takes a received question and returns the
question meant.

**The proposed inversion** (this wiki's, untested):

1. the answerer drafts a reply $r$ to the received question $u$;
2. it runs a question-recovery step over (context, $r$) and obtains $\hat q$ —
   the question the draft actually answers;
3. it compares $\hat q$ with $u$, and separately checks $\hat q$ against the
   licensing filter: a $\hat q$ containing material the exchange never supplied
   means the draft answered a question the answerer invented;
4. on divergence it clarifies, naming the divergent slot, or states $\hat q$ in
   the reply so the asker can repair it.

The quantity the design needs is the divergence between two natural-language
questions, and no note in this wiki supplies it; [[semantic-entropy]] clusters
*answers* by entailment, not questions.

**Why this is worth the draft.** The comprehension check the wiki has —
[[third-position-repair]] — is structurally unavailable until an answer exists
and the asker has read it. Step 2 needs an answer to exist but not to be sent,
so it converts a defence that lives one turn later into a check that runs
before commitment. It also supplies a candidate for the cut point
[[clarification-request]] leaves open: the trigger is not a scalar confidence
over parsing stages but a mismatch between the received and the recovered
question.

## Known as

| Name | Field | Relation |
|---|---|---|
| draft-recovered question divergence check | this wiki | exact — the four steps above named from what they do: recover the question a draft answers, then measure its divergence from the received one |
| answer-anchored question recovery | computational linguistics | *not* this concept — the property of the recovery procedures in [[qud-parsing]] and [[qud-licensing-constraints]] that step 2 consumes; this note is the inversion built on top of it |
| self-consistency / sampled agreement | LLM evaluation | *not* this concept: agreement among sampled *answers*, which is silent when every sample answers the same wrong question |
| round-trip / back-translation check | machine translation | analogy — *not* this concept: the round trip is scored by similarity of the regenerated source text, and its failure mode is paraphrase, not mis-accommodation |
| QUDeval | NLP evaluation | *not* this concept — a benchmark that scores generated QUDs against answer compatibility, givenness and anchor relevance; it measures the recovery step this check would consume |

## Why it matters

1. **It makes the wiki's stated hole actionable.**
   [[question-under-discussion]] names mis-[[presupposition-accommodation|accommodation]] as a failure with no
   detector. The conjecture says a detector cannot be built in the direction
   the stall suggests (question in, reading out) from the procedures the wiki
   has, and names the direction in which one already exists.
2. **It is falsifiable.** Prediction: on questions with a false premise or an
   unstated contrast class, an answerer running steps 1–3 flags cases that an
   input-side confidence threshold does not, because the leak shows up in the
   draft rather than in the wording ([[clarification-benchmarks]]).
3. **It prices itself honestly.** The check costs a full draft before the
   decision to ask back — a cost [[decision-theoretic-grounding]]'s
   [[value-of-information]] accounting does not carry, since it observes evidence,
   not its own output.

## Transfer

| | |
|---|---|
| **In its home field** | computational discourse analysis: a finished document, offline, questions recovered to describe how sentences hang together |
| **Here** | an answerer's self-check on an unsent draft, used to decide between sending, disclosing the reading, and asking back |
| **What survives** | the retrodictive direction and the two evaluation criteria that come with it — is the recovered question reasonable given the prior context, and does the text actually answer it |
| **What does not** | the accuracy: Ko et al.'s parser produces implausible questions about 28.5% of the time on in-domain news and worse out of domain, and Wu et al.'s QUDeval finds systems rarely satisfy answer compatibility, givenness and anchor relevance at once — so the check as specified inherits a false-alarm rate large enough to swamp the effect it is looking for |

## Limits

- **This is a conjecture, and the load-bearing part is the inference, not any
  result.** No cited source runs the loop, and neither Ko et al. nor Riester
  considers an answerer. Nothing here should be read as a finding.
- The claim "every procedure is retrodictive" covers the three procedures this
  wiki has read, not the field. Ko et al. themselves point to a prospective
  paradigm — questions elicited *without* seeing the upcoming context, in the
  expectation-driven tradition — which this pass did not read; if a working
  prospective recovery model exists, the premise of step 1 falls and the check
  becomes unnecessary rather than merely unproven.
- Step 3 has no metric. Without a divergence measure over questions the
  procedure is a shape, not an algorithm, and comparing question *strings*
  would fail on the synonymy Riester says is unavoidable.
- A divergence between $u$ and $\hat q$ has at least two causes — a
  mis-accommodated reading and a badly drafted answer to a correctly read
  question. The check as stated cannot separate them.
- The recovery step is only demonstrated over multi-sentence written monologue.
  A one-sentence reply may not carry enough given material for any licensed
  question to be recovered at all.

## Related

[[qud-parsing]] · [[qud-licensing-constraints]] · [[question-under-discussion]] · [[third-position-repair]] · [[clarification-request]] · [[decision-theoretic-grounding]]

[^s1]: ko-2023
[^s2]: riester-2019
[^s3]: wu-2023
