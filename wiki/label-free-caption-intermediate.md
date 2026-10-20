---
description: "A stronger vision-language model writes a label-free, multi-angle description of a crop image for a weaker model to answer from; the work reports +22.7 pp in disease classification."
aliases: ["explanatory caption", "explanational caption", "caption-as-intermediate", "describe-then-answer", "label-free description"]
sources: ["arxiv-2512-24947"]
---
# Label-free caption intermediate

A vision-language model can be given a written description of a picture before it answers a question about that picture. In the CPJ pipeline the description is produced by a separate model, usually a larger one, and the answering model then reads the image, the description and the question together.[^c1] The description is meant to say what is visible: plant morphology, symptom pattern, severity and uncertainty. The paper calls it an "explanatory" or "explanational" caption and treats it as an intermediate step rather than as the answer.[^c2]

The mechanism the authors give is that the description carries diagnostic detail the answering model would otherwise miss: "structured captions as an intermediate step, we provide the" model with richer context.[^c2] The captions also become an inspectable artifact: "These captions act as transparent intermediates".[^c3] Whether the description helps through its content or only through the extra text is not separated in the paper; the argument is about content.

Two design choices set it apart from an ordinary image prompt.

**The describer is not the answerer.** The paper compares captions from two generators on the same answerers. GPT-5-mini captions outperform Qwen2.5-VL-72B captions (+9.08 pp crop, +2.10 pp disease), and the authors read this as "indicating caption generation capability directly influences downstream performance".[^c4] So the quality of the intermediate is a separate variable from the quality of the answerer, and a weak answerer with a strong describer is a configuration the paper tests.

**The description withholds the names.** The caption prompt forbids crop and disease names, "focusing on" morphology and symptoms. The stated purpose is to keep captions neutral: "This prevents premature diagnostic conclusions and ensures captions" stay observations.[^c5] If the description named the disease, the answering step would receive the conclusion as a premise rather than as evidence; withholding the name is what makes the description an observation the answerer must still interpret.

**Measured effect.** With GPT-5-mini captions, GPT-5-Nano reached 63.38% on crop classification, 33.70% on disease classification and 84.5 on QA, which the paper reports as "representing gains of +22.7pp in disease classification and" +19.5 QA points over baselines without captions.[^c6] Most of the gain comes from having a caption at all, not from refining it. In the ablation, run "under the Qwen2.5-VL-72B-Instruct caption setting", unoptimized captions alone gave GPT-5-Nano +19.20 pp on disease classification, while iterative refinement added +1.20 pp.[^c7][^c8] The model-specific pattern is that GPT-5-Nano "benefits more from" caption quality, while Qwen-VL-Chat "exhibits stronger incontext learning from few-shot prompting".[^c9]

## Limits

- One benchmark (CDDMBench), two lightweight answerers (Qwen-VL-Chat, GPT-5-Nano) and models reached by API. Nothing here tests other crops, regions or describers beyond the two generators named.
- The baseline is no caption. The paper does not report a control that gives the answerer label-free text of similar length that is not a description of the image. So "the description helps" is not separated from "more text helps" (my inference from the design).
- The ablation is run only under the Qwen2.5-VL-72B caption setting, not under the GPT-5-mini captions that produce the headline numbers.
- Errors remain after captioning. The dominant category, about 18% of 150 sampled predictions, is early-stage ambiguity: "The dominant error (18%) stems from" minimal visible symptoms, which a caption cannot add.[^c10]
- The description is only as good as the image. "Caption quality issues (8%) correlate with" blur, occlusion and lighting, so the mechanism fails where the picture fails.[^c11]
- The framework "operates on single images", so disease progression over time, or variation across fields, is outside what the description can carry.[^c12]
- The label-leakage benefit that the paper ascribes to refinement is not measured separately from accuracy.

## Related

- score-gated-refinement — the step that revises these descriptions only when a judge scores them below a threshold
- [[llm-judge-biases]] — the judge that selects answers downstream in the same pipeline shows a verbosity effect
- [[specific-actionable-self-feedback]] — the ungated self-critique loop; the gate in CPJ is a judge's decision on whether to run it
- [[groundedness-gated-tool-routing]] — caption-then-text-search is one route among others, and a routed policy beat always using it

[^c1]: arxiv-2512-24947 — "large vision-language model analyzes input crop disease images to generate multi-angle descriptive captions"
[^c2]: arxiv-2512-24947 — "structured captions as an intermediate step, we provide the"
[^c3]: arxiv-2512-24947 — "These captions act as transparent intermediates"
[^c4]: arxiv-2512-24947 — "indicating caption generation capability directly influences downstream performance"
[^c5]: arxiv-2512-24947 — "This prevents premature diagnostic conclusions and ensures captions"
[^c6]: arxiv-2512-24947 — "representing gains of +22.7pp in disease classification and"
[^c7]: arxiv-2512-24947 — "under the Qwen2.5-VL-72B-Instruct caption setting to quantify"
[^c8]: arxiv-2512-24947 — "+2.30 pp / +1.20 pp / +3.0, demonstrating benefits from higher"
[^c9]: arxiv-2512-24947 — "caption quality while Qwen-VL-Chat exhibits stronger incontext learning from few-shot prompting"
[^c10]: arxiv-2512-24947 — "The dominant error (18%) stems from"
[^c11]: arxiv-2512-24947 — "Caption quality issues (8%) correlate with"
[^c12]: arxiv-2512-24947 — "The current framework operates on single"
