---
description: "A steering vector is the unit difference between mean hidden states of two labelled prompt sets, added back at a chosen layer with a signed coefficient to move a behaviour toward one side."
aliases: ["difference-of-means steering", "MD steering vector", "mean difference steering"]
sources: ["arxiv-2512-16602"]
---
# Mean-difference steering vector

A steering vector is a direction computed once from two sets of prompts and then added to the model's hidden states while it generates. Take a set P of prompts that elicit the behaviour and a set N of prompts that do not, record the last-token hidden state at one layer for each prompt, and subtract the two group means. The result is normalized to unit length, so the vector carries direction only. The prompts are run after the chat template and the generation token, so the vector reflects the state "immediately before generation."[^c1]

At inference the vector is injected at a chosen layer with a user-set intensity. The paper's formulation adds a scaled copy of the direction to every token position, "The update is applied at every decoding step as the model autoregressively generates text."[^c2] The sign of the intensity picks one of two scales, estimated separately on validation data. Those scales are set by quantile matching: the projections of refusal-positive examples are scaled to match their judge scores at the 95th percentile, and the negative side at the 5th.[^c3] A zero intensity means no intervention.

What the vector is, mechanically, is a constant offset along one direction. Its only selectivity comes from whichever behaviour is linearly carried by that direction in the activations of the chosen layer. The paper describes the baseline as "a global linear direction that separates the two activation distributions."[^c4] Nothing in the construction adapts it to the particular prompt, and the offset is applied to every token, including ones unrelated to the trigger.

## What was measured

On Qwen3-Next-80B-A3B-Thinking, which refuses 92.35% of the politically sensitive prompts in the benchmark (the paper's "high degree of political refusals"),[^c5] the mean-difference vector trained on the China-centric set cut refusals to 33.24%, against 27.06% for the ridge variant on the same set.[^c6] The same vector also weakened safety: "However, both methods degrade" safety, with refusal on the harmful JailbreakBench prompts falling to 81–82%.[^c7] The paper's conclusion is that the plain estimator reduces political refusal but trades away the safety refusal, which motivates the ridge variant in [[ridge-whitened-steering-direction]].

Two design claims come with the method. The first is that effective control needs several layers at small coefficients: the paper lists as a contribution "to multiple layers with small coefficients is necessary for effective control."[^c8] The second is that the deepest layers are excluded: "we exclude the deepest 5% of layers" from intervention, to "prevent output corruption."[^c9]

## Limits

- The vector encodes whatever separates P from N. The negative set here mixes general China questions, code, arithmetic and chat prompts, so the direction may partly encode topic or prompt format rather than refusal alone. The paper does not ablate this; that the sets' differences drive the result is my inference.
- Labels come from a judge model, not from the vector estimator. Errors in the refusal score become errors in the direction (see [[judge-scored-refusal-confidence]]).
- Over-steering is a real failure. Pushing political refusal toward its ceiling does not stay targeted: "100% refusal on political prompts causes the model" to refuse most general prompts too. The paper's usable range was about 72% refusal on political prompts with a modest rise on general prompts.[^c10]
- Steering adds no knowledge. The paper concedes that "already encoded in the model; they cannot introduce new information" applies to any such method.[^c11]
- The benchmarks cover refusal, a few general capabilities and one safety set; "these do not comprehensively cover all" capabilities, so side effects outside them are unmeasured.[^c12]

## Related

- [[ridge-whitened-steering-direction]] — the same difference, whitened by the non-refusal covariance
- [[refusal-signal-dimensionality]] — whether one direction is enough to carry refusal
- [[topology-conditioned-activation-steering]] — rebuilds the difference per query from nearest neighbours instead of one global set
- [[gated-activation-steering-for-abstention]] — the same additive offset, applied only at tokens a probe flags
- [[norm-preserving-rotation-steering]] — a steering alternative that removes a component and rescales, with no tuned strength

[^c1]: arxiv-2512-16602 — "a unit direction in a layer’s representation space that distinguishes refusal-like from compliant states"
[^c2]: arxiv-2512-16602 — "The update is applied at every decoding step as the"
[^c3]: arxiv-2512-16602 — "the Mean Difference (MD) vector at layer ℓ is defined as"
[^c4]: arxiv-2512-16602 — "This baseline captures a global linear direction that separates the two activation distributions."
[^c5]: arxiv-2512-16602 — "It exhibits a high degree of political refusals (92.35% refusal rate on CCP-SENSITIVE)."
[^c6]: arxiv-2512-16602 — "33.24% refusal rate while RMD reaches 27.06%"
[^c7]: arxiv-2512-16602 — "However, both methods degrade"
[^c8]: arxiv-2512-16602 — "to multiple layers with small coefficients is necessary for effective control."
[^c9]: arxiv-2512-16602 — "we exclude the deepest 5% of layers"
[^c10]: arxiv-2512-16602 — "we can increase the refusal rate on politics prompts"
[^c11]: arxiv-2512-16602 — "already encoded in the model; they cannot introduce new information."
[^c12]: arxiv-2512-16602 — "these do not comprehensively cover all"
