---
description: "A template's own similarity to an image shifts a CLIP classifier's answer apart from the class; content-free empty prompts reveal that pull, and a uniformity loss offsets it."
aliases: ["template bias", "template-induced bias", "template-sample similarity", "TSS bias"]
sources: ["arxiv-2512-08606"]
---
# Template-sample similarity bias

A CLIP-style classifier decides by comparing an image with text embeddings. Each text is built from a template such as "a photo of a {}" and a class name. The template alone also has an embedding, and that embedding has a cosine similarity to every image. The paper calls this template-sample similarity (TSS): the resemblance "between a text template and an image sample".[^c1] The claim is that TSS is not neutral. Its effect shows in three places. Images with higher TSS get higher prompt-sample similarity across all class prompts.[^c2] The model "exhibits an attention bias even when the input is a blank template, and this bias persists with a full prompt".[^c3] And in low-data regimes, samples with high TSS are more often classified correctly. On EuroSAT, binning samples by TSS gave a correlation of 0.9 between TSS and the probability of correct classification.[^c4] The authors read this as the model answering from fit to the frame, not fit to the class, "suggesting that models often exploit template similarity instead of truly aligning samples with their correct labels."[^c5]

The mechanism they propose has two parts. The first is a probe made of content-free text. The authors combine standard templates with "inputs that lack meaningful content", so that the prompts carry the template's structure but no category.[^c6] They generate candidate words for emptiness with GPT-4, then "compute the average similarity to all category names and select the top-25 with highest similarity", so that the words sit in the same feature space as the classes while staying vague.[^c7] "The selected 25 words are used to fill these templates", giving prompts about nothing or emptiness.[^c8] Passing these prompts through the model exposes the template's own pull on the images.

The second part is a loss on the probe. For each empty prompt, the classifier that uses the samples' visual features as its class weights should spread probability uniformly over the samples. The loss is a cross-entropy against that uniform target. "Ltb ensures that each empty prompt is classified with equal" probability over the samples, and "This approach guarantees that the similarity between the instances and the template remains uniform."[^c9] Training runs in two stages. First, unsupervised pretraining on this loss alone, whose "main objective" is "to initialize the model" without bias.[^c10] Second, few-shot fine-tuning with cross-entropy plus the same loss, weighted by a hyperparameter alpha.[^c11]

Measured effects, all on CLIP image classification. On the zero-shot model, the correlation between TSS and accuracy on EuroSAT is "strong negative correlation (-0.98) between TSS and classification accuracy". LoRA fine-tuning reduces it to "Training with LoRA reduces this correlation to -0.54", and the method gives "our method nearly eliminates this correlation (-0.05)".[^c12] The figure behind these numbers is "Result for 4-shot finetuning on EuroSAT, seed 1".[^c13] Across eleven datasets the average gain over LoRA is modest: "model improves performance by approximately 1.5 points".[^c14] Two alternatives that move TSS directly, pulling samples toward the empty template or pushing them away, gave no gain: "neither the Pull Closer nor the Push Away strategies lead to performance improvements".[^c15]

What transfers, in my reading. The part that plausibly survives into question-asking is the measurement idea: a framing can carry a pull toward some inputs that has nothing to do with content, and a content-free version of the framing can expose it. A question's wording may sit closer to some candidate answers than others, and that closeness may tilt the answer. The paper does not test language models, question answering or generation, so this is my inference. The loss does not transfer as it stands. Its uniform target assumes that the samples are the candidate answers and should be equally likely under a content-free frame. That assumption has no obvious analogue in open-ended answers.

## Limits

- The evidence is CLIP image classification with cosine similarity, on eleven datasets. The correlation analysis is on EuroSAT, and the central figure is a single EuroSAT 4-shot run at one seed.[^c13]
- The mechanism is not explained. The authors write that "the precise mechanism by which the template influences performance remains unclear".[^c16] Their account of attention drift, that TSS "can inadvertently align with irrelevant visual features during the pre-training alignment phase", is an illustration in the text, not a tested cause.[^c17]
- The empty-prompt set is chosen by GPT-4 and manual curation: "set of empty prompts is manually curated to help identify potential template-induced biases".[^c18] The paper shows that the number of empty prompts "reduces performance fluctuations",[^c19] but not how much the choice of words matters.
- The uniform TSS target is motivated, not derived. The push and pull comparisons support it only inside this setup.
- The gain over LoRA is about 1.5 points on average. Whether that is worth the extra stage and the hyperparameter alpha is not settled by the text.[^c14]
- The authors claim novelty: "this study is the first to identify and investigate the biases caused by the template".[^c20] I have not checked the prior literature.
- Everything here concerns a frozen-encoder adaptation of CLIP. Nothing in the text covers generative models, and the transfer to questions in the paragraph above is mine, not the authors'.

## Related

- [[null-image-logit-subtraction]] — the same content-free probe, a blank image, used to subtract a language prior at decoding time; here an empty text template is used to calibrate the weights in training
- [[template-set-sensitivity-of-bias-scores]] — template wording moves a bias benchmark's score from outside the model; this note is about the template moving the model's own classification from inside
- [[survey-response-model]] — question wording effects on human answers, a parallel in which the wording of the item moves the response
- [[text-modality-dominance]] — reliance on text over other evidence; the template here is a text input pulling the answer toward a frame and away from the image

[^c1]: arxiv-2512-08606 — "template-sample similarity (TSS), defined as the resemblance between a text template and an image sample, introduces bias"
[^c2]: arxiv-2512-08606 — "Concretely, images with higher TSS scores consistently generate higher PSS across all class prompts."
[^c3]: arxiv-2512-08606 — "even when the input is a blank template, and this bias"
[^c4]: arxiv-2512-08606 — "Figure 2(Left) shows a strong correlation (correlation coefficient 0.9) between TSS and the probability of"
[^c5]: arxiv-2512-08606 — "suggesting that models often exploit template similarity instead of truly aligning samples with their correct labels"
[^c6]: arxiv-2512-08606 — "we generate empty prompts by combining standard templates with inputs that lack meaningful content"
[^c7]: arxiv-2512-08606 — "we compute the average similarity to all category names and select the top-25 with highest similarity"
[^c8]: arxiv-2512-08606 — "The selected 25 words are used to fill these templates"
[^c9]: arxiv-2512-08606 — "Ltb ensures that each empty prompt is classified with equal"
[^c10]: arxiv-2512-08606 — "The main objective of this stage is to initialize the model"
[^c11]: arxiv-2512-08606 — "where α is a hyperparameter that controls the weight of the"
[^c12]: arxiv-2512-08606 — "strong negative correlation (-0.98) between TSS and classification accuracy"
[^c13]: arxiv-2512-08606 — "Result for 4-shot finetuning on EuroSAT, seed 1"
[^c14]: arxiv-2512-08606 — "model improves performance by approximately 1.5 points"
[^c15]: arxiv-2512-08606 — "neither the Pull Closer nor the Push Away strategies lead to performance improvements"
[^c16]: arxiv-2512-08606 — "the template influences performance remains unclear"
[^c17]: arxiv-2512-08606 — "it can inadvertently align with irrelevant visual features during the pre-training alignment phase"
[^c18]: arxiv-2512-08606 — "set of empty prompts is manually curated to help identify potential template-induced biases"
[^c19]: arxiv-2512-08606 — "number of empty prompts reduces performance fluctuations"
[^c20]: arxiv-2512-08606 — "To our knowledge, this study is the first to identify and investigate"
