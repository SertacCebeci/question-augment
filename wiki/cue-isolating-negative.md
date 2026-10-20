---
description: "A contrast input altered only along the cue under test, so a contrast measures reliance on that cue instead of rejection of an unrelated corruption that a generic negative would bring."
aliases: ["temporal homogenization", "temporally-hard negative", "temporally homogenized video negative"]
sources: ["arxiv-2512-04643"]
---
# Cue-isolating negative

A contrast subtracts the output given a second input from the output given the first. What the subtraction removes depends on how the second input was made. A generic corruption, such as additive noise, changes several properties of the input at once. A model that rejects such a negative can do so on the obvious damage, without using the property the contrast is meant to probe. A cue-isolating negative changes only the cue whose reliance is being measured and keeps the other properties of the input in place.

The clearest case in the work is temporal. In a video model the temporal cue is the order of frames and how information flows between them; the spatial cue is what appears within each frame. The authors reject the usual noise corruption for this reason: adding Gaussian noise to frames corrupts "both spatial and temporal structures simultaneously."[^c2] They call the result a temporally-easy negative, because it "yields a temporally-easy negative, as it provides suboptimal" contrast.[^c3]

Their alternative, temporal homogenization, builds a negative that is "temporally incoherent yet spatially consistent."[^c1] Inside the vision encoder, at each layer, every frame's features are mixed with a global summary of all frames. The homogenized feature "is defined as a linear combination" of the frame's own pre-homogenization feature and the global context, weighted by a degree parameter.[^c16] The final-layer features therefore lose frame-specific temporal variation while each frame keeps its own spatial content. The authors describe this as "neutralizing temporal variation" in each frame.[^c5] They argue that the contrast then "reflects only temporal inconsistencies," which is why the negative is temporally hard.[^c4]

The decoding step is the familiar one. The original video's logits and the negative's logits are combined so that the negative is subtracted, with a strength α. The authors state the aim as a visual contrastive decoding "to eliminate the temporal priors lying in the text decoder."[^c18] Where a token's output depends on temporal order, the negative should shift it; where the output rests on what is visible in a single frame, the shift should be small. The paper does not measure this per token for the temporal negative alone. It adds a per-token weighting on top: the frame-level attention that the preceding token pays to the original video is compared, by Jensen-Shannon divergence, with the same attention under each negative. The reasoning is that "tokens that rely on temporal consistency will exhibit strong attention shifts when the" video is homogenized.[^c6] The divergences set how strongly the temporal and spatial negatives are subtracted for that token.

What the work reports. Combining the temporal and spatial negatives gives the best average, "their combination in SEASON achieves the highest AVG score."[^c7] In the negative-design ablation, the homogenized negative is compared with "three simpler temporally-easy negatives: Average, Shuffled, and Reverse," and "Our Homogenized method achieves the highest" overall average on both backbones tested.[^c9][^c10]

## Limits

- The case against Gaussian noise is argued in the design section. The ablation the text names compares against Average, Shuffled and Reverse, which are all temporal alternatives. A noise negative is not compared head to head in what I read, so the claim that it is "easy" for a reason other than the one given is untested.
- Spatial fidelity of the homogenized features is asserted by construction. The parts of the text I read report no direct measurement of how much per-frame content survives (my reading).
- A single temporal negative can match the full combination on the temporal-only measure. The text says "the baseline of solely applying v T achieves the best temporal-only" results on one benchmark.[^c8] The authors attribute the reversal on a yes/no benchmark to a bias: the benchmark is "susceptible to compliance bias."[^c14]
- The per-token weighting is not separated from the choice of negative in the ablations I read. Whether the attention-divergence weights help beyond fixed weights is not shown there.
- The hyperparameters, contrast strength and homogenization degree, "are tuned via grid search."[^c13] The reported gains are at tuned settings.
- The baselines were re-implemented, since "the official implementations were not available at the time of writing."[^c12]
- Cost: "our method introduces moderate computational overhead compared to the base model."[^c11] By my reading of the decoding equation, each negative adds one more forward pass per step.
- The evidence is for video LLMs and two cues, temporal and spatial. The general idea, a contrast that changes one cue, is not shown for other modalities or for cues other than order and appearance.

## Related

- [[null-image-logit-subtraction]] — the same contrast inside the decoder, but with a blank image, which removes all visual content rather than one cue
- [[counterfactual-hard-negative]] — the targeted-edit idea for negatives, used there to build training pairs rather than a decoding contrast
- [[counterfactual-image-grounding-audit]] — blank and shuffled image probes used to diagnose visual reliance, not to correct the output at decode time
- [[text-modality-dominance]] — reliance on text over other evidence, the failure a cue-matched contrast is meant to expose

[^c1]: arxiv-2512-04643 — "constructs negatives which are temporally incoherent yet spatially consistent"
[^c2]: arxiv-2512-04643 — "both spatial and temporal structures simultaneously"
[^c3]: arxiv-2512-04643 — "yields a temporally-easy negative, as it provides suboptimal"
[^c4]: arxiv-2512-04643 — "which ensures the resulting contrastive signal reflects only temporal inconsistencies"
[^c5]: arxiv-2512-04643 — "neutralizing temporal variation"
[^c6]: arxiv-2512-04643 — "tokens that rely on temporal consistency will exhibit strong attention shifts when the"
[^c7]: arxiv-2512-04643 — "their combination in SEASON achieves the highest AVG score"
[^c8]: arxiv-2512-04643 — "the baseline of solely applying v T achieves the best temporal-only"
[^c9]: arxiv-2512-04643 — "We compare against three simpler temporally-easy negatives: Average, Shuffled, and Reverse"
[^c10]: arxiv-2512-04643 — "Our Homogenized method achieves the highest"
[^c11]: arxiv-2512-04643 — "our method introduces moderate computational overhead compared to the base model"
[^c12]: arxiv-2512-04643 — "As the official implementations were not available at the time of writing"
[^c13]: arxiv-2512-04643 — "are tuned via grid search"
[^c14]: arxiv-2512-04643 — "susceptible to compliance bias"
[^c16]: arxiv-2512-04643 — "is defined as a linear combination"
[^c18]: arxiv-2512-04643 — "impose a visual contrastive decoding to eliminate the temporal priors lying in the text decoder"
