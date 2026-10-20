---
description: "Adding a probe-derived steering vector only at tokens where a knowledge probe signals latent unsolvability rescues abstention on unsolvable problems without destroying accuracy on solvable ones."
aliases: ["gated activation steering", "KV-gated steering"]
sources: ["xiros-2026"]
---
# Gated activation steering for abstention

> Steering an answerer toward "I don't know" works — but only if the
> intervention is switched on and off token by token by the model's own
> latent belief that it does not know, not applied everywhere at once.

## Definition / Mechanism

Xiros, Zoumpoulidi & Paraskevopoulos (2026) intervene on the
residual stream at a targeted layer and token by adding a unit-normalized
steering vector $w$ scaled to the layer's mean activation norm:
$h'_t = h_t + m \cdot \alpha_{unit} \cdot w$, where $w$ is a knowledge (K),
verbalization (V), or combined (KV) probe direction and $m$ is a
sweepable intensity.[^c1]

Applied unconditionally at every token, this is destructive: on the
solvable-problem control split, static K, V and KV steering drive
[[abstention]] far above the ~0.01 baseline, reaching roughly 0.6–0.8 at high
intensity — the model abandons problems it could solve.[^c2]

The fix is a discrete, binary gate keyed to the knowledge probe itself:
steering is applied only at token positions where the knowledge probe's
predicted probability of unsolvability exceeds 0.5, and left off
otherwise.[^c3]

Under this gate, steering the combined KV direction ("KVgateK") is the
strongest and most stable rescue of abstention on the unsolvable split —
at or above either single-direction variant at every tested intensity, on
the one model (Qwen3-4B-Instruct, layer 18) reported in detail.[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Interpretability (this paper) | KV-gated steering | exact |

[^c5]

## Transfer

| | |
|---|---|
| In its home field | mechanistic interpretability / representation engineering: an additive intervention along a probe-identified direction in a transformer's residual stream, evaluated on classification-style behavioural metrics |
| Here | an intervention on an answerer's hidden state at generation time, aimed at flipping the commit/abstain decision on stall 10 |
| What survives | steering along a linearly decodable, probe-derived direction; the necessity of gating the intervention to a per-token trigger rather than applying it globally, to protect cases where the answer should be committed |
| What does not | the specific gate threshold (0.5) and multiplier sweep, fit and reported on the same evaluation split rather than validated on a held-out one; the requirement of a pre-trained, per-model, per-layer knowledge probe before the intervention can be applied at all |

[^c6]

## Limits

- Reported in worked detail for a single model and layer (Qwen3-4B-Instruct,
  layer 18); other models are stated to show "the same patterns" but their
  results are in an appendix this extract does not carry, so generality
  across model families rests on the authors' summary, not on figures read
  here.
- The gate threshold and steering multiplier are swept and reported on the
  same 280-sample subsets used to evaluate the rescue, not validated on a
  disjoint held-out sweep — the reported operating point may be optimistic.
- The intervention presupposes [[knowledge-verbalization-dissociation]]'s
  probes already exist for the model and layer in question; it is not an
  inference-time technique usable without first solving that probing
  problem.

## Related

[[knowledge-verbalization-dissociation]] · [[abstention]] · [[calibration]]

[^c1]: xiros-2026 — "h′t = ht + m · αunit · w where w ∈ Rd is the unit-normalized raw direction vector corresponding to a specific probe, and αunit is the mean residual stream norm at layer L."
[^c2]: xiros-2026
[^c3]: xiros-2026 — "steering is only activated at token positions where the Knowledge probe’s predicted probability pK (ht ) exceeds a confidence threshold of 0.5"
[^c4]: xiros-2026 — "KVgateK is the strongest and most stable, sitting at or above both single-direction variants, reaching the highest rescue rate at maximum intensity. Steering the combined direction is thus more reliable than steering either alone."
[^c5]: xiros-2026 — "KVgateK is the strongest and most stable"
[^c6]: xiros-2026 — "By dynamically restricting steering strictly to tokens where the model demonstrates latent solving capacity, this gating approach drastically minimizes false positives (incorrectly altering solvable problems) while maintaining a high rate of successful faithful rescues."
