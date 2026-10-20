---
description: "Input content the prompt does not ask about can distort the weights used to combine predictions; restricting weighting to the prompt-relevant part of a sample reduces that distortion."
aliases: ["prompt-irrelevant input semantics", "sample-prompt mismatch", "background distortion of ensemble weights"]
sources: ["arxiv-2512-18411"]
---
# Sample-prompt matching bias

The second bias in the AmPLe paper concerns the input, not the model. A prompt names a class and says something about it; a sample carries much more than that. The authors argue that the weights used to combine prompt-specific predictions should be computed only from the part of the sample the prompt is about. Their example is an image: it "contains superfluous semantics (such as background) that are extraneous to the prompt".[^s1] A weight generator that reads the whole image is therefore pulled by content that no prompt asks about. The abstract states the consequence: "directly utilizing all information from the input samples for generating weights of ensemble learning can lead to suboptimal performance."[^s2] The paper's claim that this is confirmed empirically rests on a figure the text cites, "as confirmed by the empirical exploration results in" Fig. 3.[^s3]

## Mechanism

The method splits each image feature into two parts. A redundancy deprivation network produces a prompt-relevant feature and a prompt-irrelevant feature, and a regulariser pushes the two apart. The regulariser is the conditional mutual information between them given the class label, I(Z_r; Z_ir | Y), estimated from batch counts. The stated aim is "thereby ensuring that the information related to prompts exists exclusively in one of the two features."[^s4] Only the prompt-relevant part then feeds the weight generator, so the ensemble weights are "debiased" in the paper's sense. The paper names the quantity as "represents the Shannon mutual information".[^s5]

What survives from information theory is the operation: a dependence is measured after conditioning, and the part of the input that the question conditions on is separated from the part it does not. What does not survive is the premise that relevance is a fact about the input. Here "relevant" is defined through the class label, so the split is only as good as the label and as good as the learned network that performs it. The paper does not show the split recovers anything a human would call the question's content.

I take the transfer to question answering to be my inference, not the paper's result: a source passage, a retrieved document or a dialogue history contains material that a given question does not condition on, and an answerer that weights evidence by all of it may be misled in the way the image background misleads the weights here.

## Limits

The evidence is one training setup in which the prompt is a class description and the input is an image. The "suboptimal" claim is made in the text and in an exploratory figure; I did not inspect the numbers behind it. The debiasing term is trained together with the rest of the model, and the paper's ablation is reported for both modules at once: the authors write that the results "further confirm the effectiveness of our proposed hybrid model-prompt ensemble learning module and adaptive-debiased weight generation module." The size of the debiasing term on its own is not separated in the text I read. The method also needs class labels, which the authors list as a limitation: "relies on class labels, often overlooking specific image details."[^s6] The gains are not uniform: "AmPLe does not yield uniform gains across all datasets."[^s7] Nothing here tests questions, answers or language inputs.

## Related

- [[model-prompt-matching-bias]] — the other bias in the same paper: the prompt's meaning varies with the model, where this note concerns what part of the input the weights should read.
- [[prompt-content-over-surface-form]] — also a claim about which part of prompt content carries the effect, measured in codebook classification rather than in image weighting.

[^s1]: arxiv-2512-18411 — "the image sample contains superfluous semantics (such as background) that are extraneous to the prompt"
[^s2]: arxiv-2512-18411 — "directly utilizing all information from the input samples for generating weights of ensemble learning can lead to suboptimal performance"
[^s3]: arxiv-2512-18411 — "as confirmed by the empirical exploration results in"
[^s4]: arxiv-2512-18411 — "thereby ensuring that the information related to prompts exists exclusively in one of the two features"
[^s5]: arxiv-2512-18411 — "represents the Shannon mutual information"
[^s6]: arxiv-2512-18411 — "relies on class labels, often overlooking specific image details"
[^s7]: arxiv-2512-18411 — "AmPLe does not yield uniform gains across all datasets."
