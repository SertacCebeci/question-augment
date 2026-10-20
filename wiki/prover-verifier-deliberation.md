---
description: "An inference-time protocol where a frozen LLM prover defends an answer to a frozen LLM verifier through challenges; whether the defence survives unrevised gates report-or-abstain."
aliases: ["PVD", "prover-verifier deliberation", "Accept + No Change", "ANC"]
sources: ["sedoc-2026"]
---
# Prover-verifier deliberation

> A frozen LLM defends a candidate answer to a second frozen LLM through a
> challenge-response dialogue; whether the defence survives unchanged is the
> signal used to decide report-or-abstain.

## Problem

A system that answers most questions correctly but cannot tell which
answers are reliable is worse in deployment than one that answers fewer
questions with near-certainty and abstains otherwise. Existing
inference-time methods (self-consistency, debate, Reflexion) improve raw
accuracy but their confidence proxies — sample agreement, debate consensus
— are indirect and were not designed to license a report/abstain decision.[^c1]

## Definition / Mechanism

Prover-Verifier Deliberation (PVD), introduced by Sedoc, Zhang & Foster (2026),
runs two frozen language models, a Prover $P$ and a Verifier $V$, over a
multiple-choice question. $P$ picks an answer and produces a one-sentence
claim, 3–5 atomic sub-claims, and a justification. At each round $V$
inspects the transcript and returns ACCEPT (terminate, accepted), REJECT
(terminate, rejected), or CHALLENGE (name the weakest sub-claim; $P$
defends or revises). A fatigue limit $T$ forces rejection if no verdict is
reached; up to $K$ retries follow a rejection, with prior failures given to
$P$ as adversarial context; if no attempt reaches acceptance-without-revision
the final answer is majority vote over attempts.

**Accept + No Change (ANC)** is the [[abstention|selective-prediction]] signal: an attempt
is ANC iff $V$ issues ACCEPT and $P$'s answer was never revised across all
rounds. An ACCEPT reached after revision indicates the prover corrected
itself under pressure and is not treated as high-confidence. ANC is scored
as a binary classifier for correctness via HC-Cov $=\Pr[\text{ANC}]$ and
HC-Prec $=\Pr[\text{correct}\mid\text{ANC}]$.[^c2]

On GPQA Diamond with Claude Sonnet 4.6 as prover and Haiku 4.5 as verifier,
PVD reaches HC-Prec 84.2% at HC-Cov 77% for about three LLM calls per
question, a ∼30-percentage-point precision gap over the non-ANC
complement; the strongest configuration (GPT-5.4 prover, GPT-5.4-mini
verifier) reaches HC-Prec 97.6% at HC-Cov 43%, a +34.8pp gap.[^c3]

Robustness runs pairing provers and verifiers from different model
families (e.g. Gemini 3.1 Pro prover with GPT-5.5-pro verifier) show high
HC-Prec transferring across families, while verifier strictness and the
verifier's domain competence — not family match — set the size of the
selection gap.[^c4]

On Humanity's Last Exam, weaker prover-verifier pairings can collapse or
invert the ANC signal: in the Engineering domain the gap turns negative
(HC-Prec 31.2% vs. 55.6% on the non-ANC complement), a diagnostic that the
verifier is operating outside its region of competence rather than a
tuning failure.[^c5]

## Transfer

| | |
|---|---|
| **Home field** | Interactive proof theory / complexity theory: a computationally powerful prover convinces a probabilistic, computationally bounded verifier of a claim's truth, with soundness and completeness bounds that fall exponentially in the number of rounds |
| **Here** | selective prediction for frozen LLMs on open-domain, no-ground-truth questions: a fixed-capability prover defends a candidate answer to a fixed-capability verifier |
| **What survives** | the challenge-response structure and the asymmetric cognitive load it rests on — the verifier only checks one local sub-claim per round rather than judging global correctness |
| **What does not** | the formal guarantees. "Because frozen language models are imperfect provers and verifiers operating over a noisy channel, formal soundness and completeness guarantees do not transfer; instead, we characterize the protocol empirically through its coverage-precision behavior." The wiki treats HC-Prec and the ACCEPT/REJECT accuracy gap as the empirical substitutes, not proofs.[^c6]

## Limits

- No ground-truth oracle is available during deliberation; ANC is a
  post-hoc classifier evaluated against benchmark labels, not a property
  guaranteed by the protocol itself.
- The gap can invert (Engineering domain, HLE) when the verifier's own
  domain competence is exceeded — the signal is only as good as the
  verifier, and this wiki has no source establishing where that boundary
  lies for a given model pair in advance.
- Reported configurations use $K{=}1, T{=}12$ single-attempt PVD except
  one retry configuration ($K{=}6$) examined only for cost, so most
  numbers describe the cheap variant, not the strongest one.
- Single source [sedoc-2026]; no independent replication yet.

## Related

[[semantic-entropy]] · [[expected-information-gain]] · [[value-of-information]]

[^c1]: sedoc-2026 — "self-consistency’s agreement rate and debate’s consensus are at best indirect proxies for correctness, and none was designed to produce a principled abstain/report decision."
[^c2]: sedoc-2026 — "an attempt is ANC if V issues ACCEPT and P’s answer was never revised across all challenge rounds. ANC is the primary selective-prediction signal"
[^c3]: sedoc-2026 — "PVD achieves HC-Prec 84.2% at HC-Cov 77% with roughly three LLM calls per question. ANC separates reliable from unreliable answers, yielding a ∼30pp HC-Prec gap over the non-ANC complement."
[^c4]: sedoc-2026 — "Robustness experiments with GPT and Gemini pairings show that high HC-Prec can transfer across model families, while verifier strictness and domain competence largely determine the size of the selection gap."
[^c5]: sedoc-2026
[^c6]: sedoc-2026 — "Because frozen language models are imperfect provers and verifiers operating over a noisy channel, formal soundness and completeness guarantees do not transfer; instead, we characterize the protocol empirically through its coverage-precision behavior."
