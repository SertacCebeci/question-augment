---
description: "A step-level critique is rewarded only when its binary label matches the final answer's correctness, so per-step verdicts can be trained with no step-level gold labels."
aliases: ["critique-consistency reward", "critique reward", "outcome-anchored critique reward", "R_crit"]
sources: ["arxiv-2512-15662"]
---
# Critique-consistency reward

Training a per-step verdict normally needs per-step labels, and those are the expensive part. The Stepwise Think-Critique (STC) paper avoids them. Its reward reads the critique only at the end of the trace: "Since no step-level ground-truth critiques are available during training, we derive supervision from" the correctness of the final answer.[^c1] Concretely, let z be 1 when the final answer equals the ground truth ("where y is the ground-truth answer"),[^c2] and let s_T be the binary label the critique gives to the final step. The critique reward is 1 when s_T equals z and 0 otherwise. The verdict is rewarded for agreeing with the outcome, not for matching a step-level label.

The mechanism is a credit route, not only a score. The paper normalizes the critique reward within a group of sampled trajectories, and the resulting advantage "are only back-propagated to critique tokens within" the trace.[^c3] The reasoning and format rewards, by contrast, update all tokens, because the critiques shape the next reasoning step. So the critique tokens get a gradient from the outcome-agreement signal, and the reasoning tokens get one from the answer.

The authors argue that the step-level effect follows by analogy. The reasoning reward on the final answer "can drive the learning of intermediate reasoning steps" in earlier work, and they say that "our critique reward drives the learning of intermediate" critic steps.[^c4] The stated effect is that the reward "naturally penalizes false judgments that do not lead to correct final critique".[^c5] The reported ablation is in line with this: the authors write that the rewards "effectively encourage balanced and reliable step-level critique".[^c6]

The reward sits beside the others in the paper's sum: a reasoning reward that is 1 when the final answer is correct, and a format reward that is the fraction of reasoning steps followed by a well-formed critique. Its job is narrow. It does not judge whether the trace is right; it judges whether the verdict agrees with the outcome.

The outcome-anchoring idea also appears in [[process-outcome-consistency-verification]], where a verifier rewards an answer only when its derivation is consistent with it, and in [[answer-reasoning-consistency-reward]], which scores the lift a trace gives the gold answer. Those score the whole answer or trace. This reward is different in one respect: it supervises a verdict about a step, and the only label it sees is the outcome.

## Limits

- Only the final step's critique is scored directly. The formula reads s_T alone, so every intermediate critique is trained through the authors' analogy, not through its own target. The text I read does not measure how well intermediate verdicts track their own correctness under this reward, apart from the judge-based F1 that the paper reports elsewhere (my reading of the formula).
- Agreement with the outcome is a noisy proxy for step correctness. A correct final answer can come from a wrong step, and a critic that says "correct" everywhere will be rewarded whenever the answer is right. The paper's reward does not separate those cases. The paper's evidence against this is that the critic flags "STC identifies 21% of" final answers as incorrect instead of collapsing to one label.[^c10] That shows the critic is not constant, but not that its flags are right (my inference).
- The step labels used for evaluation come from a judge, not from ground truth. The authors "use GPT-5-mini as the judge".[^c7] Under this reward the model is trained toward outcome agreement and tested against a judge, so the two are not the same target.
- The SFT stage that starts the policy used stepwise critiques written by a stronger model: "generating stepwise critiques with GPT-5, and filtering".[^c8] The critique reward is an RL stage on top of that, so its effect is not separated from the SFT data in this design.
- Single 1.5B model, single seed, mathematics only (see [[inline-step-critique]] for the same limits on the framework).
- Reward hacking was checked by inspection: "we did not observe evidence of" it.[^c9] The reward is a binary agreement, which is the kind of signal that a policy can game by setting a label that is usually right; the paper's inspection does not rule that out (my inference).

## Related

- [[inline-step-critique]] — the verdict format this reward trains, emitted inside the reasoning trace
- [[process-outcome-consistency-verification]] — a whole-derivation verifier rewarded for consistency with the outcome
- [[answer-reasoning-consistency-reward]] — an outcome-anchored reward that scores the lift a trace gives the gold answer
- [[process-reward-model-hackability]] — what a step-level score does when it is not anchored to outcomes, and how it gets exploited

[^c1]: arxiv-2512-15662 — "Since no step-level ground-truth critiques are available during training, we derive supervision from"
[^c2]: arxiv-2512-15662 — "where y is the ground-truth answer"
[^c3]: arxiv-2512-15662 — "are only back-propagated to critique tokens within"
[^c4]: arxiv-2512-15662 — "our critique reward drives the learning of intermediate"
[^c5]: arxiv-2512-15662 — "which naturally penalizes false judgments that do not lead to correct final critique"
[^c6]: arxiv-2512-15662 — "rewards effectively encourage balanced and reliable step-level critique"
[^c7]: arxiv-2512-15662 — "we use GPT-5-mini as the judge"
[^c8]: arxiv-2512-15662 — "generating stepwise critiques with GPT-5, and filtering"
[^c9]: arxiv-2512-15662 — "we did not observe evidence of"
[^c10]: arxiv-2512-15662 — "STC identifies 21% of"
