---
description: "A memory-update gate that asks a clarifying question instead of writing silently whenever the Shannon entropy of its six-action distribution exceeds a calibrated threshold."
aliases: ["authenticity gate"]
sources: ["hossain-2026"]
---
# Authenticity gate

Hossain, Shayoni & Morol (2026) build CAPTURE, a personalized
LLM agent whose memory-update module — the authenticity gate — must decide
whether an incoming statement that contradicts the stored user model is a
genuine preference revision or an injected/adversarial claim, without ever
observing the true label. From a continuous-time belief $h_t$ over the user
state and the extracted hypothesis, the gate predicts a distribution over six
actions — retain, add, narrow to a scope, revise, quarantine pending
corroboration, or **ask the user** — and takes the sixth, silent-write-free
action only when that distribution's uncertainty crosses a threshold:

> "The first five are silent. The sixth is not, and the agent takes it when
> the [[entropy|Shannon entropy]] of the action distribution exceeds a threshold, that is
> when H(P (at | ht , Ht )) > η."[^c1]

The threshold is not derived from a cost model; it is set post hoc to hit a
declared query budget:

> "We set η on validation to spend at most one clarifying turn per twelve
> interactions."[^c2]

Isolating the ask channel's contribution: giving the strongest heuristic
baseline (StateMem) the same fixed query budget and stored clarification
answers raises its win rate and cuts its poisoning rate, but not to CAPTURE's
level —

> "Query access is therefore worth roughly 1.5 points of win rate and 4.3
> points of poisoning resistance to StateMem, which is a real gain and does
> not account for C APTURE's remaining margin."[^c3]

— so the entropy-triggered ask is a real but partial contributor next to the
continuous-time belief and the multi-timescale ledger it sits inside. On the
paper's own benchmark the realized clarification decisions reach "precision
0.79, recall 0.70, and F1 0.74 at a realized query rate of 7.8% inside the
8.33% budget."[^c4]

## Transfer

| | |
|---|---|
| **In its home field** | Shannon entropy of a probability distribution as a general-purpose measure of uncertainty (information theory) |
| **Here** | Entropy of a *six-way action posterior* inside a memory-write decision — not of a hypothesis about a question's answer — used as the sole trigger for asking versus writing silently |
| **What survives** | The qualitative move: treat a flat action posterior as the signal to ask rather than act, and tune the threshold to a query-rate budget rather than to a derived cost |
| **What does not** | Any optimality claim for the threshold. $\eta$ is calibrated to a rate target on the paper's own synthetic generator, not derived from a cost-of-asking argument the way [[value-of-information]] or the paper's own Theorem 4 do it |

## Limits

- $\eta$ is set to hit a fixed query rate (≤1 in 12) on validation data from
  the authors' own synthetic generator, not from a stated cost of asking —
  so the threshold is a budget [[calibration]], not a derivation.
- Entropy is computed over the *action* distribution (six memory operations),
  which conflates "which action is correct" uncertainty with "is this claim
  genuine" uncertainty; the two are not shown to coincide.
- The isolated value of asking (claim[^c3]) is measured against one
  synthetic benchmark (D-PrefGuard) built by the same authors; the paper's
  own zero-shot transfer to HorizonBench is weaker and not significant on
  belief-revision accuracy.
- `hossain-2026` [?] is a September 2026 arXiv preprint, unverified beyond
  this extract.

## Related

[[value-of-information]] · [[semantic-entropy]] · [[sprt]] · [[clarification-channel-theorem]]

[^c1]: hossain-2026 — "The first five are silent. The sixth is not, and the agent takes it when the Shannon entropy of the action distribution exceeds a threshold, that is when H(P (at | ht , Ht )) > η."
[^c2]: hossain-2026 — "We set η on validation to spend at most one clarifying turn per twelve interactions."
[^c3]: hossain-2026
[^c4]: hossain-2026 — "C APTURE reaches precision 0.79, recall 0.70, and F1 0.74 at a realized query rate of 7.8% inside the 8.33% budget."
