---
description: "A single-trace uncertainty score built by re-eliciting a short answer from a frozen model conditioned on its own completed reasoning trace and scoring agreement with the original answer."
aliases: ["TrAC", "trace-conditioned answer consistency", "answer re-elicitation", "Prefix-Conditioned Elicitation"]
sources: ["yu-2026-trac"]
---
# Trace-conditioned answer consistency

> Instead of sampling a fresh trace or asking the model to judge its own
> answer, re-run the *same* frozen model past its own completed reasoning and
> see whether it still says the same thing — a cheap probe for "does this
> answer deserve to stand, or does it need another question."

## Definition / Mechanism

Yu, Jiang, Xu & Wang (2026) give a reasoning trace $y=(r,a)$ —
completed reasoning $r$ and returned answer $a$ — from a frozen model
$p_\theta$. Their intuition: re-eliciting an answer from the completed
reasoning prefix can reveal whether, and how strongly, the model continues to
support its original answer.[^c1]

They name the measured property **trace-conditioned answer consistency** and
the procedure used to measure it **answer re-elicitation**: a short fixed cue
is appended to the completed trace and the frozen model re-elicits only an
answer suffix; this is scored as **Prefix-Conditioned Elicitation (PCE)**
(agreement, likelihood, confidence of the re-elicited answer against $a$) and
fused with **Trace Uncertainty Profile (TUP)**, token-level uncertainty read
off the original decode with no extra generation. A lightweight head trained
on correctness labels combines the two into a scalar $u(x,y)\in[0,1]$, ranked
by AUROC and by the area under the risk–coverage curve (AURC).[^c2]

Unlike explicit self-verification, which asks the model to judge whether its
answer is correct, answer re-elicitation measures answer reproducibility
under a controlled re-reading of the completed trace; unlike sampling-based
consensus, it probes support within one trace rather than comparing several.[^c3]

The resulting score can support abstention, prioritize responses for human
review, or allocate additional samples to low-scoring responses.[^c4]

Across five math-reasoning benchmarks and three LLM families, TrAC improves
macro AUROC by 1.8% and reduces AURC by 3.4% relative to eight-sample
self-consistency, while using one complete reasoning trace and a short
cached answer probe.[^c5]

When eight samples are already available, augmenting sample consensus with
re-elicitation further improves macro AUROC by 4.3% and reduces AURC by
8.3%, without additional full-trace generation.[^c6]

## Why it matters

On this stall, TrAC is a candidate **trigger signal**: a cheap, single-trace
score computed after an answer is produced, usable to decide whether an axis
needs a further question (escalate to a human, resample, or abstain) rather
than a criterion for ranking which axis to ask about next. It differs from
this stall's [[value-of-information]] criteria ([[mutual-information|mutual information]], EIG) in
kind: it scores one already-produced answer's [[calibration|reliability]] rather than a
candidate question's expected value, so it belongs beside [[semantic-entropy]]
and [[abstention]] as a post-hoc uncertainty estimate that feeds the decision
to ask again, not as an axis-selection rule.

## Transfer

| | |
|---|---|
| Home field | verifiable math reasoning: a deterministic answer checker supplies offline correctness labels to train the scoring head; evaluated by AUROC/AURC against that label |
| Here | any asking loop where an answer must be scored for whether to accept it, escalate it, or ask again, with no reference answer at inference time |
| What survives | the re-elicitation move itself (probe the model's own completed context rather than sample a new trace or ask it to self-judge), and the single-trace/low-latency framing as an alternative to eight-sample consensus |
| What does not | the correctness-supervised training requirement (a labelled fold to fit the scoring head) and the validation, which is math reasoning plus two additional benchmarks, not open-ended or design-question answering |

## Limits

- The score is trained with correctness supervision from a deterministic
  verifier; the claim above that it beats self-consistency rests on that
  supervision being available, which most design or clarification questions
  lack.
- Evaluated on five math-reasoning benchmarks plus BIG-Bench Hard and
  GPQA-Diamond — verifiable, single-correct-answer domains; the wiki has no
  evidence this ranks open-ended answers.
- Only one source [?] — yu-2026-trac is newly harvested and not yet
  independently verified.

## Related

[[semantic-entropy]] · [[abstention]] · [[value-of-information]] · [[mutual-information]]

[^c1]: yu-2026-trac — "Our key intuition is that re-eliciting an answer from the completed reasoning prefix can reveal whether, and how strongly, the model continues to support its original answer."
[^c2]: yu-2026-trac — "We refer to the measured property as trace-conditioned answer consistency and to the procedure used to measure it as answer re-elicitation."
[^c3]: yu-2026-trac — "Unlike explicit self-verification, which asks the model to judge whether its answer is correct, answer re-elicitation measures answer reproducibility under a controlled re-reading of the completed trace."
[^c4]: yu-2026-trac — "The resulting score can support abstention, prioritize responses for human review, or allocate additional samples to low-scoring responses."
[^c5]: yu-2026-trac — "TrAC improves macro AUROC by 1.8% and reduces AURC by 3.4% relative to eight-sample self-consistency, while using one complete reasoning trace and a short cached answer probe."
[^c6]: yu-2026-trac — "augmenting sample consensus with re-elicitation further improves macro AUROC by 4.3% and reduces AURC by 8.3%, without additional full-trace generation."
