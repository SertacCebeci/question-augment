---
description: "A zoom-in step is scored by how well its region matches a reference evidence box, so a correct answer reached without looking at the evidence earns less reward than one reached by looking."
aliases: ["Rationale Fidelity Reward", "visual rationale fidelity", "box-referenced zoom reward", "evidence-box process reward"]
sources: ["arxiv-2511-23031"]
---
# Rationale-fidelity reward

When a vision-language model reasons by zooming into the image, each zoom can be checked against the region that actually holds the evidence. The ViRL paper calls the zoom sequence a "visual rationalization, the visual analogue of textual Chain-of-Thought".[^c1] Its reward for that sequence is per step: a zoom's box is compared with a reference box, and the step is paid a signed term. "it comprises a signed correctness term that directly reinforces plausible reasoning while penalizing misaligned ones".[^c2]

The mechanism has three parts. The first is the per-step term. "Each rationalization step ak receives a fidelity reward based on its spatial alignment" with the reference rationale, measured as an overlap u.[^c3] The term has a base part signed by whether u passes a soft threshold h0, and a discrete bonus that grows with each further increment of overlap above h0, so that refining a box is paid beyond merely passing. A step that takes no visual action gets nothing: "If no visual action is taken".[^c4]

The second part is an averaging with a redundancy cost. The per-step terms are averaged over the trajectory, and a penalty grows once the zooms exceed a budget, "discouraging repetitive or overlapping rationales and promoting concise reasoning".[^c5]

The third part is credit assignment. A single trajectory-level advantage would be "indiscriminately crediting or blaming all steps", so the advantage of each action is adjusted by its own fidelity: "visual rationales are adaptively modulated by" their fidelity, while textual steps keep the trajectory advantage.[^c6][^c7]

The reason for the term is a measured dissociation, which the paper states as a failure of outcome reward. "some models achieve high final-answer accuracy (e.g., Deepeyes [61] at 89.1%) while exhibiting low accuracy in their visual actions (57%)".[^c8] The reward is the image-side counterpart of the text-side point that an outcome reward "cannot distinguish between a correct answer achieved via a lucky guess" from one reached by grounded inspection.[^c9]

What the ablations show, in the sections read. Removing the fidelity reward leaves answers intact but removes the visual steps: "removing the rationale fidelity reward (answer-only supervision) collapses the model" and "Although answer accuracy remains superficially strong" (87.6% on V*).[^c10][^c11] Rewarding zoom-ins without the fidelity term does not help: "this boosts activity without improving, and often harming task accuracy", and "rationale counts rise while per-invocation fidelity stagnates".[^c12][^c13] The threshold matters in both directions. "A high success threshold (h0 = 0.5) over-penalizes early failures", while a low one, which "over-rewards weak alignments", reduces success to 75.5% by inducing "redundant, noisy rationales".[^c14][^c15] The schedule the authors use is "Lenient early to foster exploration, then progressively stricter as competence grows".[^c16]

## Limits

- The reference boxes are not human-drawn in the parts read. "visual rationale is obtained by localizing the referring expression with a detector" and the box is padded for context.[^c17] The reward is only as good as that detector and the referring expression. I did not find a human check of the references in the sections read (my inference from the text).
- The ablation table is on V* alone. The full method is "achieving the best balance (F1 = 0.88)" on that benchmark, and the component effects are not shown on other benchmarks in the sections read.[^c18]
- The authors do not use plain overlap for evaluation everywhere. In an appendix formulation they "adopt this coverage-based formulation instead of a conventional IoU for two main reasons", because "evidence-inclusive regions should not be penalized".[^c19][^c20] So "alignment" is not one fixed geometric quantity across the paper. The training reward's exact overlap is the one in the step formula; I did not confirm it is the same measure as the appendix coverage.
- Threshold values are chosen by the authors; only a few settings are reported (h0 at 0.5, 0.2, and a schedule). The sensitivity is not mapped beyond those points.
- The term presumes one reference region per step. A question whose evidence spans several regions, or a zoom that is right for a different reason than the reference, is not treated in the sections read (my inference).
- Whether the gains transfer to other backbones or to non-visual reasoning is not shown in the sections I read.

## Related

- [[crop-label-consistency-reward]] — the box-free counterpart: a zoom is scored against the model's own label with a CLIP similarity, so no reference region is needed; this note needs the reference and checks where the crop lies (my reading of the contrast).
- [[visual-evidence-scoring]] — grades the crops a zoom-reasoner cites against ground-truth boxes at release time, not as a training reward.
- [[process-outcome-consistency-verification]] — the text-side lucky-guess check that this reward's motivation parallels.
- [[evidence-grounded-step-reward]] — the same step-level evidence grounding, applied to retrieval steps in search rather than to image regions.
- [[perception-step-faithfulness]] — scores the visual claims a chain makes against the image without a reference box, where this note scores the region itself.

[^c1]: arxiv-2511-23031 — "visual rationalization, the visual analogue of textual Chain-of-Thought"
[^c2]: arxiv-2511-23031 — "it comprises a signed correctness term that directly reinforces plausible reasoning while penalizing misaligned ones"
[^c3]: arxiv-2511-23031 — "Each rationalization step ak receives a fidelity reward based on its spatial alignment"
[^c4]: arxiv-2511-23031 — "If no visual action is taken"
[^c5]: arxiv-2511-23031 — "discouraging repetitive or overlapping rationales and promoting concise reasoning"
[^c6]: arxiv-2511-23031 — "indiscriminately crediting or blaming all steps"
[^c7]: arxiv-2511-23031 — "visual rationales are adaptively modulated by"
[^c8]: arxiv-2511-23031 — "while exhibiting low accuracy in their visual actions (57%)"
[^c9]: arxiv-2511-23031 — "It cannot distinguish between a correct answer achieved via a lucky guess"
[^c10]: arxiv-2511-23031 — "removing the rationale fidelity reward (answer-only supervision) collapses the model"
[^c11]: arxiv-2511-23031 — "Although answer accuracy remains superficially strong"
[^c12]: arxiv-2511-23031 — "this boosts activity without improving, and often harming task accuracy"
[^c13]: arxiv-2511-23031 — "rationale counts rise while per-invocation fidelity stagnates"
[^c14]: arxiv-2511-23031 — "A high success threshold (h0 = 0.5) over-penalizes early failures"
[^c15]: arxiv-2511-23031 — "reducing success to 75.5%"
[^c16]: arxiv-2511-23031 — "Lenient early to foster exploration, then progressively stricter as competence grows"
[^c17]: arxiv-2511-23031 — "visual rationale is obtained by localizing the referring expression with a detector"
[^c18]: arxiv-2511-23031 — "achieving the best balance (F1 = 0.88)"
[^c19]: arxiv-2511-23031 — "We adopt this coverage-based formulation instead of a conventional IoU for two main reasons"
[^c20]: arxiv-2511-23031 — "evidence-inclusive regions should not be penalized"
