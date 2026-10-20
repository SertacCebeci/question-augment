---
description: "A vision-language-action agent grounds a symbolic sub-goal to 3D entities by cross-attention, and gates a [CLARIFY] abstention token on the attention's entropy, calibrated as selective prediction."
aliases: ["SACA entropy gate", "entropy-gated CLARIFY token"]
sources: ["arxiv-2604-09824"]
---
# Grounding-entropy clarification gate

> A robot policy asks only when its own goal-to-entity attention cannot
> commit — and that same entropy, thresholded, is a calibrated selective
> predictor, not just a trigger.

## Definition / Mechanism

In Darabi & Trivedi (2026)'s ProGAL-VLA, a slow
planner turns a language instruction into a short symbolic sub-goal (e.g.
"grasp green mug"), and a cross-attention module (State Alignment Cross
Attention, SACA) grounds that sub-goal against an entity-centric 3D scene
graph by attending over the graph's entities as keys and values. The
attention distribution's entropy is read off directly as an ambiguity
signal: "The attention distribution links st to specific 3D entities. Its
entropy provides an intrinsic ambiguity signal: low entropy indicates a
unique grounding, while high entropy reveals that the instruction cannot
be resolved to a single entity. Only the verified goal embedding gt is
passed to the controller."[^c1]

Thresholding this entropy is the *ask* decision: when an instruction
under-determines which entity is meant (e.g. "pick up the block" with two
candidate blocks in view), the agent withholds action and emits an
explicit abstention token rather than grounding arbitrarily — "(b) for
ambiguous instructions, it abstains by outputting a clarification token
("[CLARIFY]") instead of committing to an arbitrary entity. Acting under
ambiguity is counted as failure."[^c2]

Unlike a bare threshold rule, the entropy is evaluated as a
selective-prediction score against a Risk-Coverage curve, so the same
signal is scored both as *whether to ask* (Clar@Ambig) and as a calibrated
confidence measure (AUROC, AUPR, ECE, Coverage@95, FPR@95): "AUROC
increases from 0.52 and 0.66 to 0.81, AUPR from 0.49 and 0.63 to 0.79, and
ECE decreases from 14.3 to 4.6. Coverage at 95 percent confidence rises
from 0.31 to 0.78, while FPR@95 drops from 0.72 to 0.18... Clarification
behavior improves accordingly, with Clar@Ambig increasing from 0.09 to
0.81 and unambiguous success improving from 0.74 to 0.89."
[^c3]

The ablation against an entropy-only variant (without the contrastive
grounding loss that sharpens the attention logits) shows the entropy
signal alone is weaker: the full training objective is what makes the
entropy calibrated, not merely available.

## Known as

- robotics (this work) · SACA attention entropy — the exact mechanism name
- computational linguistics · [[entropy-threshold-clarification-trigger]] — close: also gates a question on a raw entropy threshold over a label distribution, but on text attributes, hand-set, unlearned, and scored only by downstream accuracy rather than selective-prediction metrics

## Why it matters

The entropy is read from a module (SACA) trained end-to-end for a
different purpose — grounding a symbolic goal to a perceptual entity — and
the ask signal is a side effect of the verification bottleneck, not a
purpose-built uncertainty head. This separates *when to ask* from a
dedicated classifier: it falls out of making the acting policy provably
unable to bypass a verified goal.

## Limits

Demonstrated only on one attribute-collision benchmark (color/size
attribute drops) with a single clarify action and no downstream dialogue
— the paper is explicit that "the benchmark isolates a minimal, measurable
setting" and leaves pragmatic, temporal or multi-step ambiguity
unaddressed. The threshold on Ht is not reported as learned or tied to a
task-loss trade-off; only the Risk-Coverage curve, not a chosen operating
point, is verified. Transfer to physical robots with imperfect sensing is
untested (simulation only, LIBERO-Plus and the paper's own Custom
Ambiguity Benchmark).

## Related

[[entropy-threshold-clarification-trigger]], [[abstention]],
[[semantic-entropy]], [[calibration]]

[^c1]: arxiv-2604-09824 — "The attention distribution links st to specific 3D entities. Its entropy provides an intrinsic ambiguity signal: low entropy indicates a unique grounding, while high entropy reveals that the instruction cannot be resolved to a single entity. Only the verified goal embedding gt is passed to the controller."
[^c2]: arxiv-2604-09824 — "(b) for ambiguous instructions, it abstains by outputting a clarification token (“[CLARIFY]”) instead of committing to an arbitrary entity. Acting under ambiguity is counted as failure."
[^c3]: arxiv-2604-09824 — "AUROC increases from 0.52 and 0.66 to 0.81, AUPR from 0.49 and 0.63 to 0.79, and ECE decreases from 14.3 to 4.6. Coverage at 95 percent confidence rises from 0.31 to 0.78, while FPR@95 drops from 0.72 to 0.18, indicating far fewer false safe decisions. Clarification behavior improves accordingly, with Clar@Ambig increasing from 0.09 to 0.81 and unambiguous success improving from 0.74 to 0.89."
