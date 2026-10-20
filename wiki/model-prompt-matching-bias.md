---
description: "The same textual prompt can carry different meanings for different vision-language models, so per-prompt predictions disagree across models and an ensemble can exploit that disagreement."
aliases: ["prompt-model matching bias", "model-dependent prompt semantics", "same prompt different model"]
sources: ["arxiv-2512-18411"]
---
# Model-prompt matching bias

A prompt is a probe, and two models do not read the same probe the same way. The AmPLe paper's claim is that "the same prompt can convey different semantics across distinct vision-language models."[^m1] Its evidence is a zero-shot comparison on UCF101 with two CLIP image–text models and six prompts per class. With the ViT-B/16 model one prompt "performs the best among six individual prompts"; with the ViT-B/32 model a different prompt gives the "highest performance".[^m1b] The authors read the disagreement as information: "different VLMs extract different semantic information from the input image under the guidance of identical prompts."[^m2]

## Mechanism

The bias is a mismatch between a prompt and the model that interprets it. A single model with a single prompt inherits that model's reading of the prompt, and the reading that works best for one backbone need not work best for another. The paper's response is not to choose the better backbone but to aggregate. Each of the prompts is applied to both backbones, giving 2M prediction logits, and these are combined with learned weights.[^m3] The reported comparison is between aggregating within one model (MP) and aggregating across both (MMP): "The best result of MMP highlights the potential of combining multiple prompts and different VLMs to improve model performance."[^m4]

The bias is a claim about which parts of a prompt's effect are model-specific. Its direct measurement is per-prompt accuracy under each model, not a semantic probe of what each model takes the prompt to mean. So what is shown is that the ranking of prompts flips between two backbones on one dataset, and that pooling across the two beats either alone in the authors' figure.

I take the transfer to asking to be my inference, not the paper's result: a question worded once is answered by an answerer whose reading of the wording is its own, so the question's effective meaning is partly a property of the question–answerer pair. If so, a single phrasing evaluated on a single answerer tells one about that pair. This is the same pattern that [[reformulation-method-ranking-instability]] reports for query reformulation methods, where the ranking of methods shifts with the generating model; the new element here is the per-prompt level inside a fixed task.

## Limits

The evidence is one dataset for the motivating figure, zero-shot, and two backbones of one family. The paper's own framing is that its method is an ensemble, so it does not show that the bias is separable from the benefit of simply having more diverse predictions. The authors also say that AmPLe "does not yield uniform gains across all datasets" and that when "a single strong prompt already suffices" the ensemble weighting "introduces minor trade-offs without clear benefit."[^m5] In the discussion of prompt variation the paper says "prompt variations can indeed affect" performance and calls this a limitation.[^m6] The multiple prompts are built from class labels, and "multiple prompts can introduce redundancy or repetitive information."[^m7] None of these measurements involve questions or language answerers, and none tests whether the mismatch survives when the same model is re-prompted.

## Related

- [[sample-prompt-matching-bias]] — the second bias in the same paper: which part of the input the ensemble weights should read.
- [[reformulation-method-ranking-instability]] — the ranking of reformulation methods also shifts with the backbone.
- [[model-dependent-benchmark-difficulty]] — a benchmark's item difficulty differs by model, the evaluation-side version of the same mismatch.
- [[prompt-content-over-surface-form]] — a separate account of prompt sensitivity, located in informational content rather than in which model reads it.

[^m1]: arxiv-2512-18411 — "the same prompt can convey different semantics across distinct vision-language models"
[^m1b]: arxiv-2512-18411 — "performs the best among six individual prompts"
[^m2]: arxiv-2512-18411 — "different VLMs extract different semantic information from the input image under the guidance of identical prompts"
[^m3]: arxiv-2512-18411 — "we apply the multiple prompts that incorporate different class-relevant visual descriptions of the given class to different VLMs"
[^m4]: arxiv-2512-18411 — "The best result of MMP highlights the potential of combining multiple prompts and different VLMs to improve model performance."
[^m5]: arxiv-2512-18411 — "a single strong prompt already suffices"
[^m6]: arxiv-2512-18411 — "prompt variations can indeed affect"
[^m7]: arxiv-2512-18411 — "multiple prompts can introduce redundancy or repetitive information"
