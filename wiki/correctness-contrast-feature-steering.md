---
description: "A sparse-autoencoder feature picked by how much more often it fires on correct than on hallucinated yes/no answers can be steered to reduce object hallucination; its opposite amplifies it."
aliases: ["visual understanding feature steering", "separation-score feature selection", "SAVE steering", "contrastive SAE feature steering"]
sources: ["arxiv-2512-07730"]
---
# Correctness-contrast feature steering

A sparse autoencoder (SAE) trained on a model's internal activations is a way to "decompose model activations into sparse and often monosemantic features, where each latent".[^c1] Each latent is a direction the model can be pushed along. The method here chooses one latent by its behaviour on correct versus wrong answers, not by what it means. For each feature j the paper computes how often it is active on answers that turn out correct and how often on answers that turn out hallucinated, and takes the difference. The paper calls this the separation score, and the value "captures the degree to which a feature is preferentially activated for visually grounded predictions."[^c2] The feature with the highest score is taken as the "visual understanding" feature, and the feature with the most negative score as the "hallucinated" one.

The key choice is frequency, not magnitude. The paper states that "SAE features are characterized by how frequently they" fire under a concept, and computes "the activation frequency in each set" for each feature.[^c3] A feature counts once per input when its activation is positive, so the score is a difference of proportions over two groups of answers.

The labels come from a probe. The paper poses binary object-presence questions and sorts the model's answers by whether they match the ground truth. To keep the features from encoding a preference for "yes" or "no", the paper builds a balanced set: "5,000 for objects present (GT) and 5,000 for objects absent (hallucinated)", the absent objects drawn from the LURE benchmark of generated hallucinations.[^c4] The authors state the purpose directly: "To avoid biasing the extracted SAE features toward a particular response."[^c5]

Steering then pushes the model along the selected feature while it generates. The direction matters. Along the visual-understanding feature, the paper reports that "reinforcing these features effectively reduces hallucination, whereas steering along hallucinated features amplifies it."[^c6] On CHAIR, the hallucination-related direction "yields worse CHAIR scores than the visual-understanding" direction in the paper's ablation, and adding further features beyond the top one "introduces" noise, so the method uses a single feature.[^c7]

The effect is reported as a change in the model's own behaviour, not only in its scores. Steering "toward the correct latent decreases attention to query tokens while increasing attention to image tokens."[^c8] The paper reads this as the model leaning more on visual evidence and less on the question text. That reading is the paper's interpretation of an attention measure.

## Limits

- The reported gains are on CHAIR, POPE and MMHal-Bench with three MLLMs. On LLaVA-NeXT the method is not the best: it is "achieving competitive performance, second only to Devils".[^c9] The gain is largest on Qwen2-VL, and the best result is not uniform across models.
- The feature is found on one kind of probe, a yes/no object-presence question with LURE-generated objects, and then used for open captioning. Whether the same feature is selected by a different probe, or whether the separation holds for question types other than object presence, is not tested in this text. That the selection transfers across probe types is my inference, not a result.
- Layer matters and the strength has to be retuned per layer. "Deeper layers require stronger intervention" and "effective layer-wise steering requires a separately trained SAE for" each layer.[^c10] A feature found at one layer does not carry to another, and the method needs a trained SAE at every layer used.
- The paper's ablation fixes one setting (LLaVA-1.6, steering at layer 24, one coefficient). The choice of top-1 and of the reversed direction is tested only in that setting.
- Attention and late-decoding probability shifts are observed correlates of the steering effect. Whether the attention shift causes the reduction in hallucination was not shown; it is an interpretation.
- Correctness here is object-level agreement with ground truth on a constructed probe. The feature is a correlate of correct answers on that probe. Whether suppressing or boosting it changes correctness on other tasks was not tested, and the method does not show that the feature is needed for correctness, which is the question [[sae-uncertainty-correctness-dissociation]] tests with suppression on multiple-choice questions.

## Related

- [[sae-uncertainty-correctness-dissociation]] — the same SAE-and-correctness split, but there features are sorted into uncertainty and incorrectness roles and tested by suppression; here one correctness-contrast feature is used for steering.
- [[mean-difference-steering-vector]] — steering by a difference of means over labelled prompts in the dense activation space; the contrast here is a difference of firing frequencies in a sparse basis.
- [[null-image-logit-subtraction]] — another training-free route against the language-prior side of hallucination, but it edits logits at decoding time rather than activations.
- [[text-prior-over-visual-evidence]] — the failure the paper targets when it names "language priors and visual information loss" as the two sources of object hallucination.[^c11]

[^c1]: arxiv-2512-07730 — "decompose model activations into sparse and often monosemantic features"
[^c2]: arxiv-2512-07730 — "which captures the degree to which a feature is preferentially activated for visually grounded predictions"
[^c3]: arxiv-2512-07730 — "For each feature j, the activation frequency in each set is computed as"
[^c4]: arxiv-2512-07730 — "5,000 for objects present (GT) and 5,000 for objects absent (hallucinated)"
[^c5]: arxiv-2512-07730 — "To avoid biasing the extracted SAE"
[^c6]: arxiv-2512-07730 — "Reinforcing these features effectively reduces hallucination, whereas steering along hallucinated features amplifies it."
[^c7]: arxiv-2512-07730 — "yields worse CHAIR scores than the visual-understanding"
[^c8]: arxiv-2512-07730 — "steering toward the correct latent decreases attention to query tokens while increasing attention to image tokens"
[^c9]: arxiv-2512-07730 — "achieving competitive performance, second only to Devils"
[^c10]: arxiv-2512-07730 — "effective layer-wise steering requires a separately trained SAE for"
[^c11]: arxiv-2512-07730 — "object hallucination caused by language priors and visual information loss"
