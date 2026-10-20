---
description: "Reading a vision-language model's vocabulary scores at its image-token positions gives an object confidence that tracks presence and localises better than attention maps, on one model."
aliases: ["VSC", "visual logits confidence", "visual-token vocabulary readout", "visual semantic salience"]
sources: ["arxiv-2511-20032"]
---
# Visual semantic confidence

A multimodal LLM turns an image into visual tokens and concatenates them with the text. The sequence then goes through the same final hidden states and unembedding as the answer, so every position, including the image positions, gets a vocabulary distribution.[^v0] Read at an image-token position, that distribution says which words the patch supports. Zhao et al. call this Visual Semantic Confidence (VSC): "the score of a word within the visual logits quantifies the semantic correlation between that" word and the visual context at that position.[^v1] Nothing is trained. The readout reuses the model's own head, in the same spirit as the [[logit-lens]] applied to intermediate layers, but applied here along the image rather than across depth.

Pooling over the image gives an object-level number. For an object O, the paper takes the maximum over visual tokens of the confidence in O's first word, so one strongly supporting patch is enough to raise the score.[^v9] On an existence-type VQA task (POPE) the paper reports that "objects appearing in the image consistently produce higher semantic confidence scores."[^v2] Thresholding the value gives a presence judgement. The paper reports that these VSC judgements are less accurate than the model's own responses, but still clearly above chance.[^v3]

For grounding, the paper compares the token-level VSC map with visual attention using a Dice coefficient against object masks. Its result is that "VSC demonstrates superior grounding capability compared to visual attention."[^v4] The explanation offered is that attention has a sink, which limits its grounding ability; the cost is most visible for large objects, where attention tends to focus only on local regions.[^v5] The attention-sink concept is the one in [[attention-sink]]; VSC is a different readout that avoids attention weights altogether.

The concept matters for the answerer because the paper names a failure mode it calls "Underutilization of extracted visual features": the model can extract an object with high VSC and still answer wrongly.[^v6] The paper says the understanding read through VSC "does not always fully align with the model’s responses."[^v7] So the same model holds two visual judgements, one from its vocabulary readout and one from its committed answer, and they can disagree. A comparison between them is a second channel for checking an answer. It is not a verdict on which channel is right.

The question also enters the readout. The method extracts "the objects mentioned in the question" with NLP tools and takes the grounding over those objects.[^v8] An object that the question never names gets no grounding from this route. The paper says this route "is not applicable to image captioning, which is inherently object-agnostic," and a different, uncertainty-weighted grounding is used there.[^v10] For someone formulating a visual question, the nouns chosen are therefore part of what the model is told to look for.

## Limits

- The figures read here use LLaVA-1.5-7B. The parts of the paper read here do not show the readout on other architectures, so transfer is untested in this note.
- The presence cut is fitted by grid search to maximise F1 on one COCO subset, "a value obtained via grid search optimizing the F1 score on" that subset.[^v11] A threshold tuned on one split says little about a different distribution of objects.
- The grounding comparison uses "500 images from MSCOCO" against object masks.[^v12] It is a single benchmark for localisation quality, and the object-level claim rests on the same data.
- VSC approximates an object's confidence by its first tokenised word: "we approximate this confidence using the first token o0 of the tokenized object O."[^v9] Multi-token names, synonyms and plurals are handled only through that approximation (my inference from the formula).
- Max pooling means the object score can be driven by one patch. Whether that is a grounding signal or noise on a single token is not separated in the text read here (my inference).
- The paper shows the two readings diverge but does not show the answer improves when the readout is used to correct it. The corrective method built on VSC is a separate step and is not established by the readout itself.

## Related

- [[logit-lens]] — the same head projection read across layers; VSC reads it across image positions at the final layer
- [[attention-sink]] — the attention failure that VSC is compared against on grounding
- [[visual-token-sparsification-hallucination]] — also decides which visual tokens matter, by attention and pruning rather than by vocabulary score
- [[procedural-hallucination-readout-routing]] — the "present but not used" gap in other tasks; the visual underutilization here is a case of the same gap on the image side

[^v0]: arxiv-2511-20032
[^v1]: arxiv-2511-20032 — "the score of a word within the visual logits quantifies the semantic correlation between that"
[^v2]: arxiv-2511-20032 — "objects appearing in the image consistently produce higher semantic confidence scores"
[^v3]: arxiv-2511-20032
[^v4]: arxiv-2511-20032 — "VSC demonstrates superior grounding capability compared to visual attention"
[^v5]: arxiv-2511-20032 — "Visual attention suffers from the “sink” phenomenon [10], which limits its grounding ability"
[^v6]: arxiv-2511-20032 — "Underutilization of extracted visual features"
[^v7]: arxiv-2511-20032 — "does not always fully align with the model’s responses"
[^v8]: arxiv-2511-20032 — "We first use NLP tools to extract the objects mentioned in the question"
[^v9]: arxiv-2511-20032 — "we approximate this confidence using the first token o0 of the tokenized object O"
[^v10]: arxiv-2511-20032 — "is not applicable to image captioning, which is inherently object-agnostic"
[^v11]: arxiv-2511-20032 — "a value obtained via grid search optimizing the F1 score on"
[^v12]: arxiv-2511-20032 — "We randomly select 500 images from MSCOCO to evaluate the"
