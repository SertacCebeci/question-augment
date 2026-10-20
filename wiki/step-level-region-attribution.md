---
description: "Masking only the annotated image regions and diffing each reasoning step against the unmasked trace attributes steps to visual evidence, beyond whether the final answer flips."
aliases: ["contrastive region masking", "CRM", "region-masked chain-of-thought diff", "step-level causal attribution by masking"]
sources: ["arxiv-2512-08976"]
---
# Step-level region attribution

A multimodal model writes a chain-of-thought (CoT) for a question about an image. The same question is then asked again on a copy of the image in which only some regions are blacked out, and the two traces are compared step by step. What is measured is not only whether the answer changes but which steps change and whether the changed steps still point at the evidence that was removed. Contrastive Region Masking (CRM) is the named instance. It is set against prior work "limited to final answers or attention maps", and it claims "causal, step-level attribution by systematically masking annotated regions and contrasting the resulting reasoning traces with unmasked baselines."[^c1][^c2]

The intervention is a removal of input, not a reading of attention. The regions masked are the ones the dataset marks: "we apply a mask to regions that are explicitly identified as important in the given dataset."[^c3] The masked run reuses the baseline's generation settings, "we use the same temperature values as in the pre-masking CoT generation phase", with a temperature of 0.2 for the CoT stage.[^c4][^c5] Since the question and the generation settings are held fixed and only the region differs, a change in the trace is read as a consequence of that region. That reading is the design's claim; what survives the transfer from causal inference is the contrast between two runs that differ in one input. It is not a measured mechanism inside the model, and the method is black-box by the authors' own description, "a training free diagnostic".[^c6]

The readout has three parts, and each is a per-step judgement turned into a rate. A step is disrupted when its semantic similarity to the baseline step falls below a threshold: "a threshold of 0.80 and use it to measure the step-disrupted metric". The final answer is counted as flipped under a stricter threshold of 0.90, with Sentence-BERT embeddings.[^c7] Disruption is then counted per item, not per step: the whole image counts as disrupted "if any step is modified".[^c8] The third readout is hallucination, which "Surfaces when models continue referring to missing content", so a trace that still describes a masked object is marked even when the answer has not moved.[^c9] Taken together, the three readouts are a step-resolved version of the answer-only probe: the answer can hold while a step about the removed evidence persists or vanishes.

The control is what makes the probe a claim about evidence. Specific masks are compared with random ones, where "irrelevant regions were selected by randomly picking image regions that" lie away from the annotated box.[^c10] The point of the comparison is to separate sensitivity to the annotated evidence from sensitivity to any occlusion. My reading of the reported tables is that the separation is weak: disruption is nearly the same under both masks for several models, "GPT-4o is markedly affected with 95.59% disruption under both random and specific masking",[^c11] and Gemini is "less affected with disruption rates of 79.02% under random masking and 79.08%" under the specific mask.[^c12] So in this data, most step-level change appears to come from occluding the image at all, and the evidence-specific part of the claim is not shown by the disruption figure. That inference is mine; the paper states the opposite conclusion, that CRM "surfaces systematic weaknesses that would be invisible if only the final answer was measured."[^c13]

The probe is the trace-level sibling of [[counterfactual-image-grounding-audit]], which blanks or mismatches the whole image and reads off the answer. Region-level masking with a per-step readout is a different measurement: it asks which step depends on which region, where the audit asks whether the answer depends on the image at all. A trace-level intervention on the text, such as removal or paraphrase of a CoT step, is treated in [[cot-intervention-health-metrics]]; CRM intervenes on the image and leaves the text as the thing read.

## Limits

- A changed trace shows sensitivity to the masked pixels, not that the trace used that region. The random-mask ablation is the paper's own evidence that occlusion alone moves most steps, which is why the specific-versus-random contrast carries the claim.[^c10][^c12]
- The thresholds (0.80 for steps, 0.90 for answers) are the authors' choice on a sentence embedding. The sections read contain no sensitivity analysis over them. A sentence embedding can score a reworded step as changed and a substantively different one as similar; the paper does not test either case.
- Counting per item means one modified step marks the whole image as disrupted. A rate near 80 to 95 percent says that something changed somewhere, not how much of the reasoning changed.
- Refusals and garbled output enter the same rates, and the paper does not say how they are handled. GPT-4o "sometimes explicitly refused to perform the masked CoT reasoning",[^c14] and Qwen "occassionaly inserted random letters within the CoT reasoning when part of the image were masked".[^c15] A refusal scored as a disrupted step measures a policy, not a reasoning change.
- Scale is one dataset: "Our tests are conducted on 1,611 VisArgs benchmarks."[^c16] Four models, one run per item. The reported "error margins (<1.3%)" are described as robust "across samples"; reruns and prompt variants are not reported.[^c17]
- Only annotated regions count as evidence. A model that relies on an unannotated region would show little change, so the probe can understate dependence. The paper does not test this.

## Related

- [[counterfactual-image-grounding-audit]] — whole-image blanking at the answer level; the same kind of input intervention with a coarser readout
- [[cot-intervention-health-metrics]] — interventions on the reasoning text rather than the image
- [[evidence-ablation-four-scenario-deflection-protocol]] — varying the evidence available and reading hallucination when it is missing; the same concern as CRM's hallucination readout, with the context varied instead of the image region
- [[clean-accuracy-masks-adversarial-collapse]] — a clean-accuracy score hides what input changes do to an answer; CRM adds the trace to that readout
- [[evidentiary-basis-of-hallucination]] — here the check for hallucination is the masked image, which is the evidence-basis sense of faithfulness there, not the question of whether a stated chain-of-thought reflects what drove the answer

[^c1]: arxiv-2512-08976 — "CRM provides causal, step-level attribution by systematically masking annotated regions and contrasting the resulting"
[^c2]: arxiv-2512-08976 — "limited to final answers or attention maps"
[^c3]: arxiv-2512-08976 — "we apply a mask to regions that are explicitly identified as important"
[^c4]: arxiv-2512-08976 — "we use the same temperature values as in the pre-masking"
[^c5]: arxiv-2512-08976 — "temperature of 0.2 for the CoT reasoning stage"
[^c6]: arxiv-2512-08976 — "a training free diagnostic"
[^c7]: arxiv-2512-08976 — "a threshold of 0.80 and use it to measure the step-disrupted metric"
[^c8]: arxiv-2512-08976 — "image as disrupted if any step is modified"
[^c9]: arxiv-2512-08976 — "Surfaces when models continue referring to missing content"
[^c10]: arxiv-2512-08976 — "irrelevant regions were selected by randomly picking image regions that"
[^c11]: arxiv-2512-08976 — "GPT-4o is markedly affected with 95.59% disruption under both random and specific masking."
[^c12]: arxiv-2512-08976 — "Gemini-1.5-Flash is less affected with disruption rates of 79.02% under random masking and 79.08%"
[^c13]: arxiv-2512-08976 — "systematic weaknesses that would be invisible if only the final answer was measured"
[^c14]: arxiv-2512-08976 — "GPT-4o sometimes explicitly refused to perform the masked CoT reasoning"
[^c15]: arxiv-2512-08976 — "occassionaly inserted random letters within the CoT reasoning when part of the image were"
[^c16]: arxiv-2512-08976 — "Our tests are conducted on 1,611 VisArgs benchmarks."
[^c17]: arxiv-2512-08976 — "error margins (<1.3%) shows that these differences are robust across samples"
