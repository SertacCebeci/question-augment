---
description: "Keeping only the coordinate path of a maze solution, not its verbal or image-editing steps, gave the best cross-size generalization of three chain-of-thought formats for a vision-language model."
aliases: ["short is long effect", "least-grounded CoT", "grounding-only supervision", "coordinate-path chain of thought", "implicit reasoning after grounding"]
sources: ["arxiv-2511-22586"]
---
# Least-grounded trace supervision

Before reinforcement learning, a vision-language model can be fine-tuned on worked traces, and what a trace keeps may matter more than how long it is. In a controlled maze benchmark, Qwen2.5-VL-7B was fine-tuned on three formats: a language chain of thought, a grounding chain, and a visual chain that edits the image. The grounding chain writes a coordinate for every cell it steps through: "Grounding CoT in the maze navigation task refers to every stepped grid with".[^l1] The variant that keeps only the least grounded content, a bare coordinate path with no explanation, generalized best: "CoT formats containing only the least grounded information (e.g., sparse coordinate paths) generalize best".[^l2]

The authors read this as a grounding effect rather than a length effect. Once the model's grounding is aligned with the environment, it can act without writing the path out in full: the model "can internalize and operate over its own latent spatial representations without relying on externally specified coordinate systems".[^l3] They offer the compact path as "a more flexible and compact inductive bias".[^l4] This is their hypothesis, not something the experiments isolate.

The generalization test has two forms. In the single-scale form, the model is trained with SFT and RL on 6 × 6 mazes and tested on unseen 7 × 7 mazes. In the cross-scale form, it is fine-tuned on mazes from 4 × 4 to 6 × 6, trained with RL on "mazes sized 7 × 7 to 9 × 9, and then evaluate[d] on unseen 10 × 10 mazes".[^l5] The least-grounded model kept "high success rates on unseen maze sizes", while "Visual CoT saturates after about 800 RL steps".[^l6] The authors attribute this to the trace encouraging "the model to internalize scale-invariant, local navigation rules".[^l7]

The mechanism that transfers is narrow. A trace can be shortened to what the policy must locate, and the explanation the policy does not need can be dropped without loss on this task. The authors summarize it as "concise but well-grounded supervision appears more effective for learning reusable visual reasoning patterns than verbose, heavily supervised traces".[^l8] Whether a bare path beats a short verbal rationale in a task where the rule cannot be read off the image is not tested here.

## Limits

- One model, one task family. The cross-scale results use the maze alone. The other tasks (FrozenLake, a jigsaw) are tested on a single size: "All training and evaluation are conducted on 4 × 4 grids".[^l9] The main experiments use "Using Qwen2.5-VL-7B under a standard SFT-then-RL pipeline".[^l10]
- The generalization comparison is narrow. The cross-scale figures set the least-grounded format against visual CoT only; language CoT is not in those curves. "Best" therefore means best among the formats compared in those figures.
- The least-grounded format still outputs the full coordinate path. The study does not separate the contribution of the path's content from the contribution of its brevity (my inference from the format definitions).
- The grounding claim is the authors' reading of training dynamics and test accuracy. No probe of the model's internal representation is reported in the part read here.
- Speed and generalization are different results. The least-grounded model also converged faster, "even surpassing the efficiency of visual CoT".[^l11] That is a separate claim, treated in [[convergence-ceiling-dissociation]].

## Related

- [[convergence-ceiling-dissociation]] — the same study's finding that extra visual or longer trace content speeds RL without raising the final ceiling
- [[moderate-adaptive-reasoning-length]] — on theory-of-mind tasks, longer reasoning lowers accuracy and capping it helps; another case where length is not the lever
- [[mentalese-symbolic-reasoning-trace]] — shortening traces by SFT costs accuracy that RL recovers only in part; the cost there is in what the short form loses
- [[cot-token-complexity-lower-bound]] — a theory in which trace length has a floor; here the trace is cut to its grounding rather than to a bound
- [[visual-forgetting-during-reasoning]] — longer chains draw attention away from the image, which would favour short grounded traces (my inference)

[^l1]: arxiv-2511-22586 — "Grounding CoT in the maze navigation task refers to every stepped grid with"
[^l2]: arxiv-2511-22586 — "CoT formats containing only the least grounded information (e.g., sparse coordinate paths) generalize best"
[^l3]: arxiv-2511-22586 — "over its own latent spatial representations without relying on externally specified coordinate systems"
[^l4]: arxiv-2511-22586 — "Least grounding may thus serve as a more flexible and compact inductive bias"
[^l5]: arxiv-2511-22586 — "perform RL on mazes sized 7 × 7 to 9 × 9, and then evaluate on unseen 10 × 10 mazes"
[^l6]: arxiv-2511-22586 — "maintaining high success rates on unseen maze sizes"
[^l7]: arxiv-2511-22586 — "encourages the model to internalize scale-invariant, local navigation rules"
[^l8]: arxiv-2511-22586 — "concise but well-grounded supervision appears more effective for learning reusable visual reasoning patterns than verbose, heavily supervised traces"
[^l9]: arxiv-2511-22586 — "All training and evaluation are conducted on 4 × 4 grids"
[^l10]: arxiv-2511-22586 — "Using Qwen2.5-VL-7B under a standard SFT-then-RL pipeline"
[^l11]: arxiv-2511-22586 — "even surpassing the efficiency of visual CoT"
