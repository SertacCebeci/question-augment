---
description: "Extra generated evidence (imagined views) helps only some queries and hurts past a point; a policy that first judges whether current evidence suffices beats always-on use at far lower cost."
aliases: ["adaptive visual imagination control", "AVIC", "when and how much to imagine", "evidence-sufficiency gating"]
sources: ["arxiv-2602-08236"]
---
# Sufficiency-gated imagination

Answering well can require evidence the question did not come with. In visual spatial reasoning, world models can render imagined views from hypothetical movements. The work treats this as a controllable resource with two separate questions: whether to invoke it at all, and how much to invoke.[^c1] Its AVIC policy first reasons about whether the observed view suffices. If so it answers directly. If not it writes a dynamic-length action plan for the imagined views.[^c2]

## What always-on use does

On SAT-Real, most instances (54%) were already answered correctly with no world model, and imagination was truly helpful in only 14%.[^c3] Always-on imagination gave only a 4.6% gain over the baseline at nearly two orders of magnitude more tokens and about 30x inference time.[^c4] An oracle that imagines only when it leads to a correct answer reaches 75.3%, against 66.6% for always-on and 62.0% for the baseline. This gap motivates selection.[^c5]

## How much

A single targeted view raised accuracy by about 4 points, and a second captured most of the remaining headroom. Beyond two views there was no further gain and eventually a loss, as rendering artifacts and redundant content accumulated.[^c6] Imagination helped most for action-conditioned questions (how a scene changes under movement) and little for questions answerable from what was already seen.[^c7]

## Both controls are needed

In an ablation on SAT-Real, always-on use gave 77.3% at 12.34 world-model calls. Gating alone cut calls to 0.51 but lowered accuracy to 73.3%, below the 74.0% vanilla baseline. Gating plus action-level scaling gave the best result, 79.3% at 0.73 calls.[^c8]

## Training the gate

With no ground truth for the best imagination, AVIC-R trains the policy with GRPO. The reward is QA correctness, a cost per action, and a wrong-skip penalty. Without the wrong-skip penalty the policy collapsed to never calling the world model, and accuracy fell from 77.33% to 62.67%.[^c9] My inference: a cost-only reward makes "skip" a safe default, so the penalty is what keeps the gate honest about uncertainty.

## Limits

- Results are on spatial benchmarks (SAT, MMSI, R2R) with specific world models. The work does not test whether the 2-view saturation point or the 14% helpful share transfers to other evidence-generation tools.
- The wrong-skip penalty and cost weights are tuned design choices. How sensitive the gate is to them is not established here.
- "Sufficiency of evidence" is judged by the policy model itself, so errors in its self-assessment are not separated from errors in planning.
- The oracle upper bound uses hindsight correctness and is not reachable by any real policy.

## Related

- [[selective-abstraction]] — also a per-instance decision about how much to commit, but over answer detail, not evidence gathering.
- [[accuracy-masks-selective-reliability]] — aggregate accuracy hides instance-dependent behavior, as the 54/14% split does here.
- [[moderate-adaptive-reasoning-length]] — another adaptive compute-allocation result with a point past which more hurts.

[^c1]: arxiv-2602-08236 — "when should a model invoke visual imagination, and how much imagined visual evidence is necessary if imagination is required."
[^c2]: arxiv-2602-08236 — "the policy first reasons about the sufficiency of the available visual evidence and conditionally"
[^c3]: arxiv-2602-08236 — "the majority of instances (54%) fall into Case 3, where the model already answers correctly without"
[^c4]: arxiv-2602-08236 — "While always-on imagination yields only a 4.6% accuracy gain over"
[^c5]: arxiv-2602-08236 — "only marginally improves to 66.6%, whereas this selective upper bound jumps to 75.3%,"
[^c6]: arxiv-2602-08236 — "Beyond two views, additional rollouts bring no further gains"
[^c7]: arxiv-2602-08236 — "world models are most beneficial for action-conditioned spatial reasoning"
[^c8]: arxiv-2602-08236 — "drastically reduces WM usage (0.51 calls) but also hurts accuracy (73.3%), indicating that binary"
[^c9]: arxiv-2602-08236 — "The skip-wrong term lifts overall"
