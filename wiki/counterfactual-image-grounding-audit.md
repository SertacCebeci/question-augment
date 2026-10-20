---
description: "Replacing the image with a blank or a mismatched one separates accuracy from visual dependence; accuracy-only RL can raise scores while answers stop depending on the image."
aliases: ["Visual Reliance Score", "Image Sensitivity", "Hallucinated Visual Reasoning Rate", "HVRR", "blank and shuffled image ablation", "blinding test"]
sources: ["arxiv-2603-03437", "arxiv-2512-19683", "arxiv-2512-17319", "arxiv-2512-17394", "arxiv-2512-17953", "arxiv-2512-14989", "arxiv-2511-19220"]
---
# Counterfactual image grounding audit

**What it is.** To test whether a vision-language model's answer depends on the image, each example is evaluated three times: real image, a uniform gray image, and an image drawn from another example of the same benchmark. Accuracy under the three conditions defines the metrics.[^c1] Visual Reliance Score (VRS) is accuracy(real) minus accuracy(shuffled); negative means the model does better with wrong images. Blank Drop is accuracy(real) minus accuracy(blank). Image Sensitivity (IS) is the share of examples whose answer changes when the image is shuffled, whether or not the answer becomes correct.[^c2]

**Hallucinated Visual Reasoning Rate.** In a model's written rationale, a statement counts as a novel visual claim if it uses observation language ("shows", "left", "spiculated") and adds information not in the question. HVRR is P(visual claim and the answer is the same under real and shuffled images).[^c3] It flags rationales that describe the image while the answer ignores it.

**Why accuracy alone misleads.** Three Qwen2.5-VL-7B variants (baseline, RL on text-only medical QA, RL on image-text QA) were run on 100 sampled items from each of PathVQA, PMC-VQA, SLAKE and VQA-RAD. Image-text RL had the highest accuracy (58.8% against 56.5%) but the lowest IS (39.8% against 48.2%).[^c4] On PMC-VQA, accuracy rose from 50% to 57% while VRS fell from 0.25 to 0.13.[^c5] On VQA-RAD both RL variants reached 63%, but the text-only one kept 51% accuracy with a blank image, 81% of its real-image performance, while the image-text one had IS of 29%.[^c6] Same score, different mechanism: one answers from text, the other has answers that mostly ignore the image.

**Two metrics can disagree.** On VQA-RAD, VRS rose from 0.09 to 0.17 while IS fell from 43% to 29%. The authors explain that VRS is accuracy-based and can improve through text patterns that happen to correlate with correctness when images match, whereas IS tracks answer-level change.[^c7] Hence an accuracy-difference metric alone cannot certify grounding; an answer-invariance metric is needed too (the authors' conclusion, one explanation among possible ones).

**Rationales decouple from answers.** Models produced visual claims in 68-74% of responses, and 38-43% of responses were ungrounded in the HVRR sense. Image-text RL had the highest conditional probability of an invariant answer given a visual claim, 60.9%.[^c8] In the paper's example, a text-trained model notices in its reasoning that the image is a chest X-ray, not an abdominal CT, then still asserts the liver looks normal.

**Benchmark diagnosis.** Blank-image accuracy of 48-52% on PathVQA and VRS near zero or negative show that even an image-critical benchmark has text-answerable questions.[^c9]

**Text-only parity as a benchmark-level reading.** The blind condition can also be run with a language model that has no visual input at all. On RSHR-Bench the authors compare text-only models with multimodal ones, "text-only (Llama3-8B and Qwen3-8B) and multimodal (image+text; GPT-4o and GPT-4o mini)", and report a wider gap than on XLRS-Bench: "exhibits a larger gap between text-only and multimodal settings," which they read as "indicating stronger reliance on visual information."[^c14][^c15] This compares different models, so it is a benchmark diagnostic, not a per-model grounding test. The item-side version of the same probe is [[text-answerability]].

**Blinding test on spatial questions.** The same removal, applied to metric and relational questions about street and indoor scenes, gives a small gain from vision. The authors remove the visual input and keep the textual question. For most models, "most models exhibit only a marginal improvement" in accuracy when vision is enabled (+2.2 to +6.3 points, by their table).[^c11] For human annotators the same condition gives a much larger gain, "substantially (+22.6) when vision is available."[^c13] The authors read the small model gain as reliance on textual priors: "MLLMs often rely on textual priors rather than truly grounded visual understanding."[^c12] Their test is a blind-image accuracy difference, not a log-probability or answer-invariance measure, so it sits closer to the Blank Drop above than to IS. The benchmark is open-world spatial reasoning, not medical VQA, and the blind condition there is the removal of the image alone.

**Blind condition on cultural theory-of-mind questions.** The same removal, applied to visually situated theory-of-mind questions, shows a generational split. The older Qwen-VL-Chat falls to "near-random performance without visual context" (about 39%), while "Qwen2-VL and Qwen2.5-VL maintain high accuracy" without the image.[^c16] The authors read this as frontier models shortcutting the image: "models can effectively shortcut visual reasoning", using parametric social priors.[^c17] A lexical control is run first, a TF-IDF plus logistic regression baseline near chance, "confirming that the high accuracy of frontier models is not driven by" surface patterns.[^c18] The test is accuracy only: no visual reliance score or answer-invariance measure is reported for the blind condition, so it cannot be placed on the VRS or IS axes above. The tilt of the wrong answers under this blind condition is a separate measure, taken up in [[positivity-drift-in-answer-choices]].[^c19]

**Mismatched-scene swap in video.** The same counterfactual logic is applied where the mismatch is the scene rather than the image. The HAT Action Swap set is built from videos "where the human from class A is placed on a mismatched background of class B", so an answer that follows the scene lands on a label the test can name.[^c20] The readout is which of two labels an answer falls on, not one accuracy difference: "a high SBErr shows reliance on background".[^c21] Accuracy on the ordinary benchmark cannot settle the question alone, because the same scene is evidence there; the two-sided reading is the subject of [[dual-use-context-cue]].

**Image removal on olympiad chemistry.** In a multiple-choice chemistry benchmark of 473 figure-bearing questions, the authors ablate question text, answer choices and the image, on five models of different capacity.[^c22] Removing the image sometimes helps: "image even improves accuracy, indicating misalignment in vision-language integration."[^c23] The drop from removing the image is larger on the national exam set, which the authors describe as more visually intensive: "removing the image modality causes a larger performance" drop there.[^c24] A negative blank drop is thus not only a benchmark artifact; it can be a model's visual input "may introduce spurious cues."[^c25] Accuracy is a single-model, single-benchmark reading, not a per-item grounding measure.

**Four frontier models on Italian clinical images.** On 60 Italian State Exam questions that need the picture, each model was run with its real image and with the image swapped for a blank: "We replaced each medical image with an identical blank placeholder while keeping question text and answer options unchanged."[^c26] Over 10 repetitions per model, the blank drop ran from 2.4 points for Gemini 2.0 to 27.9 for GPT-4o, with 8.5 for GPT-5-mini and 5.6 for Claude Sonnet 4.5; the authors read the smallest drop as "suggesting strong reliance on textual cues".[^c27] The same blank condition produced confident invented findings: "multiple models confidently described fabricated ECG findings" despite the blank being diagnostically empty.[^c28] The authors' qualitative reading, from examples and not a count, is that models "appeared to select answers first (possibly from textual cues)" and then justified the answer visually.[^c29] This is the same accuracy-versus-rationale split as above, now on one clinical benchmark.

## Limits

- Only n = 100 per benchmark and one 7B model family; point estimates dominate. On PathVQA no VRS confidence interval excluded zero, including the −0.09 headline figure ([-0.21, 0.05]).[^c10]
- Many differences (e.g. IS 39.8% vs 48.2%) are not accompanied here by tests; I treat them as suggestive.
- A shuffled image from the same benchmark can still be semantically plausible, so IS conflates image use with noise sensitivity (my inference).
- The visual-claim detector is keyword-based; the manual audit covered only 50 high-risk cases per model.
- The causal explanation (shortcut exploitation caused by accuracy-only rewards) is a hypothesis; no reward-ablation was run.
- Medical VQA only.
- A blank drop can be refusal rather than lost visual use. GPT-4o fell below the human average without images because "it refuses to answer the question", so its 27.9-point drop cannot be read as reliance on the picture alone.[^c30] The Italian study uses one blank condition on 60 items, and its authors call it "a coarse test of visual dependency"; they did not run membership inference, so "High accuracy without images may reflect robust textual reasoning or dataset memorization" stays open.[^c31][^c32]

## Related

- [[text-modality-dominance]] — models leaning on text over the image is the behaviour this audit measures
- [[evidence-gain-hallucination-score]] — a log-probability version of the same image-removal contrast
- [[visual-evidence-scoring]] — scoring how far visual evidence supports an answer
- [[calibration]] — a stated visual justification is not a reliable signal of what drove the answer
- [[structured-benchmark-gain-transfer]] — the same blinding idea on an open-world spatial benchmark, where indoor gains do not carry over
- [[positivity-drift-in-answer-choices]] — the tilt of wrong answers toward the positive option, which the blind condition on theory-of-mind questions also exposes
- [[occlusion-logprob-saliency]] — the localized version: which region of the image an answer leans on, rather than whether it leans on the image at all
- [[unnecessary-abstention-aware-recall]] — a refusal scored as a miss is the same accounting problem as a blank-image drop (my inference)

[^c1]: arxiv-2603-03437 — "Blank: (xtext , Blank) – question with uniform gray image (224×224, RGB [128,128,128])"
[^c2]: arxiv-2603-03437 — "measures how often the model changes its answer when"
[^c3]: arxiv-2603-03437 — "HVRR = P [NVC = 1 ∧ areal = ashuffle ]"
[^c4]: arxiv-2603-03437 — "image-text RLVR reduces image sensitivity to 39.8% overall despite improving"
[^c5]: arxiv-2603-03437 — "VRS decreases from 0.25 to"
[^c6]: arxiv-2603-03437 — "RL(text) maintains 51% accuracy with blank images, 81% of its real-image performance"
[^c7]: arxiv-2603-03437 — "This divergence occurs because VRS measures accuracy differences which can improve through better text-based pattern matching"
[^c8]: arxiv-2603-03437 — "RL(image) shows the highest conditional probability"
[^c9]: arxiv-2603-03437 — "confirming"
[^c10]: arxiv-2603-03437 — "no model shows statistically significant VRS at α = 0.05 level"
[^c11]: arxiv-2512-19683 — "most models exhibit only a marginal improvement"
[^c12]: arxiv-2512-19683 — "MLLMs often rely on textual priors rather than truly grounded visual understanding"
[^c13]: arxiv-2512-19683 — "substantially (+22.6) when vision is available"
[^c14]: arxiv-2512-17319 — "exhibits a larger gap between text-only and multimodal settings"
[^c15]: arxiv-2512-17319 — "text-only (Llama3-8B and Qwen3-8B) and multimodal (image+text; GPT-4o and GPT-4o mini)"
[^c16]: arxiv-2512-17394 — "near-random performance without visual context"
[^c17]: arxiv-2512-17394 — "models can effectively shortcut visual reasoning"
[^c18]: arxiv-2512-17394 — "confirming that the high accuracy of frontier models is not driven by"
[^c19]: arxiv-2512-17394 — "social desirability bias explains a substantial portion of the performance"
[^c20]: arxiv-2512-17953 — "where the human from class A is placed on a mismatched background of class B"
[^c21]: arxiv-2512-17953 — "a high SBErr shows reliance on background"
[^c22]: arxiv-2512-14989 — "systematically removing question text, answer choices, or image inputs"
[^c23]: arxiv-2512-14989 — "image even improves accuracy, indicating misalignment in vision-language integration."
[^c24]: arxiv-2512-14989 — "removing the image modality causes a larger performance"
[^c25]: arxiv-2512-14989 — "may introduce spurious cues."
[^c26]: arxiv-2511-19220 — "We replaced each medical image with an identical blank placeholder"
[^c27]: arxiv-2511-19220 — "suggesting strong reliance on textual cues"
[^c28]: arxiv-2511-19220 — "multiple models confidently described fabricated ECG findings"
[^c29]: arxiv-2511-19220 — "appeared to select answers first (possibly from textual cues)"
[^c30]: arxiv-2511-19220 — "it refuses to answer the question"
[^c31]: arxiv-2511-19220 — "our blank image substitution represents a coarse test of visual dependency"
[^c32]: arxiv-2511-19220 — "High accuracy without images may reflect robust textual reasoning or dataset memorization"
