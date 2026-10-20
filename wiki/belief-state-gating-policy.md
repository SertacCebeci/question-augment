---
description: "A threshold policy that decides when an LLM should pause reasoning to ask a question, scored by a probe trained on the hidden-state shift a candidate question induces."
aliases: ["belief-state gating", "gating policy", "hidden-state probe gating"]
sources: ["luo-2026-what"]
---
# Belief-state gating policy

> A learned trigger for "ask now": score a candidate question by a probe on
> the model's own hidden state, not by an [[entropy]] or [[mutual-information]]
> computation over its output distribution.

## Definition / Mechanism

Luo, Dahan & Zhu frame test-time question-asking as a student model
interrupting its own reasoning trajectory $\tau_t$ to query a teacher. The
decision of when to intervene is a threshold on a learned score: "We
introduce a gating policy that uses hidden-state probing to assess two axes
of good questions: (i) which to ask: what student questions would lead to
the most fruitful outcomes? and (ii) when to ask: when is an intervention
likely beneficial to the student?" and "We intervene on the partial
reasoning trajectory with a gating policy π(τt), formally defined as the
following threshold decision at step t"[^c1]

The score itself comes from a **belief-state probe**: a classifier trained
on the concatenation of the student's hidden state before and after
formulating a candidate question, predicting the probability the trajectory
will end correct. "We train a hidden state probe to predict the correctness
rate at time step t before generating the teacher answer." The gate fires on
the *worst case* among $N$ sampled candidate questions — "We sample N
discrete questions Q(τt), and take the score that triggers the gating policy
π(τt)" and "If there is at least one question sample that is predicted to
lead to a weak belief state, then the gate triggers" — then the
highest-scoring of the sampled questions is the one actually sent to the
teacher. The threshold γ was set to 0.6 by a hyperparameter sweep, not
derived.[^c2]

The probe is only useful if its score tracks the trajectory it was never
shown finishing: "Our probe is reasonably calibrated to actual correctness;
we achieve Brier scores of 0.157 for Qwen3-1.7B to 0.121 for Qwen3-14B
without the teacher answer" — [[calibration]] improved with model size across
the tested range.[^c3]

## Why it matters

Every selection criterion already on this stall — EIG, VoI, semantic
entropy — scores a question from the model's *output* distribution (answers
sampled, or logits over them). This mechanism instead reads a signal off the
model's *internal* state: the hidden-state shift the act of formulating a
question induces, before any teacher answer exists. It is a different
information source for the same stall-2 decision (which axis / when to
probe it), not a refinement of an existing one.

## Transfer

| | |
|---|---|
| **In its home field** | Probing classifiers in interpretability research: a linear or shallow head trained on a frozen model's hidden state to predict some external label the model was never trained to output |
| **Here** | The probe's predicted label is the *future correctness of the reasoning trajectory*, and its score is read as a real-time signal for whether to ask a question next |
| **What survives** | The core probing move — training a small predictor on hidden-state activations rather than on model outputs — and the finding that the pre+post-question concatenation is more predictive than either alone, i.e. the act of forming a question itself shifts the state in an informative way |
| **What does not** | Any guarantee of calibration outside the tested domain: the probe is trained per model, per dataset, on math reasoning with verifiable answers; the threshold γ=0.6 is swept empirically, not set by a decision-theoretic argument the way VoI's threshold is |

## Limits

This note's claim rests on a single paper's self-play and teacher-assisted
experiments on math reasoning (GSM8k, Math500, AIME24) with Qwen3 (1.7B,
4B, 14B) and Olmo-3-7B-Think, where ground-truth correctness for probe
training comes from verifiable math answers. Whether a belief-state probe
trained this way transfers to open-domain question-asking, where no
verifiable label exists to train the probe against, is untested by the
source. The gate's efficiency at flagging wrong trajectories does not by
itself establish that asking helps — see [[detection-recovery-gap]].

## Related

[[value-of-information]] · [[expected-information-gain]] · [[semantic-entropy]] · [[detection-recovery-gap]]

[^c1]: luo-2026-what — "We introduce a gating policy that uses hidden-state probing to assess two axes of good questions: (i) which to ask: what student questions would lead to the most fruitful outcomes? and (ii) when to ask: when is an intervention likely beneficial to the student?"
[^c2]: luo-2026-what — "We train a hidden state probe to predict the correctness rate at time step t before generating the teacher answer."
[^c3]: luo-2026-what — "Our probe is reasonably calibrated to actual correctness; we achieve Brier scores of 0.157 for Qwen3-1.7B to 0.121 for Qwen3-14B without the teacher answer."
