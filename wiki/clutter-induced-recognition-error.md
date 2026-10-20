---
description: "A vision-language model misreads an element's polarity in a crowded diagram yet reads it correctly alone; cropping the element out and re-reading it corrects the global reading."
aliases: ["excess-content recognition error", "inset re-reading", "crop-then-reread correction", "source-polarity crop correction"]
sources: ["arxiv-2512-10159"]
---
# Clutter-induced recognition error

A vision-language model can read one element of a figure correctly and still misread it when the whole figure is in view. The circuit study isolates a specific case: the model's judgement of which terminal of a voltage or current source is positive goes wrong on the full textbook diagram, while the same source shown alone is read reliably. The authors give the cause as a property of the model: VLMs "are more prone to hallucinations when presented with images containing excessive information", and the extra content "can cause the model to lose focus".[^c1][^c2]

The mechanism the work uses is removal of competing content, not a change of view. Each independent source is located with a fine-tuned detector, and the bounding box is used to crop it out of the diagram. "Since the cropped images contain only the sources" the model "is able to reliably recognize" their polarities.[^c3][^c4] The local answer is then written back over the global one: "This locally recognized polarity information is then used" to correct the polarity in the model's first, whole-diagram reading.[^c5] Dependent sources, whose bounding boxes the detector was not trained on, are located with rule-based image processing instead ("to extract this information for dependent sources").[^c11]

The size of the problem in this study is stated by the authors. Incorrect source-polarity recognition "accounts for 35.29% of the incorrectly solved problems" in their baseline run, which is why it was the first target.[^c6] The pattern they describe is that polarity recognition "is consistently accurate when the image contains only a single source", so the failure is tied to the crowded view and not to the concept of polarity.[^c7]

Why the distinction matters: a whole-figure reading is the model's default, and a reading that is wrong on that default can look fluent and be checked by nothing in the figure itself. Cropping changes what the model is asked to look at, so it can fix an error that more reasoning over the same image would not. This is a different lever from enlarging the image: a crop removes distractors from the same content, while a zoom raises the resolution of content that stays in view. The paper does not compare the two, so the difference is my inference from the mechanism it describes.

Measured result, with the caveat below. On 83 textbook problems the full pipeline, which includes the crop step, the ngspice cross-check and a human correction pass, reached 97.59% against Gemini 2.5 Pro's 79.52% baseline.[^c8][^c9] The four hand-drawn variants rose from 60.61%–71.21% to 89.39%–92.42%.

## Limits

- The crop step is not measured alone in the parts of the paper I read. The headline gains come from the combined pipeline, and the crop, the ngspice loop and the human pass were not reported as separate contributions in the sections read. The mechanism is the paper's account; its isolated effect is not established here.
- One model (Gemini 2.5 Pro) and one set of 83 problems from a single textbook, with a further 43 from another. "On 83 problems, the proposed pipeline achieves 97.59% accuracy" is the scale of the evidence.[^c8]
- The cause (loss of focus under excess content) is offered as an explanation of observed errors. The work does not vary the amount of content in a controlled way to test it.
- The crop depends on a detector being right. Where the detector misses or mislocates a source, the crop carries the error forward. The paper's residual error analysis places circuit recognition as the largest remaining failure: "circuit recognition remains the dominant source of remaining failures".[^c10]
- Transfer to other figures is my inference. The sources here are small, well-separated objects with polarity markings; whether clutter drives misreadings of other visual relations is not tested.

## Related

- [[coarse-to-fine-evidence-zoom]] — the other way of looking closer: a two-pass zoom into a span to raise its resolution, where this note removes competing content from the view
- [[confidence-triggered-visual-reattention]] — a crop-and-zoom re-query gated on the model's own confidence; here the crop is made for every detected source, without a confidence trigger
- [[perception-step-faithfulness]] — scoring each perception step against the image; a polarity misreading is one such step that a final answer can hide
- [[perception-cognition-gap]] — the figure is read for values but its encoded rules are misinterpreted; the circuit case is a misreading of a single mark, which the crop repairs
- [[independent-implementation-check]] — the verifier stage of the same pipeline: an ngspice run disagrees with the model when the reading is wrong, and agrees, without detecting it, when the same reading is shared

[^c1]: arxiv-2512-10159 — "are more prone to hallucinations when presented with images containing excessive information"
[^c2]: arxiv-2512-10159 — "can cause the model to lose focus"
[^c3]: arxiv-2512-10159 — "Since the cropped images contain only the sources"
[^c4]: arxiv-2512-10159 — "Gemini 2.5 Pro is able to reliably recognize"
[^c5]: arxiv-2512-10159 — "This locally recognized polarity information is then used"
[^c6]: arxiv-2512-10159 — "Since incorrect recognition of source polarities accounts for 35.29% of the"
[^c7]: arxiv-2512-10159 — "polarity recognition is consistently accurate when the image contains only a"
[^c8]: arxiv-2512-10159 — "On 83 problems, the proposed pipeline achieves 97.59% accuracy"
[^c9]: arxiv-2512-10159 — "corrections, the cumulative correctness reaches 97.59%."
[^c10]: arxiv-2512-10159 — "circuit recognition remains the dominant source of remaining failures"
[^c11]: arxiv-2512-10159 — "to extract this information for dependent sources."
