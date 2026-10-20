---
description: "START masks answer-token gradients in a first RL phase so reward can only be earned by improving the thinking trace, then trains jointly; it beat joint GRPO on ExpertQA."
aliases: ["START", "gradient-masked thinking training", "answer-as-environment RL"]
sources: ["arxiv-2603-20799"]
---
# Separated thinking and response training

START (Separated Thinking And Response Training) is a two-phase RL recipe aimed at [[thinking-stagnation]]: in general QA, joint RL lets the policy raise reward through the answer tokens and leave the thinking alone.

## Mechanism

Phase I treats answer generation as part of the environment. The model still samples [T, A] and the reward is computed on the full response, but a binary mask zeroes the policy-gradient term for every answer token, so only thinking tokens are updated.[^c1] The authors state the consequence: the model "is physically unable to improve its reward by merely adjusting its answering", so a better thinking trace is the only way to raise the advantage.[^c2] Phase II removes the mask and optimises thinking and answer jointly so the answer learns to use the new thinking.[^c3] The change is one token-level mask in the loss, with outcome reward models and no step-level annotation, so it plugs into GRPO or DAPO.[^c4]

## What was measured

On ExpertQA with Qwen3-1.7B, using the cross-generation split from thinking-stagnation, GRPO+START thinking paired with the frozen base answerer won 68.15% head-to-head against vanilla GRPO, direct evidence that thinking improved. The full model won 59.24% with reward about 0.220 against 0.2182.[^c5] A baseline that samples several answers per thought (GRPO-MA) improved thinking only moderately (54.14%) and plateaued lower; the authors argue joint optimisation still lets the model take the cheaper route through answer tokens, and that fewer unique thoughts are explored under a fixed sampling budget.[^c6] Gains were also reported with DAPO and on UltraFeedback.

## Limits

- Final-answer reward gains are small (0.2182 to 0.2201); the large effect is on the isolated thinking metric.
- One small model family and two datasets in the main comparison; no test on verifiable reasoning, and the mechanism claim (shortcut removal) is the authors' interpretation.
- The win rates are judged by a model, and the number of Phase I steps appears set by hand (about 600 steps in the shown run), not derived.
- The meta-context analysis of richer traces is descriptive and was not checked here.

## Related

- [[thinking-stagnation]] — the failure START is built to remove.
- [[reasoning-shortcut]] — reward shortcuts that bypass the intended reasoning.
- [[rlvr-answering-bias]] — outcome reward concentrating on answering behaviour.
- [[reward-only-advantage-miscalibration]] — outcome-only advantage that credits the wrong part of a sequence.

[^c1]: arxiv-2603-20799 — "During the backward pass of the RL objective (e.g., GRPO), we apply a gradient mask to the answer part."
[^c2]: arxiv-2603-20799 — "Because the gradients for tokens in A are zeroed out, the model is physically unable to improve its reward by merely adjusting its answering."
[^c3]: arxiv-2603-20799 — "the gradient mask is removed (Mi = 1 for all i ∈ T ∪ A), allowing the model to jointly optimize both thinking and answering."
[^c4]: arxiv-2603-20799 — "It requires only a minor modification to the loss calculation (a simple token-level mask)"
[^c5]: arxiv-2603-20799 — "GRPO+START achieves a remarkable 68.15% win rate against the vanilla GRPO baseline."
[^c6]: arxiv-2603-20799 — "its optimization remains joint."
