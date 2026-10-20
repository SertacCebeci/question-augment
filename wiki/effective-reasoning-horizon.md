---
description: "A reasoning model's effective horizon decides whether longer traces help: short-horizon models do best with shorter traces, long-horizon ones gain from length on hard problems."
aliases: ["short-horizon and long-horizon models", "large-horizon models", "horizon category of a reasoning model"]
sources: ["arxiv-2512-02008"]
---
# Effective reasoning horizon

A reasoning model has an effective horizon: how long a coherent chain of thought it can keep up. The horizon is a property of the model, not of the question, and it is what decides whether spending more tokens on one answer pays. The paper's definition of the two classes is by what they can do: "Models with large horizons (large-horizon models) are able to sustain deeper reasoning by means of longer traces" and so benefit "on harder tasks where greater thought is necessary".[^h1] The other class is defined by a limit: "Short-horizon models, however, cannot generate long coherent traces".[^h2]

The horizon is read off behaviour, not set by a parameter count. The authors group models by how their accuracy moves with trace length inside each model. The trace length is labelled short or long against "the model-specific median trace length", so a trace is short only relative to its own model.[^h3] For the short-horizon models (R1, DAPO-32B, QwQ-32B) the table's rule is "Shorter is always better".[^h4] For the long-horizon models (GPT-OSS-120B, Qwen3-32B, R1-32B) the rule splits by difficulty: "Shorter is better for easy" problems, and "better for hard problems" the longer trace.[^h5] The two non-reasoning models fall with the short-horizon group under the same label.

The paper attributes the horizon to training. Its stated account is "a divergence we attribute to differences in their post-training algorithms", and it ties the short horizon to GRPO-type training: "short-horizon models commonly emerge" from post-training with GRPO or GRPO-like algorithms, which the authors connect to the length bias that GRPO is known to introduce.[^h6] The claim it tests is put as a hypothesis: "the choice of post-training strategy plays a key role in determining" the effective horizon.[^h7]

What this changes on the compute side. Beam search, a method that spends more compute as its width grows, "exhibits a consistent inverse-scaling pattern: performance degrades monotonically as" the beam widens, in the short-horizon and non-reasoning families.[^h8] The same paper reports that "no single TTS strategy universally dominates", and that for a given model type the best achievable performance rises with compute, "the optimal TTS performance scales monotonically with compute budget".[^h9] So the horizon sets which strategy and which trace length to use, while the budget sets how far it can go.

Trace length alone is a poor signal. Both model families "think longer for harder problems", which makes length a symptom of difficulty; the paper adds that "longer trace lengths alone do not guarantee improved quality".[^h10] The authors also note that "problem difficulty is confounded with trace length", so a length-accuracy pattern mixes the two.[^h11]

## Limits

- The evidence is eight open-source models, from which the horizon classes are drawn. The paper's own description of its data is "two complementary reasoning benchmarks", AIME and GPQA Diamond, so the classes are not tested on other task types.[^h12]
- The post-training account is a hypothesis in the text, and no run varies the training algorithm while holding the base model fixed. The family assignments are correlational.
- The classification does not fit the training story cleanly on the text read. R1-32B is "a distilled 32B-parameter variant of DeepSeek-R1",[^h13] and yet it is listed with the long-horizon models, not with R1, which is a GRPO-trained short-horizon model in the same table. The paper's account would need the distillation to change the horizon. My inference: the GRPO explanation does not by itself cover this case, and the text read does not resolve it.
- Because the labels use each model's own median, a "long" trace of one model can be shorter than a "short" trace of another. The classes compare behaviour within models, not trace lengths across them.
- The accuracy-by-length curves are reported per cell; the slices read give no intervals, so small differences between the short and long groups are not established as real.

## Related

- [[test-time-scaling]] — the general claim that the gain from extra compute depends on the model and the task; this note names one model-side cause, the horizon, for the length axis.
- [[moderate-adaptive-reasoning-length]] — capping reasoning length helps on hard tasks and the best cap varies by model and task; the same length dependence seen from a token cap.
- [[complexity-tiered-strategy-routing]] — routes compute by inferred difficulty; the horizon note adds that the right length can also depend on which model is doing the reasoning.
- [[normalized-logit-difference-decay]] — its alias "reasoning horizon" names a different quantity. I did not read its body, so whether the two conflict is not decided here.

[^h1]: arxiv-2512-02008 — "Models with large horizons (large-horizon models) are able to sustain deeper reasoning by means of longer traces"
[^h2]: arxiv-2512-02008 — "Short-horizon models, however, cannot generate long coherent traces"
[^h3]: arxiv-2512-02008 — "model-specific median trace length"
[^h4]: arxiv-2512-02008 — "Shorter is always better"
[^h5]: arxiv-2512-02008 — "Shorter is better for easy"
[^h6]: arxiv-2512-02008 — "short-horizon models commonly emerge"
[^h7]: arxiv-2512-02008 — "the choice of post-training strategy plays a key role in determining"
[^h8]: arxiv-2512-02008 — "exhibits a consistent inverse-scaling pattern: performance degrades monotonically as"
[^h9]: arxiv-2512-02008 — "the optimal TTS performance scales monotonically with compute budget"
[^h10]: arxiv-2512-02008 — "Both reasoning and non-reasoning models think longer for harder problems"
[^h11]: arxiv-2512-02008 — "problem difficulty is confounded with trace length"
[^h12]: arxiv-2512-02008 — "We evaluate models on two complementary reasoning benchmarks"
[^h13]: arxiv-2512-02008 — "R1-32B is a distilled 32B-parameter variant of DeepSeek-R1"
