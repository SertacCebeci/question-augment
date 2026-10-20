---
description: "Per attention head, the entropy over text tokens divided by the entropy over visual tokens gives a hallucination signal that the paper reports as the most effective of the detectors it tried."
aliases: ["TVER", "text-to-visual entropy ratio", "modality-split attention entropy", "textual-to-visual attention entropy"]
sources: ["arxiv-2512-02981"]
---
# Text-to-visual attention entropy ratio

A multimodal model reads its image and its question through the same attention heads. For each head at a layer, the attention distribution over the whole sequence is partitioned into a subset on the textual token indices and a subset on the visual token indices, and the entropy of each subset is taken.[^t1] The score is the ratio of the two: textual entropy over visual entropy. The paper calls it the "Text-to-Visual Entropy Ratio (TVER)".[^t2] The point of splitting the entropy by modality is that a single entropy over the whole attention row mixes the two sources of uncertainty, while the ratio asks which side of the input the head is spread over.

The reading the paper gives the ratio is directional. A higher score "indicates a greater likelihood of hallucination, corresponding to increased entropy in T and decreased entropy in V."[^t3] Low visual entropy is read as confidence in the visual evidence, so high textual entropy alongside it is taken to be a sign that the answer is drifting away from the image. The paper's gloss is that elevated textual uncertainty "may stem from misleading" visual cues the model is confident about, and that is why the ratio is set up as a contrast rather than as a textual entropy on its own.[^t4]

The ratio is used as a switch on heads, not as a score on outputs. Heads whose ratio is above a threshold are masked, which is how the paper turns the signal into a change in what the model attends to.[^t5] The reason to prefer it, as the paper states it, is comparative: among several internal hallucination detectors drawn from prior work,[^t6] the authors "empirically find that TVER is the most effective, achieving" the best ranking on the calibration and detection measures they report.[^t7] The method needs no labels, which the paper uses as its selling point: the decision agent "leverages unsupervised uncertainty estimation" to decide when to reason introspectively.[^t8]

For the asking-and-answering concern, the transferable part is a reading an answerer can make of its own internal state before committing to a reply, without asking anyone. It does not say what question to put, and it does not say which answer is right. It says where in the input the answerer's attention is spread, and whether that spread is lopsided toward the words or toward the evidence. The entropy it is built from is the same quantity that the [[entropy]] note treats, applied to a split of one attention row.

## Limits

- The comparison that makes TVER "the most effective" is reported as a figure with AUROC and expected calibration error. The figure's caption describes the layout ("uncertainty score distributions (top) and corresponding hallucination rates (bottom) across bins"), but the text I read does not give the numbers, the models, or the benchmark for it. The ranking is the paper's own; its size is unknown here.
- The paper calls the ratio a signal with "a strong correlation with hallucination." That is a correlational claim. Nothing in the text I read shows that masking the high-ratio heads reduces hallucination by itself. The ablations in the text are over the paper's In and Ex components, not over the masking step on its own.
- The ratio is relative. Each entropy is taken over a subset whose size depends on how many text and visual tokens the prompt contains. My inference, not something the paper tests in the part I read: a long text span set against a short image could move the ratio without any change in confidence. Whether the subset sizes matter is open here.
- The formula is written for one attention head at a time, and the paper's own use selects heads by threshold. Whether a threshold chosen on one model and dataset carries to others is not established in the text I read.
- This is a reading of a model's internal attention. It is not evidence about how people ask or answer questions, and it should not be read as one.

## Related

- [[multi-signal-uncertainty-gate]] — one of its four signals is an entropy over cross-modal attention on the image; TVER keeps that attention side but takes a per-head ratio of text entropy to visual entropy instead of one dispersion over visual tokens.
- [[attention-entropy-ambiguity-signature]] — the same attention entropy read as prompt ambiguity in a text-only answerer; TVER splits it by modality, so it reads imbalance between question and evidence rather than diffuseness of the question alone (my reading).
- [[entropy]] — the quantity the ratio is built from.

[^t1]: arxiv-2512-02981 — "The aℓ are partitioned based on textual indices T and visual indices V"
[^t2]: arxiv-2512-02981 — "Text-to-Visual Entropy Ratio (TVER)"
[^t3]: arxiv-2512-02981 — "a greater likelihood of hallucination, corresponding to increased entropy in T and decreased entropy in V."
[^t4]: arxiv-2512-02981 — "uncertainty in the textual modality may stem from misleading"
[^t5]: arxiv-2512-02981 — "are masked as follows"
[^t6]: arxiv-2512-02981 — "A number of methods (Farquhar et al. 2024; Xiong et al. 2024; Zhang et al."
[^t7]: arxiv-2512-02981 — "empirically find that TVER is the most effective, achieving"
[^t8]: arxiv-2512-02981 — "In InEx, a decision agent leverages unsupervised uncertainty estimation"
