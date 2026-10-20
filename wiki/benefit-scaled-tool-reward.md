---
description: "A tool call is rewarded in proportion to the paired accuracy gain it brings on that sample, penalized where the gain is negative, and the penalty grows with the number of calls."
aliases: ["Tool Benefit Score", "adaptive tool-use reward", "AT-GRPO reward scaling", "tool benefit delta S"]
sources: ["arxiv-2512-16918", "arxiv-2512-14157", "arxiv-2512-13874", "arxiv-2512-05111", "arxiv-2512-01224"]
---
# Benefit-scaled tool reward

> A tool call earns credit only where the same question answered with the tool beats the same question answered without it; where it does not, each further call is a cost.

## Mechanism

A multimodal model that reasons by calling vision tools (cropping, frame extraction) can call them when they are not needed. The authors of AdaTooler-V describe this as a training problem: "existing open-source models often exhibit blind tool-use reasoning patterns, invoking vision tools even when they are unnecessary".[^c1] Their fix makes the reward depend on a per-sample quantity, the Tool Benefit Score ΔS, defined "to quantify the performance improvement brought by tool-use".[^c2] It is computed offline, during data annotation: the same query is answered several times with tools and several times without, and "the averaged accuracy gap is used as" the score.[^c3] A reference model (Qwen2.5-VL-72B) produces the runs, so ΔS is a property of the training item under that model, not of the policy being trained.

The score is used as a reward scale rather than a label. For a response that makes n_tool calls, the tool reward is ΔS multiplied by a decay in the call count around a chosen maximum n_max; the decay is Gaussian-type, and "γ controls the sensitivity of the Gaussian decay to tool frequency", set to 2 in the paper.[^c9] The sign of ΔS decides the direction. When the tool does not help, the reward is negative and "the model is penalized if it still invokes such tools during the reasoning process, and the penalty increases progressively with the number of tool-use."[^c4] When it does help, "the model receives a positive reward and the reward similarly grows with the number of tool-use."[^c10] This tool reward is added with a weight α to the ordinary correctness-and-format reward, and the total is normalized within each GRPO group, so a sample with ΔS near zero contributes almost nothing to the tool term.

What the mechanism does, as the authors report it, is shift behaviour during RL. The base is an SFT model that learned to call tools on instruction; "the model quickly realizes that, for most tasks, generating a direct text response is more efficient than performing a tool-based analysis", and the number of unnecessary calls falls quickly.[^c5] In their ablation, "dynamically adjusting tool-use rewards based on the Tool Benefit Score enables the model to invoke tools only when necessary", compared with the same pipeline using standard GRPO.[^c6] Removing tools altogether from the RL stage gives lower scores, with "disabling tool interactions leads to consistent drops" across four benchmarks.[^c7]

## What transfers

The useful part is the unit of measurement: the same item answered with and without an aid, and the difference taken as the aid's worth on that item. The paired contrast is the same object that [[counterfactual-search-routing-oracle]] and [[internal-prober]] estimate, for search and retrieval respectively. Those works turn the contrast into a label (search or no search) or a predicted gain used to gate a single decision. Here it becomes a continuous, signed scale on a reward, so the same measurement both rewards useful calls and charges for harmful ones. The sign flip is what distinguishes this from simply rewarding tool success.

A different tool reward appears in Ophiuchus, a medical model trained with RL on zoom and segmentation tools. Its tool term is not a paired benefit at all. It is a flat bonus "granted only when the model both produces a correct answer and invokes at least one external perception tool during its trajectory".[^c11] The gate is the final outcome, not a with-and-without contrast on the item. Under that definition a correct answer reached with a tool call earns the bonus whether or not the tool changed the answer; that is my reading of the definition, and the bonus does not measure the tool's worth on the item. The authors ablate three settings, no tool reward, an unconditional one, and the conditional one, and report that "the conditional reward yields the highest accuracy, outperforming the other settings".[^c12] Their conclusion is that "rewarding tool use alone is insufficient".[^c13] The comparison does not include a paired-benefit reward, so it does not say whether ΔS-scaling would do better than the gated bonus. The two designs price a tool call by different things: the item's counterfactual in one, the final outcome in the other.

A third design is in ARM-Thinker, a judge rather than a generator. Its tool term starts as a bonus for a reasonable attempt at a call, since "the objective is to encourage the model to actively explore tool usage"[^c15]; later credit is attached to a correct final answer where tool use helped. Its ablation compares three reward designs. The accuracy-and-format reward, with no tool term, makes the fewest calls (about 0.7 per response) and ends "finishing last at 77.5%".[^c16] A fixed per-call bonus pushes calls up to about 1.15 and reaches 78.5%, and the authors conclude that "a constant bonus induces overuse and that simply maximizing tool calls is ineffective."[^c17] This is the pressure the sign-flipped paired benefit is built against: a reward that never asks whether a call helped drifts toward overuse or underuse. The ARM gate does not measure a per-item benefit, so these numbers do not test ΔS-scaling against a gate. (my reading)

A fourth design comes from a verifier that checks answers by running code. It pays on both sides of the same gate. The bonus is for a correct verdict reached with at least one tool call, and the paper says it awards "a bonus when the model is correct and uses an" external tool.[^c18] The penalty is for a wrong verdict with no tool call, since the paper says it imposes "a penalty when the model is incorrect without relying on function calling".[^c19] A wrong verdict that did use a tool is not penalized by this term. So the reward prices the omission of computation, not the call. The paper does not compare this with a paired benefit, so it does not test ΔS-scaling against a gate. (my reading)

## Limits

- The benefit is estimated by one reference model. The paper states that "the estimation of tool benefit (ΔS) relies on a single reference model, which may introduce biased assessments of when tool use is genuinely helpful".[^c8] A tool that helps the 72B reference may not help the 7B policy being trained, so ΔS is a training-side proxy for the policy's own benefit.
- ΔS is an average over a small number of runs per condition. Near zero, its sign is noisy; the sections of the text I read do not show how the reward changes with the number of runs or with the sign threshold.
- At inference the model must decide from the question alone, and ΔS is available only during training. The paper reports that the trained policy calls tools less and scores higher on its benchmarks; it does not measure how well the policy predicts ΔS on held-out items. That prediction is my inference from the design, not a result.
- Evaluation is on one backbone family (Qwen2.5-VL-7B) and its twelve benchmarks. The n_max and γ choices are not varied in the parts I read. Whether a lower tool rate is the same thing as better adaptivity, rather than an effect of the shorter-response dynamics in RL, is not separated.

## Related

- [[counterfactual-search-routing-oracle]] — the same paired with-and-without contrast, turned into a binary routing label; this note keeps it as a graded reward scale.
- [[internal-prober]] — predicts the same kind of log-ratio gain before generation to decide whether to retrieve; the benefit target is shared, the use differs.
- [[groundedness-gated-tool-routing]] — chooses which tool to call from the entity's grounding; here the tool's worth is a training-time signal, not the routing rule.
- [[any-horizon-reasoning]] — SAGE also trains against unnecessary calls, but with fixed per-step scores rather than a paired benefit; the charge against extra calls falls on the final answer's penalty, not on the call itself.[^c14]
- [[agentic-reward-model]] — a judge that calls tools before scoring; its tool bonus is an early exploration term followed by a credit gated on the final answer, a different pricing from the paired benefit here.

[^c1]: arxiv-2512-16918 — "existing open-source models often exhibit blind tool-use reasoning patterns, invoking vision tools even when they are unnecessary"
[^c2]: arxiv-2512-16918 — "to quantify the performance improvement brought by tool-use"
[^c3]: arxiv-2512-16918 — "the averaged accuracy gap is used as"
[^c4]: arxiv-2512-16918 — "the model is penalized if it still invokes such tools during the reasoning process, and the penalty increases progressively with the number of tool-use"
[^c5]: arxiv-2512-16918 — "the model quickly realizes that, for most tasks, generating a direct text response is more efficient than"
[^c6]: arxiv-2512-16918 — "dynamically adjusting tool-use rewards based on the Tool Benefit Score enables the model to invoke tools"
[^c7]: arxiv-2512-16918 — "disabling tool interactions leads to consistent drops"
[^c8]: arxiv-2512-16918 — "relies on a single reference model, which may introduce biased assessments of when tool use is genuinely helpful"
[^c9]: arxiv-2512-16918 — "γ controls the sensitivity of the Gaussian decay to tool frequency"
[^c10]: arxiv-2512-16918 — "the model receives a positive reward and the reward similarly grows with the number of tool-use"
[^c11]: arxiv-2512-14157 — "granted only when the model both produces a correct answer and invokes at least one external perception tool during its trajectory"
[^c12]: arxiv-2512-14157 — "the conditional reward yields the highest accuracy, outperforming the other settings"
[^c13]: arxiv-2512-14157 — "rewarding tool use alone is insufficient"
[^c14]: arxiv-2512-13874 — "+0.10, if current tool call is reasonable"
[^c15]: arxiv-2512-05111 — "the objective is to encourage the model to actively explore tool usage"
[^c16]: arxiv-2512-05111 — "finishing last at 77.5%"
[^c17]: arxiv-2512-05111 — "a constant bonus induces overuse and that simply maximizing tool calls is ineffective"
[^c18]: arxiv-2512-01224 — "We award a bonus when the model is correct and uses an"
[^c19]: arxiv-2512-01224 — "impose a penalty when the model is incorrect without relying on function calling"
