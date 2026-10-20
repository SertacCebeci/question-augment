---
description: "Assigns a fixed penalty to each of four question types by mining human navigation corpora, as a computable stand-in for the type's expected information gain."
aliases: ["question type taxonomy", "cue utility score", "mined question-type costs"]
sources: ["zhao-2026"]
---
# Question-type cost mining

> When the true posterior a question would resolve is unobservable, price the question type instead of the question: mine how informative each *type* of cue has been across a corpus of human navigation language, and lock that as its cost.

## Definition / Mechanism

The source motivates cost by [[expected-information-gain|expected information gain]] but cannot compute it: "Directly computing this quantity is impractical because the posterior $p_t(S\mid q,a)$ over real targets in real scenes is unobservable. We therefore use heterogeneous human-authored navigation corpora as an empirical proxy for which cues typically reduce target and spatial [[efe-planning-as-variational-inference|ambiguity]]."[^c1]

Mined cues are grouped into four question types (appearance, region, direction/route, confirmation). For each cue $c$, a composite utility $U_c=\lambda_1\bar s_c+\lambda_2 h_c+\lambda_3 r_c$ combines average scorer-assigned importance $\bar s_c$, the fraction of high-gain mentions $h_c$, and the fraction of records where the cue ranks first $r_c$; cue utilities are mention-weighted within each type and rescaled into a locked per-type cost $w_t$:

| Question type | Primary uncertainty reduced | Penalty $w_t$ |
|---|---|---|
| Type 1 appearance | target identity among same-category instances | 0.182 |
| Type 2 region | room or region to search | 0.162 |
| Type 3 direction/route | branch, corridor, or layout direction | 0.240 |
| Type 4 confirmation | whether a visible candidate is the target | 0.103 |
[^c2]

"More informative question types receive larger penalties because they expose stronger oracle assistance and should be discounted more heavily when measuring autonomous navigation ability."[^c3]

## Known as

| Field | Name there | Match |
|---|---|---|
| Robotics / VLN | question type taxonomy | exact |
| Robotics / VLN | cue utility score | close (the per-cue quantity that feeds the per-type cost) |

## Why it matters

It gives stall 2 (which axis first) a concrete, data-derived alternative to assuming every question type costs the same or to hand-tuning costs: the price of a question type is read off how much answerer-side work it typically does in a corpus, not asserted.

## Transfer

| | Home field (information theory) | Here (embodied navigation) |
|---|---|---|
| Formalism | expected information gain $\mathrm{EIG}(q)=H[p_t(S)]-\mathbb E[H[p_t(S\mid q,a)]]$ | motivates the cost design but is never computed |
| What survives | the framing that a costlier-to-answer question should be one that resolves more uncertainty | the ordinal idea: informativeness should track cost |
| What does not | the [[entropy]] computation itself | replaced by three corpus statistics ($\bar s_c$, $h_c$, $r_c$) from an LLM cue-scorer, because the real posterior is unobservable |

[^c4]

## Limits

The four types and their costs are mined from five specific indoor-navigation corpora (R2R, REVERIE, RxR, CVDN, SOON) using one fixed-schema LLM scorer (Qwen3.5-4B); the costs are locked before evaluation and are not re-estimated per scene or per instruction, so they carry that scorer's and those corpora's biases (English route instructions, indoor object search) and are untested outside this domain. Because cost is tied to "how much oracle assistance is exposed" rather than to a demand on the answerer's time or effort, it measures information leakage, not the cost the asking literature usually means by cost.

## Related

[[weighted-success-rate]] · [[expected-information-gain]] · [[value-of-information]] · [[sensitivity-weighted-question-score]]

[^c1]: zhao-2026 — "Directly computing this quantity is impractical because the posterior pt pS | q, aq over real targets in real scenes is unobservable. We therefore use heterogeneous human-authored navigation corpora as an empirical proxy for which cues typically reduce target and spatial ambiguity."
[^c2]: zhao-2026
[^c3]: zhao-2026 — "More informative question types receive larger penalties because they expose stronger oracle assistance and should be discounted more heavily when measuring autonomous navigation ability."
[^c4]: zhao-2026 — "We derive the question taxonomy and its interaction costs from an information-gain-inspired uncertainty model."
