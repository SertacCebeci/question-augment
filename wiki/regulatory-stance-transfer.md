---
description: "A two-hour AI-literacy workshop made middle-schoolers reject underspecified LLM prompts more, follow up more after weak answers, and judge correctness more accurately two days later."
aliases: ["applied AI literacy", "regulation of LLM interaction"]
sources: ["arxiv-2604-01955"]
---
# Regulatory-stance transfer

> Teaching learners to check whether a question is well-formed before
> sending it, and to keep asking when the answer falls short, is a skill
> that moves with them into a task the training never mentioned.

## Definition / Mechanism

Clerc, Abdelghani, Desvaux, Poisson, Oudeyer & Sauzéon (2026)
run a quasi-experimental classroom study (116 French middle-schoolers,
grades 8–9): an intervention group attended a two-hour workshop —
conceptual material on how LLMs generate and fail, plus practical
drills predicting whether a prompt would elicit a satisfactory answer,
querying, evaluating, and revising — on domains unrelated to the later
test; a control group did not. Two days later, both groups solved six
science problems with LLM access, each carrying a suggested prompt that
was either well-specified or covertly underspecified. The paper treats
three behaviors as the regulatory construct: whether a suggested prompt
is accepted or replaced, how accurately the returned answer's
correctness is judged, and whether a follow-up question is asked.

Trained students accepted suggested prompts less overall (OR = 0.47),
and this gap was concentrated on the underspecified ones (51.5% vs.
66.7% acceptance) while well-specified prompts were accepted at similar
rates in both groups — the workshop did not make students
indiscriminately suspicious, it made them selective.
[^c1]

Their correctness judgments were more sensitive to whether the prompt
had been well-specified than controls' (interaction OR = 2.52).
[^c2]

Conditional on having accepted an underspecified prompt anyway, they
asked a follow-up question roughly twice as often (59.2% vs. 27.9%).
[^c3]

## Why it matters

The training never rehearsed the test's science tasks or prompts; what
transferred was a general checking-and-following-up *stance* toward an
answering system, not memorized content. That stance also paid off
downstream: reject-vs-accept and follow-up-rate contrasts predicted
answer quality more strongly in the trained group, and signal-detection
sensitivity/bias predicted final scores only within the trained group —
suggesting the workshop strengthened the link between noticing a
problem and acting on it, more than it strengthened noticing itself.
Offline self-report of AI attitudes and general metacognitive awareness
predicted none of this: the study's own behavioral indicators explained
task quality where self-report did not.
[^c4]

For a wiki whose subject is
what makes an asker (person or agent) ask and answer well, this is
evidence that the regulatory habits — checking a query's specification,
evaluating an answer, deciding to press further — are a trainable,
transferable skill separate from what the asker can report about their
own competence.

## Limits

- Quasi-experimental: classes, not individuals, were assigned to
  condition, so the intervention is confounded with whatever
  distinguished those classes' schedules; `replicated: false`.
- One school, one age band (13–15), a 90-minute test two days after a
  two-hour workshop — the paper explicitly declines to call this
  durable learning, only short-term transfer.
- The condition × prompt-specification interaction on acceptance was
  not itself significant (p = .228); the concentration on underspecified
  prompts is a follow-up contrast, not the primary test.
- Sensitivity (d′) was only numerically higher in the trained group
  (p = .150); the behavioral gap is clearer in *acting* on
  underspecification (rejecting, following up) than in *detecting* it.

## Related

[[question-asking-skill-transfer]] · [[ai-collaboration-clarity-without-effort-reduction]] · [[calibration]]

[^c1]: arxiv-2604-01955 — "were less likely than control students to accept suggested prompts overall (OR = 0.47, 𝑝 = .022;"
[^c2]: arxiv-2604-01955 — "this effect was larger in the intervention group (interaction OR = 2.52, 𝑝 = .012; Fig. 2B), indicating"
[^c3]: arxiv-2604-01955 — "Interaction control: Among accepted underspecified-prompt trials, intervention students asked followup questions more often than controls (59.2% vs. 27.9%; Welch 𝑡 = 3.80, 𝑝 < .001, 𝑑 = 0.80; Fig. 2C)."
[^c4]: arxiv-2604-01955 — "observable regulation during LLM use was more informative than offline self-reports for explaining"
