---
description: "Variance of per-layer cosine velocity across a prompt's final-token hidden states rises under jailbreaks in Qwen2 but falls in Gemma, so the signal's sign depends on the safety architecture."
aliases: ["Semantic Turbulence", "laminar flow hypothesis", "layer-wise cosine velocity variance", "cosine-velocity turbulence"]
sources: ["arxiv-2512-13741"]
---
# Semantic turbulence

Semantic turbulence is a single scalar read from inside a model during one forward pass. Take the hidden state of the final token at each layer, and measure how far the representation turns between consecutive layers: the velocity is "the magnitude of the directional change between consecutive" states, which in the paper's equation is one minus the cosine similarity of neighbouring layers.[^c2] The turbulence of a prompt is the variance of these per-layer velocities, "the variance of layer-wise cosine velocity".[^c1] The calculation is restricted to the middle of the network, "were strictly restricted to the reasoning layers of" the model, so that the embedding and vocabulary-projection layers do not dominate the variance.[^c3] No auxiliary classifier and no training are involved; the metric is a read-out of the base model's own dynamics.

The hypothesis behind it, which the paper calls the Laminar Flow Hypothesis, is that benign prompts move through representation space smoothly while adversarial prompts make the path jerky. The stated mechanism is a clash inside the network: "jailbreak attempts trigger a high-variance conflict" between safety inhibition and instruction following.[^c4] The paper illustrates this with one benign and one jailbreak trajectory. The clash itself is not measured separately; it is the explanation offered for the variance.

The measured result is a difference in means on two small safety-tuned models. On Qwen2-1.5B-Instruct, the mean turbulence rose from 1.20 × 10⁻³ to 2.10 × 10⁻³, "representing a relative surge of +75.4% (p < 0.001)".[^c5] On Gemma-2B-IT the sign reversed: "Gemma exhibited a statistically significant decrease in turbulence (-22.0%)".[^c6] The paper reads the two signs as two safety architectures. An RLHF-tuned model shows a conflict signature, with high turbulence under attack. A model trained on rigid refusal examples shows a reflex signature, and the authors conjecture that its trajectory "likely collapses into a low-entropy" region once the threat is recognised early.[^c7] That account is the authors' conjecture, not a measured mechanism.

What the concept adds to the wiki is a caution about direction. The same scalar moves up in one model and down in another, so a detector built on turbulence cannot assume that an attack raises the number. A threshold fitted on one architecture would invert on the other. The paper proposes, without testing it, a use on the answerer's side: a running variance over the last layers compared with a model-specific threshold τ, where a crossing means generation stops; the text says that "generation is halted immediately".[^c8] For the asker and answerer this is a signal about whether to keep generating, not about what the answer should say; that reading is mine.

## Limits

- **Size of the evidence.** The adversarial set has "Adversarial Test Group (N = 10)" prompts and the benign set "Benign Control Group (N = 10)".[^c9][^c13] Twenty prompts across two models give a difference in means. The text reports no classification accuracy, no ROC or AUROC, no threshold value and no held-out split, so it establishes a separation in these prompts, not a detector. The statistical test behind p < 0.001 is not named in the text I read.
- **Possible confound with input form.** The adversarial prompts are long role-play and hypothetical framings; the benign prompts are short factual or creative requests. The paper does not compare length-matched benign prompts. The variance may therefore track prompt length or structure rather than adversarial intent. This is my inference from the dataset description; the paper does not test it.
- **Precision.** All runs used "4-bit quantization (NF4)".[^c10] Absolute values, including the 10⁻³ baseline, may differ at full precision. Not tested.
- **Scale.** Two models at 1.5B and 2B parameters. Whether the sign pattern holds at larger sizes is listed as future work: "Future work will explore the scalability of this metric to larger parameters".[^c11]
- **Adaptive attackers.** An attacker who knows the metric could try to keep the variance low. The paper lists "its robustness against adaptive attacks" as open.[^c12] Nothing here tests that.
- **Locus.** Only the final token's state is used, and no other readout location is compared. Whether the signal survives a different position is unknown.
- **The reflex account.** The explanation for the Gemma drop is conjectural, and so is the claim that the metric can serve as a kill-switch. Neither was run.

## Related

- [[trajectory-geometry-uncertainty-probe]] — also reads the path of per-layer updates, but ranks factual errors for abstention with eleven features and a trained probe; turbulence is one untrained scalar aimed at adversarial intent.
- [[single-pass-internal-signal-detector]] — the same one-forward-pass economy, with a supervised detector over several internal signals rather than one dispersion statistic.
- [[recognition-refusal-dissociation]] — separates the direction that tracks answerability from the safety-refusal direction; turbulence asks whether the refusal side differs in dynamics rather than in direction, which those notes do not address.
- [[llm-red-teaming]] — the jailbreak families (persona, hypothetical framing) that the adversarial set is built from.

[^c1]: arxiv-2512-13741 — "the variance of layer-wise cosine velocity"
[^c2]: arxiv-2512-13741 — "the magnitude of the directional change between consecutive"
[^c3]: arxiv-2512-13741 — "were strictly restricted to the reasoning layers of"
[^c4]: arxiv-2512-13741 — "jailbreak attempts trigger a high-variance conflict"
[^c5]: arxiv-2512-13741 — "representing a relative surge of +75.4% (p < 0.001)"
[^c6]: arxiv-2512-13741 — "Gemma exhibited a statistically significant decrease in turbulence (-22.0%)"
[^c7]: arxiv-2512-13741 — "the latent trajectory likely collapses into a low-entropy"
[^c8]: arxiv-2512-13741 — "generation is halted immediately"
[^c9]: arxiv-2512-13741 — "Adversarial Test Group (N = 10)"
[^c10]: arxiv-2512-13741 — "4-bit quantization (NF4)"
[^c11]: arxiv-2512-13741 — "Future work will explore the scalability of this metric to larger parameters"
[^c12]: arxiv-2512-13741 — "its robustness against adaptive attacks"
[^c13]: arxiv-2512-13741 — "Benign Control Group (N = 10)"
