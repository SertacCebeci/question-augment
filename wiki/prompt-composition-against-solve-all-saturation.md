---
description: "As RL training proceeds, solved prompts pile up and add no gradient; chaining two prompts through an answer-defined variable makes easy ones hard again and raised benchmark scores in 4B-30B models."
aliases: ["Composition-RL", "sequential prompt composition", "solve-all prompts", "compositional depth curriculum"]
sources: ["arxiv-2602-12036"]
---
# Prompt composition against solve-all saturation

In RL with verifiable rewards, a prompt whose sampled answers are all correct ("solve all") gives zero advantage, like one whose answers are all wrong. Earlier data-efficiency work targeted the all-wrong prompts; this work measures the opposite tail growing as the policy improves, and repairs it by building harder prompts from the easy ones.[^c1] See [[zero-variance-group-waste]] for why both tails are wasted.

## The saturation

On Qwen3-4B-Base trained on the 12K-problem MATH set, the solve-all ratio rose from near zero to over 50% within 50 steps and settled near 75%. That leaves about 3K effectively usable prompts even with dynamic sampling, while the solve-none ratio stayed around 5%.[^c2]

## The composition operator

Two prompts q1, q2 with answers gt1, gt2 are joined in three steps: define a variable naming q1's numeric answer, replace a number in q2 with a new variable, and add a sentence relating the two ("Y is 6 less than X"). The composed prompt's answer is gt2, and it cannot be solved without solving q1 first.[^c3] Applied recursively K-1 times, K is the compositional depth.[^c4] The method trains with the ordinary GRPO objective on the composed set; the first K-1 prompts are drawn from small random pools of 20, resampled each time, and K=2 is the default.[^c5]

## What was measured

- Composition makes solved prompts hard: on a MATH500 subset the solve-all rate fell from 81.5% to 41.4% for one 1.5B model and from 88.5% to 60.0% for another.[^c6]
- Training on composed prompts beat training on the originals on every size; overall math gains were +3.6, +4.8, +6.1 and +14.3 points for 4B, 8B, 14B and 30B-A3B.[^c7]
- A curriculum that moves from depth 1 to depth 2 beat training directly on the composed set, and a depth-3 stage added a further gain.[^c8]
- Direct concatenation of the same two questions, without making q2 depend on gt1, did worse than the original data; the authors attribute this to distribution shift.[^c9]

## Proposed mechanisms (the authors' interpretation)

Two readings are offered. Skill recombination: models trained on composed prompts did better on depth-2 test prompts and, they argue, on standard ones.[^c10] Implicit process supervision: because the answer to q1 must be found before q2 can be solved, a final-answer reward also pushes the model toward the correct intermediate value; the model's recovery of v1 improved during training.[^c11] The authors frame this as support, not proof.

## Limits

- Math only for the main results, with numeric answers that the LLM can turn into a variable; the cross-domain physics-plus-math experiment is not covered here.
- Gains are against RL on the original set, not against other methods for exploiting solved prompts under the same compute (not checked by me).
- The mechanism claims (skill recombination, process supervision) are correlational; no intervention isolates them.
- The 30B-A3B gain (+14.3) is much larger than the rest, and the paper itself notes the MoE underperforms the 14B model.
- Composition lowers pass rate, but the measured drop (solve-all 41-60% left) shows many composed prompts are still solved.
- Not examined: whether composed prompts of unnatural phrasing teach the model to read a puzzle form rather than reason.

## Related

- [[zero-variance-group-waste]] — the all-agree waste this note tries to reverse at the top end
- [[curriculum-collapse]] — a failure mode of difficulty curricula; here depth rises stepwise
- [[learnability-posterior-curriculum]] — another way to keep prompts near the learnable boundary
- [[model-dependent-benchmark-difficulty]] — difficulty is relative to the current policy, so solve-all grows

[^c1]: arxiv-2602-12036 — "However, easy prompts with a pass rate of 1 also become increasingly prevalent as training progresses, thereby reducing the effective data size."
[^c2]: arxiv-2602-12036 — "The solve all ratio rises rapidly from near zero to over 50% within the first 50 steps and then stabilizes around 75%."
[^c3]: arxiv-2602-12036 — "This composition is asymmetric to the order of q1 and q2 ,"
[^c4]: arxiv-2602-12036 — "We term K as the Compositional Depth."
[^c5]: arxiv-2602-12036 — "Unless otherwise specified, we use K = 2 in all remaining"
[^c6]: arxiv-2602-12036 — "The solve all rate also drops substantially: from 81.5% to 41.4% for"
[^c7]: arxiv-2602-12036 — "Across all model sizes, Composition-RL improves the overall mathematics performance by +3.6%, +4.8%, +6.1%,"
[^c8]: arxiv-2602-12036 — "Depth 1→Depth 2 curriculum even outperforms training"
[^c9]: arxiv-2602-12036 — "this direct-concatenation variant performs even worse than RL training on the original"
[^c10]: arxiv-2602-12036 — "This result supports compositional generalization: models"
[^c11]: arxiv-2602-12036 — "the steady improvement in recovering"
