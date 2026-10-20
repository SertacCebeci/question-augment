---
description: "Visual thoughts as continuous hidden-state tokens, trained to match embeddings of intermediate sketch images, let an MLLM interleave visual and textual reasoning without tools or pixels."
aliases: ["latent sketch tokens", "visual sketching mode", "latent visual semantics reconstruction", "visual thoughts in latent space", "SkiLa"]
sources: ["arxiv-2512-16584", "arxiv-2511-19418"]
---
# Latent visual thought

A multimodal model can carry a visual step through its reasoning without drawing it and without calling a tool, provided its hidden states are trained to hold visual content. The mechanism has three parts.

First, a mode switch. The model generates ordinary text tokens until it emits a sketch-start marker; from then on it "autoregressively generates a sequence of continuous latent" tokens, feeding its last hidden state back as the next input embedding, until a sketch-end marker returns it to text.[^c1] These latent tokens are never decoded into pixels; they condition the language that follows.[^c2]

Second, a target. During training a separate sketch encoder turns each intermediate sketch image in the reasoning trace into features, which are projected into the LLM's embedding space and then average-pooled, "we apply average pooling to compress the projected".[^c3] The generated latent tokens are pushed toward these features with a mean-squared error, "to approximate the ground-truth visual semantics".[^c4] The loss is added to ordinary next-token cross-entropy with a weight of 0.5.[^c5] The authors name this latent visual semantics reconstruction: "we introduce a latent visual semantics reconstruction mechanism".[^c6] The transferable part is the supervision. The latent step is pinned to an external encoder's view of a picture the reasoning is meant to depict, not left to be shaped only by the text that comes after it.

Third, a cost profile. The sketch encoder and projector are used only in training, and "discarded, incurring zero additional parameter or computational cost compared to a standard MLLM."[^c7] The trained model at inference is an ordinary MLLM run with a different decoding loop.

The reported effect is on one base model. The authors start from "We adopt Qwen2.5-VL 7B [3] as the base model."[^c8] They report that their models "consistently outperform the Qwen2.5VL 7B baseline across all evaluated benchmarks" on the vision-centric and multimodal sets.[^c9] They credit the reconstruction target for the fine-grained perception gains: "visual semantics reconstruction enables the model to effectively imagine such visual" detail.[^c10] The spatial case is the clearest. Text-only methods "consistently fail on spatial tasks", and the model instead generates visual thoughts "to mentally simulate the" 3D object and compares it with the candidate options.[^c11]

What this changes for asking and answering, as my inference and not the paper's claim: when the answer depends on a configuration that words describe poorly, the reasoning medium matters, not only the length of the text. The paper's premise for this is that "given that current MLLMs already encode visual and text information in the same feature space" visual tokens can be inserted into text reasoning.[^c12] That premise is the paper's, and the note does not test it.

## Limits

- The mechanism is validated only where a reconstructable sketch exists. The training data was filtered: 3D data and instances where the sketch images were "complex for the MLLM to effectively learn to reconstruct" were excluded, leaving 101K samples.[^c13] The selection is part of the result, and the note cannot say how the method fares on traces that are not filtered this way.
- One base model and one training recipe. The sketch token count and loss weight were chosen on the same benchmarks reported. The token-count sweep shows the method "consistently outperforms the baseline across a wide range of token counts, from 1 to 81," but the gain is a benchmark average, not a per-task rate.[^c14]
- The paper reports benchmark scores, ablations over encoder, token count and loss weight, and selected case figures. In the sections read, none perturbs or swaps the latent sketch tokens to test whether the answer depends on them. Whether the latent tokens are causally used is therefore not established here (my inference from the sections read). The same question is raised for continuous latent reasoning in [[latent-token-causal-insensitivity]].
- "Semantically grounded" means matching a sketch encoder's features. Whether those features correspond to what a human would call the sketch is not tested.
- The spatial examples are chosen illustrations, not a measured rate. The authors' own next step is "that autonomously select the optimal reasoning pattern" among textual, visual and joint reasoning, which they have not done.[^c15]

## Related

- [[latent-token-causal-insensitivity]] — COCONUT-style latent tokens can be insensitive to perturbation; this paper's visual tokens are pinned to a reconstruction target, but it does not run the test that note describes.
- [[latent-rationale-variable]] — a latent reasoning variable is defined by its role in the likelihood; here the latent is additionally tied to an external encoder's features.
- [[noisy-latent-path-agreement]] — also works on continuous latent trajectories, but reads answer agreement, not visual content.
- [[sufficiency-gated-imagination]] — imagination as externally rendered evidence, gated per query; this note is imagination inside the model's hidden states, with no gate.
- [[decoder-level-latent-alignment]] — a sibling design: Chain-of-Visual-Thought aligns task-expert tokens through the expert's decoder and uses feature matching only for representation experts, "while representation-based signals are aligned in feature space."[^c16]

[^c1]: arxiv-2512-16584 — "where it autoregressively generates a sequence of continuous latent"
[^c2]: arxiv-2512-16584 — "without ever being decoded into pixels."
[^c3]: arxiv-2512-16584 — "we apply average pooling to compress the projected"
[^c4]: arxiv-2512-16584 — "We enforce these generated latent sketch tokens to approximate the ground-truth visual semantics"
[^c5]: arxiv-2512-16584 — "as the default latent sketch reconstruction loss weight."
[^c6]: arxiv-2512-16584 — "we introduce a latent visual semantics reconstruction mechanism"
[^c7]: arxiv-2512-16584 — "discarded, incurring zero additional parameter or computational cost compared to a standard MLLM."
[^c8]: arxiv-2512-16584 — "We adopt Qwen2.5-VL 7B [3] as the base model."
[^c9]: arxiv-2512-16584 — "Overall, our models consistently outperform the Qwen2.5VL 7B baseline across all evaluated benchmarks"
[^c10]: arxiv-2512-16584 — "visual semantics reconstruction enables the model to effectively imagine such visual"
[^c11]: arxiv-2512-16584 — "generating visual thoughts to mentally simulate the"
[^c12]: arxiv-2512-16584 — "given that current MLLMs already encode visual and text information in the same feature space"
[^c13]: arxiv-2512-16584 — "complex for the MLLM to effectively learn to reconstruct."
[^c14]: arxiv-2512-16584 — "our method consistently outperforms the baseline across a wide range of token counts, from 1 to 81."
[^c15]: arxiv-2512-16584 — "that autonomously select the optimal reasoning pattern"
[^c16]: arxiv-2511-19418 — "while representation-based signals are aligned in feature space"
