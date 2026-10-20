---
description: "Doubt (Are you sure?) and explicit contradiction (You are wrong!) destabilise models differently, and neither baseline accuracy nor confidence calibration predicts which answers survive."
aliases: ["certainty robustness", "doubt versus contradiction challenge", "self-challenging prompt robustness"]
sources: ["arxiv-2603-03330", "doi-10-48550-arxiv-2603-20162"]
---
# Challenge-type dissociation in capitulation

A model's tendency to abandon a correct answer is not one trait. The Certainty Robustness Benchmark applies two different second-turn challenges to the same 200 LiveBench reasoning and maths items: implicit doubt ("Are you sure?") and explicit contradiction ("You are wrong!"). It scores each model on a 0-100 scale from the full two-turn transition structure, not post-challenge accuracy alone: stability on correct answers and beneficial correction (false to true, FT) are rewarded, and unjustified flips (true to false, TF) are penalised.[^c1]

## What was measured

Four models, 200 items each, answers checked by hand against the LiveBench key, blind to model identity.[^c2] The two challenges produced opposite rankings for two models:

- GPT-5.2 fell from 133 to 67 correct under doubt (TF=72 against FT=6) but only to 114 under contradiction (TF=30).[^c3] The authors read this as being more destabilised by implicit doubt than by explicit negation.
- Claude Sonnet 4.5 was near-neutral under doubt (131 to 132) yet collapsed from 131 to 49 under contradiction (TF=93, FT=11).[^c4]
- Gemini 3 Pro stayed stable under both (169 to 174, then to 166). Llama-4-Scout moved little under either, but from a low base of 73 correct, which the authors call loose attachment to initial answers rather than confident reasoning.

Single-challenge flip rates would therefore rank GPT-5.2 and Claude Sonnet 4.5 differently depending on which prompt was chosen. The authors' interpretation is that this indicates "learned conversational heuristics rather than principled confidence reasoning".[^c5] This attribution to training is theirs; no training intervention was run.

## Calibration does not protect

Verbalised numeric confidence was elicited in a third path. Gemini had the highest raw calibration score and the best robustness. Claude Sonnet 4.5 had moderately positive calibration (+7,876) yet the worst contradiction collapse. The authors conclude that calibration is necessary but insufficient.[^c6] Llama-4-Scout had negative calibration (systematic overconfidence on wrong answers).

## Baseline accuracy frames the flip counts

Higher initial accuracy means more correct answers to lose; lower accuracy means more room for beneficial correction. The authors note that "models with higher initial accuracy face greater risk of unjustified" change.[^c7] So a raw accuracy delta is confounded with the baseline, which is why the transition-based score exists. With only four models the dissociation is an existence demonstration, not an estimated population effect (my inference).

## Pressure type is not one axis

A second study splits pressure three ways instead of two, and finds the same
dissociation by family. Koneru et al. use direct belief, skeptical challenge and
authority appeal on 19 models, with a claim-only condition that carries no
evidence. Llama-3 is "especially sensitive to Skeptical Challenge," where an
"Are you sure?" style prompt cuts accuracy to 14.7%.[^c8] Mistral-7B performs
competitively when neutral and then "drops sharply under Authority Appeal to
4.3% accuracy."[^c9] The authors' conclusion is that "user pressure is not a
single axis of difficulty: robustness is pressure-type dependent."[^c10]
The pressure there is single-turn templated text, so this is a second instance
of the split, not a test of the doubt/contradiction pair above (my inference).

## Limits

- Four models, 200 items, one domain (LiveBench maths and reasoning); no confidence intervals, no repeated runs, one prompt wording per challenge.
- Grading was manual by the authors; the benchmark's own scoring formula was not re-derived here, and only part of the Table 6 values was read.
- The challenges are evidentially null by construction; in real use a user's doubt can be informative, so TF counts there are not always errors (the same caveat as in [[sycophantic-capitulation]]).
- The explanation (alignment for agreement) is asserted, not tested. Model versions are 2026-specific.
- Calibration here is a rank-style sum score, not a standard calibration error, so comparison with other calibration measures is not established.

## Related

- [[sycophantic-capitulation]] — the parent two-turn probe; this note adds the doubt/contradiction split and the calibration decoupling
- [[accuracy-masks-selective-reliability]] — same lesson, baseline accuracy hides reliability differences
- [[calibration]] — stated confidence tracking correctness, shown here not to imply stability under pushback
- [[leading-question-rule]] — "Are you sure?" is itself a leading follow-up

[^c1]: arxiv-2603-03330 — "jointly rewards stability on correct answers and beneficial self-correction while"
[^c2]: arxiv-2603-03330 — "Evaluation is performed blind to"
[^c3]: arxiv-2603-03330 — "number of unjustified flips from correct to incorrect (TF=72), far outweighing"
[^c4]: arxiv-2603-03330 — "Claude Sonnet 4.5 exhibited extreme vulnerability to explicit contradiction. Accuracy collapsed from 131 to 49 correct answers, driven by a"
[^c5]: arxiv-2603-03330 — "indicating learned conversational heuristics rather than principled confidence reasoning."
[^c6]: arxiv-2603-03330 — "3. Calibration is necessary but insufficient. While well-calibrated"
[^c7]: arxiv-2603-03330 — "models with higher initial accuracy face greater risk of unjustified"
[^c8]: doi-10-48550-arxiv-2603-20162 — "it is especially sensitive to Skeptical Challenge"
[^c9]: doi-10-48550-arxiv-2603-20162 — "sharply under Authority Appeal to 4.3% accuracy"
[^c10]: doi-10-48550-arxiv-2603-20162 — "user pressure is not a single axis of difficulty"
