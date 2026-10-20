---
description: "When a vision-language model answers wrongly, it leans toward the more positive option more often than chance; excess positivity drift measures that lean among distractors."
aliases: ["positivity heuristic", "excess positivity drift", "social desirability bias in answer choice", "positivity bias in multiple choice"]
sources: ["arxiv-2512-17394"]
---
# Positivity drift in answer choices

A multiple-choice benchmark can be partly solved by a rule that never reads the question: choose the option that sounds most positive. The cultural theory-of-mind benchmark of Al Nazi and colleagues implements this rule as a sentiment-based "Positivity Heuristic" classifier that selects the most semantically positive option.[^p1] On their data the rule is not chance. It reaches "accuracies between 45% (FindingEmo) and 56%" depending on the image source.[^p2] The authors trace part of this to their own annotation: excluding "of culturally offensive or stereotypical content during annotation, which naturally skews the ground truth toward socially constructive interactions."[^p3] So part of the heuristic's score is a property of the gold labels, not of any model.

The model-side quantity is conditional on error. The question is not whether a model picks the positive option, but whether it picks it more often when it is wrong. The paper's words are that "they are more likely than chance to select" an option more positive than the correct answer, and it names the measure Excess Positivity Drift.[^p4] For Qwen2.5-VL on CulturalVQA, "this drift is substantial (0.111, p < 0.05)", which the authors translate as an 11 percentage-point increase over chance among distractors.[^p5] The tilt grows in conflict cases, where the correct answer is not the most positive option. There "the model selects the most positive distractor 22" percentage points more often than random choice would.[^p6]

The tilt is also visible without the image. In the appendix's qualitative examples, with no visual input, models "often default to socially favorable" readings, such as happiness or comfort, in ambiguous scenes instead of abstaining.[^p7] The authors name the cause as a positivity heuristic "reflecting safety alignment and socially normative priors", which is a hypothesis about training, not something their experiments isolate.[^p8]

The accounting of accuracy is coarse. The authors state that "social desirability bias explains a substantial portion of the performance" and give a share of about 56%.[^p9] The remainder, which is what lifts frontier models to high accuracy, is attributed to models "enabling them to infer plausible social contexts from" text and pretrained knowledge.[^p10] That attribution is reached by elimination: a TF-IDF plus logistic regression baseline scored near chance, "confirming that the high accuracy of frontier models is not driven by" lexical patterns.[^p11]

What this changes for asking and answering, in my reading and not in the paper's words: a benchmark's accuracy means little next to the positivity baseline, because a model can match the gold labels by tilt alone. The direction of a wrong answer is also information. If errors lean toward the positive option, they may come from the tilt rather than from the evidence, and a question writer who skews options positive gives that tilt a free ride.

## Limits

- One benchmark (CulturalToM-VQA) and one heuristic classifier. The main text does not say which sentiment model implements the heuristic; the appendix that may say was not read here.
- The drift figure quoted in the main text is for one model on one image source (Qwen2.5-VL on CulturalVQA). Drift values for the other models were not in the parts read.
- The chance baseline is random choice among distractors. Whether it controls for the dataset's own positive skew among distractors is not stated in the main text.
- The safety-alignment account is a hypothesis ("likely reflecting"); no comparison with an unaligned model is reported.
- The 56% share of accuracy is not derived in the main text, and the rest is attributed to world knowledge by elimination, which is the authors' conclusion, not a measured decomposition.
- Not tested: whether the tilt survives rewording the options, removing the options, or asking open-ended. Only option-level diagnostics on the best models were run.

## Related

- [[option-matching-shortcut]] — option-level artefacts when the choices are on the page
- [[answer-format-dependent-bias-measurement]] — the same kind of option artefact, measured across answer formats
- [[counterfactual-image-grounding-audit]] — the image-removal test that exposes the no-image side of this tilt
- [[clever-hans-effect]] — a cue that correlates with the label and is used in place of the evidence

[^p1]: arxiv-2512-17394 — "classifier that selects the most semantically positive"
[^p2]: arxiv-2512-17394 — "accuracies between 45% (FindingEmo) and 56%"
[^p3]: arxiv-2512-17394 — "of culturally offensive or stereotypical content during annotation, which naturally skews the ground"
[^p4]: arxiv-2512-17394 — "they are more likely than chance to select"
[^p5]: arxiv-2512-17394 — "this drift is substantial (0.111, p < 0.05)"
[^p6]: arxiv-2512-17394 — "the model selects the most positive distractor 22"
[^p7]: arxiv-2512-17394 — "models often default to socially favorable"
[^p8]: arxiv-2512-17394 — "reflecting safety alignment and socially normative priors"
[^p9]: arxiv-2512-17394 — "social desirability bias explains a substantial portion of the performance"
[^p10]: arxiv-2512-17394 — "enabling them to infer plausible social contexts from"
[^p11]: arxiv-2512-17394 — "confirming that the high accuracy of frontier models is not driven by"
