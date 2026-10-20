---
description: "Internal knowledge of unsolvability and its verbalized judgment are distinct, linearly-decodable hidden-state directions in LLMs, and fabrication tracks their misalignment."
aliases: ["knowledge-verbalization dissociation", "knowledge-verbalization misalignment", "knowledge-verbalization gap"]
sources: ["xiros-2026"]
---
# Knowledge-verbalization dissociation

> A model can carry the fact that a problem is unsolvable in its hidden
> state and still say something else — not because the fact was never
> computed, but because computing it and saying it are different linear
> directions, and the second one is what generation follows.

## Definition / Mechanism

Xiros, Zoumpoulidi & Paraskevopoulos (2026) train two logistic-regression
probes on pooled hidden states of seven LLMs answering math problems from
ReliableMath (313 solvable, 1,102 unsolvable variants): a **knowledge**
probe predicting the problem's ground-truth solvability, and a
**verbalization** probe predicting what the model's chain-of-thought
ultimately says (via an LLM-judge). Both probes decode substantially
above chance from hidden states, and the verbalization probe is easier to
decode than the knowledge probe for every model tested.[^c1]

The two probe directions have low cosine similarity across all seven
models (0.255–0.647), which the authors read as evidence the two
quantities occupy separate directions in hidden-[[possible-worlds|state space]] rather than
one.[^c2]

On the unsolvable-problem subset, knowledge and verbalization activations
are more correlated when the model abstains than when it fabricates an
answer ($r_{abstain} > r_{fab}$ in every model, $p<10^{-4}$), so fabrication
tracks a *drop in alignment* between what is known and what is said.[^c3]
Measuring the abstain–fabricate gap separately for each probe, the gap is
consistently larger on the verbalization probe than on the knowledge
probe — fabricated and abstained responses differ mainly in how solvability
is verbalized, not in the underlying knowledge representation.[^c4]

Prompting with stronger unsolvability cues raises abstention, and the
mechanism is verbalization, not knowledge: across all models, cues flip
the verbalization probe's prediction far more often than the knowledge
probe's, and pure knowledge-only flips are the rarest category — the
prompt changes what the model says, not what it has already represented.[^c5]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Interpretability (this paper) | knowledge–verbalization misalignment | exact |
| Interpretability (this paper) | knowledge–verbalization gap | exact |

[^c6]

## Why it matters

On stall 10 this supplies a mechanism for *why* an answerer over-commits
instead of abstaining: not usually a missing fact, but a fact that fails
to reach the verbalized decision. It is an internal analogue of
[[abstention]]'s $(f,g)$ split — $f$'s hidden state can already carry the
information $g$ would need to reject, and $g$ still does not act on it.

## Limits

- Restricted to mathematical solvability on one benchmark family; the
  authors flag as open whether the knowledge/verbalization split holds for
  general question answering.[^c7]
- The verbalization label is produced by an LLM-as-judge, validated on
  only 100 human-annotated samples; the "knowledge" label is the
  benchmark's own ground truth, not an independently verified property of
  the model's internal state.
- RQ1–RQ3 (this note) are correlational: distinct decodable directions and
  correlated misalignment do not by themselves show the verbalization
  direction is what *causes* the commit decision — that causal claim is
  tested separately by steering (see [[gated-activation-steering-for-abstention]]).

## Related

[[abstention]] · [[gated-activation-steering-for-abstention]] · [[calibration]] · [[semantic-entropy]]

[^c1]: xiros-2026 — "Knowledge and verbalization probes achieve substantially above-chance performance across all models, indicating that both quantities are encoded in model hidden states and can be linearly decoded. Verbalization is consistently easier to decode than knowledge, with V probes achieving higher AUC than K probes for every model."
[^c2]: xiros-2026 — "Low similarity indicates that knowledge and verbalization are represented separately."
[^c3]: xiros-2026 — "knowledge and verbalization are more strongly aligned during abstention than during fabrication, suggesting that fabrication is associated with a reduction in the alignment between internal solvability knowledge and verbalization."
[^c4]: xiros-2026 — "The abstain–fabricate gap is consistently larger for verbalization than for knowledge, indicating that fabricated responses differ from abstained responses primarily in how solvability is verbalized rather than in the underlying solvability knowledge itself."
[^c5]: xiros-2026
[^c6]: xiros-2026 — "Fabrication is associated with a reduced alignment between these representations and primarily reflects changes in verbalization rather than the underlying knowledge."
[^c7]: xiros-2026 — "our study is restricted to mathematical solvability, and it remains an open question whether the distinction between knowledge and verbalization extends to general question answering and other settings."
