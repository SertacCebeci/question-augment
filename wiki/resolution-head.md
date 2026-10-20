---
description: "A trained head reads a frozen LLM's mid-layer hidden-state trace and picks among clarification, tool use, abstention or direct answering, without touching the backbone."
aliases: ["Resolution Head", "resolution head"]
sources: ["ghasemabadi-2026"]
---
# Resolution Head

> Whether to ask, act, refuse or answer directly is read off a frozen
> model's own hidden-state trajectory by a small trained head, not decided
> by the [[backbone-of-a-formula|backbone]]'s surface output.

## Definition / Mechanism

Ghasemabadi, Chen, Rashidi & Niu (2026) attach a
lightweight Resolution Head to a frozen LLM or VLM. It reads a middle-layer
hidden-state trace $H^{res}$ of the model's own generated tokens, compresses
it, and outputs a score vector over the action set
$A=\{\text{info, tool, cant}\}$ (request more information, invoke a tool,
abstain); direct answering is the implicit all-zero case: "A Resolution Head
predicts appropriate resolution decision Clarification, Tool Use,
[[abstention|Abstention]], or Direct Answering... trained only on latent traces from the
same frozen LLM backbone, enabling post hoc adaptation without modifying the
model."[^c1]

The inference rule is a threshold on the top score: "the Resolution Head
predicts scores over $A=\{info, tool, cant\}$. If
$\max_{a\in A^{res}} s^{res}_a > \tau_{res}$, the system executes
$a^*=\arg\max_a s^{res}_a$; otherwise, it proceeds directly."[^c2]

The head is trained on When2Call with per-example multi-label targets
(binary cross-[[entropy]] against $y^{res}\in\{0,1\}^3$), constructed from the
backbone's own generations paired with the correct resolution label — not
the backbone's own chosen action, which is often wrong: "The model's
explicit action is not always correct — for example, it may invoke a tool
when clarification is required. The Resolution Head is therefore trained to
recover the appropriate decision from the latent trajectory rather than from
the model's surface behavior."[^c3]

## Why it matters

On stall 2 this is a working instance of routing the *whether-and-which*
decision (ask for information vs. call a tool vs. abstain vs. proceed) not
from the model's stated output but from an internal state read post hoc,
with a measured, positive quality gain over the backbone's own surface
choice: "on Qwen-VL-2B, F1 improves from 37.3 to 49.0 and accuracy from 52.7
to 65.1, while on Qwen3.5-4B, F1 improves from 43.5 to 54.5 and accuracy
from 57.9 to 69.5. Even when the model's surface action is wrong, its
hidden-state contains information for the head to recover the correct
resolution decision." Aggregated across backbones the paper reports "up to
11.7 F1 points and 12.4 accuracy points" of improvement on When2Call.[^c4]

## Limits

- The gain is measured against the *same backbone's own stated action*, not
  against a strong task-specific baseline built for the benchmark; the paper
  reports full-LLM When2Call baselines separately as a reference point
  rather than the comparison the improvement numbers are computed against.[^c5]
- The action set is fixed at three interventions plus an implicit
  direct-answer default (`A={info, tool, cant}`); it is a classification
  over a closed label set, not an open decision of *what* to ask or which
  tool — the head names the category, not the content of the question.
- Supervision requires per-example resolution labels (When2Call) and a
  fixed threshold $\tau_{res}$ tuned on held-out data; the reported operating
  point (top score > 0.5) is one choice among a precision–recall tradeoff
  the paper shows shifts with the threshold, not a value derived from a
  cost model of asking.

## Related

[[state-gated-strategy-routing]] · [[abstention]] · [[value-of-information]]

[^c1]: ghasemabadi-2026 — "A Resolution Head predicts appropriate resolution decision Clarification, Tool Use, Abstention, or Direct Answering. Both heads are trained only on latent traces from the same frozen LLM backbone, enabling post hoc adaptation without modifying the model."
[^c2]: ghasemabadi-2026 — "the Resolution Head predicts scores over A = {info, tool, cant}. If maxa∈Ares sres,a > τres , the system executes a∗ = arg maxa∈Ares sres,a ; otherwise, it proceeds directly."
[^c3]: ghasemabadi-2026 — "The model’s explicit action is not always correct—for example, it may invoke a tool when clarification is required. The Resolution Head is therefore trained to recover the appropriate decision from the latent trajectory rather than from the model’s surface behavior."
[^c4]: ghasemabadi-2026 — "on Qwen-VL-2B, F1 improves from 37.3 to 49.0 and accuracy from 52.7 to 65.1, while on Qwen3.5-4B, F1 improves from 43.5 to 54.5 and accuracy from 57.9 to 69.5. Even when the model’s surface action is wrong, its hidden-state contains information for the head to recover the correct resolution decision."
[^c5]: ghasemabadi-2026 — "We also include the task-specialized W HEN 2C ALL baselines reported by the benchmark as reference points. Unlike our lightweight head-based adaptation, these baselines are full LLMs fine-tuned directly on W HEN 2C ALL."
