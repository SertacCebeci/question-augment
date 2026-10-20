---
description: "A correct answer can survive sequential adaptation while the evidence it rests on shifts; answer-level checks miss this, so the reliance pattern has to be measured separately."
aliases: ["hidden evidence-use forgetting", "answer-preserving evidence drift", "hidden forgetting", "dominant evidence flip"]
sources: ["doi-10-48550-arxiv-2607-02020"]
---
# Hidden evidence-use drift

A model can keep giving the same correct answer while the evidence it draws on changes. Chen, Xiao and Tang call this hidden evidence-use forgetting, the case "where answer accuracy is retained while the model silently" shifts toward different or less grounded evidence channels.[^c1] The inputs in question are the channels that can support an answer: image regions, question words, OCR tokens, chart elements, document spans and language cues in the question. The paper's own list begins with "this set may include visual regions, OCR tokens".[^c2]

The measurement works on the likelihood of the correct answer. For each channel, the input is altered so that the channel is suppressed, "while keeping other channels unchanged".[^c3] The rise in negative log-likelihood of the ground-truth answer under that alteration, with negative values clipped to zero, is the channel's sensitivity; normalized across channels, the sensitivities form an evidence-use profile for the checkpoint.[^c4] Two checkpoints can then be compared on the same example. The dominant-evidence flip rate is computed only where both checkpoints answer correctly, and it "isolates cases where the answer is preserved but the dominant evidence channel changes."[^c5] A hidden forgetting event is defined as one where "answer degradation is small" while reliance drift is large.[^c6]

What this adds is a difference in the object being checked. Correctness is a property of the output; evidence use is a property of the route to it. A checker that reads only the output cannot see a change of route. The paper's own baseline shows this: a method that keeps the earlier output distribution "imposes no constraint on which evidence channel supports the prediction."[^c7] The same logic applies to any answer-level check, human or machine. A right answer is evidence that the answer is right, not that it came by the same route as before. The authors state the test they are running as "the central claim that answer-level evaluation can miss reliance drift."[^c8]

The pattern has neighbours in the wiki. [[correct-answer-trap]] shows the split at one moment: a flawed method that happens to give the right answer passes a correctness check. Here the split runs across time, between a model and its own earlier checkpoint. [[perception-step-faithfulness]] scores the route step by step and finds that a correct answer can rest on ungrounded visual claims. [[evidence-forgetting-rate]] is the reverse case: the evidence is present and the answer is still wrong.

My inference, not the paper's claim: the same two-sided check would apply to a tutor or a grader who sees only final answers. The paper tests nothing of the kind.

## Limits

The profile is, in the authors' words, "only a post-hoc diagnostic proxy for evidence use."[^c9] It records how much the answer's likelihood falls when a channel is removed. A channel can move the likelihood without being what a reader would call the evidence the answer used, and an ablated input may fall off the distribution the model was trained on. The paper does not check the profile against human judgments of grounding.

The ablations are used "only after training for diagnosis."[^c10] That keeps the diagnosis from being optimized against, but it does not show that a profile which is held steady during training still tracks the evidence the model would use at deployment.

The thresholds in the preliminary figure are "used only to visualize the qualitative phenomenon",[^c11] so the hidden-drift region is a picture, not a rate with an error bar. The hidden forgetting rate needs two cut-offs, one on answer degradation and one on reliance drift; their values are a choice of the evaluator, and the claim that drift is hidden depends on them.

The framework "assumes that each input can be decomposed into meaningful evidence channels."[^c12] Where the input has no such decomposition, the drift has no measure in this form. The experiments cover instruction-tuning streams and three MLLM backbones; video, audio and specialized domains are listed as untested.[^c13]

The paper does not show that a shift toward different evidence is harmful case by case. It reports that reliance drift and answer loss fall together on its benchmarks. A route that changed but stayed equally reliable is not separated from a degraded one by the profile alone, so "less grounded" is a claim the proxy supports only on average.

## Related

- [[correct-answer-trap]] — a correct answer hides a flawed route at one time; here the route changes across training stages.
- [[perception-step-faithfulness]] — the same worry, that a correct answer can rest on ungrounded visual claims, scored on reasoning steps rather than channel ablation.
- [[evidence-forgetting-rate]] — the reverse case: the evidence is present and the answer is still wrong.
- [[text-modality-dominance]] — a measured text-heavy reliance under corruption; a channel profile of the kind this note describes, read at a single checkpoint.

[^c1]: doi-10-48550-arxiv-2607-02020 — "where answer accuracy is retained while the model silently"
[^c2]: doi-10-48550-arxiv-2607-02020 — "this set may include visual regions, OCR tokens"
[^c3]: doi-10-48550-arxiv-2607-02020 — "suppresses channel m while keeping other channels unchanged"
[^c4]: doi-10-48550-arxiv-2607-02020 — "is the negative log-likelihood of the ground-truth answer"
[^c5]: doi-10-48550-arxiv-2607-02020 — "isolates cases where the answer is preserved but the dominant evidence channel changes."
[^c6]: doi-10-48550-arxiv-2607-02020 — "We define hidden forgetting as the event where answer degradation is small"
[^c7]: doi-10-48550-arxiv-2607-02020 — "imposes no constraint on which evidence channel supports the prediction"
[^c8]: doi-10-48550-arxiv-2607-02020 — "designed to test the central claim that answer-level evaluation can miss reliance drift"
[^c9]: doi-10-48550-arxiv-2607-02020 — "is only a post-hoc diagnostic proxy for evidence use."
[^c10]: doi-10-48550-arxiv-2607-02020 — "These ablations are used only after training for diagnosis."
[^c11]: doi-10-48550-arxiv-2607-02020 — "used only to visualize the qualitative phenomenon"
[^c12]: doi-10-48550-arxiv-2607-02020 — "assumes that each input can be decomposed into meaningful evidence channels"
[^c13]: doi-10-48550-arxiv-2607-02020 — "additional modalities such as video and audio"
