---
description: "A rationale template that has a vision-language model describe the image in text before it reasons and answers, so the reasoning is conditioned on its own written account of the visual input."
aliases: ["see-before-thinking template", "see-think-learn structured rationale", "caption-then-reason prompt", "perception-first rationale"]
sources: ["arxiv-2512-02456"]
---
# Perception-first rationale template

A chain-of-thought prompt asks a model to reason before it answers. On a visual question that reasoning can drift from what the image shows, because the model is never asked to state what it sees before it starts to infer. The see-before-thinking template changes the order of the rationale. The model writes three labelled sections in turn: a caption, a reasoning section grounded in the caption, and a conclusion that names the choice. The prompt asks for "three specific sections: CAPTION, REASONING and CONCLUSION", and the caption is to "first describe visual elements from the" image, with emphasis on what bears on the question.[^c1] The authors motivate the order by analogy: the structure "mirrors the natural human cognitive process and guides the model in better organizing its internal reasoning".[^c2]

The mechanism rests on a diagnosis of the self-training baseline. Its rationales "mix perception with reasoning, preventing the reasoning" from being properly conditioned on the visual input.[^c3] The template separates the two. The caption is a written perception step that the model produces itself, and the reasoning is asked to work from it. The training target is the whole tuple, since the model is prompted to produce "comprising an image description", a rationale and a predicted answer.[^c4] So the model is trained to describe as well as to answer.

Whether the reasoning actually uses the caption is not measured directly. The paper's evidence is qualitative: in the commonsense example, STL "attends to contextual cues such as the plants in the background and the dirt area".[^c5] The ablation measures accuracy after fine-tuning. Removing the structured prompt and the negative rationales together lowers accuracy, and the authors read the structured prompt's part as follows: "Introducing the structured rationale prompt significantly improves accuracy by guiding the model to" analyse the image first, "thereby enabling iterative refinement of its perception during training".[^c6]

The gain is therefore a property of the template inside a training loop. The text I read does not report a prompt-only comparison that isolates the template without fine-tuning.

## Limits

- The ablation is on two splits, Language Science and Commonsense. On the Natural Science split the baseline beat the method, and the authors say so: "Interestingly, STaR outperforms STL on the Natural Science dataset".[^c7] The template is not shown to help everywhere.
- The caption is not checked against the image. The paper's own comparison shows a description that mentions objects "that are not present in the image".[^c8] A fluent caption is not evidence of accurate perception.
- Only multiple-choice visual questions were tested. Open-ended answers, where a conclusion cannot be matched to a fixed option, were not.
- The paper claims better perception, but reports no perception metric in the text I read. Its quality evidence is a human preference study of 150 rationales per domain, where "STL reasoning were preferred 35% more" often than the baseline's.[^c9] That is a preference for the rationale as a whole, not a measure of the caption.

## Related

- [[label-free-caption-intermediate]] — a stronger model writes a description for a weaker model to answer from; here the model writes its own description as the first section of its rationale
- [[visual-forgetting-during-reasoning]] — attention to the image falls as the chain grows; a description written early is one way to keep visual content in play (my inference; the paper does not test this link)
- [[negative-rationale-augmentation]] — the second component the same paper adds to this template
- correctness-filtered-self-training — the loop that generates these rationales and keeps the ones that answer correctly

[^c1]: arxiv-2512-02456 — "with three specific sections: CAPTION, REASONING"
[^c2]: arxiv-2512-02456 — "guides the model in better organizing"
[^c3]: arxiv-2512-02456 — "mix perception with reasoning, preventing the reasoning"
[^c4]: arxiv-2512-02456 — "comprising an image description"
[^c5]: arxiv-2512-02456 — "STL attends to contextual cues such"
[^c6]: arxiv-2512-02456 — "thereby enabling iterative refinement of its perception during training"
[^c7]: arxiv-2512-02456 — "Interestingly, STaR outperforms STL on the Natural Science dataset"
[^c8]: arxiv-2512-02456 — "that are not present in the image"
[^c9]: arxiv-2512-02456 — "On average, STL reasoning were preferred 35% more"
