---
description: "A fine-tuned medical VLM at about 95% clean accuracy falls to roughly 25% under PGD perturbation of its image, so a clean accuracy score alone hides adversarial collapse."
aliases: ["clean-versus-robust accuracy gap", "adversarial accuracy collapse", "clean accuracy under attack"]
sources: ["arxiv-2512-19317", "doi-10-48550-arxiv-2603-11481"]
---
# Clean accuracy masks adversarial collapse

Accuracy on unperturbed inputs can sit near its ceiling while the same model's answers fail under a perturbation chosen against it. In the SafeMed-R1 study the perturbation is applied to the image of a medical visual question, and the attack is projected gradient descent (PGD), applied "primarily to the visual modality I".[^c1] The evaluation runs on OmniMedVQA "on the OmniMedVQA benchmark across eight medical imaging modalities", so the same questions are scored twice: once clean, once after the attack.[^c2]

The standard fine-tuned models are the case that makes the point. They score high on clean inputs, "our standard fine-tuned models achieve 95.43% (Instruct)" overall, and under PGD "fine-tuned models collapse under PGD attack: overall accuracy drops to roughly 25–26%".[^c3][^c4] Model, questions and answer options are unchanged; only the input differs. A clean score therefore reports how a model does when nothing is pushing its answer, and it says nothing about the answer under push. The paper's own summary is that high standard-benchmark scores "do not guarantee robustness".

The adversarially trained variant narrows the gap. The authors describe "a trade-off between clean accuracy and robustness": the trained models lose some clean accuracy, and the Think model goes from 91.47% clean to 84.45% under PGD, a drop the authors call "modest".[^c5][^c6] From those reported figures (my arithmetic), the clean-to-attacked gap is about 70 points for the standard model and about 7 points for the Think variant. The point of the number is the shape of the gap, not the size of either accuracy.

Why this matters for asking and answering: an evaluation that reports only clean accuracy measures one distribution of inputs and cannot tell a model that holds its answer under pressure from one that does not. Whether a score says anything about robustness depends on what was perturbed and how hard it was pushed (my inference, not a result of the paper).

A video benchmark measures the same gap with a conditional metric. INFACT's Base mode is clean accuracy; its Resist Rate scores only the items a model answered correctly on clean input, asking whether that correct answer survives a perturbation that should not change the label: "We measure reliability by whether a model preserves its correct Base prediction under each operator."[^c13] Its abstract states the consequence: "higher Base-mode accuracy does not reliably translate to higher reliability in the induced modes."[^c14] The perturbations there are visual degradation and misleading subtitles, not gradient attacks on the image, so the two papers measure different adversaries. What they share is the design point above: a clean score is not a stability score, and the stability figure has to be computed over the items that were right to begin with (my reading of the two definitions).

## Limits

- One attack family on one modality. "our evaluation is limited to PGD-based attacks on" the image, and the authors "did not exhaustively test other attack families, such as" optimization-based C&W attacks, text-only or multimodal attacks, or adaptive attacks on the reasoning process itself.[^c7][^c8]
- The perturbation is adversarial, not acquisition noise. The introduction names "arising from variations in imaging acquisition" as a source of similar perturbations, but the study does not measure non-adversarial variation, so whether the collapse pattern appears there is untested.[^c9]
- The certified half is not reported. The framework pairs training with randomized smoothing for certified L2 robustness, but the paper says the certified evaluation "remains computationally expensive for large VLMs" and that scaling it is still open.[^c10] No certified accuracy is shown; the collapse and recovery numbers are empirical only.
- The reasoning claim is thin. "Adv FT–Think outperforms Adv FT–Instruct (84.45% vs. 82.27%)" is a two-point gap from one run, with no interval in the sections read; the reading that reasoning "contributes positively to robustness" is the authors'.[^c11]
- One backbone and one size: the models are "our fine-tuned Qwen3-VL-4B models", so the figures are for a 4B model on one benchmark.[^c12]

## Related

- [[visual-robustness-score]] — there the perturbation is a textual prior or misleading premise that pulls answers toward a trap; here it is an input-space perturbation with no semantic content. Both show that one accuracy number can hide which way an answer moved.
- [[accuracy-masks-unstable-reasoning]] — accuracy hides differences in internal route stability; this note is the external-perturbation case of the same averaging problem.
- [[inference-time-input-noise-injection]] — random noise at inference, averaged over draws; adversarial training here uses worst-case rather than random perturbations.
- [[llm-red-teaming]] — the wider practice of probing a model from outside with adversarial inputs.

[^c1]: arxiv-2512-19317 — "applied primarily to the visual modality I"
[^c2]: arxiv-2512-19317 — "on the OmniMedVQA benchmark across eight medical imaging modalities"
[^c3]: arxiv-2512-19317 — "our standard fine-tuned models achieve 95.43% (Instruct)"
[^c4]: arxiv-2512-19317 — "fine-tuned models collapse under PGD attack: overall accuracy drops to roughly 25–26%"
[^c5]: arxiv-2512-19317 — "consistent with prior work on adversarial training, we see a trade-off between clean"
[^c6]: arxiv-2512-19317 — "clean accuracies (e.g., 91.47% → 84.45% for Adv FT–Think) is modest"
[^c7]: arxiv-2512-19317 — "our evaluation is limited to PGD-based attacks on"
[^c8]: arxiv-2512-19317 — "we did not exhaustively test other attack families, such as"
[^c9]: arxiv-2512-19317 — "arising from variations in imaging acquisition"
[^c10]: arxiv-2512-19317 — "remains computationally expensive for large VLMs"
[^c11]: arxiv-2512-19317 — "Adv FT–Think outperforms Adv FT–Instruct (84.45% vs. 82.27%)"
[^c12]: arxiv-2512-19317 — "our fine-tuned Qwen3-VL-4B models"
[^c13]: doi-10-48550-arxiv-2603-11481 — "We measure reliability by whether a model preserves its correct Base prediction under each operator."
[^c14]: doi-10-48550-arxiv-2603-11481 — "higher Base-mode accuracy does not reliably translate to higher reliability in the induced modes"
