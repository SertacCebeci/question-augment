---
description: "A correct answer in words can still be unrealizable by the channel that must carry it; scoring the answerer against its renderer's output, not only the reference, narrows that gap."
aliases: ["semantic-to-visual gap", "executable caption", "channel-feasible answer", "renderer-aware answer reward"]
sources: ["arxiv-2511-16669"]
---
# Answer-channel realizability

An answer is a commitment made for a channel that has to carry it out. A text answer can be right in its words and still fail when the channel must render it. The VANS paper (Cheng, Hou, Tao and Liao) builds this into video next-event prediction, where the answer is a generated video rather than a sentence.

The usual way to get a video answer is a cascade. "A straightforward solution is to employ a VLM for prediction followed by a VDM for generation."[^c1] The vision-language model writes a caption, and a video diffusion model renders it. The authors call the failure of this cascade a semantic-to-visual misalignment: the caption can be linguistically correct and still not renderable.

Their remedy is to score the caption by what the renderer does with it. The caption reward has a text term and a visual term. The text term "measures semantic similarity between generated and ground-truth captions using ROUGE-L".[^c2] The visual term evaluates the video rendered from the caption against a reference video with CLIP similarity. The stated purpose is that "Relying solely on rt1 can lead to captions that are linguistically correct but visually unrealistic or unexecutable by the VDM."[^c3] The joint reward "guides the VLM to generate captions that are not merely semantically accurate, but also visually plausible and actionable for the VDM."[^c4]

The mechanism is therefore that the answerer is trained against the channel's own output, so its commitments are ones the channel can carry. The ablation is the only measured part of this claim in the text read. Joint training beats "variants where GRPO is applied solely to the VLM or VDM, or where their individually optimized versions are simply cascaded."[^c5] Removing the visual term "harms visual consistency."[^c6]

## What the channel argument does not establish

The case for video as the answer channel is motivation in the paper. Video "encapsulates rich, dynamic information about the physical world that text alone struggles to convey."[^c7] The paper says that "The shift from telling to showing enables VNEP to offer more intuitive and customized answers."[^c8] The only support in the text read is one qualitative figure, where "Video answer provides an intuitive and customized response by demonstrating the action directly."[^c9] A human evaluation was run, but on generated video answers from several video models, not against a text answer.[^c10]

## Limits

- Realizability is operationalized as similarity to a reference. ROUGE-L scores the caption and CLIP similarity scores the video. Neither checks that a person or a real agent could carry out the caption. "Actionable" in this paper means close to a reference under CLIP.
- The comparison of video against text is not measured. Gemini's text answer appears in one figure. The advantage of showing over telling is asserted, not tested.
- The domain is procedural and everyday video, with the generator's capacity as the ceiling. Other answer channels (diagrams, code, speech, a tool call) are not tested.
- The gains over cascaded pipelines come from the authors' ablation table. This note relies on the text's description of it, not on the table's numbers.
- The renderer is frozen during the caption stage. Whether the answerer adapts when the renderer changes is not studied.
- My inference, not the paper's: the same check should apply to a text answerer whose answer must be executed by a tool or a person. The paper does not test a text channel, so that transfer is untested here.

## Related

- [[semantic-predictive-misalignment]] — a question that matches its target in meaning need not predict it best; the same gap between meaning-match and fit, on the question side
- [[presentation-modality-shapes-question-intention]] — the presentation medium changes what learners ask; here the medium limits what can be answered
- [[text-modality-dominance]] — modality as an input channel; this note concerns the output channel
- [[format-induced-answer-collapse]] — answer format altering answer quality, a text-side analogue of format limiting the answer

[^c1]: arxiv-2511-16669 — "A straightforward solution is to employ a VLM for prediction followed by a VDM for generation."
[^c2]: arxiv-2511-16669 — "measures semantic similarity between generated and ground-truth captions using ROUGE-L"
[^c3]: arxiv-2511-16669 — "Relying solely on rt1 can lead to captions that are linguistically correct but visually unrealistic or unexecutable by the VDM."
[^c4]: arxiv-2511-16669 — "The joint reward guides the VLM to generate captions that are not merely semantically accurate, but also visually plausible and actionable for the VDM."
[^c5]: arxiv-2511-16669 — "Joint-GRPO outperforms variants where GRPO is applied solely to the VLM or VDM"
[^c6]: arxiv-2511-16669 — "removing the video fidelity reward rv1 harms visual consistency"
[^c7]: arxiv-2511-16669 — "video encapsulates rich, dynamic information about the physical world that text alone struggles to convey"
[^c8]: arxiv-2511-16669 — "The shift from telling to showing enables VNEP to offer more intuitive and customized answers"
[^c9]: arxiv-2511-16669 — "Video answer provides an intuitive and customized response by demonstrating the action directly"
[^c10]: arxiv-2511-16669 — "we conduct a human evaluation to assess the subjective quality of generated video answers"
