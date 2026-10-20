---
description: "A closed self-training loop where a VLM proposes questions, a frozen base model rewrites/filters them for grounding and difficulty, and retraining needs no external reward model."
aliases: ["self-evolving visual questioner", "propose-rewrite-filter loop", "self-evolving questioner framework"]
sources: ["liang-2026"]
---
# Self-evolving visual questioner

> A vision-language model (VLM) improves its own question-asking without
> human annotations, an external teacher, or a reward model, by closing a
> propose → rewrite → filter → retrain loop over unlabeled images.

## Definition / Mechanism

At round $t$, the current model $M_t$ proposes candidate questions for each
unlabeled image under several visual-intent prompts (direct recognition,
comparison, spatial relations, scene understanding, grounded reasoning),
to cover more of the per-image question space than a single unconditioned
prompt would. A separate, **frozen** initial checkpoint $M_0$ then rewrites
each proposal toward a harder, more visually grounded version and filters
the resulting question-answer candidates on answerability and
perception/reasoning difficulty. Keeping the rewriter fixed at $M_0$ is
deliberate: using the same adapted checkpoint to both propose and refine
would couple the two steps to one generation distribution and collapse
exploration.[^c1]

The retained pairs train $M_{t+1}$ in two formats at once — QA-format
(anchoring answering) and QG-format (teaching question generation) — and
$M_{t+1}$ becomes the proposer for round $t+1$, closing the loop.[^c2]

No human annotation, external teacher model, or auxiliary reward model
enters at any step; the supervision is entirely self-generated and
self-filtered.[^c3]

After two rounds the average question-generation (QG) quality score rises
about 82% relative to the initial base model, while QA accuracy stays
stable or improves on several benchmarks.[^c4]

## Why it matters

The information-theoretic and decision-theoretic answers on this stall
([[mutual-information|mutual information]], EIG, GBS) are all **per-step selection rules**: given
a fixed asking policy, score each candidate question and take the best.
This method instead trains the policy itself, using the frozen
initial model as an internal, cost-free critic that pulls each round's
proposals toward harder and more diverse questions — an alternative to
computing a selection criterion at ask-time: push the asking behavior
itself toward better selection during training.

## Limits

The claim rests on filtering and rewriting being done by the *same model
family* as the proposer (a frozen earlier checkpoint), so any systematic
bias the base model has about what counts as "grounded" or "hard" is
inherited by every round rather than corrected; the paper reports the
method only on vision-language backbones and unlabeled *image* collections,
so whether an analogous propose-rewrite-filter loop transfers to text-only
or tool-using agentic questioning is untested here.

## Related

[[investigative-question-grpo-training]] · [[question-generation-as-policy]] · [[action-based-contrastive-self-training]] · [[expected-information-gain]]

[^c1]: liang-2026
[^c2]: liang-2026 — "The refined supervision is used for dual-format training with both QG-format and QA-format objectives, producing an updated model Mt+1 . The updated model is reused as the proposer in the next round, forming an iterative self-improvement loop."
[^c3]: liang-2026 — "we propose a self-evolving visual questioner framework that enables a VLM to improve itself as a visual questioner, without human annotations, external teacher models, or auxiliary reward models."
[^c4]: liang-2026 — "After two selfevolving rounds, the average QG score increases by ∼82% relative to the initial base model."
