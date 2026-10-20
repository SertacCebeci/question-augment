---
description: "A two-phase prompted interrogation — a punishment-framed initial question, then a challenge-and-explain follow-up — scored by an independent expert LLM, cutting medical-VQA calibration error by 40%."
aliases: ["MS-FBI", "Multi-Strategy Fusion-Based Interrogation"]
sources: ["du-2026-confidence"]
---
# Multi-strategy fusion-based interrogation

> Ask for a confidence score under threat of punishment, then challenge and
> demand an explanation, then hand the whole transcript to a second model
> that has not answered the question itself — the order of interrogation
> strategies, not a single better prompt, is what the measured 40% drop in
> [[calibration]] error rests on.

## Definition / Mechanism

Du, Wang, Kong et al. (2026) propose Multi-Strategy
Fusion-Based Interrogation (MS-FBI) for calibrating a multimodal LLM's
verbalized confidence in medical visual question answering. It is explicitly
imported from suspect interrogation: "Inspired by the lie detection process
in criminal interrogations (FBI, e.g.), this study designs a interrogation
system that integrates multiple strategies based on prompt engineering,
constructing a dynamically adaptive interrogation scenario."[^c1]

The system runs two phases on one model. **Initial Inquiry** asks for an
answer and a confidence score under a *Punish* prompt ("You will be punished
if the answer is wrong but you answer it with high confidence"), meant to
curb overconfidence before any content is checked. **Deep Inquiry** then
applies *Challenge* ("I do not think your answer is right...") and *Explain*
("please explain why you give this answer") to the same transcript,
producing a rebuttal $R_{mllm}$; at least one of Challenge or Explain must
fire, giving six strategy combinations (Punish on/off × three
Challenge/Explain modes). The transcript $(Q,A,C,R_{mllm})$ is then handed to
a separate, non-answering expert LLM (llama3-instruct-8B), which outputs a
reassessed confidence $C_r$ and its own reasoning $R_{exp}$: "By comparing
$C$ and $C_r$, MLLMs' introspective ability can be quantified, while
$R_{exp}$... reveals the MLLMs' decision bias patterns."[^c2]

On three medical VQA datasets (Med-VQA, VQA-RAD, SLAKE) and four MLLM
backbones, MS-FBI+expert-assessment reduced LLaVA-1.5-med-7B's average
Expected Calibration Error from 44.28% to 26.22% ("a 40.8% reduction") and
raised AUROC from 49.48% to 55.07%, outperforming a vanilla verbalized-
confidence baseline, a Punish-only prompt, and a Top-K verbalized-likelihood
baseline across all four tested backbones.[^c3]

Ablation over the six strategy combinations found no single winner:
Punish+Challenge gave the lowest ECE (27.89%) for LLaVA-1.5-med-7B and also
generalised best across models, but "strategy effectiveness is not tied to
complexity, as combining all three methods yielded suboptimal results," and
the single Challenge strategy beat every combination for LLaVA-NeXT-7B on
one dataset — the paper reports this as cross-model heterogeneity rather
than a fixed strategy order.[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| this paper (machine learning / medical AI) | MS-FBI | exact |
| this paper (machine learning / medical AI) | Multi-Strategy Fusion-Based Interrogation | exact |

## Transfer

| | |
|---|---|
| **In its home field** | Criminal interrogation / lie detection: an escalating sequence of pressure, challenge and demand for explanation used to expose contradictions in a suspect's account. |
| **Here** | A fixed two-phase prompt sequence (punishment framing, then challenge-and-explain) applied to one MLLM's own verbalized confidence, scored against ground-truth accuracy rather than legal guilt. |
| **What survives** | The structural bet that pressure followed by a demand to justify exposes miscalibration the first answer alone did not — measured here as a lower gap between confidence and accuracy (ECE) and better separation of correct from incorrect answers (AUROC). |
| **What does not** | Any claim of deception detection or ground-truth veracity (the model is not lying, it is miscalibrated); the legal/ethical constraints on real interrogation; and generalization beyond the six tested strategy combinations — the ablation shows the best combination is model- and dataset-dependent, not a fixed order. |

## Limits

- Single paper (`du-2026-confidence`, arXiv 2026, unverified beyond this
  extract `[?]`), four backbones, three datasets, one expert-assessment
  model (llama3-instruct-8B) — no independent replication.
- The expert-LLM reassessment $C_r$ is not evaluated in isolation from the
  interrogation phases; the Punish-only ablation was dropped by the authors
  themselves because "it omitted the model's rebuttal phase, making the
  expert model's calibrated confidence scores unreliable," so the two
  components' individual contributions are not separated.
- The best strategy combination varies by model and dataset (Punish+Challenge
  vs. Challenge alone vs. all three), so "MS-FBI works" does not license a
  claim about which of its six configurations to deploy without re-running
  the ablation on the target model.
- Measured only on closed-ended medical VQA; the paper itself flags that
  "more refined calibration strategies may be needed... for general LLMs."

## Related

[[calibration]] · [[information-gathering-interview-style]] · [[confidence-calibrated-cascade-judgment]] · [[five-whys]]

[^c1]: du-2026-confidence — "Inspired by the lie detection process in criminal interrogations (FBI, e.g.) [16], this study designs a interrogation system that integrates multiple strategies based on prompt engineering, constructing a dynamically adaptive interrogation scenario, and systematically capturing the deep cognitive information of MLLMs."
[^c2]: du-2026-confidence
[^c3]: du-2026-confidence — "our proposed method outperforms the baseline methods across all the medical VQA datasets and MLLMs, reducing the average ECE of LLaVA-1.5-med-7B from 44.28% to 26.22% (a 40.8% reduction) and increasing AUROC from 49.48% to 55.07%."
[^c4]: du-2026-confidence — "However, strategy effectiveness is not tied to complexity, as combining all three methods yielded suboptimal results."
