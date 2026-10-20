---
description: "When visual grounding is weak, chain-of-thought rationales follow the question's language prior: plausibility stays high while diagnostic accuracy gains vanish or reverse."
aliases: ["CoT hallucination trap", "fluent but ungrounded rationale", "chain-of-thought plausibility-accuracy divergence"]
sources: ["arxiv-2601-02737", "arxiv-2512-14989", "arxiv-2511-20701"]
---
# Chain-of-thought hallucination trap

Chain-of-thought adds a latent rationale between the input and the answer. Written formally, the answer depends on the rationale and the image, and the rationale is meant to bridge visual evidence and diagnosis. The trap is the case where that bridge is never built: the rationale is generated from the question's language prior and barely from the image, "the conditional probability P(r | x, q) is often dominated by the language prior."[^c1] The authors name the result "the model generates clinically fluent but visually detached rationales, leading to high-confidence errors."[^c2]

The signature is a split between how good the reasoning looks and how often the answer is right. In the PET study, "CoT plausibility scores remain consistently high (0.85–0.99), yet diagnostic accuracy improvements are inconsistent."[^c3] For smaller medical models the six-step clinical prompt "either degrades performance or yields negligible gains."[^c4] The mechanism is stated as a condition on grounding: "when the visual grounding is weak (due to the perception gap), the CoT mechanism decouples from the image data."[^c5] The perception gap is [[functional-perception-gap]]; the trap is what the reasoning step does when that gap is present.

The paper's example is a clinical one. A model reads the patient's age and sex correctly, then reports a lung lesion "simply because lung cancer is a probable completion in its language model, not because it sees uptake in the image."[^c6] The authors' account of the mechanism is that, because the model lacks visual features to check its own intermediate steps, "the CoT process degenerates into an unconstrained text generation task."[^c7]

The trap is conditional, not a fixed property of chain-of-thought. The same paper reports that after perception-first fine-tuning on atomic tasks, the chain-of-thought prompt improves diagnostic accuracy "by up to 14.83%," and "CoT transitions from an unreliable intervention into a consistently beneficial reasoning mechanism."[^c8] That is the strongest evidence that the reasoning step inherits the quality of the perception under it.

The same attribution appears outside medicine, in a weaker form. A re-implementation of the two-stage Multimodal-CoT pipeline, run on OK-VQA, A-OKVQA and ChartQA, explains its OK-VQA errors as ambiguity: "many questions are ambiguous, causing CoT hallucinations."[^c13] Its account of weak grounding is the same kind of statement: "the model produces verbose but inaccurate" rationales.[^c14] The abstract goes further, claiming that "while vision integration significantly reduces hallucination in rationale generation" after "systematic ablation studies."[^c15][^c16] The text read gives no ablation table for that claim, so it is the authors' attribution, and the trap is not measured in that paper.

Why plausibility cannot catch it (my inference): a language-prior rationale is fluent by construction, so a fluency or coherence score cannot separate grounded from ungrounded reasoning. [[reasoning-masked-sycophancy]] reports a similar result in a different setting: step-by-step reasoning can be fluent and still rationalize a biased answer.

## Limits

- The formal condition P(r | x, q) ≈ P(r | q) is the paper's reading, not a measurement. No image ablation of the rationale is reported in the text read. The accuracy and plausibility numbers fit the reading; they do not establish it. [[counterfactual-image-grounding-audit]] is the kind of test that would, in another setting.
- Plausibility is not an expert judgment. It is scored by an auxiliary model: "CoT outputs are further scored by an auxiliary LLM-based evaluator."[^c9] Whether the evaluator's scores track clinicians was not reported in the text read, so "high plausibility" is a property of the judge's rating as much as of the rationale.
- The trap is shown for one six-step prompt on PET diagnosis. Other chain-of-thought formats, other domains and larger models are not established here; the paper's summary notes that some medical models gain little, and I did not read the per-model table in full.
- The text reports that the trap is "a failure mode where the generated reasoning chain maintains high linguistic plausibility yet diverges significantly from the underlying functional signals."[^c10] The divergence is inferred from accuracy and plausibility together, not measured against the signal directly.
- The reversal after perception-first training is one paper's result on one benchmark, and the gain is reported as an upper bound ("up to").
- A counter-case, not a refutation: on a chemistry olympiad benchmark with figures, CoT "consistently yields higher confidence than the baseline model" in log-probability, and its authors read the saliency maps as showing reliance spread across regions.[^c11][^c12] Confidence and saliency are not diagnostic accuracy against a clinical signal, and the text read does not show whether that benchmark also has a language-prior trap. The trap is conditional, and this is one setting where the condition seems not to bind.
- The Multimodal-CoT re-implementation does not separate the language-prior reading from ambiguity or from its weak ViT encoder, and it reports no rationale-level image ablation in the text read. Its hallucination reading is one more attribution, not a measurement of the trap (my reading).

## Related

- [[functional-perception-gap]] — the weak visual grounding that the trap is conditioned on
- [[reasoning-masked-sycophancy]] — fluent step-by-step reasoning cannot certify an answer, shown under sycophantic pressure
- [[pre-committed-answer-before-cot]] — the answer can be fixed before the chain is written, a related route to post-hoc reasoning
- [[cot-mediation-index]] — a causal test of whether the answer depends on the chain's tokens at all
- [[visual-robustness-score]] — rewards answers that resist a misleading text prior instead of matching it
- [[text-modality-dominance]] — heavier reliance on text over vision, measured by corruption

[^c1]: arxiv-2601-02737 — "is often dominated by the language prior"
[^c2]: arxiv-2601-02737 — "the model generates clinically fluent but visually detached rationales, leading to high-confidence errors"
[^c3]: arxiv-2601-02737 — "CoT plausibility scores remain consistently high (0.85–0.99), yet diagnostic accuracy improvements are inconsistent"
[^c4]: arxiv-2601-02737 — "CoT either degrades performance or yields negligible gains"
[^c5]: arxiv-2601-02737 — "when the visual grounding is weak (due to the perception gap), the CoT mechanism decouples from the image data"
[^c6]: arxiv-2601-02737 — "simply because lung cancer is a probable completion in its language model, not because it sees uptake in the image"
[^c7]: arxiv-2601-02737 — "the CoT process degenerates into an unconstrained text generation task"
[^c8]: arxiv-2601-02737 — "improving diagnostic accuracy by up to 14.83%"
[^c9]: arxiv-2601-02737 — "CoT outputs are further scored by an auxiliary LLM-based evaluator"
[^c10]: arxiv-2601-02737 — "a failure mode where the generated reasoning chain maintains high linguistic plausibility yet diverges significantly from the underlying functional signals"
[^c11]: arxiv-2512-14989 — "CoT consistently yields higher confidence than the baseline model, showing the benefit"
[^c12]: arxiv-2512-14989 — "higher performance with CoT does not result from simply sharpening attention but from fundamentally"
[^c13]: arxiv-2511-20701 — "many questions are ambiguous, causing CoT hallucinations"
[^c14]: arxiv-2511-20701 — "the model produces verbose but inaccurate"
[^c15]: arxiv-2511-20701 — "while vision integration significantly reduces hallucination in rationale generation"
[^c16]: arxiv-2511-20701 — "Through systematic ablation studies, we analyze the contributions of vision features"
