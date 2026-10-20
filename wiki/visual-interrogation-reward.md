---
description: "An RL reward model formulates instance-specific visual questions offline and answers them online against rendered output, aggregating graded yes/no scores into a low-variance reward."
aliases: ["VIVA", "Visual Interrogation Verifies All", "V IVA reward"]
sources: ["arxiv-2604-05514"]
---
# Visual interrogation reward

> A reward model does not score a rendered output by holistic similarity —
> it interrogates it, one pre-drafted question at a time, and averages the
> answers.

## Definition / Mechanism

Visual Interrogation Verifies All (V IVA), introduced by
Yang et al. (2026), is a reward mechanism for RL
training of diagram-code generation. For each training instance it splits
the questioner from the verifier in time: an offline pass drafts N
instance-specific visual questions from the input (e.g. "Does the
'AuditLog' entity list an attribute named 'Timestamp' with the data type
'datetime'?"), each phrased so a *Yes* answer marks correct visual
fidelity. "Specifically, for each RL training sample, we generate
multiple visual questions derived from the input queries. A reward model
then answers these questions based on the rendered images of the rollout
code to evaluate its accuracy. Also, to enhance the training efficiency
and robustness, we decouple question generation from answer
verification. We offline generate fine-grained questions per sample,
specifically designed such that an answer of Yes corresponds to correct
visual fidelity"[^c1]

Online, during RL rollout, a VQA model answers each of a candidate's
pre-drafted questions against its own rendered image and produces a
graded (not binary) score; the questions' N graded answers are averaged
into the instance's V IVA reward, combined with a format reward, and fed
to GRPO as the group-normalized advantage. Because the answer is graded
in [0, 1] rather than forced to {0, 1}, the mechanism trades a
high-variance Bernoulli draw for a bounded-variance one, and averaging N
such questions under an equicorrelation model further attenuates the
noise any one question's VQA uncertainty contributes to the aggregate
reward, lowering the variance of the policy-gradient advantage estimate:
"Unlike conventional binary rewards (0 or 1) that follow a high-variance
Bernoulli distribution, V IVA's graded scoring function allows for
intermediate values, which mathematically ensures that the single-item
variance satisfies Var[Xk] ≤ µk (1 − µk)."[^c2]

Splitting drafting from answering also moves the "hard part" — deciding
what to check — out of the loop that has to run at every rollout. The
paper found the mechanism's accuracy tracks the quality of the offline
question set more than the scale of the online answering model, so a
small verifier model can score reliably once the questions it has to
answer are well chosen: "the marginal performance discrepancy across
these scales highlights the inherent robustness of our mechanism,
suggesting it is relatively invariant to the capacity of the reward
model. This suggests that the offline-generated visual questions, which
provide essential visual grounding, are more pivotal to the optimization
than the scale of the online feedback."[^c3]

## Why it matters

A single-shot similarity or "does this look right" judgment is a coarse,
high-variance training signal, especially where two visually identical
renders can come from structurally different code or where many valid
layouts exist for one input. V IVA replaces that one judgment with many
narrow, verifiable ones and only then aggregates — the same move that
lets a checklist beat a single holistic verdict elsewhere in the wiki
([[adversarial-metric-self-review]]), but applied here to shape a dense
training reward rather than to gate a human-facing artifact.

## Limits

The questions are drafted once, offline, by a separate LLM (GPT-4.1-mini
in this work) and never revised against what the policy actually
produces; a systematically mis-specified or ambiguous question set would
silently bias every rollout it scores, and the paper does not report a
check on question quality itself, only on downstream task metrics. The
variance bound assumes each per-question score is answered independently
enough to fit an equicorrelation model — an assumption asserted for
analytical tractability, not verified against the true VQA answer
distribution.

## Related

- [[adversarial-metric-self-review]] — a second LLM channel interrogates
  a candidate against a fixed checklist rather than scoring it wholesale;
  the same decomposition move, on a metric instead of a reward.
- [[expected-information-gain]]
- [[calibration]]

[^c1]: arxiv-2604-05514 — "Specifically, for each RL training sample, we generate multiple visual questions derived from the input queries. A reward model then answers these questions based on the rendered images of the rollout code to evaluate its accuracy. Also, to enhance the training efficiency and robustness, we decouple question generation from answer verification. We offline generate fine-grained questions per sample, specifically designed such that an answer of Yes corresponds to correct visual fidelity"
[^c2]: arxiv-2604-05514
[^c3]: arxiv-2604-05514 — "As demonstrated in Table 3, the marginal performance discrepancy across these scales highlights the inherent robustness of our mechanism, suggesting it is relatively invariant to the capacity of the reward model. This suggests that the offline-generated visual questions, which provide essential visual grounding, are more pivotal to the optimization than the scale of the online feedback."
